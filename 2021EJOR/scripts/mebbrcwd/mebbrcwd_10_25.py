
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,10,7,6,8,8,10,12,13,11],
[15,0,11,14,14,11,11,15,18,13],
[18,14,0,11,13,10,14,16,19,11],
[19,11,14,0,15,16,16,16,16,16],
[17,11,12,10,0,14,10,16,17,15],
[17,14,15,9,11,0,12,12,16,12],
[15,14,11,9,15,13,0,15,17,12],
[13,10,9,9,9,13,10,0,12,8],
[12,7,6,9,8,9,8,13,0,9],
[14,12,14,9,10,13,13,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,25,11,25,17,17,25,19,25],
[8,0,17,11,25,14,17,14,11,11],
[0,8,0,3,22,6,6,22,8,11],
[14,14,22,0,22,14,14,22,8,25],
[0,0,3,3,0,0,3,8,3,3],
[8,11,19,11,25,0,9,19,11,11],
[8,8,19,11,22,16,0,16,11,11],
[0,11,3,3,17,6,9,0,11,11],
[6,14,17,17,22,14,14,14,0,17],
[0,14,14,0,22,14,14,14,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,7,13,9,19,16,9,9],
[11,0,17,8,13,11,16,18,14,4],
[12,8,0,4,5,9,14,17,10,8],
[18,17,21,0,21,17,23,23,18,12],
[12,12,20,4,0,9,20,17,15,10],
[16,14,16,8,16,0,19,17,12,15],
[6,9,11,2,5,6,0,11,4,4],
[9,7,8,2,8,8,14,0,4,7],
[16,11,15,7,10,13,21,21,0,6],
[16,21,17,13,15,10,21,18,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,17,9,18,15,16,8,10],
[13,0,20,22,14,20,11,20,14,14],
[11,5,0,18,14,16,9,13,11,11],
[8,3,7,0,11,8,6,11,8,14],
[16,11,11,14,0,12,12,14,14,16],
[7,5,9,17,13,0,13,13,10,11],
[10,14,16,19,13,12,0,17,12,11],
[9,5,12,14,11,12,8,0,10,8],
[17,11,14,17,11,15,13,15,0,9],
[15,11,14,11,9,14,14,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,11,11,8,11,9,11,11],
[15,0,14,12,14,11,9,10,13,11],
[14,11,0,9,9,12,8,9,12,10],
[14,13,16,0,13,14,12,10,11,14],
[14,11,16,12,0,12,11,9,11,9],
[17,14,13,11,13,0,14,10,8,12],
[14,16,17,13,14,11,0,10,14,11],
[16,15,16,15,16,15,15,0,12,12],
[14,12,13,14,14,17,11,13,0,13],
[14,14,15,11,16,13,14,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,19,10,12,11,7,14,13],
[13,0,12,18,9,9,13,14,9,10],
[10,13,0,17,11,10,11,12,13,10],
[6,7,8,0,8,5,9,10,7,11],
[15,16,14,17,0,9,15,12,8,10],
[13,16,15,20,16,0,15,15,16,12],
[14,12,14,16,10,10,0,14,12,12],
[18,11,13,15,13,10,11,0,10,12],
[11,16,12,18,17,9,13,15,0,11],
[12,15,15,14,15,13,13,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,18,16,8,16,11,7,15,13],
[17,0,18,19,11,17,13,13,17,16],
[7,7,0,10,6,17,11,5,10,8],
[9,6,15,0,10,14,12,9,14,8],
[17,14,19,15,0,21,19,11,18,12],
[9,8,8,11,4,0,10,7,10,8],
[14,12,14,13,6,15,0,12,18,9],
[18,12,20,16,14,18,13,0,16,12],
[10,8,15,11,7,15,7,9,0,7],
[12,9,17,17,13,17,16,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,15,12,14,15,13,16,14],
[12,0,15,15,9,15,14,13,17,14],
[14,10,0,13,15,12,13,11,19,10],
[10,10,12,0,11,12,12,10,17,15],
[13,16,10,14,0,15,17,10,18,13],
[11,10,13,13,10,0,9,14,14,12],
[10,11,12,13,8,16,0,10,17,10],
[12,12,14,15,15,11,15,0,16,12],
[9,8,6,8,7,11,8,9,0,9],
[11,11,15,10,12,13,15,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,11,13,7,8,7,13,12],
[14,0,19,12,9,19,20,7,19,19],
[9,6,0,13,15,14,15,2,20,7],
[14,13,12,0,20,12,8,7,7,12],
[12,16,10,5,0,10,13,5,10,10],
[18,6,11,13,15,0,15,13,8,13],
[17,5,10,17,12,10,0,5,5,10],
[18,18,23,18,20,12,20,0,18,23],
[12,6,5,18,15,17,20,7,0,10],
[13,6,18,13,15,12,15,2,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,11,13,9,10,6,11,6],
[14,0,12,11,17,14,16,13,15,12],
[12,13,0,9,15,10,10,10,13,5],
[14,14,16,0,17,16,17,10,22,9],
[12,8,10,8,0,9,8,11,16,10],
[16,11,15,9,16,0,11,11,15,13],
[15,9,15,8,17,14,0,13,16,14],
[19,12,15,15,14,14,12,0,20,12],
[14,10,12,3,9,10,9,5,0,4],
[19,13,20,16,15,12,11,13,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,25,13,25,23,25,12,13,25],
[23,0,25,23,25,23,25,12,25,25],
[0,0,0,0,25,12,13,12,2,2],
[12,2,25,0,25,23,25,12,25,25],
[0,0,0,0,0,0,11,0,0,0],
[2,2,13,2,25,0,13,14,13,2],
[0,0,12,0,14,12,0,12,2,14],
[13,13,13,13,25,11,13,0,13,13],
[12,0,23,0,25,12,23,12,0,14],
[0,0,23,0,25,23,11,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,14,16,13,12,13,12,8],
[8,0,12,10,13,13,10,8,11,8],
[10,13,0,11,12,13,7,8,10,10],
[11,15,14,0,16,12,13,14,13,10],
[9,12,13,9,0,11,11,8,9,11],
[12,12,12,13,14,0,12,11,11,11],
[13,15,18,12,14,13,0,11,13,11],
[12,17,17,11,17,14,14,0,12,14],
[13,14,15,12,16,14,12,13,0,13],
[17,17,15,15,14,14,14,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,14,12,14,11,11,13,18],
[10,0,13,9,15,15,10,9,5,15],
[8,12,0,10,12,12,11,12,9,18],
[11,16,15,0,14,18,14,16,9,19],
[13,10,13,11,0,16,12,9,7,13],
[11,10,13,7,9,0,13,12,8,15],
[14,15,14,11,13,12,0,16,10,18],
[14,16,13,9,16,13,9,0,8,17],
[12,20,16,16,18,17,15,17,0,21],
[7,10,7,6,12,10,7,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,12,14,13,14,10,13,19,13],
[5,0,6,13,7,15,8,7,10,11],
[13,19,0,14,7,14,10,13,19,18],
[11,12,11,0,7,10,4,11,15,12],
[12,18,18,18,0,12,9,16,17,17],
[11,10,11,15,13,0,3,9,17,11],
[15,17,15,21,16,22,0,11,16,18],
[12,18,12,14,9,16,14,0,18,23],
[6,15,6,10,8,8,9,7,0,12],
[12,14,7,13,8,14,7,2,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,10,17,11,11,16,10,16],
[14,0,15,11,14,13,14,13,13,16],
[11,10,0,12,10,11,12,16,16,16],
[15,14,13,0,12,8,11,16,11,16],
[8,11,15,13,0,10,11,20,14,13],
[14,12,14,17,15,0,9,14,16,18],
[14,11,13,14,14,16,0,14,18,15],
[9,12,9,9,5,11,11,0,13,13],
[15,12,9,14,11,9,7,12,0,14],
[9,9,9,9,12,7,10,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,17,16,14,17,15,12],
[12,0,10,11,12,12,10,19,12,11],
[12,15,0,13,18,12,15,18,17,13],
[13,14,12,0,14,10,13,15,15,13],
[8,13,7,11,0,10,9,11,13,10],
[9,13,13,15,15,0,13,12,15,14],
[11,15,10,12,16,12,0,14,14,17],
[8,6,7,10,14,13,11,0,10,9],
[10,13,8,10,12,10,11,15,0,10],
[13,14,12,12,15,11,8,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,5,9,8,7,7,8,13,12],
[12,0,11,9,7,13,10,11,14,9],
[20,14,0,21,9,22,12,15,17,18],
[16,16,4,0,6,15,11,14,8,17],
[17,18,16,19,0,18,11,16,17,17],
[18,12,3,10,7,0,11,8,8,15],
[18,15,13,14,14,14,0,9,14,15],
[17,14,10,11,9,17,16,0,8,17],
[12,11,8,17,8,17,11,17,0,12],
[13,16,7,8,8,10,10,8,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,19,10,13,12,8,11,14,12],
[15,0,12,9,9,15,16,12,11,13],
[6,13,0,4,12,6,4,14,5,4],
[15,16,21,0,19,15,19,17,9,14],
[12,16,13,6,0,16,13,14,6,13],
[13,10,19,10,9,0,15,11,6,10],
[17,9,21,6,12,10,0,14,9,10],
[14,13,11,8,11,14,11,0,10,8],
[11,14,20,16,19,19,16,15,0,11],
[13,12,21,11,12,15,15,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,10,18,12,18,11,14,12],
[14,0,16,13,16,10,18,16,14,22],
[11,9,0,16,21,17,16,7,16,16],
[15,12,9,0,10,7,11,11,15,15],
[7,9,4,15,0,16,17,9,14,11],
[13,15,8,18,9,0,11,10,13,14],
[7,7,9,14,8,14,0,5,8,16],
[14,9,18,14,16,15,20,0,14,19],
[11,11,9,10,11,12,17,11,0,15],
[13,3,9,10,14,11,9,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,20,10,15,18,14,12,14,13],
[16,0,16,10,9,13,13,12,16,17],
[5,9,0,7,6,5,4,0,9,4],
[15,15,18,0,15,15,10,13,12,13],
[10,16,19,10,0,18,16,12,16,17],
[7,12,20,10,7,0,14,6,17,16],
[11,12,21,15,9,11,0,8,17,16],
[13,13,25,12,13,19,17,0,16,17],
[11,9,16,13,9,8,8,9,0,13],
[12,8,21,12,8,9,9,8,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,14,11,11,12,12,11,14],
[8,0,10,9,12,8,8,9,11,12],
[13,15,0,13,9,9,10,10,12,12],
[11,16,12,0,11,10,12,11,12,14],
[14,13,16,14,0,11,10,12,13,15],
[14,17,16,15,14,0,12,13,16,15],
[13,17,15,13,15,13,0,12,15,15],
[13,16,15,14,13,12,13,0,13,17],
[14,14,13,13,12,9,10,12,0,16],
[11,13,13,11,10,10,10,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,12,8,12,13,9,10,6],
[12,0,13,10,11,14,10,9,10,9],
[17,12,0,12,11,13,10,12,9,10],
[13,15,13,0,12,16,14,16,16,11],
[17,14,14,13,0,13,16,16,11,13],
[13,11,12,9,12,0,14,13,12,8],
[12,15,15,11,9,11,0,13,10,10],
[16,16,13,9,9,12,12,0,10,9],
[15,15,16,9,14,13,15,15,0,10],
[19,16,15,14,12,17,15,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,21,15,15,16,12,15,17,20],
[15,0,16,17,10,12,14,18,19,22],
[4,9,0,16,10,14,9,17,19,18],
[10,8,9,0,14,12,16,16,19,17],
[10,15,15,11,0,22,13,12,25,17],
[9,13,11,13,3,0,13,7,12,15],
[13,11,16,9,12,12,0,16,15,18],
[10,7,8,9,13,18,9,0,19,17],
[8,6,6,6,0,13,10,6,0,10],
[5,3,7,8,8,10,7,8,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,15,12,12,15,13,13,15],
[17,0,14,12,14,12,14,12,13,14],
[11,11,0,13,13,12,18,16,16,14],
[10,13,12,0,11,10,12,12,9,14],
[13,11,12,14,0,16,14,14,13,14],
[13,13,13,15,9,0,16,12,16,20],
[10,11,7,13,11,9,0,15,16,15],
[12,13,9,13,11,13,10,0,15,12],
[12,12,9,16,12,9,9,10,0,15],
[10,11,11,11,11,5,10,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,8,11,10,10,12,11,16],
[10,0,19,14,19,13,17,10,16,18],
[9,6,0,10,10,12,8,11,17,14],
[17,11,15,0,19,19,18,15,14,20],
[14,6,15,6,0,7,8,10,10,14],
[15,12,13,6,18,0,12,11,14,13],
[15,8,17,7,17,13,0,13,16,13],
[13,15,14,10,15,14,12,0,15,12],
[14,9,8,11,15,11,9,10,0,10],
[9,7,11,5,11,12,12,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,24,24,15,14,15,11,10],
[3,0,14,23,24,16,15,8,11,11],
[4,11,0,19,20,11,2,4,11,11],
[1,2,6,0,23,16,7,2,3,10],
[1,1,5,2,0,9,1,2,2,9],
[10,9,14,9,16,0,14,10,11,9],
[11,10,23,18,24,11,0,11,11,11],
[10,17,21,23,23,15,14,0,18,18],
[14,14,14,22,23,14,14,7,0,8],
[15,14,14,15,16,16,14,7,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,16,13,13,14,13,17,12],
[6,0,16,11,13,11,11,12,12,11],
[8,9,0,7,7,6,11,10,11,8],
[9,14,18,0,13,9,8,13,11,10],
[12,12,18,12,0,15,14,20,14,15],
[12,14,19,16,10,0,14,11,14,8],
[11,14,14,17,11,11,0,12,15,9],
[12,13,15,12,5,14,13,0,15,13],
[8,13,14,14,11,11,10,10,0,7],
[13,14,17,15,10,17,16,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,9,2,12,7,6,6,15],
[17,0,13,8,13,16,9,14,18,13],
[18,12,0,20,12,12,12,12,12,15],
[16,17,5,0,7,10,7,6,10,19],
[23,12,13,18,0,17,18,20,17,18],
[13,9,13,15,8,0,9,14,9,19],
[18,16,13,18,7,16,0,8,12,14],
[19,11,13,19,5,11,17,0,11,19],
[19,7,13,15,8,16,13,14,0,20],
[10,12,10,6,7,6,11,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,14,12,8,12,11,13,13],
[11,0,12,8,7,9,11,10,10,11],
[11,13,0,11,10,11,11,10,11,14],
[11,17,14,0,12,11,14,16,12,14],
[13,18,15,13,0,12,14,10,14,16],
[17,16,14,14,13,0,15,11,13,17],
[13,14,14,11,11,10,0,10,10,13],
[14,15,15,9,15,14,15,0,12,14],
[12,15,14,13,11,12,15,13,0,14],
[12,14,11,11,9,8,12,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,14,11,15,15,14,16,12],
[13,0,12,16,11,14,16,14,15,12],
[13,13,0,13,13,15,18,17,15,12],
[11,9,12,0,8,14,12,12,13,10],
[14,14,12,17,0,13,13,14,15,15],
[10,11,10,11,12,0,15,12,16,7],
[10,9,7,13,12,10,0,14,15,10],
[11,11,8,13,11,13,11,0,15,10],
[9,10,10,12,10,9,10,10,0,7],
[13,13,13,15,10,18,15,15,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,12,15,18,16,13,16,14],
[14,0,10,16,20,17,17,12,14,13],
[9,15,0,13,15,16,16,13,12,15],
[13,9,12,0,18,19,14,15,11,14],
[10,5,10,7,0,15,9,13,7,11],
[7,8,9,6,10,0,15,12,14,11],
[9,8,9,11,16,10,0,10,13,7],
[12,13,12,10,12,13,15,0,15,13],
[9,11,13,14,18,11,12,10,0,11],
[11,12,10,11,14,14,18,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,12,8,5,20,13,17,16],
[8,0,7,3,5,3,14,8,7,6],
[8,18,0,18,14,12,18,18,15,10],
[13,22,7,0,6,7,14,16,8,7],
[17,20,11,19,0,6,17,16,11,10],
[20,22,13,18,19,0,20,18,19,12],
[5,11,7,11,8,5,0,12,13,8],
[12,17,7,9,9,7,13,0,10,6],
[8,18,10,17,14,6,12,15,0,5],
[9,19,15,18,15,13,17,19,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,11,3,10,13,20,14,10],
[16,0,16,16,16,12,22,22,16,16],
[18,9,0,12,0,15,6,21,15,12],
[14,9,13,0,3,16,9,20,18,16],
[22,9,25,22,0,21,15,25,25,25],
[15,13,10,9,4,0,10,15,15,15],
[12,3,19,16,10,15,0,19,19,15],
[5,3,4,5,0,10,6,0,8,12],
[11,9,10,7,0,10,6,17,0,7],
[15,9,13,9,0,10,10,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,19,9,6,14,15,10,13],
[12,0,19,20,17,11,22,21,15,12],
[10,6,0,13,11,11,12,13,8,11],
[6,5,12,0,7,6,12,9,5,3],
[16,8,14,18,0,9,20,17,11,17],
[19,14,14,19,16,0,21,16,10,16],
[11,3,13,13,5,4,0,12,4,8],
[10,4,12,16,8,9,13,0,6,10],
[15,10,17,20,14,15,21,19,0,22],
[12,13,14,22,8,9,17,15,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,13,15,11,10,12,14],
[14,0,11,11,12,11,12,14,12,14],
[11,14,0,10,14,13,15,14,16,13],
[14,14,15,0,12,11,13,13,11,12],
[12,13,11,13,0,11,12,10,10,10],
[10,14,12,14,14,0,9,12,10,14],
[14,13,10,12,13,16,0,14,12,13],
[15,11,11,12,15,13,11,0,13,12],
[13,13,9,14,15,15,13,12,0,15],
[11,11,12,13,15,11,12,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,12,0,10,6,14,12,13,13],
[19,0,6,12,6,8,8,8,15,11],
[13,19,0,13,12,19,15,6,13,17],
[25,13,12,0,10,6,21,12,15,17],
[15,19,13,15,0,19,15,15,15,7],
[19,17,6,19,6,0,15,12,19,11],
[11,17,10,4,10,10,0,10,11,11],
[13,17,19,13,10,13,15,0,13,17],
[12,10,12,10,10,6,14,12,0,10],
[12,14,8,8,18,14,14,8,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,20,10,15,14,19,11,16],
[8,0,10,12,10,9,9,17,9,7],
[9,15,0,19,12,13,13,18,12,12],
[5,13,6,0,11,12,9,16,10,10],
[15,15,13,14,0,13,14,19,12,14],
[10,16,12,13,12,0,13,19,14,10],
[11,16,12,16,11,12,0,15,10,13],
[6,8,7,9,6,6,10,0,8,7],
[14,16,13,15,13,11,15,17,0,16],
[9,18,13,15,11,15,12,18,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,18,12,13,7,13,20,7,12],
[16,0,16,11,14,4,12,13,8,16],
[7,9,0,7,15,8,15,9,9,8],
[13,14,18,0,15,12,14,14,10,13],
[12,11,10,10,0,11,18,14,14,11],
[18,21,17,13,14,0,16,15,8,19],
[12,13,10,11,7,9,0,7,6,6],
[5,12,16,11,11,10,18,0,7,11],
[18,17,16,15,11,17,19,18,0,16],
[13,9,17,12,14,6,19,14,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,11,12,13,17,10,17,11],
[15,0,16,11,14,15,15,13,19,14],
[11,9,0,11,13,12,14,17,17,15],
[14,14,14,0,12,11,19,16,18,15],
[13,11,12,13,0,14,15,10,16,13],
[12,10,13,14,11,0,16,13,18,15],
[8,10,11,6,10,9,0,9,17,12],
[15,12,8,9,15,12,16,0,16,12],
[8,6,8,7,9,7,8,9,0,11],
[14,11,10,10,12,10,13,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,11,12,11,13,10,11,12],
[15,0,17,15,16,14,13,17,15,12],
[8,8,0,13,11,8,12,11,13,10],
[14,10,12,0,11,10,10,14,12,12],
[13,9,14,14,0,15,10,10,13,13],
[14,11,17,15,10,0,10,10,13,13],
[12,12,13,15,15,15,0,13,13,14],
[15,8,14,11,15,15,12,0,11,16],
[14,10,12,13,12,12,12,14,0,10],
[13,13,15,13,12,12,11,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,7,10,21,15,16,12,11,15],
[10,0,13,10,18,8,15,10,10,9],
[18,12,0,15,18,16,17,12,8,18],
[15,15,10,0,21,18,19,15,14,14],
[4,7,7,4,0,8,16,0,4,7],
[10,17,9,7,17,0,19,10,7,10],
[9,10,8,6,9,6,0,6,1,9],
[13,15,13,10,25,15,19,0,7,15],
[14,15,17,11,21,18,24,18,0,18],
[10,16,7,11,18,15,16,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,10,8,11,13,15,15,12],
[11,0,16,9,10,9,14,14,18,13],
[7,9,0,5,4,5,9,6,8,5],
[15,16,20,0,15,10,15,17,18,17],
[17,15,21,10,0,14,17,15,12,12],
[14,16,20,15,11,0,19,19,17,16],
[12,11,16,10,8,6,0,15,11,8],
[10,11,19,8,10,6,10,0,13,10],
[10,7,17,7,13,8,14,12,0,12],
[13,12,20,8,13,9,17,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,14,3,5,6,14,6,11],
[20,0,13,15,12,14,11,15,11,15],
[15,12,0,13,8,12,9,16,8,13],
[11,10,12,0,7,10,7,10,5,9],
[22,13,17,18,0,12,14,12,12,13],
[20,11,13,15,13,0,10,14,11,14],
[19,14,16,18,11,15,0,15,15,13],
[11,10,9,15,13,11,10,0,11,11],
[19,14,17,20,13,14,10,14,0,13],
[14,10,12,16,12,11,12,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,16,13,15,18,15,13,10],
[15,0,17,17,15,16,16,10,12,15],
[10,8,0,16,11,7,16,13,12,7],
[9,8,9,0,9,9,11,6,14,10],
[12,10,14,16,0,12,17,12,9,10],
[10,9,18,16,13,0,14,11,12,10],
[7,9,9,14,8,11,0,7,12,11],
[10,15,12,19,13,14,18,0,11,12],
[12,13,13,11,16,13,13,14,0,13],
[15,10,18,15,15,15,14,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,15,6,13,3,11,7,14],
[14,0,17,13,7,9,9,15,9,12],
[12,8,0,11,7,8,5,12,6,11],
[10,12,14,0,7,14,9,16,12,14],
[19,18,18,18,0,15,15,16,16,10],
[12,16,17,11,10,0,13,15,13,13],
[22,16,20,16,10,12,0,13,10,18],
[14,10,13,9,9,10,12,0,9,7],
[18,16,19,13,9,12,15,16,0,15],
[11,13,14,11,15,12,7,18,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,11,12,13,15,15,9,12,13],
[6,0,9,12,9,12,12,6,11,11],
[14,16,0,13,10,13,13,13,15,16],
[13,13,12,0,10,10,12,10,15,15],
[12,16,15,15,0,16,15,8,15,15],
[10,13,12,15,9,0,12,13,16,12],
[10,13,12,13,10,13,0,8,14,15],
[16,19,12,15,17,12,17,0,19,14],
[13,14,10,10,10,9,11,6,0,13],
[12,14,9,10,10,13,10,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,13,15,14,11,14,17,10],
[10,0,8,13,12,8,9,10,12,10],
[12,17,0,13,13,12,12,12,13,11],
[12,12,12,0,14,10,10,17,16,13],
[10,13,12,11,0,13,8,14,12,12],
[11,17,13,15,12,0,11,17,15,12],
[14,16,13,15,17,14,0,15,15,11],
[11,15,13,8,11,8,10,0,14,10],
[8,13,12,9,13,10,10,11,0,8],
[15,15,14,12,13,13,14,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,11,16,13,13,13,13,13],
[12,0,9,14,8,15,13,7,16,16],
[14,16,0,10,11,17,15,17,18,15],
[14,11,15,0,17,15,14,12,20,23],
[9,17,14,8,0,14,12,15,17,16],
[12,10,8,10,11,0,10,15,10,13],
[12,12,10,11,13,15,0,13,10,11],
[12,18,8,13,10,10,12,0,15,16],
[12,9,7,5,8,15,15,10,0,10],
[12,9,10,2,9,12,14,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,18,23,18,9,21,21,18],
[4,0,3,1,12,3,1,1,10,12],
[5,22,0,23,15,10,3,14,13,10],
[7,24,2,0,16,3,2,7,14,12],
[2,13,10,9,0,3,10,13,2,11],
[7,22,15,22,22,0,13,13,14,23],
[16,24,22,23,15,12,0,24,12,15],
[4,24,11,18,12,12,1,0,10,12],
[4,15,12,11,23,11,13,15,0,11],
[7,13,15,13,14,2,10,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,14,16,15,13,19,19,13],
[13,0,12,14,14,15,14,11,14,13],
[9,13,0,7,9,5,14,10,13,7],
[11,11,18,0,16,13,13,18,17,15],
[9,11,16,9,0,9,18,11,16,14],
[10,10,20,12,16,0,14,14,19,13],
[12,11,11,12,7,11,0,12,18,8],
[6,14,15,7,14,11,13,0,14,17],
[6,11,12,8,9,6,7,11,0,9],
[12,12,18,10,11,12,17,8,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,7,7,3,15,16,7,19],
[6,0,6,7,6,6,12,13,13,6],
[10,19,0,10,7,6,19,10,10,16],
[18,18,15,0,6,18,18,12,15,15],
[18,19,18,19,0,12,18,19,19,25],
[22,19,19,7,13,0,19,16,7,22],
[10,13,6,7,7,6,0,10,7,10],
[9,12,15,13,6,9,15,0,13,12],
[18,12,15,10,6,18,18,12,0,15],
[6,19,9,10,0,3,15,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,5,8,6,11,11,8,9,13],
[11,0,9,12,12,14,11,10,11,15],
[20,16,0,12,13,12,17,11,13,15],
[17,13,13,0,13,14,13,12,10,16],
[19,13,12,12,0,17,14,12,8,19],
[14,11,13,11,8,0,12,10,11,13],
[14,14,8,12,11,13,0,10,9,16],
[17,15,14,13,13,15,15,0,12,15],
[16,14,12,15,17,14,16,13,0,17],
[12,10,10,9,6,12,9,10,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,7,11,9,14,8,15,10],
[16,0,11,14,12,11,18,16,17,16],
[14,14,0,16,13,9,16,13,14,16],
[18,11,9,0,16,13,22,15,17,14],
[14,13,12,9,0,11,15,12,13,14],
[16,14,16,12,14,0,21,14,20,15],
[11,7,9,3,10,4,0,8,16,9],
[17,9,12,10,13,11,17,0,16,16],
[10,8,11,8,12,5,9,9,0,12],
[15,9,9,11,11,10,16,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,15,18,15,8,18,15,7],
[7,0,0,0,18,15,8,10,7,0],
[10,25,0,10,25,22,18,10,7,14],
[10,25,15,0,25,22,11,18,15,7],
[7,7,0,0,0,7,8,7,7,7],
[10,10,3,3,18,0,11,10,7,7],
[17,17,7,14,17,14,0,17,14,14],
[7,15,15,7,18,15,8,0,15,7],
[10,18,18,10,18,18,11,10,0,7],
[18,25,11,18,18,18,11,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,13,22,15,12,16,14,16],
[10,0,14,8,16,12,11,11,12,15],
[8,11,0,11,16,11,12,12,9,14],
[12,17,14,0,17,15,16,12,17,13],
[3,9,9,8,0,7,6,11,6,9],
[10,13,14,10,18,0,10,12,16,15],
[13,14,13,9,19,15,0,15,17,16],
[9,14,13,13,14,13,10,0,14,13],
[11,13,16,8,19,9,8,11,0,14],
[9,10,11,12,16,10,9,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,9,11,7,9,4,13,7],
[16,0,17,12,15,13,12,8,13,16],
[19,8,0,14,14,12,12,9,14,5],
[16,13,11,0,15,11,10,13,15,16],
[14,10,11,10,0,12,10,14,9,10],
[18,12,13,14,13,0,17,13,11,7],
[16,13,13,15,15,8,0,9,10,9],
[21,17,16,12,11,12,16,0,16,14],
[12,12,11,10,16,14,15,9,0,11],
[18,9,20,9,15,18,16,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,12,12,9,14,11,10,10],
[16,0,12,11,18,9,18,12,12,13],
[14,13,0,13,11,16,18,14,11,12],
[13,14,12,0,12,9,15,10,13,10],
[13,7,14,13,0,14,19,15,12,10],
[16,16,9,16,11,0,19,11,13,11],
[11,7,7,10,6,6,0,4,7,11],
[14,13,11,15,10,14,21,0,12,13],
[15,13,14,12,13,12,18,13,0,8],
[15,12,13,15,15,14,14,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,12,9,9,9,7,10,11],
[12,0,11,13,8,9,4,6,6,8],
[16,14,0,8,7,11,6,5,6,8],
[13,12,17,0,11,9,9,8,9,9],
[16,17,18,14,0,14,14,9,13,13],
[16,16,14,16,11,0,12,7,11,14],
[16,21,19,16,11,13,0,16,14,22],
[18,19,20,17,16,18,9,0,15,12],
[15,19,19,16,12,14,11,10,0,13],
[14,17,17,16,12,11,3,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,11,13,15,12,12,12,12],
[17,0,13,12,14,18,17,16,13,14],
[18,12,0,9,14,19,12,16,14,17],
[14,13,16,0,14,18,15,15,12,16],
[12,11,11,11,0,19,11,11,10,14],
[10,7,6,7,6,0,9,6,7,7],
[13,8,13,10,14,16,0,13,13,14],
[13,9,9,10,14,19,12,0,9,19],
[13,12,11,13,15,18,12,16,0,15],
[13,11,8,9,11,18,11,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,10,15,9,13,20,13,15],
[16,0,16,16,16,13,11,21,14,15],
[10,9,0,11,13,9,10,19,14,14],
[15,9,14,0,16,10,12,21,15,11],
[10,9,12,9,0,9,7,16,12,11],
[16,12,16,15,16,0,13,20,15,17],
[12,14,15,13,18,12,0,18,16,16],
[5,4,6,4,9,5,7,0,6,8],
[12,11,11,10,13,10,9,19,0,13],
[10,10,11,14,14,8,9,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,15,17,15,8,7,23,15],
[9,0,17,8,9,7,8,15,24,8],
[8,8,0,8,9,7,8,0,16,0],
[10,17,17,0,9,8,8,8,25,0],
[8,16,16,16,0,7,8,15,16,8],
[10,18,18,17,18,0,9,9,17,9],
[17,17,17,17,17,16,0,9,25,9],
[18,10,25,17,10,16,16,0,18,8],
[2,1,9,0,9,8,0,7,0,0],
[10,17,25,25,17,16,16,17,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,13,12,7,9,6,6,3],
[15,0,11,15,18,19,19,18,20,14],
[20,14,0,20,19,11,18,14,23,6],
[12,10,5,0,17,8,17,9,13,5],
[13,7,6,8,0,10,19,13,14,10],
[18,6,14,17,15,0,11,15,18,11],
[16,6,7,8,6,14,0,6,11,5],
[19,7,11,16,12,10,19,0,20,3],
[19,5,2,12,11,7,14,5,0,3],
[22,11,19,20,15,14,20,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,13,14,13,16,12,10,15],
[10,0,12,13,13,9,9,6,8,12],
[9,13,0,14,13,11,7,9,9,11],
[12,12,11,0,9,9,9,6,6,7],
[11,12,12,16,0,8,12,7,11,11],
[12,16,14,16,17,0,12,12,11,14],
[9,16,18,16,13,13,0,14,9,12],
[13,19,16,19,18,13,11,0,15,20],
[15,17,16,19,14,14,16,10,0,16],
[10,13,14,18,14,11,13,5,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,9,12,11,13,13,13,17],
[10,0,14,11,13,11,12,12,14,13],
[11,11,0,10,8,12,10,9,13,13],
[16,14,15,0,12,15,13,13,16,16],
[13,12,17,13,0,11,13,13,19,16],
[14,14,13,10,14,0,11,11,16,14],
[12,13,15,12,12,14,0,12,17,14],
[12,13,16,12,12,14,13,0,14,15],
[12,11,12,9,6,9,8,11,0,15],
[8,12,12,9,9,11,11,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,10,8,10,8,14,13,10],
[11,0,11,12,13,11,10,15,15,10],
[14,14,0,8,9,14,11,14,14,12],
[15,13,17,0,14,12,15,16,17,14],
[17,12,16,11,0,12,14,15,16,12],
[15,14,11,13,13,0,11,16,15,11],
[17,15,14,10,11,14,0,16,15,16],
[11,10,11,9,10,9,9,0,14,8],
[12,10,11,8,9,10,10,11,0,11],
[15,15,13,11,13,14,9,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,11,9,6,6,9,10,3],
[12,0,15,12,19,14,16,10,12,14],
[14,10,0,11,14,14,4,13,13,14],
[14,13,14,0,13,17,7,9,13,7],
[16,6,11,12,0,14,7,10,15,8],
[19,11,11,8,11,0,8,10,15,14],
[19,9,21,18,18,17,0,12,13,10],
[16,15,12,16,15,15,13,0,16,11],
[15,13,12,12,10,10,12,9,0,14],
[22,11,11,18,17,11,15,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,19,20,10,19,12,15,11,16],
[10,0,9,14,8,8,10,16,10,10],
[6,16,0,11,5,14,7,16,9,12],
[5,11,14,0,3,14,7,14,9,13],
[15,17,20,22,0,18,13,17,9,15],
[6,17,11,11,7,0,9,12,4,12],
[13,15,18,18,12,16,0,18,14,11],
[10,9,9,11,8,13,7,0,11,10],
[14,15,16,16,16,21,11,14,0,19],
[9,15,13,12,10,13,14,15,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,10,17,13,9,10,14,13],
[13,0,19,14,13,15,14,13,12,15],
[10,6,0,8,12,10,9,10,11,13],
[15,11,17,0,14,10,10,14,11,13],
[8,12,13,11,0,12,10,11,8,15],
[12,10,15,15,13,0,9,12,13,13],
[16,11,16,15,15,16,0,15,16,17],
[15,12,15,11,14,13,10,0,16,13],
[11,13,14,14,17,12,9,9,0,14],
[12,10,12,12,10,12,8,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,8,8,12,10,10,11,9,8],
[13,0,9,9,14,17,13,16,15,11],
[17,16,0,11,16,18,14,17,15,13],
[17,16,14,0,17,12,12,17,18,16],
[13,11,9,8,0,10,6,11,12,5],
[15,8,7,13,15,0,9,12,17,10],
[15,12,11,13,19,16,0,15,16,12],
[14,9,8,8,14,13,10,0,10,13],
[16,10,10,7,13,8,9,15,0,10],
[17,14,12,9,20,15,13,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,18,10,8,11,12,17,10],
[6,0,13,10,3,8,8,12,6,5],
[9,12,0,7,9,8,11,9,16,11],
[7,15,18,0,8,11,10,12,11,10],
[15,22,16,17,0,9,10,13,22,16],
[17,17,17,14,16,0,15,14,15,11],
[14,17,14,15,15,10,0,14,13,13],
[13,13,16,13,12,11,11,0,14,7],
[8,19,9,14,3,10,12,11,0,12],
[15,20,14,15,9,14,12,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,12,13,15,12,15,12,14],
[9,0,18,12,14,11,14,15,15,10],
[8,7,0,10,9,7,11,12,10,5],
[13,13,15,0,8,12,15,13,12,11],
[12,11,16,17,0,11,17,18,18,12],
[10,14,18,13,14,0,15,15,14,13],
[13,11,14,10,8,10,0,14,14,9],
[10,10,13,12,7,10,11,0,12,9],
[13,10,15,13,7,11,11,13,0,11],
[11,15,20,14,13,12,16,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,9,18,11,10,16,13,13],
[14,0,11,13,17,16,9,18,12,14],
[19,14,0,11,19,12,18,20,13,13],
[16,12,14,0,23,17,18,21,19,18],
[7,8,6,2,0,10,9,11,14,8],
[14,9,13,8,15,0,15,15,10,15],
[15,16,7,7,16,10,0,17,11,13],
[9,7,5,4,14,10,8,0,8,9],
[12,13,12,6,11,15,14,17,0,14],
[12,11,12,7,17,10,12,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,13,13,16,9,15,14,13],
[9,0,13,6,12,16,11,17,12,11],
[14,12,0,7,13,11,10,7,13,11],
[12,19,18,0,12,18,11,16,16,14],
[12,13,12,13,0,15,8,11,15,14],
[9,9,14,7,10,0,13,11,10,10],
[16,14,15,14,17,12,0,16,13,16],
[10,8,18,9,14,14,9,0,16,12],
[11,13,12,9,10,15,12,9,0,11],
[12,14,14,11,11,15,9,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,4,10,10,12,10,7,6,10],
[13,0,5,8,8,10,5,6,14,9],
[21,20,0,12,25,19,23,13,14,23],
[15,17,13,0,21,17,15,11,15,15],
[15,17,0,4,0,8,8,3,9,10],
[13,15,6,8,17,0,15,2,15,8],
[15,20,2,10,17,10,0,8,16,7],
[18,19,12,14,22,23,17,0,19,14],
[19,11,11,10,16,10,9,6,0,13],
[15,16,2,10,15,17,18,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,18,15,14,16,11,16,16],
[11,0,7,11,12,7,13,10,8,11],
[11,18,0,21,13,13,21,12,16,15],
[7,14,4,0,12,11,13,7,14,10],
[10,13,12,13,0,11,20,12,15,14],
[11,18,12,14,14,0,18,13,15,16],
[9,12,4,12,5,7,0,12,8,7],
[14,15,13,18,13,12,13,0,17,12],
[9,17,9,11,10,10,17,8,0,14],
[9,14,10,15,11,9,18,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,14,13,15,15,14,15,15],
[13,0,11,11,9,16,13,9,12,13],
[12,14,0,15,8,16,16,10,10,16],
[11,14,10,0,12,11,16,14,11,11],
[12,16,17,13,0,17,17,14,15,17],
[10,9,9,14,8,0,13,11,12,11],
[10,12,9,9,8,12,0,10,11,10],
[11,16,15,11,11,14,15,0,10,16],
[10,13,15,14,10,13,14,15,0,14],
[10,12,9,14,8,14,15,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,20,11,11,7,11,16,16,11],
[25,0,20,11,11,7,20,16,16,11],
[5,5,0,0,0,5,0,5,16,2],
[14,14,25,0,16,5,14,14,25,16],
[14,14,25,9,0,5,18,14,16,11],
[18,18,20,20,20,0,18,14,25,11],
[14,5,25,11,7,7,0,16,16,16],
[9,9,20,11,11,11,9,0,16,11],
[9,9,9,0,9,0,9,9,0,11],
[14,14,23,9,14,14,9,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,14,11,16,13,12,10,10],
[14,0,16,13,12,16,13,16,13,13],
[13,9,0,12,11,13,11,14,9,10],
[11,12,13,0,12,10,13,14,11,10],
[14,13,14,13,0,17,12,16,15,11],
[9,9,12,15,8,0,11,12,12,9],
[12,12,14,12,13,14,0,17,14,10],
[13,9,11,11,9,13,8,0,12,7],
[15,12,16,14,10,13,11,13,0,12],
[15,12,15,15,14,16,15,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,18,18,17,13,18,21,18],
[13,0,10,16,14,14,16,17,13,16],
[10,15,0,12,12,15,14,15,13,12],
[7,9,13,0,7,8,11,13,14,12],
[7,11,13,18,0,14,17,14,18,13],
[8,11,10,17,11,0,15,19,14,17],
[12,9,11,14,8,10,0,16,19,15],
[7,8,10,12,11,6,9,0,15,17],
[4,12,12,11,7,11,6,10,0,13],
[7,9,13,13,12,8,10,8,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,14,16,10,20,14,14,14],
[8,0,13,13,12,14,9,6,14,10],
[8,12,0,11,16,17,12,9,13,16],
[11,12,14,0,16,14,15,7,15,13],
[9,13,9,9,0,17,12,10,14,15],
[15,11,8,11,8,0,13,9,13,9],
[5,16,13,10,13,12,0,9,15,11],
[11,19,16,18,15,16,16,0,16,16],
[11,11,12,10,11,12,10,9,0,14],
[11,15,9,12,10,16,14,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,10,10,14,12,16,18,15],
[16,0,10,13,11,16,16,15,18,13],
[15,15,0,10,12,18,13,14,14,10],
[15,12,15,0,19,16,15,15,20,15],
[15,14,13,6,0,13,14,13,18,13],
[11,9,7,9,12,0,9,13,16,12],
[13,9,12,10,11,16,0,14,18,14],
[9,10,11,10,12,12,11,0,12,9],
[7,7,11,5,7,9,7,13,0,9],
[10,12,15,10,12,13,11,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,13,15,15,13,9,15,10],
[8,0,9,11,11,11,9,9,11,10],
[12,16,0,10,12,10,11,10,10,10],
[12,14,15,0,12,12,16,13,14,11],
[10,14,13,13,0,12,15,8,12,8],
[10,14,15,13,13,0,13,10,14,11],
[12,16,14,9,10,12,0,10,13,10],
[16,16,15,12,17,15,15,0,13,16],
[10,14,15,11,13,11,12,12,0,12],
[15,15,15,14,17,14,15,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,12,7,6,12,10,16,12],
[12,0,11,12,14,12,12,9,9,9],
[14,14,0,15,8,14,15,15,21,17],
[13,13,10,0,7,15,16,10,16,14],
[18,11,17,18,0,14,9,15,15,11],
[19,13,11,10,11,0,16,14,16,18],
[13,13,10,9,16,9,0,9,9,12],
[15,16,10,15,10,11,16,0,11,14],
[9,16,4,9,10,9,16,14,0,15],
[13,16,8,11,14,7,13,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,17,13,11,15,14,15,18],
[12,0,10,17,14,11,15,14,16,16],
[16,15,0,18,16,12,15,14,17,18],
[8,8,7,0,11,8,12,9,12,12],
[12,11,9,14,0,12,12,13,15,15],
[14,14,13,17,13,0,12,15,11,16],
[10,10,10,13,13,13,0,13,15,14],
[11,11,11,16,12,10,12,0,16,14],
[10,9,8,13,10,14,10,9,0,12],
[7,9,7,13,10,9,11,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,13,12,7,12,6,8,8],
[12,0,10,13,9,8,7,10,12,9],
[10,15,0,11,15,8,11,6,8,10],
[12,12,14,0,8,9,7,7,6,14],
[13,16,10,17,0,9,12,10,10,11],
[18,17,17,16,16,0,12,13,16,16],
[13,18,14,18,13,13,0,12,9,12],
[19,15,19,18,15,12,13,0,13,15],
[17,13,17,19,15,9,16,12,0,14],
[17,16,15,11,14,9,13,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,9,14,10,10,13,14,12],
[10,0,7,8,13,9,7,7,14,11],
[13,18,0,10,17,14,11,13,15,15],
[16,17,15,0,16,14,14,12,14,15],
[11,12,8,9,0,10,8,8,11,11],
[15,16,11,11,15,0,12,10,12,14],
[15,18,14,11,17,13,0,9,13,14],
[12,18,12,13,17,15,16,0,14,11],
[11,11,10,11,14,13,12,11,0,11],
[13,14,10,10,14,11,11,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,10,14,12,15,9,14,12],
[10,0,13,16,16,16,18,16,15,15],
[8,12,0,10,9,9,10,10,6,7],
[15,9,15,0,16,13,17,12,14,14],
[11,9,16,9,0,9,14,10,11,7],
[13,9,16,12,16,0,19,18,16,13],
[10,7,15,8,11,6,0,9,10,6],
[16,9,15,13,15,7,16,0,11,15],
[11,10,19,11,14,9,15,14,0,9],
[13,10,18,11,18,12,19,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,18,12,13,16,13,18,14],
[13,0,16,20,25,10,19,13,25,15],
[14,9,0,11,18,6,18,11,15,20],
[7,5,14,0,18,8,13,15,14,16],
[13,0,7,7,0,7,12,10,16,11],
[12,15,19,17,18,0,18,15,18,19],
[9,6,7,12,13,7,0,10,12,10],
[12,12,14,10,15,10,15,0,19,15],
[7,0,10,11,9,7,13,6,0,9],
[11,10,5,9,14,6,15,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,9,13,7,5,8,11,16],
[20,0,12,11,17,11,10,12,20,20],
[15,13,0,14,17,12,12,11,17,18],
[16,14,11,0,15,13,14,10,19,16],
[12,8,8,10,0,7,7,7,16,10],
[18,14,13,12,18,0,12,13,17,19],
[20,15,13,11,18,13,0,13,19,18],
[17,13,14,15,18,12,12,0,17,17],
[14,5,8,6,9,8,6,8,0,14],
[9,5,7,9,15,6,7,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,12,14,12,11,12,13,14],
[15,0,12,16,15,11,12,13,15,14],
[14,13,0,10,16,12,12,11,12,12],
[13,9,15,0,18,12,11,12,13,13],
[11,10,9,7,0,10,10,11,10,12],
[13,14,13,13,15,0,14,12,16,16],
[14,13,13,14,15,11,0,13,13,13],
[13,12,14,13,14,13,12,0,14,15],
[12,10,13,12,15,9,12,11,0,12],
[11,11,13,12,13,9,12,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,14,14,19,17,16,14,12],
[9,0,12,12,9,13,17,10,12,9],
[10,13,0,11,15,19,11,18,14,15],
[11,13,14,0,14,17,15,14,12,11],
[11,16,10,11,0,14,13,13,14,9],
[6,12,6,8,11,0,10,12,11,6],
[8,8,14,10,12,15,0,13,13,11],
[9,15,7,11,12,13,12,0,14,13],
[11,13,11,13,11,14,12,11,0,12],
[13,16,10,14,16,19,14,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,4,10,11,11,9,13,13],
[16,0,11,12,13,15,15,13,12,14],
[18,14,0,14,17,15,15,16,13,12],
[21,13,11,0,16,13,16,15,12,13],
[15,12,8,9,0,10,15,14,12,11],
[14,10,10,12,15,0,15,12,10,16],
[14,10,10,9,10,10,0,12,13,13],
[16,12,9,10,11,13,13,0,15,13],
[12,13,12,13,13,15,12,10,0,17],
[12,11,13,12,14,9,12,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,14,10,9,10,11,10],
[14,0,9,11,12,14,11,9,9,11],
[13,16,0,14,11,14,14,14,12,11],
[12,14,11,0,13,11,14,11,12,15],
[11,13,14,12,0,12,12,14,13,9],
[15,11,11,14,13,0,12,9,13,14],
[16,14,11,11,13,13,0,14,10,12],
[15,16,11,14,11,16,11,0,10,11],
[14,16,13,13,12,12,15,15,0,14],
[15,14,14,10,16,11,13,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,13,12,14,13,11,13,6],
[15,0,8,15,18,13,15,16,12,13],
[15,17,0,17,17,17,15,16,15,10],
[12,10,8,0,12,11,11,16,13,9],
[13,7,8,13,0,14,12,12,11,8],
[11,12,8,14,11,0,11,13,12,8],
[12,10,10,14,13,14,0,15,13,10],
[14,9,9,9,13,12,10,0,12,7],
[12,13,10,12,14,13,12,13,0,11],
[19,12,15,16,17,17,15,18,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,16,17,13,11,10,16,12],
[15,0,15,17,15,17,16,15,12,12],
[10,10,0,10,11,14,11,12,12,10],
[9,8,15,0,13,9,13,11,11,11],
[8,10,14,12,0,12,11,11,10,9],
[12,8,11,16,13,0,10,10,12,7],
[14,9,14,12,14,15,0,11,10,16],
[15,10,13,14,14,15,14,0,12,10],
[9,13,13,14,15,13,15,13,0,11],
[13,13,15,14,16,18,9,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,12,13,11,10,14,12,16],
[14,0,13,9,13,14,14,14,10,13],
[15,12,0,10,12,14,12,14,9,17],
[13,16,15,0,11,15,16,16,11,16],
[12,12,13,14,0,11,14,15,13,12],
[14,11,11,10,14,0,12,13,11,14],
[15,11,13,9,11,13,0,13,12,15],
[11,11,11,9,10,12,12,0,10,14],
[13,15,16,14,12,14,13,15,0,19],
[9,12,8,9,13,11,10,11,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,13,11,15,15,12,14,15],
[12,0,14,12,10,14,12,12,12,15],
[8,11,0,12,14,15,12,11,15,13],
[12,13,13,0,12,17,11,13,13,15],
[14,15,11,13,0,17,12,9,14,15],
[10,11,10,8,8,0,6,9,14,12],
[10,13,13,14,13,19,0,11,14,14],
[13,13,14,12,16,16,14,0,11,13],
[11,13,10,12,11,11,11,14,0,11],
[10,10,12,10,10,13,11,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,21,7,8,14,8,12,11,9],
[13,0,13,11,10,11,5,9,15,9],
[4,12,0,7,7,11,10,11,10,7],
[18,14,18,0,12,11,8,17,10,9],
[17,15,18,13,0,6,9,9,8,6],
[11,14,14,14,19,0,14,14,12,6],
[17,20,15,17,16,11,0,11,10,4],
[13,16,14,8,16,11,14,0,10,9],
[14,10,15,15,17,13,15,15,0,14],
[16,16,18,16,19,19,21,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,9,19,12,15,11,7,11],
[11,0,10,13,18,12,18,14,11,6],
[9,15,0,9,14,13,14,8,11,9],
[16,12,16,0,17,18,18,17,14,13],
[6,7,11,8,0,12,15,11,10,7],
[13,13,12,7,13,0,16,11,9,12],
[10,7,11,7,10,9,0,11,7,7],
[14,11,17,8,14,14,14,0,9,13],
[18,14,14,11,15,16,18,16,0,15],
[14,19,16,12,18,13,18,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,15,17,18,21,12,18,23],
[12,0,16,13,15,11,21,15,16,15],
[8,9,0,8,10,13,14,12,13,13],
[10,12,17,0,9,12,15,14,12,13],
[8,10,15,16,0,14,25,12,10,17],
[7,14,12,13,11,0,19,12,13,15],
[4,4,11,10,0,6,0,8,5,14],
[13,10,13,11,13,13,17,0,21,14],
[7,9,12,13,15,12,20,4,0,13],
[2,10,12,12,8,10,11,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,14,13,13,10,12,16,14],
[11,0,7,7,10,8,8,10,10,8],
[16,18,0,13,14,14,14,15,16,11],
[11,18,12,0,10,7,9,15,13,11],
[12,15,11,15,0,9,13,14,15,13],
[12,17,11,18,16,0,9,13,17,14],
[15,17,11,16,12,16,0,15,15,15],
[13,15,10,10,11,12,10,0,15,15],
[9,15,9,12,10,8,10,10,0,11],
[11,17,14,14,12,11,10,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,14,11,11,15,13,15,12],
[11,0,16,16,10,15,13,14,15,13],
[8,9,0,8,7,10,9,5,10,8],
[11,9,17,0,10,10,11,9,11,14],
[14,15,18,15,0,14,12,13,16,17],
[14,10,15,15,11,0,13,12,12,15],
[10,12,16,14,13,12,0,14,10,14],
[12,11,20,16,12,13,11,0,17,16],
[10,10,15,14,9,13,15,8,0,13],
[13,12,17,11,8,10,11,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,11,0,6,11,10,11,13],
[20,0,20,20,10,20,20,24,19,18],
[15,5,0,16,5,10,6,13,9,18],
[14,5,9,0,10,9,14,13,13,18],
[25,15,20,15,0,11,16,15,15,13],
[19,5,15,16,14,0,10,9,10,18],
[14,5,19,11,9,15,0,14,14,13],
[15,1,12,12,10,16,11,0,6,14],
[14,6,16,12,10,15,11,19,0,14],
[12,7,7,7,12,7,12,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,13,15,13,15,9,16],
[15,0,10,12,12,15,16,16,11,15],
[15,15,0,13,15,18,14,17,12,14],
[15,13,12,0,16,13,17,17,13,14],
[12,13,10,9,0,10,12,15,10,16],
[10,10,7,12,15,0,14,10,10,13],
[12,9,11,8,13,11,0,13,16,16],
[10,9,8,8,10,15,12,0,10,12],
[16,14,13,12,15,15,9,15,0,17],
[9,10,11,11,9,12,9,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,22,12,18,15,15,13,17],
[11,0,9,10,12,17,10,12,11,13],
[17,16,0,16,16,22,15,10,14,16],
[3,15,9,0,11,18,11,8,11,14],
[13,13,9,14,0,21,12,9,12,15],
[7,8,3,7,4,0,6,11,7,16],
[10,15,10,14,13,19,0,10,17,16],
[10,13,15,17,16,14,15,0,18,19],
[12,14,11,14,13,18,8,7,0,15],
[8,12,9,11,10,9,9,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,10,10,10,13,10,13,17],
[11,0,17,14,12,13,19,12,15,14],
[13,8,0,5,5,8,10,3,7,8],
[15,11,20,0,16,19,13,11,15,15],
[15,13,20,9,0,13,11,12,11,16],
[15,12,17,6,12,0,17,7,15,13],
[12,6,15,12,14,8,0,6,11,15],
[15,13,22,14,13,18,19,0,11,14],
[12,10,18,10,14,10,14,14,0,13],
[8,11,17,10,9,12,10,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,6,0,0,13,13,7,0],
[18,0,18,18,18,18,25,18,18,6],
[19,7,0,19,19,19,19,7,19,7],
[19,7,6,0,7,19,25,7,7,7],
[25,7,6,18,0,18,25,13,13,6],
[25,7,6,6,7,0,13,13,7,13],
[12,0,6,0,0,12,0,0,0,0],
[12,7,18,18,12,12,25,0,19,0],
[18,7,6,18,12,18,25,6,0,6],
[25,19,18,18,19,12,25,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,8,0,10,17,2,8,2],
[23,0,7,14,1,18,23,2,8,14],
[23,18,0,16,16,18,21,11,18,25],
[17,11,9,0,9,12,18,2,3,18],
[25,24,9,16,0,19,25,2,10,16],
[15,7,7,13,6,0,13,7,13,16],
[8,2,4,7,0,12,0,2,10,4],
[23,23,14,23,23,18,23,0,9,23],
[17,17,7,22,15,12,15,16,0,18],
[23,11,0,7,9,9,21,2,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,10,10,10,15,10,10,10],
[15,0,5,10,10,15,15,10,0,10],
[10,20,0,20,20,20,25,20,10,20],
[15,15,5,0,10,5,5,20,0,0],
[15,15,5,15,0,5,15,20,15,0],
[15,10,5,20,20,0,25,20,10,20],
[10,10,0,20,10,0,0,20,10,10],
[15,15,5,5,5,5,5,0,5,5],
[15,25,15,25,10,15,15,20,0,10],
[15,15,5,25,25,5,15,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,13,12,15,13,8,13,10],
[13,0,12,12,15,19,15,12,16,14],
[12,13,0,15,11,15,21,12,15,13],
[12,13,10,0,10,13,15,9,9,11],
[13,10,14,15,0,12,18,14,14,15],
[10,6,10,12,13,0,10,12,8,13],
[12,10,4,10,7,15,0,13,10,13],
[17,13,13,16,11,13,12,0,15,9],
[12,9,10,16,11,17,15,10,0,12],
[15,11,12,14,10,12,12,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,7,18,13,19,14,18,12],
[16,0,14,13,13,7,19,14,22,17],
[10,11,0,6,11,5,17,7,16,10],
[18,12,19,0,12,19,23,14,23,19],
[7,12,14,13,0,14,12,19,18,14],
[12,18,20,6,11,0,17,8,18,17],
[6,6,8,2,13,8,0,7,17,17],
[11,11,18,11,6,17,18,0,16,17],
[7,3,9,2,7,7,8,9,0,17],
[13,8,15,6,11,8,8,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,11,9,14,12,12,13,15],
[10,0,11,9,11,12,11,11,12,12],
[14,14,0,14,13,14,13,14,13,12],
[14,16,11,0,15,14,13,16,13,13],
[16,14,12,10,0,16,11,12,14,12],
[11,13,11,11,9,0,11,10,11,9],
[13,14,12,12,14,14,0,14,12,13],
[13,14,11,9,13,15,11,0,12,13],
[12,13,12,12,11,14,13,13,0,11],
[10,13,13,12,13,16,12,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,11,17,12,15,10,16,16],
[13,0,13,13,19,12,16,9,17,15],
[11,12,0,12,13,10,15,4,13,12],
[14,12,13,0,11,13,14,6,13,12],
[8,6,12,14,0,11,9,8,9,12],
[13,13,15,12,14,0,10,13,19,18],
[10,9,10,11,16,15,0,9,15,15],
[15,16,21,19,17,12,16,0,21,22],
[9,8,12,12,16,6,10,4,0,16],
[9,10,13,13,13,7,10,3,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,12,11,10,12,13,10,11],
[15,0,18,18,14,18,17,17,14,11],
[13,7,0,13,9,10,13,9,10,10],
[13,7,12,0,6,7,11,7,7,14],
[14,11,16,19,0,16,15,13,12,12],
[15,7,15,18,9,0,15,14,12,12],
[13,8,12,14,10,10,0,8,10,10],
[12,8,16,18,12,11,17,0,12,14],
[15,11,15,18,13,13,15,13,0,14],
[14,14,15,11,13,13,15,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,15,10,15,10,9,9,11],
[5,0,20,16,6,5,0,5,5,6],
[5,5,0,5,11,10,5,10,5,11],
[10,9,20,0,6,5,5,5,0,11],
[15,19,14,19,0,10,5,10,5,10],
[10,20,15,20,15,0,9,9,5,11],
[15,25,20,20,20,16,0,10,5,16],
[16,20,15,20,15,16,15,0,11,11],
[16,20,20,25,20,20,20,14,0,11],
[14,19,14,14,15,14,9,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,14,12,15,19,8,16,14,7],
[5,0,12,8,8,10,11,8,7,2],
[11,13,0,9,14,16,11,14,13,8],
[13,17,16,0,15,19,11,18,20,11],
[10,17,11,10,0,9,10,10,13,10],
[6,15,9,6,16,0,8,9,15,13],
[17,14,14,14,15,17,0,10,14,9],
[9,17,11,7,15,16,15,0,14,9],
[11,18,12,5,12,10,11,11,0,12],
[18,23,17,14,15,12,16,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,17,11,9,12,10,16,14,12],
[14,0,13,11,16,15,14,16,15,14],
[8,12,0,10,12,10,11,11,11,8],
[14,14,15,0,16,14,10,20,16,11],
[16,9,13,9,0,11,7,14,10,8],
[13,10,15,11,14,0,13,16,15,11],
[15,11,14,15,18,12,0,18,19,14],
[9,9,14,5,11,9,7,0,10,7],
[11,10,14,9,15,10,6,15,0,8],
[13,11,17,14,17,14,11,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,12,9,12,10,11,12,8],
[11,0,11,12,5,11,9,9,13,7],
[14,14,0,10,11,15,14,11,14,12],
[13,13,15,0,8,13,10,7,15,11],
[16,20,14,17,0,16,13,8,16,13],
[13,14,10,12,9,0,11,8,12,8],
[15,16,11,15,12,14,0,11,12,9],
[14,16,14,18,17,17,14,0,17,11],
[13,12,11,10,9,13,13,8,0,10],
[17,18,13,14,12,17,16,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,10,11,8,11,14,7,7,5],
[21,0,12,13,17,15,14,16,12,17],
[15,13,0,8,14,11,14,9,9,11],
[14,12,17,0,16,15,16,10,12,10],
[17,8,11,9,0,12,16,11,7,5],
[14,10,14,10,13,0,15,8,9,7],
[11,11,11,9,9,10,0,9,6,9],
[18,9,16,15,14,17,16,0,14,13],
[18,13,16,13,18,16,19,11,0,11],
[20,8,14,15,20,18,16,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,15,12,11,8,14,10,12],
[12,0,14,15,15,14,8,14,10,13],
[13,11,0,14,13,14,13,13,10,11],
[10,10,11,0,13,7,6,14,10,11],
[13,10,12,12,0,13,11,15,11,14],
[14,11,11,18,12,0,9,14,12,12],
[17,17,12,19,14,16,0,18,16,12],
[11,11,12,11,10,11,7,0,8,10],
[15,15,15,15,14,13,9,17,0,17],
[13,12,14,14,11,13,13,15,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,13,18,14,15,16,19,10,12],
[6,0,7,13,15,7,11,9,5,9],
[12,18,0,19,18,14,12,11,11,14],
[7,12,6,0,12,7,10,10,10,11],
[11,10,7,13,0,7,9,10,5,11],
[10,18,11,18,18,0,14,14,12,10],
[9,14,13,15,16,11,0,11,12,12],
[6,16,14,15,15,11,14,0,7,10],
[15,20,14,15,20,13,13,18,0,11],
[13,16,11,14,14,15,13,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,7,4,11,6,17,6,11],
[12,0,12,10,6,16,12,13,8,11],
[10,13,0,7,3,10,11,14,6,7],
[18,15,18,0,8,16,20,18,15,16],
[21,19,22,17,0,21,24,21,10,17],
[14,9,15,9,4,0,10,8,7,9],
[19,13,14,5,1,15,0,21,9,10],
[8,12,11,7,4,17,4,0,9,12],
[19,17,19,10,15,18,16,16,0,23],
[14,14,18,9,8,16,15,13,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,11,8,14,15,15,13,15],
[12,0,15,14,12,19,16,15,15,16],
[13,10,0,16,12,18,11,12,12,15],
[14,11,9,0,9,14,14,14,12,12],
[17,13,13,16,0,16,14,16,12,15],
[11,6,7,11,9,0,12,10,11,9],
[10,9,14,11,11,13,0,10,12,11],
[10,10,13,11,9,15,15,0,12,14],
[12,10,13,13,13,14,13,13,0,11],
[10,9,10,13,10,16,14,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,17,14,12,18,9,15,16],
[10,0,10,17,15,13,12,12,12,15],
[10,15,0,15,12,8,14,15,13,11],
[8,8,10,0,9,11,12,10,6,13],
[11,10,13,16,0,6,13,15,6,14],
[13,12,17,14,19,0,13,17,17,20],
[7,13,11,13,12,12,0,9,16,15],
[16,13,10,15,10,8,16,0,13,13],
[10,13,12,19,19,8,9,12,0,12],
[9,10,14,12,11,5,10,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,15,17,16,14,11,14,18],
[8,0,8,10,12,10,11,12,8,16],
[13,17,0,14,16,12,14,12,16,15],
[10,15,11,0,14,12,13,15,13,15],
[8,13,9,11,0,12,11,8,12,15],
[9,15,13,13,13,0,12,15,14,17],
[11,14,11,12,14,13,0,14,12,17],
[14,13,13,10,17,10,11,0,10,15],
[11,17,9,12,13,11,13,15,0,16],
[7,9,10,10,10,8,8,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,2,6,4,6,7,4,3],
[13,0,17,3,10,8,10,8,5,12],
[12,8,0,8,13,8,9,13,13,9],
[23,22,17,0,10,16,8,9,10,23],
[19,15,12,15,0,9,15,14,14,16],
[21,17,17,9,16,0,12,15,13,20],
[19,15,16,17,10,13,0,16,20,18],
[18,17,12,16,11,10,9,0,13,18],
[21,20,12,15,11,12,5,12,0,19],
[22,13,16,2,9,5,7,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,20,20,17,12,14,15,13,20],
[9,0,9,17,10,13,9,8,8,12],
[5,16,0,16,8,8,5,7,4,11],
[5,8,9,0,11,6,7,7,5,13],
[8,15,17,14,0,12,9,10,9,19],
[13,12,17,19,13,0,8,9,7,16],
[11,16,20,18,16,17,0,10,11,18],
[10,17,18,18,15,16,15,0,10,15],
[12,17,21,20,16,18,14,15,0,20],
[5,13,14,12,6,9,7,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,11,13,12,13,14,16,15],
[11,0,10,10,11,11,9,10,14,10],
[14,15,0,14,13,12,11,16,13,12],
[14,15,11,0,13,13,13,15,15,15],
[12,14,12,12,0,13,11,16,14,11],
[13,14,13,12,12,0,13,15,15,14],
[12,16,14,12,14,12,0,13,15,14],
[11,15,9,10,9,10,12,0,13,9],
[9,11,12,10,11,10,10,12,0,11],
[10,15,13,10,14,11,11,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,17,14,9,12,14,10,13,10],
[16,0,16,16,11,19,15,16,16,13],
[8,9,0,16,11,12,15,11,9,9],
[11,9,9,0,8,10,12,10,14,11],
[16,14,14,17,0,17,17,12,17,13],
[13,6,13,15,8,0,13,9,13,9],
[11,10,10,13,8,12,0,11,10,12],
[15,9,14,15,13,16,14,0,15,11],
[12,9,16,11,8,12,15,10,0,10],
[15,12,16,14,12,16,13,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,13,12,17,13,11,16,14],
[9,0,14,11,10,16,10,11,13,10],
[12,11,0,15,13,15,11,11,15,13],
[12,14,10,0,16,15,11,9,13,11],
[13,15,12,9,0,15,11,11,14,11],
[8,9,10,10,10,0,10,9,9,6],
[12,15,14,14,14,15,0,11,12,13],
[14,14,14,16,14,16,14,0,13,12],
[9,12,10,12,11,16,13,12,0,13],
[11,15,12,14,14,19,12,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,14,12,14,13,11,12,13],
[9,0,16,13,14,11,15,11,12,14],
[10,9,0,10,13,11,8,11,10,11],
[11,12,15,0,16,14,11,13,11,12],
[13,11,12,9,0,12,10,7,8,13],
[11,14,14,11,13,0,13,11,11,11],
[12,10,17,14,15,12,0,13,14,14],
[14,14,14,12,18,14,12,0,15,14],
[13,13,15,14,17,14,11,10,0,15],
[12,11,14,13,12,14,11,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,13,13,18,11,14,19,12],
[8,0,13,16,15,15,14,16,18,17],
[8,12,0,8,9,16,9,10,17,11],
[12,9,17,0,16,12,13,16,20,13],
[12,10,16,9,0,13,14,14,19,15],
[7,10,9,13,12,0,13,11,14,11],
[14,11,16,12,11,12,0,15,16,10],
[11,9,15,9,11,14,10,0,16,12],
[6,7,8,5,6,11,9,9,0,11],
[13,8,14,12,10,14,15,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,14,22,17,17,17,12,12,12],
[3,0,5,10,9,11,13,7,9,5],
[11,20,0,17,12,20,20,15,12,8],
[3,15,8,0,12,20,15,10,12,8],
[8,16,13,13,0,21,16,8,10,8],
[8,14,5,5,4,0,10,9,9,5],
[8,12,5,10,9,15,0,4,14,5],
[13,18,10,15,17,16,21,0,10,5],
[13,16,13,13,15,16,11,15,0,13],
[13,20,17,17,17,20,20,20,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,6,16,9,12,18,8,15],
[18,0,21,18,16,13,21,17,12,15],
[17,4,0,10,15,5,10,14,15,16],
[19,7,15,0,15,9,15,17,12,15],
[9,9,10,10,0,10,10,10,6,16],
[16,12,20,16,15,0,21,17,12,20],
[13,4,15,10,15,4,0,17,12,14],
[7,8,11,8,15,8,8,0,3,18],
[17,13,10,13,19,13,13,22,0,19],
[10,10,9,10,9,5,11,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,19,11,13,17,11,13,14,14],
[10,0,15,8,12,8,7,11,14,12],
[6,10,0,9,11,9,11,9,15,14],
[14,17,16,0,14,17,15,12,12,21],
[12,13,14,11,0,13,13,15,17,17],
[8,17,16,8,12,0,14,5,16,17],
[14,18,14,10,12,11,0,12,10,15],
[12,14,16,13,10,20,13,0,15,15],
[11,11,10,13,8,9,15,10,0,16],
[11,13,11,4,8,8,10,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,13,16,8,15,10,18,11],
[16,0,11,13,10,11,18,14,15,12],
[12,14,0,8,11,10,13,11,14,13],
[12,12,17,0,13,12,13,13,17,17],
[9,15,14,12,0,13,12,10,14,13],
[17,14,15,13,12,0,19,14,16,17],
[10,7,12,12,13,6,0,9,13,12],
[15,11,14,12,15,11,16,0,18,17],
[7,10,11,8,11,9,12,7,0,10],
[14,13,12,8,12,8,13,8,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,14,18,18,15,13,14,8],
[14,0,16,18,20,17,16,8,16,18],
[16,9,0,9,17,16,14,13,16,8],
[11,7,16,0,16,19,19,9,15,8],
[7,5,8,9,0,16,19,10,16,6],
[7,8,9,6,9,0,7,9,1,6],
[10,9,11,6,6,18,0,11,16,5],
[12,17,12,16,15,16,14,0,11,14],
[11,9,9,10,9,24,9,14,0,9],
[17,7,17,17,19,19,20,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,4,7,7,15,7,11,7],
[17,0,18,10,13,9,21,13,25,21],
[21,7,0,13,17,7,15,11,11,11],
[21,15,12,0,21,11,15,15,19,15],
[18,12,8,4,0,12,12,16,12,8],
[18,16,18,14,13,0,12,15,19,12],
[10,4,10,10,13,13,0,7,13,9],
[18,12,14,10,9,10,18,0,18,14],
[14,0,14,6,13,6,12,7,0,14],
[18,4,14,10,17,13,16,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,1,7,7,3,5,3,9,14],
[23,0,10,8,17,15,17,13,17,21],
[24,15,0,21,21,12,17,16,22,24],
[18,17,4,0,15,11,11,9,13,20],
[18,8,4,10,0,14,11,6,13,20],
[22,10,13,14,11,0,12,13,16,24],
[20,8,8,14,14,13,0,11,14,19],
[22,12,9,16,19,12,14,0,12,20],
[16,8,3,12,12,9,11,13,0,17],
[11,4,1,5,5,1,6,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,10,14,9,7,10,10,10],
[11,0,15,14,12,11,11,8,13,13],
[13,10,0,12,10,11,6,8,11,9],
[15,11,13,0,15,14,12,10,11,14],
[11,13,15,10,0,7,11,9,11,10],
[16,14,14,11,18,0,11,13,10,15],
[18,14,19,13,14,14,0,11,17,9],
[15,17,17,15,16,12,14,0,11,18],
[15,12,14,14,14,15,8,14,0,13],
[15,12,16,11,15,10,16,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,11,13,15,12,11,11,15],
[14,0,12,14,15,14,12,14,16,12],
[16,13,0,13,13,15,12,14,16,12],
[14,11,12,0,15,14,15,13,14,16],
[12,10,12,10,0,12,12,12,15,16],
[10,11,10,11,13,0,13,11,14,15],
[13,13,13,10,13,12,0,13,14,13],
[14,11,11,12,13,14,12,0,15,13],
[14,9,9,11,10,11,11,10,0,12],
[10,13,13,9,9,10,12,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,8,10,12,11,15,10,9],
[14,0,14,10,12,13,12,17,13,13],
[15,11,0,15,14,15,13,16,17,16],
[17,15,10,0,11,15,16,20,15,17],
[15,13,11,14,0,14,10,16,11,11],
[13,12,10,10,11,0,10,15,9,12],
[14,13,12,9,15,15,0,16,10,15],
[10,8,9,5,9,10,9,0,11,7],
[15,12,8,10,14,16,15,14,0,11],
[16,12,9,8,14,13,10,18,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,10,12,3,7,11,9,11],
[15,0,11,14,15,10,9,13,13,13],
[17,14,0,15,13,12,12,16,10,14],
[15,11,10,0,15,13,12,17,15,17],
[13,10,12,10,0,10,10,9,9,11],
[22,15,13,12,15,0,13,18,12,16],
[18,16,13,13,15,12,0,14,13,13],
[14,12,9,8,16,7,11,0,11,16],
[16,12,15,10,16,13,12,14,0,14],
[14,12,11,8,14,9,12,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,7,7,18,18,25,25,18],
[0,0,0,0,0,0,0,7,7,11],
[7,25,0,14,14,25,25,18,18,18],
[18,25,11,0,7,18,18,18,18,18],
[18,25,11,18,0,18,18,18,18,11],
[7,25,0,7,7,0,11,18,18,11],
[7,25,0,7,7,14,0,7,7,11],
[0,18,7,7,7,7,18,0,18,18],
[0,18,7,7,7,7,18,7,0,18],
[7,14,7,7,14,14,14,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,10,12,11,16,12,10,13],
[15,0,14,10,10,14,17,14,13,12],
[7,11,0,11,8,15,10,7,7,16],
[15,15,14,0,12,11,15,11,12,16],
[13,15,17,13,0,12,18,11,9,15],
[14,11,10,14,13,0,18,7,9,11],
[9,8,15,10,7,7,0,12,6,14],
[13,11,18,14,14,18,13,0,13,16],
[15,12,18,13,16,16,19,12,0,16],
[12,13,9,9,10,14,11,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,13,14,12,14,15,11,15],
[10,0,15,13,13,11,10,12,14,13],
[10,10,0,11,13,11,12,11,11,10],
[12,12,14,0,12,14,10,12,9,15],
[11,12,12,13,0,14,14,15,13,14],
[13,14,14,11,11,0,11,15,10,13],
[11,15,13,15,11,14,0,14,12,12],
[10,13,14,13,10,10,11,0,11,13],
[14,11,14,16,12,15,13,14,0,13],
[10,12,15,10,11,12,13,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,8,12,11,12,9,13,9],
[11,0,18,13,17,11,15,12,16,12],
[12,7,0,9,14,10,9,12,14,12],
[17,12,16,0,19,15,12,13,18,17],
[13,8,11,6,0,11,8,9,12,14],
[14,14,15,10,14,0,13,14,15,13],
[13,10,16,13,17,12,0,14,13,15],
[16,13,13,12,16,11,11,0,16,15],
[12,9,11,7,13,10,12,9,0,5],
[16,13,13,8,11,12,10,10,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,11,14,12,15,9,10,15,7],
[8,0,7,6,5,10,8,8,10,8],
[14,18,0,8,9,21,12,12,18,12],
[11,19,17,0,13,18,20,19,19,14],
[13,20,16,12,0,18,17,19,17,17],
[10,15,4,7,7,0,11,7,10,8],
[16,17,13,5,8,14,0,14,15,14],
[15,17,13,6,6,18,11,0,15,18],
[10,15,7,6,8,15,10,10,0,11],
[18,17,13,11,8,17,11,7,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,9,15,9,20,17,15],
[15,0,12,17,21,12,12,25,25,18],
[15,13,0,13,16,12,15,16,13,18],
[15,8,12,0,21,12,8,21,21,14],
[16,4,9,4,0,9,9,11,17,15],
[10,13,13,13,16,0,15,16,13,18],
[16,13,10,17,16,10,0,20,17,17],
[5,0,9,4,14,9,5,0,13,11],
[8,0,12,4,8,12,8,12,0,18],
[10,7,7,11,10,7,8,14,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,14,8,12,15,14,12,13],
[15,0,11,15,14,16,18,18,16,16],
[15,14,0,15,13,15,16,12,13,14],
[11,10,10,0,13,11,18,12,12,13],
[17,11,12,12,0,14,17,16,15,13],
[13,9,10,14,11,0,16,14,12,15],
[10,7,9,7,8,9,0,11,8,12],
[11,7,13,13,9,11,14,0,13,13],
[13,9,12,13,10,13,17,12,0,16],
[12,9,11,12,12,10,13,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,11,11,12,9,14,10,9],
[14,0,13,11,14,11,14,13,12,10],
[16,12,0,11,16,14,14,14,13,17],
[14,14,14,0,14,13,12,16,11,14],
[14,11,9,11,0,12,12,12,13,10],
[13,14,11,12,13,0,11,12,10,12],
[16,11,11,13,13,14,0,15,14,10],
[11,12,11,9,13,13,10,0,10,10],
[15,13,12,14,12,15,11,15,0,11],
[16,15,8,11,15,13,15,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,22,15,17,19,10,18,15],
[12,0,12,19,7,19,12,18,11,20],
[12,13,0,19,7,13,13,13,11,15],
[3,6,6,0,6,7,9,0,9,6],
[10,18,18,19,0,15,21,11,17,15],
[8,6,12,18,10,0,13,13,12,14],
[6,13,12,16,4,12,0,12,12,12],
[15,7,12,25,14,12,13,0,18,14],
[7,14,14,16,8,13,13,7,0,16],
[10,5,10,19,10,11,13,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,7,11,11,10,12,12,10,12],
[14,0,14,14,10,14,16,14,13,15],
[18,11,0,10,12,13,12,12,11,14],
[14,11,15,0,11,10,13,13,10,14],
[14,15,13,14,0,16,15,13,9,16],
[15,11,12,15,9,0,13,13,9,12],
[13,9,13,12,10,12,0,9,13,15],
[13,11,13,12,12,12,16,0,12,12],
[15,12,14,15,16,16,12,13,0,14],
[13,10,11,11,9,13,10,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,8,12,10,8,11,7,9],
[17,0,11,12,18,13,10,15,10,12],
[16,14,0,9,16,12,11,14,12,13],
[17,13,16,0,17,15,12,18,13,12],
[13,7,9,8,0,10,5,11,7,9],
[15,12,13,10,15,0,8,13,9,11],
[17,15,14,13,20,17,0,16,12,15],
[14,10,11,7,14,12,9,0,11,11],
[18,15,13,12,18,16,13,14,0,12],
[16,13,12,13,16,14,10,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,6,10,19,19,16,10,16,0],
[9,0,6,10,19,19,16,10,16,0],
[19,19,0,19,19,19,10,19,19,19],
[15,15,6,0,19,9,6,6,15,9],
[6,6,6,6,0,9,6,6,6,6],
[6,6,6,16,16,0,16,16,16,6],
[9,9,15,19,19,9,0,19,19,9],
[15,15,6,19,19,9,6,0,15,9],
[9,9,6,10,19,9,6,10,0,0],
[25,25,6,16,19,19,16,16,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,11,11,8,11,13,13,13],
[16,0,11,10,13,9,12,9,11,13],
[12,14,0,13,8,11,13,12,14,15],
[14,15,12,0,11,10,10,15,14,15],
[14,12,17,14,0,14,11,11,12,15],
[17,16,14,15,11,0,11,17,13,17],
[14,13,12,15,14,14,0,17,19,13],
[12,16,13,10,14,8,8,0,12,14],
[12,14,11,11,13,12,6,13,0,15],
[12,12,10,10,10,8,12,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,7,9,10,12,8,7,15],
[14,0,11,11,12,13,16,13,12,16],
[12,14,0,11,14,15,13,11,13,17],
[18,14,14,0,12,13,12,13,15,18],
[16,13,11,13,0,18,14,13,14,16],
[15,12,10,12,7,0,12,13,11,15],
[13,9,12,13,11,13,0,14,16,16],
[17,12,14,12,12,12,11,0,14,15],
[18,13,12,10,11,14,9,11,0,14],
[10,9,8,7,9,10,9,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,13,12,8,12,13,10,12],
[16,0,12,14,13,14,18,16,13,14],
[13,13,0,14,11,7,13,16,12,12],
[12,11,11,0,11,9,13,12,12,12],
[13,12,14,14,0,9,13,16,12,13],
[17,11,18,16,16,0,16,16,14,15],
[13,7,12,12,12,9,0,12,9,11],
[12,9,9,13,9,9,13,0,10,11],
[15,12,13,13,13,11,16,15,0,11],
[13,11,13,13,12,10,14,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,15,15,16,13,13,12,16],
[9,0,10,10,15,8,9,10,12,11],
[11,15,0,15,16,11,9,13,13,7],
[10,15,10,0,13,10,9,13,10,12],
[10,10,9,12,0,8,10,8,10,12],
[9,17,14,15,17,0,13,14,15,12],
[12,16,16,16,15,12,0,12,15,13],
[12,15,12,12,17,11,13,0,11,12],
[13,13,12,15,15,10,10,14,0,15],
[9,14,18,13,13,13,12,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,13,18,14,12,14,17,15],
[11,0,12,11,14,12,12,14,14,15],
[13,13,0,12,15,13,11,15,12,15],
[12,14,13,0,16,11,14,10,12,13],
[7,11,10,9,0,10,12,11,10,10],
[11,13,12,14,15,0,13,17,12,16],
[13,13,14,11,13,12,0,10,11,11],
[11,11,10,15,14,8,15,0,13,13],
[8,11,13,13,15,13,14,12,0,14],
[10,10,10,12,15,9,14,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,14,16,9,5,8,8,17],
[13,0,13,15,16,10,13,16,13,19],
[15,12,0,13,19,12,11,14,9,15],
[11,10,12,0,16,11,7,9,9,12],
[9,9,6,9,0,9,9,10,10,13],
[16,15,13,14,16,0,11,16,11,13],
[20,12,14,18,16,14,0,14,8,16],
[17,9,11,16,15,9,11,0,9,14],
[17,12,16,16,15,14,17,16,0,18],
[8,6,10,13,12,12,9,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,13,12,16,18,14,17,15,11],
[6,0,12,11,9,11,9,5,12,7],
[12,13,0,15,15,18,11,9,12,14],
[13,14,10,0,14,13,10,9,15,6],
[9,16,10,11,0,16,11,10,14,13],
[7,14,7,12,9,0,11,10,15,8],
[11,16,14,15,14,14,0,9,12,8],
[8,20,16,16,15,15,16,0,20,14],
[10,13,13,10,11,10,13,5,0,8],
[14,18,11,19,12,17,17,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,12,9,11,11,12,6,12],
[10,0,16,6,6,11,15,11,10,14],
[16,9,0,7,9,5,12,12,6,17],
[13,19,18,0,10,10,18,15,13,15],
[16,19,16,15,0,10,16,14,7,15],
[14,14,20,15,15,0,14,12,13,18],
[14,10,13,7,9,11,0,11,5,13],
[13,14,13,10,11,13,14,0,9,10],
[19,15,19,12,18,12,20,16,0,18],
[13,11,8,10,10,7,12,15,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,10,12,12,11,11,11,6,8],
[8,0,7,11,5,9,2,9,6,6],
[15,18,0,17,11,15,12,14,14,8],
[13,14,8,0,6,11,9,13,8,6],
[13,20,14,19,0,14,9,15,12,15],
[14,16,10,14,11,0,13,14,14,12],
[14,23,13,16,16,12,0,13,15,15],
[14,16,11,12,10,11,12,0,12,11],
[19,19,11,17,13,11,10,13,0,14],
[17,19,17,19,10,13,10,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,12,14,19,15,16,15,17],
[10,0,14,11,10,16,12,14,9,10],
[8,11,0,10,12,14,12,14,10,12],
[13,14,15,0,12,18,13,13,11,15],
[11,15,13,13,0,18,15,13,12,15],
[6,9,11,7,7,0,8,9,8,8],
[10,13,13,12,10,17,0,11,11,15],
[9,11,11,12,12,16,14,0,16,13],
[10,16,15,14,13,17,14,9,0,16],
[8,15,13,10,10,17,10,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,6,14,9,6,16,10,10],
[15,0,8,13,12,12,10,21,19,13],
[20,17,0,13,20,14,9,19,13,17],
[19,12,12,0,19,14,16,19,16,14],
[11,13,5,6,0,9,11,15,10,12],
[16,13,11,11,16,0,4,15,14,12],
[19,15,16,9,14,21,0,19,17,13],
[9,4,6,6,10,10,6,0,12,6],
[15,6,12,9,15,11,8,13,0,9],
[15,12,8,11,13,13,12,19,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,11,12,13,13,16,15,14,13],
[8,0,15,11,8,15,12,15,17,14],
[14,10,0,9,9,13,9,15,17,15],
[13,14,16,0,9,13,13,20,19,14],
[12,17,16,16,0,15,17,18,20,18],
[12,10,12,12,10,0,10,20,16,17],
[9,13,16,12,8,15,0,13,12,13],
[10,10,10,5,7,5,12,0,11,13],
[11,8,8,6,5,9,13,14,0,10],
[12,11,10,11,7,8,12,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,17,21,11,16,20,9,16],
[13,0,20,13,17,14,23,18,12,20],
[14,5,0,14,14,14,9,15,5,17],
[8,12,11,0,15,11,12,12,9,9],
[4,8,11,10,0,11,13,17,8,15],
[14,11,11,14,14,0,14,14,14,11],
[9,2,16,13,12,11,0,18,5,20],
[5,7,10,13,8,11,7,0,4,10],
[16,13,20,16,17,11,20,21,0,20],
[9,5,8,16,10,14,5,15,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,22,15,15,11,17,17,19,17],
[7,0,7,10,5,12,6,4,7,5],
[3,18,0,15,10,11,12,8,8,8],
[10,15,10,0,15,13,17,13,10,13],
[10,20,15,10,0,10,9,18,10,14],
[14,13,14,12,15,0,11,13,14,13],
[8,19,13,8,16,14,0,19,13,14],
[8,21,17,12,7,12,6,0,12,12],
[6,18,17,15,15,11,12,13,0,13],
[8,20,17,12,11,12,11,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,14,13,10,11,9,10,9],
[18,0,14,17,16,12,13,8,11,8],
[13,11,0,15,12,10,12,11,9,11],
[11,8,10,0,10,9,7,9,11,7],
[12,9,13,15,0,8,9,9,9,9],
[15,13,15,16,17,0,13,11,13,11],
[14,12,13,18,16,12,0,15,14,14],
[16,17,14,16,16,14,10,0,9,12],
[15,14,16,14,16,12,11,16,0,12],
[16,17,14,18,16,14,11,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,9,12,8,8,4,8,11],
[17,0,14,19,9,18,12,14,23,18],
[16,11,0,14,10,15,13,11,15,9],
[16,6,11,0,10,15,15,11,15,4],
[13,16,15,15,0,16,14,10,16,14],
[17,7,10,10,9,0,8,12,15,12],
[17,13,12,10,11,17,0,16,18,14],
[21,11,14,14,15,13,9,0,11,12],
[17,2,10,10,9,10,7,14,0,12],
[14,7,16,21,11,13,11,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,13,11,15,12,12,13,11],
[12,0,12,14,8,19,10,13,11,12],
[16,13,0,11,14,16,16,13,12,13],
[12,11,14,0,9,14,15,14,14,11],
[14,17,11,16,0,19,16,16,16,12],
[10,6,9,11,6,0,12,8,10,10],
[13,15,9,10,9,13,0,13,12,10],
[13,12,12,11,9,17,12,0,12,10],
[12,14,13,11,9,15,13,13,0,10],
[14,13,12,14,13,15,15,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,6,12,11,13,15,11,13],
[16,0,13,10,19,11,16,14,13,15],
[15,12,0,13,17,12,16,18,15,19],
[19,15,12,0,15,15,15,15,18,14],
[13,6,8,10,0,6,14,14,11,15],
[14,14,13,10,19,0,12,12,13,14],
[12,9,9,10,11,13,0,12,13,12],
[10,11,7,10,11,13,13,0,13,11],
[14,12,10,7,14,12,12,12,0,12],
[12,10,6,11,10,11,13,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,12,4,8,8,9,6,13,7],
[20,0,15,12,17,13,17,15,18,14],
[13,10,0,10,14,11,17,11,15,10],
[21,13,15,0,16,11,22,18,19,16],
[17,8,11,9,0,7,17,11,13,17],
[17,12,14,14,18,0,18,17,16,15],
[16,8,8,3,8,7,0,11,13,12],
[19,10,14,7,14,8,14,0,16,14],
[12,7,10,6,12,9,12,9,0,13],
[18,11,15,9,8,10,13,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,16,23,13,17,14,12,16],
[10,0,12,12,14,10,11,13,8,10],
[9,13,0,15,10,10,16,12,9,11],
[9,13,10,0,7,10,9,13,9,8],
[2,11,15,18,0,12,13,13,14,13],
[12,15,15,15,13,0,15,14,10,16],
[8,14,9,16,12,10,0,18,12,16],
[11,12,13,12,12,11,7,0,9,13],
[13,17,16,16,11,15,13,16,0,15],
[9,15,14,17,12,9,9,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,9,12,13,10,9,13,13],
[11,0,11,12,12,11,10,8,9,15],
[15,14,0,14,14,10,7,12,11,16],
[16,13,11,0,11,6,12,10,11,13],
[13,13,11,14,0,16,14,11,17,19],
[12,14,15,19,9,0,16,13,16,15],
[15,15,18,13,11,9,0,13,12,12],
[16,17,13,15,14,12,12,0,11,18],
[12,16,14,14,8,9,13,14,0,16],
[12,10,9,12,6,10,13,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,14,13,13,8,15,14,15],
[11,0,11,19,10,13,9,13,13,15],
[12,14,0,14,12,11,12,13,18,15],
[11,6,11,0,9,11,7,12,5,9],
[12,15,13,16,0,12,14,13,14,18],
[12,12,14,14,13,0,15,17,18,9],
[17,16,13,18,11,10,0,17,13,15],
[10,12,12,13,12,8,8,0,9,12],
[11,12,7,20,11,7,12,16,0,14],
[10,10,10,16,7,16,10,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,10,8,11,11,7,9,11],
[16,0,15,14,12,16,17,13,10,17],
[13,10,0,9,10,11,13,11,11,13],
[15,11,16,0,14,20,13,11,13,16],
[17,13,15,11,0,15,15,14,14,15],
[14,9,14,5,10,0,14,10,12,14],
[14,8,12,12,10,11,0,9,8,14],
[18,12,14,14,11,15,16,0,17,19],
[16,15,14,12,11,13,17,8,0,16],
[14,8,12,9,10,11,11,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,9,6,7,8,5,7,7],
[17,0,8,12,10,9,7,10,11,11],
[19,17,0,18,11,14,12,13,13,17],
[16,13,7,0,11,9,9,12,12,11],
[19,15,14,14,0,16,11,10,15,17],
[18,16,11,16,9,0,11,10,10,15],
[17,18,13,16,14,14,0,12,11,16],
[20,15,12,13,15,15,13,0,13,17],
[18,14,12,13,10,15,14,12,0,12],
[18,14,8,14,8,10,9,8,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,16,10,8,10,13,10,7],
[16,0,12,17,15,10,16,16,13,11],
[14,13,0,14,12,6,11,13,10,10],
[9,8,11,0,12,7,9,13,10,6],
[15,10,13,13,0,10,16,11,10,14],
[17,15,19,18,15,0,16,17,12,12],
[15,9,14,16,9,9,0,13,7,11],
[12,9,12,12,14,8,12,0,11,8],
[15,12,15,15,15,13,18,14,0,15],
[18,14,15,19,11,13,14,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,12,15,13,14,14,16,11,8],
[6,0,5,7,7,7,10,7,7,8],
[13,20,0,17,10,10,14,13,15,8],
[10,18,8,0,11,12,13,12,15,11],
[12,18,15,14,0,15,12,13,12,14],
[11,18,15,13,10,0,11,13,10,13],
[11,15,11,12,13,14,0,11,11,11],
[9,18,12,13,12,12,14,0,12,12],
[14,18,10,10,13,15,14,13,0,16],
[17,17,17,14,11,12,14,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,11,13,15,9,12,10,14],
[15,0,13,13,13,17,11,15,14,12],
[13,12,0,12,9,12,8,12,14,13],
[14,12,13,0,14,18,14,16,14,16],
[12,12,16,11,0,15,11,10,10,12],
[10,8,13,7,10,0,8,10,9,12],
[16,14,17,11,14,17,0,15,15,15],
[13,10,13,9,15,15,10,0,12,13],
[15,11,11,11,15,16,10,13,0,17],
[11,13,12,9,13,13,10,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,9,10,13,13,14,14,9],
[12,0,16,13,12,15,14,16,18,14],
[7,9,0,11,11,11,9,11,11,12],
[16,12,14,0,13,14,14,15,16,13],
[15,13,14,12,0,16,16,13,21,12],
[12,10,14,11,9,0,9,11,13,9],
[12,11,16,11,9,16,0,12,15,9],
[11,9,14,10,12,14,13,0,14,7],
[11,7,14,9,4,12,10,11,0,7],
[16,11,13,12,13,16,16,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,14,12,17,13,14,10,14],
[12,0,10,9,8,15,10,12,11,13],
[12,15,0,11,13,15,16,16,13,13],
[11,16,14,0,13,18,20,15,15,15],
[13,17,12,12,0,16,15,16,13,14],
[8,10,10,7,9,0,10,11,9,13],
[12,15,9,5,10,15,0,13,9,11],
[11,13,9,10,9,14,12,0,9,14],
[15,14,12,10,12,16,16,16,0,14],
[11,12,12,10,11,12,14,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,17,14,14,19,9,14,14],
[15,0,13,14,17,13,17,12,15,9],
[12,12,0,20,13,13,17,14,15,12],
[8,11,5,0,11,9,10,8,9,8],
[11,8,12,14,0,7,18,11,13,12],
[11,12,12,16,18,0,19,6,16,12],
[6,8,8,15,7,6,0,3,10,8],
[16,13,11,17,14,19,22,0,15,12],
[11,10,10,16,12,9,15,10,0,10],
[11,16,13,17,13,13,17,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,10,8,13,14,11,7,11],
[14,0,13,11,11,11,15,14,11,14],
[17,12,0,11,13,15,16,13,10,15],
[15,14,14,0,12,12,15,15,13,17],
[17,14,12,13,0,15,17,17,15,16],
[12,14,10,13,10,0,12,13,9,14],
[11,10,9,10,8,13,0,12,10,16],
[14,11,12,10,8,12,13,0,10,9],
[18,14,15,12,10,16,15,15,0,16],
[14,11,10,8,9,11,9,16,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,16,23,12,23,14,14,5],
[11,0,14,20,18,14,25,23,18,14],
[11,11,0,11,20,14,16,16,9,16],
[9,5,14,0,18,14,14,7,11,7],
[2,7,5,7,0,14,7,7,9,5],
[13,11,11,11,11,0,11,11,11,9],
[2,0,9,11,18,14,0,0,11,2],
[11,2,9,18,18,14,25,0,11,2],
[11,7,16,14,16,14,14,14,0,7],
[20,11,9,18,20,16,23,23,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,0,8,15,3,15,8,8],
[14,0,14,14,12,19,7,17,22,9],
[15,11,0,5,15,14,5,20,13,10],
[25,11,20,0,15,19,13,20,18,10],
[17,13,10,10,0,14,10,13,15,12],
[10,6,11,6,11,0,8,13,8,11],
[22,18,20,12,15,17,0,15,20,18],
[10,8,5,5,12,12,10,0,5,12],
[17,3,12,7,10,17,5,20,0,7],
[17,16,15,15,13,14,7,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,7,7,7,8,11,8,7],
[16,0,10,14,11,16,13,16,11,9],
[15,15,0,11,12,13,11,15,17,11],
[18,11,14,0,12,16,6,15,14,13],
[18,14,13,13,0,15,9,17,18,8],
[18,9,12,9,10,0,6,9,14,11],
[17,12,14,19,16,19,0,13,17,11],
[14,9,10,10,8,16,12,0,12,5],
[17,14,8,11,7,11,8,13,0,7],
[18,16,14,12,17,14,14,20,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,11,14,11,10,12,8,6],
[12,0,13,17,17,16,10,16,10,11],
[17,12,0,14,15,12,13,12,10,14],
[14,8,11,0,17,13,13,12,10,13],
[11,8,10,8,0,11,9,8,6,5],
[14,9,13,12,14,0,10,15,9,10],
[15,15,12,12,16,15,0,16,10,10],
[13,9,13,13,17,10,9,0,9,12],
[17,15,15,15,19,16,15,16,0,9],
[19,14,11,12,20,15,15,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,12,10,11,13,12,9,13],
[13,0,13,14,12,8,15,9,8,9],
[11,12,0,13,12,12,12,12,9,13],
[13,11,12,0,11,13,17,9,10,12],
[15,13,13,14,0,12,16,14,13,14],
[14,17,13,12,13,0,16,14,11,9],
[12,10,13,8,9,9,0,11,12,13],
[13,16,13,16,11,11,14,0,9,16],
[16,17,16,15,12,14,13,16,0,15],
[12,16,12,13,11,16,12,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,13,15,16,14,14,11,14],
[10,0,10,10,12,10,7,12,8,12],
[10,15,0,14,16,16,13,13,11,14],
[12,15,11,0,18,14,11,11,13,17],
[10,13,9,7,0,9,6,12,8,11],
[9,15,9,11,16,0,11,9,9,13],
[11,18,12,14,19,14,0,12,10,14],
[11,13,12,14,13,16,13,0,10,16],
[14,17,14,12,17,16,15,15,0,17],
[11,13,11,8,14,12,11,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,18,17,13,14,18,16,14],
[14,0,16,18,11,17,13,18,15,15],
[10,9,0,9,12,11,12,14,10,10],
[7,7,16,0,9,17,13,17,13,12],
[8,14,13,16,0,16,11,14,10,9],
[12,8,14,8,9,0,6,13,8,13],
[11,12,13,12,14,19,0,16,12,14],
[7,7,11,8,11,12,9,0,8,7],
[9,10,15,12,15,17,13,17,0,12],
[11,10,15,13,16,12,11,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,11,18,18,14,13,11,13],
[10,0,13,8,16,8,11,14,12,18],
[9,12,0,8,15,10,11,12,11,8],
[14,17,17,0,20,13,16,16,13,10],
[7,9,10,5,0,8,7,12,10,10],
[7,17,15,12,17,0,17,10,11,12],
[11,14,14,9,18,8,0,13,14,15],
[12,11,13,9,13,15,12,0,5,7],
[14,13,14,12,15,14,11,20,0,18],
[12,7,17,15,15,13,10,18,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,15,14,15,11,11,15,15],
[15,0,15,12,15,12,15,15,15,12],
[10,10,0,0,10,4,3,10,14,13],
[10,13,25,0,15,25,14,21,25,20],
[11,10,15,10,0,10,15,11,15,10],
[10,13,21,0,15,0,8,15,25,16],
[14,10,22,11,10,17,0,12,17,17],
[14,10,15,4,14,10,13,0,20,10],
[10,10,11,0,10,0,8,5,0,6],
[10,13,12,5,15,9,8,15,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,12,12,6,10,9,9,11,11],
[20,0,14,13,11,18,13,14,15,13],
[13,11,0,11,8,17,16,9,12,10],
[13,12,14,0,8,11,13,10,12,11],
[19,14,17,17,0,17,16,12,17,17],
[15,7,8,14,8,0,9,12,12,13],
[16,12,9,12,9,16,0,8,16,15],
[16,11,16,15,13,13,17,0,15,14],
[14,10,13,13,8,13,9,10,0,12],
[14,12,15,14,8,12,10,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,24,20,20,20,25,12,21],
[6,0,14,5,11,6,10,6,6,10],
[1,11,0,6,12,6,11,7,7,12],
[1,20,19,0,17,10,9,15,7,21],
[5,14,13,8,0,10,9,9,1,5],
[5,19,19,15,15,0,20,15,12,16],
[5,15,14,16,16,5,0,16,17,20],
[0,19,18,10,16,10,9,0,12,20],
[13,19,18,18,24,13,8,13,0,18],
[4,15,13,4,20,9,5,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,16,16,17,15,13,17],
[13,0,10,12,11,14,13,13,13,15],
[13,15,0,11,13,11,13,11,13,16],
[12,13,14,0,12,14,12,13,11,16],
[9,14,12,13,0,16,15,14,13,14],
[9,11,14,11,9,0,13,13,15,13],
[8,12,12,13,10,12,0,11,15,14],
[10,12,14,12,11,12,14,0,13,14],
[12,12,12,14,12,10,10,12,0,17],
[8,10,9,9,11,12,11,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,1,10,17,9,9,9,18,18],
[15,0,16,9,16,8,24,9,25,8],
[24,9,0,10,17,9,9,9,25,17],
[15,16,15,0,7,0,16,9,24,8],
[8,9,8,18,0,9,17,9,18,17],
[16,17,16,25,16,0,24,9,25,9],
[16,1,16,9,8,1,0,10,16,9],
[16,16,16,16,16,16,15,0,16,9],
[7,0,0,1,7,0,9,9,0,0],
[7,17,8,17,8,16,16,16,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,9,14,11,15,18,14,13],
[14,0,19,12,19,11,14,15,14,9],
[16,6,0,10,7,10,11,16,10,7],
[16,13,15,0,12,12,13,17,13,8],
[11,6,18,13,0,10,10,16,9,7],
[14,14,15,13,15,0,16,16,14,11],
[10,11,14,12,15,9,0,11,10,16],
[7,10,9,8,9,9,14,0,8,9],
[11,11,15,12,16,11,15,17,0,12],
[12,16,18,17,18,14,9,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 25, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_10_25.csv", index=False, header=False)