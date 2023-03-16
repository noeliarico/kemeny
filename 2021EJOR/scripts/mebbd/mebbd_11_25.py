
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,13,6,9,10,8,15,14,8,11,8],
[12,0,8,10,7,7,11,14,10,10,11],
[19,17,0,15,13,13,15,13,8,16,11],
[16,15,10,0,14,8,12,14,13,10,11],
[15,18,12,11,0,13,15,16,13,14,12],
[17,18,12,17,12,0,17,17,16,16,10],
[10,14,10,13,10,8,0,10,12,13,14],
[11,11,12,11,9,8,15,0,10,9,11],
[17,15,17,12,12,9,13,15,0,15,8],
[14,15,9,15,11,9,12,16,10,0,10],
[17,14,14,14,13,15,11,14,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,8,10,6,6,10,6,0,13],
[14,0,9,9,10,15,6,10,6,10,10],
[14,16,0,19,4,13,10,10,0,4,16],
[17,16,6,0,10,16,16,16,6,7,13],
[15,15,21,15,0,15,11,14,12,15,21],
[19,10,12,9,10,0,15,5,7,4,15],
[19,19,15,9,14,10,0,14,4,4,21],
[15,15,15,9,11,20,11,0,11,15,21],
[19,19,25,19,13,18,21,14,0,9,21],
[25,15,21,18,10,21,21,10,16,0,25],
[12,15,9,12,4,10,4,4,4,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,17,14,7,11,14,12,15,12],
[8,0,11,11,7,6,8,9,9,9,7],
[11,14,0,13,11,6,9,10,11,15,12],
[8,14,12,0,10,9,9,13,12,13,11],
[11,18,14,15,0,13,10,14,13,17,15],
[18,19,19,16,12,0,12,15,11,19,14],
[14,17,16,16,15,13,0,13,11,17,14],
[11,16,15,12,11,10,12,0,10,15,14],
[13,16,14,13,12,14,14,15,0,17,12],
[10,16,10,12,8,6,8,10,8,0,9],
[13,18,13,14,10,11,11,11,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,8,9,18,8,11,19,12,15,11],
[7,0,13,13,15,13,15,18,9,15,8],
[17,12,0,9,12,14,5,19,12,15,11],
[16,12,16,0,15,16,3,19,10,16,16],
[7,10,13,10,0,7,1,10,6,9,4],
[17,12,11,9,18,0,11,19,18,15,17],
[14,10,20,22,24,14,0,25,19,16,17],
[6,7,6,6,15,6,0,0,2,8,8],
[13,16,13,15,19,7,6,23,0,22,14],
[10,10,10,9,16,10,9,17,3,0,11],
[14,17,14,9,21,8,8,17,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,16,11,10,9,9,8,9,8,11],
[18,0,16,15,13,15,11,16,8,15,16],
[9,9,0,14,10,8,7,10,11,11,7],
[14,10,11,0,9,12,10,12,9,12,8],
[15,12,15,16,0,13,10,16,14,14,11],
[16,10,17,13,12,0,7,11,10,9,14],
[16,14,18,15,15,18,0,12,13,11,18],
[17,9,15,13,9,14,13,0,10,13,13],
[16,17,14,16,11,15,12,15,0,15,17],
[17,10,14,13,11,16,14,12,10,0,16],
[14,9,18,17,14,11,7,12,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,15,13,8,15,13,12,9,15],
[12,0,12,15,16,13,13,12,12,11,14],
[14,13,0,12,15,12,13,8,12,8,11],
[10,10,13,0,14,14,9,15,12,9,16],
[12,9,10,11,0,8,14,11,9,11,14],
[17,12,13,11,17,0,14,15,16,12,13],
[10,12,12,16,11,11,0,14,13,9,16],
[12,13,17,10,14,10,11,0,10,14,15],
[13,13,13,13,16,9,12,15,0,14,16],
[16,14,17,16,14,13,16,11,11,0,17],
[10,11,14,9,11,12,9,10,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,13,15,14,14,13,16,15,12],
[12,0,10,15,12,16,12,12,15,15,12],
[17,15,0,14,18,15,16,12,17,17,12],
[12,10,11,0,13,17,10,14,15,12,14],
[10,13,7,12,0,10,13,10,16,8,7],
[11,9,10,8,15,0,11,13,14,10,11],
[11,13,9,15,12,14,0,10,17,11,9],
[12,13,13,11,15,12,15,0,11,15,11],
[9,10,8,10,9,11,8,14,0,9,10],
[10,10,8,13,17,15,14,10,16,0,12],
[13,13,13,11,18,14,16,14,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,9,9,9,9,19,15,9,9],
[16,0,16,16,25,10,6,16,6,0,16],
[10,9,0,10,19,0,9,19,6,9,9],
[16,9,15,0,15,9,9,25,6,9,15],
[16,0,6,10,0,0,0,10,6,0,0],
[16,15,25,16,25,0,15,25,6,15,25],
[16,19,16,16,25,10,0,16,16,10,16],
[6,9,6,0,15,0,9,0,6,9,15],
[10,19,19,19,19,19,9,19,0,9,19],
[16,25,16,16,25,10,15,16,16,0,16],
[16,9,16,10,25,0,9,10,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,18,14,9,10,15,17,4,16],
[15,0,20,22,8,7,10,15,22,9,10],
[10,5,0,17,6,2,6,14,20,7,5],
[7,3,8,0,8,8,13,11,20,7,10],
[11,17,19,17,0,6,13,15,25,14,13],
[16,18,23,17,19,0,18,16,24,9,9],
[15,15,19,12,12,7,0,15,19,11,16],
[10,10,11,14,10,9,10,0,25,9,16],
[8,3,5,5,0,1,6,0,0,0,9],
[21,16,18,18,11,16,14,16,25,0,16],
[9,15,20,15,12,16,9,9,16,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,14,16,14,14,14,6,15,8,14],
[19,0,14,10,25,17,14,9,23,8,8],
[11,11,0,2,17,9,9,9,9,9,0],
[9,15,23,0,23,17,15,9,15,17,14],
[11,0,8,2,0,17,0,9,9,8,8],
[11,8,16,8,8,0,8,2,17,2,8],
[11,11,16,10,25,17,0,11,15,17,8],
[19,16,16,16,16,23,14,0,23,8,14],
[10,2,16,10,16,8,10,2,0,8,10],
[17,17,16,8,17,23,8,17,17,0,8],
[11,17,25,11,17,17,17,11,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,5,14,14,10,13,10,7],
[14,0,12,9,9,8,17,12,13,12,8],
[12,13,0,13,12,13,11,11,12,16,12],
[15,16,12,0,13,13,18,16,11,13,6],
[20,16,13,12,0,18,16,15,17,18,18],
[11,17,12,12,7,0,15,16,14,20,9],
[11,8,14,7,9,10,0,14,9,11,8],
[15,13,14,9,10,9,11,0,13,16,5],
[12,12,13,14,8,11,16,12,0,14,8],
[15,13,9,12,7,5,14,9,11,0,8],
[18,17,13,19,7,16,17,20,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,11,15,13,14,14,18,10,12],
[14,0,18,8,13,14,18,10,17,9,13],
[12,7,0,11,10,13,13,8,14,7,9],
[14,17,14,0,13,14,12,14,16,15,14],
[10,12,15,12,0,11,13,16,17,12,16],
[12,11,12,11,14,0,17,11,16,16,14],
[11,7,12,13,12,8,0,10,15,11,11],
[11,15,17,11,9,14,15,0,13,10,10],
[7,8,11,9,8,9,10,12,0,5,8],
[15,16,18,10,13,9,14,15,20,0,16],
[13,12,16,11,9,11,14,15,17,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,15,13,14,16,17,13,11,11],
[14,0,16,16,14,14,16,19,14,12,12],
[9,9,0,8,10,12,9,13,10,9,6],
[10,9,17,0,12,11,13,17,12,12,8],
[12,11,15,13,0,11,14,16,12,13,9],
[11,11,13,14,14,0,14,16,13,11,10],
[9,9,16,12,11,11,0,15,12,10,8],
[8,6,12,8,9,9,10,0,11,7,6],
[12,11,15,13,13,12,13,14,0,11,13],
[14,13,16,13,12,14,15,18,14,0,11],
[14,13,19,17,16,15,17,19,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,9,15,12,8,12,15,10,14],
[14,0,10,9,11,4,6,11,11,14,12],
[11,15,0,8,18,15,15,15,16,16,15],
[16,16,17,0,19,13,12,13,16,19,20],
[10,14,7,6,0,4,5,6,15,15,15],
[13,21,10,12,21,0,11,12,17,21,15],
[17,19,10,13,20,14,0,14,16,16,19],
[13,14,10,12,19,13,11,0,18,13,22],
[10,14,9,9,10,8,9,7,0,16,10],
[15,11,9,6,10,4,9,12,9,0,11],
[11,13,10,5,10,10,6,3,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,15,16,16,12,9,14,13,9],
[9,0,13,9,9,14,12,8,8,11,5],
[13,12,0,8,15,14,12,7,10,9,9],
[10,16,17,0,15,16,13,11,12,10,14],
[9,16,10,10,0,14,13,8,9,10,9],
[9,11,11,9,11,0,10,10,9,12,6],
[13,13,13,12,12,15,0,14,8,10,5],
[16,17,18,14,17,15,11,0,14,12,9],
[11,17,15,13,16,16,17,11,0,10,9],
[12,14,16,15,15,13,15,13,15,0,9],
[16,20,16,11,16,19,20,16,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,12,17,10,15,15,9,13,15],
[12,0,13,15,18,12,14,16,11,13,15],
[11,12,0,12,14,9,14,10,8,10,13],
[13,10,13,0,18,11,14,13,13,15,14],
[8,7,11,7,0,6,12,10,7,8,8],
[15,13,16,14,19,0,14,14,12,14,16],
[10,11,11,11,13,11,0,9,10,9,11],
[10,9,15,12,15,11,16,0,12,14,12],
[16,14,17,12,18,13,15,13,0,16,16],
[12,12,15,10,17,11,16,11,9,0,11],
[10,10,12,11,17,9,14,13,9,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,14,11,10,16,16,13,15,10],
[11,0,14,13,12,11,14,12,11,10,13],
[11,11,0,11,8,8,12,11,10,10,10],
[11,12,14,0,13,13,15,13,13,15,16],
[14,13,17,12,0,15,15,20,12,13,13],
[15,14,17,12,10,0,13,13,15,14,11],
[9,11,13,10,10,12,0,10,14,13,15],
[9,13,14,12,5,12,15,0,9,12,13],
[12,14,15,12,13,10,11,16,0,14,11],
[10,15,15,10,12,11,12,13,11,0,13],
[15,12,15,9,12,14,10,12,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,16,12,12,10,13,13,12,11],
[15,0,14,15,15,14,12,12,11,13,8],
[12,11,0,14,12,13,12,12,13,14,13],
[9,10,11,0,12,12,9,8,12,11,9],
[13,10,13,13,0,10,9,12,13,13,9],
[13,11,12,13,15,0,14,15,13,15,10],
[15,13,13,16,16,11,0,11,11,16,9],
[12,13,13,17,13,10,14,0,11,13,9],
[12,14,12,13,12,12,14,14,0,11,10],
[13,12,11,14,12,10,9,12,14,0,10],
[14,17,12,16,16,15,16,16,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,14,11,15,12,16,14,17,14],
[12,0,14,12,11,12,11,15,12,12,11],
[11,11,0,13,15,13,11,15,11,14,13],
[11,13,12,0,11,16,12,16,15,15,12],
[14,14,10,14,0,16,14,16,15,16,15],
[10,13,12,9,9,0,10,13,10,12,10],
[13,14,14,13,11,15,0,16,12,14,10],
[9,10,10,9,9,12,9,0,11,11,8],
[11,13,14,10,10,15,13,14,0,14,12],
[8,13,11,10,9,13,11,14,11,0,8],
[11,14,12,13,10,15,15,17,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,17,13,12,17,12,11,14,16],
[9,0,11,14,13,11,10,13,10,18,10],
[12,14,0,15,12,10,16,10,11,17,16],
[8,11,10,0,11,11,14,13,9,14,7],
[12,12,13,14,0,13,16,16,11,12,6],
[13,14,15,14,12,0,14,9,13,17,13],
[8,15,9,11,9,11,0,10,5,14,7],
[13,12,15,12,9,16,15,0,10,13,11],
[14,15,14,16,14,12,20,15,0,18,13],
[11,7,8,11,13,8,11,12,7,0,9],
[9,15,9,18,19,12,18,14,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,13,17,18,15,9,9,15,8],
[14,0,13,13,16,16,16,12,12,16,11],
[9,12,0,12,13,16,15,11,13,14,8],
[12,12,13,0,18,17,15,9,14,18,7],
[8,9,12,7,0,16,12,8,8,13,6],
[7,9,9,8,9,0,6,10,11,11,6],
[10,9,10,10,13,19,0,12,11,14,9],
[16,13,14,16,17,15,13,0,8,16,9],
[16,13,12,11,17,14,14,17,0,17,13],
[10,9,11,7,12,14,11,9,8,0,6],
[17,14,17,18,19,19,16,16,12,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,16,14,17,13,15,16,12,13],
[10,0,8,12,9,12,8,11,15,12,9],
[11,17,0,13,10,12,9,13,11,12,12],
[9,13,12,0,14,10,10,15,12,10,10],
[11,16,15,11,0,14,8,13,10,11,12],
[8,13,13,15,11,0,8,14,10,10,12],
[12,17,16,15,17,17,0,14,17,14,14],
[10,14,12,10,12,11,11,0,13,10,12],
[9,10,14,13,15,15,8,12,0,14,15],
[13,13,13,15,14,15,11,15,11,0,13],
[12,16,13,15,13,13,11,13,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,14,13,11,13,8,13,15,14],
[13,0,14,15,9,15,14,10,11,10,8],
[12,11,0,9,11,11,11,9,8,7,11],
[11,10,16,0,12,13,12,10,13,11,11],
[12,16,14,13,0,16,15,14,14,16,12],
[14,10,14,12,9,0,13,6,13,11,11],
[12,11,14,13,10,12,0,10,12,10,10],
[17,15,16,15,11,19,15,0,15,14,14],
[12,14,17,12,11,12,13,10,0,12,13],
[10,15,18,14,9,14,15,11,13,0,12],
[11,17,14,14,13,14,15,11,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,9,6,11,12,14,9,9,7],
[15,0,12,12,8,11,15,12,15,12,9],
[17,13,0,13,13,12,18,11,12,15,8],
[16,13,12,0,11,10,15,13,12,16,13],
[19,17,12,14,0,16,19,13,14,17,12],
[14,14,13,15,9,0,14,16,14,14,10],
[13,10,7,10,6,11,0,10,11,14,9],
[11,13,14,12,12,9,15,0,13,13,9],
[16,10,13,13,11,11,14,12,0,13,9],
[16,13,10,9,8,11,11,12,12,0,8],
[18,16,17,12,13,15,16,16,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,15,17,13,10,9,16,15,16],
[9,0,9,9,20,13,6,13,15,9,15],
[13,16,0,15,17,14,15,11,14,21,17],
[10,16,10,0,20,9,14,10,16,13,13],
[8,5,8,5,0,8,6,8,5,10,6],
[12,12,11,16,17,0,10,13,13,13,16],
[15,19,10,11,19,15,0,14,20,13,19],
[16,12,14,15,17,12,11,0,12,15,16],
[9,10,11,9,20,12,5,13,0,11,13],
[10,16,4,12,15,12,12,10,14,0,18],
[9,10,8,12,19,9,6,9,12,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,11,16,14,13,16,20,13,15],
[10,0,12,13,17,13,12,12,14,13,11],
[8,13,0,12,14,12,13,14,18,10,11],
[14,12,13,0,16,11,12,14,17,14,14],
[9,8,11,9,0,10,10,10,14,11,9],
[11,12,13,14,15,0,14,11,16,13,12],
[12,13,12,13,15,11,0,16,16,11,13],
[9,13,11,11,15,14,9,0,13,13,13],
[5,11,7,8,11,9,9,12,0,10,7],
[12,12,15,11,14,12,14,12,15,0,14],
[10,14,14,11,16,13,12,12,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,9,13,12,16,11,9,7],
[14,0,13,10,8,12,9,16,13,11,11],
[12,12,0,9,9,10,17,20,11,11,10],
[15,15,16,0,13,14,14,18,13,12,13],
[16,17,16,12,0,15,17,21,17,14,17],
[12,13,15,11,10,0,16,19,12,9,9],
[13,16,8,11,8,9,0,13,10,9,9],
[9,9,5,7,4,6,12,0,5,6,6],
[14,12,14,12,8,13,15,20,0,13,12],
[16,14,14,13,11,16,16,19,12,0,12],
[18,14,15,12,8,16,16,19,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,11,12,11,11,14,10,11,11],
[15,0,15,11,16,13,13,18,13,14,14],
[12,10,0,14,13,12,13,14,13,14,12],
[14,14,11,0,12,11,11,15,11,11,11],
[13,9,12,13,0,7,11,9,12,11,10],
[14,12,13,14,18,0,13,14,14,10,14],
[14,12,12,14,14,12,0,14,13,13,13],
[11,7,11,10,16,11,11,0,10,12,14],
[15,12,12,14,13,11,12,15,0,14,16],
[14,11,11,14,14,15,12,13,11,0,13],
[14,11,13,14,15,11,12,11,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,7,18,4,14,8,12,10,8],
[15,0,12,13,11,9,15,10,15,11,13],
[17,13,0,12,19,6,7,8,8,11,11],
[18,12,13,0,17,8,10,5,9,13,8],
[7,14,6,8,0,6,9,3,6,8,6],
[21,16,19,17,19,0,16,8,12,15,11],
[11,10,18,15,16,9,0,10,11,10,5],
[17,15,17,20,22,17,15,0,8,14,13],
[13,10,17,16,19,13,14,17,0,10,12],
[15,14,14,12,17,10,15,11,15,0,11],
[17,12,14,17,19,14,20,12,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,19,15,12,13,16,8,14,14],
[12,0,14,16,13,8,11,16,12,16,17],
[11,11,0,10,15,11,9,13,3,6,9],
[6,9,15,0,16,10,8,13,10,6,8],
[10,12,10,9,0,6,12,14,6,8,9],
[13,17,14,15,19,0,15,19,11,14,14],
[12,14,16,17,13,10,0,20,7,17,15],
[9,9,12,12,11,6,5,0,9,9,13],
[17,13,22,15,19,14,18,16,0,12,13],
[11,9,19,19,17,11,8,16,13,0,14],
[11,8,16,17,16,11,10,12,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,18,14,13,13,10,8,8,7],
[16,0,6,15,13,11,9,13,9,12,7],
[18,19,0,19,16,18,17,14,11,19,14],
[7,10,6,0,8,6,9,7,4,9,7],
[11,12,9,17,0,14,12,12,9,10,12],
[12,14,7,19,11,0,17,12,4,8,13],
[12,16,8,16,13,8,0,13,6,10,8],
[15,12,11,18,13,13,12,0,13,10,6],
[17,16,14,21,16,21,19,12,0,16,13],
[17,13,6,16,15,17,15,15,9,0,10],
[18,18,11,18,13,12,17,19,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,12,14,9,16,16,12,14,12],
[10,0,9,10,13,8,12,11,9,11,10],
[10,16,0,13,17,10,11,12,8,13,14],
[13,15,12,0,15,14,15,13,13,15,13],
[11,12,8,10,0,9,12,13,9,10,10],
[16,17,15,11,16,0,14,15,16,17,14],
[9,13,14,10,13,11,0,11,12,12,10],
[9,14,13,12,12,10,14,0,11,14,15],
[13,16,17,12,16,9,13,14,0,13,11],
[11,14,12,10,15,8,13,11,12,0,12],
[13,15,11,12,15,11,15,10,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,18,11,11,11,12,10,10,13],
[9,0,15,15,15,18,13,15,11,11,9],
[15,10,0,19,13,12,9,11,12,13,11],
[7,10,6,0,10,8,11,8,8,2,12],
[14,10,12,15,0,17,12,13,10,6,13],
[14,7,13,17,8,0,12,15,8,9,12],
[14,12,16,14,13,13,0,13,14,14,7],
[13,10,14,17,12,10,12,0,10,10,15],
[15,14,13,17,15,17,11,15,0,8,16],
[15,14,12,23,19,16,11,15,17,0,16],
[12,16,14,13,12,13,18,10,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,0,2,9,6,7,12,4,6],
[20,0,9,8,10,9,7,9,15,7,9],
[17,16,0,16,16,18,18,17,20,13,9],
[25,17,9,0,6,13,12,8,20,5,8],
[23,15,9,19,0,18,20,14,19,12,9],
[16,16,7,12,7,0,6,10,15,4,7],
[19,18,7,13,5,19,0,8,19,10,7],
[18,16,8,17,11,15,17,0,17,4,10],
[13,10,5,5,6,10,6,8,0,7,10],
[21,18,12,20,13,21,15,21,18,0,14],
[19,16,16,17,16,18,18,15,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,15,13,13,18,13,14,13],
[13,0,9,10,13,10,7,15,9,12,10],
[13,16,0,14,11,15,10,15,13,11,13],
[12,15,11,0,14,12,13,15,11,13,12],
[10,12,14,11,0,15,12,17,13,14,13],
[12,15,10,13,10,0,11,16,8,9,13],
[12,18,15,12,13,14,0,16,12,14,16],
[7,10,10,10,8,9,9,0,7,8,12],
[12,16,12,14,12,17,13,18,0,13,16],
[11,13,14,12,11,16,11,17,12,0,15],
[12,15,12,13,12,12,9,13,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,14,14,12,21,17,18,21,14,16],
[6,0,8,8,4,6,11,10,11,6,6],
[11,17,0,16,7,19,14,16,23,11,11],
[11,17,9,0,14,18,12,18,14,13,15],
[13,21,18,11,0,16,14,14,19,7,9],
[4,19,6,7,9,0,12,12,12,5,0],
[8,14,11,13,11,13,0,10,16,4,8],
[7,15,9,7,11,13,15,0,14,7,9],
[4,14,2,11,6,13,9,11,0,9,4],
[11,19,14,12,18,20,21,18,16,0,9],
[9,19,14,10,16,25,17,16,21,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,13,15,11,10,17,15,11,13],
[11,0,10,14,16,12,10,14,15,10,12],
[14,15,0,16,19,13,13,14,16,12,14],
[12,11,9,0,17,10,13,11,13,9,12],
[10,9,6,8,0,10,12,14,12,9,13],
[14,13,12,15,15,0,14,16,17,12,12],
[15,15,12,12,13,11,0,14,15,10,12],
[8,11,11,14,11,9,11,0,12,10,14],
[10,10,9,12,13,8,10,13,0,10,11],
[14,15,13,16,16,13,15,15,15,0,11],
[12,13,11,13,12,13,13,11,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,9,11,11,3,14,9,8,6,10],
[20,0,12,17,20,10,24,14,18,12,19],
[16,13,0,16,19,10,19,14,16,12,16],
[14,8,9,0,14,13,18,19,8,6,13],
[14,5,6,11,0,3,14,6,8,12,13],
[22,15,15,12,22,0,14,9,14,14,16],
[11,1,6,7,11,11,0,11,1,7,11],
[16,11,11,6,19,16,14,0,14,12,16],
[17,7,9,17,17,11,24,11,0,12,17],
[19,13,13,19,13,11,18,13,13,0,8],
[15,6,9,12,12,9,14,9,8,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,7,13,12,10,10,13,15,11,10],
[12,0,8,10,8,9,7,10,12,8,10],
[18,17,0,11,13,16,11,15,16,15,15],
[12,15,14,0,15,14,10,13,12,12,11],
[13,17,12,10,0,12,14,14,14,11,10],
[15,16,9,11,13,0,12,12,15,14,10],
[15,18,14,15,11,13,0,16,13,12,13],
[12,15,10,12,11,13,9,0,19,14,8],
[10,13,9,13,11,10,12,6,0,8,8],
[14,17,10,13,14,11,13,11,17,0,10],
[15,15,10,14,15,15,12,17,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,10,16,10,15,16,14,14,14],
[15,0,20,11,17,13,15,18,14,12,14],
[7,5,0,11,13,12,12,11,7,5,13],
[15,14,14,0,17,15,20,14,15,12,13],
[9,8,12,8,0,7,13,13,10,10,8],
[15,12,13,10,18,0,19,16,11,11,12],
[10,10,13,5,12,6,0,12,6,7,12],
[9,7,14,11,12,9,13,0,6,7,9],
[11,11,18,10,15,14,19,19,0,6,14],
[11,13,20,13,15,14,18,18,19,0,15],
[11,11,12,12,17,13,13,16,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,12,14,7,17,11,19,17,13],
[12,0,14,11,10,11,16,12,15,12,10],
[7,11,0,7,7,9,14,6,16,12,8],
[13,14,18,0,10,9,14,7,17,13,10],
[11,15,18,15,0,12,13,9,16,13,8],
[18,14,16,16,13,0,18,9,13,15,11],
[8,9,11,11,12,7,0,7,17,15,11],
[14,13,19,18,16,16,18,0,13,15,11],
[6,10,9,8,9,12,8,12,0,12,12],
[8,13,13,12,12,10,10,10,13,0,11],
[12,15,17,15,17,14,14,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,10,17,13,11,10,15,14,16],
[12,0,12,8,13,17,10,10,15,14,16],
[13,13,0,12,17,19,12,9,13,17,14],
[15,17,13,0,19,18,12,13,19,18,17],
[8,12,8,6,0,9,9,12,12,9,9],
[12,8,6,7,16,0,10,10,14,9,11],
[14,15,13,13,16,15,0,14,15,12,15],
[15,15,16,12,13,15,11,0,17,19,13],
[10,10,12,6,13,11,10,8,0,12,13],
[11,11,8,7,16,16,13,6,13,0,12],
[9,9,11,8,16,14,10,12,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,9,2,17,4,13,9,2,5,11],
[20,0,19,15,17,17,20,11,13,15,21],
[16,6,0,6,17,6,13,13,6,7,18],
[23,10,19,0,20,13,16,14,4,8,14],
[8,8,8,5,0,2,8,9,2,8,14],
[21,8,19,12,23,0,21,15,12,15,21],
[12,5,12,9,17,4,0,9,11,17,18],
[16,14,12,11,16,10,16,0,6,14,14],
[23,12,19,21,23,13,14,19,0,21,21],
[20,10,18,17,17,10,8,11,4,0,13],
[14,4,7,11,11,4,7,11,4,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,14,9,6,8,11,8,19,8],
[15,0,8,8,14,8,13,11,9,13,9],
[17,17,0,15,19,13,12,16,8,18,14],
[11,17,10,0,14,9,12,12,9,20,14],
[16,11,6,11,0,9,12,8,4,13,14],
[19,17,12,16,16,0,13,17,12,20,20],
[17,12,13,13,13,12,0,12,13,15,13],
[14,14,9,13,17,8,13,0,9,13,12],
[17,16,17,16,21,13,12,16,0,21,17],
[6,12,7,5,12,5,10,12,4,0,3],
[17,16,11,11,11,5,12,13,8,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,13,14,15,13,14,11,9,15],
[16,0,8,14,14,15,10,14,11,11,14],
[15,17,0,16,15,12,15,18,14,15,15],
[12,11,9,0,15,14,17,15,16,12,12],
[11,11,10,10,0,10,9,10,10,10,12],
[10,10,13,11,15,0,16,16,11,11,12],
[12,15,10,8,16,9,0,13,16,8,12],
[11,11,7,10,15,9,12,0,8,6,12],
[14,14,11,9,15,14,9,17,0,10,16],
[16,14,10,13,15,14,17,19,15,0,15],
[10,11,10,13,13,13,13,13,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,8,11,17,8,2,10,7,4],
[20,0,10,8,14,17,8,12,8,5,7],
[23,15,0,17,18,20,11,14,17,7,11],
[17,17,8,0,14,10,1,8,11,10,10],
[14,11,7,11,0,11,7,12,8,5,3],
[8,8,5,15,14,0,15,9,8,10,9],
[17,17,14,24,18,10,0,16,14,18,14],
[23,13,11,17,13,16,9,0,15,7,8],
[15,17,8,14,17,17,11,10,0,7,10],
[18,20,18,15,20,15,7,18,18,0,15],
[21,18,14,15,22,16,11,17,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,10,10,11,9,6,6,9,15],
[16,0,16,11,11,16,9,10,16,8,17],
[13,9,0,13,11,15,10,9,13,10,14],
[15,14,12,0,10,16,14,12,14,11,19],
[15,14,14,15,0,12,13,11,14,14,17],
[14,9,10,9,13,0,11,9,11,9,14],
[16,16,15,11,12,14,0,14,16,13,17],
[19,15,16,13,14,16,11,0,19,14,18],
[19,9,12,11,11,14,9,6,0,9,15],
[16,17,15,14,11,16,12,11,16,0,15],
[10,8,11,6,8,11,8,7,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,13,9,17,12,14,11,6,12],
[10,0,12,11,9,11,12,9,11,11,10],
[13,13,0,15,13,13,17,17,12,7,14],
[12,14,10,0,9,13,12,12,8,5,10],
[16,16,12,16,0,12,15,14,14,13,15],
[8,14,12,12,13,0,12,10,12,12,10],
[13,13,8,13,10,13,0,14,12,10,9],
[11,16,8,13,11,15,11,0,10,9,14],
[14,14,13,17,11,13,13,15,0,12,11],
[19,14,18,20,12,13,15,16,13,0,12],
[13,15,11,15,10,15,16,11,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,11,18,9,18,12,12,14,13],
[10,0,13,10,13,11,16,10,12,10,16],
[14,12,0,14,11,14,12,8,12,14,14],
[14,15,11,0,14,13,17,11,7,13,9],
[7,12,14,11,0,12,15,12,6,13,13],
[16,14,11,12,13,0,19,7,13,11,9],
[7,9,13,8,10,6,0,11,10,8,11],
[13,15,17,14,13,18,14,0,12,14,13],
[13,13,13,18,19,12,15,13,0,17,15],
[11,15,11,12,12,14,17,11,8,0,14],
[12,9,11,16,12,16,14,12,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,13,14,20,18,18,15,16,17],
[15,0,11,12,16,17,14,19,19,16,16],
[15,14,0,12,15,16,15,14,14,19,17],
[12,13,13,0,16,18,15,11,11,11,12],
[11,9,10,9,0,16,16,19,13,9,15],
[5,8,9,7,9,0,14,11,13,11,8],
[7,11,10,10,9,11,0,12,11,15,12],
[7,6,11,14,6,14,13,0,11,11,13],
[10,6,11,14,12,12,14,14,0,10,18],
[9,9,6,14,16,14,10,14,15,0,13],
[8,9,8,13,10,17,13,12,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,6,12,6,10,5,13,6,8,14],
[11,0,11,12,9,11,13,13,8,12,13],
[19,14,0,12,8,15,8,14,8,12,18],
[13,13,13,0,12,14,14,7,12,13,14],
[19,16,17,13,0,13,14,13,15,12,15],
[15,14,10,11,12,0,12,10,8,11,10],
[20,12,17,11,11,13,0,12,12,8,13],
[12,12,11,18,12,15,13,0,14,11,16],
[19,17,17,13,10,17,13,11,0,13,13],
[17,13,13,12,13,14,17,14,12,0,16],
[11,12,7,11,10,15,12,9,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,16,9,10,12,8,14,9,10],
[14,0,10,16,14,13,9,14,16,14,7],
[15,15,0,18,15,20,14,17,18,15,11],
[9,9,7,0,13,13,4,12,14,13,4],
[16,11,10,12,0,17,8,19,19,17,7],
[15,12,5,12,8,0,7,14,11,11,5],
[13,16,11,21,17,18,0,13,19,17,16],
[17,11,8,13,6,11,12,0,12,11,10],
[11,9,7,11,6,14,6,13,0,13,6],
[16,11,10,12,8,14,8,14,12,0,12],
[15,18,14,21,18,20,9,15,19,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,9,12,11,17,14,10,12,14],
[13,0,13,8,11,12,11,13,11,9,11],
[11,12,0,8,11,11,14,13,11,12,17],
[16,17,17,0,14,11,19,14,12,16,21],
[13,14,14,11,0,12,13,12,11,10,16],
[14,13,14,14,13,0,15,14,9,11,14],
[8,14,11,6,12,10,0,10,11,11,14],
[11,12,12,11,13,11,15,0,13,10,15],
[15,14,14,13,14,16,14,12,0,14,17],
[13,16,13,9,15,14,14,15,11,0,16],
[11,14,8,4,9,11,11,10,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,16,12,15,13,15,12,8,12],
[10,0,10,9,11,13,9,9,14,8,12],
[14,15,0,18,16,12,11,16,14,13,11],
[9,16,7,0,12,15,12,10,11,11,12],
[13,14,9,13,0,15,9,14,16,16,14],
[10,12,13,10,10,0,7,13,14,7,12],
[12,16,14,13,16,18,0,13,16,11,10],
[10,16,9,15,11,12,12,0,11,12,17],
[13,11,11,14,9,11,9,14,0,13,11],
[17,17,12,14,9,18,14,13,12,0,13],
[13,13,14,13,11,13,15,8,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,11,16,12,11,12,14,11],
[12,0,13,10,16,14,15,14,11,11,15],
[12,12,0,8,14,14,13,11,12,12,14],
[13,15,17,0,12,15,14,10,13,12,13],
[14,9,11,13,0,15,14,15,14,10,11],
[9,11,11,10,10,0,10,11,9,12,12],
[13,10,12,11,11,15,0,11,13,10,11],
[14,11,14,15,10,14,14,0,14,11,17],
[13,14,13,12,11,16,12,11,0,11,10],
[11,14,13,13,15,13,15,14,14,0,12],
[14,10,11,12,14,13,14,8,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,12,12,20,12,12,5,12,12],
[13,0,12,25,20,20,25,20,13,20,20],
[13,13,0,13,20,8,13,13,13,13,13],
[13,0,12,0,20,20,8,20,13,0,20],
[13,5,5,5,0,8,13,5,5,5,5],
[5,5,17,5,17,0,5,5,5,5,17],
[13,0,12,17,12,20,0,12,5,0,12],
[13,5,12,5,20,20,13,0,13,0,12],
[20,12,12,12,20,20,20,12,0,12,12],
[13,5,12,25,20,20,25,25,13,0,20],
[13,5,12,5,20,8,13,13,13,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,9,12,12,10,10,8,8,9],
[15,0,9,12,10,14,15,12,12,12,12],
[15,16,0,13,19,15,15,11,13,16,14],
[16,13,12,0,14,9,16,11,15,14,12],
[13,15,6,11,0,12,14,10,9,13,15],
[13,11,10,16,13,0,13,13,11,11,12],
[15,10,10,9,11,12,0,7,9,11,10],
[15,13,14,14,15,12,18,0,15,13,11],
[17,13,12,10,16,14,16,10,0,11,14],
[17,13,9,11,12,14,14,12,14,0,15],
[16,13,11,13,10,13,15,14,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,11,11,10,11,19,10,18,10],
[15,0,12,16,12,14,14,18,16,20,16],
[16,13,0,17,11,11,8,13,13,16,8],
[14,9,8,0,10,8,10,13,8,10,8],
[14,13,14,15,0,18,11,19,18,18,8],
[15,11,14,17,7,0,8,15,12,16,10],
[14,11,17,15,14,17,0,15,14,13,8],
[6,7,12,12,6,10,10,0,8,12,4],
[15,9,12,17,7,13,11,17,0,22,7],
[7,5,9,15,7,9,12,13,3,0,8],
[15,9,17,17,17,15,17,21,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,16,8,11,9,7,13,5,15],
[14,0,15,13,11,14,8,8,9,8,16],
[14,10,0,16,17,13,14,10,12,12,16],
[9,12,9,0,8,9,9,10,8,9,9],
[17,14,8,17,0,15,17,10,13,12,12],
[14,11,12,16,10,0,12,7,10,4,13],
[16,17,11,16,8,13,0,6,13,8,12],
[18,17,15,15,15,18,19,0,12,16,16],
[12,16,13,17,12,15,12,13,0,10,14],
[20,17,13,16,13,21,17,9,15,0,14],
[10,9,9,16,13,12,13,9,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,12,15,14,17,15,15,15,10],
[12,0,13,13,12,15,13,15,12,13,11],
[10,12,0,13,9,10,14,13,10,11,11],
[13,12,12,0,12,13,16,14,14,14,14],
[10,13,16,13,0,17,15,15,16,14,15],
[11,10,15,12,8,0,15,13,12,14,11],
[8,12,11,9,10,10,0,11,11,11,10],
[10,10,12,11,10,12,14,0,11,11,15],
[10,13,15,11,9,13,14,14,0,13,10],
[10,12,14,11,11,11,14,14,12,0,12],
[15,14,14,11,10,14,15,10,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,18,9,12,8,14,9,12,11],
[18,0,10,18,18,14,13,14,14,13,20],
[11,15,0,17,17,16,8,17,9,16,15],
[7,7,8,0,9,7,4,13,0,12,11],
[16,7,8,16,0,7,4,13,5,12,7],
[13,11,9,18,18,0,8,18,14,13,11],
[17,12,17,21,21,17,0,18,10,16,20],
[11,11,8,12,12,7,7,0,8,12,11],
[16,11,16,25,20,11,15,17,0,16,15],
[13,12,9,13,13,12,9,13,9,0,11],
[14,5,10,14,18,14,5,14,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,10,13,15,13,11,13,12,10],
[11,0,7,10,11,12,9,12,9,10,9],
[12,18,0,14,14,16,14,10,11,15,12],
[15,15,11,0,13,17,17,11,14,11,13],
[12,14,11,12,0,14,14,11,11,11,11],
[10,13,9,8,11,0,13,9,10,10,11],
[12,16,11,8,11,12,0,9,9,11,7],
[14,13,15,14,14,16,16,0,11,15,9],
[12,16,14,11,14,15,16,14,0,14,11],
[13,15,10,14,14,15,14,10,11,0,11],
[15,16,13,12,14,14,18,16,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,20,15,19,14,11,19,15,14],
[15,0,16,24,15,19,14,12,20,16,19],
[14,9,0,19,6,14,14,15,14,19,18],
[5,1,6,0,5,5,13,10,13,10,10],
[10,10,19,20,0,20,19,19,21,21,19],
[6,6,11,20,5,0,13,15,15,16,10],
[11,11,11,12,6,12,0,12,15,20,15],
[14,13,10,15,6,10,13,0,10,19,14],
[6,5,11,12,4,10,10,15,0,15,15],
[10,9,6,15,4,9,5,6,10,0,11],
[11,6,7,15,6,15,10,11,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,16,12,19,20,13,21,15,15],
[10,0,12,17,8,10,17,9,14,14,10],
[11,13,0,19,12,16,15,10,18,14,14],
[9,8,6,0,11,12,10,8,13,7,11],
[13,17,13,14,0,15,18,10,14,13,14],
[6,15,9,13,10,0,12,6,15,7,11],
[5,8,10,15,7,13,0,6,11,9,10],
[12,16,15,17,15,19,19,0,16,15,16],
[4,11,7,12,11,10,14,9,0,8,12],
[10,11,11,18,12,18,16,10,17,0,17],
[10,15,11,14,11,14,15,9,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,19,20,18,7,24,19,19,13,10],
[15,0,18,21,14,16,21,14,15,10,25],
[6,7,0,21,15,7,21,14,6,1,16],
[5,4,4,0,5,0,5,4,4,0,10],
[7,11,10,20,0,7,21,20,10,7,11],
[18,9,18,25,18,0,18,18,13,13,24],
[1,4,4,20,4,7,0,13,4,0,10],
[6,11,11,21,5,7,12,0,6,1,11],
[6,10,19,21,15,12,21,19,0,15,16],
[12,15,24,25,18,12,25,24,10,0,15],
[15,0,9,15,14,1,15,14,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,20,14,12,13,14,9,17,17],
[16,0,9,21,11,12,13,17,13,15,16],
[15,16,0,22,17,11,18,20,15,17,23],
[5,4,3,0,6,10,7,6,7,7,6],
[11,14,8,19,0,14,9,15,6,10,10],
[13,13,14,15,11,0,11,14,9,18,18],
[12,12,7,18,16,14,0,11,17,17,15],
[11,8,5,19,10,11,14,0,12,16,13],
[16,12,10,18,19,16,8,13,0,18,22],
[8,10,8,18,15,7,8,9,7,0,12],
[8,9,2,19,15,7,10,12,3,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,19,17,10,12,16,14,19,12,23],
[12,0,13,19,7,12,7,14,13,11,17],
[6,12,0,15,7,10,7,12,13,8,14],
[8,6,10,0,7,13,10,9,11,7,14],
[15,18,18,18,0,13,11,14,21,15,20],
[13,13,15,12,12,0,9,9,14,9,13],
[9,18,18,15,14,16,0,12,16,13,22],
[11,11,13,16,11,16,13,0,15,12,11],
[6,12,12,14,4,11,9,10,0,12,13],
[13,14,17,18,10,16,12,13,13,0,17],
[2,8,11,11,5,12,3,14,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,14,12,13,18,13,14,24,16,14],
[2,0,14,9,10,15,4,9,18,5,10],
[11,11,0,6,16,5,10,11,16,15,9],
[13,16,19,0,11,11,10,14,24,13,10],
[12,15,9,14,0,10,15,13,23,19,10],
[7,10,20,14,15,0,13,15,24,10,9],
[12,21,15,15,10,12,0,6,21,11,14],
[11,16,14,11,12,10,19,0,21,15,14],
[1,7,9,1,2,1,4,4,0,1,4],
[9,20,10,12,6,15,14,10,24,0,11],
[11,15,16,15,15,16,11,11,21,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,16,13,16,13,15,11,15,11],
[10,0,11,18,17,13,11,18,13,15,8],
[13,14,0,17,12,13,16,17,14,16,12],
[9,7,8,0,12,10,6,13,9,10,7],
[12,8,13,13,0,14,13,18,11,14,10],
[9,12,12,15,11,0,7,15,9,13,9],
[12,14,9,19,12,18,0,17,11,14,14],
[10,7,8,12,7,10,8,0,13,13,10],
[14,12,11,16,14,16,14,12,0,16,15],
[10,10,9,15,11,12,11,12,9,0,12],
[14,17,13,18,15,16,11,15,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,11,16,14,13,13,10,8,11],
[16,0,16,16,17,14,10,16,13,14,12],
[13,9,0,11,11,12,12,15,13,7,13],
[14,9,14,0,17,10,11,15,13,12,11],
[9,8,14,8,0,8,5,15,8,9,11],
[11,11,13,15,17,0,7,12,9,11,10],
[12,15,13,14,20,18,0,18,14,12,17],
[12,9,10,10,10,13,7,0,12,8,15],
[15,12,12,12,17,16,11,13,0,12,15],
[17,11,18,13,16,14,13,17,13,0,14],
[14,13,12,14,14,15,8,10,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,15,15,12,15,13,13,13,11],
[12,0,17,16,15,13,12,14,11,11,10],
[9,8,0,12,12,12,10,13,9,9,9],
[10,9,13,0,11,8,9,11,8,7,6],
[10,10,13,14,0,10,12,12,9,11,6],
[13,12,13,17,15,0,14,15,12,11,8],
[10,13,15,16,13,11,0,13,11,13,8],
[12,11,12,14,13,10,12,0,8,12,12],
[12,14,16,17,16,13,14,17,0,14,14],
[12,14,16,18,14,14,12,13,11,0,10],
[14,15,16,19,19,17,17,13,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,9,16,22,20,15,19,18,17,16],
[2,0,10,12,22,22,15,15,13,18,12],
[16,15,0,15,25,23,12,10,13,13,19],
[9,13,10,0,15,17,17,9,18,14,15],
[3,3,0,10,0,23,9,10,8,13,8],
[5,3,2,8,2,0,2,4,8,9,2],
[10,10,13,8,16,23,0,10,14,15,11],
[6,10,15,16,15,21,15,0,18,14,10],
[7,12,12,7,17,17,11,7,0,17,7],
[8,7,12,11,12,16,10,11,8,0,12],
[9,13,6,10,17,23,14,15,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,13,12,11,13,13,13,11,15],
[15,0,11,13,15,12,16,13,11,11,13],
[15,14,0,19,18,13,11,12,14,11,16],
[12,12,6,0,12,10,9,7,11,11,14],
[13,10,7,13,0,10,8,11,8,10,12],
[14,13,12,15,15,0,14,13,10,13,15],
[12,9,14,16,17,11,0,10,10,13,14],
[12,12,13,18,14,12,15,0,11,11,15],
[12,14,11,14,17,15,15,14,0,16,17],
[14,14,14,14,15,12,12,14,9,0,13],
[10,12,9,11,13,10,11,10,8,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,17,11,12,10,16,13,9,20],
[16,0,11,15,9,13,13,17,10,16,15],
[12,14,0,13,13,13,14,13,15,14,15],
[8,10,12,0,13,12,12,16,12,9,12],
[14,16,12,12,0,15,13,15,15,15,13],
[13,12,12,13,10,0,9,11,13,13,16],
[15,12,11,13,12,16,0,16,16,15,15],
[9,8,12,9,10,14,9,0,14,14,12],
[12,15,10,13,10,12,9,11,0,12,12],
[16,9,11,16,10,12,10,11,13,0,15],
[5,10,10,13,12,9,10,13,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,14,15,12,12,13,10,10,11],
[10,0,8,8,12,10,11,11,9,9,10],
[15,17,0,14,15,12,14,15,12,13,13],
[11,17,11,0,15,13,11,16,10,12,13],
[10,13,10,10,0,12,11,8,9,11,9],
[13,15,13,12,13,0,16,10,14,13,11],
[13,14,11,14,14,9,0,15,10,8,15],
[12,14,10,9,17,15,10,0,9,10,15],
[15,16,13,15,16,11,15,16,0,11,17],
[15,16,12,13,14,12,17,15,14,0,14],
[14,15,12,12,16,14,10,10,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,15,15,16,12,16,12,15,16],
[10,0,9,16,17,13,15,17,16,15,16],
[12,16,0,14,15,13,15,17,12,13,15],
[10,9,11,0,16,11,15,17,14,13,15],
[10,8,10,9,0,7,8,12,12,10,8],
[9,12,12,14,18,0,15,14,16,15,18],
[13,10,10,10,17,10,0,14,16,12,12],
[9,8,8,8,13,11,11,0,14,12,14],
[13,9,13,11,13,9,9,11,0,9,9],
[10,10,12,12,15,10,13,13,16,0,11],
[9,9,10,10,17,7,13,11,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,17,11,13,13,16,10,13,9],
[10,0,11,17,9,12,11,13,12,10,12],
[14,14,0,18,11,13,11,13,8,13,10],
[8,8,7,0,7,9,8,7,8,9,7],
[14,16,14,18,0,13,16,14,11,13,14],
[12,13,12,16,12,0,12,14,9,12,9],
[12,14,14,17,9,13,0,13,10,11,10],
[9,12,12,18,11,11,12,0,8,13,7],
[15,13,17,17,14,16,15,17,0,14,12],
[12,15,12,16,12,13,14,12,11,0,10],
[16,13,15,18,11,16,15,18,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,16,15,14,15,20,11,7,14,16],
[17,0,9,21,7,24,16,13,17,14,24],
[9,16,0,16,16,15,16,16,12,16,16],
[10,4,9,0,7,12,10,0,11,4,11],
[11,18,9,18,0,18,20,14,13,18,19],
[10,1,10,13,7,0,14,1,7,13,18],
[5,9,9,15,5,11,0,5,8,5,16],
[14,12,9,25,11,24,20,0,18,24,21],
[18,8,13,14,12,18,17,7,0,14,25],
[11,11,9,21,7,12,20,1,11,0,12],
[9,1,9,14,6,7,9,4,0,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,15,16,25,25,9,17,17,17],
[16,0,16,14,16,25,24,16,17,9,9],
[17,9,0,15,14,19,23,9,19,15,15],
[10,11,10,0,8,11,24,8,11,17,17],
[9,9,11,17,0,11,17,17,11,15,15],
[0,0,6,14,14,0,22,6,15,7,7],
[0,1,2,1,8,3,0,9,3,9,9],
[16,9,16,17,8,19,16,0,19,9,9],
[8,8,6,14,14,10,22,6,0,14,14],
[8,16,10,8,10,18,16,16,11,0,23],
[8,16,10,8,10,18,16,16,11,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,16,11,13,13,14,16,14,13],
[10,0,16,13,14,13,13,13,15,10,15],
[11,9,0,13,9,13,13,14,15,12,13],
[9,12,12,0,9,15,14,9,16,15,14],
[14,11,16,16,0,14,14,13,17,16,16],
[12,12,12,10,11,0,12,11,11,13,12],
[12,12,12,11,11,13,0,13,12,12,12],
[11,12,11,16,12,14,12,0,16,14,12],
[9,10,10,9,8,14,13,9,0,11,10],
[11,15,13,10,9,12,13,11,14,0,11],
[12,10,12,11,9,13,13,13,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,12,13,15,7,13,12,10,6],
[17,0,16,17,19,20,14,19,12,14,17],
[13,9,0,15,11,15,8,15,11,10,11],
[13,8,10,0,10,12,9,10,8,6,7],
[12,6,14,15,0,17,6,13,10,11,8],
[10,5,10,13,8,0,4,12,5,9,6],
[18,11,17,16,19,21,0,17,14,14,12],
[12,6,10,15,12,13,8,0,8,10,10],
[13,13,14,17,15,20,11,17,0,15,14],
[15,11,15,19,14,16,11,15,10,0,9],
[19,8,14,18,17,19,13,15,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,8,8,8,8,10,10,14,8],
[15,0,9,10,8,13,15,17,11,16,7],
[17,16,0,13,13,16,18,15,14,12,13],
[17,15,12,0,11,17,13,14,17,16,10],
[17,17,12,14,0,14,15,17,17,16,16],
[17,12,9,8,11,0,12,16,12,14,8],
[17,10,7,12,10,13,0,11,10,10,11],
[15,8,10,11,8,9,14,0,11,13,6],
[15,14,11,8,8,13,15,14,0,11,11],
[11,9,13,9,9,11,15,12,14,0,9],
[17,18,12,15,9,17,14,19,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,8,12,17,6,10,14,7,10,14],
[13,0,11,11,13,15,12,12,13,14,15],
[17,14,0,14,17,10,10,18,12,14,14],
[13,14,11,0,18,12,14,11,10,13,12],
[8,12,8,7,0,9,10,11,7,11,11],
[19,10,15,13,16,0,16,17,14,18,14],
[15,13,15,11,15,9,0,16,9,14,14],
[11,13,7,14,14,8,9,0,6,16,7],
[18,12,13,15,18,11,16,19,0,11,15],
[15,11,11,12,14,7,11,9,14,0,10],
[11,10,11,13,14,11,11,18,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,14,17,15,12,12,15,10,15],
[14,0,13,15,15,14,9,17,12,14,14],
[16,12,0,13,19,16,12,16,10,15,14],
[11,10,12,0,16,17,9,11,9,8,14],
[8,10,6,9,0,10,10,11,10,12,13],
[10,11,9,8,15,0,6,11,9,8,11],
[13,16,13,16,15,19,0,18,11,15,15],
[13,8,9,14,14,14,7,0,8,11,16],
[10,13,15,16,15,16,14,17,0,19,13],
[15,11,10,17,13,17,10,14,6,0,13],
[10,11,11,11,12,14,10,9,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,11,12,16,11,14,9,13],
[14,0,16,16,10,14,20,19,15,13,21],
[11,9,0,17,6,9,14,9,13,10,13],
[14,9,8,0,9,9,15,11,14,11,13],
[14,15,19,16,0,11,15,20,11,8,18],
[13,11,16,16,14,0,14,13,16,11,16],
[9,5,11,10,10,11,0,7,13,6,9],
[14,6,16,14,5,12,18,0,11,8,15],
[11,10,12,11,14,9,12,14,0,8,13],
[16,12,15,14,17,14,19,17,17,0,16],
[12,4,12,12,7,9,16,10,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,13,11,9,11,11,11,12,9],
[15,0,12,10,10,14,14,13,13,15,9],
[15,13,0,10,13,13,16,11,13,13,10],
[12,15,15,0,12,12,16,10,10,13,10],
[14,15,12,13,0,10,14,12,10,15,13],
[16,11,12,13,15,0,14,11,11,15,11],
[14,11,9,9,11,11,0,7,11,10,10],
[14,12,14,15,13,14,18,0,13,16,9],
[14,12,12,15,15,14,14,12,0,13,10],
[13,10,12,12,10,10,15,9,12,0,8],
[16,16,15,15,12,14,15,16,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,4,7,11,12,8,11,9],
[14,0,14,16,11,11,13,10,10,14,13],
[12,11,0,14,9,9,10,9,10,10,10],
[15,9,11,0,7,10,12,11,14,13,12],
[21,14,16,18,0,11,15,16,15,15,15],
[18,14,16,15,14,0,16,14,14,15,12],
[14,12,15,13,10,9,0,10,9,14,15],
[13,15,16,14,9,11,15,0,13,15,14],
[17,15,15,11,10,11,16,12,0,11,14],
[14,11,15,12,10,10,11,10,14,0,12],
[16,12,15,13,10,13,10,11,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,11,8,8,8,0,0,11,7],
[7,0,3,0,0,0,0,0,0,18,7],
[14,22,0,15,15,7,15,14,14,18,7],
[14,25,10,0,15,0,15,14,7,18,7],
[17,25,10,10,0,10,10,14,14,18,10],
[17,25,18,25,15,0,15,14,14,18,7],
[17,25,10,10,15,10,0,7,14,18,10],
[25,25,11,11,11,11,18,0,10,18,10],
[25,25,11,18,11,11,11,15,0,18,10],
[14,7,7,7,7,7,7,7,7,0,14],
[18,18,18,18,15,18,15,15,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,12,13,12,15,15,13,17,13],
[15,0,13,10,15,18,15,14,16,17,14],
[11,12,0,9,10,13,11,10,9,13,12],
[13,15,16,0,11,13,14,13,14,12,15],
[12,10,15,14,0,17,14,14,13,17,12],
[13,7,12,12,8,0,15,12,11,13,13],
[10,10,14,11,11,10,0,11,7,11,10],
[10,11,15,12,11,13,14,0,9,14,13],
[12,9,16,11,12,14,18,16,0,13,14],
[8,8,12,13,8,12,14,11,12,0,12],
[12,11,13,10,13,12,15,12,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,8,11,9,7,8,6,13,2],
[18,0,15,13,14,9,13,13,14,12,11],
[19,10,0,9,12,10,8,17,9,10,6],
[17,12,16,0,14,13,12,17,6,14,7],
[14,11,13,11,0,9,8,11,7,9,9],
[16,16,15,12,16,0,11,15,10,17,15],
[18,12,17,13,17,14,0,16,10,14,10],
[17,12,8,8,14,10,9,0,10,14,10],
[19,11,16,19,18,15,15,15,0,14,14],
[12,13,15,11,16,8,11,11,11,0,6],
[23,14,19,18,16,10,15,15,11,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,3,12,3,12,7,5,9,5],
[17,0,12,7,21,7,12,14,14,9,12],
[13,13,0,12,14,14,13,15,13,13,12],
[22,18,13,0,18,18,9,20,20,18,10],
[13,4,11,7,0,3,11,15,6,0,3],
[22,18,11,7,22,0,13,17,20,18,14],
[13,13,12,16,14,12,0,14,14,11,10],
[18,11,10,5,10,8,11,0,7,7,1],
[20,11,12,5,19,5,11,18,0,9,10],
[16,16,12,7,25,7,14,18,16,0,12],
[20,13,13,15,22,11,15,24,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,11,14,10,13,16,8,17,15],
[12,0,9,11,7,13,17,16,12,7,12],
[10,16,0,7,10,9,13,12,12,7,8],
[14,14,18,0,7,18,13,18,8,13,18],
[11,18,15,18,0,15,15,19,14,22,11],
[15,12,16,7,10,0,7,19,15,14,11],
[12,8,12,12,10,18,0,15,15,15,12],
[9,9,13,7,6,6,10,0,8,16,9],
[17,13,13,17,11,10,10,17,0,20,13],
[8,18,18,12,3,11,10,9,5,0,11],
[10,13,17,7,14,14,13,16,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,15,13,17,12,17,13,18,17],
[9,0,9,16,9,14,14,9,19,19,15],
[17,16,0,20,10,9,16,13,17,17,20],
[10,9,5,0,6,11,9,11,6,15,15],
[12,16,15,19,0,14,12,18,21,25,21],
[8,11,16,14,11,0,7,16,11,16,17],
[13,11,9,16,13,18,0,12,19,19,15],
[8,16,12,14,7,9,13,0,13,17,17],
[12,6,8,19,4,14,6,12,0,19,18],
[7,6,8,10,0,9,6,8,6,0,13],
[8,10,5,10,4,8,10,8,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,20,10,15,8,8,12,11,12,11],
[16,0,16,11,15,9,11,17,15,16,18],
[5,9,0,7,9,7,5,6,9,8,9],
[15,14,18,0,21,10,14,21,16,17,20],
[10,10,16,4,0,9,8,11,9,12,13],
[17,16,18,15,16,0,10,16,16,13,17],
[17,14,20,11,17,15,0,12,12,11,11],
[13,8,19,4,14,9,13,0,9,16,10],
[14,10,16,9,16,9,13,16,0,17,15],
[13,9,17,8,13,12,14,9,8,0,7],
[14,7,16,5,12,8,14,15,10,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,8,7,18,17,15,8,13,13],
[18,0,18,12,9,20,15,19,11,15,9],
[13,7,0,12,14,13,22,18,12,13,7],
[17,13,13,0,7,20,14,21,8,14,13],
[18,16,11,18,0,21,22,14,13,13,16],
[7,5,12,5,4,0,14,12,8,12,5],
[8,10,3,11,3,11,0,14,13,11,5],
[10,6,7,4,11,13,11,0,10,8,5],
[17,14,13,17,12,17,12,15,0,17,14],
[12,10,12,11,12,13,14,17,8,0,5],
[12,16,18,12,9,20,20,20,11,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,12,13,8,14,12,9,13,9],
[10,0,8,13,15,8,14,14,9,12,9],
[11,17,0,14,16,13,14,14,13,12,12],
[13,12,11,0,14,8,11,13,11,11,10],
[12,10,9,11,0,5,9,12,7,10,9],
[17,17,12,17,20,0,13,16,11,15,13],
[11,11,11,14,16,12,0,14,12,15,12],
[13,11,11,12,13,9,11,0,9,10,9],
[16,16,12,14,18,14,13,16,0,13,14],
[12,13,13,14,15,10,10,15,12,0,13],
[16,16,13,15,16,12,13,16,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,18,16,17,12,17,15,14,18],
[9,0,13,18,14,15,9,16,15,14,15],
[11,12,0,13,14,17,10,13,16,12,12],
[7,7,12,0,9,11,13,12,15,8,13],
[9,11,11,16,0,12,10,11,17,13,14],
[8,10,8,14,13,0,11,14,16,13,13],
[13,16,15,12,15,14,0,16,16,12,17],
[8,9,12,13,14,11,9,0,12,9,15],
[10,10,9,10,8,9,9,13,0,7,10],
[11,11,13,17,12,12,13,16,18,0,14],
[7,10,13,12,11,12,8,10,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,15,17,10,17,11,11,10,11,9],
[1,0,9,14,10,8,9,9,5,10,7],
[10,16,0,8,11,11,8,16,2,2,6],
[8,11,17,0,11,5,0,8,1,4,1],
[15,15,14,14,0,10,7,15,13,14,7],
[8,17,14,20,15,0,6,14,12,13,12],
[14,16,17,25,18,19,0,15,14,17,9],
[14,16,9,17,10,11,10,0,8,9,9],
[15,20,23,24,12,13,11,17,0,13,17],
[14,15,23,21,11,12,8,16,12,0,7],
[16,18,19,24,18,13,16,16,8,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,15,14,7,12,6,17,11,13],
[14,0,8,12,16,9,11,3,15,7,12],
[15,17,0,16,17,7,13,17,17,13,14],
[10,13,9,0,9,12,10,11,15,10,9],
[11,9,8,16,0,7,12,6,15,14,10],
[18,16,18,13,18,0,11,11,21,13,12],
[13,14,12,15,13,14,0,8,11,7,14],
[19,22,8,14,19,14,17,0,24,17,18],
[8,10,8,10,10,4,14,1,0,6,10],
[14,18,12,15,11,12,18,8,19,0,12],
[12,13,11,16,15,13,11,7,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,15,15,13,17,14,10,12,18],
[10,0,12,13,14,10,17,15,11,12,14],
[15,13,0,10,14,7,14,15,10,12,16],
[10,12,15,0,14,11,16,12,12,12,13],
[10,11,11,11,0,10,14,13,11,13,13],
[12,15,18,14,15,0,16,15,13,13,17],
[8,8,11,9,11,9,0,9,8,10,12],
[11,10,10,13,12,10,16,0,10,11,15],
[15,14,15,13,14,12,17,15,0,14,18],
[13,13,13,13,12,12,15,14,11,0,16],
[7,11,9,12,12,8,13,10,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,9,16,14,16,12,11,15,12],
[10,0,14,14,16,17,15,15,14,16,13],
[13,11,0,14,15,14,10,15,15,16,12],
[16,11,11,0,16,17,15,15,14,14,13],
[9,9,10,9,0,15,15,12,10,11,13],
[11,8,11,8,10,0,7,11,6,12,14],
[9,10,15,10,10,18,0,13,9,11,10],
[13,10,10,10,13,14,12,0,8,11,10],
[14,11,10,11,15,19,16,17,0,12,12],
[10,9,9,11,14,13,14,14,13,0,13],
[13,12,13,12,12,11,15,15,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,0,19,7,4,25,4,7,11],
[21,0,17,13,15,7,13,25,17,13,15],
[21,8,0,13,15,15,0,21,21,21,15],
[25,12,12,0,19,19,12,25,19,19,19],
[6,10,10,6,0,0,6,25,10,13,7],
[18,18,10,6,25,0,10,25,18,21,25],
[21,12,25,13,19,15,0,25,25,21,19],
[0,0,4,0,0,0,0,0,4,7,7],
[21,8,4,6,15,7,0,21,0,7,15],
[18,12,4,6,12,4,4,18,18,0,12],
[14,10,10,6,18,0,6,18,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,8,11,11,15,11,11,9,11],
[13,0,17,9,9,10,12,12,13,10,10],
[10,8,0,9,9,9,12,10,11,3,10],
[17,16,16,0,13,12,13,12,12,11,15],
[14,16,16,12,0,10,14,11,15,11,15],
[14,15,16,13,15,0,15,11,16,13,14],
[10,13,13,12,11,10,0,7,8,10,10],
[14,13,15,13,14,14,18,0,17,10,16],
[14,12,14,13,10,9,17,8,0,11,13],
[16,15,22,14,14,12,15,15,14,0,12],
[14,15,15,10,10,11,15,9,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,11,15,12,14,13,12,17,14],
[13,0,11,10,13,13,15,13,13,13,13],
[13,14,0,11,17,14,15,13,15,14,13],
[14,15,14,0,14,12,15,14,15,15,12],
[10,12,8,11,0,10,11,9,9,12,10],
[13,12,11,13,15,0,12,12,12,13,11],
[11,10,10,10,14,13,0,11,14,15,13],
[12,12,12,11,16,13,14,0,11,12,13],
[13,12,10,10,16,13,11,14,0,12,10],
[8,12,11,10,13,12,10,13,13,0,10],
[11,12,12,13,15,14,12,12,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,23,23,12,23,23,14,23,23],
[2,0,13,2,13,14,11,2,2,0,13],
[0,12,0,12,11,12,12,12,12,12,23],
[2,23,13,0,13,12,11,14,2,12,13],
[2,12,14,12,0,12,12,12,14,12,12],
[13,11,13,13,13,0,11,13,13,11,13],
[2,14,13,14,13,14,0,14,14,14,25],
[2,23,13,11,13,12,11,0,2,0,11],
[11,23,13,23,11,12,11,23,0,23,11],
[2,25,13,13,13,14,11,25,2,0,13],
[2,12,2,12,13,12,0,14,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,13,11,13,13,13,12,10,20],
[15,0,17,15,12,14,17,15,15,13,16],
[8,8,0,7,5,6,10,11,12,9,10],
[12,10,18,0,12,8,13,12,14,7,14],
[14,13,20,13,0,12,10,13,11,7,15],
[12,11,19,17,13,0,13,12,13,13,15],
[12,8,15,12,15,12,0,12,10,11,14],
[12,10,14,13,12,13,13,0,14,12,13],
[13,10,13,11,14,12,15,11,0,9,14],
[15,12,16,18,18,12,14,13,16,0,17],
[5,9,15,11,10,10,11,12,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,14,11,10,8,13,11,10,10],
[14,0,15,15,12,13,13,21,15,13,16],
[14,10,0,17,11,16,11,21,16,13,15],
[11,10,8,0,8,12,10,15,13,10,11],
[14,13,14,17,0,16,13,18,17,14,12],
[15,12,9,13,9,0,17,17,10,10,11],
[17,12,14,15,12,8,0,22,8,10,16],
[12,4,4,10,7,8,3,0,7,11,12],
[14,10,9,12,8,15,17,18,0,13,14],
[15,12,12,15,11,15,15,14,12,0,18],
[15,9,10,14,13,14,9,13,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,9,10,13,6,10,16,15,9],
[7,0,7,10,10,6,6,10,15,11,9],
[14,18,0,18,12,6,9,15,9,18,9],
[16,15,7,0,9,10,9,9,13,14,10],
[15,15,13,16,0,15,12,15,18,14,16],
[12,19,19,15,10,0,9,16,17,18,10],
[19,19,16,16,13,16,0,19,19,19,10],
[15,15,10,16,10,9,6,0,15,18,15],
[9,10,16,12,7,8,6,10,0,17,7],
[10,14,7,11,11,7,6,7,8,0,8],
[16,16,16,15,9,15,15,10,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,10,17,13,2,5,10,19,5],
[13,0,22,20,17,10,13,13,10,17,10],
[10,3,0,7,17,10,10,0,10,17,0],
[15,5,18,0,10,13,15,15,10,12,12],
[8,8,8,15,0,5,5,5,3,9,5],
[12,15,15,12,20,0,5,12,7,9,9],
[23,12,15,10,20,20,0,15,20,22,10],
[20,12,25,10,20,13,10,0,13,20,13],
[15,15,15,15,22,18,5,12,0,19,12],
[6,8,8,13,16,16,3,5,6,0,3],
[20,15,25,13,20,16,15,12,13,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,11,13,1,4,2,7,7],
[20,0,16,12,17,18,7,15,11,13,16],
[21,9,0,13,13,19,7,17,11,8,11],
[21,13,12,0,15,20,0,14,9,15,13],
[14,8,12,10,0,18,8,15,10,13,5],
[12,7,6,5,7,0,1,9,2,2,4],
[24,18,18,25,17,24,0,19,10,16,14],
[21,10,8,11,10,16,6,0,5,10,9],
[23,14,14,16,15,23,15,20,0,8,15],
[18,12,17,10,12,23,9,15,17,0,10],
[18,9,14,12,20,21,11,16,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,10,9,10,12,9,11,9,10],
[13,0,14,12,12,15,17,15,13,11,13],
[11,11,0,11,10,12,18,15,12,11,14],
[15,13,14,0,11,13,15,15,12,7,13],
[16,13,15,14,0,17,15,17,13,10,17],
[15,10,13,12,8,0,15,15,13,9,15],
[13,8,7,10,10,10,0,13,12,7,11],
[16,10,10,10,8,10,12,0,15,8,13],
[14,12,13,13,12,12,13,10,0,13,12],
[16,14,14,18,15,16,18,17,12,0,18],
[15,12,11,12,8,10,14,12,13,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,7,7,13,12,16,15,14,10],
[12,0,13,10,10,11,15,12,13,11,8],
[15,12,0,11,10,15,12,13,12,12,11],
[18,15,14,0,13,17,18,17,15,14,11],
[18,15,15,12,0,20,18,18,17,15,13],
[12,14,10,8,5,0,11,14,12,9,6],
[13,10,13,7,7,14,0,14,11,12,9],
[9,13,12,8,7,11,11,0,12,13,10],
[10,12,13,10,8,13,14,13,0,6,9],
[11,14,13,11,10,16,13,12,19,0,8],
[15,17,14,14,12,19,16,15,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,16,14,18,16,14,15,11,11],
[11,0,13,10,16,13,15,12,15,9,15],
[11,12,0,12,10,16,13,8,15,17,12],
[9,15,13,0,15,17,14,16,15,12,16],
[11,9,15,10,0,16,16,12,18,9,15],
[7,12,9,8,9,0,17,9,15,7,14],
[9,10,12,11,9,8,0,9,13,9,13],
[11,13,17,9,13,16,16,0,15,11,14],
[10,10,10,10,7,10,12,10,0,7,13],
[14,16,8,13,16,18,16,14,18,0,14],
[14,10,13,9,10,11,12,11,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,11,10,14,13,15,12,16,15],
[12,0,9,10,11,12,12,19,15,12,16],
[15,16,0,15,15,17,22,17,11,15,13],
[14,15,10,0,11,18,18,16,8,15,13],
[15,14,10,14,0,16,17,20,13,16,16],
[11,13,8,7,9,0,7,12,13,15,12],
[12,13,3,7,8,18,0,14,11,16,12],
[10,6,8,9,5,13,11,0,8,13,13],
[13,10,14,17,12,12,14,17,0,16,13],
[9,13,10,10,9,10,9,12,9,0,15],
[10,9,12,12,9,13,13,12,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,7,17,11,16,6,14,9,10,12],
[14,0,12,15,6,13,10,9,8,8,16],
[18,13,0,20,12,14,12,9,3,10,17],
[8,10,5,0,6,10,4,9,3,8,10],
[14,19,13,19,0,13,13,12,13,18,13],
[9,12,11,15,12,0,7,14,6,8,15],
[19,15,13,21,12,18,0,17,7,9,13],
[11,16,16,16,13,11,8,0,9,10,15],
[16,17,22,22,12,19,18,16,0,15,21],
[15,17,15,17,7,17,16,15,10,0,17],
[13,9,8,15,12,10,12,10,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,15,16,7,14,17,14,17,18],
[9,0,9,8,11,13,13,10,13,14,15],
[14,16,0,11,14,13,19,20,17,18,22],
[10,17,14,0,19,10,15,15,17,20,18],
[9,14,11,6,0,11,14,15,16,17,15],
[18,12,12,15,14,0,14,15,16,17,22],
[11,12,6,10,11,11,0,10,17,8,18],
[8,15,5,10,10,10,15,0,17,10,20],
[11,12,8,8,9,9,8,8,0,13,22],
[8,11,7,5,8,8,17,15,12,0,16],
[7,10,3,7,10,3,7,5,3,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,6,11,5,8,9,19,11,6,12],
[15,0,5,6,7,15,7,23,16,1,12],
[19,20,0,11,18,19,15,23,15,12,16],
[14,19,14,0,11,14,7,17,11,8,11],
[20,18,7,14,0,22,11,23,13,7,16],
[17,10,6,11,3,0,9,24,12,6,12],
[16,18,10,18,14,16,0,22,13,17,22],
[6,2,2,8,2,1,3,0,2,2,7],
[14,9,10,14,12,13,12,23,0,6,12],
[19,24,13,17,18,19,8,23,19,0,23],
[13,13,9,14,9,13,3,18,13,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,14,18,20,14,7,7,11,10],
[13,0,14,16,17,17,10,14,12,16,13],
[12,11,0,10,16,14,10,7,8,12,8],
[11,9,15,0,13,14,11,9,9,9,10],
[7,8,9,12,0,9,8,5,7,9,4],
[5,8,11,11,16,0,8,7,8,12,4],
[11,15,15,14,17,17,0,11,10,15,10],
[18,11,18,16,20,18,14,0,13,13,14],
[18,13,17,16,18,17,15,12,0,14,16],
[14,9,13,16,16,13,10,12,11,0,10],
[15,12,17,15,21,21,15,11,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,11,8,9,9,10,9,14,12],
[13,0,12,12,10,11,11,7,10,12,13],
[14,13,0,13,12,14,13,9,12,16,14],
[14,13,12,0,14,14,13,12,12,18,16],
[17,15,13,11,0,13,11,8,14,18,13],
[16,14,11,11,12,0,12,10,12,15,13],
[16,14,12,12,14,13,0,14,12,16,15],
[15,18,16,13,17,15,11,0,14,18,16],
[16,15,13,13,11,13,13,11,0,19,16],
[11,13,9,7,7,10,9,7,6,0,10],
[13,12,11,9,12,12,10,9,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,1,17,19,13,22,9,20,3,3],
[15,0,11,16,18,15,24,15,22,17,13],
[24,14,0,16,21,19,22,12,20,21,10],
[8,9,9,0,19,8,22,9,16,11,11],
[6,7,4,6,0,12,14,12,4,6,2],
[12,10,6,17,13,0,14,4,10,10,3],
[3,1,3,3,11,11,0,11,4,3,3],
[16,10,13,16,13,21,14,0,14,9,10],
[5,3,5,9,21,15,21,11,0,2,5],
[22,8,4,14,19,15,22,16,23,0,4],
[22,12,15,14,23,22,22,15,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,16,14,21,12,15,15,11,17],
[13,0,14,13,15,17,12,15,13,20,14],
[8,11,0,9,16,16,12,7,18,12,14],
[9,12,16,0,19,12,12,18,13,16,17],
[11,10,9,6,0,12,9,9,10,11,9],
[4,8,9,13,13,0,10,10,14,8,10],
[13,13,13,13,16,15,0,13,15,12,17],
[10,10,18,7,16,15,12,0,16,8,14],
[10,12,7,12,15,11,10,9,0,12,11],
[14,5,13,9,14,17,13,17,13,0,15],
[8,11,11,8,16,15,8,11,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,15,19,15,19,15,19,16,9],
[6,0,0,6,12,6,10,12,6,6,6],
[6,25,0,12,16,21,22,18,25,22,15],
[10,19,13,0,13,13,13,19,13,16,13],
[6,13,9,12,0,15,19,18,19,16,15],
[10,19,4,12,10,0,10,16,10,10,9],
[6,15,3,12,6,15,0,12,9,12,9],
[10,13,7,6,7,9,13,0,7,10,3],
[6,19,0,12,6,15,16,18,0,12,9],
[9,19,3,9,9,15,13,15,13,0,15],
[16,19,10,12,10,16,16,22,16,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,5,8,13,5,7,15,15,2,2],
[23,0,16,12,21,10,18,16,20,13,13],
[20,9,0,14,14,8,9,18,16,2,9],
[17,13,11,0,20,11,15,10,15,9,12],
[12,4,11,5,0,4,6,4,13,6,6],
[20,15,17,14,21,0,15,12,15,9,8],
[18,7,16,10,19,10,0,16,20,6,13],
[10,9,7,15,21,13,9,0,10,9,10],
[10,5,9,10,12,10,5,15,0,2,11],
[23,12,23,16,19,16,19,16,23,0,18],
[23,12,16,13,19,17,12,15,14,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,14,11,14,11,7,21,25,11],
[11,0,11,14,15,7,15,4,7,18,15],
[7,14,0,14,11,14,7,7,21,25,7],
[11,11,11,0,8,4,15,4,18,22,4],
[14,10,14,17,0,7,7,3,17,17,7],
[11,18,11,21,18,0,18,14,21,25,18],
[14,10,18,10,18,7,0,7,17,21,14],
[18,21,18,21,22,11,18,0,21,21,18],
[4,18,4,7,8,4,8,4,0,25,8],
[0,7,0,3,8,0,4,4,0,0,0],
[14,10,18,21,18,7,11,7,17,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,14,12,16,14,16,12,18,18],
[9,0,12,8,12,12,14,17,11,19,19],
[14,13,0,11,15,14,16,17,10,14,18],
[11,17,14,0,15,14,17,23,14,18,21],
[13,13,10,10,0,12,14,18,9,16,18],
[9,13,11,11,13,0,14,17,12,15,16],
[11,11,9,8,11,11,0,16,11,16,16],
[9,8,8,2,7,8,9,0,7,15,17],
[13,14,15,11,16,13,14,18,0,16,20],
[7,6,11,7,9,10,9,10,9,0,12],
[7,6,7,4,7,9,9,8,5,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,12,11,12,12,12,12,11,14],
[15,0,16,14,13,12,13,10,13,11,10],
[11,9,0,9,7,10,6,6,8,9,12],
[13,11,16,0,13,10,10,12,7,12,11],
[14,12,18,12,0,13,9,13,11,10,13],
[13,13,15,15,12,0,10,11,13,8,9],
[13,12,19,15,16,15,0,13,13,15,16],
[13,15,19,13,12,14,12,0,11,17,16],
[13,12,17,18,14,12,12,14,0,13,13],
[14,14,16,13,15,17,10,8,12,0,15],
[11,15,13,14,12,16,9,9,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,14,15,16,15,12,18,12],
[12,0,16,9,13,14,13,16,11,14,14],
[12,9,0,11,12,11,15,17,12,15,13],
[13,16,14,0,13,13,14,14,12,15,15],
[11,12,13,12,0,13,16,16,12,14,13],
[10,11,14,12,12,0,13,18,11,13,9],
[9,12,10,11,9,12,0,20,15,12,11],
[10,9,8,11,9,7,5,0,6,13,9],
[13,14,13,13,13,14,10,19,0,14,16],
[7,11,10,10,11,12,13,12,11,0,11],
[13,11,12,10,12,16,14,16,9,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,20,16,8,16,20,16,8,20,13],
[9,0,12,17,9,12,17,25,9,25,9],
[5,13,0,13,5,8,13,21,5,25,13],
[9,8,12,0,5,20,17,20,17,25,9],
[17,16,20,20,0,20,17,20,12,25,17],
[9,13,17,5,5,0,17,13,5,25,5],
[5,8,12,8,8,8,0,16,0,12,13],
[9,0,4,5,5,12,9,0,9,17,5],
[17,16,20,8,13,20,25,16,0,25,13],
[5,0,0,0,0,0,13,8,0,0,5],
[12,16,12,16,8,20,12,20,12,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,15,11,8,10,17,15,8,8],
[16,0,11,13,11,3,8,9,16,11,5],
[10,14,0,10,10,2,10,10,10,3,4],
[10,12,15,0,12,4,7,15,10,5,6],
[14,14,15,13,0,13,8,16,15,16,16],
[17,22,23,21,12,0,16,20,17,17,23],
[15,17,15,18,17,9,0,16,15,15,10],
[8,16,15,10,9,5,9,0,9,11,9],
[10,9,15,15,10,8,10,16,0,9,12],
[17,14,22,20,9,8,10,14,16,0,12],
[17,20,21,19,9,2,15,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,20,16,9,11,13,14,14,11],
[11,0,5,14,16,8,5,13,8,11,11],
[12,20,0,15,16,15,11,19,17,17,17],
[5,11,10,0,13,5,5,10,5,11,8],
[9,9,9,12,0,12,11,17,14,15,12],
[16,17,10,20,13,0,16,13,19,16,16],
[14,20,14,20,14,9,0,14,25,14,14],
[12,12,6,15,8,12,11,0,17,11,15],
[11,17,8,20,11,6,0,8,0,11,11],
[11,14,8,14,10,9,11,14,14,0,9],
[14,14,8,17,13,9,11,10,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,14,17,9,14,12,11,11,18],
[14,0,12,19,15,15,16,14,10,16,21],
[14,13,0,15,14,12,16,14,13,15,19],
[11,6,10,0,14,12,14,10,6,10,12],
[8,10,11,11,0,10,13,9,8,13,15],
[16,10,13,13,15,0,14,12,8,11,18],
[11,9,9,11,12,11,0,11,10,11,16],
[13,11,11,15,16,13,14,0,11,12,22],
[14,15,12,19,17,17,15,14,0,15,20],
[14,9,10,15,12,14,14,13,10,0,17],
[7,4,6,13,10,7,9,3,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,14,8,15,15,12,18,21,12],
[9,0,13,11,6,11,14,7,16,14,11],
[9,12,0,14,13,12,14,12,17,17,13],
[11,14,11,0,11,10,12,13,16,17,12],
[17,19,12,14,0,17,15,12,22,18,15],
[10,14,13,15,8,0,11,11,15,15,14],
[10,11,11,13,10,14,0,12,15,15,12],
[13,18,13,12,13,14,13,0,17,17,15],
[7,9,8,9,3,10,10,8,0,9,9],
[4,11,8,8,7,10,10,8,16,0,15],
[13,14,12,13,10,11,13,10,16,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,24,13,25,24,19,14,25,14],
[9,0,11,16,13,11,19,19,11,13,4],
[15,14,0,22,12,17,22,19,14,19,7],
[1,9,3,0,12,16,13,18,14,15,3],
[12,12,13,13,0,14,16,22,12,14,12],
[0,14,8,9,11,0,17,18,11,18,0],
[1,6,3,12,9,8,0,12,12,15,6],
[6,6,6,7,3,7,13,0,3,13,6],
[11,14,11,11,13,14,13,22,0,11,4],
[0,12,6,10,11,7,10,12,14,0,0],
[11,21,18,22,13,25,19,19,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,11,10,9,10,12,12,9,13],
[17,0,17,15,15,14,13,16,12,13,19],
[11,8,0,10,10,9,8,14,11,8,12],
[14,10,15,0,11,8,10,12,11,13,16],
[15,10,15,14,0,10,7,11,13,16,16],
[16,11,16,17,15,0,9,10,14,14,18],
[15,12,17,15,18,16,0,16,18,17,18],
[13,9,11,13,14,15,9,0,12,9,15],
[13,13,14,14,12,11,7,13,0,14,17],
[16,12,17,12,9,11,8,16,11,0,15],
[12,6,13,9,9,7,7,10,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,22,16,19,15,13,17,19,14],
[10,0,10,12,12,14,10,13,16,14,11],
[13,15,0,18,17,15,15,11,13,17,13],
[3,13,7,0,13,15,9,13,17,12,13],
[9,13,8,12,0,11,8,11,13,9,4],
[6,11,10,10,14,0,8,11,14,12,13],
[10,15,10,16,17,17,0,12,12,10,15],
[12,12,14,12,14,14,13,0,12,15,11],
[8,9,12,8,12,11,13,13,0,11,12],
[6,11,8,13,16,13,15,10,14,0,11],
[11,14,12,12,21,12,10,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,16,14,15,15,10,16,12,17],
[10,0,9,10,11,12,6,10,15,13,10],
[11,16,0,14,17,11,11,13,17,18,13],
[9,15,11,0,13,12,8,14,13,15,14],
[11,14,8,12,0,14,8,12,14,12,14],
[10,13,14,13,11,0,13,13,16,13,13],
[10,19,14,17,17,12,0,15,16,19,18],
[15,15,12,11,13,12,10,0,12,17,15],
[9,10,8,12,11,9,9,13,0,14,8],
[13,12,7,10,13,12,6,8,11,0,12],
[8,15,12,11,11,12,7,10,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,20,9,2,9,9,14,9,15,9],
[16,0,16,18,11,25,13,5,11,11,18],
[5,9,0,7,0,9,7,14,2,8,7],
[16,7,18,0,5,7,0,7,7,13,7],
[23,14,25,20,0,14,12,19,14,20,14],
[16,0,16,18,11,0,0,5,5,11,5],
[16,12,18,25,13,25,0,12,18,18,13],
[11,20,11,18,6,20,13,0,11,11,18],
[16,14,23,18,11,20,7,14,0,11,13],
[10,14,17,12,5,14,7,14,14,0,12],
[16,7,18,18,11,20,12,7,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,12,15,15,13,11,11,10,15],
[10,0,5,10,13,11,10,11,11,6,15],
[15,20,0,14,18,17,12,13,16,10,20],
[13,15,11,0,17,15,11,12,13,11,11],
[10,12,7,8,0,11,6,10,9,8,14],
[10,14,8,10,14,0,13,11,10,9,15],
[12,15,13,14,19,12,0,13,14,11,16],
[14,14,12,13,15,14,12,0,12,12,13],
[14,14,9,12,16,15,11,13,0,14,19],
[15,19,15,14,17,16,14,13,11,0,18],
[10,10,5,14,11,10,9,12,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,8,8,1,18,16,18,11,11],
[16,0,10,9,9,8,18,16,19,3,8],
[15,15,0,8,16,2,15,15,15,8,15],
[17,16,17,0,14,3,18,15,19,12,11],
[17,16,9,11,0,10,23,24,18,17,11],
[24,17,23,22,15,0,18,16,25,12,17],
[7,7,10,7,2,7,0,7,8,7,1],
[9,9,10,10,1,9,18,0,18,10,11],
[7,6,10,6,7,0,17,7,0,7,0],
[14,22,17,13,8,13,18,15,18,0,8],
[14,17,10,14,14,8,24,14,25,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,5,9,5,9,5,14,15,8],
[9,0,2,5,7,7,8,7,6,10,1],
[17,23,0,12,11,9,9,5,11,10,12],
[20,20,13,0,11,5,12,5,17,17,8],
[16,18,14,14,0,16,8,15,13,15,11],
[20,18,16,20,9,0,15,14,20,17,14],
[16,17,16,13,17,10,0,17,21,17,11],
[20,18,20,20,10,11,8,0,13,17,15],
[11,19,14,8,12,5,4,12,0,8,15],
[10,15,15,8,10,8,8,8,17,0,11],
[17,24,13,17,14,11,14,10,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,19,13,9,19,10,11,15,14],
[13,0,14,12,14,8,11,5,12,12,12],
[11,11,0,11,8,6,13,11,10,11,7],
[6,13,14,0,18,12,15,13,12,9,16],
[12,11,17,7,0,8,13,10,8,7,6],
[16,17,19,13,17,0,14,15,12,14,14],
[6,14,12,10,12,11,0,11,11,9,14],
[15,20,14,12,15,10,14,0,14,13,16],
[14,13,15,13,17,13,14,11,0,13,13],
[10,13,14,16,18,11,16,12,12,0,13],
[11,13,18,9,19,11,11,9,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,18,14,14,15,14,17,11,10],
[8,0,11,13,6,11,7,6,12,9,11],
[10,14,0,11,12,15,10,9,14,9,9],
[7,12,14,0,10,13,11,7,9,10,8],
[11,19,13,15,0,15,10,8,15,10,10],
[11,14,10,12,10,0,11,10,14,11,9],
[10,18,15,14,15,14,0,9,17,12,12],
[11,19,16,18,17,15,16,0,16,17,12],
[8,13,11,16,10,11,8,9,0,8,8],
[14,16,16,15,15,14,13,8,17,0,14],
[15,14,16,17,15,16,13,13,17,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,10,19,16,13,14,13,12,14],
[9,0,9,10,14,11,14,10,9,12,7],
[13,16,0,15,17,19,12,15,16,13,13],
[15,15,10,0,16,14,13,10,12,13,9],
[6,11,8,9,0,11,9,7,7,6,5],
[9,14,6,11,14,0,11,9,9,8,9],
[12,11,13,12,16,14,0,13,13,11,12],
[11,15,10,15,18,16,12,0,10,12,10],
[12,16,9,13,18,16,12,15,0,12,13],
[13,13,12,12,19,17,14,13,13,0,13],
[11,18,12,16,20,16,13,15,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,12,16,16,16,10,12,13,13],
[13,0,14,13,14,12,17,12,10,10,11],
[12,11,0,10,14,13,15,12,10,9,13],
[13,12,15,0,13,15,13,10,12,8,12],
[9,11,11,12,0,15,13,10,7,9,9],
[9,13,12,10,10,0,14,10,9,10,10],
[9,8,10,12,12,11,0,12,7,8,8],
[15,13,13,15,15,15,13,0,10,10,10],
[13,15,15,13,18,16,18,15,0,13,11],
[12,15,16,17,16,15,17,15,12,0,11],
[12,14,12,13,16,15,17,15,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,23,25,17,12,17,17,17,17],
[8,0,14,19,13,15,19,10,19,14,12],
[13,11,0,24,19,18,17,11,12,18,17],
[2,6,1,0,7,2,8,2,1,3,7],
[0,12,6,18,0,12,6,7,6,12,12],
[8,10,7,23,13,0,7,6,12,18,16],
[13,6,8,17,19,18,0,12,7,13,17],
[8,15,14,23,18,19,13,0,17,24,22],
[8,6,13,24,19,13,18,8,0,14,12],
[8,11,7,22,13,7,12,1,11,0,17],
[8,13,8,18,13,9,8,3,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,11,11,20,18,2,11,11,16],
[5,0,14,16,14,9,9,5,7,16,14],
[5,11,0,2,2,2,0,2,16,11,7],
[14,9,23,0,23,9,9,14,16,18,23],
[14,11,23,2,0,11,9,11,16,11,14],
[5,16,23,16,14,0,18,5,16,16,14],
[7,16,25,16,16,7,0,7,16,16,16],
[23,20,23,11,14,20,18,0,16,11,14],
[14,18,9,9,9,9,9,9,0,9,14],
[14,9,14,7,14,9,9,14,16,0,5],
[9,11,18,2,11,11,9,11,11,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,16,12,14,14,14,14,15,14],
[13,0,12,15,14,15,14,14,15,19,15],
[12,13,0,14,12,15,14,12,15,20,16],
[9,10,11,0,10,12,11,13,11,14,13],
[13,11,13,15,0,15,13,14,14,20,17],
[11,10,10,13,10,0,14,14,13,17,10],
[11,11,11,14,12,11,0,8,9,14,12],
[11,11,13,12,11,11,17,0,13,17,14],
[11,10,10,14,11,12,16,12,0,14,13],
[10,6,5,11,5,8,11,8,11,0,8],
[11,10,9,12,8,15,13,11,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,13,13,15,9,11,17,13,16],
[8,0,7,12,8,11,6,10,13,14,12],
[12,18,0,15,16,14,13,14,16,15,18],
[12,13,10,0,12,10,7,11,16,12,17],
[12,17,9,13,0,14,7,9,13,15,12],
[10,14,11,15,11,0,9,12,17,13,14],
[16,19,12,18,18,16,0,19,19,17,18],
[14,15,11,14,16,13,6,0,13,15,17],
[8,12,9,9,12,8,6,12,0,9,17],
[12,11,10,13,10,12,8,10,16,0,15],
[9,13,7,8,13,11,7,8,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,17,12,15,18,10,15,21,14],
[12,0,11,17,14,19,19,10,12,18,14],
[11,14,0,16,16,17,18,8,13,18,15],
[8,8,9,0,14,9,10,7,13,19,12],
[13,11,9,11,0,14,13,6,9,16,8],
[10,6,8,16,11,0,16,8,9,20,9],
[7,6,7,15,12,9,0,11,12,15,10],
[15,15,17,18,19,17,14,0,14,17,12],
[10,13,12,12,16,16,13,11,0,16,16],
[4,7,7,6,9,5,10,8,9,0,9],
[11,11,10,13,17,16,15,13,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,9,7,9,13,10,9,7,15],
[17,0,17,11,16,15,16,16,16,14,18],
[12,8,0,5,11,9,11,9,7,8,15],
[16,14,20,0,12,14,12,16,16,13,17],
[18,9,14,13,0,15,13,16,16,13,18],
[16,10,16,11,10,0,14,13,12,12,17],
[12,9,14,13,12,11,0,14,12,12,14],
[15,9,16,9,9,12,11,0,14,13,16],
[16,9,18,9,9,13,13,11,0,8,16],
[18,11,17,12,12,13,13,12,17,0,19],
[10,7,10,8,7,8,11,9,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,18,14,16,13,14,12,17,12],
[9,0,7,9,10,12,9,11,8,7,12],
[10,18,0,15,14,15,15,10,12,14,17],
[7,16,10,0,11,7,10,8,8,7,7],
[11,15,11,14,0,8,8,10,8,7,12],
[9,13,10,18,17,0,13,8,13,11,13],
[12,16,10,15,17,12,0,14,11,11,12],
[11,14,15,17,15,17,11,0,12,13,11],
[13,17,13,17,17,12,14,13,0,14,13],
[8,18,11,18,18,14,14,12,11,0,9],
[13,13,8,18,13,12,13,14,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,9,15,15,20,16,18,14,15,8],
[8,0,9,9,9,14,10,15,11,9,0],
[16,16,0,19,16,11,10,16,21,16,15],
[10,16,6,0,4,11,16,9,18,16,0],
[10,16,9,21,0,16,16,17,18,16,7],
[5,11,14,14,9,0,14,14,11,14,5],
[9,15,15,9,9,11,0,15,14,9,9],
[7,10,9,16,8,11,10,0,18,10,7],
[11,14,4,7,7,14,11,7,0,14,4],
[10,16,9,9,9,11,16,15,11,0,0],
[17,25,10,25,18,20,16,18,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,13,14,16,12,15,16,15,14],
[13,0,19,14,17,14,11,14,14,9,18],
[6,6,0,9,14,8,7,11,11,8,10],
[12,11,16,0,12,15,8,16,15,9,16],
[11,8,11,13,0,13,9,12,14,10,12],
[9,11,17,10,12,0,9,13,13,8,17],
[13,14,18,17,16,16,0,12,17,13,15],
[10,11,14,9,13,12,13,0,11,11,9],
[9,11,14,10,11,12,8,14,0,10,15],
[10,16,17,16,15,17,12,14,15,0,16],
[11,7,15,9,13,8,10,16,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,9,13,11,12,13,14,14],
[14,0,14,13,14,11,12,13,14,9,14],
[12,11,0,9,11,10,11,15,16,13,13],
[13,12,16,0,16,13,17,13,14,14,16],
[16,11,14,9,0,13,9,12,12,11,12],
[12,14,15,12,12,0,16,13,13,15,16],
[14,13,14,8,16,9,0,14,15,15,11],
[13,12,10,12,13,12,11,0,13,10,13],
[12,11,9,11,13,12,10,12,0,13,13],
[11,16,12,11,14,10,10,15,12,0,13],
[11,11,12,9,13,9,14,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,9,9,0,0,0,5,11,9,0],
[25,0,14,9,16,16,0,14,20,25,11],
[16,11,0,20,16,11,11,16,11,20,11],
[16,16,5,0,16,16,5,16,11,16,16],
[25,9,9,9,0,0,9,14,20,9,0],
[25,9,14,9,25,0,9,14,20,20,0],
[25,25,14,20,16,16,0,25,20,25,11],
[20,11,9,9,11,11,0,0,20,20,11],
[14,5,14,14,5,5,5,5,0,14,5],
[16,0,5,9,16,5,0,5,11,0,0],
[25,14,14,9,25,25,14,14,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,15,13,12,13,10,16,11,18],
[15,0,18,14,12,11,12,13,10,13,14],
[10,7,0,7,7,6,7,6,7,7,10],
[10,11,18,0,11,9,10,7,5,9,12],
[12,13,18,14,0,16,15,13,19,13,21],
[13,14,19,16,9,0,15,7,14,11,13],
[12,13,18,15,10,10,0,10,13,10,11],
[15,12,19,18,12,18,15,0,17,13,18],
[9,15,18,20,6,11,12,8,0,12,13],
[14,12,18,16,12,14,15,12,13,0,17],
[7,11,15,13,4,12,14,7,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,12,16,17,16,12,18,14,12],
[12,0,10,11,17,14,10,12,18,12,8],
[9,15,0,14,17,14,16,10,19,12,11],
[13,14,11,0,16,14,16,11,18,13,12],
[9,8,8,9,0,11,10,11,13,14,7],
[8,11,11,11,14,0,12,8,12,9,10],
[9,15,9,9,15,13,0,13,14,17,11],
[13,13,15,14,14,17,12,0,15,14,15],
[7,7,6,7,12,13,11,10,0,8,5],
[11,13,13,12,11,16,8,11,17,0,12],
[13,17,14,13,18,15,14,10,20,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,14,10,9,10,13,8,11,11],
[13,0,11,8,6,3,6,7,1,10,8],
[13,14,0,16,11,12,10,14,10,13,12],
[11,17,9,0,11,11,9,10,11,12,12],
[15,19,14,14,0,17,10,14,11,15,15],
[16,22,13,14,8,0,12,15,6,15,11],
[15,19,15,16,15,13,0,11,13,18,14],
[12,18,11,15,11,10,14,0,10,13,11],
[17,24,15,14,14,19,12,15,0,17,20],
[14,15,12,13,10,10,7,12,8,0,11],
[14,17,13,13,10,14,11,14,5,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,11,12,9,7,17,8,7,6],
[13,0,12,14,12,12,12,15,14,15,10],
[16,13,0,21,16,15,14,19,16,17,10],
[14,11,4,0,15,10,11,16,17,12,10],
[13,13,9,10,0,8,10,13,13,9,8],
[16,13,10,15,17,0,13,18,18,16,12],
[18,13,11,14,15,12,0,20,13,13,13],
[8,10,6,9,12,7,5,0,8,9,4],
[17,11,9,8,12,7,12,17,0,8,13],
[18,10,8,13,16,9,12,16,17,0,12],
[19,15,15,15,17,13,12,21,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,9,13,10,11,13,11,11,15],
[15,0,18,15,17,11,18,15,15,15,14],
[15,7,0,13,13,11,13,11,13,13,14],
[16,10,12,0,11,11,18,13,9,12,11],
[12,8,12,14,0,9,16,11,10,14,13],
[15,14,14,14,16,0,12,13,11,14,15],
[14,7,12,7,9,13,0,13,9,8,14],
[12,10,14,12,14,12,12,0,11,12,12],
[14,10,12,16,15,14,16,14,0,15,13],
[14,10,12,13,11,11,17,13,10,0,12],
[10,11,11,14,12,10,11,13,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,11,14,12,3,9,16,11,7,8],
[20,0,11,14,10,12,4,21,19,11,8],
[14,14,0,16,17,14,14,14,13,10,13],
[11,11,9,0,10,11,14,14,14,10,9],
[13,15,8,15,0,13,18,18,12,9,9],
[22,13,11,14,12,0,9,13,11,9,16],
[16,21,11,11,7,16,0,21,16,8,8],
[9,4,11,11,7,12,4,0,8,4,8],
[14,6,12,11,13,14,9,17,0,12,13],
[18,14,15,15,16,16,17,21,13,0,11],
[17,17,12,16,16,9,17,17,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,11,12,8,8,8,14,12,9],
[17,0,8,12,14,11,11,12,13,10,10],
[15,17,0,16,17,12,12,11,16,10,12],
[14,13,9,0,13,10,11,13,17,11,7],
[13,11,8,12,0,8,12,11,16,12,10],
[17,14,13,15,17,0,15,17,16,12,13],
[17,14,13,14,13,10,0,15,14,15,11],
[17,13,14,12,14,8,10,0,16,12,9],
[11,12,9,8,9,9,11,9,0,4,7],
[13,15,15,14,13,13,10,13,21,0,9],
[16,15,13,18,15,12,14,16,18,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,9,10,9,8,13,10,8,7],
[14,0,7,12,9,8,11,10,8,10,6],
[19,18,0,17,15,15,13,14,13,10,10],
[16,13,8,0,11,10,11,13,8,5,7],
[15,16,10,14,0,5,10,8,10,2,9],
[16,17,10,15,20,0,13,13,12,8,13],
[17,14,12,14,15,12,0,12,15,10,15],
[12,15,11,12,17,12,13,0,11,7,14],
[15,17,12,17,15,13,10,14,0,12,9],
[17,15,15,20,23,17,15,18,13,0,12],
[18,19,15,18,16,12,10,11,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,3,7,13,5,10,8,5,10],
[17,0,9,6,9,21,14,13,16,17,13],
[20,16,0,18,14,21,16,11,19,17,12],
[22,19,7,0,13,21,10,11,17,16,15],
[18,16,11,12,0,21,15,12,18,19,15],
[12,4,4,4,4,0,7,10,8,5,7],
[20,11,9,15,10,18,0,11,12,18,11],
[15,12,14,14,13,15,14,0,18,16,13],
[17,9,6,8,7,17,13,7,0,10,10],
[20,8,8,9,6,20,7,9,15,0,11],
[15,12,13,10,10,18,14,12,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,13,12,10,8,7,13,5,5],
[18,0,16,12,16,17,17,14,15,15,10],
[14,9,0,13,13,11,14,7,11,12,11],
[12,13,12,0,12,15,10,10,12,13,12],
[13,9,12,13,0,12,11,8,8,10,13],
[15,8,14,10,13,0,7,9,10,8,10],
[17,8,11,15,14,18,0,9,11,14,10],
[18,11,18,15,17,16,16,0,16,16,13],
[12,10,14,13,17,15,14,9,0,12,9],
[20,10,13,12,15,17,11,9,13,0,13],
[20,15,14,13,12,15,15,12,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,12,12,16,13,11,16,12,11],
[13,0,11,11,11,17,9,12,17,12,14],
[9,14,0,10,12,13,11,10,10,15,15],
[13,14,15,0,11,14,8,8,15,12,10],
[13,14,13,14,0,15,10,11,13,15,15],
[9,8,12,11,10,0,9,13,11,14,14],
[12,16,14,17,15,16,0,16,17,14,14],
[14,13,15,17,14,12,9,0,19,13,15],
[9,8,15,10,12,14,8,6,0,11,13],
[13,13,10,13,10,11,11,12,14,0,13],
[14,11,10,15,10,11,11,10,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,10,16,14,8,13,14,14,14],
[11,0,10,12,10,13,9,11,12,15,9],
[12,15,0,13,10,15,11,7,14,14,10],
[15,13,12,0,12,13,11,12,16,19,15],
[9,15,15,13,0,13,11,11,17,15,10],
[11,12,10,12,12,0,13,10,13,13,8],
[17,16,14,14,14,12,0,13,21,15,16],
[12,14,18,13,14,15,12,0,14,14,13],
[11,13,11,9,8,12,4,11,0,11,15],
[11,10,11,6,10,12,10,11,14,0,16],
[11,16,15,10,15,17,9,12,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,17,12,16,16,8,15,11,9,15],
[16,0,17,13,18,14,16,17,12,15,16],
[8,8,0,12,9,6,10,9,8,6,15],
[13,12,13,0,12,12,12,12,9,11,13],
[9,7,16,13,0,9,13,14,12,14,10],
[9,11,19,13,16,0,11,16,16,12,15],
[17,9,15,13,12,14,0,15,15,12,12],
[10,8,16,13,11,9,10,0,11,8,12],
[14,13,17,16,13,9,10,14,0,11,13],
[16,10,19,14,11,13,13,17,14,0,16],
[10,9,10,12,15,10,13,13,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,9,12,13,12,14,12,10,8],
[13,0,15,14,17,11,12,14,12,11,10],
[10,10,0,10,14,12,11,14,11,8,10],
[16,11,15,0,15,13,16,16,14,11,13],
[13,8,11,10,0,14,13,13,10,11,9],
[12,14,13,12,11,0,15,15,13,13,12],
[13,13,14,9,12,10,0,13,12,10,10],
[11,11,11,9,12,10,12,0,11,9,8],
[13,13,14,11,15,12,13,14,0,12,6],
[15,14,17,14,14,12,15,16,13,0,10],
[17,15,15,12,16,13,15,17,19,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,8,19,7,19,17,4,5,14],
[17,0,15,11,18,12,20,18,12,10,16],
[20,10,0,17,20,16,22,19,13,18,17],
[17,14,8,0,18,15,19,17,15,13,14],
[6,7,5,7,0,7,16,15,4,9,16],
[18,13,9,10,18,0,22,18,14,15,16],
[6,5,3,6,9,3,0,8,1,5,5],
[8,7,6,8,10,7,17,0,4,4,14],
[21,13,12,10,21,11,24,21,0,19,18],
[20,15,7,12,16,10,20,21,6,0,14],
[11,9,8,11,9,9,20,11,7,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,20,20,13,23,21,12,17,19,13],
[14,0,19,18,12,15,23,6,21,18,10],
[5,6,0,14,14,14,14,8,19,21,14],
[5,7,11,0,13,16,15,5,11,10,11],
[12,13,11,12,0,15,12,11,11,8,11],
[2,10,11,9,10,0,10,11,16,9,4],
[4,2,11,10,13,15,0,3,12,9,11],
[13,19,17,20,14,14,22,0,20,20,12],
[8,4,6,14,14,9,13,5,0,4,6],
[6,7,4,15,17,16,16,5,21,0,6],
[12,15,11,14,14,21,14,13,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,15,15,14,15,12,17,15,13],
[13,0,12,11,13,12,12,12,18,13,15],
[11,13,0,11,12,11,12,12,15,13,17],
[10,14,14,0,13,15,11,10,16,13,12],
[10,12,13,12,0,14,12,11,18,11,14],
[11,13,14,10,11,0,11,13,19,11,15],
[10,13,13,14,13,14,0,10,17,13,13],
[13,13,13,15,14,12,15,0,15,13,15],
[8,7,10,9,7,6,8,10,0,10,8],
[10,12,12,12,14,14,12,12,15,0,15],
[12,10,8,13,11,10,12,10,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,10,13,17,16,8,10,12,9],
[14,0,13,14,15,17,18,10,10,13,11],
[15,12,0,13,13,15,18,13,11,12,10],
[15,11,12,0,10,15,17,10,10,13,10],
[12,10,12,15,0,18,17,13,13,16,12],
[8,8,10,10,7,0,12,8,10,12,8],
[9,7,7,8,8,13,0,8,9,13,4],
[17,15,12,15,12,17,17,0,12,18,16],
[15,15,14,15,12,15,16,13,0,14,14],
[13,12,13,12,9,13,12,7,11,0,10],
[16,14,15,15,13,17,21,9,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,19,16,15,18,14,16,14,11],
[7,0,9,14,14,11,14,12,9,14,8],
[10,16,0,18,17,15,18,15,16,15,13],
[6,11,7,0,11,10,12,9,9,12,7],
[9,11,8,14,0,10,15,11,12,12,10],
[10,14,10,15,15,0,16,15,13,14,13],
[7,11,7,13,10,9,0,10,11,9,10],
[11,13,10,16,14,10,15,0,13,13,13],
[9,16,9,16,13,12,14,12,0,11,10],
[11,11,10,13,13,11,16,12,14,0,10],
[14,17,12,18,15,12,15,12,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,12,13,17,14,11,16,13,12],
[13,0,8,10,14,17,9,10,12,13,10],
[12,17,0,11,12,15,7,11,12,11,8],
[13,15,14,0,12,13,14,13,14,9,11],
[12,11,13,13,0,19,11,13,14,9,12],
[8,8,10,12,6,0,5,9,12,8,7],
[11,16,18,11,14,20,0,17,15,12,15],
[14,15,14,12,12,16,8,0,13,12,12],
[9,13,13,11,11,13,10,12,0,9,11],
[12,12,14,16,16,17,13,13,16,0,13],
[13,15,17,14,13,18,10,13,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,11,6,16,6,8,8,11,5],
[20,0,14,13,14,19,9,13,13,14,17],
[19,11,0,14,14,20,14,19,14,19,18],
[14,12,11,0,5,14,16,11,9,18,15],
[19,11,11,20,0,15,17,10,9,20,14],
[9,6,5,11,10,0,9,11,7,16,12],
[19,16,11,9,8,16,0,7,10,12,12],
[17,12,6,14,15,14,18,0,8,14,9],
[17,12,11,16,16,18,15,17,0,16,13],
[14,11,6,7,5,9,13,11,9,0,13],
[20,8,7,10,11,13,13,16,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,15,16,12,9,14,20,15,14],
[11,0,14,14,17,10,13,9,13,14,12],
[10,11,0,11,7,11,12,9,12,8,12],
[10,11,14,0,11,5,13,4,13,14,10],
[9,8,18,14,0,10,10,10,15,20,9],
[13,15,14,20,15,0,15,6,17,13,14],
[16,12,13,12,15,10,0,14,11,20,20],
[11,16,16,21,15,19,11,0,13,18,15],
[5,12,13,12,10,8,14,12,0,18,15],
[10,11,17,11,5,12,5,7,7,0,6],
[11,13,13,15,16,11,5,10,10,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,15,15,17,17,13,12,14,14],
[7,0,14,11,10,12,12,10,7,13,11],
[8,11,0,8,10,17,14,14,10,9,10],
[10,14,17,0,14,17,16,14,13,14,14],
[10,15,15,11,0,13,13,13,11,12,15],
[8,13,8,8,12,0,11,9,6,10,9],
[8,13,11,9,12,14,0,13,10,9,12],
[12,15,11,11,12,16,12,0,11,12,12],
[13,18,15,12,14,19,15,14,0,15,14],
[11,12,16,11,13,15,16,13,10,0,12],
[11,14,15,11,10,16,13,13,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,15,15,16,10,10,10,16,21],
[12,0,19,16,15,12,7,10,9,14,22],
[11,6,0,15,8,12,1,6,5,8,20],
[10,9,10,0,10,13,7,6,6,10,17],
[10,10,17,15,0,7,6,6,14,11,17],
[9,13,13,12,18,0,14,13,13,12,19],
[15,18,24,18,19,11,0,23,17,14,20],
[15,15,19,19,19,12,2,0,17,13,22],
[15,16,20,19,11,12,8,8,0,15,22],
[9,11,17,15,14,13,11,12,10,0,17],
[4,3,5,8,8,6,5,3,3,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,13,10,7,9,4,9,8,8,12],
[20,0,12,11,16,14,17,14,13,18,18],
[12,13,0,9,14,14,12,17,14,17,16],
[15,14,16,0,15,14,12,12,13,17,18],
[18,9,11,10,0,16,12,13,10,16,18],
[16,11,11,11,9,0,14,11,11,13,13],
[21,8,13,13,13,11,0,13,11,15,14],
[16,11,8,13,12,14,12,0,12,14,14],
[17,12,11,12,15,14,14,13,0,16,15],
[17,7,8,8,9,12,10,11,9,0,13],
[13,7,9,7,7,12,11,11,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,12,18,14,15,15,14,13,13],
[17,0,9,11,13,12,15,16,15,11,11],
[13,16,0,11,17,15,12,15,15,12,14],
[13,14,14,0,21,8,14,13,19,12,16],
[7,12,8,4,0,7,9,13,15,7,10],
[11,13,10,17,18,0,11,16,13,15,9],
[10,10,13,11,16,14,0,15,17,10,15],
[10,9,10,12,12,9,10,0,15,12,9],
[11,10,10,6,10,12,8,10,0,9,10],
[12,14,13,13,18,10,15,13,16,0,9],
[12,14,11,9,15,16,10,16,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,9,12,10,10,15,10,4,11],
[16,0,12,14,13,9,14,17,18,13,21],
[17,13,0,13,12,13,11,17,15,13,19],
[16,11,12,0,11,14,15,15,19,15,15],
[13,12,13,14,0,12,15,14,16,10,19],
[15,16,12,11,13,0,14,15,14,12,21],
[15,11,14,10,10,11,0,16,12,10,15],
[10,8,8,10,11,10,9,0,9,8,16],
[15,7,10,6,9,11,13,16,0,8,15],
[21,12,12,10,15,13,15,17,17,0,18],
[14,4,6,10,6,4,10,9,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,16,11,15,11,12,10,11,10],
[15,0,16,13,18,14,14,14,7,17,13],
[12,9,0,10,11,13,5,14,8,10,13],
[9,12,15,0,11,14,11,9,12,13,13],
[14,7,14,14,0,8,12,16,9,10,14],
[10,11,12,11,17,0,10,13,9,16,13],
[14,11,20,14,13,15,0,13,14,17,15],
[13,11,11,16,9,12,12,0,9,13,8],
[15,18,17,13,16,16,11,16,0,16,15],
[14,8,15,12,15,9,8,12,9,0,11],
[15,12,12,12,11,12,10,17,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,10,16,8,12,11,11,14,13],
[15,0,15,13,14,13,14,15,14,18,12],
[13,10,0,13,16,11,13,16,12,18,16],
[15,12,12,0,15,12,12,15,12,16,13],
[9,11,9,10,0,11,10,15,10,11,12],
[17,12,14,13,14,0,15,15,11,17,12],
[13,11,12,13,15,10,0,16,9,18,10],
[14,10,9,10,10,10,9,0,10,13,11],
[14,11,13,13,15,14,16,15,0,15,12],
[11,7,7,9,14,8,7,12,10,0,11],
[12,13,9,12,13,13,15,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,9,14,13,13,12,8,19,8],
[13,0,12,12,18,11,15,12,13,18,12],
[10,13,0,11,14,12,12,11,11,19,7],
[16,13,14,0,16,13,15,15,10,15,14],
[11,7,11,9,0,11,13,10,7,17,11],
[12,14,13,12,14,0,15,11,13,18,12],
[12,10,13,10,12,10,0,10,12,12,11],
[13,13,14,10,15,14,15,0,11,18,12],
[17,12,14,15,18,12,13,14,0,19,14],
[6,7,6,10,8,7,13,7,6,0,10],
[17,13,18,11,14,13,14,13,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,10,14,16,14,14,15,10,18,13],
[6,0,5,8,6,7,11,9,8,5,12],
[15,20,0,13,12,12,20,11,13,19,11],
[11,17,12,0,15,12,13,15,8,17,13],
[9,19,13,10,0,14,15,6,11,21,10],
[11,18,13,13,11,0,14,9,4,14,13],
[11,14,5,12,10,11,0,11,11,10,11],
[10,16,14,10,19,16,14,0,12,19,16],
[15,17,12,17,14,21,14,13,0,17,13],
[7,20,6,8,4,11,15,6,8,0,9],
[12,13,14,12,15,12,14,9,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,15,14,20,14,11,11,10,15],
[9,0,14,11,8,8,13,10,7,10,10],
[10,11,0,11,6,7,12,5,6,7,10],
[10,14,14,0,9,15,13,14,7,6,14],
[11,17,19,16,0,16,19,15,10,14,17],
[5,17,18,10,9,0,18,10,10,14,17],
[11,12,13,12,6,7,0,11,14,12,15],
[14,15,20,11,10,15,14,0,6,7,14],
[14,18,19,18,15,15,11,19,0,16,12],
[15,15,18,19,11,11,13,18,9,0,12],
[10,15,15,11,8,8,10,11,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,15,16,8,12,11,18,12,15],
[16,0,13,15,13,15,12,19,15,16,15],
[13,12,0,9,15,12,10,14,10,14,15],
[10,10,16,0,12,12,13,14,12,10,13],
[9,12,10,13,0,9,9,14,11,8,14],
[17,10,13,13,16,0,10,13,14,18,10],
[13,13,15,12,16,15,0,17,17,17,15],
[14,6,11,11,11,12,8,0,13,10,11],
[7,10,15,13,14,11,8,12,0,10,13],
[13,9,11,15,17,7,8,15,15,0,12],
[10,10,10,12,11,15,10,14,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,17,11,13,11,17,12,8,14],
[11,0,15,9,11,11,15,14,10,10,10],
[8,10,0,7,11,10,11,15,11,8,12],
[8,16,18,0,12,13,15,18,12,10,12],
[14,14,14,13,0,19,12,19,14,15,11],
[12,14,15,12,6,0,15,14,15,10,7],
[14,10,14,10,13,10,0,15,12,11,10],
[8,11,10,7,6,11,10,0,6,8,11],
[13,15,14,13,11,10,13,19,0,9,12],
[17,15,17,15,10,15,14,17,16,0,11],
[11,15,13,13,14,18,15,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,9,11,11,13,12,12,11],
[15,0,17,15,14,13,14,13,15,12,13],
[14,8,0,10,11,12,12,13,11,10,13],
[15,10,15,0,15,16,13,13,18,14,17],
[16,11,14,10,0,13,12,14,14,14,15],
[14,12,13,9,12,0,17,14,15,12,14],
[14,11,13,12,13,8,0,13,16,11,14],
[12,12,12,12,11,11,12,0,17,11,13],
[13,10,14,7,11,10,9,8,0,8,12],
[13,13,15,11,11,13,14,14,17,0,17],
[14,12,12,8,10,11,11,12,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,11,9,13,12,10,11,8,8],
[13,0,12,12,10,11,13,9,11,9,9],
[13,13,0,11,14,11,12,14,10,10,12],
[14,13,14,0,9,10,12,14,14,13,12],
[16,15,11,16,0,11,13,13,13,12,10],
[12,14,14,15,14,0,14,11,13,13,7],
[13,12,13,13,12,11,0,13,13,11,11],
[15,16,11,11,12,14,12,0,13,10,9],
[14,14,15,11,12,12,12,12,0,12,11],
[17,16,15,12,13,12,14,15,13,0,14],
[17,16,13,13,15,18,14,16,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,8,15,9,16,14,9,18,10],
[15,0,11,12,12,16,18,13,9,16,20],
[16,14,0,11,10,10,17,16,10,20,13],
[17,13,14,0,18,10,18,14,9,16,14],
[10,13,15,7,0,5,16,15,7,15,15],
[16,9,15,15,20,0,17,15,15,18,20],
[9,7,8,7,9,8,0,9,5,10,12],
[11,12,9,11,10,10,16,0,9,15,17],
[16,16,15,16,18,10,20,16,0,21,12],
[7,9,5,9,10,7,15,10,4,0,11],
[15,5,12,11,10,5,13,8,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,12,7,12,11,6,9,14,9],
[18,0,8,15,9,13,10,10,11,13,13],
[20,17,0,17,15,14,15,14,11,14,15],
[13,10,8,0,7,12,14,12,10,12,10],
[18,16,10,18,0,16,18,10,13,16,13],
[13,12,11,13,9,0,12,8,8,13,7],
[14,15,10,11,7,13,0,4,8,10,10],
[19,15,11,13,15,17,21,0,12,16,20],
[16,14,14,15,12,17,17,13,0,16,16],
[11,12,11,13,9,12,15,9,9,0,9],
[16,12,10,15,12,18,15,5,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,6,8,11,8,17,7,4,12],
[14,0,12,13,5,8,13,14,8,9,16],
[15,13,0,10,11,8,7,12,9,6,12],
[19,12,15,0,13,11,10,15,17,8,13],
[17,20,14,12,0,12,10,18,9,10,19],
[14,17,17,14,13,0,12,16,10,16,17],
[17,12,18,15,15,13,0,13,17,10,16],
[8,11,13,10,7,9,12,0,4,7,11],
[18,17,16,8,16,15,8,21,0,10,19],
[21,16,19,17,15,9,15,18,15,0,15],
[13,9,13,12,6,8,9,14,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,10,14,13,13,10,10,12,9],
[16,0,13,9,17,15,12,11,13,15,15],
[14,12,0,15,16,16,14,12,15,13,14],
[15,16,10,0,14,12,11,11,14,14,14],
[11,8,9,11,0,12,8,10,9,12,11],
[12,10,9,13,13,0,12,12,8,12,11],
[12,13,11,14,17,13,0,14,10,11,11],
[15,14,13,14,15,13,11,0,13,14,14],
[15,12,10,11,16,17,15,12,0,11,12],
[13,10,12,11,13,13,14,11,14,0,16],
[16,10,11,11,14,14,14,11,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,8,8,17,16,8,7,8,25],
[17,0,18,8,19,19,18,25,22,19,24],
[19,7,0,7,16,16,15,15,16,16,24],
[17,17,18,0,16,17,23,25,16,12,25],
[17,6,9,9,0,23,14,16,22,18,23],
[8,6,9,8,2,0,14,16,13,9,14],
[9,7,10,2,11,11,0,7,16,11,24],
[17,0,10,0,9,9,18,0,14,9,17],
[18,3,9,9,3,12,9,11,0,3,20],
[17,6,9,13,7,16,14,16,22,0,22],
[0,1,1,0,2,11,1,8,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,12,11,14,15,15,12,11],
[12,0,11,9,11,11,10,11,9,10,14],
[12,14,0,10,12,11,13,10,10,9,14],
[13,16,15,0,12,11,13,12,12,13,11],
[13,14,13,13,0,11,10,13,12,9,13],
[14,14,14,14,14,0,11,15,13,13,15],
[11,15,12,12,15,14,0,15,12,13,14],
[10,14,15,13,12,10,10,0,13,12,11],
[10,16,15,13,13,12,13,12,0,13,14],
[13,15,16,12,16,12,12,13,12,0,12],
[14,11,11,14,12,10,11,14,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,14,9,15,9,17,13,12,11],
[14,0,11,12,14,14,12,16,11,12,10],
[17,14,0,13,14,15,11,14,16,16,13],
[11,13,12,0,12,14,9,14,14,12,11],
[16,11,11,13,0,14,13,13,9,15,10],
[10,11,10,11,11,0,7,12,10,12,9],
[16,13,14,16,12,18,0,17,15,15,12],
[8,9,11,11,12,13,8,0,13,10,8],
[12,14,9,11,16,15,10,12,0,13,13],
[13,13,9,13,10,13,10,15,12,0,12],
[14,15,12,14,15,16,13,17,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,14,11,12,13,14,17,14,12],
[12,0,16,14,13,16,14,9,15,16,15],
[13,9,0,12,4,11,12,13,16,11,11],
[11,11,13,0,8,14,11,12,16,13,13],
[14,12,21,17,0,18,16,16,17,16,17],
[13,9,14,11,7,0,12,10,12,14,13],
[12,11,13,14,9,13,0,10,17,14,14],
[11,16,12,13,9,15,15,0,15,12,11],
[8,10,9,9,8,13,8,10,0,13,9],
[11,9,14,12,9,11,11,13,12,0,10],
[13,10,14,12,8,12,11,14,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,12,13,15,14,10,13,11,9],
[11,0,12,11,12,8,14,12,15,9,8],
[9,13,0,11,12,13,14,12,14,13,12],
[13,14,14,0,14,11,15,9,16,12,13],
[12,13,13,11,0,15,15,10,12,12,11],
[10,17,12,14,10,0,14,11,14,13,12],
[11,11,11,10,10,11,0,9,13,10,10],
[15,13,13,16,15,14,16,0,9,15,15],
[12,10,11,9,13,11,12,16,0,11,8],
[14,16,12,13,13,12,15,10,14,0,12],
[16,17,13,12,14,13,15,10,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 25, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_11_25.csv", index=False, header=False)