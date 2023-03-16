
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,24,22,22,22,18,19,22,19,20],
[27,0,24,32,25,19,24,28,35,28],
[29,27,0,29,25,24,23,23,21,23],
[29,19,22,0,21,22,20,25,22,21],
[29,26,26,30,0,19,17,22,27,27],
[33,32,27,29,32,0,34,30,27,25],
[32,27,28,31,34,17,0,27,24,27],
[29,23,28,26,29,21,24,0,20,21],
[32,16,30,29,24,24,27,31,0,19],
[31,23,28,30,24,26,24,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,25,28,27,32,31,25,27],
[28,0,30,21,27,22,26,32,22,29],
[28,21,0,26,29,24,22,28,21,30],
[26,30,25,0,32,26,24,32,24,28],
[23,24,22,19,0,20,25,30,20,26],
[24,29,27,25,31,0,26,35,26,30],
[19,25,29,27,26,25,0,32,24,30],
[20,19,23,19,21,16,19,0,21,26],
[26,29,30,27,31,25,27,30,0,32],
[24,22,21,23,25,21,21,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,17,22,20,20,16,21,29,22],
[27,0,22,24,24,22,22,28,27,21],
[34,29,0,24,27,26,21,28,34,25],
[29,27,27,0,22,27,26,21,30,20],
[31,27,24,29,0,27,22,26,34,26],
[31,29,25,24,24,0,23,25,29,22],
[35,29,30,25,29,28,0,23,33,23],
[30,23,23,30,25,26,28,0,29,24],
[22,24,17,21,17,22,18,22,0,20],
[29,30,26,31,25,29,28,27,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,26,19,24,14,9,16,9,19],
[33,0,32,33,23,27,19,19,31,29],
[25,19,0,18,30,21,20,14,20,22],
[32,18,33,0,26,26,15,15,32,33],
[27,28,21,25,0,28,22,29,27,18],
[37,24,30,25,23,0,24,19,37,19],
[42,32,31,36,29,27,0,24,30,33],
[35,32,37,36,22,32,27,0,43,31],
[42,20,31,19,24,14,21,8,0,27],
[32,22,29,18,33,32,18,20,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,34,22,25,34,20,29,25],
[27,0,25,34,20,21,31,31,22,26],
[22,26,0,32,16,25,30,21,25,26],
[17,17,19,0,17,18,29,22,22,21],
[29,31,35,34,0,25,34,31,25,26],
[26,30,26,33,26,0,34,24,28,24],
[17,20,21,22,17,17,0,23,22,19],
[31,20,30,29,20,27,28,0,23,23],
[22,29,26,29,26,23,29,28,0,22],
[26,25,25,30,25,27,32,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,24,35,25,29,31,24,24],
[29,0,28,23,29,31,30,36,27,31],
[18,23,0,21,29,21,25,25,22,27],
[27,28,30,0,40,30,31,27,23,34],
[16,22,22,11,0,19,21,20,17,28],
[26,20,30,21,32,0,28,28,19,23],
[22,21,26,20,30,23,0,23,16,31],
[20,15,26,24,31,23,28,0,13,26],
[27,24,29,28,34,32,35,38,0,41],
[27,20,24,17,23,28,20,25,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,34,29,23,24,21,26,26],
[26,0,26,26,24,22,26,28,24,27],
[25,25,0,29,29,24,24,21,25,25],
[17,25,22,0,26,24,25,17,28,25],
[22,27,22,25,0,21,26,22,21,22],
[28,29,27,27,30,0,30,22,25,24],
[27,25,27,26,25,21,0,20,22,25],
[30,23,30,34,29,29,31,0,26,34],
[25,27,26,23,30,26,29,25,0,23],
[25,24,26,26,29,27,26,17,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,37,32,46,27,40,24,21,22],
[25,0,36,25,42,31,36,25,36,22],
[14,15,0,14,31,15,12,9,22,9],
[19,26,37,0,42,15,27,20,33,22],
[5,9,20,9,0,3,20,9,15,12],
[24,20,36,36,48,0,36,26,35,25],
[11,15,39,24,31,15,0,9,18,10],
[27,26,42,31,42,25,42,0,35,34],
[30,15,29,18,36,16,33,16,0,19],
[29,29,42,29,39,26,41,17,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,27,26,23,28,23,28,26,30],
[19,0,22,28,23,30,25,23,20,25],
[24,29,0,26,24,29,26,30,28,32],
[25,23,25,0,23,28,24,27,21,28],
[28,28,27,28,0,25,27,28,24,30],
[23,21,22,23,26,0,20,26,19,28],
[28,26,25,27,24,31,0,25,22,29],
[23,28,21,24,23,25,26,0,23,34],
[25,31,23,30,27,32,29,28,0,30],
[21,26,19,23,21,23,22,17,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,28,28,22,30,29,25,25],
[23,0,21,24,23,20,23,21,20,22],
[25,30,0,27,30,21,25,25,23,22],
[23,27,24,0,25,26,28,24,29,25],
[23,28,21,26,0,26,28,23,25,22],
[29,31,30,25,25,0,23,27,31,24],
[21,28,26,23,23,28,0,20,26,27],
[22,30,26,27,28,24,31,0,22,27],
[26,31,28,22,26,20,25,29,0,25],
[26,29,29,26,29,27,24,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,24,27,29,24,29,27,28],
[23,0,25,23,22,24,23,31,24,23],
[26,26,0,28,26,26,24,29,28,26],
[27,28,23,0,27,25,31,32,25,26],
[24,29,25,24,0,23,24,29,29,23],
[22,27,25,26,28,0,29,23,27,28],
[27,28,27,20,27,22,0,25,29,28],
[22,20,22,19,22,28,26,0,21,20],
[24,27,23,26,22,24,22,30,0,22],
[23,28,25,25,28,23,23,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,26,28,24,25,25,23,25],
[27,0,20,26,28,30,26,27,23,27],
[29,31,0,32,35,28,27,31,28,25],
[25,25,19,0,32,29,25,23,20,24],
[23,23,16,19,0,21,21,19,15,18],
[27,21,23,22,30,0,30,21,21,22],
[26,25,24,26,30,21,0,26,25,24],
[26,24,20,28,32,30,25,0,28,24],
[28,28,23,31,36,30,26,23,0,22],
[26,24,26,27,33,29,27,27,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,25,30,36,30,33,26,31,30],
[18,0,21,30,22,19,25,24,26,30],
[26,30,0,34,33,22,32,24,31,28],
[21,21,17,0,30,21,27,20,24,28],
[15,29,18,21,0,24,26,26,22,32],
[21,32,29,30,27,0,35,25,27,27],
[18,26,19,24,25,16,0,15,21,24],
[25,27,27,31,25,26,36,0,29,27],
[20,25,20,27,29,24,30,22,0,27],
[21,21,23,23,19,24,27,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,20,15,17,22,26,18,20,25],
[32,0,23,23,26,25,27,33,29,32],
[31,28,0,31,33,25,33,27,25,34],
[36,28,20,0,26,24,32,33,23,35],
[34,25,18,25,0,29,29,30,21,35],
[29,26,26,27,22,0,29,28,23,30],
[25,24,18,19,22,22,0,24,19,31],
[33,18,24,18,21,23,27,0,22,29],
[31,22,26,28,30,28,32,29,0,34],
[26,19,17,16,16,21,20,22,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,26,25,22,25,30,23,25,27],
[31,0,30,21,21,24,28,25,27,27],
[25,21,0,22,21,23,23,21,19,26],
[26,30,29,0,27,27,31,29,25,31],
[29,30,30,24,0,28,31,24,28,32],
[26,27,28,24,23,0,28,24,24,28],
[21,23,28,20,20,23,0,21,23,26],
[28,26,30,22,27,27,30,0,23,30],
[26,24,32,26,23,27,28,28,0,30],
[24,24,25,20,19,23,25,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,22,30,30,32,23,21,25],
[28,0,16,21,35,33,27,17,37,22],
[32,35,0,20,30,28,30,25,38,19],
[29,30,31,0,49,29,36,27,35,22],
[21,16,21,2,0,16,17,9,21,14],
[21,18,23,22,35,0,29,25,28,21],
[19,24,21,15,34,22,0,19,32,10],
[28,34,26,24,42,26,32,0,33,20],
[30,14,13,16,30,23,19,18,0,27],
[26,29,32,29,37,30,41,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,27,33,27,10,25,14,23],
[26,0,13,19,14,19,24,6,26,34],
[30,38,0,19,29,34,24,29,19,28],
[24,32,32,0,32,32,18,27,16,17],
[18,37,22,19,0,31,18,38,27,28],
[24,32,17,19,20,0,7,27,22,23],
[41,27,27,33,33,44,0,25,30,23],
[26,45,22,24,13,24,26,0,26,28],
[37,25,32,35,24,29,21,25,0,34],
[28,17,23,34,23,28,28,23,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,38,37,23,24,35,31,29,26],
[18,0,35,36,28,29,32,27,27,15],
[13,16,0,25,16,14,24,16,15,12],
[14,15,26,0,18,11,24,18,11,12],
[28,23,35,33,0,24,38,32,25,31],
[27,22,37,40,27,0,36,21,16,25],
[16,19,27,27,13,15,0,13,10,12],
[20,24,35,33,19,30,38,0,17,23],
[22,24,36,40,26,35,41,34,0,39],
[25,36,39,39,20,26,39,28,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,18,27,21,16,31,23,24,32],
[18,0,23,27,17,21,39,22,30,33],
[33,28,0,32,25,30,29,30,24,28],
[24,24,19,0,20,22,16,17,18,24],
[30,34,26,31,0,22,40,28,21,45],
[35,30,21,29,29,0,34,25,27,33],
[20,12,22,35,11,17,0,27,19,33],
[28,29,21,34,23,26,24,0,16,26],
[27,21,27,33,30,24,32,35,0,31],
[19,18,23,27,6,18,18,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,26,23,26,20,34,25,28],
[26,0,26,25,19,14,21,29,25,19],
[22,25,0,23,23,23,24,30,24,23],
[25,26,28,0,23,16,25,26,21,27],
[28,32,28,28,0,21,29,26,24,15],
[25,37,28,35,30,0,25,31,26,26],
[31,30,27,26,22,26,0,32,26,22],
[17,22,21,25,25,20,19,0,16,11],
[26,26,27,30,27,25,25,35,0,26],
[23,32,28,24,36,25,29,40,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,22,32,23,27,25,32,26],
[22,0,27,31,38,26,31,31,35,29],
[24,24,0,33,40,27,31,39,34,26],
[29,20,18,0,34,27,28,26,21,19],
[19,13,11,17,0,16,14,18,17,15],
[28,25,24,24,35,0,26,27,29,28],
[24,20,20,23,37,25,0,29,29,25],
[26,20,12,25,33,24,22,0,27,26],
[19,16,17,30,34,22,22,24,0,19],
[25,22,25,32,36,23,26,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,33,21,24,24,28,22,27,23],
[28,0,33,23,31,26,27,30,31,25],
[18,18,0,24,25,23,26,28,31,24],
[30,28,27,0,27,23,29,30,31,26],
[27,20,26,24,0,27,24,22,29,24],
[27,25,28,28,24,0,26,25,30,25],
[23,24,25,22,27,25,0,27,31,26],
[29,21,23,21,29,26,24,0,25,28],
[24,20,20,20,22,21,20,26,0,21],
[28,26,27,25,27,26,25,23,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,25,27,29,16,25,20,24],
[29,0,29,31,26,30,33,31,22,28],
[25,22,0,27,26,33,24,28,29,26],
[26,20,24,0,30,30,16,25,23,19],
[24,25,25,21,0,29,23,26,21,15],
[22,21,18,21,22,0,17,25,17,20],
[35,18,27,35,28,34,0,23,25,27],
[26,20,23,26,25,26,28,0,21,25],
[31,29,22,28,30,34,26,30,0,28],
[27,23,25,32,36,31,24,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,28,10,18,15,17,16,27],
[33,0,20,31,15,25,24,19,27,27],
[34,31,0,30,21,31,22,27,28,32],
[23,20,21,0,12,19,13,18,19,23],
[41,36,30,39,0,35,32,24,30,35],
[33,26,20,32,16,0,22,23,25,26],
[36,27,29,38,19,29,0,27,32,33],
[34,32,24,33,27,28,24,0,32,28],
[35,24,23,32,21,26,19,19,0,25],
[24,24,19,28,16,25,18,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,24,25,24,23,22,27,21],
[24,0,25,23,22,21,25,20,22,22],
[25,26,0,31,24,20,27,25,21,24],
[27,28,20,0,24,22,23,21,24,27],
[26,29,27,27,0,22,28,22,28,19],
[27,30,31,29,29,0,29,26,26,22],
[28,26,24,28,23,22,0,22,28,23],
[29,31,26,30,29,25,29,0,30,27],
[24,29,30,27,23,25,23,21,0,26],
[30,29,27,24,32,29,28,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,32,9,23,20,5,24,23,16],
[34,0,32,18,25,27,9,18,21,23],
[19,19,0,22,29,12,20,22,27,22],
[42,33,29,0,25,24,20,27,25,25],
[28,26,22,26,0,28,25,30,30,40],
[31,24,39,27,23,0,21,31,30,34],
[46,42,31,31,26,30,0,42,23,42],
[27,33,29,24,21,20,9,0,23,21],
[28,30,24,26,21,21,28,28,0,31],
[35,28,29,26,11,17,9,30,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,14,22,14,22,7,21,21],
[26,0,33,22,27,22,32,25,20,18],
[27,18,0,19,19,17,20,13,20,17],
[37,29,32,0,38,33,32,30,28,24],
[29,24,32,13,0,17,25,9,17,18],
[37,29,34,18,34,0,34,21,23,28],
[29,19,31,19,26,17,0,16,23,17],
[44,26,38,21,42,30,35,0,22,30],
[30,31,31,23,34,28,28,29,0,16],
[30,33,34,27,33,23,34,21,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,22,27,25,21,14,20,24],
[25,0,16,25,21,21,23,23,20,26],
[32,35,0,30,27,26,27,24,21,24],
[29,26,21,0,26,24,26,24,20,26],
[24,30,24,25,0,28,25,19,21,27],
[26,30,25,27,23,0,27,23,27,25],
[30,28,24,25,26,24,0,22,22,21],
[37,28,27,27,32,28,29,0,25,28],
[31,31,30,31,30,24,29,26,0,30],
[27,25,27,25,24,26,30,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,30,23,34,33,31,28,25,26],
[18,0,27,22,30,24,20,25,26,22],
[21,24,0,29,31,24,28,22,27,24],
[28,29,22,0,33,27,31,24,29,29],
[17,21,20,18,0,18,18,23,18,25],
[18,27,27,24,33,0,30,19,27,24],
[20,31,23,20,33,21,0,21,25,24],
[23,26,29,27,28,32,30,0,28,23],
[26,25,24,22,33,24,26,23,0,22],
[25,29,27,22,26,27,27,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,28,30,24,27,30,26,27],
[23,0,23,30,36,20,30,28,22,26],
[24,28,0,32,30,34,36,26,13,27],
[23,21,19,0,22,14,19,22,19,18],
[21,15,21,29,0,29,34,23,18,19],
[27,31,17,37,22,0,29,18,25,25],
[24,21,15,32,17,22,0,12,13,23],
[21,23,25,29,28,33,39,0,26,31],
[25,29,38,32,33,26,38,25,0,20],
[24,25,24,33,32,26,28,20,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,20,19,27,23,20,20,20,27],
[22,0,18,20,21,15,15,14,17,17],
[31,33,0,23,25,20,23,22,17,24],
[32,31,28,0,25,19,24,26,25,28],
[24,30,26,26,0,23,27,22,21,26],
[28,36,31,32,28,0,31,25,24,29],
[31,36,28,27,24,20,0,26,25,34],
[31,37,29,25,29,26,25,0,29,23],
[31,34,34,26,30,27,26,22,0,25],
[24,34,27,23,25,22,17,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,29,32,33,29,27,25,33],
[21,0,25,20,25,16,23,22,23,24],
[22,26,0,33,30,27,24,27,29,29],
[22,31,18,0,17,26,16,21,25,25],
[19,26,21,34,0,24,28,24,29,33],
[18,35,24,25,27,0,23,30,30,33],
[22,28,27,35,23,28,0,32,26,33],
[24,29,24,30,27,21,19,0,33,33],
[26,28,22,26,22,21,25,18,0,29],
[18,27,22,26,18,18,18,18,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,32,34,27,30,23,24,30,19],
[23,0,29,29,25,25,26,25,26,29],
[19,22,0,19,15,26,14,23,25,18],
[17,22,32,0,20,28,15,22,25,20],
[24,26,36,31,0,29,23,24,22,23],
[21,26,25,23,22,0,16,24,24,20],
[28,25,37,36,28,35,0,30,32,21],
[27,26,28,29,27,27,21,0,32,24],
[21,25,26,26,29,27,19,19,0,27],
[32,22,33,31,28,31,30,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,22,26,28,23,30,21,19],
[24,0,26,23,23,22,15,29,21,16],
[23,25,0,14,26,23,25,26,18,26],
[29,28,37,0,27,29,24,36,32,21],
[25,28,25,24,0,26,18,22,16,26],
[23,29,28,22,25,0,23,24,20,28],
[28,36,26,27,33,28,0,27,23,32],
[21,22,25,15,29,27,24,0,26,21],
[30,30,33,19,35,31,28,25,0,29],
[32,35,25,30,25,23,19,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,37,29,23,29,23,29,37],
[22,0,8,23,23,23,38,8,0,8],
[22,43,0,36,29,36,30,37,42,36],
[14,28,15,0,29,23,30,1,14,14],
[22,28,22,22,0,22,15,22,13,22],
[28,28,15,28,29,0,30,15,14,28],
[22,13,21,21,36,21,0,21,13,21],
[28,43,14,50,29,36,30,0,29,42],
[22,51,9,37,38,37,38,22,0,22],
[14,43,15,37,29,23,30,9,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,19,19,37,13,11,19,19],
[39,0,25,49,51,45,35,35,41,51],
[32,26,0,37,34,47,30,35,19,34],
[32,2,14,0,20,24,34,22,23,38],
[32,0,17,31,0,25,18,11,19,27],
[14,6,4,27,26,0,22,17,19,26],
[38,16,21,17,33,29,0,31,33,43],
[40,16,16,29,40,34,20,0,33,40],
[32,10,32,28,32,32,18,18,0,22],
[32,0,17,13,24,25,8,11,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,24,12,26,23,27,25,18],
[26,0,28,31,26,22,21,30,36,20],
[25,23,0,22,13,21,24,28,24,17],
[27,20,29,0,10,29,23,32,33,25],
[39,25,38,41,0,32,34,41,47,28],
[25,29,30,22,19,0,26,29,31,19],
[28,30,27,28,17,25,0,29,31,17],
[24,21,23,19,10,22,22,0,25,11],
[26,15,27,18,4,20,20,26,0,9],
[33,31,34,26,23,32,34,40,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,26,26,27,24,26,35,32,30],
[31,0,29,25,27,22,31,29,30,30],
[25,22,0,19,22,17,12,27,34,31],
[25,26,32,0,40,30,27,36,32,40],
[24,24,29,11,0,21,27,28,28,27],
[27,29,34,21,30,0,20,38,24,31],
[25,20,39,24,24,31,0,30,34,33],
[16,22,24,15,23,13,21,0,22,24],
[19,21,17,19,23,27,17,29,0,27],
[21,21,20,11,24,20,18,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,28,27,31,23,27,29,31],
[21,0,23,26,25,30,24,32,25,26],
[27,28,0,24,29,29,23,26,26,29],
[23,25,27,0,26,31,21,30,26,26],
[24,26,22,25,0,31,22,26,33,30],
[20,21,22,20,20,0,24,24,22,24],
[28,27,28,30,29,27,0,33,25,31],
[24,19,25,21,25,27,18,0,27,23],
[22,26,25,25,18,29,26,24,0,25],
[20,25,22,25,21,27,20,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,34,31,32,28,33,25,29],
[22,0,21,22,22,22,25,20,25,25],
[24,30,0,29,23,28,29,28,22,33],
[17,29,22,0,24,24,27,27,18,24],
[20,29,28,27,0,30,26,27,28,27],
[19,29,23,27,21,0,24,29,22,23],
[23,26,22,24,25,27,0,22,21,21],
[18,31,23,24,24,22,29,0,18,27],
[26,26,29,33,23,29,30,33,0,31],
[22,26,18,27,24,28,30,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,36,28,31,30,26,30,19,27],
[28,0,33,32,35,31,26,25,24,18],
[15,18,0,22,22,24,18,16,15,16],
[23,19,29,0,33,35,26,25,24,23],
[20,16,29,18,0,25,20,18,16,23],
[21,20,27,16,26,0,26,20,16,20],
[25,25,33,25,31,25,0,26,20,23],
[21,26,35,26,33,31,25,0,29,22],
[32,27,36,27,35,35,31,22,0,24],
[24,33,35,28,28,31,28,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,19,27,31,26,20,32,16],
[30,0,24,24,25,29,21,29,30,21],
[22,27,0,26,24,26,16,19,30,25],
[32,27,25,0,25,28,27,30,33,26],
[24,26,27,26,0,29,23,19,32,21],
[20,22,25,23,22,0,21,24,27,17],
[25,30,35,24,28,30,0,26,34,23],
[31,22,32,21,32,27,25,0,38,26],
[19,21,21,18,19,24,17,13,0,20],
[35,30,26,25,30,34,28,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,32,26,22,23,24,22,23,24],
[32,0,33,34,23,30,26,28,32,28],
[19,18,0,25,18,16,15,22,19,24],
[25,17,26,0,20,22,26,30,23,25],
[29,28,33,31,0,23,26,29,27,26],
[28,21,35,29,28,0,30,20,27,24],
[27,25,36,25,25,21,0,29,25,29],
[29,23,29,21,22,31,22,0,21,19],
[28,19,32,28,24,24,26,30,0,31],
[27,23,27,26,25,27,22,32,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,22,31,31,18,35,20,31],
[20,0,13,22,15,19,0,17,20,15],
[22,38,0,38,38,22,38,22,24,22],
[29,29,13,0,15,15,2,35,20,13],
[20,36,13,36,0,20,36,20,24,20],
[20,32,29,36,31,0,16,36,20,20],
[33,51,13,49,15,35,0,33,35,17],
[16,34,29,16,31,15,18,0,20,18],
[31,31,27,31,27,31,16,31,0,31],
[20,36,29,38,31,31,34,33,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,31,31,35,28,28,25,23,25],
[21,0,26,26,24,23,23,21,21,28],
[20,25,0,18,25,17,14,17,17,18],
[20,25,33,0,29,22,22,28,21,26],
[16,27,26,22,0,23,20,17,22,20],
[23,28,34,29,28,0,19,22,24,26],
[23,28,37,29,31,32,0,24,27,28],
[26,30,34,23,34,29,27,0,24,32],
[28,30,34,30,29,27,24,27,0,30],
[26,23,33,25,31,25,23,19,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,23,32,12,23,6,6,27,22],
[39,0,31,26,22,31,26,26,31,45],
[28,20,0,20,20,27,28,14,10,24],
[19,25,31,0,25,31,19,6,25,25],
[39,29,31,26,0,31,26,14,31,39],
[28,20,24,20,20,0,28,14,20,34],
[45,25,23,32,25,23,0,16,27,35],
[45,25,37,45,37,37,35,0,29,41],
[24,20,41,26,20,31,24,22,0,40],
[29,6,27,26,12,17,16,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,20,18,26,21,24,28,29],
[27,0,23,28,20,29,21,25,24,30],
[31,28,0,27,22,24,25,29,25,31],
[31,23,24,0,17,25,17,30,25,27],
[33,31,29,34,0,25,22,23,33,31],
[25,22,27,26,26,0,29,22,24,28],
[30,30,26,34,29,22,0,25,32,33],
[27,26,22,21,28,29,26,0,25,29],
[23,27,26,26,18,27,19,26,0,19],
[22,21,20,24,20,23,18,22,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,8,28,4,17,22,8,17,42],
[48,0,23,38,37,31,32,34,32,42],
[43,28,0,35,43,38,43,32,18,45],
[23,13,16,0,15,29,31,17,28,38],
[47,14,8,36,0,17,30,14,17,47],
[34,20,13,22,34,0,21,11,25,34],
[29,19,8,20,21,30,0,24,16,44],
[43,17,19,34,37,40,27,0,18,47],
[34,19,33,23,34,26,35,33,0,36],
[9,9,6,13,4,17,7,4,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,24,28,24,28,22,34,23],
[27,0,25,27,29,27,26,20,35,31],
[29,26,0,36,23,33,33,28,34,33],
[27,24,15,0,24,27,29,19,31,21],
[23,22,28,27,0,26,29,23,32,24],
[27,24,18,24,25,0,28,25,26,26],
[23,25,18,22,22,23,0,19,25,24],
[29,31,23,32,28,26,32,0,25,26],
[17,16,17,20,19,25,26,26,0,23],
[28,20,18,30,27,25,27,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,24,30,28,23,24,29,28],
[30,0,28,32,27,28,25,29,28,30],
[23,23,0,23,19,25,27,22,17,16],
[27,19,28,0,28,26,27,24,25,25],
[21,24,32,23,0,28,26,24,25,23],
[23,23,26,25,23,0,22,20,26,24],
[28,26,24,24,25,29,0,23,23,22],
[27,22,29,27,27,31,28,0,25,25],
[22,23,34,26,26,25,28,26,0,26],
[23,21,35,26,28,27,29,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,29,28,29,22,30,29,24],
[29,0,25,30,29,32,26,33,33,25],
[22,26,0,29,24,28,19,29,31,25],
[22,21,22,0,24,23,14,23,24,21],
[23,22,27,27,0,30,20,31,23,28],
[22,19,23,28,21,0,21,29,26,22],
[29,25,32,37,31,30,0,31,27,29],
[21,18,22,28,20,22,20,0,26,24],
[22,18,20,27,28,25,24,25,0,26],
[27,26,26,30,23,29,22,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,24,30,23,25,22,29,20],
[27,0,25,24,30,20,21,20,29,23],
[30,26,0,30,23,20,27,22,25,27],
[27,27,21,0,25,21,17,26,25,22],
[21,21,28,26,0,18,26,18,21,25],
[28,31,31,30,33,0,27,30,27,23],
[26,30,24,34,25,24,0,29,29,21],
[29,31,29,25,33,21,22,0,26,28],
[22,22,26,26,30,24,22,25,0,23],
[31,28,24,29,26,28,30,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,18,14,21,26,21,23,20],
[27,0,29,25,16,23,24,27,26,19],
[26,22,0,21,13,18,23,20,24,18],
[33,26,30,0,22,22,29,22,23,23],
[37,35,38,29,0,24,26,31,31,28],
[30,28,33,29,27,0,30,27,25,30],
[25,27,28,22,25,21,0,29,25,24],
[30,24,31,29,20,24,22,0,26,26],
[28,25,27,28,20,26,26,25,0,28],
[31,32,33,28,23,21,27,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,18,8,15,26,19,28,35],
[26,0,17,21,15,19,23,16,32,32],
[30,34,0,34,23,25,23,31,38,30],
[33,30,17,0,35,29,35,33,40,34],
[43,36,28,16,0,33,46,32,45,38],
[36,32,26,22,18,0,24,22,24,38],
[25,28,28,16,5,27,0,28,34,30],
[32,35,20,18,19,29,23,0,26,30],
[23,19,13,11,6,27,17,25,0,25],
[16,19,21,17,13,13,21,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,20,23,27,39,28,27,47,42],
[0,0,11,19,18,28,1,9,36,19],
[31,40,0,32,15,40,24,40,36,39],
[28,32,19,0,16,27,20,17,29,43],
[24,33,36,35,0,44,25,25,40,35],
[12,23,11,24,7,0,17,16,28,16],
[23,50,27,31,26,34,0,24,36,38],
[24,42,11,34,26,35,27,0,36,35],
[4,15,15,22,11,23,15,15,0,15],
[9,32,12,8,16,35,13,16,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,26,22,20,28,19,15,27],
[25,0,28,27,26,28,27,30,26,27],
[20,23,0,17,19,23,27,19,15,25],
[25,24,34,0,31,33,31,25,23,28],
[29,25,32,20,0,24,25,29,20,28],
[31,23,28,18,27,0,32,24,26,27],
[23,24,24,20,26,19,0,26,22,26],
[32,21,32,26,22,27,25,0,17,21],
[36,25,36,28,31,25,29,34,0,34],
[24,24,26,23,23,24,25,30,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,23,21,26,26,25,21,24],
[26,0,25,24,22,27,27,28,24,22],
[26,26,0,25,27,25,23,26,25,25],
[28,27,26,0,26,31,26,26,25,25],
[30,29,24,25,0,27,29,30,28,24],
[25,24,26,20,24,0,25,27,21,20],
[25,24,28,25,22,26,0,27,26,27],
[26,23,25,25,21,24,24,0,23,20],
[30,27,26,26,23,30,25,28,0,24],
[27,29,26,26,27,31,24,31,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,30,24,29,27,25,32,28],
[23,0,23,18,23,29,23,25,24,31],
[23,28,0,29,19,26,33,27,26,29],
[21,33,22,0,18,27,26,22,24,28],
[27,28,32,33,0,26,32,24,29,36],
[22,22,25,24,25,0,20,28,21,26],
[24,28,18,25,19,31,0,26,27,27],
[26,26,24,29,27,23,25,0,25,26],
[19,27,25,27,22,30,24,26,0,28],
[23,20,22,23,15,25,24,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,25,23,23,25,24,22,23],
[25,0,26,29,21,19,30,27,21,26],
[25,25,0,23,13,21,25,22,23,26],
[26,22,28,0,22,25,25,31,26,28],
[28,30,38,29,0,29,25,25,25,29],
[28,32,30,26,22,0,29,28,30,23],
[26,21,26,26,26,22,0,28,18,25],
[27,24,29,20,26,23,23,0,22,25],
[29,30,28,25,26,21,33,29,0,29],
[28,25,25,23,22,28,26,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,28,25,29,25,30,30,28],
[26,0,22,24,25,29,24,24,26,37],
[22,29,0,25,25,28,22,24,29,34],
[23,27,26,0,31,29,28,24,31,28],
[26,26,26,20,0,29,25,27,31,27],
[22,22,23,22,22,0,22,24,22,28],
[26,27,29,23,26,29,0,26,32,31],
[21,27,27,27,24,27,25,0,26,33],
[21,25,22,20,20,29,19,25,0,26],
[23,14,17,23,24,23,20,18,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,21,26,20,18,22,24,38],
[20,0,30,19,31,24,24,22,20,34],
[23,21,0,23,30,30,12,28,28,31],
[30,32,28,0,34,32,18,23,25,33],
[25,20,21,17,0,31,10,9,18,26],
[31,27,21,19,20,0,13,18,19,28],
[33,27,39,33,41,38,0,28,24,40],
[29,29,23,28,42,33,23,0,29,27],
[27,31,23,26,33,32,27,22,0,27],
[13,17,20,18,25,23,11,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,28,27,29,27,22,27,32],
[22,0,28,26,26,26,27,27,31,35],
[23,23,0,25,25,22,22,25,23,27],
[23,25,26,0,23,25,22,30,27,35],
[24,25,26,28,0,24,27,22,27,33],
[22,25,29,26,27,0,26,24,30,32],
[24,24,29,29,24,25,0,29,31,32],
[29,24,26,21,29,27,22,0,22,30],
[24,20,28,24,24,21,20,29,0,28],
[19,16,24,16,18,19,19,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,36,38,33,18,29,34,48],
[21,0,28,33,28,27,22,12,37,35],
[22,23,0,31,33,28,28,22,35,40],
[15,18,20,0,24,20,18,18,21,33],
[13,23,18,27,0,27,21,24,33,37],
[18,24,23,31,24,0,19,24,34,35],
[33,29,23,33,30,32,0,29,26,35],
[22,39,29,33,27,27,22,0,32,39],
[17,14,16,30,18,17,25,19,0,25],
[3,16,11,18,14,16,16,12,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,17,29,24,22,21,16,21],
[37,0,22,29,31,31,30,20,26,32],
[34,29,0,22,32,32,23,20,26,27],
[34,22,29,0,34,30,26,18,25,24],
[22,20,19,17,0,23,12,11,10,21],
[27,20,19,21,28,0,30,21,12,22],
[29,21,28,25,39,21,0,34,24,29],
[30,31,31,33,40,30,17,0,24,27],
[35,25,25,26,41,39,27,27,0,32],
[30,19,24,27,30,29,22,24,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,25,27,23,27,23,25,30],
[29,0,27,26,27,21,23,30,24,24],
[25,24,0,27,18,23,26,30,23,23],
[26,25,24,0,20,27,28,26,21,29],
[24,24,33,31,0,23,24,28,20,28],
[28,30,28,24,28,0,24,27,31,33],
[24,28,25,23,27,27,0,27,28,30],
[28,21,21,25,23,24,24,0,20,23],
[26,27,28,30,31,20,23,31,0,31],
[21,27,28,22,23,18,21,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,34,23,19,24,17,19,17],
[28,0,15,19,16,20,18,18,11,17],
[29,36,0,30,22,18,24,30,16,26],
[17,32,21,0,17,22,28,26,17,30],
[28,35,29,34,0,24,29,34,29,24],
[32,31,33,29,27,0,22,23,16,23],
[27,33,27,23,22,29,0,28,27,24],
[34,33,21,25,17,28,23,0,15,20],
[32,40,35,34,22,35,24,36,0,25],
[34,34,25,21,27,28,27,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,26,23,26,22,26,25,26],
[23,0,28,23,27,24,19,27,25,24],
[27,23,0,28,29,29,23,25,23,26],
[25,28,23,0,29,30,27,27,26,28],
[28,24,22,22,0,25,22,27,20,25],
[25,27,22,21,26,0,24,27,29,28],
[29,32,28,24,29,27,0,29,24,27],
[25,24,26,24,24,24,22,0,23,19],
[26,26,28,25,31,22,27,28,0,27],
[25,27,25,23,26,23,24,32,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,35,45,30,25,32,29,30],
[21,0,27,35,46,31,28,22,29,29],
[24,24,0,27,47,34,27,24,35,25],
[16,16,24,0,36,27,27,24,26,22],
[6,5,4,15,0,16,11,7,10,14],
[21,20,17,24,35,0,21,23,20,18],
[26,23,24,24,40,30,0,21,22,25],
[19,29,27,27,44,28,30,0,31,37],
[22,22,16,25,41,31,29,20,0,29],
[21,22,26,29,37,33,26,14,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,26,19,21,29,27,25,24,21],
[18,0,31,14,23,18,25,17,24,16],
[25,20,0,19,19,25,25,21,29,23],
[32,37,32,0,22,32,36,24,30,31],
[30,28,32,29,0,28,27,28,26,23],
[22,33,26,19,23,0,31,22,32,20],
[24,26,26,15,24,20,0,20,29,23],
[26,34,30,27,23,29,31,0,35,31],
[27,27,22,21,25,19,22,16,0,28],
[30,35,28,20,28,31,28,20,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,23,35,23,26,39,51,39,39],
[12,0,35,25,12,12,25,22,12,0],
[28,16,0,41,28,28,28,28,28,16],
[16,26,10,0,26,26,26,26,26,26],
[28,39,23,25,0,38,51,38,26,26],
[25,39,23,25,13,0,51,35,23,13],
[12,26,23,25,0,0,0,22,0,0],
[0,29,23,25,13,16,29,0,16,29],
[12,39,23,25,25,28,51,35,0,29],
[12,51,35,25,25,38,51,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,37,21,20,8,13,19,11,29],
[21,0,33,32,26,16,18,28,12,22],
[14,18,0,11,17,12,13,23,8,26],
[30,19,40,0,21,17,13,23,9,22],
[31,25,34,30,0,23,19,30,28,22],
[43,35,39,34,28,0,30,32,22,34],
[38,33,38,38,32,21,0,32,26,33],
[32,23,28,28,21,19,19,0,9,23],
[40,39,43,42,23,29,25,42,0,33],
[22,29,25,29,29,17,18,28,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,19,24,31,15,20,20,28],
[34,0,30,29,30,26,20,29,25,28],
[35,21,0,27,31,27,29,31,24,30],
[32,22,24,0,26,32,21,30,23,33],
[27,21,20,25,0,25,21,20,20,24],
[20,25,24,19,26,0,20,27,23,30],
[36,31,22,30,30,31,0,27,27,29],
[31,22,20,21,31,24,24,0,22,24],
[31,26,27,28,31,28,24,29,0,33],
[23,23,21,18,27,21,22,27,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,29,29,29,25,23,25,22],
[26,0,27,25,27,22,23,21,26,23],
[22,24,0,26,28,29,23,23,24,15],
[22,26,25,0,29,29,30,21,30,24],
[22,24,23,22,0,26,19,20,20,20],
[22,29,22,22,25,0,23,18,24,22],
[26,28,28,21,32,28,0,26,24,27],
[28,30,28,30,31,33,25,0,25,29],
[26,25,27,21,31,27,27,26,0,21],
[29,28,36,27,31,29,24,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,16,9,38,33,26,22,35,33],
[15,0,14,15,26,37,23,17,20,11],
[35,37,0,28,29,33,14,28,28,34],
[42,36,23,0,38,33,33,22,47,33],
[13,25,22,13,0,25,26,19,18,18],
[18,14,18,18,26,0,26,26,23,14],
[25,28,37,18,25,25,0,14,39,28],
[29,34,23,29,32,25,37,0,30,25],
[16,31,23,4,33,28,12,21,0,28],
[18,40,17,18,33,37,23,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,28,27,24,35,19,25,23],
[25,0,21,24,14,27,33,21,19,22],
[20,30,0,33,18,28,30,26,19,21],
[23,27,18,0,17,24,30,23,19,20],
[24,37,33,34,0,33,34,26,29,26],
[27,24,23,27,18,0,31,21,26,20],
[16,18,21,21,17,20,0,15,19,19],
[32,30,25,28,25,30,36,0,27,28],
[26,32,32,32,22,25,32,24,0,28],
[28,29,30,31,25,31,32,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,14,17,9,14,11,17,16],
[37,0,28,26,29,23,22,26,26,22],
[35,23,0,28,23,27,29,21,19,22],
[37,25,23,0,25,18,19,27,27,25],
[34,22,28,26,0,26,31,27,33,20],
[42,28,24,33,25,0,22,21,28,27],
[37,29,22,32,20,29,0,23,22,16],
[40,25,30,24,24,30,28,0,28,26],
[34,25,32,24,18,23,29,23,0,23],
[35,29,29,26,31,24,35,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,51,38,27,22,46,27,31],
[0,0,20,18,5,17,12,10,10,5],
[5,31,0,18,5,18,22,10,11,21],
[0,33,33,0,11,17,21,17,10,20],
[13,46,46,40,0,23,17,46,39,40],
[24,34,33,34,28,0,38,33,34,38],
[29,39,29,30,34,13,0,39,39,34],
[5,41,41,34,5,18,12,0,15,21],
[24,41,40,41,12,17,12,36,0,34],
[20,46,30,31,11,13,17,30,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,16,26,9,11,27,24,18,6],
[24,0,11,26,13,18,25,30,23,19],
[35,40,0,36,21,22,44,43,37,30],
[25,25,15,0,9,13,27,21,25,16],
[42,38,30,42,0,23,37,41,30,26],
[40,33,29,38,28,0,36,33,29,25],
[24,26,7,24,14,15,0,23,19,11],
[27,21,8,30,10,18,28,0,24,15],
[33,28,14,26,21,22,32,27,0,23],
[45,32,21,35,25,26,40,36,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,25,22,27,19,22,25,21],
[33,0,28,26,22,32,28,26,26,32],
[28,23,0,22,24,23,22,21,27,28],
[26,25,29,0,27,27,27,20,28,29],
[29,29,27,24,0,25,24,21,24,26],
[24,19,28,24,26,0,28,25,24,28],
[32,23,29,24,27,23,0,25,24,32],
[29,25,30,31,30,26,26,0,32,32],
[26,25,24,23,27,27,27,19,0,31],
[30,19,23,22,25,23,19,19,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,27,0,48,24,24,0,48,0],
[3,0,3,0,24,3,0,3,51,3],
[24,48,0,24,24,48,48,24,48,24],
[51,51,27,0,51,27,51,27,51,3],
[3,27,27,0,0,27,24,3,51,3],
[27,48,3,24,24,0,48,24,48,27],
[27,51,3,0,27,3,0,3,51,3],
[51,48,27,24,48,27,48,0,51,27],
[3,0,3,0,0,3,0,0,0,3],
[51,48,27,48,48,24,48,24,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,33,27,26,32,33,23,21],
[31,0,23,29,34,24,36,24,36,40],
[36,28,0,22,27,21,29,27,34,26],
[18,22,29,0,27,27,39,24,19,29],
[24,17,24,24,0,27,39,29,36,21],
[25,27,30,24,24,0,35,30,21,30],
[19,15,22,12,12,16,0,16,18,22],
[18,27,24,27,22,21,35,0,12,35],
[28,15,17,32,15,30,33,39,0,28],
[30,11,25,22,30,21,29,16,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,18,21,17,15,13,20,24],
[36,0,31,24,26,25,23,29,23,28],
[35,20,0,32,26,29,26,27,31,29],
[33,27,19,0,27,30,24,19,25,32],
[30,25,25,24,0,35,24,25,29,39],
[34,26,22,21,16,0,32,25,24,29],
[36,28,25,27,27,19,0,24,26,25],
[38,22,24,32,26,26,27,0,29,33],
[31,28,20,26,22,27,25,22,0,28],
[27,23,22,19,12,22,26,18,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,29,29,25,30,29,34,32],
[22,0,31,30,29,33,26,27,25,23],
[26,20,0,31,30,28,31,26,32,31],
[22,21,20,0,22,26,26,22,20,22],
[22,22,21,29,0,23,24,19,26,22],
[26,18,23,25,28,0,21,24,24,25],
[21,25,20,25,27,30,0,20,25,26],
[22,24,25,29,32,27,31,0,27,27],
[17,26,19,31,25,27,26,24,0,25],
[19,28,20,29,29,26,25,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,26,27,30,24,33,27,26,29],
[20,0,26,22,22,27,32,20,28,25],
[25,25,0,25,33,26,23,19,27,18],
[24,29,26,0,32,28,34,23,29,27],
[21,29,18,19,0,16,27,22,24,20],
[27,24,25,23,35,0,27,24,28,28],
[18,19,28,17,24,24,0,19,25,20],
[24,31,32,28,29,27,32,0,28,29],
[25,23,24,22,27,23,26,23,0,28],
[22,26,33,24,31,23,31,22,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,31,24,6,21,23,20,12],
[32,0,25,24,36,32,25,24,38,29],
[27,26,0,25,25,22,31,20,20,23],
[20,27,26,0,28,19,17,22,22,17],
[27,15,26,23,0,11,28,16,20,16],
[45,19,29,32,40,0,33,28,27,30],
[30,26,20,34,23,18,0,23,21,26],
[28,27,31,29,35,23,28,0,24,27],
[31,13,31,29,31,24,30,27,0,20],
[39,22,28,34,35,21,25,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,34,33,22,26,26,25,15,29],
[29,0,36,34,27,29,31,28,38,22],
[17,15,0,25,13,26,21,24,21,13],
[18,17,26,0,17,20,17,19,18,28],
[29,24,38,34,0,37,40,36,37,27],
[25,22,25,31,14,0,17,29,15,21],
[25,20,30,34,11,34,0,33,29,19],
[26,23,27,32,15,22,18,0,12,22],
[36,13,30,33,14,36,22,39,0,28],
[22,29,38,23,24,30,32,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,21,25,25,26,32,25,26],
[22,0,26,20,26,18,19,24,21,22],
[26,25,0,15,26,21,24,30,20,28],
[30,31,36,0,27,25,27,33,26,31],
[26,25,25,24,0,21,20,25,26,28],
[26,33,30,26,30,0,25,31,26,30],
[25,32,27,24,31,26,0,29,24,23],
[19,27,21,18,26,20,22,0,24,25],
[26,30,31,25,25,25,27,27,0,27],
[25,29,23,20,23,21,28,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,26,25,17,23,25,29,25],
[32,0,28,27,27,23,28,30,29,26],
[29,23,0,26,22,22,27,28,25,30],
[25,24,25,0,30,18,21,32,31,32],
[26,24,29,21,0,27,23,30,25,27],
[34,28,29,33,24,0,27,34,27,33],
[28,23,24,30,28,24,0,29,33,26],
[26,21,23,19,21,17,22,0,23,29],
[22,22,26,20,26,24,18,28,0,29],
[26,25,21,19,24,18,25,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,19,23,29,26,24,23,21,28],
[21,0,18,13,24,16,18,22,20,26],
[32,33,0,24,34,33,27,34,34,14],
[28,38,27,0,30,31,22,32,20,34],
[22,27,17,21,0,21,20,19,20,22],
[25,35,18,20,30,0,19,26,23,13],
[27,33,24,29,31,32,0,31,27,27],
[28,29,17,19,32,25,20,0,20,23],
[30,31,17,31,31,28,24,31,0,25],
[23,25,37,17,29,38,24,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,20,25,25,21,18,19,24,20],
[32,0,30,27,35,29,20,35,33,23],
[31,21,0,28,27,27,18,24,25,27],
[26,24,23,0,32,23,20,25,28,22],
[26,16,24,19,0,21,17,19,20,24],
[30,22,24,28,30,0,21,28,25,26],
[33,31,33,31,34,30,0,25,30,30],
[32,16,27,26,32,23,26,0,27,26],
[27,18,26,23,31,26,21,24,0,23],
[31,28,24,29,27,25,21,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,29,21,37,23,23,30,23],
[26,0,27,33,26,35,26,15,22,31],
[28,24,0,26,26,30,26,20,24,26],
[22,18,25,0,15,24,21,20,21,20],
[30,25,25,36,0,33,30,28,32,30],
[14,16,21,27,18,0,12,14,23,18],
[28,25,25,30,21,39,0,21,29,25],
[28,36,31,31,23,37,30,0,24,32],
[21,29,27,30,19,28,22,27,0,26],
[28,20,25,31,21,33,26,19,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,15,23,21,32,26,21,22,12],
[28,0,27,26,26,32,23,22,25,21],
[36,24,0,29,30,36,21,26,24,25],
[28,25,22,0,28,34,27,22,26,22],
[30,25,21,23,0,31,23,25,24,26],
[19,19,15,17,20,0,26,18,26,17],
[25,28,30,24,28,25,0,19,23,22],
[30,29,25,29,26,33,32,0,33,23],
[29,26,27,25,27,25,28,18,0,23],
[39,30,26,29,25,34,29,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,13,25,22,20,17,24,22],
[30,0,26,23,29,22,37,20,25,28],
[29,25,0,30,39,26,32,29,35,18],
[38,28,21,0,31,26,23,12,29,17],
[26,22,12,20,0,14,21,10,17,13],
[29,29,25,25,37,0,23,13,15,21],
[31,14,19,28,30,28,0,17,17,30],
[34,31,22,39,41,38,34,0,30,22],
[27,26,16,22,34,36,34,21,0,27],
[29,23,33,34,38,30,21,29,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,30,28,29,23,24,27,23],
[24,0,29,29,27,28,24,24,30,23],
[28,22,0,27,30,28,23,30,27,26],
[21,22,24,0,22,27,20,28,27,24],
[23,24,21,29,0,27,27,26,29,22],
[22,23,23,24,24,0,21,25,28,25],
[28,27,28,31,24,30,0,30,29,25],
[27,27,21,23,25,26,21,0,27,23],
[24,21,24,24,22,23,22,24,0,19],
[28,28,25,27,29,26,26,28,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,25,21,23,21,22,25,25],
[26,0,20,27,24,18,22,19,23,21],
[29,31,0,25,22,25,25,23,23,28],
[26,24,26,0,19,20,19,23,23,23],
[30,27,29,32,0,21,21,22,24,27],
[28,33,26,31,30,0,27,25,28,32],
[30,29,26,32,30,24,0,30,27,28],
[29,32,28,28,29,26,21,0,24,30],
[26,28,28,28,27,23,24,27,0,22],
[26,30,23,28,24,19,23,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,25,32,35,28,34,28,32],
[24,0,24,28,28,32,25,29,23,33],
[24,27,0,26,31,31,27,32,26,35],
[26,23,25,0,27,32,28,32,28,30],
[19,23,20,24,0,26,28,27,26,27],
[16,19,20,19,25,0,16,21,20,26],
[23,26,24,23,23,35,0,31,26,30],
[17,22,19,19,24,30,20,0,19,24],
[23,28,25,23,25,31,25,32,0,29],
[19,18,16,21,24,25,21,27,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,24,23,30,26,30,21,27],
[24,0,22,21,25,27,19,28,27,23],
[25,29,0,27,21,27,28,26,31,26],
[27,30,24,0,23,27,24,28,29,31],
[28,26,30,28,0,27,24,30,26,24],
[21,24,24,24,24,0,22,23,22,25],
[25,32,23,27,27,29,0,26,26,24],
[21,23,25,23,21,28,25,0,26,23],
[30,24,20,22,25,29,25,25,0,23],
[24,28,25,20,27,26,27,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,34,21,23,35,36,27,19,25],
[29,0,32,23,30,32,26,33,23,29],
[17,19,0,14,19,23,20,23,14,18],
[30,28,37,0,25,34,33,36,27,23],
[28,21,32,26,0,33,31,27,24,27],
[16,19,28,17,18,0,28,24,18,22],
[15,25,31,18,20,23,0,23,17,20],
[24,18,28,15,24,27,28,0,20,23],
[32,28,37,24,27,33,34,31,0,32],
[26,22,33,28,24,29,31,28,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,30,20,24,26,30,19,17],
[24,0,18,24,23,18,30,29,20,20],
[29,33,0,33,24,22,29,29,26,20],
[21,27,18,0,23,23,23,31,22,17],
[31,28,27,28,0,28,30,27,24,29],
[27,33,29,28,23,0,28,33,23,23],
[25,21,22,28,21,23,0,25,17,18],
[21,22,22,20,24,18,26,0,22,19],
[32,31,25,29,27,28,34,29,0,32],
[34,31,31,34,22,28,33,32,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,21,17,29,30,15,20,21,27],
[36,0,30,32,26,39,25,31,35,32],
[30,21,0,21,19,27,15,24,30,24],
[34,19,30,0,32,35,27,32,30,31],
[22,25,32,19,0,32,20,17,25,28],
[21,12,24,16,19,0,13,20,15,21],
[36,26,36,24,31,38,0,29,31,29],
[31,20,27,19,34,31,22,0,30,28],
[30,16,21,21,26,36,20,21,0,27],
[24,19,27,20,23,30,22,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,29,27,24,32,19,24,30],
[28,0,19,25,27,23,29,19,27,26],
[24,32,0,32,28,26,29,28,28,31],
[22,26,19,0,22,22,27,20,22,27],
[24,24,23,29,0,23,35,22,26,32],
[27,28,25,29,28,0,30,20,28,29],
[19,22,22,24,16,21,0,15,24,29],
[32,32,23,31,29,31,36,0,27,33],
[27,24,23,29,25,23,27,24,0,27],
[21,25,20,24,19,22,22,18,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,30,28,22,32,32,21,30],
[28,0,23,32,28,29,31,29,30,33],
[27,28,0,31,24,23,27,30,28,26],
[21,19,20,0,24,20,27,24,28,25],
[23,23,27,27,0,22,25,25,22,25],
[29,22,28,31,29,0,32,28,28,30],
[19,20,24,24,26,19,0,24,24,28],
[19,22,21,27,26,23,27,0,28,34],
[30,21,23,23,29,23,27,23,0,32],
[21,18,25,26,26,21,23,17,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,30,14,20,25,28,26,26],
[30,0,35,39,28,24,33,40,31,24],
[25,16,0,29,14,21,23,31,25,21],
[21,12,22,0,23,18,26,29,25,25],
[37,23,37,28,0,28,38,34,36,32],
[31,27,30,33,23,0,33,36,29,22],
[26,18,28,25,13,18,0,25,23,16],
[23,11,20,22,17,15,26,0,26,16],
[25,20,26,26,15,22,28,25,0,17],
[25,27,30,26,19,29,35,35,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,23,17,20,31,22,20,25],
[28,0,23,24,14,19,22,25,24,25],
[25,28,0,25,22,24,34,27,20,33],
[28,27,26,0,26,27,24,29,27,25],
[34,37,29,25,0,28,30,36,29,33],
[31,32,27,24,23,0,27,26,23,32],
[20,29,17,27,21,24,0,24,24,27],
[29,26,24,22,15,25,27,0,24,23],
[31,27,31,24,22,28,27,27,0,28],
[26,26,18,26,18,19,24,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,15,22,23,23,20,19,17],
[26,0,32,31,29,36,27,19,23,26],
[26,19,0,25,23,24,24,28,24,19],
[36,20,26,0,28,30,26,26,17,16],
[29,22,28,23,0,26,23,12,12,13],
[28,15,27,21,25,0,14,13,23,17],
[28,24,27,25,28,37,0,14,25,34],
[31,32,23,25,39,38,37,0,30,27],
[32,28,27,34,39,28,26,21,0,33],
[34,25,32,35,38,34,17,24,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,51,27,27,27,19,27,27],
[32,0,24,32,32,32,32,27,48,35],
[32,27,0,32,32,32,8,27,48,11],
[0,19,19,0,16,3,3,19,16,19],
[24,19,19,35,0,27,3,19,43,3],
[24,19,19,48,24,0,3,19,48,27],
[24,19,43,48,48,48,0,43,48,51],
[32,24,24,32,32,32,8,0,48,8],
[24,3,3,35,8,3,3,3,0,3],
[24,16,40,32,48,24,0,43,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,24,25,20,23,23,24,23],
[31,0,25,28,27,26,32,26,26,22],
[27,26,0,26,23,22,23,29,31,24],
[27,23,25,0,21,26,23,26,22,24],
[26,24,28,30,0,24,24,31,30,23],
[31,25,29,25,27,0,24,25,27,28],
[28,19,28,28,27,27,0,22,27,23],
[28,25,22,25,20,26,29,0,24,24],
[27,25,20,29,21,24,24,27,0,24],
[28,29,27,27,28,23,28,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,24,27,32,25,29,20,27],
[19,0,22,16,26,24,24,18,15,21],
[21,29,0,25,30,30,26,19,19,26],
[27,35,26,0,36,33,30,23,26,36],
[24,25,21,15,0,26,19,22,18,24],
[19,27,21,18,25,0,21,17,15,21],
[26,27,25,21,32,30,0,23,17,27],
[22,33,32,28,29,34,28,0,25,32],
[31,36,32,25,33,36,34,26,0,34],
[24,30,25,15,27,30,24,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,22,25,23,17,27,19,27],
[28,0,22,26,22,25,23,26,25,25],
[26,29,0,24,24,24,23,28,23,26],
[29,25,27,0,30,26,26,28,23,29],
[26,29,27,21,0,26,28,29,26,29],
[28,26,27,25,25,0,27,31,26,32],
[34,28,28,25,23,24,0,30,23,26],
[24,25,23,23,22,20,21,0,19,23],
[32,26,28,28,25,25,28,32,0,33],
[24,26,25,22,22,19,25,28,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,23,21,25,25,34,24,17],
[21,0,21,20,21,12,18,16,20,15],
[25,30,0,27,27,25,30,23,29,26],
[28,31,24,0,33,26,25,23,27,22],
[30,30,24,18,0,31,25,25,28,23],
[26,39,26,25,20,0,28,25,27,21],
[26,33,21,26,26,23,0,24,28,20],
[17,35,28,28,26,26,27,0,33,26],
[27,31,22,24,23,24,23,18,0,22],
[34,36,25,29,28,30,31,25,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,30,31,29,16,30,23,23],
[26,0,26,34,24,32,28,37,25,26],
[28,25,0,29,28,30,24,38,27,26],
[21,17,22,0,22,24,23,25,17,21],
[20,27,23,29,0,30,24,33,28,30],
[22,19,21,27,21,0,21,27,18,24],
[35,23,27,28,27,30,0,35,28,31],
[21,14,13,26,18,24,16,0,20,18],
[28,26,24,34,23,33,23,31,0,25],
[28,25,25,30,21,27,20,33,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,22,15,25,28,28,28,23],
[30,0,30,26,20,29,28,32,29,29],
[29,21,0,24,18,25,23,30,32,27],
[29,25,27,0,27,31,30,29,33,26],
[36,31,33,24,0,28,30,29,35,33],
[26,22,26,20,23,0,31,32,32,26],
[23,23,28,21,21,20,0,30,27,21],
[23,19,21,22,22,19,21,0,20,21],
[23,22,19,18,16,19,24,31,0,21],
[28,22,24,25,18,25,30,30,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,30,27,29,30,30,25,27],
[28,0,23,32,24,29,27,35,24,30],
[27,28,0,31,23,27,28,30,25,32],
[21,19,20,0,20,25,20,22,20,24],
[24,27,28,31,0,34,29,32,28,22],
[22,22,24,26,17,0,24,26,26,21],
[21,24,23,31,22,27,0,27,29,25],
[21,16,21,29,19,25,24,0,22,20],
[26,27,26,31,23,25,22,29,0,27],
[24,21,19,27,29,30,26,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,34,24,34,34,37,33,23,42],
[32,0,38,24,33,28,34,27,18,36],
[17,13,0,14,18,18,21,9,8,18],
[27,27,37,0,20,30,28,20,22,32],
[17,18,33,31,0,30,30,22,22,34],
[17,23,33,21,21,0,25,21,14,27],
[14,17,30,23,21,26,0,18,10,30],
[18,24,42,31,29,30,33,0,27,34],
[28,33,43,29,29,37,41,24,0,39],
[9,15,33,19,17,24,21,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,30,27,24,28,28,25,24],
[26,0,28,26,19,24,22,21,24,26],
[23,23,0,28,22,26,28,24,28,27],
[21,25,23,0,24,26,24,23,29,28],
[24,32,29,27,0,26,30,27,32,26],
[27,27,25,25,25,0,29,25,30,28],
[23,29,23,27,21,22,0,29,27,27],
[23,30,27,28,24,26,22,0,27,27],
[26,27,23,22,19,21,24,24,0,27],
[27,25,24,23,25,23,24,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,18,28,24,27,22,20,22,26],
[25,0,20,23,19,21,23,26,28,28],
[33,31,0,31,23,34,29,27,25,31],
[23,28,20,0,22,24,21,22,20,21],
[27,32,28,29,0,29,27,28,28,24],
[24,30,17,27,22,0,24,25,19,30],
[29,28,22,30,24,27,0,29,27,29],
[31,25,24,29,23,26,22,0,19,24],
[29,23,26,31,23,32,24,32,0,33],
[25,23,20,30,27,21,22,27,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,20,12,23,23,21,20,20],
[26,0,23,22,27,24,25,25,22,24],
[28,28,0,20,19,28,24,20,21,21],
[31,29,31,0,31,27,29,29,26,25],
[39,24,32,20,0,25,24,26,27,26],
[28,27,23,24,26,0,28,21,22,24],
[28,26,27,22,27,23,0,26,20,22],
[30,26,31,22,25,30,25,0,22,21],
[31,29,30,25,24,29,31,29,0,29],
[31,27,30,26,25,27,29,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,27,30,25,27,28,28,22,25],
[14,0,20,23,24,21,15,23,16,24],
[24,31,0,23,28,25,20,24,21,22],
[21,28,28,0,26,22,29,21,20,23],
[26,27,23,25,0,26,21,31,16,26],
[24,30,26,29,25,0,22,23,25,21],
[23,36,31,22,30,29,0,21,22,21],
[23,28,27,30,20,28,30,0,21,24],
[29,35,30,31,35,26,29,30,0,25],
[26,27,29,28,25,30,30,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,21,25,34,24,40,32,26,41],
[12,0,7,15,18,7,17,31,25,34],
[30,44,0,22,26,23,36,36,32,39],
[26,36,29,0,21,26,33,39,29,33],
[17,33,25,30,0,32,32,30,26,32],
[27,44,28,25,19,0,40,37,33,43],
[11,34,15,18,19,11,0,34,27,36],
[19,20,15,12,21,14,17,0,20,20],
[25,26,19,22,25,18,24,31,0,33],
[10,17,12,18,19,8,15,31,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,23,28,24,34,30,31,37,30],
[15,0,17,21,17,23,20,18,40,17],
[28,34,0,39,33,36,27,22,31,33],
[23,30,12,0,24,25,31,20,32,24],
[27,34,18,27,0,32,33,25,37,29],
[17,28,15,26,19,0,24,23,37,21],
[21,31,24,20,18,27,0,20,30,32],
[20,33,29,31,26,28,31,0,32,30],
[14,11,20,19,14,14,21,19,0,20],
[21,34,18,27,22,30,19,21,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,19,17,20,15,20,15,18],
[37,0,23,32,28,24,21,27,25,26],
[39,28,0,36,33,25,26,29,30,33],
[32,19,15,0,21,18,23,24,11,23],
[34,23,18,30,0,22,20,30,23,26],
[31,27,26,33,29,0,18,31,30,27],
[36,30,25,28,31,33,0,32,30,23],
[31,24,22,27,21,20,19,0,11,28],
[36,26,21,40,28,21,21,40,0,30],
[33,25,18,28,25,24,28,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,28,31,25,26,32,27,25,23],
[33,0,24,29,35,30,29,29,26,32],
[23,27,0,26,29,26,31,20,27,26],
[20,22,25,0,21,22,30,21,24,29],
[26,16,22,30,0,28,30,23,23,26],
[25,21,25,29,23,0,27,26,29,20],
[19,22,20,21,21,24,0,23,22,28],
[24,22,31,30,28,25,28,0,28,27],
[26,25,24,27,28,22,29,23,0,19],
[28,19,25,22,25,31,23,24,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,21,20,21,23,21,31,19],
[30,0,32,27,21,26,29,24,31,23],
[27,19,0,18,24,14,21,18,24,24],
[30,24,33,0,25,25,30,24,31,33],
[31,30,27,26,0,27,22,21,33,25],
[30,25,37,26,24,0,36,28,35,31],
[28,22,30,21,29,15,0,20,31,23],
[30,27,33,27,30,23,31,0,28,26],
[20,20,27,20,18,16,20,23,0,18],
[32,28,27,18,26,20,28,25,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,32,25,32,24,30,33,37,32],
[15,0,21,21,23,21,19,21,26,30],
[19,30,0,21,29,20,23,28,25,32],
[26,30,30,0,24,19,22,27,30,33],
[19,28,22,27,0,22,26,25,27,30],
[27,30,31,32,29,0,25,31,32,35],
[21,32,28,29,25,26,0,26,28,30],
[18,30,23,24,26,20,25,0,23,30],
[14,25,26,21,24,19,23,28,0,24],
[19,21,19,18,21,16,21,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,28,28,25,25,29,23,23,27],
[32,0,28,27,24,23,30,28,25,32],
[23,23,0,26,25,23,27,23,24,24],
[23,24,25,0,24,23,28,23,24,21],
[26,27,26,27,0,24,30,24,25,26],
[26,28,28,28,27,0,24,28,26,28],
[22,21,24,23,21,27,0,22,25,28],
[28,23,28,28,27,23,29,0,26,24],
[28,26,27,27,26,25,26,25,0,24],
[24,19,27,30,25,23,23,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,17,25,32,27,34,32,37,24],
[18,0,13,16,14,29,22,21,13,12],
[34,38,0,26,30,31,24,25,29,20],
[26,35,25,0,26,33,31,36,24,11],
[19,37,21,25,0,29,20,33,28,22],
[24,22,20,18,22,0,21,29,19,23],
[17,29,27,20,31,30,0,30,15,18],
[19,30,26,15,18,22,21,0,13,5],
[14,38,22,27,23,32,36,38,0,31],
[27,39,31,40,29,28,33,46,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,19,24,28,23,27,23,29],
[25,0,17,15,30,20,18,22,16,31],
[24,34,0,24,36,25,26,31,30,34],
[32,36,27,0,30,28,31,25,36,35],
[27,21,15,21,0,24,18,22,25,21],
[23,31,26,23,27,0,26,26,21,31],
[28,33,25,20,33,25,0,26,18,26],
[24,29,20,26,29,25,25,0,24,33],
[28,35,21,15,26,30,33,27,0,35],
[22,20,17,16,30,20,25,18,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,26,24,22,28,25,27,28],
[25,0,21,27,22,19,26,33,25,26],
[31,30,0,27,24,28,26,31,25,31],
[25,24,24,0,20,22,19,31,22,23],
[27,29,27,31,0,23,27,28,27,26],
[29,32,23,29,28,0,27,30,28,33],
[23,25,25,32,24,24,0,32,25,30],
[26,18,20,20,23,21,19,0,12,30],
[24,26,26,29,24,23,26,39,0,24],
[23,25,20,28,25,18,21,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,22,27,23,27,28,30,28],
[26,0,26,25,24,22,23,28,28,25],
[21,25,0,23,22,20,21,25,24,25],
[29,26,28,0,27,24,25,27,28,27],
[24,27,29,24,0,18,23,23,27,24],
[28,29,31,27,33,0,24,31,32,32],
[24,28,30,26,28,27,0,27,27,28],
[23,23,26,24,28,20,24,0,27,25],
[21,23,27,23,24,19,24,24,0,22],
[23,26,26,24,27,19,23,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,18,25,27,15,20,12,24],
[27,0,24,28,27,27,22,27,17,31],
[26,27,0,24,28,35,23,14,23,22],
[33,23,27,0,29,32,17,30,29,33],
[26,24,23,22,0,29,22,20,20,28],
[24,24,16,19,22,0,25,25,15,28],
[36,29,28,34,29,26,0,30,22,31],
[31,24,37,21,31,26,21,0,28,31],
[39,34,28,22,31,36,29,23,0,34],
[27,20,29,18,23,23,20,20,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,23,33,27,20,29,30,27],
[22,0,20,26,27,26,25,23,26,23],
[24,31,0,23,27,34,27,25,29,30],
[28,25,28,0,30,33,27,26,25,27],
[18,24,24,21,0,21,18,22,21,25],
[24,25,17,18,30,0,18,22,23,25],
[31,26,24,24,33,33,0,27,29,27],
[22,28,26,25,29,29,24,0,23,28],
[21,25,22,26,30,28,22,28,0,30],
[24,28,21,24,26,26,24,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,21,30,23,26,23,22,21,25],
[22,0,24,27,29,21,30,26,22,24],
[30,27,0,33,30,28,31,26,25,28],
[21,24,18,0,26,21,26,22,19,22],
[28,22,21,25,0,29,27,22,27,25],
[25,30,23,30,22,0,29,23,20,26],
[28,21,20,25,24,22,0,17,23,26],
[29,25,25,29,29,28,34,0,24,29],
[30,29,26,32,24,31,28,27,0,35],
[26,27,23,29,26,25,25,22,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,29,24,22,24,22,21,24],
[31,0,20,32,28,17,23,22,19,27],
[24,31,0,39,32,34,35,26,29,31],
[22,19,12,0,23,21,21,24,16,16],
[27,23,19,28,0,27,31,26,27,30],
[29,34,17,30,24,0,29,28,25,27],
[27,28,16,30,20,22,0,18,13,23],
[29,29,25,27,25,23,33,0,21,26],
[30,32,22,35,24,26,38,30,0,25],
[27,24,20,35,21,24,28,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,20,31,25,23,21,20,19,18],
[20,0,18,31,20,24,19,27,18,19],
[31,33,0,27,28,34,24,23,21,22],
[20,20,24,0,22,26,20,23,22,17],
[26,31,23,29,0,31,18,23,17,26],
[28,27,17,25,20,0,18,19,16,18],
[30,32,27,31,33,33,0,23,26,24],
[31,24,28,28,28,32,28,0,27,20],
[32,33,30,29,34,35,25,24,0,21],
[33,32,29,34,25,33,27,31,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,18,17,23,22,19,17,27,24],
[25,0,22,21,31,28,21,26,30,26],
[33,29,0,23,39,28,28,29,31,28],
[34,30,28,0,31,33,28,25,37,37],
[28,20,12,20,0,22,22,16,27,22],
[29,23,23,18,29,0,23,21,31,30],
[32,30,23,23,29,28,0,16,27,32],
[34,25,22,26,35,30,35,0,27,30],
[24,21,20,14,24,20,24,24,0,19],
[27,25,23,14,29,21,19,21,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,31,21,30,36,29,22,22],
[28,0,28,28,26,33,28,24,26,26],
[26,23,0,29,20,29,28,21,19,22],
[20,23,22,0,23,31,24,22,24,20],
[30,25,31,28,0,33,32,22,28,26],
[21,18,22,20,18,0,27,23,19,24],
[15,23,23,27,19,24,0,25,20,20],
[22,27,30,29,29,28,26,0,27,29],
[29,25,32,27,23,32,31,24,0,29],
[29,25,29,31,25,27,31,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,20,28,27,28,28,35,34],
[25,0,24,26,29,29,24,26,39,26],
[19,27,0,25,31,25,28,27,33,30],
[31,25,26,0,29,31,30,22,30,33],
[23,22,20,22,0,26,25,22,30,25],
[24,22,26,20,25,0,23,27,34,25],
[23,27,23,21,26,28,0,29,31,27],
[23,25,24,29,29,24,22,0,34,27],
[16,12,18,21,21,17,20,17,0,18],
[17,25,21,18,26,26,24,24,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,14,20,29,28,26,28,31,27],
[26,0,25,32,37,36,35,21,39,28],
[37,26,0,24,33,31,26,25,37,24],
[31,19,27,0,25,37,35,23,34,28],
[22,14,18,26,0,28,32,23,33,20],
[23,15,20,14,23,0,18,21,34,19],
[25,16,25,16,19,33,0,18,26,19],
[23,30,26,28,28,30,33,0,34,27],
[20,12,14,17,18,17,25,17,0,20],
[24,23,27,23,31,32,32,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,32,23,22,26,19,29,19,26],
[30,0,28,29,25,24,26,32,24,22],
[19,23,0,23,18,27,22,29,22,21],
[28,22,28,0,27,21,23,26,24,18],
[29,26,33,24,0,29,23,28,26,17],
[25,27,24,30,22,0,25,28,27,21],
[32,25,29,28,28,26,0,30,22,20],
[22,19,22,25,23,23,21,0,21,24],
[32,27,29,27,25,24,29,30,0,20],
[25,29,30,33,34,30,31,27,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,22,25,26,26,16,26,24],
[26,0,18,24,30,26,28,16,26,20],
[26,33,0,24,28,24,33,23,27,29],
[29,27,27,0,27,25,28,22,27,24],
[26,21,23,24,0,26,27,18,25,25],
[25,25,27,26,25,0,30,22,25,25],
[25,23,18,23,24,21,0,15,20,19],
[35,35,28,29,33,29,36,0,36,25],
[25,25,24,24,26,26,31,15,0,23],
[27,31,22,27,26,26,32,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,28,25,28,25,21,30,29,19],
[32,0,34,34,36,33,28,33,38,24],
[23,17,0,31,20,19,20,24,33,22],
[26,17,20,0,21,16,16,26,23,17],
[23,15,31,30,0,29,14,34,30,17],
[26,18,32,35,22,0,20,32,32,26],
[30,23,31,35,37,31,0,30,30,28],
[21,18,27,25,17,19,21,0,26,17],
[22,13,18,28,21,19,21,25,0,18],
[32,27,29,34,34,25,23,34,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,32,30,23,36,25,22,35],
[25,0,30,37,34,25,30,32,21,34],
[25,21,0,27,29,27,32,24,28,28],
[19,14,24,0,27,19,28,25,18,29],
[21,17,22,24,0,14,25,23,24,21],
[28,26,24,32,37,0,35,24,21,33],
[15,21,19,23,26,16,0,23,23,23],
[26,19,27,26,28,27,28,0,24,27],
[29,30,23,33,27,30,28,27,0,26],
[16,17,23,22,30,18,28,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,18,19,25,20,21,26,21],
[27,0,24,24,18,31,19,26,27,26],
[26,27,0,23,26,27,22,23,26,26],
[33,27,28,0,28,32,27,22,28,27],
[32,33,25,23,0,31,20,25,28,26],
[26,20,24,19,20,0,18,22,21,22],
[31,32,29,24,31,33,0,25,32,29],
[30,25,28,29,26,29,26,0,29,27],
[25,24,25,23,23,30,19,22,0,22],
[30,25,25,24,25,29,22,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,30,25,25,35,24,30,27],
[23,0,21,24,27,21,25,26,28,24],
[27,30,0,27,28,29,35,32,25,25],
[21,27,24,0,25,25,27,29,27,27],
[26,24,23,26,0,23,28,23,21,18],
[26,30,22,26,28,0,27,32,25,24],
[16,26,16,24,23,24,0,23,19,18],
[27,25,19,22,28,19,28,0,23,23],
[21,23,26,24,30,26,32,28,0,23],
[24,27,26,24,33,27,33,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,23,22,24,23,22,18,19,23],
[37,0,32,30,25,35,35,33,24,26],
[28,19,0,24,26,29,24,27,26,26],
[29,21,27,0,28,30,22,28,22,21],
[27,26,25,23,0,25,25,27,25,25],
[28,16,22,21,26,0,19,20,15,20],
[29,16,27,29,26,32,0,16,21,21],
[33,18,24,23,24,31,35,0,20,23],
[32,27,25,29,26,36,30,31,0,23],
[28,25,25,30,26,31,30,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,36,26,22,31,30,27,29],
[21,0,16,33,27,19,27,22,20,22],
[27,35,0,32,31,27,26,33,22,29],
[15,18,19,0,22,21,18,19,24,18],
[25,24,20,29,0,24,19,25,26,23],
[29,32,24,30,27,0,34,28,22,30],
[20,24,25,33,32,17,0,28,25,26],
[21,29,18,32,26,23,23,0,18,25],
[24,31,29,27,25,29,26,33,0,28],
[22,29,22,33,28,21,25,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,27,23,32,29,32,33,22],
[23,0,18,24,20,28,29,27,24,20],
[30,33,0,26,25,31,26,30,35,31],
[24,27,25,0,20,25,21,24,27,26],
[28,31,26,31,0,28,24,28,31,28],
[19,23,20,26,23,0,21,20,27,21],
[22,22,25,30,27,30,0,25,26,24],
[19,24,21,27,23,31,26,0,26,23],
[18,27,16,24,20,24,25,25,0,23],
[29,31,20,25,23,30,27,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,27,24,25,22,26,24,22],
[27,0,27,28,26,33,22,33,25,26],
[27,24,0,25,24,29,27,28,21,21],
[24,23,26,0,27,32,27,32,23,24],
[27,25,27,24,0,26,26,28,24,24],
[26,18,22,19,25,0,19,20,19,23],
[29,29,24,24,25,32,0,30,26,25],
[25,18,23,19,23,31,21,0,21,24],
[27,26,30,28,27,32,25,30,0,26],
[29,25,30,27,27,28,26,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,17,23,28,28,27,31,23],
[28,0,27,23,22,34,26,31,31,28],
[25,24,0,22,23,30,29,32,28,24],
[34,28,29,0,25,31,27,34,35,29],
[28,29,28,26,0,30,27,29,34,22],
[23,17,21,20,21,0,21,28,24,28],
[23,25,22,24,24,30,0,28,25,28],
[24,20,19,17,22,23,23,0,28,24],
[20,20,23,16,17,27,26,23,0,20],
[28,23,27,22,29,23,23,27,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,31,23,28,34,24,17,32],
[25,0,25,33,25,27,31,26,24,26],
[26,26,0,24,24,24,30,17,26,29],
[20,18,27,0,23,22,27,20,24,28],
[28,26,27,28,0,25,31,20,27,26],
[23,24,27,29,26,0,32,25,22,27],
[17,20,21,24,20,19,0,15,17,24],
[27,25,34,31,31,26,36,0,28,29],
[34,27,25,27,24,29,34,23,0,33],
[19,25,22,23,25,24,27,22,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,30,25,24,24,26,26,30,26],
[17,0,21,23,26,21,27,24,26,24],
[21,30,0,28,31,26,24,25,32,26],
[26,28,23,0,27,24,24,24,27,28],
[27,25,20,24,0,24,29,21,23,21],
[27,30,25,27,27,0,22,27,30,23],
[25,24,27,27,22,29,0,26,28,26],
[25,27,26,27,30,24,25,0,30,29],
[21,25,19,24,28,21,23,21,0,25],
[25,27,25,23,30,28,25,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,20,26,27,28,25,33,25],
[26,0,21,25,26,24,21,18,26,22],
[26,30,0,33,24,29,34,22,32,24],
[31,26,18,0,29,32,31,26,32,28],
[25,25,27,22,0,23,27,20,24,25],
[24,27,22,19,28,0,22,26,27,22],
[23,30,17,20,24,29,0,23,24,23],
[26,33,29,25,31,25,28,0,32,23],
[18,25,19,19,27,24,27,19,0,21],
[26,29,27,23,26,29,28,28,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,31,23,31,30,26,20,19],
[28,0,21,28,23,26,32,26,23,22],
[28,30,0,34,31,28,30,32,26,25],
[20,23,17,0,19,20,26,22,16,17],
[28,28,20,32,0,26,35,27,24,26],
[20,25,23,31,25,0,24,27,20,20],
[21,19,21,25,16,27,0,20,22,18],
[25,25,19,29,24,24,31,0,24,20],
[31,28,25,35,27,31,29,27,0,24],
[32,29,26,34,25,31,33,31,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,16,24,27,10,23,31,25],
[29,0,34,27,36,34,22,30,35,35],
[28,17,0,25,26,20,18,35,22,26],
[35,24,26,0,31,34,29,27,34,23],
[27,15,25,20,0,21,24,34,24,27],
[24,17,31,17,30,0,16,30,40,28],
[41,29,33,22,27,35,0,24,34,25],
[28,21,16,24,17,21,27,0,32,27],
[20,16,29,17,27,11,17,19,0,25],
[26,16,25,28,24,23,26,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,29,27,24,31,24,27],
[23,0,34,29,30,29,21,29,26,23],
[21,17,0,26,24,25,19,23,21,21],
[22,22,25,0,25,20,19,26,26,29],
[22,21,27,26,0,22,25,30,23,23],
[24,22,26,31,29,0,23,26,26,25],
[27,30,32,32,26,28,0,31,23,32],
[20,22,28,25,21,25,20,0,19,20],
[27,25,30,25,28,25,28,32,0,28],
[24,28,30,22,28,26,19,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,19,40,30,30,23,22,23],
[25,0,33,16,42,20,31,22,13,13],
[23,18,0,18,28,33,33,26,12,26],
[32,35,33,0,45,35,43,24,19,24],
[11,9,23,6,0,15,10,17,20,8],
[21,31,18,16,36,0,26,28,22,19],
[21,20,18,8,41,25,0,19,22,19],
[28,29,25,27,34,23,32,0,27,19],
[29,38,39,32,31,29,29,24,0,24],
[28,38,25,27,43,32,32,32,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,29,24,23,25,27,25,21],
[25,0,30,31,25,27,21,22,33,21],
[20,21,0,31,22,26,17,20,28,22],
[22,20,20,0,24,28,24,27,24,19],
[27,26,29,27,0,23,24,29,29,22],
[28,24,25,23,28,0,26,26,28,27],
[26,30,34,27,27,25,0,26,29,19],
[24,29,31,24,22,25,25,0,32,22],
[26,18,23,27,22,23,22,19,0,21],
[30,30,29,32,29,24,32,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,28,23,23,23,34,23,28],
[30,0,23,26,32,21,30,34,28,29],
[27,28,0,10,14,21,14,27,29,23],
[23,25,41,0,31,31,32,38,40,31],
[28,19,37,20,0,30,15,27,30,22],
[28,30,30,20,21,0,26,36,25,36],
[28,21,37,19,36,25,0,34,41,26],
[17,17,24,13,24,15,17,0,15,14],
[28,23,22,11,21,26,10,36,0,29],
[23,22,28,20,29,15,25,37,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,23,24,22,28,17,30,30],
[31,0,27,23,27,27,32,26,30,29],
[26,24,0,22,23,29,24,20,26,28],
[28,28,29,0,24,32,31,26,31,32],
[27,24,28,27,0,29,33,21,26,30],
[29,24,22,19,22,0,29,20,24,30],
[23,19,27,20,18,22,0,23,24,27],
[34,25,31,25,30,31,28,0,25,32],
[21,21,25,20,25,27,27,26,0,28],
[21,22,23,19,21,21,24,19,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,38,20,33,33,38,25,33],
[30,0,12,30,20,25,25,30,17,25],
[31,39,0,18,46,38,30,39,38,39],
[13,21,33,0,33,20,20,46,33,33],
[31,31,5,18,0,18,30,31,17,31],
[18,26,13,31,33,0,30,39,38,34],
[18,26,21,31,21,21,0,39,38,21],
[13,21,12,5,20,12,12,0,17,13],
[26,34,13,18,34,13,13,34,0,26],
[18,26,12,18,20,17,30,38,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,39,32,28,28,28,28,28,26],
[29,0,23,22,17,16,23,16,23,10],
[12,28,0,18,34,12,22,22,22,10],
[19,29,33,0,35,23,17,41,23,21],
[23,34,17,16,0,16,23,26,16,26],
[23,35,39,28,35,0,35,51,33,27],
[23,28,29,34,28,16,0,44,34,22],
[23,35,29,10,25,0,7,0,19,16],
[23,28,29,28,35,18,17,32,0,20],
[25,41,41,30,25,24,29,35,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,20,32,20,16,24,17,29],
[29,0,29,21,27,24,28,17,28,35],
[30,22,0,23,28,23,26,24,26,32],
[31,30,28,0,32,18,23,23,28,46],
[19,24,23,19,0,16,17,17,21,29],
[31,27,28,33,35,0,23,19,27,32],
[35,23,25,28,34,28,0,28,23,29],
[27,34,27,28,34,32,23,0,28,37],
[34,23,25,23,30,24,28,23,0,31],
[22,16,19,5,22,19,22,14,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,32,26,27,34,27,34,29,26],
[27,0,34,29,25,33,27,36,34,28],
[19,17,0,18,21,23,22,28,22,24],
[25,22,33,0,29,33,24,28,29,28],
[24,26,30,22,0,28,25,29,27,29],
[17,18,28,18,23,0,17,24,27,18],
[24,24,29,27,26,34,0,34,30,29],
[17,15,23,23,22,27,17,0,21,22],
[22,17,29,22,24,24,21,30,0,22],
[25,23,27,23,22,33,22,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,24,29,36,38,34,30,29,33],
[19,0,18,28,28,27,24,23,28,27],
[27,33,0,40,22,25,33,21,29,29],
[22,23,11,0,21,22,22,16,31,26],
[15,23,29,30,0,26,22,18,30,28],
[13,24,26,29,25,0,22,27,20,26],
[17,27,18,29,29,29,0,21,19,23],
[21,28,30,35,33,24,30,0,31,29],
[22,23,22,20,21,31,32,20,0,25],
[18,24,22,25,23,25,28,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,33,35,31,28,30,37,25,29],
[21,0,26,29,26,26,22,34,23,25],
[18,25,0,29,29,28,27,32,24,19],
[16,22,22,0,23,27,23,30,18,24],
[20,25,22,28,0,28,23,33,22,24],
[23,25,23,24,23,0,28,37,23,32],
[21,29,24,28,28,23,0,36,31,23],
[14,17,19,21,18,14,15,0,21,18],
[26,28,27,33,29,28,20,30,0,24],
[22,26,32,27,27,19,28,33,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,36,33,32,27,32,25,35,24],
[21,0,31,21,27,24,21,21,23,26],
[15,20,0,24,28,20,25,21,25,20],
[18,30,27,0,29,18,29,21,23,24],
[19,24,23,22,0,28,26,25,19,28],
[24,27,31,33,23,0,28,25,30,21],
[19,30,26,22,25,23,0,22,20,27],
[26,30,30,30,26,26,29,0,28,23],
[16,28,26,28,32,21,31,23,0,27],
[27,25,31,27,23,30,24,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,14,30,28,30,30,30,14,51],
[23,0,37,32,37,23,28,25,21,51],
[37,14,0,46,30,37,37,39,35,46],
[21,19,5,0,35,28,42,30,12,51],
[23,14,21,16,0,16,16,25,5,37],
[21,28,14,23,35,0,42,9,35,51],
[21,23,14,9,35,9,0,9,21,30],
[21,26,12,21,26,42,42,0,26,42],
[37,30,16,39,46,16,30,25,0,46],
[0,0,5,0,14,0,21,9,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,23,21,36,30,27,18,30,18],
[20,0,21,20,18,32,28,23,28,12],
[28,30,0,24,28,28,18,15,34,17],
[30,31,27,0,28,31,25,28,34,24],
[15,33,23,23,0,25,30,14,33,16],
[21,19,23,20,26,0,20,16,27,19],
[24,23,33,26,21,31,0,24,34,14],
[33,28,36,23,37,35,27,0,27,33],
[21,23,17,17,18,24,17,24,0,20],
[33,39,34,27,35,32,37,18,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,28,26,26,28,28,25,27],
[25,0,23,24,22,22,24,24,25,23],
[24,28,0,25,26,27,24,25,25,29],
[23,27,26,0,26,22,25,29,29,27],
[25,29,25,25,0,22,22,25,26,32],
[25,29,24,29,29,0,22,31,28,28],
[23,27,27,26,29,29,0,28,26,28],
[23,27,26,22,26,20,23,0,25,25],
[26,26,26,22,25,23,25,26,0,29],
[24,28,22,24,19,23,23,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,25,19,21,27,20,22,27],
[27,0,25,29,27,25,27,27,25,27],
[28,26,0,23,27,25,25,28,23,31],
[26,22,28,0,25,26,25,27,23,28],
[32,24,24,26,0,21,21,29,24,31],
[30,26,26,25,30,0,33,27,26,29],
[24,24,26,26,30,18,0,25,26,26],
[31,24,23,24,22,24,26,0,24,28],
[29,26,28,28,27,25,25,27,0,33],
[24,24,20,23,20,22,25,23,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,23,33,31,37,26,34,26],
[26,0,25,27,27,28,37,26,33,26],
[24,26,0,33,28,22,36,23,34,30],
[28,24,18,0,20,22,31,22,26,16],
[18,24,23,31,0,24,32,18,29,26],
[20,23,29,29,27,0,33,25,31,22],
[14,14,15,20,19,18,0,20,26,19],
[25,25,28,29,33,26,31,0,34,25],
[17,18,17,25,22,20,25,17,0,22],
[25,25,21,35,25,29,32,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,16,23,26,23,17,28,22],
[28,0,28,24,25,27,27,29,27,31],
[25,23,0,17,29,28,22,19,32,18],
[35,27,34,0,36,33,31,22,32,26],
[28,26,22,15,0,31,23,25,33,29],
[25,24,23,18,20,0,22,19,28,24],
[28,24,29,20,28,29,0,26,26,29],
[34,22,32,29,26,32,25,0,29,27],
[23,24,19,19,18,23,25,22,0,23],
[29,20,33,25,22,27,22,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,22,36,30,25,26,29,30],
[25,0,27,27,31,31,28,31,23,30],
[21,24,0,20,30,23,20,21,26,34],
[29,24,31,0,38,25,32,27,25,37],
[15,20,21,13,0,8,17,19,22,27],
[21,20,28,26,43,0,23,24,33,28],
[26,23,31,19,34,28,0,23,23,33],
[25,20,30,24,32,27,28,0,25,33],
[22,28,25,26,29,18,28,26,0,27],
[21,21,17,14,24,23,18,18,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,24,30,21,24,26,29,22],
[27,0,25,27,29,26,30,25,31,26],
[27,26,0,25,31,23,34,28,29,21],
[27,24,26,0,25,29,26,30,28,24],
[21,22,20,26,0,21,27,22,29,24],
[30,25,28,22,30,0,27,23,34,27],
[27,21,17,25,24,24,0,25,26,20],
[25,26,23,21,29,28,26,0,32,28],
[22,20,22,23,22,17,25,19,0,25],
[29,25,30,27,27,24,31,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,18,32,20,26,21,17,25],
[22,0,16,22,28,28,28,25,19,21],
[28,35,0,21,23,12,42,20,28,14],
[33,29,30,0,27,27,32,21,24,26],
[19,23,28,24,0,26,30,20,23,20],
[31,23,39,24,25,0,33,23,34,19],
[25,23,9,19,21,18,0,23,23,20],
[30,26,31,30,31,28,28,0,19,27],
[34,32,23,27,28,17,28,32,0,15],
[26,30,37,25,31,32,31,24,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,28,21,24,20,24,27,34],
[27,0,34,34,27,30,20,19,28,32],
[25,17,0,24,10,20,20,17,34,31],
[23,17,27,0,22,25,16,22,23,29],
[30,24,41,29,0,20,27,27,39,40],
[27,21,31,26,31,0,26,23,35,36],
[31,31,31,35,24,25,0,21,29,31],
[27,32,34,29,24,28,30,0,32,38],
[24,23,17,28,12,16,22,19,0,36],
[17,19,20,22,11,15,20,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,29,23,23,27,23,24,21],
[25,0,27,22,23,22,31,17,25,27],
[26,24,0,27,22,21,27,28,31,25],
[22,29,24,0,24,27,31,18,27,25],
[28,28,29,27,0,29,32,23,31,33],
[28,29,30,24,22,0,27,22,27,27],
[24,20,24,20,19,24,0,21,25,23],
[28,34,23,33,28,29,30,0,32,29],
[27,26,20,24,20,24,26,19,0,25],
[30,24,26,26,18,24,28,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,24,27,16,30,26,38,31],
[29,0,26,25,36,31,32,18,25,36],
[18,25,0,21,33,25,26,19,37,29],
[27,26,30,0,36,33,30,24,31,31],
[24,15,18,15,0,27,35,16,29,33],
[35,20,26,18,24,0,28,23,33,35],
[21,19,25,21,16,23,0,18,30,35],
[25,33,32,27,35,28,33,0,31,27],
[13,26,14,20,22,18,21,20,0,23],
[20,15,22,20,18,16,16,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,25,38,20,40,34,29,23,27],
[17,0,19,32,25,27,21,16,24,25],
[26,32,0,33,26,33,28,25,23,26],
[13,19,18,0,16,22,25,14,16,21],
[31,26,25,35,0,30,33,22,29,29],
[11,24,18,29,21,0,24,21,15,20],
[17,30,23,26,18,27,0,23,20,21],
[22,35,26,37,29,30,28,0,26,26],
[28,27,28,35,22,36,31,25,0,25],
[24,26,25,30,22,31,30,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,22,26,33,21,24,26,26],
[19,0,26,18,21,29,21,21,26,19],
[21,25,0,24,29,31,23,22,21,25],
[29,33,27,0,26,32,28,29,30,25],
[25,30,22,25,0,29,24,29,26,25],
[18,22,20,19,22,0,18,16,17,17],
[30,30,28,23,27,33,0,30,30,25],
[27,30,29,22,22,35,21,0,33,25],
[25,25,30,21,25,34,21,18,0,26],
[25,32,26,26,26,34,26,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,41,25,37,26,27,25,31],
[27,0,24,26,21,32,32,29,29,37],
[23,27,0,32,29,21,29,20,26,26],
[10,25,19,0,28,33,31,24,21,20],
[26,30,22,23,0,30,37,35,40,24],
[14,19,30,18,21,0,26,24,24,20],
[25,19,22,20,14,25,0,24,32,21],
[24,22,31,27,16,27,27,0,29,23],
[26,22,25,30,11,27,19,22,0,28],
[20,14,25,31,27,31,30,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,30,31,17,1,17,31,10,20],
[24,0,21,11,1,15,19,11,11,2],
[21,30,0,27,7,14,8,18,2,17],
[20,40,24,0,21,15,9,8,11,30],
[34,50,44,30,0,25,19,21,21,44],
[50,36,37,36,26,0,38,37,21,36],
[34,32,43,42,32,13,0,30,33,32],
[20,40,33,43,30,14,21,0,23,23],
[41,40,49,40,30,30,18,28,0,40],
[31,49,34,21,7,15,19,28,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,35,25,27,27,31,31,27],
[18,0,23,25,19,22,20,20,22,21],
[20,28,0,23,24,22,27,16,22,19],
[16,26,28,0,21,23,19,20,23,19],
[26,32,27,30,0,20,30,23,31,27],
[24,29,29,28,31,0,27,23,29,30],
[24,31,24,32,21,24,0,24,30,24],
[20,31,35,31,28,28,27,0,31,33],
[20,29,29,28,20,22,21,20,0,23],
[24,30,32,32,24,21,27,18,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,27,17,12,27,17,14,20,19],
[34,0,22,36,13,35,25,31,28,36],
[24,29,0,24,24,27,29,14,15,17],
[34,15,27,0,25,18,17,14,20,15],
[39,38,27,26,0,24,38,23,27,26],
[24,16,24,33,27,0,29,23,17,17],
[34,26,22,34,13,22,0,9,13,27],
[37,20,37,37,28,28,42,0,30,18],
[31,23,36,31,24,34,38,21,0,24],
[32,15,34,36,25,34,24,33,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,26,28,33,31,31,27,26],
[20,0,22,26,22,27,26,25,24,21],
[27,29,0,27,27,30,30,27,32,25],
[25,25,24,0,20,25,28,23,30,18],
[23,29,24,31,0,26,24,30,29,22],
[18,24,21,26,25,0,25,24,26,22],
[20,25,21,23,27,26,0,27,32,22],
[20,26,24,28,21,27,24,0,30,21],
[24,27,19,21,22,25,19,21,0,19],
[25,30,26,33,29,29,29,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,38,25,30,42,32,31,27,32],
[24,0,33,28,31,33,36,28,26,24],
[13,18,0,15,25,20,19,20,17,19],
[26,23,36,0,29,30,26,30,29,23],
[21,20,26,22,0,28,28,27,23,24],
[9,18,31,21,23,0,22,26,22,22],
[19,15,32,25,23,29,0,27,22,28],
[20,23,31,21,24,25,24,0,20,25],
[24,25,34,22,28,29,29,31,0,30],
[19,27,32,28,27,29,23,26,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,39,26,28,23,29,30,36,31],
[19,0,26,20,21,18,27,26,35,25],
[12,25,0,20,23,17,21,26,29,20],
[25,31,31,0,29,30,22,30,35,24],
[23,30,28,22,0,22,24,25,34,25],
[28,33,34,21,29,0,29,35,37,30],
[22,24,30,29,27,22,0,28,31,29],
[21,25,25,21,26,16,23,0,34,25],
[15,16,22,16,17,14,20,17,0,14],
[20,26,31,27,26,21,22,26,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,28,29,28,28,27,28,27],
[20,0,22,20,19,19,24,28,13,24],
[26,29,0,29,28,26,32,32,24,28],
[23,31,22,0,22,25,26,27,24,29],
[22,32,23,29,0,28,27,28,24,27],
[23,32,25,26,23,0,33,30,20,25],
[23,27,19,25,24,18,0,25,16,22],
[24,23,19,24,23,21,26,0,20,23],
[23,38,27,27,27,31,35,31,0,32],
[24,27,23,22,24,26,29,28,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,33,34,33,37,28,31,21,35],
[24,0,27,35,32,32,26,25,27,33],
[18,24,0,32,26,26,20,25,19,28],
[17,16,19,0,20,21,15,12,12,17],
[18,19,25,31,0,32,15,29,17,28],
[14,19,25,30,19,0,18,25,14,29],
[23,25,31,36,36,33,0,34,28,37],
[20,26,26,39,22,26,17,0,19,29],
[30,24,32,39,34,37,23,32,0,31],
[16,18,23,34,23,22,14,22,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,17,30,26,16,27,22,23],
[25,0,33,22,32,27,19,30,28,28],
[27,18,0,18,27,18,23,23,27,19],
[34,29,33,0,29,30,23,35,32,28],
[21,19,24,22,0,26,21,26,23,25],
[25,24,33,21,25,0,18,30,26,29],
[35,32,28,28,30,33,0,27,33,25],
[24,21,28,16,25,21,24,0,26,22],
[29,23,24,19,28,25,18,25,0,26],
[28,23,32,23,26,22,26,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,25,27,20,20,19,23,20],
[27,0,21,20,23,21,22,20,24,20],
[30,30,0,25,28,22,26,23,26,21],
[26,31,26,0,29,21,28,24,26,25],
[24,28,23,22,0,21,22,19,22,23],
[31,30,29,30,30,0,26,26,26,25],
[31,29,25,23,29,25,0,23,21,25],
[32,31,28,27,32,25,28,0,25,26],
[28,27,25,25,29,25,30,26,0,22],
[31,31,30,26,28,26,26,25,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,20,33,21,36,25,32,30],
[25,0,29,29,29,21,27,20,26,26],
[26,22,0,25,24,21,31,30,34,23],
[31,22,26,0,24,26,30,22,31,28],
[18,22,27,27,0,18,28,20,30,31],
[30,30,30,25,33,0,36,29,37,39],
[15,24,20,21,23,15,0,17,32,24],
[26,31,21,29,31,22,34,0,35,29],
[19,25,17,20,21,14,19,16,0,28],
[21,25,28,23,20,12,27,22,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,16,17,30,41,20,17,32,9],
[31,0,16,9,34,44,29,21,34,9],
[35,35,0,27,35,39,13,17,35,4],
[34,42,24,0,40,51,32,17,42,21],
[21,17,16,11,0,33,7,16,11,4],
[10,7,12,0,18,0,7,5,0,5],
[31,22,38,19,44,44,0,31,31,31],
[34,30,34,34,35,46,20,0,42,4],
[19,17,16,9,40,51,20,9,0,9],
[42,42,47,30,47,46,20,47,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,33,22,26,30,26,27,32],
[24,0,33,25,23,26,33,23,24,27],
[20,18,0,18,22,18,23,21,19,22],
[18,26,33,0,25,25,28,22,20,21],
[29,28,29,26,0,29,29,24,25,29],
[25,25,33,26,22,0,27,26,25,30],
[21,18,28,23,22,24,0,21,19,26],
[25,28,30,29,27,25,30,0,26,27],
[24,27,32,31,26,26,32,25,0,28],
[19,24,29,30,22,21,25,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,26,30,23,34,29,26,34],
[23,0,24,34,25,24,26,18,15,28],
[25,27,0,28,23,24,28,25,18,29],
[25,17,23,0,29,23,18,27,22,29],
[21,26,28,22,0,26,33,22,21,28],
[28,27,27,28,25,0,31,34,27,26],
[17,25,23,33,18,20,0,15,17,27],
[22,33,26,24,29,17,36,0,25,28],
[25,36,33,29,30,24,34,26,0,25],
[17,23,22,22,23,25,24,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,36,30,26,33,30,25,28],
[24,0,24,32,22,27,26,22,20,21],
[22,27,0,32,25,25,29,23,27,21],
[15,19,19,0,16,22,20,12,14,17],
[21,29,26,35,0,29,28,23,26,22],
[25,24,26,29,22,0,24,22,24,22],
[18,25,22,31,23,27,0,21,19,17],
[21,29,28,39,28,29,30,0,26,26],
[26,31,24,37,25,27,32,25,0,28],
[23,30,30,34,29,29,34,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,35,29,26,21,29,30,34,29],
[22,0,30,28,30,25,25,24,23,31],
[16,21,0,27,21,21,23,16,24,31],
[22,23,24,0,21,21,24,25,28,28],
[25,21,30,30,0,25,26,25,28,35],
[30,26,30,30,26,0,28,24,30,28],
[22,26,28,27,25,23,0,24,32,29],
[21,27,35,26,26,27,27,0,29,34],
[17,28,27,23,23,21,19,22,0,31],
[22,20,20,23,16,23,22,17,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,34,35,35,27,21,29,27],
[30,0,25,34,22,38,18,19,26,20],
[28,26,0,29,25,29,19,28,28,16],
[17,17,22,0,26,29,19,20,24,13],
[16,29,26,25,0,34,26,26,22,20],
[16,13,22,22,17,0,15,15,19,9],
[24,33,32,32,25,36,0,19,27,21],
[30,32,23,31,25,36,32,0,25,12],
[22,25,23,27,29,32,24,26,0,29],
[24,31,35,38,31,42,30,39,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,29,28,29,27,29,24,28,34],
[28,0,25,25,32,23,22,24,34,35],
[22,26,0,26,24,19,28,23,25,28],
[23,26,25,0,30,24,28,26,28,33],
[22,19,27,21,0,27,24,20,24,29],
[24,28,32,27,24,0,29,25,30,32],
[22,29,23,23,27,22,0,27,30,31],
[27,27,28,25,31,26,24,0,32,34],
[23,17,26,23,27,21,21,19,0,33],
[17,16,23,18,22,19,20,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,25,17,16,20,22,17,21],
[37,0,29,30,23,24,38,35,35,28],
[36,22,0,29,25,20,26,38,29,23],
[26,21,22,0,18,23,24,26,26,21],
[34,28,26,33,0,28,27,36,29,22],
[35,27,31,28,23,0,29,38,19,21],
[31,13,25,27,24,22,0,30,32,25],
[29,16,13,25,15,13,21,0,21,17],
[34,16,22,25,22,32,19,30,0,24],
[30,23,28,30,29,30,26,34,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 51, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_10_51.csv", index=False, header=False)