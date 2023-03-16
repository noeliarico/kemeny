
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,25,21,14,13,10,18,21,25,13,17,14,25,13,25],
[0,0,14,10,6,6,14,14,21,13,13,14,25,9,14],
[4,11,0,4,2,8,6,0,11,11,15,0,23,7,16],
[11,15,21,0,13,4,18,13,19,11,13,12,25,11,25],
[12,19,23,12,0,16,16,23,23,23,23,16,23,19,23],
[15,19,17,21,9,0,14,17,17,13,13,17,25,9,25],
[7,11,19,7,9,11,0,7,15,11,11,15,23,7,23],
[4,11,25,12,2,8,18,0,19,15,17,12,25,11,18],
[0,4,14,6,2,8,10,6,0,4,6,2,18,2,18],
[12,12,14,14,2,12,14,10,21,0,10,10,18,9,18],
[8,12,10,12,2,12,14,8,19,15,0,8,18,15,16],
[11,11,25,13,9,8,10,13,23,15,17,0,25,11,25],
[0,0,2,0,2,0,2,0,7,7,7,0,0,7,0],
[12,16,18,14,6,16,18,14,23,16,10,14,18,0,18],
[0,11,9,0,2,0,2,7,7,7,9,0,25,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,7,3,5,8,8,10,7,7,9,8,6,4],
[16,0,12,16,10,14,10,14,16,17,13,9,14,17,19],
[17,13,0,15,10,13,2,11,9,15,8,9,15,15,11],
[18,9,10,0,5,13,8,8,12,9,9,12,12,10,7],
[22,15,15,20,0,19,17,21,21,16,16,11,20,15,13],
[20,11,12,12,6,0,10,12,13,13,11,9,8,9,9],
[17,15,23,17,8,15,0,16,12,18,17,10,13,19,18],
[17,11,14,17,4,13,9,0,11,15,10,11,11,13,5],
[15,9,16,13,4,12,13,14,0,11,13,9,18,12,10],
[18,8,10,16,9,12,7,10,14,0,8,10,10,11,14],
[18,12,17,16,9,14,8,15,12,17,0,8,10,17,12],
[16,16,16,13,14,16,15,14,16,15,17,0,15,10,17],
[17,11,10,13,5,17,12,14,7,15,15,10,0,11,8],
[19,8,10,15,10,16,6,12,13,14,8,15,14,0,11],
[21,6,14,18,12,16,7,20,15,11,13,8,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,12,8,12,12,12,9,9,9,9,9,7,6],
[18,0,14,15,12,14,15,20,11,13,12,12,13,14,8],
[13,11,0,14,13,16,12,15,13,14,10,15,13,14,12],
[13,10,11,0,14,15,11,14,13,10,12,10,8,10,11],
[17,13,12,11,0,17,11,18,15,12,14,13,9,12,13],
[13,11,9,10,8,0,9,17,9,11,10,10,10,8,7],
[13,10,13,14,14,16,0,16,11,12,13,12,12,12,8],
[13,5,10,11,7,8,9,0,6,8,12,9,8,9,4],
[16,14,12,12,10,16,14,19,0,14,15,15,13,11,14],
[16,12,11,15,13,14,13,17,11,0,13,13,12,10,12],
[16,13,15,13,11,15,12,13,10,12,0,12,13,13,11],
[16,13,10,15,12,15,13,16,10,12,13,0,9,11,9],
[16,12,12,17,16,15,13,17,12,13,12,16,0,15,15],
[18,11,11,15,13,17,13,16,14,15,12,14,10,0,11],
[19,17,13,14,12,18,17,21,11,13,14,16,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,13,10,16,11,14,18,10,11,14,14,13,14],
[10,0,12,11,12,14,13,11,12,9,14,11,12,6,7],
[14,13,0,16,16,13,15,14,13,15,11,18,12,13,12],
[12,14,9,0,11,12,14,13,17,13,11,13,13,10,9],
[15,13,9,14,0,14,14,13,15,12,10,12,16,12,11],
[9,11,12,13,11,0,12,11,12,5,11,12,10,8,10],
[14,12,10,11,11,13,0,14,13,9,11,11,11,12,11],
[11,14,11,12,12,14,11,0,13,10,13,11,12,8,6],
[7,13,12,8,10,13,12,12,0,6,10,9,11,9,9],
[15,16,10,12,13,20,16,15,19,0,12,13,12,12,13],
[14,11,14,14,15,14,14,12,15,13,0,13,17,10,12],
[11,14,7,12,13,13,14,14,16,12,12,0,13,9,9],
[11,13,13,12,9,15,14,13,14,13,8,12,0,11,14],
[12,19,12,15,13,17,13,17,16,13,15,16,14,0,13],
[11,18,13,16,14,15,14,19,16,12,13,16,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,10,20,10,6,12,10,8,11,12,11,8,12],
[13,0,13,7,15,9,6,13,4,9,14,10,8,8,10],
[8,12,0,5,11,10,5,14,6,3,13,11,4,6,6],
[15,18,20,0,17,13,10,19,13,9,19,17,14,14,10],
[5,10,14,8,0,13,9,12,9,11,13,11,7,9,5],
[15,16,15,12,12,0,10,12,10,9,16,12,7,10,8],
[19,19,20,15,16,15,0,11,9,6,15,12,12,11,11],
[13,12,11,6,13,13,14,0,6,5,9,5,6,8,8],
[15,21,19,12,16,15,16,19,0,13,19,16,11,13,16],
[17,16,22,16,14,16,19,20,12,0,17,16,13,10,12],
[14,11,12,6,12,9,10,16,6,8,0,5,7,6,9],
[13,15,14,8,14,13,13,20,9,9,20,0,8,7,9],
[14,17,21,11,18,18,13,19,14,12,18,17,0,13,17],
[17,17,19,11,16,15,14,17,12,15,19,18,12,0,12],
[13,15,19,15,20,17,14,17,9,13,16,16,8,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,16,14,10,11,13,16,11,11,11,12,13,8],
[14,0,13,15,10,12,8,15,14,11,11,15,15,10,10],
[15,12,0,11,9,11,9,10,12,10,11,17,12,13,8],
[9,10,14,0,12,7,6,12,11,10,9,13,17,8,10],
[11,15,16,13,0,8,7,12,15,11,12,14,16,12,9],
[15,13,14,18,17,0,13,18,13,17,12,19,21,16,15],
[14,17,16,19,18,12,0,14,14,18,11,18,16,16,10],
[12,10,15,13,13,7,11,0,14,14,14,13,15,12,11],
[9,11,13,14,10,12,11,11,0,11,14,13,14,13,8],
[14,14,15,15,14,8,7,11,14,0,12,17,18,14,12],
[14,14,14,16,13,13,14,11,11,13,0,15,16,16,10],
[14,10,8,12,11,6,7,12,12,8,10,0,11,13,6],
[13,10,13,8,9,4,9,10,11,7,9,14,0,12,9],
[12,15,12,17,13,9,9,13,12,11,9,12,13,0,14],
[17,15,17,15,16,10,15,14,17,13,15,19,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,19,22,16,17,16,21,19,11,21,18,13,15],
[7,0,16,12,14,14,11,14,17,12,7,15,20,9,10],
[9,9,0,13,13,13,16,6,20,6,12,15,15,10,12],
[6,13,12,0,15,10,12,5,17,11,12,10,19,13,7],
[3,11,12,10,0,13,13,12,16,11,8,14,14,10,10],
[9,11,12,15,12,0,10,8,14,11,12,11,15,11,8],
[8,14,9,13,12,15,0,10,19,8,13,14,14,13,10],
[9,11,19,20,13,17,15,0,20,13,15,16,17,14,17],
[4,8,5,8,9,11,6,5,0,3,9,14,13,14,4],
[6,13,19,14,14,14,17,12,22,0,12,15,19,15,11],
[14,18,13,13,17,13,12,10,16,13,0,15,17,14,10],
[4,10,10,15,11,14,11,9,11,10,10,0,16,12,9],
[7,5,10,6,11,10,11,8,12,6,8,9,0,5,5],
[12,16,15,12,15,14,12,11,11,10,11,13,20,0,11],
[10,15,13,18,15,17,15,8,21,14,15,16,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,21,18,9,8,8,13,9,8,9,25,17,14,14],
[16,0,17,14,8,7,12,12,8,7,13,16,21,12,13],
[4,8,0,14,0,4,3,13,5,4,9,16,12,9,9],
[7,11,11,0,11,11,7,15,12,7,11,15,11,11,16],
[16,17,25,14,0,16,12,25,12,16,22,25,21,21,20],
[17,18,21,14,9,0,17,9,5,14,13,21,21,21,14],
[17,13,22,18,13,8,0,13,13,17,17,20,25,17,18],
[12,13,12,10,0,16,12,0,5,9,4,12,16,16,9],
[16,17,20,13,13,20,12,20,0,9,17,20,16,16,20],
[17,18,21,18,9,11,8,16,16,0,13,25,17,17,21],
[16,12,16,14,3,12,8,21,8,12,0,25,16,16,12],
[0,9,9,10,0,4,5,13,5,0,0,0,12,4,5],
[8,4,13,14,4,4,0,9,9,8,9,13,0,4,9],
[11,13,16,14,4,4,8,9,9,8,9,21,21,0,9],
[11,12,16,9,5,11,7,16,5,4,13,20,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,7,7,12,11,15,10,9,16,11,11,11,7],
[15,0,14,16,14,12,13,11,13,11,19,11,18,12,12],
[14,11,0,10,3,14,8,11,11,10,12,14,12,9,6],
[18,9,15,0,9,11,14,13,14,17,16,16,20,16,11],
[18,11,22,16,0,14,15,14,18,14,21,18,16,15,18],
[13,13,11,14,11,0,11,14,14,11,18,15,15,16,7],
[14,12,17,11,10,14,0,15,17,19,23,17,16,16,14],
[10,14,14,12,11,11,10,0,10,12,12,15,10,12,13],
[15,12,14,11,7,11,8,15,0,15,20,16,15,5,10],
[16,14,15,8,11,14,6,13,10,0,12,16,11,13,11],
[9,6,13,9,4,7,2,13,5,13,0,11,8,7,6],
[14,14,11,9,7,10,8,10,9,9,14,0,11,8,8],
[14,7,13,5,9,10,9,15,10,14,17,14,0,12,9],
[14,13,16,9,10,9,9,13,20,12,18,17,13,0,10],
[18,13,19,14,7,18,11,12,15,14,19,17,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,16,14,13,13,15,12,11,21,15,16,15,13],
[10,0,14,11,14,17,13,18,15,14,14,13,18,19,12],
[13,11,0,16,15,16,17,15,10,11,17,17,17,18,10],
[9,14,9,0,13,14,12,16,11,13,12,16,13,16,11],
[11,11,10,12,0,10,9,8,7,8,14,11,10,13,9],
[12,8,9,11,15,0,8,14,8,10,13,10,12,15,15],
[12,12,8,13,16,17,0,16,12,13,16,13,13,17,11],
[10,7,10,9,17,11,9,0,7,10,16,12,12,15,11],
[13,10,15,14,18,17,13,18,0,15,17,15,14,18,13],
[14,11,14,12,17,15,12,15,10,0,16,16,12,16,11],
[4,11,8,13,11,12,9,9,8,9,0,11,11,13,9],
[10,12,8,9,14,15,12,13,10,9,14,0,12,16,10],
[9,7,8,12,15,13,12,13,11,13,14,13,0,16,9],
[10,6,7,9,12,10,8,10,7,9,12,9,9,0,9],
[12,13,15,14,16,10,14,14,12,14,16,15,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,16,17,14,18,17,16,15,15,13,17,12],
[14,0,14,12,13,13,12,16,12,14,10,11,13,12,11],
[12,11,0,13,12,14,10,18,15,17,12,13,16,15,8],
[13,13,12,0,12,13,12,15,13,16,15,11,14,13,11],
[9,12,13,13,0,15,15,17,13,14,13,15,12,16,11],
[8,12,11,12,10,0,13,12,10,13,14,9,12,8,9],
[11,13,15,13,10,12,0,17,19,17,12,13,15,12,14],
[7,9,7,10,8,13,8,0,11,16,10,12,11,10,8],
[8,13,10,12,12,15,6,14,0,16,11,11,13,10,8],
[9,11,8,9,11,12,8,9,9,0,10,11,11,10,7],
[10,15,13,10,12,11,13,15,14,15,0,13,11,12,11],
[10,14,12,14,10,16,12,13,14,14,12,0,10,10,9],
[12,12,9,11,13,13,10,14,12,14,14,15,0,14,11],
[8,13,10,12,9,17,13,15,15,15,13,15,11,0,9],
[13,14,17,14,14,16,11,17,17,18,14,16,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,17,16,11,18,19,14,12,13,18,16,15,17],
[7,0,13,10,10,12,13,9,11,12,11,11,11,9,4],
[12,12,0,12,13,13,12,12,12,12,11,11,13,10,9],
[8,15,13,0,11,12,9,16,15,13,12,15,17,8,12],
[9,15,12,14,0,13,6,15,9,12,14,13,14,14,8],
[14,13,12,13,12,0,12,13,12,16,12,12,16,10,10],
[7,12,13,16,19,13,0,17,18,10,11,18,12,12,9],
[6,16,13,9,10,12,8,0,11,10,11,18,15,8,10],
[11,14,13,10,16,13,7,14,0,12,8,15,15,9,12],
[13,13,13,12,13,9,15,15,13,0,8,13,17,10,9],
[12,14,14,13,11,13,14,14,17,17,0,16,15,15,11],
[7,14,14,10,12,13,7,7,10,12,9,0,16,11,11],
[9,14,12,8,11,9,13,10,10,8,10,9,0,8,11],
[10,16,15,17,11,15,13,17,16,15,10,14,17,0,13],
[8,21,16,13,17,15,16,15,13,16,14,14,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,11,8,9,17,8,12,13,14,22,15,14,14],
[9,0,10,8,6,11,14,8,11,13,12,15,12,14,8],
[12,15,0,9,13,13,17,6,12,15,14,18,17,17,12],
[14,17,16,0,10,18,13,17,14,8,12,16,14,17,13],
[17,19,12,15,0,22,13,11,15,18,9,20,21,17,19],
[16,14,12,7,3,0,11,5,6,12,9,18,14,13,11],
[8,11,8,12,12,14,0,10,10,9,12,17,11,13,9],
[17,17,19,8,14,20,15,0,15,13,13,20,20,20,17],
[13,14,13,11,10,19,15,10,0,16,12,20,19,24,18],
[12,12,10,17,7,13,16,12,9,0,12,16,11,11,10],
[11,13,11,13,16,16,13,12,13,13,0,14,16,15,12],
[3,10,7,9,5,7,8,5,5,9,11,0,11,8,8],
[10,13,8,11,4,11,14,5,6,14,9,14,0,10,15],
[11,11,8,8,8,12,12,5,1,14,10,17,15,0,11],
[11,17,13,12,6,14,16,8,7,15,13,17,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,12,16,17,9,12,13,12,12,13,14,15,12],
[11,0,12,11,13,17,13,14,11,12,14,15,16,15,12],
[11,13,0,5,13,13,6,15,13,11,12,11,11,9,11],
[13,14,20,0,17,17,10,16,15,13,16,15,13,15,17],
[9,12,12,8,0,12,7,14,8,9,10,13,11,8,13],
[8,8,12,8,13,0,8,12,11,13,11,13,14,11,9],
[16,12,19,15,18,17,0,16,16,14,17,19,15,18,15],
[13,11,10,9,11,13,9,0,11,11,9,9,11,13,7],
[12,14,12,10,17,14,9,14,0,11,16,13,18,14,11],
[13,13,14,12,16,12,11,14,14,0,11,11,16,14,11],
[13,11,13,9,15,14,8,16,9,14,0,13,16,11,12],
[12,10,14,10,12,12,6,16,12,14,12,0,10,10,13],
[11,9,14,12,14,11,10,14,7,9,9,15,0,13,13],
[10,10,16,10,17,14,7,12,11,11,14,15,12,0,13],
[13,13,14,8,12,16,10,18,14,14,13,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,15,12,12,14,15,9,12,12,11,10,16,13],
[12,0,11,16,12,13,11,11,13,12,13,14,11,15,14],
[15,14,0,16,11,15,13,15,12,13,14,13,12,15,17],
[10,9,9,0,8,6,10,13,9,10,10,7,8,10,10],
[13,13,14,17,0,13,13,13,14,11,14,13,13,16,15],
[13,12,10,19,12,0,13,14,10,13,11,12,13,17,13],
[11,14,12,15,12,12,0,14,13,15,15,13,8,12,15],
[10,14,10,12,12,11,11,0,13,13,11,13,10,12,14],
[16,12,13,16,11,15,12,12,0,11,13,14,12,15,14],
[13,13,12,15,14,12,10,12,14,0,12,16,12,15,16],
[13,12,11,15,11,14,10,14,12,13,0,10,7,14,13],
[14,11,12,18,12,13,12,12,11,9,15,0,11,17,15],
[15,14,13,17,12,12,17,15,13,13,18,14,0,18,13],
[9,10,10,15,9,8,13,13,10,10,11,8,7,0,11],
[12,11,8,15,10,12,10,11,11,9,12,10,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,14,14,11,13,9,14,15,12,10,12,12,12],
[11,0,13,9,10,14,17,9,16,13,13,14,12,15,14],
[7,12,0,13,10,13,13,9,11,16,11,13,14,13,14],
[11,16,12,0,9,13,19,13,13,14,16,18,13,14,13],
[11,15,15,16,0,15,14,9,16,15,13,12,11,13,12],
[14,11,12,12,10,0,14,9,12,13,13,13,16,13,13],
[12,8,12,6,11,11,0,3,12,11,12,11,13,9,13],
[16,16,16,12,16,16,22,0,18,16,16,16,15,17,15],
[11,9,14,12,9,13,13,7,0,13,13,12,12,15,13],
[10,12,9,11,10,12,14,9,12,0,15,11,12,14,14],
[13,12,14,9,12,12,13,9,12,10,0,9,12,9,13],
[15,11,12,7,13,12,14,9,13,14,16,0,18,8,14],
[13,13,11,12,14,9,12,10,13,13,13,7,0,9,10],
[13,10,12,11,12,12,16,8,10,11,16,17,16,0,13],
[13,11,11,12,13,12,12,10,12,11,12,11,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,16,15,11,12,15,12,16,14,15,17,15,16],
[12,0,16,15,14,13,12,13,10,14,13,13,19,16,14],
[13,9,0,11,13,11,12,12,9,13,11,14,17,13,13],
[9,10,14,0,13,11,13,9,12,15,9,13,13,8,16],
[10,11,12,12,0,14,12,11,9,15,9,14,18,14,13],
[14,12,14,14,11,0,11,14,11,12,9,14,13,10,11],
[13,13,13,12,13,14,0,11,11,12,12,16,13,10,14],
[10,12,13,16,14,11,14,0,14,14,11,16,15,13,13],
[13,15,16,13,16,14,14,11,0,16,13,17,18,15,13],
[9,11,12,10,10,13,13,11,9,0,12,11,15,11,15],
[11,12,14,16,16,16,13,14,12,13,0,15,14,13,16],
[10,12,11,12,11,11,9,9,8,14,10,0,13,11,10],
[8,6,8,12,7,12,12,10,7,10,11,12,0,13,8],
[10,9,12,17,11,15,15,12,10,14,12,14,12,0,13],
[9,11,12,9,12,14,11,12,12,10,9,15,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,4,19,12,9,16,14,13,11,12,12,10,19],
[16,0,16,14,12,14,12,14,15,16,13,20,21,7,18],
[14,9,0,11,11,12,5,13,12,11,13,22,13,9,16],
[21,11,14,0,18,14,12,19,18,18,11,20,13,13,20],
[6,13,14,7,0,14,13,18,13,17,13,17,15,9,19],
[13,11,13,11,11,0,9,12,11,18,9,19,17,6,18],
[16,13,20,13,12,16,0,13,12,17,13,20,16,15,16],
[9,11,12,6,7,13,12,0,5,14,5,13,11,6,13],
[11,10,13,7,12,14,13,20,0,15,11,15,14,11,17],
[12,9,14,7,8,7,8,11,10,0,10,18,15,4,13],
[14,12,12,14,12,16,12,20,14,15,0,23,11,8,22],
[13,5,3,5,8,6,5,12,10,7,2,0,5,2,14],
[13,4,12,12,10,8,9,14,11,10,14,20,0,8,13],
[15,18,16,12,16,19,10,19,14,21,17,23,17,0,19],
[6,7,9,5,6,7,9,12,8,12,3,11,12,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,8,9,4,4,9,17,12,4,8,9,4,13],
[21,0,17,12,13,17,12,17,25,20,21,12,17,12,17],
[21,8,0,16,17,21,20,17,25,12,13,16,13,16,21],
[17,13,9,0,21,5,21,9,17,12,17,13,9,17,25],
[16,12,8,4,0,4,8,4,21,12,16,8,9,8,17],
[21,8,4,20,21,0,20,17,25,16,12,16,17,20,25],
[21,13,5,4,17,5,0,5,21,12,13,13,5,8,21],
[16,8,8,16,21,8,20,0,25,16,12,20,21,20,25],
[8,0,0,8,4,0,4,0,0,4,0,4,0,4,13],
[13,5,13,13,13,9,13,9,21,0,9,17,13,13,17],
[21,4,12,8,9,13,12,13,25,16,0,12,9,8,13],
[17,13,9,12,17,9,12,5,21,8,13,0,9,12,17],
[16,8,12,16,16,8,20,4,25,12,16,16,0,20,25],
[21,13,9,8,17,5,17,5,21,12,17,13,5,0,21],
[12,8,4,0,8,0,4,0,12,8,12,8,0,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,25,16,18,18,23,18,18,18,11,16,11,18,18],
[14,0,14,7,9,14,15,14,18,14,17,14,10,14,7],
[0,11,0,13,18,9,8,14,11,14,5,14,9,13,10],
[9,18,12,0,18,19,10,25,18,18,12,14,18,18,12],
[7,16,7,7,0,14,8,15,16,8,8,8,10,7,7],
[7,11,16,6,11,0,14,9,4,7,3,7,9,8,3],
[2,10,17,15,17,11,0,17,11,10,5,8,10,17,11],
[7,11,11,0,10,16,8,0,11,14,12,14,5,11,9],
[7,7,14,7,9,21,14,14,0,7,10,7,9,7,14],
[7,11,11,7,17,18,15,11,18,0,12,1,5,11,9],
[14,8,20,13,17,22,20,13,15,13,0,13,8,13,13],
[9,11,11,11,17,18,17,11,18,24,12,0,5,11,11],
[14,15,16,7,15,16,15,20,16,20,17,20,0,14,7],
[7,11,12,7,18,17,8,14,18,14,12,14,11,0,10],
[7,18,15,13,18,22,14,16,11,16,12,14,18,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,11,9,11,13,13,11,16,8,10,16,10,11],
[15,0,17,19,12,14,16,15,12,17,13,15,18,16,15],
[10,8,0,12,9,8,8,11,12,15,10,7,11,10,12],
[14,6,13,0,11,10,10,12,9,15,8,10,13,11,14],
[16,13,16,14,0,10,11,15,16,16,13,15,16,13,16],
[14,11,17,15,15,0,16,15,11,14,15,14,17,14,12],
[12,9,17,15,14,9,0,14,13,16,9,15,11,9,13],
[12,10,14,13,10,10,11,0,11,13,11,15,13,11,10],
[14,13,13,16,9,14,12,14,0,16,12,12,14,12,14],
[9,8,10,10,9,11,9,12,9,0,10,8,14,9,9],
[17,12,15,17,12,10,16,14,13,15,0,15,10,11,13],
[15,10,18,15,10,11,10,10,13,17,10,0,13,14,14],
[9,7,14,12,9,8,14,12,11,11,15,12,0,9,9],
[15,9,15,14,12,11,16,14,13,16,14,11,16,0,8],
[14,10,13,11,9,13,12,15,11,16,12,11,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,11,7,12,16,14,11,6,13,12,13,7,17],
[10,0,13,12,6,9,17,11,12,11,7,10,15,8,13],
[8,12,0,10,10,11,15,11,10,10,13,13,13,6,12],
[14,13,15,0,10,15,15,10,11,11,11,12,15,8,12],
[18,19,15,15,0,16,15,18,14,12,15,15,15,9,19],
[13,16,14,10,9,0,12,11,12,14,10,15,15,8,11],
[9,8,10,10,10,13,0,5,8,7,13,12,4,6,10],
[11,14,14,15,7,14,20,0,13,9,14,11,13,6,7],
[14,13,15,14,11,13,17,12,0,8,14,13,12,6,13],
[19,14,15,14,13,11,18,16,17,0,14,13,14,10,15],
[12,18,12,14,10,15,12,11,11,11,0,15,10,6,11],
[13,15,12,13,10,10,13,14,12,12,10,0,15,13,15],
[12,10,12,10,10,10,21,12,13,11,15,10,0,9,10],
[18,17,19,17,16,17,19,19,19,15,19,12,16,0,14],
[8,12,13,13,6,14,15,18,12,10,14,10,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,11,12,11,12,8,11,13,10,12,14,14,9],
[12,0,8,10,11,12,13,11,12,13,11,13,14,11,9],
[15,17,0,13,16,15,16,14,12,18,14,12,12,15,16],
[14,15,12,0,13,18,19,14,18,16,11,17,16,14,14],
[13,14,9,12,0,13,12,9,14,13,9,14,17,13,11],
[14,13,10,7,12,0,15,11,13,13,13,11,13,11,12],
[13,12,9,6,13,10,0,5,11,9,8,7,12,9,10],
[17,14,11,11,16,14,20,0,13,16,15,17,14,16,15],
[14,13,13,7,11,12,14,12,0,15,10,13,15,14,10],
[12,12,7,9,12,12,16,9,10,0,11,11,9,12,9],
[15,14,11,14,16,12,17,10,15,14,0,16,17,13,17],
[13,12,13,8,11,14,18,8,12,14,9,0,15,13,11],
[11,11,13,9,8,12,13,11,10,16,8,10,0,13,11],
[11,14,10,11,12,14,16,9,11,13,12,12,12,0,10],
[16,16,9,11,14,13,15,10,15,16,8,14,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,17,11,8,13,14,11,15,14,17,17,16,12],
[12,0,12,17,14,14,13,12,13,11,18,15,19,13,12],
[12,13,0,15,11,13,15,10,12,13,15,15,17,14,11],
[8,8,10,0,6,7,9,7,8,12,10,11,11,11,8],
[14,11,14,19,0,13,13,13,13,17,15,14,17,13,11],
[17,11,12,18,12,0,13,13,15,16,19,18,18,16,12],
[12,12,10,16,12,12,0,13,12,12,14,13,14,13,13],
[11,13,15,18,12,12,12,0,11,12,15,15,15,15,12],
[14,12,13,17,12,10,13,14,0,14,14,15,16,15,13],
[10,14,12,13,8,9,13,13,11,0,15,15,15,15,11],
[11,7,10,15,10,6,11,10,11,10,0,12,13,11,8],
[8,10,10,14,11,7,12,10,10,10,13,0,12,12,9],
[8,6,8,14,8,7,11,10,9,10,12,13,0,9,9],
[9,12,11,14,12,9,12,10,10,10,14,13,16,0,12],
[13,13,14,17,14,13,12,13,12,14,17,16,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,6,4,7,7,9,6,10,8,9,9,11,6],
[19,0,14,10,13,15,15,14,12,13,14,16,16,17,12],
[17,11,0,14,12,12,15,17,11,13,17,16,15,17,12],
[19,15,11,0,12,15,13,16,11,15,15,18,17,16,14],
[21,12,13,13,0,12,16,17,12,12,16,15,16,16,13],
[18,10,13,10,13,0,14,14,13,11,12,18,10,14,11],
[18,10,10,12,9,11,0,12,7,12,11,14,12,12,11],
[16,11,8,9,8,11,13,0,10,13,14,12,9,14,9],
[19,13,14,14,13,12,18,15,0,16,18,18,12,14,12],
[15,12,12,10,13,14,13,12,9,0,15,16,9,12,10],
[17,11,8,10,9,13,14,11,7,10,0,14,10,14,12],
[16,9,9,7,10,7,11,13,7,9,11,0,10,14,10],
[16,9,10,8,9,15,13,16,13,16,15,15,0,16,13],
[14,8,8,9,9,11,13,11,11,13,11,11,9,0,7],
[19,13,13,11,12,14,14,16,13,15,13,15,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,9,12,11,15,17,9,10,16,12,11,15,16,15],
[5,0,7,9,7,8,13,7,12,10,9,8,10,9,15],
[16,18,0,12,16,15,15,14,16,14,15,12,14,14,20],
[13,16,13,0,14,14,18,17,15,14,14,16,14,11,16],
[14,18,9,11,0,15,20,13,13,15,11,11,16,13,20],
[10,17,10,11,10,0,19,11,12,19,7,13,17,16,23],
[8,12,10,7,5,6,0,7,8,12,9,11,12,8,22],
[16,18,11,8,12,14,18,0,13,17,12,12,15,12,21],
[15,13,9,10,12,13,17,12,0,16,9,8,17,11,20],
[9,15,11,11,10,6,13,8,9,0,9,9,12,7,17],
[13,16,10,11,14,18,16,13,16,16,0,13,16,14,19],
[14,17,13,9,14,12,14,13,17,16,12,0,16,16,18],
[10,15,11,11,9,8,13,10,8,13,9,9,0,13,20],
[9,16,11,14,12,9,17,13,14,18,11,9,12,0,19],
[10,10,5,9,5,2,3,4,5,8,6,7,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,11,11,10,8,9,6,12,10,6,10,17,11,9],
[20,0,15,13,15,9,18,13,18,18,13,11,22,15,16],
[14,10,0,8,11,5,12,7,12,12,3,6,19,8,12],
[14,12,17,0,17,9,18,14,17,13,13,11,19,15,12],
[15,10,14,8,0,5,15,10,14,15,9,9,21,8,8],
[17,16,20,16,20,0,19,14,15,14,13,12,19,13,10],
[16,7,13,7,10,6,0,7,15,11,8,10,14,9,9],
[19,12,18,11,15,11,18,0,14,13,14,17,19,9,9],
[13,7,13,8,11,10,10,11,0,11,12,13,15,14,8],
[15,7,13,12,10,11,14,12,14,0,6,9,13,10,8],
[19,12,22,12,16,12,17,11,13,19,0,10,21,14,12],
[15,14,19,14,16,13,15,8,12,16,15,0,18,15,11],
[8,3,6,6,4,6,11,6,10,12,4,7,0,9,3],
[14,10,17,10,17,12,16,16,11,15,11,10,16,0,7],
[16,9,13,13,17,15,16,16,17,17,13,14,22,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,14,14,10,18,13,16,13,14,16,12,13,14],
[13,0,10,11,14,14,14,14,12,10,11,13,15,11,15],
[10,15,0,11,11,9,14,9,13,11,13,12,13,8,13],
[11,14,14,0,11,10,13,13,12,11,12,13,10,11,15],
[11,11,14,14,0,8,14,13,11,12,13,13,12,12,14],
[15,11,16,15,17,0,12,14,16,15,12,13,10,14,18],
[7,11,11,12,11,13,0,14,16,14,8,15,12,12,15],
[12,11,16,12,12,11,11,0,14,15,12,13,12,15,14],
[9,13,12,13,14,9,9,11,0,11,8,13,11,10,13],
[12,15,14,14,13,10,11,10,14,0,12,11,11,12,14],
[11,14,12,13,12,13,17,13,17,13,0,16,13,14,15],
[9,12,13,12,12,12,10,12,12,14,9,0,13,11,13],
[13,10,12,15,13,15,13,13,14,14,12,12,0,14,12],
[12,14,17,14,13,11,13,10,15,13,11,14,11,0,15],
[11,10,12,10,11,7,10,11,12,11,10,12,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,16,21,10,20,10,16,14,13,17,19,10,18],
[4,0,8,4,9,6,5,6,9,12,6,5,8,0,10],
[6,17,0,11,18,10,15,6,9,14,4,13,12,9,16],
[9,21,14,0,13,15,12,12,15,21,14,14,13,16,15],
[4,16,7,12,0,10,11,6,7,16,6,12,7,10,7],
[15,19,15,10,15,0,15,14,12,20,14,15,17,6,13],
[5,20,10,13,14,10,0,2,8,10,3,12,13,8,9],
[15,19,19,13,19,11,23,0,11,15,10,14,17,12,18],
[9,16,16,10,18,13,17,14,0,20,15,17,14,13,14],
[11,13,11,4,9,5,15,10,5,0,7,8,13,0,11],
[12,19,21,11,19,11,22,15,10,18,0,12,12,8,17],
[8,20,12,11,13,10,13,11,8,17,13,0,13,5,14],
[6,17,13,12,18,8,12,8,11,12,13,12,0,10,19],
[15,25,16,9,15,19,17,13,12,25,17,20,15,0,20],
[7,15,9,10,18,12,16,7,11,14,8,11,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,13,18,13,21,11,14,10,18,20,18,18,17],
[11,0,14,12,15,12,22,14,12,11,15,17,7,12,14],
[12,11,0,11,18,16,16,14,15,14,15,10,15,16,18],
[12,13,14,0,15,13,22,11,10,11,8,16,14,11,14],
[7,10,7,10,0,11,16,11,6,10,7,13,4,4,10],
[12,13,9,12,14,0,14,7,13,13,12,16,13,6,16],
[4,3,9,3,9,11,0,7,6,7,10,13,10,7,6],
[14,11,11,14,14,18,18,0,11,11,14,10,11,14,15],
[11,13,10,15,19,12,19,14,0,14,8,14,10,8,10],
[15,14,11,14,15,12,18,14,11,0,12,13,14,15,13],
[7,10,10,17,18,13,15,11,17,13,0,13,14,11,17],
[5,8,15,9,12,9,12,15,11,12,12,0,12,9,11],
[7,18,10,11,21,12,15,14,15,11,11,13,0,12,11],
[7,13,9,14,21,19,18,11,17,10,14,16,13,0,17],
[8,11,7,11,15,9,19,10,15,12,8,14,14,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,13,8,18,8,18,7,4,10,7,14,7,14],
[11,0,10,11,16,22,9,10,7,10,14,8,17,11,18],
[17,15,0,14,15,19,12,18,10,7,6,9,13,13,19],
[12,14,11,0,17,17,12,13,15,10,11,5,10,11,18],
[17,9,10,8,0,16,8,13,13,6,6,3,7,9,19],
[7,3,6,8,9,0,2,7,0,5,5,1,6,0,11],
[17,16,13,13,17,23,0,23,20,10,15,11,17,13,21],
[7,15,7,12,12,18,2,0,4,7,9,0,10,6,15],
[18,18,15,10,12,25,5,21,0,8,13,9,18,13,19],
[21,15,18,15,19,20,15,18,17,0,9,14,17,15,19],
[15,11,19,14,19,20,10,16,12,16,0,10,13,15,19],
[18,17,16,20,22,24,14,25,16,11,15,0,22,14,24],
[11,8,12,15,18,19,8,15,7,8,12,3,0,13,16],
[18,14,12,14,16,25,12,19,12,10,10,11,12,0,22],
[11,7,6,7,6,14,4,10,6,6,6,1,9,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,21,21,17,21,17,21,21,15,21,21,19,17,21],
[14,0,14,17,6,13,6,13,10,10,13,21,16,6,13],
[4,11,0,11,6,17,17,15,21,11,11,15,15,17,17],
[4,8,14,0,6,10,6,18,18,4,11,18,12,6,10],
[8,19,19,19,0,19,15,15,25,19,19,19,19,25,15],
[4,12,8,15,6,0,4,15,18,4,11,12,12,10,6],
[8,19,8,19,10,21,0,15,21,4,15,15,19,17,13],
[4,12,10,7,10,10,10,0,10,4,7,18,12,10,10],
[4,15,4,7,0,7,4,15,0,0,3,15,12,10,3],
[10,15,14,21,6,21,21,21,25,0,21,21,15,13,9],
[4,12,14,14,6,14,10,18,22,4,0,18,16,10,10],
[4,4,10,7,6,13,10,7,10,4,7,0,12,10,6],
[6,9,10,13,6,13,6,13,13,10,9,13,0,9,13],
[8,19,8,19,0,15,8,15,15,12,15,15,16,0,15],
[4,12,8,15,10,19,12,15,22,16,15,19,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,10,12,7,9,11,13,13,14,10,12,10,7],
[17,0,13,14,14,13,12,13,18,17,18,13,15,15,19],
[19,12,0,13,18,9,11,15,16,17,20,13,15,14,14],
[15,11,12,0,14,8,12,14,14,18,19,10,13,12,14],
[13,11,7,11,0,6,9,12,13,10,15,8,13,10,8],
[18,12,16,17,19,0,13,20,18,16,16,15,19,16,17],
[16,13,14,13,16,12,0,15,14,17,18,14,13,15,18],
[14,12,10,11,13,5,10,0,13,10,12,7,8,11,11],
[12,7,9,11,12,7,11,12,0,10,14,9,13,12,12],
[12,8,8,7,15,9,8,15,15,0,14,6,13,7,13],
[11,7,5,6,10,9,7,13,11,11,0,7,12,9,8],
[15,12,12,15,17,10,11,18,16,19,18,0,13,10,11],
[13,10,10,12,12,6,12,17,12,12,13,12,0,13,15],
[15,10,11,13,15,9,10,14,13,18,16,15,12,0,13],
[18,6,11,11,17,8,7,14,13,12,17,14,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,7,14,13,10,9,11,9,11,12,11,12,10],
[12,0,11,9,15,12,14,12,8,9,17,10,11,15,11],
[17,14,0,8,13,15,14,11,14,8,14,13,12,15,13],
[18,16,17,0,18,16,17,17,14,12,15,17,11,19,16],
[11,10,12,7,0,13,12,11,12,7,12,12,10,10,12],
[12,13,10,9,12,0,13,12,13,8,12,13,10,12,12],
[15,11,11,8,13,12,0,11,7,6,10,12,12,10,9],
[16,13,14,8,14,13,14,0,13,9,13,16,12,14,14],
[14,17,11,11,13,12,18,12,0,8,16,15,12,12,14],
[16,16,17,13,18,17,19,16,17,0,15,16,11,15,16],
[14,8,11,10,13,13,15,12,9,10,0,10,10,11,9],
[13,15,12,8,13,12,13,9,10,9,15,0,15,15,10],
[14,14,13,14,15,15,13,13,13,14,15,10,0,17,13],
[13,10,10,6,15,13,15,11,13,10,14,10,8,0,11],
[15,14,12,9,13,13,16,11,11,9,16,15,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,15,9,11,10,16,13,15,16,15,17,12,14],
[13,0,12,10,10,7,9,13,11,15,11,12,13,10,12],
[12,13,0,13,14,10,12,17,13,15,15,15,18,8,13],
[10,15,12,0,9,11,10,13,18,14,13,12,15,10,16],
[16,15,11,16,0,14,17,17,15,18,18,18,18,13,15],
[14,18,15,14,11,0,14,17,15,18,15,13,15,15,16],
[15,16,13,15,8,11,0,13,14,16,15,14,16,13,11],
[9,12,8,12,8,8,12,0,14,17,11,13,10,9,9],
[12,14,12,7,10,10,11,11,0,12,9,10,11,11,13],
[10,10,10,11,7,7,9,8,13,0,12,11,13,9,12],
[9,14,10,12,7,10,10,14,16,13,0,12,12,11,9],
[10,13,10,13,7,12,11,12,15,14,13,0,11,10,14],
[8,12,7,10,7,10,9,15,14,12,13,14,0,9,11],
[13,15,17,15,12,10,12,16,14,16,14,15,16,0,13],
[11,13,12,9,10,9,14,16,12,13,16,11,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,11,13,18,10,15,17,18,17,16,16,12,10],
[7,0,13,8,8,12,7,13,8,12,12,13,13,8,6],
[8,12,0,6,6,15,6,13,3,11,11,14,17,5,6],
[14,17,19,0,15,19,12,21,15,20,16,15,19,12,12],
[12,17,19,10,0,21,8,18,8,10,14,15,17,9,9],
[7,13,10,6,4,0,9,13,6,13,10,9,9,4,8],
[15,18,19,13,17,16,0,22,16,15,12,17,20,13,11],
[10,12,12,4,7,12,3,0,4,8,11,7,14,6,11],
[8,17,22,10,17,19,9,21,0,16,14,18,19,12,9],
[7,13,14,5,15,12,10,17,9,0,12,13,12,10,11],
[8,13,14,9,11,15,13,14,11,13,0,12,16,11,9],
[9,12,11,10,10,16,8,18,7,12,13,0,10,13,9],
[9,12,8,6,8,16,5,11,6,13,9,15,0,7,7],
[13,17,20,13,16,21,12,19,13,15,14,12,18,0,13],
[15,19,19,13,16,17,14,14,16,14,16,16,18,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,6,11,10,11,3,9,8,10,7,5,8,8],
[14,0,9,12,12,16,18,12,12,14,15,12,9,10,8],
[16,16,0,7,15,11,10,7,11,5,10,7,5,5,12],
[19,13,18,0,10,14,8,7,13,13,14,8,9,9,11],
[14,13,10,15,0,15,13,11,15,9,16,13,6,11,13],
[15,9,14,11,10,0,14,10,12,11,9,10,6,9,9],
[14,7,15,17,12,11,0,13,17,10,11,11,4,4,11],
[22,13,18,18,14,15,12,0,19,16,18,19,14,15,17],
[16,13,14,12,10,13,8,6,0,16,14,10,8,9,13],
[17,11,20,12,16,14,15,9,9,0,10,13,9,13,15],
[15,10,15,11,9,16,14,7,11,15,0,12,11,15,14],
[18,13,18,17,12,15,14,6,15,12,13,0,10,10,17],
[20,16,20,16,19,19,21,11,17,16,14,15,0,20,13],
[17,15,20,16,14,16,21,10,16,12,10,15,5,0,15],
[17,17,13,14,12,16,14,8,12,10,11,8,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,14,13,12,18,19,13,9,22,13,19,8,18],
[15,0,12,15,15,11,20,19,14,11,19,13,14,16,19],
[10,13,0,16,19,10,20,14,10,8,18,13,15,12,18],
[11,10,9,0,17,15,11,11,12,6,17,14,15,5,18],
[12,10,6,8,0,12,11,7,10,3,17,13,14,7,11],
[13,14,15,10,13,0,16,15,10,13,16,12,16,12,18],
[7,5,5,14,14,9,0,5,7,4,14,12,15,6,11],
[6,6,11,14,18,10,20,0,11,10,14,11,16,12,19],
[12,11,15,13,15,15,18,14,0,9,14,12,14,11,19],
[16,14,17,19,22,12,21,15,16,0,24,16,21,10,20],
[3,6,7,8,8,9,11,11,11,1,0,5,11,5,12],
[12,12,12,11,12,13,13,14,13,9,20,0,15,9,15],
[6,11,10,10,11,9,10,9,11,4,14,10,0,7,12],
[17,9,13,20,18,13,19,13,14,15,20,16,18,0,23],
[7,6,7,7,14,7,14,6,6,5,13,10,13,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,16,12,13,10,16,13,14,12,16,15,12,10],
[13,0,18,17,15,17,10,18,14,15,15,15,16,12,14],
[11,7,0,13,12,12,8,12,10,9,8,10,13,9,7],
[9,8,12,0,12,13,9,10,8,7,9,10,13,12,10],
[13,10,13,13,0,13,13,17,11,12,12,12,15,11,11],
[12,8,13,12,12,0,7,15,10,8,10,10,10,11,9],
[15,15,17,16,12,18,0,18,17,12,15,13,16,13,10],
[9,7,13,15,8,10,7,0,9,9,13,12,13,11,8],
[12,11,15,17,14,15,8,16,0,14,12,12,12,11,7],
[11,10,16,18,13,17,13,16,11,0,17,16,16,14,11],
[13,10,17,16,13,15,10,12,13,8,0,14,17,13,10],
[9,10,15,15,13,15,12,13,13,9,11,0,12,12,10],
[10,9,12,12,10,15,9,12,13,9,8,13,0,8,9],
[13,13,16,13,14,14,12,14,14,11,12,13,17,0,9],
[15,11,18,15,14,16,15,17,18,14,15,15,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,15,16,11,12,12,11,6,15,12,11,16,20],
[11,0,13,18,13,14,11,9,11,11,14,11,9,13,15],
[9,12,0,7,13,7,12,6,13,13,10,9,16,14,8],
[10,7,18,0,18,19,16,14,17,11,19,16,14,19,20],
[9,12,12,7,0,8,1,2,13,10,12,5,9,12,9],
[14,11,18,6,17,0,15,12,15,15,17,12,17,22,18],
[13,14,13,9,24,10,0,7,14,10,17,15,13,17,17],
[13,16,19,11,23,13,18,0,18,10,17,10,18,23,23],
[14,14,12,8,12,10,11,7,0,8,10,3,14,16,10],
[19,14,12,14,15,10,15,15,17,0,16,17,15,16,18],
[10,11,15,6,13,8,8,8,15,9,0,7,15,13,10],
[13,14,16,9,20,13,10,15,22,8,18,0,22,20,22],
[14,16,9,11,16,8,12,7,11,10,10,3,0,17,15],
[9,12,11,6,13,3,8,2,9,9,12,5,8,0,4],
[5,10,17,5,16,7,8,2,15,7,15,3,10,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,16,11,13,17,16,16,11,9,10,10,17,16],
[13,0,14,14,4,10,15,6,5,7,1,6,12,6,14],
[7,11,0,10,5,3,16,7,16,9,5,12,10,7,12],
[9,11,15,0,6,4,15,6,12,9,7,4,8,8,8],
[14,21,20,19,0,8,20,8,20,11,9,14,12,9,21],
[12,15,22,21,17,0,21,15,16,14,11,15,20,10,23],
[8,10,9,10,5,4,0,6,10,6,6,8,6,10,13],
[9,19,18,19,17,10,19,0,17,11,11,10,15,18,23],
[9,20,9,13,5,9,15,8,0,11,6,16,8,13,14],
[14,18,16,16,14,11,19,14,14,0,13,13,15,11,17],
[16,24,20,18,16,14,19,14,19,12,0,14,15,14,23],
[15,19,13,21,11,10,17,15,9,12,11,0,11,15,15],
[15,13,15,17,13,5,19,10,17,10,10,14,0,13,13],
[8,19,18,17,16,15,15,7,12,14,11,10,12,0,20],
[9,11,13,17,4,2,12,2,11,8,2,10,12,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,14,13,14,17,22,17,16,22,14,12,17,18],
[10,0,12,13,8,9,16,18,13,12,14,8,11,13,13],
[9,13,0,10,9,5,10,12,8,10,10,6,12,7,12],
[11,12,15,0,12,8,16,16,14,13,11,13,9,15,14],
[12,17,16,13,0,13,16,21,17,16,19,15,13,13,16],
[11,16,20,17,12,0,15,20,20,15,13,14,14,13,15],
[8,9,15,9,9,10,0,15,14,10,16,5,11,10,12],
[3,7,13,9,4,5,10,0,11,11,12,8,8,11,11],
[8,12,17,11,8,5,11,14,0,14,13,13,12,11,13],
[9,13,15,12,9,10,15,14,11,0,9,7,13,12,15],
[3,11,15,14,6,12,9,13,12,16,0,10,12,13,12],
[11,17,19,12,10,11,20,17,12,18,15,0,17,14,20],
[13,14,13,16,12,11,14,17,13,12,13,8,0,15,14],
[8,12,18,10,12,12,15,14,14,13,12,11,10,0,14],
[7,12,13,11,9,10,13,14,12,10,13,5,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,7,11,13,10,10,12,11,13,11,10,16,14,12],
[12,0,9,12,11,8,9,13,14,11,13,13,13,15,12],
[18,16,0,15,11,13,12,15,15,14,14,13,12,11,15],
[14,13,10,0,9,11,14,7,13,12,12,13,13,11,14],
[12,14,14,16,0,11,11,16,10,16,11,14,12,13,13],
[15,17,12,14,14,0,15,14,17,13,13,17,16,17,15],
[15,16,13,11,14,10,0,15,14,14,14,15,15,15,14],
[13,12,10,18,9,11,10,0,13,13,14,11,12,12,14],
[14,11,10,12,15,8,11,12,0,12,11,13,16,17,13],
[12,14,11,13,9,12,11,12,13,0,11,12,10,14,14],
[14,12,11,13,14,12,11,11,14,14,0,13,13,14,13],
[15,12,12,12,11,8,10,14,12,13,12,0,13,17,12],
[9,12,13,12,13,9,10,13,9,15,12,12,0,15,13],
[11,10,14,14,12,8,10,13,8,11,11,8,10,0,11],
[13,13,10,11,12,10,11,11,12,11,12,13,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,5,13,20,13,13,17,10,18,18,5,13,8],
[7,0,8,5,0,7,12,7,12,10,12,12,7,13,0],
[12,17,0,12,5,12,12,12,12,17,12,12,17,5,5],
[20,20,13,0,13,20,20,20,17,20,25,25,12,13,8],
[12,25,20,12,0,20,20,17,12,17,12,12,17,13,20],
[5,18,13,5,5,0,13,5,5,10,5,5,5,13,8],
[12,13,13,5,5,12,0,5,12,10,12,12,5,13,5],
[12,18,13,5,8,20,20,0,12,10,20,20,10,13,13],
[8,13,13,8,13,20,13,13,0,13,8,8,13,8,8],
[15,15,8,5,8,15,15,15,12,0,20,20,7,13,8],
[7,13,13,0,13,20,13,5,17,5,0,20,5,8,8],
[7,13,13,0,13,20,13,5,17,5,5,0,5,8,8],
[20,18,8,13,8,20,20,15,12,18,20,20,0,13,8],
[12,12,20,12,12,12,12,12,17,12,17,17,12,0,7],
[17,25,20,17,5,17,20,12,17,17,17,17,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,5,17,12,12,17,8,12,12,9,12,12,8],
[17,0,15,9,13,8,9,9,7,12,11,16,13,14,14],
[14,10,0,7,13,8,11,15,7,16,9,1,15,14,6],
[20,16,18,0,24,22,24,24,10,19,22,18,24,13,13],
[8,12,12,1,0,12,9,13,9,13,12,8,16,5,5],
[13,17,17,3,13,0,7,15,11,14,11,10,18,14,6],
[13,16,14,1,16,18,0,15,6,15,18,12,17,14,10],
[8,16,10,1,12,10,10,0,6,7,14,8,17,5,5],
[17,18,18,15,16,14,19,19,0,16,18,19,22,12,12],
[13,13,9,6,12,11,10,18,9,0,15,10,21,10,6],
[13,14,16,3,13,14,7,11,7,10,0,11,13,14,6],
[16,9,24,7,17,15,13,17,6,15,14,0,20,17,13],
[13,12,10,1,9,7,8,8,3,4,12,5,0,4,6],
[13,11,11,12,20,11,11,20,13,15,11,8,21,0,10],
[17,11,19,12,20,19,15,20,13,19,19,12,19,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,11,7,3,7,3,3,3,7,7,0,0,0],
[22,0,22,19,14,3,15,7,19,14,7,22,11,7,8],
[22,3,0,22,14,3,10,10,22,17,10,14,7,10,11],
[14,6,3,0,7,3,10,6,6,6,3,10,0,3,3],
[18,11,11,18,0,14,15,3,11,11,10,11,3,15,8],
[22,22,22,22,11,0,22,14,22,22,7,22,14,19,19],
[18,10,15,15,10,3,0,6,18,13,10,10,7,7,18],
[22,18,15,19,22,11,19,0,19,18,7,19,15,15,15],
[22,6,3,19,14,3,7,6,0,10,7,14,7,7,8],
[22,11,8,19,14,3,12,7,15,0,7,12,0,7,8],
[18,18,15,22,15,18,15,18,18,18,0,15,15,12,12],
[18,3,11,15,14,3,15,6,11,13,10,0,0,7,8],
[25,14,18,25,22,11,18,10,18,25,10,25,0,18,11],
[25,18,15,22,10,6,18,10,18,18,13,18,7,0,11],
[25,17,14,22,17,6,7,10,17,17,13,17,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,14,10,12,12,10,12,15,9,13,12,8,13],
[9,0,13,12,10,10,12,10,12,12,10,15,12,10,14],
[10,12,0,14,9,10,11,7,13,13,10,15,9,8,14],
[11,13,11,0,9,9,14,11,15,10,9,11,14,7,13],
[15,15,16,16,0,11,14,15,16,18,14,19,13,15,16],
[13,15,15,16,14,0,13,14,13,14,13,16,10,10,16],
[13,13,14,11,11,12,0,13,13,14,12,15,12,7,15],
[15,15,18,14,10,11,12,0,18,18,12,15,12,10,15],
[13,13,12,10,9,12,12,7,0,10,8,13,11,10,13],
[10,13,12,15,7,11,11,7,15,0,9,11,10,8,14],
[16,15,15,16,11,12,13,13,17,16,0,17,11,12,17],
[12,10,10,14,6,9,10,10,12,14,8,0,9,9,11],
[13,13,16,11,12,15,13,13,14,15,14,16,0,10,13],
[17,15,17,18,10,15,18,15,15,17,13,16,15,0,15],
[12,11,11,12,9,9,10,10,12,11,8,14,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,15,14,16,13,14,17,12,17,9,13,14,13],
[8,0,10,12,15,13,10,10,8,9,12,9,12,13,9],
[12,15,0,17,16,18,12,11,18,11,13,12,17,14,14],
[10,13,8,0,12,10,12,11,13,12,13,12,14,12,11],
[11,10,9,13,0,16,11,7,14,9,14,8,15,16,10],
[9,12,7,15,9,0,11,9,14,8,14,11,14,11,13],
[12,15,13,13,14,14,0,11,14,14,14,11,16,16,13],
[11,15,14,14,18,16,14,0,17,13,16,13,15,14,12],
[8,17,7,12,11,11,11,8,0,10,12,9,15,13,11],
[13,16,14,13,16,17,11,12,15,0,13,11,14,14,9],
[8,13,12,12,11,11,11,9,13,12,0,8,12,15,8],
[16,16,13,13,17,14,14,12,16,14,17,0,16,15,14],
[12,13,8,11,10,11,9,10,10,11,13,9,0,14,12],
[11,12,11,13,9,14,9,11,12,11,10,10,11,0,11],
[12,16,11,14,15,12,12,13,14,16,17,11,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,17,11,11,15,8,7,12,21,14,13,13,7],
[7,0,9,10,8,13,13,12,8,7,14,8,10,9,5],
[11,16,0,19,14,11,15,14,12,13,13,16,16,15,10],
[8,15,6,0,7,11,12,8,10,7,12,12,8,9,7],
[14,17,11,18,0,15,17,14,12,18,17,17,16,14,10],
[14,12,14,14,10,0,13,12,15,9,15,14,11,9,13],
[10,12,10,13,8,12,0,9,8,13,14,12,12,10,8],
[17,13,11,17,11,13,16,0,9,15,18,17,17,13,15],
[18,17,13,15,13,10,17,16,0,14,18,18,13,12,16],
[13,18,12,18,7,16,12,10,11,0,15,17,15,10,9],
[4,11,12,13,8,10,11,7,7,10,0,10,12,12,6],
[11,17,9,13,8,11,13,8,7,8,15,0,15,11,5],
[12,15,9,17,9,14,13,8,12,10,13,10,0,8,10],
[12,16,10,16,11,16,15,12,13,15,13,14,17,0,12],
[18,20,15,18,15,12,17,10,9,16,19,20,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,8,11,14,12,8,10,7,15,11,13,11,13],
[12,0,11,6,11,18,9,12,10,6,13,11,13,11,16],
[14,14,0,7,10,17,12,12,9,13,15,11,9,12,9],
[17,19,18,0,18,18,17,16,13,15,16,15,12,16,16],
[14,14,15,7,0,14,15,11,13,13,13,13,11,13,13],
[11,7,8,7,11,0,9,9,8,9,9,11,6,8,8],
[13,16,13,8,10,16,0,9,12,14,16,13,10,14,16],
[17,13,13,9,14,16,16,0,13,8,14,13,11,16,14],
[15,15,16,12,12,17,13,12,0,12,16,15,11,13,14],
[18,19,12,10,12,16,11,17,13,0,17,13,14,15,15],
[10,12,10,9,12,16,9,11,9,8,0,11,7,12,11],
[14,14,14,10,12,14,12,12,10,12,14,0,10,15,15],
[12,12,16,13,14,19,15,14,14,11,18,15,0,14,16],
[14,14,13,9,12,17,11,9,12,10,13,10,11,0,11],
[12,9,16,9,12,17,9,11,11,10,14,10,9,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,9,15,15,12,14,14,6,8,7,10,19,19],
[10,0,11,12,16,17,10,13,12,9,10,6,5,14,10],
[14,14,0,10,13,18,14,12,10,8,10,14,15,20,18],
[16,13,15,0,23,15,15,15,11,14,19,15,13,20,15],
[10,9,12,2,0,8,16,3,9,5,1,11,11,17,16],
[10,8,7,10,17,0,16,15,8,9,9,10,7,17,16],
[13,15,11,10,9,9,0,10,17,6,8,13,10,15,12],
[11,12,13,10,22,10,15,0,7,6,8,14,14,19,18],
[11,13,15,14,16,17,8,18,0,6,12,12,9,19,12],
[19,16,17,11,20,16,19,19,19,0,9,16,10,20,19],
[17,15,15,6,24,16,17,17,13,16,0,17,15,21,18],
[18,19,11,10,14,15,12,11,13,9,8,0,10,17,20],
[15,20,10,12,14,18,15,11,16,15,10,15,0,15,19],
[6,11,5,5,8,8,10,6,6,5,4,8,10,0,8],
[6,15,7,10,9,9,13,7,13,6,7,5,6,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,10,12,12,16,16,15,11,12,13,10,14,13],
[12,0,9,9,12,12,12,16,15,13,12,17,13,14,15],
[12,16,0,12,15,12,12,15,15,13,13,15,10,15,14],
[15,16,13,0,17,15,14,17,12,13,13,15,12,15,15],
[13,13,10,8,0,13,11,16,13,11,7,14,11,15,12],
[13,13,13,10,12,0,17,18,15,15,13,15,14,14,16],
[9,13,13,11,14,8,0,17,12,14,10,16,12,16,13],
[9,9,10,8,9,7,8,0,13,11,10,11,10,12,13],
[10,10,10,13,12,10,13,12,0,11,8,15,9,11,13],
[14,12,12,12,14,10,11,14,14,0,13,12,12,16,11],
[13,13,12,12,18,12,15,15,17,12,0,15,12,16,13],
[12,8,10,10,11,10,9,14,10,13,10,0,8,14,10],
[15,12,15,13,14,11,13,15,16,13,13,17,0,18,16],
[11,11,10,10,10,11,9,13,14,9,9,11,7,0,14],
[12,10,11,10,13,9,12,12,12,14,12,15,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,19,16,14,12,11,13,19,19,18,14,9,14],
[8,0,18,11,16,9,11,11,11,10,19,13,14,10,12],
[9,7,0,10,8,11,10,9,9,10,11,12,11,9,7],
[6,14,15,0,15,10,13,9,14,12,13,19,13,12,10],
[9,9,17,10,0,11,11,11,13,12,17,15,13,9,15],
[11,16,14,15,14,0,12,11,14,16,18,20,12,10,15],
[13,14,15,12,14,13,0,14,14,14,18,18,14,12,12],
[14,14,16,16,14,14,11,0,15,16,16,17,12,12,17],
[12,14,16,11,12,11,11,10,0,14,15,17,14,11,13],
[6,15,15,13,13,9,11,9,11,0,16,15,11,10,9],
[6,6,14,12,8,7,7,9,10,9,0,13,7,9,9],
[7,12,13,6,10,5,7,8,8,10,12,0,10,7,9],
[11,11,14,12,12,13,11,13,11,14,18,15,0,9,12],
[16,15,16,13,16,15,13,13,14,15,16,18,16,0,12],
[11,13,18,15,10,10,13,8,12,16,16,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,15,11,8,5,8,10,9,8,10,5,11,9,22],
[18,0,15,18,10,6,11,18,14,9,14,10,16,16,22],
[10,10,0,13,10,7,11,12,11,8,9,11,10,10,13],
[14,7,12,0,9,7,7,5,9,7,9,8,8,5,13],
[17,15,15,16,0,13,19,15,14,16,10,13,13,15,18],
[20,19,18,18,12,0,14,15,17,12,12,11,12,12,21],
[17,14,14,18,6,11,0,17,11,11,12,11,17,16,18],
[15,7,13,20,10,10,8,0,13,8,8,5,8,8,20],
[16,11,14,16,11,8,14,12,0,6,7,8,13,13,24],
[17,16,17,18,9,13,14,17,19,0,15,8,15,10,21],
[15,11,16,16,15,13,13,17,18,10,0,11,18,10,21],
[20,15,14,17,12,14,14,20,17,17,14,0,14,15,19],
[14,9,15,17,12,13,8,17,12,10,7,11,0,8,22],
[16,9,15,20,10,13,9,17,12,15,15,10,17,0,20],
[3,3,12,12,7,4,7,5,1,4,4,6,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,10,11,10,11,11,11,10,14,10,11,9,10],
[15,0,18,15,9,14,15,15,14,11,16,11,15,17,12],
[12,7,0,13,10,11,13,11,11,10,16,10,11,12,10],
[15,10,12,0,7,12,15,12,14,8,14,10,9,13,9],
[14,16,15,18,0,12,16,15,13,10,18,13,12,14,11],
[15,11,14,13,13,0,13,11,12,10,12,13,12,9,11],
[14,10,12,10,9,12,0,10,10,7,14,10,8,11,6],
[14,10,14,13,10,14,15,0,14,11,18,15,12,15,10],
[14,11,14,11,12,13,15,11,0,9,16,11,10,16,11],
[15,14,15,17,15,15,18,14,16,0,22,14,12,15,12],
[11,9,9,11,7,13,11,7,9,3,0,8,7,7,9],
[15,14,15,15,12,12,15,10,14,11,17,0,14,15,13],
[14,10,14,16,13,13,17,13,15,13,18,11,0,13,13],
[16,8,13,12,11,16,14,10,9,10,18,10,12,0,10],
[15,13,15,16,14,14,19,15,14,13,16,12,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,12,10,7,8,10,12,14,14,10,7,10,12],
[15,0,12,15,10,12,13,11,11,14,15,14,13,10,16],
[17,13,0,13,12,15,14,17,12,12,15,12,14,10,9],
[13,10,12,0,13,14,13,13,13,16,16,12,11,12,17],
[15,15,13,12,0,12,13,13,14,14,11,14,8,13,12],
[18,13,10,11,13,0,12,13,14,12,12,14,14,11,10],
[17,12,11,12,12,13,0,11,18,12,15,15,9,12,16],
[15,14,8,12,12,12,14,0,12,12,13,14,14,11,11],
[13,14,13,12,11,11,7,13,0,13,11,13,10,12,12],
[11,11,13,9,11,13,13,13,12,0,12,15,9,12,10],
[11,10,10,9,14,13,10,12,14,13,0,12,12,11,13],
[15,11,13,13,11,11,10,11,12,10,13,0,9,12,14],
[18,12,11,14,17,11,16,11,15,16,13,16,0,14,13],
[15,15,15,13,12,14,13,14,13,13,14,13,11,0,13],
[13,9,16,8,13,15,9,14,13,15,12,11,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,9,11,13,7,4,13,8,12,12,8,12,8],
[15,0,9,8,16,15,10,7,9,13,11,10,16,10,8],
[18,16,0,5,14,16,10,5,11,12,12,17,11,15,10],
[16,17,20,0,18,20,10,15,16,13,14,17,15,18,8],
[14,9,11,7,0,14,8,10,12,9,12,12,14,10,8],
[12,10,9,5,11,0,8,4,9,5,15,11,10,11,7],
[18,15,15,15,17,17,0,10,14,10,18,16,11,17,10],
[21,18,20,10,15,21,15,0,13,14,20,18,19,18,12],
[12,16,14,9,13,16,11,12,0,12,15,18,17,15,12],
[17,12,13,12,16,20,15,11,13,0,17,17,13,13,8],
[13,14,13,11,13,10,7,5,10,8,0,13,11,11,8],
[13,15,8,8,13,14,9,7,7,8,12,0,15,8,7],
[17,9,14,10,11,15,14,6,8,12,14,10,0,10,13],
[13,15,10,7,15,14,8,7,10,12,14,17,15,0,13],
[17,17,15,17,17,18,15,13,13,17,17,18,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,2,10,3,12,6,12,8,5,5,9,6,11],
[18,0,18,14,15,12,11,14,12,11,16,10,15,12,14],
[18,7,0,11,13,12,10,11,12,8,8,12,15,11,11],
[23,11,14,0,15,11,17,16,19,13,16,13,15,11,10],
[15,10,12,10,0,9,14,15,15,9,15,6,12,13,8],
[22,13,13,14,16,0,15,18,20,12,15,9,18,11,13],
[13,14,15,8,11,10,0,15,19,7,9,7,16,10,9],
[19,11,14,9,10,7,10,0,12,10,9,11,13,11,9],
[13,13,13,6,10,5,6,13,0,6,6,7,12,8,10],
[17,14,17,12,16,13,18,15,19,0,14,16,17,16,15],
[20,9,17,9,10,10,16,16,19,11,0,9,16,14,13],
[20,15,13,12,19,16,18,14,18,9,16,0,17,12,9],
[16,10,10,10,13,7,9,12,13,8,9,8,0,12,8],
[19,13,14,14,12,14,15,14,17,9,11,13,13,0,9],
[14,11,14,15,17,12,16,16,15,10,12,16,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,0,19,10,22,14,7,0,3,0,7,0,13,13],
[22,0,0,19,10,19,19,12,5,3,12,7,12,17,18],
[25,25,0,19,25,25,25,12,18,17,18,17,22,25,18],
[6,6,6,0,13,20,20,10,6,6,6,13,6,13,13],
[15,15,0,12,0,22,19,12,5,3,12,14,12,13,18],
[3,6,0,5,3,0,7,0,3,3,0,0,0,10,6],
[11,6,0,5,6,18,0,12,11,3,11,3,8,13,18],
[18,13,13,15,13,25,13,0,18,13,13,10,18,20,20],
[25,20,7,19,20,22,14,7,0,10,10,14,19,20,13],
[22,22,8,19,22,22,22,12,15,0,15,22,22,22,18],
[25,13,7,19,13,25,14,12,15,10,0,7,12,20,18],
[18,18,8,12,11,25,22,15,11,3,18,0,15,18,18],
[25,13,3,19,13,25,17,7,6,3,13,10,0,20,13],
[12,8,0,12,12,15,12,5,5,3,5,7,5,0,8],
[12,7,7,12,7,19,7,5,12,7,7,7,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,15,15,11,13,11,13,10,14,9,14,14,12],
[12,0,14,15,10,13,11,11,14,13,13,7,14,12,9],
[8,11,0,9,8,7,8,8,13,10,8,6,12,8,8],
[10,10,16,0,8,11,10,13,15,16,9,6,13,6,11],
[10,15,17,17,0,13,14,15,18,15,13,9,14,10,10],
[14,12,18,14,12,0,14,15,18,14,11,10,18,11,11],
[12,14,17,15,11,11,0,14,17,17,13,11,12,12,11],
[14,14,17,12,10,10,11,0,16,11,11,11,16,11,14],
[12,11,12,10,7,7,8,9,0,12,9,7,12,8,8],
[15,12,15,9,10,11,8,14,13,0,11,7,17,12,10],
[11,12,17,16,12,14,12,14,16,14,0,9,15,10,9],
[16,18,19,19,16,15,14,14,18,18,16,0,19,16,12],
[11,11,13,12,11,7,13,9,13,8,10,6,0,10,10],
[11,13,17,19,15,14,13,14,17,13,15,9,15,0,9],
[13,16,17,14,15,14,14,11,17,15,16,13,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,11,14,16,16,19,13,16,17,9,15,19,9],
[13,0,15,12,15,14,17,17,16,15,16,13,13,20,13],
[8,10,0,11,12,6,10,14,12,11,10,9,12,16,13],
[14,13,14,0,13,12,12,13,11,14,13,12,11,16,10],
[11,10,13,12,0,9,10,17,12,13,16,8,15,16,7],
[9,11,19,13,16,0,15,15,14,16,16,8,17,17,11],
[9,8,15,13,15,10,0,15,12,16,13,9,11,19,11],
[6,8,11,12,8,10,10,0,14,12,12,6,14,12,8],
[12,9,13,14,13,11,13,11,0,12,10,11,10,16,11],
[9,10,14,11,12,9,9,13,13,0,16,9,11,16,11],
[8,9,15,12,9,9,12,13,15,9,0,11,10,17,10],
[16,12,16,13,17,17,16,19,14,16,14,0,13,18,9],
[10,12,13,14,10,8,14,11,15,14,15,12,0,15,12],
[6,5,9,9,9,8,6,13,9,9,8,7,10,0,8],
[16,12,12,15,18,14,14,17,14,14,15,16,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,5,0,9,1,1,13,4,1,1,5,1,0,1],
[24,0,25,16,24,12,24,24,24,24,12,16,24,24,20],
[20,0,0,0,20,8,20,8,12,12,12,16,12,20,12],
[25,9,25,0,25,13,25,13,12,25,21,17,25,20,21],
[16,1,5,0,0,5,16,5,4,16,13,5,17,12,13],
[24,13,17,12,20,0,16,24,16,16,12,16,16,12,12],
[24,1,5,0,9,9,0,13,12,4,13,5,13,12,1],
[12,1,17,12,20,1,12,0,4,12,13,17,13,12,13],
[21,1,13,13,21,9,13,21,0,13,13,17,13,13,13],
[24,1,13,0,9,9,21,13,12,0,13,5,21,20,9],
[24,13,13,4,12,13,12,12,12,12,0,4,24,24,12],
[20,9,9,8,20,9,20,8,8,20,21,0,21,20,21],
[24,1,13,0,8,9,12,12,12,4,1,4,0,20,9],
[25,1,5,5,13,13,13,13,12,5,1,5,5,0,1],
[24,5,13,4,12,13,24,12,12,16,13,4,16,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,13,18,13,18,14,12,15,10,14,11,17,11],
[11,0,16,10,13,12,12,9,7,11,8,12,7,9,8],
[10,9,0,6,10,8,9,11,9,11,8,9,7,10,7],
[12,15,19,0,14,13,13,11,13,15,9,12,10,9,11],
[7,12,15,11,0,11,11,10,8,11,4,12,7,11,8],
[12,13,17,12,14,0,15,14,8,15,12,13,11,11,13],
[7,13,16,12,14,10,0,8,8,11,7,15,9,10,9],
[11,16,14,14,15,11,17,0,11,11,9,16,9,11,12],
[13,18,16,12,17,17,17,14,0,14,13,14,8,14,10],
[10,14,14,10,14,10,14,14,11,0,8,14,10,14,11],
[15,17,17,16,21,13,18,16,12,17,0,17,9,16,14],
[11,13,16,13,13,12,10,9,11,11,8,0,9,10,10],
[14,18,18,15,18,14,16,16,17,15,16,16,0,16,12],
[8,16,15,16,14,14,15,14,11,11,9,15,9,0,9],
[14,17,18,14,17,12,16,13,15,14,11,15,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,14,18,16,9,10,16,21,19,21,10,16,18],
[14,0,15,10,15,18,17,14,18,17,18,21,16,18,24],
[6,10,0,10,15,15,9,13,16,16,17,19,12,17,22],
[11,15,15,0,16,15,11,11,17,23,17,18,14,11,19],
[7,10,10,9,0,13,9,9,16,13,23,13,4,13,16],
[9,7,10,10,12,0,6,5,11,14,14,12,9,9,10],
[16,8,16,14,16,19,0,10,15,19,15,18,13,15,17],
[15,11,12,14,16,20,15,0,15,17,20,18,11,18,19],
[9,7,9,8,9,14,10,10,0,10,12,10,7,10,14],
[4,8,9,2,12,11,6,8,15,0,16,10,6,11,17],
[6,7,8,8,2,11,10,5,13,9,0,13,3,10,11],
[4,4,6,7,12,13,7,7,15,15,12,0,7,7,14],
[15,9,13,11,21,16,12,14,18,19,22,18,0,17,21],
[9,7,8,14,12,16,10,7,15,14,15,18,8,0,18],
[7,1,3,6,9,15,8,6,11,8,14,11,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,13,10,12,9,13,11,12,12,9,11,14,9],
[15,0,14,13,12,14,11,14,13,12,12,12,11,12,12],
[13,11,0,11,13,11,12,12,11,14,10,14,13,13,12],
[12,12,14,0,14,12,13,14,11,17,9,13,14,13,8],
[15,13,12,11,0,14,16,14,11,14,10,13,10,14,9],
[13,11,14,13,11,0,11,12,12,13,9,11,13,11,9],
[16,14,13,12,9,14,0,15,8,14,13,12,12,18,11],
[12,11,13,11,11,13,10,0,10,15,10,13,12,14,7],
[14,12,14,14,14,13,17,15,0,15,11,15,14,13,10],
[13,13,11,8,11,12,11,10,10,0,12,12,12,17,9],
[13,13,15,16,15,16,12,15,14,13,0,15,16,15,13],
[16,13,11,12,12,14,13,12,10,13,10,0,11,14,14],
[14,14,12,11,15,12,13,13,11,13,9,14,0,14,12],
[11,13,12,12,11,14,7,11,12,8,10,11,11,0,10],
[16,13,13,17,16,16,14,18,15,16,12,11,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,16,12,9,16,13,11,13,14,15,8,9],
[11,0,9,11,13,11,8,8,12,7,10,12,8,9,6],
[12,16,0,15,15,10,14,15,17,13,16,16,13,11,11],
[10,14,10,0,15,9,8,12,11,10,11,13,9,11,6],
[9,12,10,10,0,8,9,10,10,5,9,10,11,8,6],
[13,14,15,16,17,0,15,13,13,9,16,15,12,14,11],
[16,17,11,17,16,10,0,15,15,13,16,12,13,11,9],
[9,17,10,13,15,12,10,0,13,10,12,12,12,11,9],
[12,13,8,14,15,12,10,12,0,10,13,14,12,13,9],
[14,18,12,15,20,16,12,15,15,0,14,14,13,11,12],
[12,15,9,14,16,9,9,13,12,11,0,9,11,9,7],
[11,13,9,12,15,10,13,13,11,11,16,0,11,10,8],
[10,17,12,16,14,13,12,13,13,12,14,14,0,12,9],
[17,16,14,14,17,11,14,14,12,14,16,15,13,0,14],
[16,19,14,19,19,14,16,16,16,13,18,17,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,12,9,11,13,12,9,10,11,9,11,13,11],
[17,0,17,13,15,14,12,13,16,15,14,12,13,17,15],
[12,8,0,11,10,8,9,7,8,8,10,7,12,11,9],
[13,12,14,0,13,12,11,13,13,13,14,15,12,11,14],
[16,10,15,12,0,12,12,11,12,12,10,13,12,13,10],
[14,11,17,13,13,0,11,11,12,13,14,12,14,17,13],
[12,13,16,14,13,14,0,11,14,14,16,14,15,17,16],
[13,12,18,12,14,14,14,0,12,14,15,15,13,15,13],
[16,9,17,12,13,13,11,13,0,13,12,12,12,15,15],
[15,10,17,12,13,12,11,11,12,0,10,10,10,13,13],
[14,11,15,11,15,11,9,10,13,15,0,12,11,16,16],
[16,13,18,10,12,13,11,10,13,15,13,0,13,14,15],
[14,12,13,13,13,11,10,12,13,15,14,12,0,12,15],
[12,8,14,14,12,8,8,10,10,12,9,11,13,0,11],
[14,10,16,11,15,12,9,12,10,12,9,10,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,20,15,20,20,16,20,15,15,21,15,15,15],
[15,0,10,10,10,10,10,11,20,15,10,15,10,10,10],
[15,15,0,20,9,14,10,10,10,5,14,15,5,9,14],
[5,15,5,0,14,5,10,10,10,5,5,15,5,9,14],
[10,15,16,11,0,10,5,10,15,10,5,15,0,10,10],
[5,15,11,20,15,0,10,10,10,5,14,15,0,9,14],
[5,15,15,15,20,15,0,11,16,5,15,15,11,15,15],
[9,14,15,15,15,15,14,0,14,9,9,14,4,10,14],
[5,5,15,15,10,15,9,11,0,0,9,10,10,10,15],
[10,10,20,20,15,20,20,16,25,0,20,10,10,15,20],
[10,15,11,20,20,11,10,16,16,5,0,10,11,15,15],
[4,10,10,10,10,10,10,11,15,15,15,0,10,10,10],
[10,15,20,20,25,25,14,21,15,15,14,15,0,25,20],
[10,15,16,16,15,16,10,15,15,10,10,15,0,0,14],
[10,15,11,11,15,11,10,11,10,5,10,15,5,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,17,15,12,15,17,18,16,14,14,13,17,15],
[9,0,8,9,11,9,6,14,11,7,7,9,9,11,12],
[13,17,0,14,16,11,15,17,16,15,15,13,11,14,15],
[8,16,11,0,12,10,12,16,10,10,10,9,9,15,16],
[10,14,9,13,0,7,13,11,10,13,12,12,11,13,15],
[13,16,14,15,18,0,18,16,16,11,13,11,12,15,13],
[10,19,10,13,12,7,0,15,11,12,11,12,12,13,12],
[8,11,8,9,14,9,10,0,12,12,10,11,9,9,11],
[7,14,9,15,15,9,14,13,0,13,12,9,7,14,10],
[9,18,10,15,12,14,13,13,12,0,9,8,11,14,12],
[11,18,10,15,13,12,14,15,13,16,0,12,12,14,14],
[11,16,12,16,13,14,13,14,16,17,13,0,12,14,13],
[12,16,14,16,14,13,13,16,18,14,13,13,0,18,13],
[8,14,11,10,12,10,12,16,11,11,11,11,7,0,13],
[10,13,10,9,10,12,13,14,15,13,11,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,10,13,16,12,11,11,13,12,13,12,16,10],
[14,0,14,13,12,14,15,14,13,11,13,14,13,14,11],
[11,11,0,9,11,14,13,13,11,12,9,13,12,11,12],
[15,12,16,0,16,15,14,13,13,12,12,13,13,16,12],
[12,13,14,9,0,13,14,13,11,12,10,15,14,14,12],
[9,11,11,10,12,0,15,9,13,12,14,12,12,15,10],
[13,10,12,11,11,10,0,14,10,9,14,9,15,13,10],
[14,11,12,12,12,16,11,0,11,14,11,12,14,13,11],
[14,12,14,12,14,12,15,14,0,14,15,12,15,15,13],
[12,14,13,13,13,13,16,11,11,0,15,12,13,16,12],
[13,12,16,13,15,11,11,14,10,10,0,12,15,14,8],
[12,11,12,12,10,13,16,13,13,13,13,0,13,14,11],
[13,12,13,12,11,13,10,11,10,12,10,12,0,17,7],
[9,11,14,9,11,10,12,12,10,9,11,11,8,0,10],
[15,14,13,13,13,15,15,14,12,13,17,14,18,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,11,9,7,10,11,12,6,10,8,9,8,9],
[17,0,15,14,12,12,13,14,16,10,14,14,15,15,13],
[15,10,0,9,11,13,9,11,14,11,12,12,10,12,13],
[14,11,16,0,12,13,13,14,13,8,11,14,11,12,13],
[16,13,14,13,0,13,14,13,14,11,15,14,14,12,13],
[18,13,12,12,12,0,14,16,14,8,13,13,11,14,14],
[15,12,16,12,11,11,0,15,14,12,14,13,14,14,13],
[14,11,14,11,12,9,10,0,11,9,14,9,11,12,12],
[13,9,11,12,11,11,11,14,0,13,13,12,12,13,13],
[19,15,14,17,14,17,13,16,12,0,18,16,14,15,14],
[15,11,13,14,10,12,11,11,12,7,0,12,12,13,13],
[17,11,13,11,11,12,12,16,13,9,13,0,12,15,12],
[16,10,15,14,11,14,11,14,13,11,13,13,0,14,14],
[17,10,13,13,13,11,11,13,12,10,12,10,11,0,14],
[16,12,12,12,12,11,12,13,12,11,12,13,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,12,14,11,11,12,12,12,11,17,14,11,12],
[9,0,8,8,13,4,11,11,9,9,10,12,11,11,9],
[13,17,0,13,16,14,14,13,13,14,11,16,16,11,15],
[13,17,12,0,13,14,14,13,13,12,12,17,15,12,14],
[11,12,9,12,0,9,10,11,13,10,9,14,16,10,13],
[14,21,11,11,16,0,12,14,12,13,11,17,14,14,14],
[14,14,11,11,15,13,0,12,13,12,11,16,15,13,12],
[13,14,12,12,14,11,13,0,10,10,13,14,15,12,11],
[13,16,12,12,12,13,12,15,0,14,10,15,15,16,15],
[13,16,11,13,15,12,13,15,11,0,10,18,17,14,13],
[14,15,14,13,16,14,14,12,15,15,0,16,20,14,16],
[8,13,9,8,11,8,9,11,10,7,9,0,13,9,9],
[11,14,9,10,9,11,10,10,10,8,5,12,0,8,12],
[14,14,14,13,15,11,12,13,9,11,11,16,17,0,12],
[13,16,10,11,12,11,13,14,10,12,9,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,16,8,8,16,11,17,19,14,7,9,15,11,20],
[17,0,16,15,18,14,15,19,19,15,13,12,15,16,15],
[9,9,0,10,7,10,11,16,12,12,7,8,7,14,9],
[17,10,15,0,10,16,13,21,17,13,11,8,11,13,15],
[17,7,18,15,0,16,10,16,14,19,13,6,18,15,15],
[9,11,15,9,9,0,15,21,17,12,4,7,7,14,10],
[14,10,14,12,15,10,0,18,18,12,10,13,13,17,16],
[8,6,9,4,9,4,7,0,8,6,5,5,7,11,8],
[6,6,13,8,11,8,7,17,0,9,8,7,11,11,12],
[11,10,13,12,6,13,13,19,16,0,5,5,11,11,16],
[18,12,18,14,12,21,15,20,17,20,0,5,14,17,16],
[16,13,17,17,19,18,12,20,18,20,20,0,21,16,19],
[10,10,18,14,7,18,12,18,14,14,11,4,0,12,14],
[14,9,11,12,10,11,8,14,14,14,8,9,13,0,14],
[5,10,16,10,10,15,9,17,13,9,9,6,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,9,11,16,11,13,11,15,20,11,14,15,17],
[18,0,18,8,20,19,14,15,9,16,18,19,17,20,19],
[11,7,0,9,9,13,11,15,8,9,16,8,13,15,14],
[16,17,16,0,19,20,11,15,12,14,18,17,19,17,14],
[14,5,16,6,0,14,9,9,7,13,16,14,10,15,15],
[9,6,12,5,11,0,10,11,10,11,18,9,10,14,14],
[14,11,14,14,16,15,0,16,14,16,19,14,12,15,15],
[12,10,10,10,16,14,9,0,11,11,12,13,10,10,14],
[14,16,17,13,18,15,11,14,0,15,22,15,17,16,17],
[10,9,16,11,12,14,9,14,10,0,14,14,16,14,14],
[5,7,9,7,9,7,6,13,3,11,0,4,8,13,8],
[14,6,17,8,11,16,11,12,10,11,21,0,6,15,13],
[11,8,12,6,15,15,13,15,8,9,17,19,0,14,18],
[10,5,10,8,10,11,10,15,9,11,12,10,11,0,8],
[8,6,11,11,10,11,10,11,8,11,17,12,7,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,11,17,11,13,8,12,8,12,11,8,11,9],
[17,0,11,11,18,11,13,13,13,14,16,13,14,12,15],
[13,14,0,11,15,13,10,11,16,15,15,8,9,10,13],
[14,14,14,0,16,9,17,12,13,13,15,11,12,16,11],
[8,7,10,9,0,7,8,8,9,7,9,8,8,7,7],
[14,14,12,16,18,0,15,13,12,15,18,8,12,12,16],
[12,12,15,8,17,10,0,11,14,11,11,9,8,15,12],
[17,12,14,13,17,12,14,0,11,11,11,9,10,10,15],
[13,12,9,12,16,13,11,14,0,9,11,11,8,13,16],
[17,11,10,12,18,10,14,14,16,0,17,13,13,11,16],
[13,9,10,10,16,7,14,14,14,8,0,8,11,14,15],
[14,12,17,14,17,17,16,16,14,12,17,0,15,13,15],
[17,11,16,13,17,13,17,15,17,12,14,10,0,16,15],
[14,13,15,9,18,13,10,15,12,14,11,12,9,0,16],
[16,10,12,14,18,9,13,10,9,9,10,10,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,19,5,12,10,13,0,12,13,12,6,19,5,6],
[20,0,15,20,15,11,20,8,13,8,12,20,20,5,8],
[6,10,0,11,13,11,18,6,12,11,17,11,25,5,6],
[20,5,14,0,12,6,20,13,12,13,17,20,25,5,6],
[13,10,12,13,0,11,13,8,12,13,17,13,25,5,18],
[15,14,14,19,14,0,15,7,14,8,12,20,20,19,15],
[12,5,7,5,12,10,0,5,12,6,17,10,24,5,5],
[25,17,19,12,17,18,20,0,24,25,17,20,25,17,18],
[13,12,13,13,13,11,13,1,0,6,12,13,20,12,6],
[12,17,14,12,12,17,19,0,19,0,17,12,24,12,12],
[13,13,8,8,8,13,8,8,13,8,0,8,18,13,13],
[19,5,14,5,12,5,15,5,12,13,17,0,24,5,6],
[6,5,0,0,0,5,1,0,5,1,7,1,0,5,6],
[20,20,20,20,20,6,20,8,13,13,12,20,20,0,13],
[19,17,19,19,7,10,20,7,19,13,12,19,19,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,10,20,10,6,10,9,16,13,14,10,11,9],
[13,0,8,9,19,10,8,11,5,15,16,13,10,7,13],
[16,17,0,16,20,12,12,15,13,17,20,18,14,15,17],
[15,16,9,0,19,10,13,15,8,17,15,16,9,12,12],
[5,6,5,6,0,7,5,8,3,11,8,12,9,7,9],
[15,15,13,15,18,0,14,17,13,14,17,13,12,13,11],
[19,17,13,12,20,11,0,14,13,17,20,19,10,14,13],
[15,14,10,10,17,8,11,0,11,14,15,16,7,13,12],
[16,20,12,17,22,12,12,14,0,17,19,16,9,16,16],
[9,10,8,8,14,11,8,11,8,0,10,14,8,10,13],
[12,9,5,10,17,8,5,10,6,15,0,14,4,8,7],
[11,12,7,9,13,12,6,9,9,11,11,0,6,11,13],
[15,15,11,16,16,13,15,18,16,17,21,19,0,15,19],
[14,18,10,13,18,12,11,12,9,15,17,14,10,0,11],
[16,12,8,13,16,14,12,13,9,12,18,12,6,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,16,18,14,13,8,15,14,17,14,8,9,12],
[16,0,17,19,22,11,17,7,17,15,20,19,7,18,12],
[12,8,0,14,11,14,12,13,14,14,17,13,13,9,8],
[9,6,11,0,17,11,9,5,15,14,18,13,5,13,10],
[7,3,14,8,0,13,12,3,9,8,20,17,4,16,7],
[11,14,11,14,12,0,14,10,15,17,18,16,10,16,15],
[12,8,13,16,13,11,0,6,13,11,20,19,8,18,6],
[17,18,12,20,22,15,19,0,18,11,19,18,21,18,14],
[10,8,11,10,16,10,12,7,0,9,12,13,7,13,4],
[11,10,11,11,17,8,14,14,16,0,15,13,12,14,7],
[8,5,8,7,5,7,5,6,13,10,0,10,8,10,1],
[11,6,12,12,8,9,6,7,12,12,15,0,8,15,7],
[17,18,12,20,21,15,17,4,18,13,17,17,0,17,14],
[16,7,16,12,9,9,7,7,12,11,15,10,8,0,12],
[13,13,17,15,18,10,19,11,21,18,24,18,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,14,16,11,14,19,15,14,16,16,16,9,15],
[6,0,12,11,12,9,11,13,13,14,13,13,12,12,14],
[10,13,0,8,14,9,15,11,12,12,14,15,12,8,13],
[11,14,17,0,18,11,16,19,13,17,16,15,18,9,17],
[9,13,11,7,0,7,15,12,7,12,11,14,12,7,11],
[14,16,16,14,18,0,19,16,12,19,18,17,15,14,16],
[11,14,10,9,10,6,0,13,11,12,13,11,14,7,9],
[6,12,14,6,13,9,12,0,11,12,13,9,6,8,14],
[10,12,13,12,18,13,14,14,0,15,14,18,12,10,13],
[11,11,13,8,13,6,13,13,10,0,14,14,12,7,12],
[9,12,11,9,14,7,12,12,11,11,0,15,14,10,16],
[9,12,10,10,11,8,14,16,7,11,10,0,10,8,10],
[9,13,13,7,13,10,11,19,13,13,11,15,0,10,14],
[16,13,17,16,18,11,18,17,15,18,15,17,15,0,18],
[10,11,12,8,14,9,16,11,12,13,9,15,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,10,12,9,17,11,13,12,11,11,14,11,7],
[14,0,6,11,7,7,16,8,7,12,9,10,10,11,9],
[19,19,0,14,17,10,21,16,14,18,16,18,13,17,12],
[15,14,11,0,14,9,18,11,14,14,9,13,13,11,6],
[13,18,8,11,0,14,20,15,17,17,11,15,13,10,7],
[16,18,15,16,11,0,20,14,18,20,18,17,16,15,12],
[8,9,4,7,5,5,0,4,9,8,5,4,6,7,3],
[14,17,9,14,10,11,21,0,17,16,13,14,12,14,6],
[12,18,11,11,8,7,16,8,0,14,13,9,14,12,8],
[13,13,7,11,8,5,17,9,11,0,10,14,11,9,7],
[14,16,9,16,14,7,20,12,12,15,0,16,13,8,7],
[14,15,7,12,10,8,21,11,16,11,9,0,10,9,8],
[11,15,12,12,12,9,19,13,11,14,12,15,0,7,9],
[14,14,8,14,15,10,18,11,13,16,17,16,18,0,13],
[18,16,13,19,18,13,22,19,17,18,18,17,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,8,16,13,15,18,16,18,19,21,14,18,20,21],
[7,0,11,12,10,12,14,12,19,15,16,8,15,13,15],
[17,14,0,19,14,16,18,16,18,17,16,12,15,18,18],
[9,13,6,0,11,20,18,18,9,9,16,13,15,17,13],
[12,15,11,14,0,18,13,20,14,8,23,14,15,25,13],
[10,13,9,5,7,0,14,10,9,9,12,3,10,12,10],
[7,11,7,7,12,11,0,11,11,7,19,4,9,17,6],
[9,13,9,7,5,15,14,0,13,7,16,7,8,19,7],
[7,6,7,16,11,16,14,12,0,11,14,11,12,11,12],
[6,10,8,16,17,16,18,18,14,0,16,12,17,18,16],
[4,9,9,9,2,13,6,9,11,9,0,5,7,12,9],
[11,17,13,12,11,22,21,18,14,13,20,0,20,22,13],
[7,10,10,10,10,15,16,17,13,8,18,5,0,15,11],
[5,12,7,8,0,13,8,6,14,7,13,3,10,0,9],
[4,10,7,12,12,15,19,18,13,9,16,12,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,7,12,10,12,7,13,6,17,9,8,14,14],
[9,0,10,12,5,9,9,9,11,11,5,8,8,9,8],
[10,15,0,6,5,10,10,8,13,10,11,5,9,11,9],
[18,13,19,0,11,18,16,14,17,14,16,10,13,16,16],
[13,20,20,14,0,13,17,11,16,14,17,13,13,17,18],
[15,16,15,7,12,0,15,8,12,9,13,10,10,18,14],
[13,16,15,9,8,10,0,9,11,7,14,12,9,11,13],
[18,16,17,11,14,17,16,0,16,14,14,8,11,17,15],
[12,14,12,8,9,13,14,9,0,8,15,8,8,13,11],
[19,14,15,11,11,16,18,11,17,0,14,11,12,16,14],
[8,20,14,9,8,12,11,11,10,11,0,11,10,10,13],
[16,17,20,15,12,15,13,17,17,14,14,0,13,17,18],
[17,17,16,12,12,15,16,14,17,13,15,12,0,19,19],
[11,16,14,9,8,7,14,8,12,9,15,8,6,0,16],
[11,17,16,9,7,11,12,10,14,11,12,7,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,23,18,12,19,9,13,16,18,19,15,18,16,14],
[10,0,17,15,10,18,12,13,11,11,11,8,17,16,11],
[2,8,0,5,7,8,5,9,6,10,6,1,11,12,4],
[7,10,20,0,10,14,6,11,11,18,13,9,12,14,10],
[13,15,18,15,0,15,8,11,13,15,13,12,19,13,11],
[6,7,17,11,10,0,5,10,9,14,11,7,13,13,9],
[16,13,20,19,17,20,0,14,17,16,18,15,22,21,12],
[12,12,16,14,14,15,11,0,14,10,15,13,17,10,13],
[9,14,19,14,12,16,8,11,0,20,16,11,18,17,15],
[7,14,15,7,10,11,9,15,5,0,15,7,14,15,9],
[6,14,19,12,12,14,7,10,9,10,0,9,14,13,5],
[10,17,24,16,13,18,10,12,14,18,16,0,18,14,13],
[7,8,14,13,6,12,3,8,7,11,11,7,0,12,9],
[9,9,13,11,12,12,4,15,8,10,12,11,13,0,7],
[11,14,21,15,14,16,13,12,10,16,20,12,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,9,10,9,11,9,9,9,10,12,11,4,12],
[16,0,14,11,10,10,6,11,10,8,14,12,12,8,14],
[18,11,0,14,15,10,12,9,14,14,10,12,10,8,12],
[16,14,11,0,14,12,8,8,9,13,10,11,10,12,17],
[15,15,10,11,0,9,11,11,13,4,12,13,12,12,14],
[16,15,15,13,16,0,13,14,14,15,16,17,12,12,16],
[14,19,13,17,14,12,0,14,9,12,17,10,14,12,15],
[16,14,16,17,14,11,11,0,9,16,15,12,13,10,16],
[16,15,11,16,12,11,16,16,0,10,14,15,17,13,16],
[16,17,11,12,21,10,13,9,15,0,15,10,10,13,16],
[15,11,15,15,13,9,8,10,11,10,0,13,11,11,15],
[13,13,13,14,12,8,15,13,10,15,12,0,12,10,15],
[14,13,15,15,13,13,11,12,8,15,14,13,0,11,16],
[21,17,17,13,13,13,13,15,12,12,14,15,14,0,15],
[13,11,13,8,11,9,10,9,9,9,10,10,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,19,20,17,18,17,19,18,11,18,14,15,11,17],
[7,0,20,14,12,11,14,18,9,14,15,16,10,12,17],
[6,5,0,8,5,5,9,13,7,9,7,11,5,10,7],
[5,11,17,0,17,14,10,11,14,14,13,13,11,9,14],
[8,13,20,8,0,11,11,11,13,11,13,13,9,9,15],
[7,14,20,11,14,0,11,18,11,14,11,16,6,11,11],
[8,11,16,15,14,14,0,13,10,12,12,13,12,10,14],
[6,7,12,14,14,7,12,0,10,13,8,7,8,9,11],
[7,16,18,11,12,14,15,15,0,11,17,13,11,8,15],
[14,11,16,11,14,11,13,12,14,0,14,10,12,15,17],
[7,10,18,12,12,14,13,17,8,11,0,16,1,11,12],
[11,9,14,12,12,9,12,18,12,15,9,0,7,15,11],
[10,15,20,14,16,19,13,17,14,13,24,18,0,12,20],
[14,13,15,16,16,14,15,16,17,10,14,10,13,0,13],
[8,8,18,11,10,14,11,14,10,8,13,14,5,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,10,12,14,11,18,14,13,12,14,17,14,17],
[11,0,17,11,9,12,8,9,12,11,10,12,18,9,16],
[8,8,0,6,10,6,6,9,13,11,9,7,10,10,12],
[15,14,19,0,16,12,13,16,13,16,13,13,18,14,14],
[13,16,15,9,0,14,13,15,15,14,16,9,17,12,13],
[11,13,19,13,11,0,6,11,14,10,13,8,16,10,16],
[14,17,19,12,12,19,0,12,21,12,12,11,20,17,19],
[7,16,16,9,10,14,13,0,17,17,13,15,18,11,13],
[11,13,12,12,10,11,4,8,0,8,7,8,13,12,16],
[12,14,14,9,11,15,13,8,17,0,11,11,18,16,18],
[13,15,16,12,9,12,13,12,18,14,0,10,15,13,16],
[11,13,18,12,16,17,14,10,17,14,15,0,17,15,16],
[8,7,15,7,8,9,5,7,12,7,10,8,0,13,11],
[11,16,15,11,13,15,8,14,13,9,12,10,12,0,18],
[8,9,13,11,12,9,6,12,9,7,9,9,14,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,7,4,11,10,5,10,4,3,8,5,11,9],
[17,0,8,18,12,17,12,14,14,14,10,19,7,13,16],
[18,17,0,19,15,15,14,12,19,17,19,24,16,14,17],
[18,7,6,0,9,12,12,9,11,12,11,19,8,13,13],
[21,13,10,16,0,14,17,10,17,11,11,20,7,17,13],
[14,8,10,13,11,0,12,8,13,9,11,14,6,13,11],
[15,13,11,13,8,13,0,9,11,11,12,17,7,19,15],
[20,11,13,16,15,17,16,0,14,15,9,18,11,21,16],
[15,11,6,14,8,12,14,11,0,9,9,13,6,17,9],
[21,11,8,13,14,16,14,10,16,0,14,23,8,19,16],
[22,15,6,14,14,14,13,16,16,11,0,11,12,14,9],
[17,6,1,6,5,11,8,7,12,2,14,0,5,10,9],
[20,18,9,17,18,19,18,14,19,17,13,20,0,18,15],
[14,12,11,12,8,12,6,4,8,6,11,15,7,0,13],
[16,9,8,12,12,14,10,9,16,9,16,16,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,10,12,10,13,10,14,16,15,13,12,11,12],
[14,0,12,13,16,12,11,17,10,20,15,16,18,13,15],
[14,13,0,15,14,17,13,12,10,15,15,14,15,14,16],
[15,12,10,0,14,12,15,13,12,15,12,13,10,12,11],
[13,9,11,11,0,10,13,9,12,15,15,15,12,12,10],
[15,13,8,13,15,0,14,12,12,18,16,15,15,14,14],
[12,14,12,10,12,11,0,15,14,14,15,11,17,8,14],
[15,8,13,12,16,13,10,0,12,22,18,10,17,13,19],
[11,15,15,13,13,13,11,13,0,12,16,13,15,10,10],
[9,5,10,10,10,7,11,3,13,0,9,10,8,7,5],
[10,10,10,13,10,9,10,7,9,16,0,7,12,9,14],
[12,9,11,12,10,10,14,15,12,15,18,0,17,12,16],
[13,7,10,15,13,10,8,8,10,17,13,8,0,10,15],
[14,12,11,13,13,11,17,12,15,18,16,13,15,0,17],
[13,10,9,14,15,11,11,6,15,20,11,9,10,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,10,8,6,11,9,11,7,12,8,8,10,11],
[15,0,12,16,16,11,13,12,12,14,15,12,12,15,16],
[16,13,0,12,15,13,11,14,15,11,14,13,12,15,16],
[15,9,13,0,12,11,12,12,11,12,15,9,14,12,13],
[17,9,10,13,0,11,12,10,14,11,18,13,12,16,13],
[19,14,12,14,14,0,16,13,13,17,19,13,17,19,13],
[14,12,14,13,13,9,0,14,13,12,14,12,15,16,12],
[16,13,11,13,15,12,11,0,12,10,15,12,12,13,16],
[14,13,10,14,11,12,12,13,0,11,19,11,12,14,13],
[18,11,14,13,14,8,13,15,14,0,16,14,14,17,14],
[13,10,11,10,7,6,11,10,6,9,0,8,9,14,10],
[17,13,12,16,12,12,13,13,14,11,17,0,14,15,11],
[17,13,13,11,13,8,10,13,13,11,16,11,0,16,14],
[15,10,10,13,9,6,9,12,11,8,11,10,9,0,9],
[14,9,9,12,12,12,13,9,12,11,15,14,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,15,13,12,9,12,10,11,17,17,15,7,12],
[9,0,14,14,13,16,11,9,9,10,14,16,16,7,10],
[14,11,0,19,10,14,14,11,12,15,16,15,18,14,12],
[10,11,6,0,9,10,10,9,6,11,13,13,12,8,9],
[12,12,15,16,0,13,11,12,10,13,16,13,17,9,9],
[13,9,11,15,12,0,8,8,7,8,14,13,12,9,6],
[16,14,11,15,14,17,0,11,12,11,14,13,15,10,11],
[13,16,14,16,13,17,14,0,12,10,19,15,18,13,17],
[15,16,13,19,15,18,13,13,0,15,16,17,18,9,9],
[14,15,10,14,12,17,14,15,10,0,14,14,12,8,12],
[8,11,9,12,9,11,11,6,9,11,0,12,16,6,8],
[8,9,10,12,12,12,12,10,8,11,13,0,13,9,9],
[10,9,7,13,8,13,10,7,7,13,9,12,0,6,9],
[18,18,11,17,16,16,15,12,16,17,19,16,19,0,13],
[13,15,13,16,16,19,14,8,16,13,17,16,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,11,14,18,15,15,22,16,13,12,9,19,11,9],
[3,0,4,6,8,5,8,6,14,8,10,5,7,7,4],
[14,21,0,12,15,16,12,16,17,16,14,10,15,14,15],
[11,19,13,0,13,14,12,12,15,10,12,10,11,14,15],
[7,17,10,12,0,10,10,7,16,9,14,8,9,7,10],
[10,20,9,11,15,0,10,14,16,11,12,12,14,9,9],
[10,17,13,13,15,15,0,16,21,14,15,16,13,11,12],
[3,19,9,13,18,11,9,0,17,10,12,9,14,8,10],
[9,11,8,10,9,9,4,8,0,6,8,5,11,8,8],
[12,17,9,15,16,14,11,15,19,0,11,16,12,11,11],
[13,15,11,13,11,13,10,13,17,14,0,8,16,15,10],
[16,20,15,15,17,13,9,16,20,9,17,0,14,10,17],
[6,18,10,14,16,11,12,11,14,13,9,11,0,9,9],
[14,18,11,11,18,16,14,17,17,14,10,15,16,0,13],
[16,21,10,10,15,16,13,15,17,14,15,8,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,9,9,0,13,9,9,16,9,9,21,9,9,21],
[4,0,13,13,4,13,13,4,16,13,0,9,9,13,25],
[16,12,0,25,0,13,9,0,16,9,0,12,9,9,21],
[16,12,0,0,0,4,9,0,16,9,0,12,9,9,21],
[25,21,25,25,0,13,13,13,16,13,21,21,9,9,25],
[12,12,12,21,12,0,21,12,12,21,12,12,21,9,21],
[16,12,16,16,12,4,0,4,16,16,12,12,0,0,16],
[16,21,25,25,12,13,21,0,16,25,12,21,9,9,21],
[9,9,9,9,9,13,9,9,0,9,9,9,9,9,21],
[16,12,16,16,12,4,9,0,16,0,12,12,9,0,21],
[16,25,25,25,4,13,13,13,16,13,0,21,13,13,25],
[4,16,13,13,4,13,13,4,16,13,4,0,13,13,25],
[16,16,16,16,16,4,25,16,16,16,12,12,0,4,25],
[16,12,16,16,16,16,25,16,16,25,12,12,21,0,25],
[4,0,4,4,0,4,9,4,4,4,0,0,0,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,14,19,15,11,19,22,20,14,13,21,18,17],
[8,0,10,5,19,5,7,13,18,12,5,6,8,21,9],
[7,15,0,6,18,5,5,16,16,14,10,10,10,18,10],
[11,20,19,0,21,14,16,17,23,23,12,13,24,20,13],
[6,6,7,4,0,4,6,14,14,10,3,6,8,21,6],
[10,20,20,11,21,0,4,19,20,21,15,15,19,22,12],
[14,18,20,9,19,21,0,21,19,21,13,12,16,21,14],
[6,12,9,8,11,6,4,0,17,18,12,7,14,20,12],
[3,7,9,2,11,5,6,8,0,12,4,2,5,20,5],
[5,13,11,2,15,4,4,7,13,0,10,5,12,20,10],
[11,20,15,13,22,10,12,13,21,15,0,16,13,21,11],
[12,19,15,12,19,10,13,18,23,20,9,0,21,21,12],
[4,17,15,1,17,6,9,11,20,13,12,4,0,19,9],
[7,4,7,5,4,3,4,5,5,5,4,4,6,0,7],
[8,16,15,12,19,13,11,13,20,15,14,13,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,12,10,10,9,12,13,15,9,12,11,8,13],
[12,0,12,15,10,11,10,9,10,19,9,10,14,10,13],
[11,13,0,13,13,10,9,10,9,15,12,11,13,5,8],
[13,10,12,0,8,6,9,10,8,13,7,8,14,8,12],
[15,15,12,17,0,10,10,12,6,13,13,6,15,11,10],
[15,14,15,19,15,0,15,11,15,15,11,11,15,12,12],
[16,15,16,16,15,10,0,11,12,15,16,13,11,11,10],
[13,16,15,15,13,14,14,0,10,18,14,15,12,13,13],
[12,15,16,17,19,10,13,15,0,16,13,16,13,10,12],
[10,6,10,12,12,10,10,7,9,0,10,13,7,11,10],
[16,16,13,18,12,14,9,11,12,15,0,11,14,13,12],
[13,15,14,17,19,14,12,10,9,12,14,0,13,11,11],
[14,11,12,11,10,10,14,13,12,18,11,12,0,12,14],
[17,15,20,17,14,13,14,12,15,14,12,14,13,0,12],
[12,12,17,13,15,13,15,12,13,15,13,14,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,9,10,9,11,12,8,12,9,8,9,8,10],
[10,0,9,11,13,11,15,10,8,10,11,12,9,11,11],
[16,16,0,17,17,15,17,15,12,13,11,16,13,14,14],
[16,14,8,0,11,13,14,12,12,12,10,11,11,11,13],
[15,12,8,14,0,9,9,10,12,10,8,11,11,9,12],
[16,14,10,12,16,0,12,11,13,13,11,12,11,12,13],
[14,10,8,11,16,13,0,12,9,13,11,11,8,8,9],
[13,15,10,13,15,14,13,0,15,15,11,11,13,12,14],
[17,17,13,13,13,12,16,10,0,13,13,12,12,10,15],
[13,15,12,13,15,12,12,10,12,0,15,13,12,11,11],
[16,14,14,15,17,14,14,14,12,10,0,12,14,12,12],
[17,13,9,14,14,13,14,14,13,12,13,0,16,15,12],
[16,16,12,14,14,14,17,12,13,13,11,9,0,13,14],
[17,14,11,14,16,13,17,13,15,14,13,10,12,0,13],
[15,14,11,12,13,12,16,11,10,14,13,13,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,18,12,11,16,15,14,15,11,13,17,10,11],
[6,0,9,9,7,9,9,7,3,9,6,7,8,4,6],
[8,16,0,17,10,12,12,16,12,13,16,11,15,8,13],
[7,16,8,0,12,5,9,12,8,6,8,7,6,3,4],
[13,18,15,13,0,11,9,14,11,8,11,9,12,8,10],
[14,16,13,20,14,0,14,17,15,17,14,12,15,13,9],
[9,16,13,16,16,11,0,16,15,12,13,11,13,12,10],
[10,18,9,13,11,8,9,0,7,13,10,8,12,9,9],
[11,22,13,17,14,10,10,18,0,11,11,6,15,8,9],
[10,16,12,19,17,8,13,12,14,0,12,12,10,8,9],
[14,19,9,17,14,11,12,15,14,13,0,13,16,8,9],
[12,18,14,18,16,13,14,17,19,13,12,0,14,11,13],
[8,17,10,19,13,10,12,13,10,15,9,11,0,11,8],
[15,21,17,22,17,12,13,16,17,17,17,14,14,0,12],
[14,19,12,21,15,16,15,16,16,16,16,12,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,17,15,15,11,15,17,17,13,15,11,15,13],
[10,0,9,10,8,2,8,6,6,8,4,13,9,8,4],
[14,16,0,12,18,6,10,10,10,8,12,15,13,16,8],
[8,15,13,0,6,8,6,6,10,8,15,13,15,8,15],
[10,17,7,19,0,13,13,11,15,13,11,11,9,13,11],
[10,23,19,17,12,0,17,17,10,21,19,13,13,21,21],
[14,17,15,19,12,8,0,17,8,8,17,15,15,10,19],
[10,19,15,19,14,8,8,0,10,8,17,17,19,16,21],
[8,19,15,15,10,15,17,15,0,17,19,19,15,21,19],
[8,17,17,17,12,4,17,17,8,0,19,15,11,14,13],
[12,21,13,10,14,6,8,8,6,6,0,15,9,8,11],
[10,12,10,12,14,12,10,8,6,10,10,0,6,14,14],
[14,16,12,10,16,12,10,6,10,14,16,19,0,14,12],
[10,17,9,17,12,4,15,9,4,11,17,11,11,0,11],
[12,21,17,10,14,4,6,4,6,12,14,11,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,13,11,10,13,15,9,7,14,9,11,12,16],
[12,0,6,6,10,7,4,8,6,9,8,8,5,7,19],
[15,19,0,19,18,16,12,18,13,12,17,13,7,13,21],
[12,19,6,0,12,10,12,13,8,9,10,9,5,16,24],
[14,15,7,13,0,7,14,16,12,7,14,9,13,10,16],
[15,18,9,15,18,0,14,12,13,10,16,10,12,14,19],
[12,21,13,13,11,11,0,19,11,14,12,15,9,11,18],
[10,17,7,12,9,13,6,0,9,7,13,9,9,16,18],
[16,19,12,17,13,12,14,16,0,17,16,11,10,14,23],
[18,16,13,16,18,15,11,18,8,0,15,8,11,12,19],
[11,17,8,15,11,9,13,12,9,10,0,10,6,12,17],
[16,17,12,16,16,15,10,16,14,17,15,0,11,13,20],
[14,20,18,20,12,13,16,16,15,14,19,14,0,15,20],
[13,18,12,9,15,11,14,9,11,13,13,12,10,0,19],
[9,6,4,1,9,6,7,7,2,6,8,5,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,11,8,13,10,9,6,9,17,15,11,9,12],
[10,0,12,11,5,13,10,4,10,9,11,10,14,9,12],
[15,13,0,13,6,12,11,7,8,13,15,14,15,10,18],
[14,14,12,0,8,14,13,12,12,9,16,14,9,11,14],
[17,20,19,17,0,17,10,17,17,16,17,14,18,18,21],
[12,12,13,11,8,0,12,6,8,14,14,11,13,10,13],
[15,15,14,12,15,13,0,11,12,12,14,14,15,16,17],
[16,21,18,13,8,19,14,0,11,15,18,15,14,19,18],
[19,15,17,13,8,17,13,14,0,14,17,16,14,16,19],
[16,16,12,16,9,11,13,10,11,0,13,15,13,14,13],
[8,14,10,9,8,11,11,7,8,12,0,12,13,13,15],
[10,15,11,11,11,14,11,10,9,10,13,0,11,14,15],
[14,11,10,16,7,12,10,11,11,12,12,14,0,10,13],
[16,16,15,14,7,15,9,6,9,11,12,11,15,0,17],
[13,13,7,11,4,12,8,7,6,12,10,10,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,12,14,17,1,4,4,7,1,5,12,10,10,5],
[20,0,18,17,13,13,10,13,13,6,8,15,11,16,13],
[13,7,0,13,8,8,13,11,12,8,8,8,8,11,8],
[11,8,12,0,11,11,10,8,12,4,15,11,9,8,12],
[8,12,17,14,0,6,9,12,12,8,12,13,9,13,9],
[24,12,17,14,19,0,14,12,12,3,14,14,12,17,14],
[21,15,12,15,16,11,0,3,3,9,15,10,9,14,20],
[21,12,14,17,13,13,22,0,19,13,17,10,8,11,17],
[18,12,13,13,13,13,22,6,0,6,17,8,6,11,17],
[24,19,17,21,17,22,16,12,19,0,19,19,20,15,22],
[20,17,17,10,13,11,10,8,8,6,0,10,9,11,11],
[13,10,17,14,12,11,15,15,17,6,15,0,6,10,15],
[15,14,17,16,16,13,16,17,19,5,16,19,0,14,16],
[15,9,14,17,12,8,11,14,14,10,14,15,11,0,16],
[20,12,17,13,16,11,5,8,8,3,14,10,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,14,11,11,14,10,7,12,12,12,12,9,13],
[15,0,9,12,13,12,16,15,15,13,17,16,15,12,14],
[16,16,0,14,13,16,13,15,10,15,18,16,15,15,15],
[11,13,11,0,15,13,17,12,13,17,15,16,16,10,11],
[14,12,12,10,0,12,17,9,11,11,16,13,13,12,10],
[14,13,9,12,13,0,19,14,9,12,19,17,16,11,12],
[11,9,12,8,8,6,0,7,5,6,11,14,9,7,8],
[15,10,10,13,16,11,18,0,9,11,18,13,17,13,11],
[18,10,15,12,14,16,20,16,0,15,19,16,19,13,13],
[13,12,10,8,14,13,19,14,10,0,16,16,13,11,11],
[13,8,7,10,9,6,14,7,6,9,0,13,11,8,9],
[13,9,9,9,12,8,11,12,9,9,12,0,11,9,10],
[13,10,10,9,12,9,16,8,6,12,14,14,0,11,10],
[16,13,10,15,13,14,18,12,12,14,17,16,14,0,10],
[12,11,10,14,15,13,17,14,12,14,16,15,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,9,10,14,11,10,13,12,9,7,14,8,11,7],
[21,0,16,12,17,17,20,16,16,13,13,20,16,16,11],
[16,9,0,9,18,15,16,16,13,14,11,17,14,11,13],
[15,13,16,0,12,17,15,14,11,15,14,15,15,15,8],
[11,8,7,13,0,11,14,12,6,13,9,15,10,9,11],
[14,8,10,8,14,0,12,12,7,10,10,15,9,11,9],
[15,5,9,10,11,13,0,14,10,11,9,12,9,9,7],
[12,9,9,11,13,13,11,0,13,14,9,11,10,11,10],
[13,9,12,14,19,18,15,12,0,14,11,15,12,12,11],
[16,12,11,10,12,15,14,11,11,0,5,12,12,14,4],
[18,12,14,11,16,15,16,16,14,20,0,15,14,18,13],
[11,5,8,10,10,10,13,14,10,13,10,0,12,11,9],
[17,9,11,10,15,16,16,15,13,13,11,13,0,13,8],
[14,9,14,10,16,14,16,14,13,11,7,14,12,0,5],
[18,14,12,17,14,16,18,15,14,21,12,16,17,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,17,5,5,15,15,5,12,18,13,18,15,8],
[20,0,8,20,0,13,25,13,3,15,18,13,13,13,3],
[20,17,0,17,10,20,22,17,10,22,25,13,20,20,13],
[8,5,8,0,5,8,5,5,5,12,8,3,8,8,8],
[20,25,15,20,0,25,25,25,25,15,25,20,20,25,3],
[20,12,5,17,0,0,22,15,5,12,25,13,13,10,3],
[10,0,3,20,0,3,0,3,3,7,18,13,13,3,3],
[10,12,8,20,0,10,22,0,8,12,25,13,13,3,3],
[20,22,15,20,0,20,22,17,0,12,25,13,20,20,3],
[13,10,3,13,10,13,18,13,13,0,18,13,13,13,3],
[7,7,0,17,0,0,7,0,0,7,0,3,3,0,3],
[12,12,12,22,5,12,12,12,12,12,22,0,22,12,8],
[7,12,5,17,5,12,12,12,5,12,22,3,0,12,8],
[10,12,5,17,0,15,22,22,5,12,25,13,13,0,3],
[17,22,12,17,22,22,22,22,22,22,22,17,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,25,25,20,16,20,16,20,25,16,20,20,21,12],
[9,0,13,25,8,21,25,9,13,21,21,8,13,21,9],
[0,12,0,17,4,16,16,16,0,12,16,8,4,16,12],
[0,0,8,0,8,16,8,4,8,4,4,8,8,16,0],
[5,17,21,17,0,21,25,21,17,21,21,16,17,21,17],
[9,4,9,9,4,0,13,0,4,9,4,4,4,21,4],
[5,0,9,17,0,12,0,0,0,17,0,4,0,21,0],
[9,16,9,21,4,25,25,0,4,21,16,4,4,25,4],
[5,12,25,17,8,21,25,21,0,21,21,20,8,21,17],
[0,4,13,21,4,16,8,4,4,0,4,8,4,21,0],
[9,4,9,21,4,21,25,9,4,21,0,4,4,21,9],
[5,17,17,17,9,21,21,21,5,17,21,0,9,21,17],
[5,12,21,17,8,21,25,21,17,21,21,16,0,21,17],
[4,4,9,9,4,4,4,0,4,4,4,4,4,0,4],
[13,16,13,25,8,21,25,21,8,25,16,8,8,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,22,12,16,17,15,7,18,24,16,17,11,14,18],
[14,0,13,12,14,7,13,7,7,19,11,11,9,13,16],
[3,12,0,15,8,17,12,9,4,20,18,12,13,2,8],
[13,13,10,0,12,13,13,9,13,16,14,13,9,12,13],
[9,11,17,13,0,17,23,7,2,18,16,16,11,14,11],
[8,18,8,12,8,0,13,13,1,19,15,12,13,8,10],
[10,12,13,12,2,12,0,8,3,19,17,12,12,1,12],
[18,18,16,16,18,12,17,0,11,18,11,11,17,16,18],
[7,18,21,12,23,24,22,14,0,23,22,23,18,17,24],
[1,6,5,9,7,6,6,7,2,0,7,6,7,0,2],
[9,14,7,11,9,10,8,14,3,18,0,7,13,7,9],
[8,14,13,12,9,13,13,14,2,19,18,0,14,8,15],
[14,16,12,16,14,12,13,8,7,18,12,11,0,12,11],
[11,12,23,13,11,17,24,9,8,25,18,17,13,0,18],
[7,9,17,12,14,15,13,7,1,23,16,10,14,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,14,14,14,15,15,13,16,13,14,12,16,12],
[14,0,11,12,11,12,12,14,14,12,11,12,13,11,14],
[11,14,0,12,11,16,15,18,17,16,9,14,14,16,11],
[11,13,13,0,21,16,13,15,17,15,14,16,19,15,14],
[11,14,14,4,0,10,7,13,17,13,13,13,11,11,7],
[11,13,9,9,15,0,16,19,14,14,8,10,12,11,9],
[10,13,10,12,18,9,0,15,16,13,11,16,18,18,11],
[10,11,7,10,12,6,10,0,16,11,7,14,9,10,7],
[12,11,8,8,8,11,9,9,0,12,5,5,10,11,11],
[9,13,9,10,12,11,12,14,13,0,10,10,11,11,9],
[12,14,16,11,12,17,14,18,20,15,0,18,15,15,13],
[11,13,11,9,12,15,9,11,20,15,7,0,10,13,10],
[13,12,11,6,14,13,7,16,15,14,10,15,0,13,9],
[9,14,9,10,14,14,7,15,14,14,10,12,12,0,12],
[13,11,14,11,18,16,14,18,14,16,12,15,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,10,7,11,9,14,10,13,13,10,10,14,11],
[14,0,16,14,13,16,16,14,17,23,19,14,15,12,13],
[14,9,0,8,8,16,14,15,8,16,16,6,10,15,13],
[15,11,17,0,11,15,16,14,14,18,18,15,11,18,14],
[18,12,17,14,0,19,17,18,21,21,21,14,20,17,17],
[14,9,9,10,6,0,9,10,8,14,16,5,12,11,10],
[16,9,11,9,8,16,0,14,13,14,11,13,14,10,14],
[11,11,10,11,7,15,11,0,13,16,14,9,11,11,18],
[15,8,17,11,4,17,12,12,0,17,17,9,10,15,11],
[12,2,9,7,4,11,11,9,8,0,13,6,8,8,10],
[12,6,9,7,4,9,14,11,8,12,0,9,9,12,16],
[15,11,19,10,11,20,12,16,16,19,16,0,13,14,12],
[15,10,15,14,5,13,11,14,15,17,16,12,0,13,14],
[11,13,10,7,8,14,15,14,10,17,13,11,12,0,12],
[14,12,12,11,8,15,11,7,14,15,9,13,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,15,13,10,14,10,8,9,14,16,13,10,10],
[12,0,9,15,11,11,13,11,8,11,14,12,11,10,11],
[15,16,0,16,11,14,18,13,12,10,18,16,14,15,15],
[10,10,9,0,11,11,16,14,7,12,13,16,12,15,10],
[12,14,14,14,0,14,13,12,10,15,15,15,13,12,8],
[15,14,11,14,11,0,18,16,13,14,12,19,15,15,15],
[11,12,7,9,12,7,0,10,9,8,9,11,8,10,10],
[15,14,12,11,13,9,15,0,12,10,10,18,11,13,12],
[17,17,13,18,15,12,16,13,0,15,14,16,17,12,16],
[16,14,15,13,10,11,17,15,10,0,14,19,14,14,16],
[11,11,7,12,10,13,16,15,11,11,0,15,8,15,10],
[9,13,9,9,10,6,14,7,9,6,10,0,11,8,11],
[12,14,11,13,12,10,17,14,8,11,17,14,0,14,11],
[15,15,10,10,13,10,15,12,13,11,10,17,11,0,11],
[15,14,10,15,17,10,15,13,9,9,15,14,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,5,8,10,12,10,6,7,7,10,8,8,6],
[14,0,14,9,9,10,13,12,8,15,12,17,11,12,13],
[19,11,0,12,11,12,16,13,10,16,16,14,12,15,12],
[20,16,13,0,11,15,16,13,14,13,14,20,12,14,13],
[17,16,14,14,0,15,17,14,11,14,13,18,12,14,12],
[15,15,13,10,10,0,13,11,13,14,11,16,14,13,13],
[13,12,9,9,8,12,0,12,7,10,10,15,11,10,8],
[15,13,12,12,11,14,13,0,11,15,14,16,13,15,10],
[19,17,15,11,14,12,18,14,0,15,13,18,15,15,13],
[18,10,9,12,11,11,15,10,10,0,11,16,8,13,10],
[18,13,9,11,12,14,15,11,12,14,0,14,13,13,12],
[15,8,11,5,7,9,10,9,7,9,11,0,8,13,7],
[17,14,13,13,13,11,14,12,10,17,12,17,0,13,11],
[17,13,10,11,11,12,15,10,10,12,12,12,12,0,14],
[19,12,13,12,13,12,17,15,12,15,13,18,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,14,11,15,9,14,15,17,14,18,13,17,11],
[12,0,9,6,10,13,6,14,13,12,12,19,15,14,6],
[12,16,0,11,10,14,9,19,19,16,15,17,18,19,13],
[11,19,14,0,17,19,15,21,18,18,15,16,19,18,17],
[14,15,15,8,0,18,10,15,19,15,12,18,16,16,12],
[10,12,11,6,7,0,4,10,13,18,9,13,17,18,12],
[16,19,16,10,15,21,0,21,22,18,17,17,20,21,17],
[11,11,6,4,10,15,4,0,15,14,10,15,15,15,9],
[10,12,6,7,6,12,3,10,0,15,7,12,15,13,10],
[8,13,9,7,10,7,7,11,10,0,13,17,13,18,12],
[11,13,10,10,13,16,8,15,18,12,0,16,13,16,10],
[7,6,8,9,7,12,8,10,13,8,9,0,15,16,7],
[12,10,7,6,9,8,5,10,10,12,12,10,0,14,8],
[8,11,6,7,9,7,4,10,12,7,9,9,11,0,8],
[14,19,12,8,13,13,8,16,15,13,15,18,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,20,15,16,13,16,10,20,13,14,10,16,15,16],
[9,0,13,13,11,8,13,6,13,8,11,8,10,10,11],
[5,12,0,8,10,8,11,8,12,10,13,7,8,10,11],
[10,12,17,0,12,13,11,11,15,14,12,11,12,11,14],
[9,14,15,13,0,10,13,12,13,16,14,12,14,13,14],
[12,17,17,12,15,0,15,13,16,17,18,15,15,16,19],
[9,12,14,14,12,10,0,9,14,10,9,8,12,12,11],
[15,19,17,14,13,12,16,0,19,14,15,11,15,15,15],
[5,12,13,10,12,9,11,6,0,11,10,10,13,12,7],
[12,17,15,11,9,8,15,11,14,0,13,11,14,9,13],
[11,14,12,13,11,7,16,10,15,12,0,10,11,11,13],
[15,17,18,14,13,10,17,14,15,14,15,0,13,15,12],
[9,15,17,13,11,10,13,10,12,11,14,12,0,11,13],
[10,15,15,14,12,9,13,10,13,16,14,10,14,0,15],
[9,14,14,11,11,6,14,10,18,12,12,13,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,14,13,11,12,13,11,13,11,15,12,8,14],
[12,0,10,10,15,15,11,13,10,12,12,12,10,12,10],
[15,15,0,15,18,16,15,15,14,15,14,16,13,12,17],
[11,15,10,0,14,19,13,13,15,15,13,15,12,14,12],
[12,10,7,11,0,16,13,13,11,12,11,16,11,13,13],
[14,10,9,6,9,0,11,9,9,11,12,14,10,10,10],
[13,14,10,12,12,14,0,15,10,13,16,14,11,8,9],
[12,12,10,12,12,16,10,0,13,11,11,16,15,11,9],
[14,15,11,10,14,16,15,12,0,14,13,17,14,11,15],
[12,13,10,10,13,14,12,14,11,0,9,14,8,11,14],
[14,13,11,12,14,13,9,14,12,16,0,14,11,11,10],
[10,13,9,10,9,11,11,9,8,11,11,0,7,10,11],
[13,15,12,13,14,15,14,10,11,17,14,18,0,12,13],
[17,13,13,11,12,15,17,14,14,14,14,15,13,0,14],
[11,15,8,13,12,15,16,16,10,11,15,14,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,15,16,13,13,17,14,10,10,8,13,12,10],
[13,0,14,9,16,14,14,15,15,10,17,14,9,16,16],
[14,11,0,11,18,15,14,12,9,11,15,9,8,15,12],
[10,16,14,0,16,13,14,14,15,11,11,14,12,12,14],
[9,9,7,9,0,13,12,9,11,9,10,8,8,10,10],
[12,11,10,12,12,0,14,9,15,13,11,9,10,12,9],
[12,11,11,11,13,11,0,11,15,12,10,9,10,15,13],
[8,10,13,11,16,16,14,0,15,12,9,7,8,12,9],
[11,10,16,10,14,10,10,10,0,10,10,10,8,11,13],
[15,15,14,14,16,12,13,13,15,0,15,10,13,15,16],
[15,8,10,14,15,14,15,16,15,10,0,10,9,15,13],
[17,11,16,11,17,16,16,18,15,15,15,0,10,17,15],
[12,16,17,13,17,15,15,17,17,12,16,15,0,15,17],
[13,9,10,13,15,13,10,13,14,10,10,8,10,0,11],
[15,9,13,11,15,16,12,16,12,9,12,10,8,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,9,13,10,13,10,12,10,14,11,13,14,10],
[15,0,12,10,12,11,12,9,12,12,12,10,11,14,10],
[12,13,0,10,13,15,16,14,14,11,12,9,15,20,13],
[16,15,15,0,18,13,15,10,12,15,14,13,15,17,13],
[12,13,12,7,0,9,12,8,13,16,11,12,11,19,7],
[15,14,10,12,16,0,13,12,15,13,14,15,14,15,10],
[12,13,9,10,13,12,0,15,13,10,11,10,17,16,11],
[15,16,11,15,17,13,10,0,11,11,19,14,18,16,15],
[13,13,11,13,12,10,12,14,0,12,10,15,14,15,11],
[15,13,14,10,9,12,15,14,13,0,11,15,14,17,12],
[11,13,13,11,14,11,14,6,15,14,0,8,11,14,8],
[14,15,16,12,13,10,15,11,10,10,17,0,12,20,13],
[12,14,10,10,14,11,8,7,11,11,14,13,0,11,9],
[11,11,5,8,6,10,9,9,10,8,11,5,14,0,11],
[15,15,12,12,18,15,14,10,14,13,17,12,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,11,18,5,9,13,11,12,10,12,11,15,7],
[14,0,9,9,19,8,15,10,12,13,16,16,12,14,7],
[13,16,0,11,13,10,12,18,17,18,13,14,18,16,9],
[14,16,14,0,16,13,13,18,14,15,14,14,11,19,13],
[7,6,12,9,0,5,5,10,8,10,9,12,9,16,3],
[20,17,15,12,20,0,17,22,20,22,19,18,14,19,15],
[16,10,13,12,20,8,0,13,12,11,12,10,12,16,9],
[12,15,7,7,15,3,12,0,15,11,13,12,6,11,10],
[14,13,8,11,17,5,13,10,0,12,7,10,6,15,10],
[13,12,7,10,15,3,14,14,13,0,10,13,3,14,9],
[15,9,12,11,16,6,13,12,18,15,0,12,13,18,14],
[13,9,11,11,13,7,15,13,15,12,13,0,9,16,10],
[14,13,7,14,16,11,13,19,19,22,12,16,0,15,12],
[10,11,9,6,9,6,9,14,10,11,7,9,10,0,7],
[18,18,16,12,22,10,16,15,15,16,11,15,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,4,11,15,3,8,7,18,3,8,8,7,0,3],
[7,0,4,0,4,0,3,0,18,3,8,0,4,0,0],
[21,21,0,18,21,18,21,10,21,13,21,18,10,13,13],
[14,25,7,0,14,3,22,10,18,10,22,3,14,14,10],
[10,21,4,11,0,3,14,3,21,6,14,8,11,6,6],
[22,25,7,22,22,0,22,14,22,17,22,15,14,14,14],
[17,22,4,3,11,3,0,7,18,7,11,0,11,4,3],
[18,25,15,15,22,11,18,0,21,18,18,12,14,7,10],
[7,7,4,7,4,3,7,4,0,7,7,4,4,4,7],
[22,22,12,15,19,8,18,7,18,0,18,8,11,7,7],
[17,17,4,3,11,3,14,7,18,7,0,0,11,11,10],
[17,25,7,22,17,10,25,13,21,17,25,0,17,17,13],
[18,21,15,11,14,11,14,11,21,14,14,8,0,6,6],
[25,25,12,11,19,11,21,18,21,18,14,8,19,0,13],
[22,25,12,15,19,11,22,15,18,18,15,12,19,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,7,6,9,8,12,10,9,6,9,6,11],
[15,0,9,13,7,7,16,14,14,16,14,12,13,11,11],
[15,16,0,17,13,10,18,16,17,17,14,9,14,11,13],
[15,12,8,0,9,11,13,11,14,13,12,8,11,10,14],
[18,18,12,16,0,11,20,17,19,19,15,12,16,12,15],
[19,18,15,14,14,0,20,20,19,17,16,15,14,12,19],
[16,9,7,12,5,5,0,12,14,14,14,8,14,9,10],
[17,11,9,14,8,5,13,0,13,14,8,8,11,10,14],
[13,11,8,11,6,6,11,12,0,10,11,6,8,8,9],
[15,9,8,12,6,8,11,11,15,0,11,8,8,10,9],
[16,11,11,13,10,9,11,17,14,14,0,7,11,8,12],
[19,13,16,17,13,10,17,17,19,17,18,0,17,15,15],
[16,12,11,14,9,11,11,14,17,17,14,8,0,12,13],
[19,14,14,15,13,13,16,15,17,15,17,10,13,0,12],
[14,14,12,11,10,6,15,11,16,16,13,10,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,14,12,9,8,11,9,11,11,8,18,11,15],
[10,0,9,11,9,10,9,8,11,5,6,2,13,9,18],
[10,16,0,13,12,8,6,10,12,5,7,5,19,9,15],
[11,14,12,0,7,10,4,9,10,5,5,7,9,8,13],
[13,16,13,18,0,9,11,16,16,11,12,10,20,13,21],
[16,15,17,15,16,0,15,18,12,13,16,14,17,19,21],
[17,16,19,21,14,10,0,13,10,13,10,11,24,16,22],
[14,17,15,16,9,7,12,0,7,8,9,7,17,14,21],
[16,14,13,15,9,13,15,18,0,11,9,8,20,15,23],
[14,20,20,20,14,12,12,17,14,0,9,9,23,12,22],
[14,19,18,20,13,9,15,16,16,16,0,13,21,17,24],
[17,23,20,18,15,11,14,18,17,16,12,0,23,16,20],
[7,12,6,16,5,8,1,8,5,2,4,2,0,6,12],
[14,16,16,17,12,6,9,11,10,13,8,9,19,0,23],
[10,7,10,12,4,4,3,4,2,3,1,5,13,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,8,11,11,9,10,14,14,15,9,11,15,8],
[14,0,15,10,9,15,14,9,12,12,18,14,9,16,10],
[14,10,0,14,14,14,15,11,14,17,16,13,13,17,14],
[17,15,11,0,16,15,11,15,15,15,15,18,13,18,15],
[14,16,11,9,0,17,15,12,10,14,14,16,14,15,13],
[14,10,11,10,8,0,10,9,12,14,15,14,13,14,11],
[16,11,10,14,10,15,0,10,16,17,9,15,11,17,13],
[15,16,14,10,13,16,15,0,17,14,12,17,16,22,14],
[11,13,11,10,15,13,9,8,0,13,12,16,13,15,13],
[11,13,8,10,11,11,8,11,12,0,11,13,11,18,9],
[10,7,9,10,11,10,16,13,13,14,0,9,10,12,11],
[16,11,12,7,9,11,10,8,9,12,16,0,11,15,10],
[14,16,12,12,11,12,14,9,12,14,15,14,0,15,13],
[10,9,8,7,10,11,8,3,10,7,13,10,10,0,7],
[17,15,11,10,12,14,12,11,12,16,14,15,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,11,8,9,14,8,11,10,14,14,13,10,10,13],
[20,0,17,17,14,18,13,17,8,14,17,18,19,14,19],
[14,8,0,14,10,13,9,17,9,14,12,17,18,11,14],
[17,8,11,0,11,18,9,11,12,13,13,16,17,10,16],
[16,11,15,14,0,15,9,11,7,9,11,13,14,8,16],
[11,7,12,7,10,0,5,9,5,12,14,15,15,9,15],
[17,12,16,16,16,20,0,16,14,16,14,17,22,16,19],
[14,8,8,14,14,16,9,0,11,9,11,13,15,14,14],
[15,17,16,13,18,20,11,14,0,15,17,15,16,11,18],
[11,11,11,12,16,13,9,16,10,0,18,15,15,11,16],
[11,8,13,12,14,11,11,14,8,7,0,11,15,12,17],
[12,7,8,9,12,10,8,12,10,10,14,0,12,9,14],
[15,6,7,8,11,10,3,10,9,10,10,13,0,8,11],
[15,11,14,15,17,16,9,11,14,14,13,16,17,0,15],
[12,6,11,9,9,10,6,11,7,9,8,11,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,5,3,9,9,6,9,6,3,10,8,13,7],
[18,0,11,8,11,13,10,14,11,16,13,14,10,12,10],
[15,14,0,14,12,15,14,15,7,13,11,14,12,17,10],
[20,17,11,0,12,16,12,16,14,17,8,17,10,20,13],
[22,14,13,13,0,21,19,13,10,14,18,15,12,16,16],
[16,12,10,9,4,0,10,12,13,9,10,13,8,15,13],
[16,15,11,13,6,15,0,16,9,19,13,17,11,15,16],
[19,11,10,9,12,13,9,0,12,14,11,12,8,16,11],
[16,14,18,11,15,12,16,13,0,12,12,15,14,15,12],
[19,9,12,8,11,16,6,11,13,0,11,13,11,14,13],
[22,12,14,17,7,15,12,14,13,14,0,15,13,15,14],
[15,11,11,8,10,12,8,13,10,12,10,0,6,12,6],
[17,15,13,15,13,17,14,17,11,14,12,19,0,18,13],
[12,13,8,5,9,10,10,9,10,11,10,13,7,0,5],
[18,15,15,12,9,12,9,14,13,12,11,19,12,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,13,5,18,12,15,10,13,9,11,9,9,12,9],
[19,0,22,10,20,16,17,24,18,16,22,18,14,24,15],
[12,3,0,8,14,12,14,13,13,7,12,11,6,16,12],
[20,15,17,0,20,18,18,19,17,13,19,10,8,19,13],
[7,5,11,5,0,5,7,11,12,6,8,4,7,7,5],
[13,9,13,7,20,0,13,13,17,8,12,11,10,17,9],
[10,8,11,7,18,12,0,11,12,10,8,10,11,12,10],
[15,1,12,6,14,12,14,0,8,7,14,12,8,16,7],
[12,7,12,8,13,8,13,17,0,6,15,9,6,17,9],
[16,9,18,12,19,17,15,18,19,0,17,15,7,17,18],
[14,3,13,6,17,13,17,11,10,8,0,9,8,14,9],
[16,7,14,15,21,14,15,13,16,10,16,0,8,18,12],
[16,11,19,17,18,15,14,17,19,18,17,17,0,17,17],
[13,1,9,6,18,8,13,9,8,8,11,7,8,0,8],
[16,10,13,12,20,16,15,18,16,7,16,13,8,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,6,15,13,15,15,10,10,10,4,10,3,17,13],
[8,0,5,10,6,8,11,9,6,8,10,6,9,4,15],
[19,20,0,18,18,17,20,21,14,14,12,14,8,16,16],
[10,15,7,0,11,4,16,10,7,14,10,10,7,7,15],
[12,19,7,14,0,9,14,10,7,13,10,7,5,10,18],
[10,17,8,21,16,0,14,11,12,14,11,12,8,7,18],
[10,14,5,9,11,11,0,10,8,11,10,7,8,4,16],
[15,16,4,15,15,14,15,0,8,13,6,9,3,11,14],
[15,19,11,18,18,13,17,17,0,12,9,19,13,13,15],
[15,17,11,11,12,11,14,12,13,0,13,11,8,10,21],
[21,15,13,15,15,14,15,19,16,12,0,15,14,14,19],
[15,19,11,15,18,13,18,16,6,14,10,0,9,9,15],
[22,16,17,18,20,17,17,22,12,17,11,16,0,18,21],
[8,21,9,18,15,18,21,14,12,15,11,16,7,0,19],
[12,10,9,10,7,7,9,11,10,4,6,10,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,11,9,8,7,4,9,8,17,4,7,9,11,18],
[8,0,6,12,5,7,8,9,10,15,8,9,10,9,9],
[14,19,0,13,12,11,9,14,8,18,11,11,8,15,17],
[16,13,12,0,9,8,4,10,11,18,5,3,13,7,15],
[17,20,13,16,0,13,11,14,11,14,15,11,13,19,22],
[18,18,14,17,12,0,14,14,18,18,15,13,13,19,20],
[21,17,16,21,14,11,0,20,17,23,16,14,13,17,21],
[16,16,11,15,11,11,5,0,13,12,17,11,10,13,20],
[17,15,17,14,14,7,8,12,0,13,17,12,13,11,17],
[8,10,7,7,11,7,2,13,12,0,6,8,10,8,14],
[21,17,14,20,10,10,9,8,8,19,0,11,17,14,22],
[18,16,14,22,14,12,11,14,13,17,14,0,16,16,20],
[16,15,17,12,12,12,12,15,12,15,8,9,0,13,16],
[14,16,10,18,6,6,8,12,14,17,11,9,12,0,19],
[7,16,8,10,3,5,4,5,8,11,3,5,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,15,12,13,12,11,12,12,8,16,14,17,15],
[10,0,12,11,11,13,12,10,10,11,8,13,11,14,10],
[11,13,0,12,9,12,8,11,8,11,13,14,13,14,12],
[10,14,13,0,12,12,14,11,11,12,11,13,12,15,12],
[13,14,16,13,0,14,14,13,13,13,11,15,15,19,16],
[12,12,13,13,11,0,12,10,12,10,6,13,14,16,13],
[13,13,17,11,11,13,0,14,11,13,10,17,15,17,16],
[14,15,14,14,12,15,11,0,13,13,9,17,17,19,14],
[13,15,17,14,12,13,14,12,0,12,11,17,17,16,14],
[13,14,14,13,12,15,12,12,13,0,9,13,13,18,14],
[17,17,12,14,14,19,15,16,14,16,0,18,20,20,15],
[9,12,11,12,10,12,8,8,8,12,7,0,14,13,13],
[11,14,12,13,10,11,10,8,8,12,5,11,0,14,11],
[8,11,11,10,6,9,8,6,9,7,5,12,11,0,11],
[10,15,13,13,9,12,9,11,11,11,10,12,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,11,10,10,13,8,10,11,10,12,10,15,10],
[17,0,14,11,8,13,25,11,10,13,6,15,6,11,20],
[17,11,0,11,11,5,25,13,10,13,9,7,9,17,15],
[14,14,14,0,14,14,25,12,14,12,6,8,6,11,22],
[15,17,14,11,0,13,23,15,14,21,12,15,14,17,22],
[15,12,20,11,12,0,23,14,22,15,12,14,8,15,22],
[12,0,0,0,2,2,0,8,10,4,2,4,6,7,12],
[17,14,12,13,10,11,17,0,20,15,14,10,8,17,14],
[15,15,15,11,11,3,15,5,0,15,9,5,9,15,15],
[14,12,12,13,4,10,21,10,10,0,10,12,10,15,22],
[15,19,16,19,13,13,23,11,16,15,0,15,16,23,25],
[13,10,18,17,10,11,21,15,20,13,10,0,6,13,20],
[15,19,16,19,11,17,19,17,16,15,9,19,0,19,25],
[10,14,8,14,8,10,18,8,10,10,2,12,6,0,20],
[15,5,10,3,3,3,13,11,10,3,0,5,0,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,15,19,15,10,18,18,16,12,9,19,19,22],
[6,0,10,3,6,7,10,10,15,13,7,10,10,15,9],
[10,15,0,10,10,8,19,13,21,10,10,10,10,15,13],
[10,22,15,0,17,10,13,10,15,17,15,12,22,22,22],
[6,19,15,8,0,9,10,9,18,16,6,9,19,19,9],
[10,18,17,15,16,0,12,18,17,19,15,15,18,18,18],
[15,15,6,12,15,13,0,16,9,10,16,13,16,15,15],
[7,15,12,15,16,7,9,0,15,13,19,5,15,15,18],
[7,10,4,10,7,8,16,10,0,7,7,10,7,13,10],
[9,12,15,8,9,6,15,12,18,0,6,9,12,12,9],
[13,18,15,10,19,10,9,6,18,19,0,8,13,18,10],
[16,15,15,13,16,10,12,20,15,16,17,0,11,15,16],
[6,15,15,3,6,7,9,10,18,13,12,14,0,18,14],
[6,10,10,3,6,7,10,10,12,13,7,10,7,0,9],
[3,16,12,3,16,7,10,7,15,16,15,9,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,11,13,10,13,11,12,14,13,13,14,14],
[10,0,12,15,11,11,11,8,10,13,8,9,10,10,12],
[14,13,0,16,14,15,13,15,14,12,12,13,13,13,15],
[10,10,9,0,10,10,8,13,12,10,7,9,10,11,12],
[14,14,11,15,0,11,11,13,13,11,9,12,11,12,16],
[12,14,10,15,14,0,12,13,12,14,9,13,11,13,13],
[15,14,12,17,14,13,0,14,14,14,11,14,14,14,13],
[12,17,10,12,12,12,11,0,8,11,10,13,11,14,13],
[14,15,11,13,12,13,11,17,0,14,8,15,12,12,12],
[13,12,13,15,14,11,11,14,11,0,11,13,9,13,13],
[11,17,13,18,16,16,14,15,17,14,0,16,14,17,15],
[12,16,12,16,13,12,11,12,10,12,9,0,12,11,13],
[12,15,12,15,14,14,11,14,13,16,11,13,0,15,13],
[11,15,12,14,13,12,11,11,13,12,8,14,10,0,14],
[11,13,10,13,9,12,12,12,13,12,10,12,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,10,5,8,12,8,10,6,11,14,7,6,7],
[19,0,11,13,11,18,16,15,17,12,13,13,9,11,12],
[18,14,0,10,8,13,17,16,19,11,12,13,10,13,9],
[15,12,15,0,5,15,11,16,12,11,8,12,13,10,9],
[20,14,17,20,0,19,13,14,13,16,12,20,11,13,12],
[17,7,12,10,6,0,10,12,9,10,8,9,10,6,8],
[13,9,8,14,12,15,0,15,11,8,11,11,9,15,7],
[17,10,9,9,11,13,10,0,10,11,13,11,16,10,11],
[15,8,6,13,12,16,14,15,0,10,9,11,9,10,12],
[19,13,14,14,9,15,17,14,15,0,14,16,12,10,13],
[14,12,13,17,13,17,14,12,16,11,0,14,15,11,16],
[11,12,12,13,5,16,14,14,14,9,11,0,8,12,7],
[18,16,15,12,14,15,16,9,16,13,10,17,0,12,16],
[19,14,12,15,12,19,10,15,15,15,14,13,13,0,14],
[18,13,16,16,13,17,18,14,13,12,9,18,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,13,12,14,14,12,12,14,10,14,13,6,11],
[13,0,12,11,11,15,13,8,10,11,11,13,15,10,11],
[11,13,0,13,11,14,19,13,14,15,15,16,15,12,15],
[12,14,12,0,13,16,14,11,15,14,13,15,15,8,12],
[13,14,14,12,0,12,18,11,13,15,12,18,13,13,12],
[11,10,11,9,13,0,14,8,13,9,8,12,9,6,8],
[11,12,6,11,7,11,0,9,8,10,8,14,8,7,6],
[13,17,12,14,14,17,16,0,11,15,14,16,16,13,9],
[13,15,11,10,12,12,17,14,0,15,13,18,14,12,13],
[11,14,10,11,10,16,15,10,10,0,12,12,12,10,13],
[15,14,10,12,13,17,17,11,12,13,0,14,14,13,10],
[11,12,9,10,7,13,11,9,7,13,11,0,12,7,9],
[12,10,10,10,12,16,17,9,11,13,11,13,0,8,10],
[19,15,13,17,12,19,18,12,13,15,12,18,17,0,15],
[14,14,10,13,13,17,19,16,12,12,15,16,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,16,16,18,12,12,12,13,11,15,15,15,10],
[11,0,11,13,19,13,12,13,14,15,15,18,10,14,13],
[13,14,0,15,16,18,13,9,12,17,12,17,11,13,12],
[9,12,10,0,13,15,12,12,10,13,13,16,10,14,11],
[9,6,9,12,0,12,11,11,11,12,10,12,8,10,12],
[7,12,7,10,13,0,9,10,11,8,10,11,12,9,9],
[13,13,12,13,14,16,0,14,15,13,15,17,10,14,13],
[13,12,16,13,14,15,11,0,14,12,11,14,15,15,10],
[13,11,13,15,14,14,10,11,0,12,10,15,12,16,11],
[12,10,8,12,13,17,12,13,13,0,13,13,12,11,10],
[14,10,13,12,15,15,10,14,15,12,0,15,12,16,15],
[10,7,8,9,13,14,8,11,10,12,10,0,8,15,9],
[10,15,14,15,17,13,15,10,13,13,13,17,0,14,9],
[10,11,12,11,15,16,11,10,9,14,9,10,11,0,12],
[15,12,13,14,13,16,12,15,14,15,10,16,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,16,9,15,15,14,13,13,10,16,12,15,11],
[16,0,11,17,9,12,15,14,12,15,13,18,5,14,8],
[11,14,0,17,14,5,8,11,10,16,14,15,12,11,13],
[9,8,8,0,11,8,10,12,7,11,14,16,9,15,4],
[16,16,11,14,0,9,12,15,13,19,17,17,19,16,9],
[10,13,20,17,16,0,17,13,13,16,13,18,16,11,15],
[10,10,17,15,13,8,0,15,10,16,15,22,12,12,11],
[11,11,14,13,10,12,10,0,10,11,15,17,13,15,8],
[12,13,15,18,12,12,15,15,0,20,15,17,16,14,7],
[12,10,9,14,6,9,9,14,5,0,13,12,7,9,7],
[15,12,11,11,8,12,10,10,10,12,0,13,11,13,7],
[9,7,10,9,8,7,3,8,8,13,12,0,10,7,5],
[13,20,13,16,6,9,13,12,9,18,14,15,0,12,8],
[10,11,14,10,9,14,13,10,11,16,12,18,13,0,11],
[14,17,12,21,16,10,14,17,18,18,18,20,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,7,11,5,1,1,8,4,4,11,11,4,7],
[17,0,4,10,11,3,9,10,15,9,4,15,12,4,6],
[21,21,0,14,11,18,12,17,21,11,7,13,17,12,17],
[18,15,11,0,13,13,13,11,15,12,14,10,18,13,15],
[14,14,14,12,0,8,10,12,16,16,10,10,13,7,10],
[20,22,7,12,17,0,13,13,20,9,9,13,16,6,11],
[24,16,13,12,15,12,0,14,19,11,13,16,16,9,14],
[24,15,8,14,13,12,11,0,13,12,10,16,14,9,8],
[17,10,4,10,9,5,6,12,0,4,9,8,12,5,11],
[21,16,14,13,9,16,14,13,21,0,5,11,13,13,8],
[21,21,18,11,15,16,12,15,16,20,0,16,24,13,22],
[14,10,12,15,15,12,9,9,17,14,9,0,10,10,8],
[14,13,8,7,12,9,9,11,13,12,1,15,0,10,10],
[21,21,13,12,18,19,16,16,20,12,12,15,15,0,11],
[18,19,8,10,15,14,11,17,14,17,3,17,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,12,11,11,4,19,11,11,9,19,11,16,14],
[14,0,3,14,5,14,7,14,16,10,9,19,8,6,9],
[17,22,0,21,13,12,12,12,14,14,23,16,17,8,12],
[13,11,4,0,4,13,4,12,15,14,10,18,6,4,8],
[14,20,12,21,0,14,13,15,14,14,15,19,10,12,8],
[14,11,13,12,11,0,14,11,11,11,14,18,6,8,12],
[21,18,13,21,12,11,0,16,16,17,19,21,13,16,16],
[6,11,13,13,10,14,9,0,11,5,11,12,10,8,12],
[14,9,11,10,11,14,9,14,0,11,10,18,9,13,14],
[14,15,11,11,11,14,8,20,14,0,10,19,15,11,14],
[16,16,2,15,10,11,6,14,15,15,0,18,8,10,8],
[6,6,9,7,6,7,4,13,7,6,7,0,11,9,2],
[14,17,8,19,15,19,12,15,16,10,17,14,0,11,14],
[9,19,17,21,13,17,9,17,12,14,15,16,14,0,12],
[11,16,13,17,17,13,9,13,11,11,17,23,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,17,17,19,14,15,9,12,13,14,17,14,14],
[11,0,13,9,14,13,18,15,13,12,13,13,9,14,8],
[13,12,0,12,17,17,11,12,9,7,11,12,12,17,12],
[8,16,13,0,9,10,16,12,8,14,13,16,14,8,16],
[8,11,8,16,0,16,11,7,3,6,11,11,11,16,8],
[6,12,8,15,9,0,11,15,6,10,11,6,10,7,12],
[11,7,14,9,14,14,0,15,12,12,8,14,9,14,4],
[10,10,13,13,18,10,10,0,8,3,10,10,8,10,10],
[16,12,16,17,22,19,13,17,0,15,8,13,17,19,12],
[13,13,18,11,19,15,13,22,10,0,10,13,9,16,13],
[12,12,14,12,14,14,17,15,17,15,0,15,12,14,7],
[11,12,13,9,14,19,11,15,12,12,10,0,4,14,9],
[8,16,13,11,14,15,16,17,8,16,13,21,0,19,13],
[11,11,8,17,9,18,11,15,6,9,11,11,6,0,11],
[11,17,13,9,17,13,21,15,13,12,18,16,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,8,10,12,12,10,11,17,13,13,13,19,12,8],
[13,0,19,15,21,11,17,15,17,15,11,11,23,15,15],
[17,6,0,13,12,9,13,13,13,15,11,9,19,15,6],
[15,10,12,0,18,4,17,17,19,17,9,11,25,19,6],
[13,4,13,7,0,9,11,9,15,11,9,9,15,15,9],
[13,14,16,21,16,0,21,19,19,19,19,19,21,23,6],
[15,8,12,8,14,4,0,15,19,17,9,9,19,14,6],
[14,10,12,8,16,6,10,0,14,12,4,8,23,12,8],
[8,8,12,6,10,6,6,11,0,15,11,6,17,12,8],
[12,10,10,8,14,6,8,13,10,0,6,6,21,8,6],
[12,14,14,16,16,6,16,21,14,19,0,12,23,12,10],
[12,14,16,14,16,6,16,17,19,19,13,0,21,16,6],
[6,2,6,0,10,4,6,2,8,4,2,4,0,8,4],
[13,10,10,6,10,2,11,13,13,17,13,9,17,0,4],
[17,10,19,19,16,19,19,17,17,19,15,19,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,12,14,13,12,11,11,13,12,15,16,13],
[14,0,16,14,14,14,14,13,13,13,12,15,18,18,15],
[11,9,0,10,9,10,12,12,11,12,9,11,12,15,11],
[14,11,15,0,13,13,11,11,11,8,13,12,15,15,14],
[13,11,16,12,0,13,14,12,12,11,13,11,17,17,14],
[11,11,15,12,12,0,15,13,15,12,9,10,14,16,12],
[12,11,13,14,11,10,0,10,12,12,10,12,13,15,11],
[13,12,13,14,13,12,15,0,14,12,11,12,18,15,12],
[14,12,14,14,13,10,13,11,0,13,11,10,18,16,12],
[14,12,13,17,14,13,13,13,12,0,14,12,19,14,15],
[12,13,16,12,12,16,15,14,14,11,0,13,17,16,15],
[13,10,14,13,14,15,13,13,15,13,12,0,18,17,17],
[10,7,13,10,8,11,12,7,7,6,8,7,0,13,9],
[9,7,10,10,8,9,10,10,9,11,9,8,12,0,11],
[12,10,14,11,11,13,14,13,13,10,10,8,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,12,14,17,0,3,0,8,12,9,9,0,16],
[12,0,12,9,13,20,12,12,9,8,11,12,9,3,12],
[17,13,0,4,17,25,10,7,14,12,15,4,13,7,16],
[13,16,21,0,17,21,13,12,13,12,15,4,12,3,16],
[11,12,8,8,0,11,0,11,8,8,8,11,8,11,11],
[8,5,0,4,14,0,0,7,0,8,4,1,0,4,7],
[25,13,15,12,25,25,0,15,22,12,15,16,21,15,24],
[22,13,18,13,14,18,10,0,18,9,12,9,18,12,17],
[25,16,11,12,17,25,3,7,0,15,15,12,24,15,16],
[17,17,13,13,17,17,13,16,10,0,7,13,16,7,16],
[13,14,10,10,17,21,10,13,10,18,0,13,10,3,13],
[16,13,21,21,14,24,9,16,13,12,12,0,13,7,16],
[16,16,12,13,17,25,4,7,1,9,15,12,0,15,17],
[25,22,18,22,14,21,10,13,10,18,22,18,10,0,17],
[9,13,9,9,14,18,1,8,9,9,12,9,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,15,15,15,14,13,11,15,13,15,11,17,13],
[11,0,9,16,12,14,11,7,15,14,11,12,11,16,13],
[10,16,0,14,12,15,14,11,14,14,12,11,14,17,17],
[10,9,11,0,12,12,10,10,8,13,11,11,7,16,11],
[10,13,13,13,0,12,9,9,14,11,13,10,11,14,12],
[10,11,10,13,13,0,11,9,10,9,9,10,12,14,11],
[11,14,11,15,16,14,0,12,13,12,15,11,13,16,15],
[12,18,14,15,16,16,13,0,14,16,13,15,12,16,17],
[14,10,11,17,11,15,12,11,0,10,12,12,13,17,10],
[10,11,11,12,14,16,13,9,15,0,12,11,13,16,13],
[12,14,13,14,12,16,10,12,13,13,0,10,11,16,13],
[10,13,14,14,15,15,14,10,13,14,15,0,15,15,14],
[14,14,11,18,14,13,12,13,12,12,14,10,0,17,14],
[8,9,8,9,11,11,9,9,8,9,9,10,8,0,11],
[12,12,8,14,13,14,10,8,15,12,12,11,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,15,15,11,17,19,10,22,13,22,11,20,19,17],
[0,0,10,15,8,15,12,3,19,6,17,4,10,11,12],
[10,15,0,17,8,13,16,15,19,10,19,6,22,18,12],
[10,10,8,0,11,16,19,13,15,10,14,9,20,14,8],
[14,17,17,14,0,12,19,10,11,10,17,11,20,16,9],
[8,10,12,9,13,0,16,10,11,7,14,11,14,8,9],
[6,13,9,6,6,9,0,8,10,9,18,7,9,14,11],
[15,22,10,12,15,15,17,0,19,7,20,4,15,15,12],
[3,6,6,10,14,14,15,6,0,9,10,7,13,14,11],
[12,19,15,15,15,18,16,18,16,0,20,4,23,23,12],
[3,8,6,11,8,11,7,5,15,5,0,6,11,14,8],
[14,21,19,16,14,14,18,21,18,21,19,0,21,19,11],
[5,15,3,5,5,11,16,10,12,2,14,4,0,14,5],
[6,14,7,11,9,17,11,10,11,2,11,6,11,0,9],
[8,13,13,17,16,16,14,13,14,13,17,14,20,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,21,17,11,15,17,18,16,15,15,15,15,19],
[7,0,7,17,9,10,4,12,14,14,6,7,3,9,15],
[11,18,0,17,12,11,10,12,13,14,9,8,6,10,13],
[4,8,8,0,8,8,7,10,8,11,8,7,5,10,8],
[8,16,13,17,0,15,6,15,10,11,12,9,11,9,10],
[14,15,14,17,10,0,8,11,15,11,12,14,10,13,13],
[10,21,15,18,19,17,0,17,14,17,16,10,15,13,16],
[8,13,13,15,10,14,8,0,13,8,11,10,9,13,14],
[7,11,12,17,15,10,11,12,0,14,13,9,12,9,10],
[9,11,11,14,14,14,8,17,11,0,14,13,12,10,12],
[10,19,16,17,13,13,9,14,12,11,0,11,11,9,12],
[10,18,17,18,16,11,15,15,16,12,14,0,16,8,16],
[10,22,19,20,14,15,10,16,13,13,14,9,0,14,16],
[10,16,15,15,16,12,12,12,16,15,16,17,11,0,17],
[6,10,12,17,15,12,9,11,15,13,13,9,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,21,13,11,13,15,14,12,16,14,11,18,18],
[10,0,13,17,12,12,11,14,13,9,12,9,10,13,8],
[14,12,0,19,15,10,6,11,15,12,13,8,7,10,10],
[4,8,6,0,8,9,7,7,10,7,7,6,6,7,6],
[12,13,10,17,0,9,9,18,10,16,12,7,10,13,13],
[14,13,15,16,16,0,14,17,11,14,15,12,10,13,15],
[12,14,19,18,16,11,0,16,14,12,17,13,12,17,13],
[10,11,14,18,7,8,9,0,12,12,11,5,10,10,11],
[11,12,10,15,15,14,11,13,0,12,13,9,8,11,12],
[13,16,13,18,9,11,13,13,13,0,14,11,11,15,12],
[9,13,12,18,13,10,8,14,12,11,0,11,11,12,17],
[11,16,17,19,18,13,12,20,16,14,14,0,14,14,18],
[14,15,18,19,15,15,13,15,17,14,14,11,0,15,16],
[7,12,15,18,12,12,8,15,14,10,13,11,10,0,13],
[7,17,15,19,12,10,12,14,13,13,8,7,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,14,14,13,14,14,13,14,14,14,15,15,12],
[11,0,14,11,14,14,14,13,12,17,12,14,15,13,12],
[8,11,0,9,11,10,14,13,10,14,13,13,11,12,13],
[11,14,16,0,12,14,15,14,13,16,15,16,14,14,16],
[11,11,14,13,0,12,12,10,9,14,11,12,12,13,11],
[12,11,15,11,13,0,10,13,10,18,14,13,16,14,13],
[11,11,11,10,13,15,0,17,14,13,12,15,12,14,10],
[11,12,12,11,15,12,8,0,11,12,11,13,14,13,8],
[12,13,15,12,16,15,11,14,0,14,13,14,14,14,11],
[11,8,11,9,11,7,12,13,11,0,12,14,9,11,8],
[11,13,12,10,14,11,13,14,12,13,0,17,11,14,13],
[11,11,12,9,13,12,10,12,11,11,8,0,12,11,9],
[10,10,14,11,13,9,13,11,11,16,14,13,0,11,11],
[10,12,13,11,12,11,11,12,11,14,11,14,14,0,9],
[13,13,12,9,14,12,15,17,14,17,12,16,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,10,16,13,14,9,13,15,12,14,13,12,15],
[11,0,10,9,15,11,13,10,10,10,9,8,9,15,11],
[14,15,0,10,15,16,15,13,13,16,15,14,12,14,15],
[15,16,15,0,16,13,13,10,17,18,13,16,14,17,17],
[9,10,10,9,0,11,9,10,13,12,12,13,11,12,14],
[12,14,9,12,14,0,14,11,13,12,13,15,10,12,13],
[11,12,10,12,16,11,0,13,14,14,10,11,10,17,11],
[16,15,12,15,15,14,12,0,17,20,11,16,11,15,15],
[12,15,12,8,12,12,11,8,0,11,11,12,7,13,15],
[10,15,9,7,13,13,11,5,14,0,13,13,9,14,14],
[13,16,10,12,13,12,15,14,14,12,0,14,9,16,12],
[11,17,11,9,12,10,14,9,13,12,11,0,10,16,12],
[12,16,13,11,14,15,15,14,18,16,16,15,0,17,13],
[13,10,11,8,13,13,8,10,12,11,9,9,8,0,13],
[10,14,10,8,11,12,14,10,10,11,13,13,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,15,11,5,12,12,15,13,15,8,12,14,13],
[12,0,12,17,12,10,10,9,13,14,13,11,13,15,13],
[12,13,0,17,13,12,14,11,16,13,12,10,13,15,15],
[10,8,8,0,10,5,9,9,13,10,8,7,8,13,10],
[14,13,12,15,0,13,10,11,16,11,13,9,12,13,13],
[20,15,13,20,12,0,16,15,16,15,16,14,14,15,16],
[13,15,11,16,15,9,0,12,18,15,13,12,12,14,16],
[13,16,14,16,14,10,13,0,15,14,14,13,10,12,14],
[10,12,9,12,9,9,7,10,0,9,13,8,9,11,10],
[12,11,12,15,14,10,10,11,16,0,11,13,12,13,14],
[10,12,13,17,12,9,12,11,12,14,0,11,13,13,12],
[17,14,15,18,16,11,13,12,17,12,14,0,13,15,16],
[13,12,12,17,13,11,13,15,16,13,12,12,0,15,13],
[11,10,10,12,12,10,11,13,14,12,12,10,10,0,12],
[12,12,10,15,12,9,9,11,15,11,13,9,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,12,12,16,10,9,15,13,11,9,16,8,12],
[10,0,10,12,12,15,10,11,11,15,10,11,13,7,11],
[14,15,0,11,14,16,11,11,13,17,14,13,17,9,9],
[13,13,14,0,11,13,13,11,12,12,18,15,15,11,13],
[13,13,11,14,0,13,12,12,14,15,14,14,14,11,10],
[9,10,9,12,12,0,9,11,10,12,13,10,9,5,10],
[15,15,14,12,13,16,0,8,11,14,14,12,13,10,15],
[16,14,14,14,13,14,17,0,15,16,14,12,18,9,12],
[10,14,12,13,11,15,14,10,0,15,15,12,13,8,11],
[12,10,8,13,10,13,11,9,10,0,10,11,15,9,9],
[14,15,11,7,11,12,11,11,10,15,0,12,14,11,12],
[16,14,12,10,11,15,13,13,13,14,13,0,15,13,12],
[9,12,8,10,11,16,12,7,12,10,11,10,0,7,9],
[17,18,16,14,14,20,15,16,17,16,14,12,18,0,14],
[13,14,16,12,15,15,10,13,14,16,13,13,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,5,4,23,16,9,16,9,15,9,2,11,17],
[15,0,9,8,2,13,10,8,10,12,13,8,5,10,11],
[15,16,0,15,6,22,19,16,17,10,18,16,11,17,15],
[20,17,10,0,13,23,20,9,16,11,23,12,13,17,17],
[21,23,19,12,0,21,18,18,16,20,21,14,13,16,17],
[2,12,3,2,4,0,4,8,12,7,15,5,0,4,9],
[9,15,6,5,7,21,0,7,16,9,19,10,1,6,15],
[16,17,9,16,7,17,18,0,14,11,17,8,12,16,12],
[9,15,8,9,9,13,9,11,0,10,9,9,9,7,9],
[16,13,15,14,5,18,16,14,15,0,15,10,14,10,14],
[10,12,7,2,4,10,6,8,16,10,0,8,2,8,17],
[16,17,9,13,11,20,15,17,16,15,17,0,9,13,15],
[23,20,14,12,12,25,24,13,16,11,23,16,0,20,20],
[14,15,8,8,9,21,19,9,18,15,17,12,5,0,18],
[8,14,10,8,8,16,10,13,16,11,8,10,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,13,0,6,12,0,12,0,0,6,0,0,13],
[18,0,12,13,0,6,12,12,12,6,12,18,12,6,13],
[13,13,0,13,13,13,6,13,13,7,0,12,13,7,13],
[12,12,12,0,6,6,6,12,12,0,6,18,12,6,19],
[25,25,12,19,0,13,12,19,19,6,12,18,19,13,19],
[19,19,12,19,12,0,12,12,6,6,12,18,12,12,19],
[13,13,19,19,13,13,0,13,19,13,7,12,13,13,19],
[25,13,12,13,6,13,12,0,19,6,12,12,12,6,19],
[13,13,12,13,6,19,6,6,0,6,6,12,6,6,19],
[25,19,18,25,19,19,12,19,19,0,12,18,19,13,25],
[25,13,25,19,13,13,18,13,19,13,0,12,13,13,19],
[19,7,13,7,7,7,13,13,13,7,13,0,19,13,7],
[25,13,12,13,6,13,12,13,19,6,12,6,0,13,13],
[25,19,18,19,12,13,12,19,19,12,12,12,12,0,19],
[12,12,12,6,6,6,6,6,6,0,6,18,12,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,11,11,10,12,11,10,13,12,11,8,11,7],
[17,0,13,16,12,17,12,12,13,13,13,13,14,13,10],
[21,12,0,21,16,22,14,13,16,17,17,16,12,12,13],
[14,9,4,0,10,16,9,10,8,10,9,12,6,12,9],
[14,13,9,15,0,16,11,11,9,12,13,13,11,14,10],
[15,8,3,9,9,0,9,7,8,11,10,15,6,10,5],
[13,13,11,16,14,16,0,12,14,15,14,16,8,14,11],
[14,13,12,15,14,18,13,0,12,13,12,14,10,13,9],
[15,12,9,17,16,17,11,13,0,15,15,16,9,17,14],
[12,12,8,15,13,14,10,12,10,0,14,16,7,14,11],
[13,12,8,16,12,15,11,13,10,11,0,11,7,12,5],
[14,12,9,13,12,10,9,11,9,9,14,0,9,12,7],
[17,11,13,19,14,19,17,15,16,18,18,16,0,16,13],
[14,12,13,13,11,15,11,12,8,11,13,13,9,0,10],
[18,15,12,16,15,20,14,16,11,14,20,18,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,14,7,5,14,1,11,5,10,3,8,4,11],
[17,0,10,15,6,3,14,4,10,6,7,2,16,2,9],
[16,15,0,18,10,13,16,11,10,17,12,9,16,16,6],
[11,10,7,0,5,7,11,5,8,6,3,4,6,10,10],
[18,19,15,20,0,20,15,15,13,12,21,13,14,19,10],
[20,22,12,18,5,0,14,5,17,6,12,12,13,13,10],
[11,11,9,14,10,11,0,11,18,12,13,6,11,11,11],
[24,21,14,20,10,20,14,0,17,15,14,11,13,18,15],
[14,15,15,17,12,8,7,8,0,12,8,8,9,7,13],
[20,19,8,19,13,19,13,10,13,0,16,8,14,19,14],
[15,18,13,22,4,13,12,11,17,9,0,7,9,13,11],
[22,23,16,21,12,13,19,14,17,17,18,0,21,15,9],
[17,9,9,19,11,12,14,12,16,11,16,4,0,10,12],
[21,23,9,15,6,12,14,7,18,6,12,10,15,0,12],
[14,16,19,15,15,15,14,10,12,11,14,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,19,9,12,16,6,15,18,18,11,9,14,5,14],
[9,0,17,12,14,13,5,16,15,11,8,9,9,6,9],
[6,8,0,6,11,13,5,13,18,6,10,8,11,6,11],
[16,13,19,0,9,13,13,15,15,13,9,12,8,6,11],
[13,11,14,16,0,12,9,12,12,11,6,9,10,11,6],
[9,12,12,12,13,0,9,14,8,6,12,9,11,7,11],
[19,20,20,12,16,16,0,22,15,22,12,15,17,12,14],
[10,9,12,10,13,11,3,0,13,9,6,6,9,6,6],
[7,10,7,10,13,17,10,12,0,7,11,7,14,7,10],
[7,14,19,12,14,19,3,16,18,0,12,10,14,8,12],
[14,17,15,16,19,13,13,19,14,13,0,11,11,14,11],
[16,16,17,13,16,16,10,19,18,15,14,0,16,14,16],
[11,16,14,17,15,14,8,16,11,11,14,9,0,11,17],
[20,19,19,19,14,18,13,19,18,17,11,11,14,0,14],
[11,16,14,14,19,14,11,19,15,13,14,9,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,19,16,18,15,22,19,15,11,16,20,20,13,15],
[16,0,16,12,13,16,21,19,14,13,13,18,19,18,16],
[6,9,0,15,13,11,15,11,7,13,12,15,16,12,14],
[9,13,10,0,13,8,10,12,8,9,16,19,16,15,14],
[7,12,12,12,0,9,13,15,14,6,15,12,11,12,11],
[10,9,14,17,16,0,16,9,12,8,15,14,16,11,16],
[3,4,10,15,12,9,0,12,8,9,12,19,17,14,14],
[6,6,14,13,10,16,13,0,15,11,15,13,12,10,15],
[10,11,18,17,11,13,17,10,0,10,17,16,18,11,14],
[14,12,12,16,19,17,16,14,15,0,20,23,20,16,15],
[9,12,13,9,10,10,13,10,8,5,0,16,16,14,10],
[5,7,10,6,13,11,6,12,9,2,9,0,19,10,10],
[5,6,9,9,14,9,8,13,7,5,9,6,0,8,6],
[12,7,13,10,13,14,11,15,14,9,11,15,17,0,15],
[10,9,11,11,14,9,11,10,11,10,15,15,19,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,5,12,8,9,6,7,10,19,9,9,12,7,9],
[7,0,4,8,6,4,5,7,8,10,11,4,7,5,5],
[20,21,0,22,11,17,17,19,17,19,18,17,17,17,18],
[13,17,3,0,5,11,10,12,9,17,9,5,9,10,14],
[17,19,14,20,0,16,11,18,18,20,14,16,17,13,17],
[16,21,8,14,9,0,13,11,12,14,12,9,11,10,11],
[19,20,8,15,14,12,0,18,16,16,16,15,17,14,13],
[18,18,6,13,7,14,7,0,11,16,11,10,16,13,17],
[15,17,8,16,7,13,9,14,0,19,12,13,18,13,17],
[6,15,6,8,5,11,9,9,6,0,12,6,11,7,12],
[16,14,7,16,11,13,9,14,13,13,0,10,12,14,14],
[16,21,8,20,9,16,10,15,12,19,15,0,19,17,19],
[13,18,8,16,8,14,8,9,7,14,13,6,0,10,12],
[18,20,8,15,12,15,11,12,12,18,11,8,15,0,17],
[16,20,7,11,8,14,12,8,8,13,11,6,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,15,10,15,10,7,11,9,7,10,12,13,11,16],
[17,0,17,16,20,16,15,19,11,12,13,7,16,13,17],
[10,8,0,9,14,11,12,11,15,5,17,6,13,10,12],
[15,9,16,0,22,13,11,11,17,11,12,13,10,16,18],
[10,5,11,3,0,5,7,7,11,8,12,5,9,16,8],
[15,9,14,12,20,0,14,8,14,13,17,11,14,16,14],
[18,10,13,14,18,11,0,15,15,13,20,10,17,10,15],
[14,6,14,14,18,17,10,0,16,10,19,11,10,13,13],
[16,14,10,8,14,11,10,9,0,8,12,12,12,10,15],
[18,13,20,14,17,12,12,15,17,0,20,17,12,16,18],
[15,12,8,13,13,8,5,6,13,5,0,5,7,12,13],
[13,18,19,12,20,14,15,14,13,8,20,0,12,12,17],
[12,9,12,15,16,11,8,15,13,13,18,13,0,18,13],
[14,12,15,9,9,9,15,12,15,9,13,13,7,0,16],
[9,8,13,7,17,11,10,12,10,7,12,8,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,14,15,14,14,13,12,12,13,11,17,16,13],
[8,0,9,9,7,8,11,10,11,8,11,8,12,11,11],
[8,16,0,13,11,10,11,11,11,8,10,8,13,13,12],
[11,16,12,0,11,15,13,12,13,10,14,13,15,16,13],
[10,18,14,14,0,14,15,15,14,11,16,12,15,16,14],
[11,17,15,10,11,0,11,11,15,11,14,16,15,15,14],
[11,14,14,12,10,14,0,9,15,13,15,14,17,15,14],
[12,15,14,13,10,14,16,0,15,12,15,13,15,15,14],
[13,14,14,12,11,10,10,10,0,14,13,11,14,14,10],
[13,17,17,15,14,14,12,13,11,0,15,14,18,14,14],
[12,14,15,11,9,11,10,10,12,10,0,9,13,13,14],
[14,17,17,12,13,9,11,12,14,11,16,0,17,16,14],
[8,13,12,10,10,10,8,10,11,7,12,8,0,13,14],
[9,14,12,9,9,10,10,10,11,11,12,9,12,0,11],
[12,14,13,12,11,11,11,11,15,11,11,11,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,15,8,15,14,13,12,16,13,15,17,10,14],
[14,0,15,20,14,14,11,16,12,19,15,13,22,17,14],
[11,10,0,13,11,11,11,14,9,17,12,12,14,10,11],
[10,5,12,0,10,8,13,15,8,14,11,12,14,12,10],
[17,11,14,15,0,10,13,13,10,12,15,11,14,17,15],
[10,11,14,17,15,0,9,16,13,16,15,13,18,12,16],
[11,14,14,12,12,16,0,17,17,16,17,16,16,15,14],
[12,9,11,10,12,9,8,0,12,16,15,12,14,16,12],
[13,13,16,17,15,12,8,13,0,12,17,16,18,15,16],
[9,6,8,11,13,9,9,9,13,0,9,10,14,12,11],
[12,10,13,14,10,10,8,10,8,16,0,11,15,11,11],
[10,12,13,13,14,12,9,13,9,15,14,0,13,11,9],
[8,3,11,11,11,7,9,11,7,11,10,12,0,9,8],
[15,8,15,13,8,13,10,9,10,13,14,14,16,0,10],
[11,11,14,15,10,9,11,13,9,14,14,16,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,3,15,9,13,9,9,12,15,18,14,7,9,14],
[16,0,11,12,18,16,13,20,15,22,20,13,17,11,16],
[22,14,0,18,13,19,16,16,15,18,21,17,10,11,16],
[10,13,7,0,10,10,14,17,16,16,17,11,12,18,18],
[16,7,12,15,0,17,14,15,11,15,13,13,10,8,16],
[12,9,6,15,8,0,12,13,12,15,16,12,10,8,16],
[16,12,9,11,11,13,0,16,11,18,18,12,12,11,14],
[16,5,9,8,10,12,9,0,10,17,18,12,7,7,17],
[13,10,10,9,14,13,14,15,0,14,11,7,9,2,16],
[10,3,7,9,10,10,7,8,11,0,7,7,9,11,16],
[7,5,4,8,12,9,7,7,14,18,0,9,6,11,18],
[11,12,8,14,12,13,13,13,18,18,16,0,10,12,14],
[18,8,15,13,15,15,13,18,16,16,19,15,0,11,18],
[16,14,14,7,17,17,14,18,23,14,14,13,14,0,16],
[11,9,9,7,9,9,11,8,9,9,7,11,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,15,14,15,12,18,13,16,13,20,16,19,16],
[9,0,14,9,11,13,8,19,12,14,15,15,10,13,17],
[11,11,0,14,16,12,10,16,7,15,12,17,12,8,13],
[10,16,11,0,15,14,8,18,10,14,10,15,14,14,16],
[11,14,9,10,0,12,12,12,11,12,11,15,18,14,15],
[10,12,13,11,13,0,16,13,13,12,10,19,18,18,17],
[13,17,15,17,13,9,0,14,13,9,13,16,16,15,15],
[7,6,9,7,13,12,11,0,8,11,7,11,13,12,14],
[12,13,18,15,14,12,12,17,0,15,14,18,13,10,19],
[9,11,10,11,13,13,16,14,10,0,8,16,14,15,21],
[12,10,13,15,14,15,12,18,11,17,0,13,10,20,17],
[5,10,8,10,10,6,9,14,7,9,12,0,14,15,17],
[9,15,13,11,7,7,9,12,12,11,15,11,0,14,13],
[6,12,17,11,11,7,10,13,15,10,5,10,11,0,13],
[9,8,12,9,10,8,10,11,6,4,8,8,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,11,11,11,14,14,12,16,16,18,15,13,9],
[9,0,12,13,14,11,12,10,12,15,14,15,13,12,13],
[15,13,0,11,11,11,12,13,13,15,14,16,13,13,13],
[14,12,14,0,14,13,11,12,15,17,17,14,14,11,15],
[14,11,14,11,0,14,12,12,15,17,10,15,10,11,16],
[14,14,14,12,11,0,13,12,13,14,12,17,13,13,10],
[11,13,13,14,13,12,0,13,12,12,12,15,13,13,12],
[11,15,12,13,13,13,12,0,15,17,14,18,16,14,14],
[13,13,12,10,10,12,13,10,0,15,13,15,15,11,11],
[9,10,10,8,8,11,13,8,10,0,10,8,9,13,9],
[9,11,11,8,15,13,13,11,12,15,0,14,11,13,14],
[7,10,9,11,10,8,10,7,10,17,11,0,10,9,9],
[10,12,12,11,15,12,12,9,10,16,14,15,0,11,14],
[12,13,12,14,14,12,12,11,14,12,12,16,14,0,14],
[16,12,12,10,9,15,13,11,14,16,11,16,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,12,10,13,7,10,12,9,12,9,11,10,13],
[11,0,11,11,10,9,9,11,10,13,10,11,10,10,16],
[10,14,0,13,8,12,12,11,12,13,11,13,10,9,16],
[13,14,12,0,12,15,16,13,13,14,19,11,11,13,20],
[15,15,17,13,0,15,13,17,17,13,16,12,10,6,18],
[12,16,13,10,10,0,8,10,9,12,11,12,9,9,15],
[18,16,13,9,12,17,0,14,18,16,16,10,10,14,19],
[15,14,14,12,8,15,11,0,13,11,18,12,8,11,20],
[13,15,13,12,8,16,7,12,0,13,11,11,7,9,15],
[16,12,12,11,12,13,9,14,12,0,17,14,11,10,17],
[13,15,14,6,9,14,9,7,14,8,0,12,9,10,13],
[16,14,12,14,13,13,15,13,14,11,13,0,10,13,16],
[14,15,15,14,15,16,15,17,18,14,16,15,0,10,18],
[15,15,16,12,19,16,11,14,16,15,15,12,15,0,15],
[12,9,9,5,7,10,6,5,10,8,12,9,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,9,11,11,10,13,12,8,13,11,10,9,11],
[16,0,12,14,11,16,12,13,15,12,12,16,15,11,15],
[16,13,0,11,12,16,10,12,13,12,12,15,12,13,11],
[16,11,14,0,10,18,13,14,15,12,11,16,14,9,13],
[14,14,13,15,0,15,13,11,14,15,11,16,14,12,14],
[14,9,9,7,10,0,8,12,8,9,9,10,9,5,8],
[15,13,15,12,12,17,0,14,13,14,11,14,14,12,14],
[12,12,13,11,14,13,11,0,13,11,10,15,14,10,15],
[13,10,12,10,11,17,12,12,0,12,10,13,13,10,12],
[17,13,13,13,10,16,11,14,13,0,15,12,13,12,13],
[12,13,13,14,14,16,14,15,15,10,0,16,12,10,15],
[14,9,10,9,9,15,11,10,12,13,9,0,11,9,11],
[15,10,13,11,11,16,11,11,12,12,13,14,0,12,14],
[16,14,12,16,13,20,13,15,15,13,15,16,13,0,15],
[14,10,14,12,11,17,11,10,13,12,10,14,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,13,11,16,4,5,16,12,9,12,12,5,13,13],
[22,0,17,19,20,19,10,13,19,13,15,20,22,17,17],
[12,8,0,12,16,16,8,17,10,7,15,19,13,17,13],
[14,6,13,0,19,13,8,17,10,11,13,17,10,9,13],
[9,5,9,6,0,10,9,9,5,3,9,15,10,7,9],
[21,6,9,12,15,0,1,15,12,7,14,13,8,9,9],
[20,15,17,17,16,24,0,19,15,9,16,22,16,18,13],
[9,12,8,8,16,10,6,0,8,8,8,15,11,11,12],
[13,6,15,15,20,13,10,17,0,14,17,17,10,14,14],
[16,12,18,14,22,18,16,17,11,0,19,22,19,19,13],
[13,10,10,12,16,11,9,17,8,6,0,13,11,13,10],
[13,5,6,8,10,12,3,10,8,3,12,0,11,14,7],
[20,3,12,15,15,17,9,14,15,6,14,14,0,13,12],
[12,8,8,16,18,16,7,14,11,6,12,11,12,0,12],
[12,8,12,12,16,16,12,13,11,12,15,18,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,15,16,21,12,15,12,18,15,12,14,12,11],
[11,0,18,8,19,19,18,13,16,19,14,10,12,17,16],
[8,7,0,4,8,13,12,8,5,15,7,4,6,6,13],
[10,17,21,0,11,21,15,11,16,22,15,12,14,12,15],
[9,6,17,14,0,18,15,8,10,17,10,11,13,9,11],
[4,6,12,4,7,0,9,10,6,7,2,6,5,8,11],
[13,7,13,10,10,16,0,5,10,18,8,9,13,9,7],
[10,12,17,14,17,15,20,0,13,20,15,14,13,17,17],
[13,9,20,9,15,19,15,12,0,17,12,8,8,8,15],
[7,6,10,3,8,18,7,5,8,0,7,4,8,6,6],
[10,11,18,10,15,23,17,10,13,18,0,9,13,11,14],
[13,15,21,13,14,19,16,11,17,21,16,0,14,15,16],
[11,13,19,11,12,20,12,12,17,17,12,11,0,8,14],
[13,8,19,13,16,17,16,8,17,19,14,10,17,0,16],
[14,9,12,10,14,14,18,8,10,19,11,9,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,17,9,13,12,16,16,14,17,17,14,12,14],
[13,0,18,13,13,16,13,15,10,20,16,18,12,12,12],
[6,7,0,6,5,9,5,11,6,10,10,12,5,5,9],
[8,12,19,0,7,11,11,13,10,16,11,14,11,12,11],
[16,12,20,18,0,14,15,16,14,19,16,17,14,17,13],
[12,9,16,14,11,0,10,7,11,15,11,13,11,10,13],
[13,12,20,14,10,15,0,15,15,16,10,16,10,11,12],
[9,10,14,12,9,18,10,0,11,14,10,12,15,12,15],
[9,15,19,15,11,14,10,14,0,19,12,17,13,13,14],
[11,5,15,9,6,10,9,11,6,0,11,10,4,6,7],
[8,9,15,14,9,14,15,15,13,14,0,15,15,14,14],
[8,7,13,11,8,12,9,13,8,15,10,0,14,11,14],
[11,13,20,14,11,14,15,10,12,21,10,11,0,13,11],
[13,13,20,13,8,15,14,13,12,19,11,14,12,0,9],
[11,13,16,14,12,12,13,10,11,18,11,11,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,9,16,15,17,18,16,14,18,14,19,15,19,17],
[5,0,9,9,10,8,11,11,11,16,3,10,15,8,11],
[16,16,0,17,11,15,16,14,11,17,9,16,20,16,22],
[9,16,8,0,12,14,14,11,13,16,8,13,17,13,15],
[10,15,14,13,0,17,13,20,8,14,12,16,20,15,16],
[8,17,10,11,8,0,10,10,9,11,6,11,10,10,18],
[7,14,9,11,12,15,0,13,13,18,6,16,14,9,16],
[9,14,11,14,5,15,12,0,9,15,4,11,13,12,16],
[11,14,14,12,17,16,12,16,0,14,9,13,18,13,13],
[7,9,8,9,11,14,7,10,11,0,6,11,16,10,15],
[11,22,16,17,13,19,19,21,16,19,0,22,17,12,23],
[6,15,9,12,9,14,9,14,12,14,3,0,16,7,15],
[10,10,5,8,5,15,11,12,7,9,8,9,0,13,17],
[6,17,9,12,10,15,16,13,12,15,13,18,12,0,18],
[8,14,3,10,9,7,9,9,12,10,2,10,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,17,14,10,12,11,15,12,15,14,14,14,12],
[8,0,4,9,15,9,9,8,11,11,15,9,14,8,11],
[12,21,0,12,15,13,13,12,19,11,21,14,16,17,15],
[8,16,13,0,17,9,12,12,13,13,16,10,15,9,14],
[11,10,10,8,0,9,7,14,14,5,10,11,10,8,12],
[15,16,12,16,16,0,11,17,15,12,17,17,16,12,17],
[13,16,12,13,18,14,0,17,12,11,15,16,16,13,11],
[14,17,13,13,11,8,8,0,12,9,15,15,15,15,13],
[10,14,6,12,11,10,13,13,0,10,13,11,11,12,9],
[13,14,14,12,20,13,14,16,15,0,18,16,14,9,15],
[10,10,4,9,15,8,10,10,12,7,0,9,8,8,6],
[11,16,11,15,14,8,9,10,14,9,16,0,10,10,9],
[11,11,9,10,15,9,9,10,14,11,17,15,0,10,10],
[11,17,8,16,17,13,12,10,13,16,17,15,15,0,10],
[13,14,10,11,13,8,14,12,16,10,19,16,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,19,14,11,15,11,17,17,14,14,18,14,13],
[7,0,9,15,11,10,11,5,11,9,9,7,12,8,6],
[10,16,0,16,12,9,10,11,6,9,12,10,13,9,6],
[6,10,9,0,12,6,12,7,9,8,11,8,8,10,7],
[11,14,13,13,0,13,14,9,12,13,11,10,15,9,13],
[14,15,16,19,12,0,16,12,12,15,15,12,16,15,13],
[10,14,15,13,11,9,0,8,14,10,12,11,11,13,10],
[14,20,14,18,16,13,17,0,12,15,15,14,15,17,14],
[8,14,19,16,13,13,11,13,0,9,13,10,12,14,9],
[8,16,16,17,12,10,15,10,16,0,14,13,17,16,15],
[11,16,13,14,14,10,13,10,12,11,0,12,12,12,9],
[11,18,15,17,15,13,14,11,15,12,13,0,15,13,13],
[7,13,12,17,10,9,14,10,13,8,13,10,0,12,12],
[11,17,16,15,16,10,12,8,11,9,13,12,13,0,10],
[12,19,19,18,12,12,15,11,16,10,16,12,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,14,11,9,13,7,9,7,12,7,11,11,12],
[14,0,10,15,14,15,18,10,12,8,14,15,12,13,14],
[16,15,0,17,17,16,14,12,12,10,17,8,14,11,13],
[11,10,8,0,9,5,12,7,8,9,9,7,9,11,10],
[14,11,8,16,0,14,11,8,11,11,11,8,8,7,10],
[16,10,9,20,11,0,12,13,12,10,14,12,12,10,11],
[12,7,11,13,14,13,0,7,13,10,12,13,9,4,8],
[18,15,13,18,17,12,18,0,14,12,13,8,10,15,16],
[16,13,13,17,14,13,12,11,0,6,12,9,9,9,11],
[18,17,15,16,14,15,15,13,19,0,16,13,9,12,13],
[13,11,8,16,14,11,13,12,13,9,0,10,9,10,12],
[18,10,17,18,17,13,12,17,16,12,15,0,15,11,16],
[14,13,11,16,17,13,16,15,16,16,16,10,0,7,12],
[14,12,14,14,18,15,21,10,16,13,15,14,18,0,16],
[13,11,12,15,15,14,17,9,14,12,13,9,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,12,15,10,12,15,9,10,13,9,12,13,13],
[14,0,11,13,15,12,12,15,11,10,15,12,14,13,15],
[14,14,0,19,15,14,15,17,13,13,12,14,13,15,11],
[13,12,6,0,13,7,12,12,9,7,13,9,12,10,12],
[10,10,10,12,0,10,12,15,10,10,15,12,13,12,13],
[15,13,11,18,15,0,14,15,15,13,17,15,18,12,14],
[13,13,10,13,13,11,0,12,9,11,12,13,9,11,13],
[10,10,8,13,10,10,13,0,12,9,9,12,11,11,10],
[16,14,12,16,15,10,16,13,0,9,14,14,12,10,13],
[15,15,12,18,15,12,14,16,16,0,16,13,14,16,16],
[12,10,13,12,10,8,13,16,11,9,0,13,7,11,13],
[16,13,11,16,13,10,12,13,11,12,12,0,13,15,15],
[13,11,12,13,12,7,16,14,13,11,18,12,0,13,14],
[12,12,10,15,13,13,14,14,15,9,14,10,12,0,13],
[12,10,14,13,12,11,12,15,12,9,12,10,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,8,14,11,18,11,16,18,15,19,16,14,12,17],
[8,0,11,11,5,8,11,11,11,13,9,5,15,8,9],
[17,14,0,9,14,13,15,8,17,11,15,11,15,13,14],
[11,14,16,0,11,11,17,11,16,11,13,14,13,14,15],
[14,20,11,14,0,15,15,14,17,17,11,10,14,13,15],
[7,17,12,14,10,0,14,14,10,12,12,16,12,6,9],
[14,14,10,8,10,11,0,9,12,11,13,10,14,11,13],
[9,14,17,14,11,11,16,0,17,19,11,10,14,8,13],
[7,14,8,9,8,15,13,8,0,13,13,12,5,7,17],
[10,12,14,14,8,13,14,6,12,0,9,12,10,8,14],
[6,16,10,12,14,13,12,14,12,16,0,15,11,6,15],
[9,20,14,11,15,9,15,15,13,13,10,0,15,10,10],
[11,10,10,12,11,13,11,11,20,15,14,10,0,10,14],
[13,17,12,11,12,19,14,17,18,17,19,15,15,0,18],
[8,16,11,10,10,16,12,12,8,11,10,15,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,6,7,12,10,9,9,10,12,16,11,15,8],
[16,0,19,12,9,11,16,12,13,13,17,15,14,16,9],
[12,6,0,5,7,8,8,7,11,11,11,11,9,12,6],
[19,13,20,0,11,12,14,11,17,16,16,17,16,17,11],
[18,16,18,14,0,11,13,12,14,18,18,17,20,18,13],
[13,14,17,13,14,0,17,11,15,15,16,15,17,16,12],
[15,9,17,11,12,8,0,8,9,10,9,11,9,12,8],
[16,13,18,14,13,14,17,0,15,16,17,12,15,15,12],
[16,12,14,8,11,10,16,10,0,18,16,14,14,17,10],
[15,12,14,9,7,10,15,9,7,0,13,12,10,10,5],
[13,8,14,9,7,9,16,8,9,12,0,12,12,10,7],
[9,10,14,8,8,10,14,13,11,13,13,0,16,14,7],
[14,11,16,9,5,8,16,10,11,15,13,9,0,13,5],
[10,9,13,8,7,9,13,10,8,15,15,11,12,0,6],
[17,16,19,14,12,13,17,13,15,20,18,18,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,6,19,14,12,12,13,10,13,9,13,12,8,13],
[13,0,13,14,15,14,13,18,12,13,12,16,14,15,16],
[19,12,0,18,13,12,13,17,11,10,8,15,14,12,10],
[6,11,7,0,10,11,12,15,11,9,9,14,8,7,10],
[11,10,12,15,0,11,10,11,12,9,8,11,6,7,11],
[13,11,13,14,14,0,11,13,13,14,12,15,10,12,15],
[13,12,12,13,15,14,0,15,14,14,15,15,14,13,15],
[12,7,8,10,14,12,10,0,12,11,10,13,11,8,11],
[15,13,14,14,13,12,11,13,0,11,12,15,10,14,15],
[12,12,15,16,16,11,11,14,14,0,9,11,10,10,12],
[16,13,17,16,17,13,10,15,13,16,0,15,10,14,12],
[12,9,10,11,14,10,10,12,10,14,10,0,8,10,11],
[13,11,11,17,19,15,11,14,15,15,15,17,0,11,17],
[17,10,13,18,18,13,12,17,11,15,11,15,14,0,14],
[12,9,15,15,14,10,10,14,10,13,13,14,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,12,7,14,8,9,12,14,8,12,9,7,11,13],
[19,0,17,17,17,12,13,17,17,15,17,20,15,17,17],
[13,8,0,12,17,11,9,13,14,13,16,12,6,17,17],
[18,8,13,0,17,13,13,13,14,9,11,16,14,15,16],
[11,8,8,8,0,11,12,16,15,6,11,9,8,10,14],
[17,13,14,12,14,0,15,13,14,12,12,11,11,12,14],
[16,12,16,12,13,10,0,17,14,13,16,17,14,14,17],
[13,8,12,12,9,12,8,0,15,14,13,12,9,12,13],
[11,8,11,11,10,11,11,10,0,10,11,12,6,13,15],
[17,10,12,16,19,13,12,11,15,0,16,14,10,14,17],
[13,8,9,14,14,13,9,12,14,9,0,11,11,12,13],
[16,5,13,9,16,14,8,13,13,11,14,0,7,13,11],
[18,10,19,11,17,14,11,16,19,15,14,18,0,19,17],
[14,8,8,10,15,13,11,13,12,11,13,12,6,0,16],
[12,8,8,9,11,11,8,12,10,8,12,14,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,14,9,14,10,12,12,14,13,7,12,10,11],
[17,0,13,12,9,12,8,10,9,14,15,12,9,9,9],
[13,12,0,9,14,12,11,12,13,14,13,9,13,10,12],
[11,13,16,0,12,13,12,13,14,15,16,14,13,11,14],
[16,16,11,13,0,14,15,11,13,16,14,13,10,14,9],
[11,13,13,12,11,0,10,13,14,13,14,12,12,9,13],
[15,17,14,13,10,15,0,11,11,16,19,11,12,13,14],
[13,15,13,12,14,12,14,0,11,15,15,11,10,10,12],
[13,16,12,11,12,11,14,14,0,14,16,15,12,12,14],
[11,11,11,10,9,12,9,10,11,0,11,8,8,9,11],
[12,10,12,9,11,11,6,10,9,14,0,8,12,9,13],
[18,13,16,11,12,13,14,14,10,17,17,0,11,11,12],
[13,16,12,12,15,13,13,15,13,17,13,14,0,13,13],
[15,16,15,14,11,16,12,15,13,16,16,14,12,0,16],
[14,16,13,11,16,12,11,13,11,14,12,13,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,8,8,6,8,11,7,10,4,9,10,6,6],
[11,0,10,6,11,5,8,12,14,8,7,5,10,10,8],
[15,15,0,9,12,14,15,15,15,13,10,13,16,15,11],
[17,19,16,0,14,18,18,18,19,21,13,18,18,14,9],
[17,14,13,11,0,9,15,23,17,16,11,11,13,11,16],
[19,20,11,7,16,0,12,18,18,14,10,13,15,14,8],
[17,17,10,7,10,13,0,18,19,14,8,14,15,13,9],
[14,13,10,7,2,7,7,0,12,10,9,10,11,8,6],
[18,11,10,6,8,7,6,13,0,11,7,10,12,5,4],
[15,17,12,4,9,11,11,15,14,0,6,14,14,10,8],
[21,18,15,12,14,15,17,16,18,19,0,14,17,16,8],
[16,20,12,7,14,12,11,15,15,11,11,0,12,13,11],
[15,15,9,7,12,10,10,14,13,11,8,13,0,11,6],
[19,15,10,11,14,11,12,17,20,15,9,12,14,0,8],
[19,17,14,16,9,17,16,19,21,17,17,14,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,13,14,9,12,10,11,14,14,18,17,12],
[14,0,12,15,11,13,9,9,11,11,14,15,15,16,13],
[13,13,0,11,14,8,10,10,11,14,12,13,16,13,10],
[12,10,14,0,9,11,8,8,10,11,14,13,12,15,14],
[12,14,11,16,0,15,11,8,5,14,13,11,12,13,9],
[11,12,17,14,10,0,11,11,10,11,13,14,13,14,15],
[16,16,15,17,14,14,0,16,11,17,19,17,19,17,14],
[13,16,15,17,17,14,9,0,11,18,17,20,17,20,15],
[15,14,14,15,20,15,14,14,0,14,15,21,19,19,12],
[14,14,11,14,11,14,8,7,11,0,10,12,14,15,11],
[11,11,13,11,12,12,6,8,10,15,0,13,11,13,9],
[11,10,12,12,14,11,8,5,4,13,12,0,10,17,11],
[7,10,9,13,13,12,6,8,6,11,14,15,0,13,10],
[8,9,12,10,12,11,8,5,6,10,12,8,12,0,10],
[13,12,15,11,16,10,11,10,13,14,16,14,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,11,10,9,11,11,10,12,13,10,9,10,13],
[15,0,17,20,16,10,14,18,13,17,18,16,14,15,16],
[15,8,0,15,12,12,10,16,12,12,16,16,13,11,15],
[14,5,10,0,8,6,11,12,7,12,11,11,11,12,11],
[15,9,13,17,0,13,16,16,12,16,16,16,14,12,16],
[16,15,13,19,12,0,14,17,15,14,17,18,15,15,17],
[14,11,15,14,9,11,0,16,14,12,12,15,17,13,12],
[14,7,9,13,9,8,9,0,9,8,10,13,13,8,10],
[15,12,13,18,13,10,11,16,0,14,15,13,12,11,9],
[13,8,13,13,9,11,13,17,11,0,13,13,11,17,13],
[12,7,9,14,9,8,13,15,10,12,0,13,11,13,10],
[15,9,9,14,9,7,10,12,12,12,12,0,7,11,13],
[16,11,12,14,11,10,8,12,13,14,14,18,0,14,8],
[15,10,14,13,13,10,12,17,14,8,12,14,11,0,9],
[12,9,10,14,9,8,13,15,16,12,15,12,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,5,7,7,21,9,12,21,9,5,25,12,7,25],
[13,0,9,13,20,20,18,4,20,13,0,18,20,13,13],
[20,16,0,20,20,16,20,11,20,13,16,20,20,20,20],
[18,12,5,0,7,21,18,16,25,18,5,25,21,7,18],
[18,5,5,18,0,21,18,9,18,18,5,18,21,0,18],
[4,5,9,4,4,0,9,4,9,13,5,9,16,4,4],
[16,7,5,7,7,16,0,7,16,9,0,25,7,7,16],
[13,21,14,9,16,21,18,0,21,9,14,25,21,16,18],
[4,5,5,0,7,16,9,4,0,9,5,18,12,0,13],
[16,12,12,7,7,12,16,16,16,0,12,16,12,7,16],
[20,25,9,20,20,20,25,11,20,13,0,25,25,20,20],
[0,7,5,0,7,16,0,0,7,9,0,0,7,7,9],
[13,5,5,4,4,9,18,4,13,13,0,18,0,4,13],
[18,12,5,18,25,21,18,9,25,18,5,18,21,0,18],
[0,12,5,7,7,21,9,7,12,9,5,16,12,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,10,10,20,19,12,8,20,13,10,23,12,12],
[6,0,10,2,10,4,5,5,7,11,15,2,11,1,4],
[10,15,0,11,11,11,14,7,9,14,15,11,19,11,7],
[15,23,14,0,13,19,19,13,17,16,18,11,18,4,12],
[15,15,14,12,0,16,17,12,12,15,9,11,13,12,16],
[5,21,14,6,9,0,9,8,10,19,15,7,18,8,7],
[6,20,11,6,8,16,0,5,12,19,14,6,14,8,4],
[13,20,18,12,13,17,20,0,14,19,18,11,16,13,13],
[17,18,16,8,13,15,13,11,0,14,10,13,22,11,15],
[5,14,11,9,10,6,6,6,11,0,17,6,11,5,6],
[12,10,10,7,16,10,11,7,15,8,0,6,16,7,10],
[15,23,14,14,14,18,19,14,12,19,19,0,19,9,18],
[2,14,6,7,12,7,11,9,3,14,9,6,0,9,9],
[13,24,14,21,13,17,17,12,14,20,18,16,16,0,11],
[13,21,18,13,9,18,21,12,10,19,15,7,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,14,8,0,8,14,13,14,9,8,15,13,9],
[17,0,18,20,9,11,19,20,19,21,15,18,21,15,14],
[17,7,0,16,11,17,21,17,21,17,17,19,21,15,16],
[11,5,9,0,5,5,9,11,5,11,10,13,15,9,5],
[17,16,14,20,0,12,14,16,25,20,10,13,21,15,14],
[25,14,8,20,13,0,19,24,25,20,15,13,16,19,14],
[17,6,4,16,11,6,0,16,11,12,10,15,15,10,16],
[11,5,8,14,9,1,9,0,14,16,10,8,16,10,9],
[12,6,4,20,0,0,14,11,0,7,10,13,16,5,5],
[11,4,8,14,5,5,13,9,18,0,10,13,15,15,14],
[16,10,8,15,15,10,15,15,15,15,0,14,19,14,15],
[17,7,6,12,12,12,10,17,12,12,11,0,12,6,11],
[10,4,4,10,4,9,10,9,9,10,6,13,0,10,5],
[12,10,10,16,10,6,15,15,20,10,11,19,15,0,11],
[16,11,9,20,11,11,9,16,20,11,10,14,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,19,13,13,9,14,14,12,15,14,13,15,10],
[14,0,15,18,15,9,11,17,15,7,18,18,13,14,13],
[13,10,0,14,8,10,7,13,13,9,14,16,12,12,15],
[6,7,11,0,8,5,3,11,10,7,12,11,9,13,9],
[12,10,17,17,0,17,11,12,17,12,17,19,17,13,11],
[12,16,15,20,8,0,13,13,17,12,19,18,14,15,13],
[16,14,18,22,14,12,0,16,14,17,18,16,16,21,16],
[11,8,12,14,13,12,9,0,12,9,15,15,13,14,8],
[11,10,12,15,8,8,11,13,0,9,17,16,11,16,11],
[13,18,16,18,13,13,8,16,16,0,18,16,14,19,15],
[10,7,11,13,8,6,7,10,8,7,0,13,9,9,6],
[11,7,9,14,6,7,9,10,9,9,12,0,8,8,7],
[12,12,13,16,8,11,9,12,14,11,16,17,0,13,8],
[10,11,13,12,12,10,4,11,9,6,16,17,12,0,12],
[15,12,10,16,14,12,9,17,14,10,19,18,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,18,8,11,14,6,13,9,14,17,11,14,11],
[14,0,15,19,12,12,14,6,10,8,14,17,9,19,18],
[10,10,0,20,11,16,13,10,9,9,9,16,11,15,15],
[7,6,5,0,11,9,9,6,5,5,8,9,9,8,7],
[17,13,14,14,0,15,16,6,7,11,14,13,12,12,17],
[14,13,9,16,10,0,13,9,13,13,10,13,10,15,13],
[11,11,12,16,9,12,0,10,11,10,8,12,5,13,12],
[19,19,15,19,19,16,15,0,13,13,12,16,9,18,18],
[12,15,16,20,18,12,14,12,0,14,15,21,17,20,13],
[16,17,16,20,14,12,15,12,11,0,16,15,11,17,18],
[11,11,16,17,11,15,17,13,10,9,0,18,13,15,14],
[8,8,9,16,12,12,13,9,4,10,7,0,16,10,8],
[14,16,14,16,13,15,20,16,8,14,12,9,0,14,13],
[11,6,10,17,13,10,12,7,5,8,10,15,11,0,14],
[14,7,10,18,8,12,13,7,12,7,11,17,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,5,12,15,9,5,5,8,10,13,5,6],
[20,0,12,13,11,13,13,11,13,16,13,13,25,7,8],
[19,13,0,15,14,19,11,16,14,6,7,18,15,6,12],
[18,12,10,0,13,18,10,11,13,10,11,17,13,6,6],
[20,14,11,12,0,17,11,4,8,12,12,12,15,6,6],
[13,12,6,7,8,0,11,11,13,6,7,18,14,7,6],
[10,12,14,15,14,14,0,12,13,6,15,14,14,9,9],
[16,14,9,14,21,14,13,0,15,13,9,20,20,8,7],
[20,12,11,12,17,12,12,10,0,10,13,12,25,1,7],
[20,9,19,15,13,19,19,12,15,0,20,20,16,14,14],
[17,12,18,14,13,18,10,16,12,5,0,22,18,13,19],
[15,12,7,8,13,7,11,5,13,5,3,0,15,6,11],
[12,0,10,12,10,11,11,5,0,9,7,10,0,1,6],
[20,18,19,19,19,18,16,17,24,11,12,19,24,0,20],
[19,17,13,19,19,19,16,18,18,11,6,14,19,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,10,6,8,4,12,16,13,11,11,12,8,10],
[17,0,11,18,10,14,13,19,18,17,16,18,14,15,10],
[22,14,0,18,14,19,11,14,19,19,21,15,21,18,16],
[15,7,7,0,8,11,5,13,10,14,12,9,13,12,7],
[19,15,11,17,0,12,14,16,16,17,16,15,15,17,12],
[17,11,6,14,13,0,12,13,15,15,16,16,11,13,12],
[21,12,14,20,11,13,0,18,19,18,19,16,12,18,13],
[13,6,11,12,9,12,7,0,13,13,12,14,12,15,12],
[9,7,6,15,9,10,6,12,0,9,13,16,14,10,13],
[12,8,6,11,8,10,7,12,16,0,9,13,14,8,10],
[14,9,4,13,9,9,6,13,12,16,0,12,13,10,8],
[14,7,10,16,10,9,9,11,9,12,13,0,8,11,11],
[13,11,4,12,10,14,13,13,11,11,12,17,0,12,10],
[17,10,7,13,8,12,7,10,15,17,15,14,13,0,15],
[15,15,9,18,13,13,12,13,12,15,17,14,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,12,13,15,9,14,14,12,12,15,19,12,16],
[12,0,18,14,8,25,11,12,9,19,12,18,17,17,14],
[10,7,0,15,14,18,8,8,10,20,11,19,11,12,12],
[13,11,10,0,11,12,9,13,9,14,12,13,13,12,14],
[12,17,11,14,0,23,11,16,12,19,10,20,15,15,16],
[10,0,7,13,2,0,9,11,3,11,6,8,12,8,11],
[16,14,17,16,14,16,0,13,10,17,11,21,18,13,18],
[11,13,17,12,9,14,12,0,13,16,12,20,14,13,16],
[11,16,15,16,13,22,15,12,0,20,16,18,15,12,15],
[13,6,5,11,6,14,8,9,5,0,6,7,13,4,12],
[13,13,14,13,15,19,14,13,9,19,0,15,15,14,11],
[10,7,6,12,5,17,4,5,7,18,10,0,16,10,14],
[6,8,14,12,10,13,7,11,10,12,10,9,0,10,5],
[13,8,13,13,10,17,12,12,13,21,11,15,15,0,15],
[9,11,13,11,9,14,7,9,10,13,14,11,20,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,11,16,9,14,18,15,11,11,14,18,15,14],
[15,0,16,12,14,9,16,17,10,10,13,15,19,13,16],
[14,9,0,10,16,10,15,18,11,11,15,14,15,14,17],
[14,13,15,0,17,7,19,18,11,14,14,16,18,16,17],
[9,11,9,8,0,7,10,13,10,10,10,13,13,11,18],
[16,16,15,18,18,0,21,22,10,17,17,17,23,18,19],
[11,9,10,6,15,4,0,15,9,10,8,12,13,14,16],
[7,8,7,7,12,3,10,0,10,10,7,9,16,10,10],
[10,15,14,14,15,15,16,15,0,17,14,14,19,18,19],
[14,15,14,11,15,8,15,15,8,0,12,12,15,13,16],
[14,12,10,11,15,8,17,18,11,13,0,13,13,14,16],
[11,10,11,9,12,8,13,16,11,13,12,0,15,11,14],
[7,6,10,7,12,2,12,9,6,10,12,10,0,14,15],
[10,12,11,9,14,7,11,15,7,12,11,14,11,0,14],
[11,9,8,8,7,6,9,15,6,9,9,11,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,9,12,12,13,15,12,11,15,10,9,10,14],
[15,0,15,14,16,18,17,12,10,17,15,11,10,17,15],
[13,10,0,9,13,14,13,12,12,14,17,11,11,15,16],
[16,11,16,0,16,16,15,13,13,16,16,16,10,18,15],
[13,9,12,9,0,15,15,14,12,11,16,12,8,16,14],
[13,7,11,9,10,0,9,13,7,10,15,11,8,15,12],
[12,8,12,10,10,16,0,11,9,15,15,13,10,15,13],
[10,13,13,12,11,12,14,0,10,12,16,14,12,13,14],
[13,15,13,12,13,18,16,15,0,15,17,13,16,14,13],
[14,8,11,9,14,15,10,13,10,0,15,11,8,16,11],
[10,10,8,9,9,10,10,9,8,10,0,11,8,13,8],
[15,14,14,9,13,14,12,11,12,14,14,0,12,13,13],
[16,15,14,15,17,17,15,13,9,17,17,13,0,18,13],
[15,8,10,7,9,10,10,12,11,9,12,12,7,0,11],
[11,10,9,10,11,13,12,11,12,14,17,12,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,9,13,11,10,14,10,10,13,15,10,9,9],
[14,0,15,13,15,17,8,15,11,14,11,17,11,13,13],
[9,10,0,15,13,10,14,15,13,13,10,19,9,13,9],
[16,12,10,0,14,14,16,17,15,17,10,16,14,16,13],
[12,10,12,11,0,11,12,13,15,8,9,12,10,15,10],
[14,8,15,11,14,0,11,17,10,14,11,15,12,14,11],
[15,17,11,9,13,14,0,18,18,9,7,18,14,10,12],
[11,10,10,8,12,8,7,0,13,8,6,11,15,10,11],
[15,14,12,10,10,15,7,12,0,13,9,15,7,10,12],
[15,11,12,8,17,11,16,17,12,0,12,16,13,16,9],
[12,14,15,15,16,14,18,19,16,13,0,19,15,15,12],
[10,8,6,9,13,10,7,14,10,9,6,0,9,9,7],
[15,14,16,11,15,13,11,10,18,12,10,16,0,11,13],
[16,12,12,9,10,11,15,15,15,9,10,16,14,0,10],
[16,12,16,12,15,14,13,14,13,16,13,18,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,13,12,6,16,12,16,17,17,11,14,7,8],
[15,0,13,12,14,16,15,11,15,14,17,10,13,9,8],
[10,12,0,11,15,11,12,9,13,17,20,14,13,9,12],
[12,13,14,0,13,10,12,9,15,12,15,13,14,13,8],
[13,11,10,12,0,10,11,11,9,7,12,12,11,8,8],
[19,9,14,15,15,0,14,10,13,14,14,10,15,5,6],
[9,10,13,13,14,11,0,13,12,14,16,11,11,10,11],
[13,14,16,16,14,15,12,0,16,13,17,16,13,12,10],
[9,10,12,10,16,12,13,9,0,8,15,13,11,12,9],
[8,11,8,13,18,11,11,12,17,0,18,7,14,9,10],
[8,8,5,10,13,11,9,8,10,7,0,8,12,9,9],
[14,15,11,12,13,15,14,9,12,18,17,0,13,10,14],
[11,12,12,11,14,10,14,12,14,11,13,12,0,11,9],
[18,16,16,12,17,20,15,13,13,16,16,15,14,0,13],
[17,17,13,17,17,19,14,15,16,15,16,11,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,14,14,17,10,13,12,12,12,12,12,9,11],
[14,0,14,15,17,16,12,14,12,10,12,10,10,13,15],
[13,11,0,13,15,15,13,16,14,14,13,14,12,13,12],
[11,10,12,0,11,13,10,7,7,10,11,9,9,8,8],
[11,8,10,14,0,17,7,10,7,13,12,9,12,8,13],
[8,9,10,12,8,0,7,9,7,13,10,7,11,5,9],
[15,13,12,15,18,18,0,13,11,12,16,11,13,13,16],
[12,11,9,18,15,16,12,0,11,12,16,9,13,13,15],
[13,13,11,18,18,18,14,14,0,16,17,9,14,14,15],
[13,15,11,15,12,12,13,13,9,0,17,12,10,14,15],
[13,13,12,14,13,15,9,9,8,8,0,10,6,10,12],
[13,15,11,16,16,18,14,16,16,13,15,0,16,15,15],
[13,15,13,16,13,14,12,12,11,15,19,9,0,12,16],
[16,12,12,17,17,20,12,12,11,11,15,10,13,0,17],
[14,10,13,17,12,16,9,10,10,10,13,10,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,14,12,10,13,14,11,13,9,15,15,10,16],
[14,0,11,13,13,13,17,14,12,12,12,13,12,13,14],
[16,14,0,14,12,12,16,18,8,17,12,17,17,14,18],
[11,12,11,0,11,10,16,15,11,11,10,14,10,12,14],
[13,12,13,14,0,13,13,16,11,14,15,17,16,14,19],
[15,12,13,15,12,0,14,16,10,16,9,16,15,13,18],
[12,8,9,9,12,11,0,15,10,13,10,13,11,10,13],
[11,11,7,10,9,9,10,0,10,14,10,14,12,8,13],
[14,13,17,14,14,15,15,15,0,18,13,17,17,12,18],
[12,13,8,14,11,9,12,11,7,0,7,12,14,11,15],
[16,13,13,15,10,16,15,15,12,18,0,17,16,15,14],
[10,12,8,11,8,9,12,11,8,13,8,0,13,6,11],
[10,13,8,15,9,10,14,13,8,11,9,12,0,11,14],
[15,12,11,13,11,12,15,17,13,14,10,19,14,0,16],
[9,11,7,11,6,7,12,12,7,10,11,14,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,8,7,13,8,7,10,7,11,13,8,9,10],
[18,0,14,11,13,13,14,12,14,14,12,15,16,15,12],
[17,11,0,10,13,14,12,9,10,13,13,15,11,13,11],
[17,14,15,0,15,14,15,13,15,14,11,15,12,12,12],
[18,12,12,10,0,16,13,12,15,15,11,14,13,15,11],
[12,12,11,11,9,0,10,8,10,11,9,10,7,8,8],
[17,11,13,10,12,15,0,11,10,12,13,15,9,13,11],
[18,13,16,12,13,17,14,0,15,15,15,14,15,16,13],
[15,11,15,10,10,15,15,10,0,14,14,13,11,10,10],
[18,11,12,11,10,14,13,10,11,0,11,17,13,11,11],
[14,13,12,14,14,16,12,10,11,14,0,15,11,13,12],
[12,10,10,10,11,15,10,11,12,8,10,0,10,11,9],
[17,9,14,13,12,18,16,10,14,12,14,15,0,11,12],
[16,10,12,13,10,17,12,9,15,14,12,14,14,0,12],
[15,13,14,13,14,17,14,12,15,14,13,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,10,7,9,13,10,12,9,15,7,10,12,8],
[18,0,17,16,13,18,16,18,17,14,17,16,19,16,11],
[15,8,0,10,13,10,13,13,15,13,16,6,10,14,6],
[15,9,15,0,9,15,15,14,13,9,16,12,12,11,14],
[18,12,12,16,0,13,12,15,16,16,17,13,13,16,14],
[16,7,15,10,12,0,15,14,17,9,19,11,16,13,11],
[12,9,12,10,13,10,0,14,15,11,13,7,10,12,8],
[15,7,12,11,10,11,11,0,14,12,14,9,14,12,11],
[13,8,10,12,9,8,10,11,0,8,9,11,8,10,10],
[16,11,12,16,9,16,14,13,17,0,19,15,13,17,12],
[10,8,9,9,8,6,12,11,16,6,0,10,13,13,10],
[18,9,19,13,12,14,18,16,14,10,15,0,14,13,10],
[15,6,15,13,12,9,15,11,17,12,12,11,0,13,13],
[13,9,11,14,9,12,13,13,15,8,12,12,12,0,10],
[17,14,19,11,11,14,17,14,15,13,15,15,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,15,13,7,14,15,13,6,7,12,10,11,13],
[15,0,16,17,15,14,15,17,14,13,10,17,14,15,15],
[11,9,0,14,11,9,13,12,10,10,7,10,11,8,9],
[10,8,11,0,9,10,13,12,11,7,9,12,10,10,11],
[12,10,14,16,0,9,14,16,12,11,13,15,14,15,15],
[18,11,16,15,16,0,17,20,15,14,11,18,14,15,14],
[11,10,12,12,11,8,0,12,11,9,9,5,9,11,11],
[10,8,13,13,9,5,13,0,11,7,10,8,12,8,11],
[12,11,15,14,13,10,14,14,0,9,11,11,9,10,13],
[19,12,15,18,14,11,16,18,16,0,11,15,13,15,14],
[18,15,18,16,12,14,16,15,14,14,0,15,15,15,16],
[13,8,15,13,10,7,20,17,14,10,10,0,14,10,14],
[15,11,14,15,11,11,16,13,16,12,10,11,0,13,10],
[14,10,17,15,10,10,14,17,15,10,10,15,12,0,16],
[12,10,16,14,10,11,14,14,12,11,9,11,15,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,9,13,16,9,21,13,14,11,14,10,13,16],
[14,0,19,6,15,12,11,19,14,9,7,14,15,9,12],
[17,6,0,9,11,13,9,20,14,14,9,15,13,11,15],
[16,19,16,0,20,18,15,21,16,20,11,16,17,14,19],
[12,10,14,5,0,14,9,14,17,8,7,9,13,9,11],
[9,13,12,7,11,0,13,14,9,9,7,13,8,10,7],
[16,14,16,10,16,12,0,19,16,14,7,19,9,9,11],
[4,6,5,4,11,11,6,0,9,7,9,14,6,10,14],
[12,11,11,9,8,16,9,16,0,11,7,15,9,11,13],
[11,16,11,5,17,16,11,18,14,0,9,12,13,14,15],
[14,18,16,14,18,18,18,16,18,16,0,18,15,15,12],
[11,11,10,9,16,12,6,11,10,13,7,0,11,9,13],
[15,10,12,8,12,17,16,19,16,12,10,14,0,11,19],
[12,16,14,11,16,15,16,15,14,11,10,16,14,0,14],
[9,13,10,6,14,18,14,11,12,10,13,12,6,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,25,12,13,17,5,7,2,8,7,14,18,11,13],
[15,0,20,14,13,12,14,7,2,8,12,9,13,8,8],
[0,5,0,12,6,0,0,0,0,1,5,0,10,6,0],
[13,11,13,0,13,12,6,8,8,3,7,13,13,6,8],
[12,12,19,12,0,12,12,2,2,6,5,7,12,11,7],
[8,13,25,13,13,0,8,6,1,6,12,13,11,11,6],
[20,11,25,19,13,17,0,12,8,13,17,14,13,13,13],
[18,18,25,17,23,19,13,0,1,11,12,12,25,18,18],
[23,23,25,17,23,24,17,24,0,11,17,17,25,23,23],
[17,17,24,22,19,19,12,14,14,0,17,17,24,12,19],
[18,13,20,18,20,13,8,13,8,8,0,13,13,11,13],
[11,16,25,12,18,12,11,13,8,8,12,0,18,11,8],
[7,12,15,12,13,14,12,0,0,1,12,7,0,1,8],
[14,17,19,19,14,14,12,7,2,13,14,14,24,0,19],
[12,17,25,17,18,19,12,7,2,6,12,17,17,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,10,7,9,15,11,8,6,14,7,6,11,11,13],
[19,0,16,15,13,16,13,17,9,18,13,11,18,16,17],
[15,9,0,12,9,13,8,10,5,13,10,9,9,15,12],
[18,10,13,0,11,18,14,9,10,17,10,12,15,17,17],
[16,12,16,14,0,19,16,14,10,18,14,14,13,21,14],
[10,9,12,7,6,0,13,9,6,15,11,9,8,15,12],
[14,12,17,11,9,12,0,11,11,14,9,10,11,13,11],
[17,8,15,16,11,16,14,0,10,20,8,11,14,16,16],
[19,16,20,15,15,19,14,15,0,20,16,13,12,16,16],
[11,7,12,8,7,10,11,5,5,0,8,8,7,11,9],
[18,12,15,15,11,14,16,17,9,17,0,12,13,16,14],
[19,14,16,13,11,16,15,14,12,17,13,0,13,19,15],
[14,7,16,10,12,17,14,11,13,18,12,12,0,20,20],
[14,9,10,8,4,10,12,9,9,14,9,6,5,0,11],
[12,8,13,8,11,13,14,9,9,16,11,10,5,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,13,16,12,12,13,18,14,14,15,15,13,10],
[15,0,11,12,18,14,15,16,14,14,14,16,11,10,11],
[12,14,0,13,16,15,14,15,17,17,14,17,14,15,15],
[12,13,12,0,19,15,16,18,13,16,15,16,12,13,14],
[9,7,9,6,0,11,8,14,10,9,10,13,5,9,10],
[13,11,10,10,14,0,14,15,13,13,12,14,12,10,10],
[13,10,11,9,17,11,0,10,10,13,11,16,10,9,9],
[12,9,10,7,11,10,15,0,12,10,14,15,8,11,8],
[7,11,8,12,15,12,15,13,0,13,13,15,8,10,10],
[11,11,8,9,16,12,12,15,12,0,12,15,10,12,11],
[11,11,11,10,15,13,14,11,12,13,0,14,13,11,11],
[10,9,8,9,12,11,9,10,10,10,11,0,9,11,9],
[10,14,11,13,20,13,15,17,17,15,12,16,0,11,13],
[12,15,10,12,16,15,16,14,15,13,14,14,14,0,13],
[15,14,10,11,15,15,16,17,15,14,14,16,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,12,11,10,15,12,10,10,11,14,10,13,8],
[14,0,11,13,13,11,15,11,13,10,8,10,11,12,11],
[15,14,0,16,13,15,11,11,11,10,11,11,13,11,11],
[13,12,9,0,11,14,12,10,12,9,10,10,14,10,10],
[14,12,12,14,0,11,11,10,12,10,9,11,13,10,8],
[15,14,10,11,14,0,11,11,16,10,11,12,14,14,9],
[10,10,14,13,14,14,0,15,13,10,13,10,12,14,11],
[13,14,14,15,15,14,10,0,10,14,10,11,14,12,10],
[15,12,14,13,13,9,12,15,0,11,9,11,12,15,10],
[15,15,15,16,15,15,15,11,14,0,15,15,16,14,13],
[14,17,14,15,16,14,12,15,16,10,0,15,15,14,11],
[11,15,14,15,14,13,15,14,14,10,10,0,14,14,11],
[15,14,12,11,12,11,13,11,13,9,10,11,0,13,11],
[12,13,14,15,15,11,11,13,10,11,11,11,12,0,14],
[17,14,14,15,17,16,14,15,15,12,14,14,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,13,8,12,10,15,12,21,11,16,13,13,9],
[7,0,10,11,8,10,8,13,13,19,8,11,12,11,9],
[12,15,0,15,13,15,17,18,17,15,12,17,16,19,13],
[12,14,10,0,13,12,14,16,16,20,14,11,16,12,13],
[17,17,12,12,0,10,19,18,17,21,13,13,17,13,16],
[13,15,10,13,15,0,15,12,14,16,13,13,18,10,10],
[15,17,8,11,6,10,0,17,13,16,8,12,16,15,8],
[10,12,7,9,7,13,8,0,11,12,5,14,13,12,8],
[13,12,8,9,8,11,12,14,0,17,10,11,12,12,7],
[4,6,10,5,4,9,9,13,8,0,6,7,11,12,6],
[14,17,13,11,12,12,17,20,15,19,0,15,18,13,15],
[9,14,8,14,12,12,13,11,14,18,10,0,18,14,12],
[12,13,9,9,8,7,9,12,13,14,7,7,0,9,10],
[12,14,6,13,12,15,10,13,13,13,12,11,16,0,14],
[16,16,12,12,9,15,17,17,18,19,10,13,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([15, 25, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_15_25.csv", index=False, header=False)