
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,62,29,36,37,59,56,47,62],
[38,0,55,46,48,62,34,52,53],
[71,45,0,57,50,71,53,52,54],
[64,54,43,0,65,72,52,51,63],
[63,52,50,35,0,69,48,31,42],
[41,38,29,28,31,0,44,42,45],
[44,66,47,48,52,56,0,51,53],
[53,48,48,49,69,58,49,0,56],
[38,47,46,37,58,55,47,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,54,49,59,49,52,53,51],
[44,0,45,36,55,43,53,54,40],
[46,55,0,50,59,49,63,65,49],
[51,64,50,0,56,54,59,56,46],
[41,45,41,44,0,44,53,52,45],
[51,57,51,46,56,0,53,62,44],
[48,47,37,41,47,47,0,49,38],
[47,46,35,44,48,38,51,0,34],
[49,60,51,54,55,56,62,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,51,56,53,59,58,59,48],
[38,0,40,55,44,54,49,55,45],
[49,60,0,64,63,62,64,67,59],
[44,45,36,0,49,49,49,34,45],
[47,56,37,51,0,50,54,50,42],
[41,46,38,51,50,0,53,42,47],
[42,51,36,51,46,47,0,40,43],
[41,45,33,66,50,58,60,0,51],
[52,55,41,55,58,53,57,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,49,61,54,49,64,51,59],
[38,0,47,48,48,40,48,51,50],
[51,53,0,53,52,47,51,53,52],
[39,52,47,0,53,53,50,55,53],
[46,52,48,47,0,44,49,47,57],
[51,60,53,47,56,0,52,58,58],
[36,52,49,50,51,48,0,49,55],
[49,49,47,45,53,42,51,0,49],
[41,50,48,47,43,42,45,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,61,49,45,40,51,61,49],
[51,0,64,54,49,52,55,59,51],
[39,36,0,44,36,31,43,47,40],
[51,46,56,0,41,38,41,56,46],
[55,51,64,59,0,46,55,61,59],
[60,48,69,62,54,0,58,64,60],
[49,45,57,59,45,42,0,57,55],
[39,41,53,44,39,36,43,0,44],
[51,49,60,54,41,40,45,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,54,59,58,52,62,50,52],
[47,0,46,54,52,47,44,46,43],
[46,54,0,47,49,43,47,49,42],
[41,46,53,0,48,47,44,44,44],
[42,48,51,52,0,51,47,45,44],
[48,53,57,53,49,0,45,50,49],
[38,56,53,56,53,55,0,50,46],
[50,54,51,56,55,50,50,0,43],
[48,57,58,56,56,51,54,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,49,57,55,50,44,51,48],
[55,0,47,55,48,53,52,56,41],
[51,53,0,56,40,50,46,56,48],
[43,45,44,0,46,54,48,50,42],
[45,52,60,54,0,51,51,50,36],
[50,47,50,46,49,0,49,50,41],
[56,48,54,52,49,51,0,48,51],
[49,44,44,50,50,50,52,0,44],
[52,59,52,58,64,59,49,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,59,47,45,50,56,41,38],
[44,0,48,41,41,43,46,42,48],
[41,52,0,45,46,44,56,42,40],
[53,59,55,0,53,51,57,47,51],
[55,59,54,47,0,51,57,47,41],
[50,57,56,49,49,0,45,43,45],
[44,54,44,43,43,55,0,38,47],
[59,58,58,53,53,57,62,0,49],
[62,52,60,49,59,55,53,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,30,42,41,38,49,54],
[55,0,45,44,54,47,38,49,49],
[57,55,0,51,49,37,40,39,43],
[70,56,49,0,61,53,52,58,47],
[58,46,51,39,0,46,44,47,46],
[59,53,63,47,54,0,50,53,42],
[62,62,60,48,56,50,0,52,52],
[51,51,61,42,53,47,48,0,52],
[46,51,57,53,54,58,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,43,74,44,54,46,51,67],
[72,0,56,66,44,44,59,56,69],
[57,44,0,59,57,37,51,47,50],
[26,34,41,0,29,28,39,39,38],
[56,56,43,71,0,52,58,30,56],
[46,56,63,72,48,0,56,38,66],
[54,41,49,61,42,44,0,50,50],
[49,44,53,61,70,62,50,0,56],
[33,31,50,62,44,34,50,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,60,56,58,59,62,52,55],
[50,0,53,53,51,58,64,49,55],
[40,47,0,49,49,49,55,47,50],
[44,47,51,0,51,47,57,50,45],
[42,49,51,49,0,49,54,43,49],
[41,42,51,53,51,0,49,49,54],
[38,36,45,43,46,51,0,43,40],
[48,51,53,50,57,51,57,0,46],
[45,45,50,55,51,46,60,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,28,42,62,62,24,44,38],
[45,0,48,35,59,48,54,28,43],
[72,52,0,66,64,59,29,46,43],
[58,65,34,0,50,45,49,38,43],
[38,41,36,50,0,56,51,47,34],
[38,52,41,55,44,0,47,38,44],
[76,46,71,51,49,53,0,56,31],
[56,72,54,62,53,62,44,0,56],
[62,57,57,57,66,56,69,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,46,46,44,54,47,45],
[47,0,51,51,47,43,56,53,47],
[56,49,0,55,52,51,54,51,50],
[54,49,45,0,47,42,58,52,45],
[54,53,48,53,0,46,60,49,48],
[56,57,49,58,54,0,58,55,53],
[46,44,46,42,40,42,0,45,42],
[53,47,49,48,51,45,55,0,45],
[55,53,50,55,52,47,58,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,46,31,41,41,17,41,77],
[69,0,69,81,81,81,50,100,100],
[54,31,0,54,64,54,71,64,100],
[69,19,46,0,50,100,50,46,46],
[59,19,36,50,0,67,40,50,36],
[59,19,46,0,33,0,40,29,46],
[83,50,29,50,60,60,0,60,77],
[59,0,36,54,50,71,40,0,46],
[23,0,0,54,64,54,23,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,49,54,41,53,54,63,55],
[47,0,40,53,47,47,52,65,51],
[51,60,0,63,43,55,42,62,56],
[46,47,37,0,48,48,50,57,42],
[59,53,57,52,0,52,46,65,44],
[47,53,45,52,48,0,56,65,62],
[46,48,58,50,54,44,0,62,58],
[37,35,38,43,35,35,38,0,42],
[45,49,44,58,56,38,42,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,35,61,20,62,73,62],
[54,0,34,57,63,63,44,73,44],
[50,66,0,50,60,48,59,69,70],
[65,43,50,0,61,38,62,50,62],
[39,37,40,39,0,47,81,40,58],
[80,37,52,62,53,0,79,62,64],
[38,56,41,38,19,21,0,59,30],
[27,27,31,50,60,38,41,0,71],
[38,56,30,38,42,36,70,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,55,63,48,64,57,56,66],
[37,0,43,56,42,57,50,58,42],
[45,57,0,74,51,57,52,48,57],
[37,44,26,0,36,53,36,48,50],
[52,58,49,64,0,58,52,63,54],
[36,43,43,47,42,0,35,48,37],
[43,50,48,64,48,65,0,47,56],
[44,42,52,52,37,52,53,0,46],
[34,58,43,50,46,63,44,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,40,24,33,39,28,44,31],
[56,0,46,39,50,52,27,52,8],
[60,54,0,33,62,39,45,59,16],
[76,61,67,0,75,39,39,73,25],
[67,50,38,25,0,31,31,61,15],
[61,48,61,61,69,0,29,52,40],
[72,73,55,61,69,71,0,94,50],
[56,48,41,27,39,48,6,0,4],
[69,92,84,75,85,60,50,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,56,77,77,56,59,56,85],
[67,0,38,52,70,85,52,31,70],
[44,62,0,52,70,70,52,52,70],
[23,48,48,0,41,41,23,41,47],
[23,30,30,59,0,15,36,0,70],
[44,15,30,59,85,0,52,46,70],
[41,48,48,77,64,48,0,56,70],
[44,69,48,59,100,54,44,0,85],
[15,30,30,53,30,30,30,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,49,55,39,47,51,50],
[51,0,48,47,55,49,51,47,56],
[51,52,0,49,55,56,59,58,58],
[51,53,51,0,54,48,46,54,47],
[45,45,45,46,0,38,46,53,47],
[61,51,44,52,62,0,53,48,53],
[53,49,41,54,54,47,0,57,51],
[49,53,42,46,47,52,43,0,56],
[50,44,42,53,53,47,49,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,39,42,54,54,45,35,44],
[59,0,47,55,52,61,53,52,45],
[61,53,0,51,57,52,51,52,48],
[58,45,49,0,52,54,40,42,41],
[46,48,43,48,0,46,45,43,35],
[46,39,48,46,54,0,34,37,38],
[55,47,49,60,55,66,0,38,50],
[65,48,48,58,57,63,62,0,47],
[56,55,52,59,65,62,50,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,77,55,58,39,60,55,77],
[24,0,36,43,26,30,48,29,60],
[23,64,0,35,23,29,61,34,68],
[45,57,65,0,47,37,64,42,60],
[42,74,77,53,0,55,53,57,82],
[61,70,71,63,45,0,54,45,88],
[40,52,39,36,47,46,0,31,67],
[45,71,66,58,43,55,69,0,84],
[23,40,32,40,18,12,33,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,52,52,40,51,47,57],
[54,0,46,50,62,49,63,55,60],
[49,54,0,49,51,51,63,51,60],
[48,50,51,0,56,44,54,57,57],
[48,38,49,44,0,42,51,50,57],
[60,51,49,56,58,0,50,57,53],
[49,37,37,46,49,50,0,40,57],
[53,45,49,43,50,43,60,0,57],
[43,40,40,43,43,47,43,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,63,53,41,54,49,49],
[43,0,60,54,47,39,48,47,45],
[41,40,0,53,36,48,46,43,41],
[37,46,47,0,39,41,45,41,50],
[47,53,64,61,0,45,47,47,50],
[59,61,52,59,55,0,51,49,52],
[46,52,54,55,53,49,0,51,47],
[51,53,57,59,53,51,49,0,49],
[51,55,59,50,50,48,53,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,47,53,36,40,43,47,51],
[65,0,64,63,52,47,63,58,63],
[53,36,0,50,48,46,42,52,51],
[47,37,50,0,45,38,43,48,48],
[64,48,52,55,0,43,48,50,64],
[60,53,54,62,57,0,47,56,56],
[57,37,58,57,52,53,0,50,52],
[53,42,48,52,50,44,50,0,54],
[49,37,49,52,36,44,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,58,57,51,46,51,50,47],
[47,0,47,44,51,49,53,46,48],
[42,53,0,50,54,45,51,47,45],
[43,56,50,0,49,45,53,42,34],
[49,49,46,51,0,52,47,43,45],
[54,51,55,55,48,0,44,33,48],
[49,47,49,47,53,56,0,38,49],
[50,54,53,58,57,67,62,0,52],
[53,52,55,66,55,52,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,44,48,51,54,51,45,52],
[53,0,43,57,51,59,52,51,48],
[56,57,0,48,64,57,55,51,59],
[52,43,52,0,63,62,56,49,57],
[49,49,36,37,0,50,44,43,54],
[46,41,43,38,50,0,42,41,43],
[49,48,45,44,56,58,0,39,48],
[55,49,49,51,57,59,61,0,59],
[48,52,41,43,46,57,52,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,39,40,41,48,48,41,44],
[50,0,46,52,44,47,48,46,55],
[61,54,0,50,48,41,44,51,50],
[60,48,50,0,54,51,48,52,42],
[59,56,52,46,0,37,50,49,43],
[52,53,59,49,63,0,57,47,54],
[52,52,56,52,50,43,0,44,50],
[59,54,49,48,51,53,56,0,56],
[56,45,50,58,57,46,50,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,49,49,53,40,56,45],
[52,0,56,48,54,53,52,62,55],
[45,44,0,50,54,52,55,62,46],
[51,52,50,0,51,56,51,64,53],
[51,46,46,49,0,50,47,50,47],
[47,47,48,44,50,0,51,55,48],
[60,48,45,49,53,49,0,62,53],
[44,38,38,36,50,45,38,0,44],
[55,45,54,47,53,52,47,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,65,60,47,55,49,56],
[53,0,46,62,57,51,53,53,58],
[55,54,0,64,61,50,52,56,62],
[35,38,36,0,51,38,44,41,43],
[40,43,39,49,0,45,41,42,44],
[53,49,50,62,55,0,51,50,55],
[45,47,48,56,59,49,0,48,52],
[51,47,44,59,58,50,52,0,53],
[44,42,38,57,56,45,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,60,66,54,59,49,62,61],
[41,0,53,53,43,37,50,55,44],
[40,47,0,60,52,48,44,51,56],
[34,47,40,0,31,34,39,43,35],
[46,57,48,69,0,36,37,57,50],
[41,63,52,66,64,0,48,71,56],
[51,50,56,61,63,52,0,60,58],
[38,45,49,57,43,29,40,0,45],
[39,56,44,65,50,44,42,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,36,47,24,40,39,33,40],
[55,0,49,47,34,56,45,46,43],
[64,51,0,34,51,64,55,44,47],
[53,53,66,0,39,54,57,47,58],
[76,66,49,61,0,69,73,65,59],
[60,44,36,46,31,0,59,41,54],
[61,55,45,43,27,41,0,48,41],
[67,54,56,53,35,59,52,0,65],
[60,57,53,42,41,46,59,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,54,59,52,51,51,62,50],
[50,0,53,52,52,59,42,55,49],
[46,47,0,52,54,56,44,50,41],
[41,48,48,0,48,55,41,46,48],
[48,48,46,52,0,53,46,49,46],
[49,41,44,45,47,0,45,45,43],
[49,58,56,59,54,55,0,57,46],
[38,45,50,54,51,55,43,0,42],
[50,51,59,52,54,57,54,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,63,60,60,62,52,56],
[53,0,54,60,49,62,63,53,60],
[46,46,0,48,50,59,54,50,54],
[37,40,52,0,52,51,53,43,54],
[40,51,50,48,0,51,56,36,52],
[40,38,41,49,49,0,50,43,49],
[38,37,46,47,44,50,0,39,45],
[48,47,50,57,64,57,61,0,60],
[44,40,46,46,48,51,55,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,57,57,58,47,56,51,58],
[51,0,63,56,51,50,63,51,44],
[43,37,0,37,46,37,43,40,45],
[43,44,63,0,46,48,56,56,48],
[42,49,54,54,0,50,51,52,50],
[53,50,63,52,50,0,54,45,50],
[44,37,57,44,49,46,0,45,49],
[49,49,60,44,48,55,55,0,46],
[42,56,55,52,50,50,51,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,70,54,51,59,47,47],
[49,0,66,66,51,48,38,58,33],
[45,34,0,64,51,45,38,58,31],
[30,34,36,0,34,51,44,51,39],
[46,49,49,66,0,51,57,71,41],
[49,52,55,49,49,0,32,41,39],
[41,62,62,56,43,68,0,80,53],
[53,42,42,49,29,59,20,0,29],
[53,67,69,61,59,61,47,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,45,39,50,46,43,48],
[55,0,38,44,37,46,43,42,40],
[54,62,0,45,49,51,51,48,51],
[55,56,55,0,49,56,51,53,47],
[61,63,51,51,0,47,49,46,52],
[50,54,49,44,53,0,49,47,44],
[54,57,49,49,51,51,0,46,46],
[57,58,52,47,54,53,54,0,48],
[52,60,49,53,48,56,54,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,54,40,45,63,43,61,59],
[27,0,55,35,40,37,47,32,58],
[46,45,0,39,27,55,62,36,68],
[60,65,61,0,50,58,55,50,75],
[55,60,73,50,0,66,63,36,76],
[37,63,45,42,34,0,37,48,52],
[57,53,38,45,37,63,0,34,63],
[39,68,64,50,64,52,66,0,86],
[41,42,32,25,24,48,37,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,61,53,47,47,60,46,44],
[59,0,56,49,47,45,50,53,49],
[39,44,0,62,35,42,45,45,37],
[47,51,38,0,35,46,46,42,57],
[53,53,65,65,0,44,65,47,50],
[53,55,58,54,56,0,55,51,44],
[40,50,55,54,35,45,0,39,44],
[54,47,55,58,53,49,61,0,54],
[56,51,63,43,50,56,56,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,42,54,46,49,45,43,46],
[53,0,48,59,46,52,54,54,56],
[58,52,0,55,51,59,50,55,51],
[46,41,45,0,44,43,55,39,44],
[54,54,49,56,0,52,56,45,44],
[51,48,41,57,48,0,47,44,44],
[55,46,50,45,44,53,0,46,47],
[57,46,45,61,55,56,54,0,50],
[54,44,49,56,56,56,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,48,44,49,48,47,57],
[51,0,46,49,47,50,46,49,57],
[49,54,0,53,47,55,43,50,62],
[52,51,47,0,56,52,49,60,59],
[56,53,53,44,0,56,54,62,61],
[51,50,45,48,44,0,42,52,51],
[52,54,57,51,46,58,0,56,60],
[53,51,50,40,38,48,44,0,59],
[43,43,38,41,39,49,40,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,54,53,47,50,53,51],
[48,0,52,59,53,54,58,56,50],
[48,48,0,54,49,51,52,48,40],
[46,41,46,0,51,49,52,55,48],
[47,47,51,49,0,51,45,49,38],
[53,46,49,51,49,0,48,49,47],
[50,42,48,48,55,52,0,50,45],
[47,44,52,45,51,51,50,0,39],
[49,50,60,52,62,53,55,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,45,50,57,57,50,51],
[47,0,45,44,51,50,49,54,51],
[50,55,0,50,50,54,53,54,62],
[55,56,50,0,49,61,57,48,55],
[50,49,50,51,0,56,51,57,46],
[43,50,46,39,44,0,49,54,44],
[43,51,47,43,49,51,0,52,48],
[50,46,46,52,43,46,48,0,53],
[49,49,38,45,54,56,52,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,68,54,71,52,45,59,56],
[47,0,53,42,51,54,53,56,47],
[32,47,0,57,68,48,52,63,43],
[46,58,43,0,48,49,49,52,60],
[29,49,32,52,0,45,45,42,50],
[48,46,52,51,55,0,43,55,49],
[55,47,48,51,55,57,0,69,51],
[41,44,37,48,58,45,31,0,47],
[44,53,57,40,50,51,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,55,60,62,63,46,53],
[45,0,45,55,53,58,53,54,46],
[44,55,0,49,48,52,57,54,50],
[45,45,51,0,55,61,58,52,47],
[40,47,52,45,0,54,57,37,42],
[38,42,48,39,46,0,46,44,30],
[37,47,43,42,43,54,0,46,44],
[54,46,46,48,63,56,54,0,45],
[47,54,50,53,58,70,56,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,49,65,52,53,52,65,61],
[41,0,45,51,47,41,52,55,50],
[51,55,0,56,53,58,49,51,60],
[35,49,44,0,47,43,42,45,50],
[48,53,47,53,0,48,44,58,59],
[47,59,42,57,52,0,48,54,57],
[48,48,51,58,56,52,0,59,58],
[35,45,49,55,42,46,41,0,52],
[39,50,40,50,41,43,42,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,45,50,48,48,41,44],
[54,0,51,54,53,50,54,47,51],
[50,49,0,51,46,42,52,50,43],
[55,46,49,0,49,52,51,44,45],
[50,47,54,51,0,54,57,43,52],
[52,50,58,48,46,0,47,41,40],
[52,46,48,49,43,53,0,48,52],
[59,53,50,56,57,59,52,0,48],
[56,49,57,55,48,60,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,41,44,60,48,48,39],
[54,0,51,51,48,53,53,62,48],
[55,49,0,44,46,53,51,52,46],
[59,49,56,0,59,62,50,63,56],
[56,52,54,41,0,57,53,53,53],
[40,47,47,38,43,0,42,51,39],
[52,47,49,50,47,58,0,56,42],
[52,38,48,37,47,49,44,0,45],
[61,52,54,44,47,61,58,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,41,43,51,42,44,42,49],
[58,0,58,53,66,60,51,46,59],
[59,42,0,50,60,52,55,48,53],
[57,47,50,0,57,48,58,50,54],
[49,34,40,43,0,38,40,41,45],
[58,40,48,52,62,0,52,48,55],
[56,49,45,42,60,48,0,42,53],
[58,54,52,50,59,52,58,0,54],
[51,41,47,46,55,45,47,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,46,56,39,59,52,50,45],
[47,0,46,56,41,54,52,46,47],
[54,54,0,61,61,64,50,53,62],
[44,44,39,0,47,54,42,61,39],
[61,59,39,53,0,59,53,48,42],
[41,46,36,46,41,0,42,45,36],
[48,48,50,58,47,58,0,51,48],
[50,54,47,39,52,55,49,0,46],
[55,53,38,61,58,64,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,38,45,54,52,56,57,52],
[51,0,50,50,56,50,58,57,49],
[62,50,0,52,56,59,60,60,59],
[55,50,48,0,56,50,48,59,56],
[46,44,44,44,0,34,59,51,45],
[48,50,41,50,66,0,55,55,59],
[44,42,40,52,41,45,0,57,48],
[43,43,40,41,49,45,43,0,44],
[48,51,41,44,55,41,52,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,55,56,56,53,57,52],
[49,0,43,49,47,49,51,53,48],
[50,57,0,51,60,50,47,51,49],
[45,51,49,0,50,48,52,50,45],
[44,53,40,50,0,46,46,56,51],
[44,51,50,52,54,0,51,44,49],
[47,49,53,48,54,49,0,54,46],
[43,47,49,50,44,56,46,0,40],
[48,52,51,55,49,51,54,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,69,32,58,45,64,40,69],
[35,0,53,36,58,62,66,52,71],
[31,47,0,40,57,45,38,37,51],
[68,64,60,0,48,72,60,50,56],
[42,42,43,52,0,58,51,47,65],
[55,38,55,28,42,0,53,33,64],
[36,34,62,40,49,47,0,23,40],
[60,48,63,50,53,67,77,0,66],
[31,29,49,44,35,36,60,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,43,51,44,28,34,34,33],
[57,0,31,55,54,42,42,44,50],
[57,69,0,56,50,51,50,57,53],
[49,45,44,0,36,31,40,25,42],
[56,46,50,64,0,40,53,52,55],
[72,58,49,69,60,0,48,57,60],
[66,58,50,60,47,52,0,56,46],
[66,56,43,75,48,43,44,0,57],
[67,50,47,58,45,40,54,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,59,65,40,53,49,49,66],
[68,0,59,56,44,51,65,68,52],
[41,41,0,52,26,46,53,46,60],
[35,44,48,0,39,40,59,34,48],
[60,56,74,61,0,50,63,54,69],
[47,49,54,60,50,0,78,64,68],
[51,35,47,41,37,22,0,41,49],
[51,32,54,66,46,36,59,0,75],
[34,48,40,52,31,32,51,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,64,64,1,26,65,26,64],
[62,0,27,26,62,62,62,26,27],
[36,73,0,35,36,36,74,35,64],
[36,74,65,0,36,36,74,1,65],
[99,38,64,64,0,99,100,64,64],
[74,38,64,64,1,0,65,38,64],
[35,38,26,26,0,35,0,0,64],
[74,74,65,99,36,62,100,0,65],
[36,73,36,35,36,36,36,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,50,60,50,55,55,64],
[54,0,42,56,49,56,59,57,57],
[58,58,0,60,48,62,53,56,69],
[50,44,40,0,47,50,55,51,49],
[40,51,52,53,0,55,58,57,65],
[50,44,38,50,45,0,58,50,53],
[45,41,47,45,42,42,0,47,54],
[45,43,44,49,43,50,53,0,64],
[36,43,31,51,35,47,46,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,50,49,55,65,57,44],
[48,0,49,47,40,58,68,55,33],
[48,51,0,41,46,50,65,52,36],
[50,53,59,0,54,54,63,55,46],
[51,60,54,46,0,47,63,52,59],
[45,42,50,46,53,0,67,50,39],
[35,32,35,37,37,33,0,35,34],
[43,45,48,45,48,50,65,0,42],
[56,67,64,54,41,61,66,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,47,48,47,48,51,59],
[51,0,48,55,54,45,50,52,53],
[47,52,0,59,43,47,50,52,53],
[53,45,41,0,45,41,54,49,58],
[52,46,57,55,0,50,53,53,60],
[53,55,53,59,50,0,59,52,57],
[52,50,50,46,47,41,0,44,54],
[49,48,48,51,47,48,56,0,56],
[41,47,47,42,40,43,46,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,77,75,56,77,75,64,77],
[59,0,59,59,59,55,78,78,36],
[23,41,0,45,23,52,75,64,11],
[25,41,55,0,11,77,52,19,36],
[44,41,77,89,0,77,52,66,77],
[23,45,48,23,23,0,64,42,48],
[25,22,25,48,48,36,0,25,36],
[36,22,36,81,34,58,75,0,36],
[23,64,89,64,23,52,64,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,52,40,39,42,39,52,41],
[46,0,45,39,42,38,42,48,42],
[48,55,0,44,44,43,37,29,32],
[60,61,56,0,48,50,52,43,47],
[61,58,56,52,0,49,48,52,42],
[58,62,57,50,51,0,51,44,43],
[61,58,63,48,52,49,0,46,54],
[48,52,71,57,48,56,54,0,45],
[59,58,68,53,58,57,46,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,48,52,55,55,56,53],
[44,0,47,52,48,51,50,49,53],
[44,53,0,53,55,56,60,56,50],
[52,48,47,0,48,52,50,55,51],
[48,52,45,52,0,52,55,56,55],
[45,49,44,48,48,0,52,53,47],
[45,50,40,50,45,48,0,48,46],
[44,51,44,45,44,47,52,0,47],
[47,47,50,49,45,53,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,46,50,44,53,58,51],
[47,0,40,48,47,45,50,55,44],
[44,60,0,35,45,50,46,59,44],
[54,52,65,0,55,48,47,52,49],
[50,53,55,45,0,50,44,53,49],
[56,55,50,52,50,0,50,63,53],
[47,50,54,53,56,50,0,46,37],
[42,45,41,48,47,37,54,0,47],
[49,56,56,51,51,47,63,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,57,57,55,52,51,54],
[54,0,47,52,51,45,46,45,41],
[49,53,0,58,56,56,51,48,45],
[43,48,42,0,53,59,42,47,43],
[43,49,44,47,0,51,44,47,51],
[45,55,44,41,49,0,51,44,47],
[48,54,49,58,56,49,0,51,51],
[49,55,52,53,53,56,49,0,42],
[46,59,55,57,49,53,49,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,47,44,30,68,50,11,67],
[43,0,34,33,30,57,58,25,43],
[53,66,0,36,66,85,42,34,50],
[56,67,64,0,47,83,47,64,78],
[70,70,34,53,0,59,59,37,56],
[32,43,15,17,41,0,42,36,48],
[50,42,58,53,41,58,0,39,72],
[89,75,66,36,63,64,61,0,56],
[33,57,50,22,44,52,28,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,53,52,52,46,47,56],
[50,0,41,53,49,53,50,52,44],
[48,59,0,59,62,50,52,53,48],
[47,47,41,0,48,43,44,47,49],
[48,51,38,52,0,47,50,47,45],
[48,47,50,57,53,0,51,50,48],
[54,50,48,56,50,49,0,50,51],
[53,48,47,53,53,50,50,0,45],
[44,56,52,51,55,52,49,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,50,45,36,38,42,50],
[67,0,60,69,60,52,50,52,56],
[72,40,0,63,42,48,56,63,68],
[50,31,37,0,42,32,43,42,57],
[55,40,58,58,0,35,51,50,62],
[64,48,52,68,65,0,64,63,69],
[62,50,44,57,49,36,0,48,58],
[58,48,37,58,50,37,52,0,58],
[50,44,32,43,38,31,42,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,65,39,50,50,45,48,58],
[60,0,50,57,67,57,52,60,61],
[35,50,0,38,78,45,59,56,75],
[61,43,62,0,60,51,62,61,66],
[50,33,22,40,0,50,47,37,40],
[50,43,55,49,50,0,47,60,63],
[55,48,41,38,53,53,0,54,43],
[52,40,44,39,63,40,46,0,63],
[42,39,25,34,60,37,57,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,49,29,29,30,29,49,30],
[90,0,90,57,82,38,57,100,71],
[51,10,0,0,10,0,0,45,28],
[71,43,100,0,82,63,57,81,81],
[71,18,90,18,0,56,37,53,71],
[70,62,100,37,44,0,37,82,82],
[71,43,100,43,63,63,0,81,81],
[51,0,55,19,47,18,19,0,36],
[70,29,72,19,29,18,19,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,68,73,23,63,89,46,52],
[26,0,34,33,20,29,76,19,21],
[32,66,0,32,20,39,60,9,28],
[27,67,68,0,10,37,87,25,22],
[77,80,80,90,0,66,88,48,63],
[37,71,61,63,34,0,79,47,55],
[11,24,40,13,12,21,0,8,9],
[54,81,91,75,52,53,92,0,47],
[48,79,72,78,37,45,91,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,57,41,64,53,43,52,44],
[40,0,57,53,61,53,43,51,40],
[43,43,0,45,51,52,42,47,49],
[59,47,55,0,71,71,51,52,47],
[36,39,49,29,0,52,39,36,43],
[47,47,48,29,48,0,35,43,53],
[57,57,58,49,61,65,0,62,65],
[48,49,53,48,64,57,38,0,46],
[56,60,51,53,57,47,35,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,63,51,48,63,57,59,51],
[46,0,61,53,61,60,50,36,43],
[37,39,0,42,37,55,40,39,44],
[49,47,58,0,54,60,49,48,43],
[52,39,63,46,0,66,46,45,50],
[37,40,45,40,34,0,40,36,42],
[43,50,60,51,54,60,0,40,44],
[41,64,61,52,55,64,60,0,49],
[49,57,56,57,50,58,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,49,49,52,55,53,61,48],
[43,0,48,47,44,50,54,59,42],
[51,52,0,47,49,58,51,65,54],
[51,53,53,0,50,58,56,60,60],
[48,56,51,50,0,50,59,55,59],
[45,50,42,42,50,0,56,62,48],
[47,46,49,44,41,44,0,55,52],
[39,41,35,40,45,38,45,0,46],
[52,58,46,40,41,52,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,57,66,54,69,54,62,46],
[36,0,52,52,43,60,43,48,43],
[43,48,0,58,43,63,53,51,42],
[34,48,42,0,38,50,35,48,24],
[46,57,57,62,0,58,39,53,56],
[31,40,37,50,42,0,48,49,41],
[46,57,47,65,61,52,0,67,54],
[38,52,49,52,47,51,33,0,41],
[54,57,58,76,44,59,46,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,43,57,48,58,46,49,50],
[53,0,41,49,58,49,45,46,50],
[57,59,0,61,52,52,49,47,61],
[43,51,39,0,48,52,42,48,43],
[52,42,48,52,0,51,35,43,46],
[42,51,48,48,49,0,35,36,43],
[54,55,51,58,65,65,0,53,49],
[51,54,53,52,57,64,47,0,56],
[50,50,39,57,54,57,51,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,55,52,60,64,50,61],
[43,0,47,44,47,53,56,49,52],
[44,53,0,53,44,56,52,50,57],
[45,56,47,0,45,53,51,50,57],
[48,53,56,55,0,56,56,49,55],
[40,47,44,47,44,0,50,52,50],
[36,44,48,49,44,50,0,49,63],
[50,51,50,50,51,48,51,0,64],
[39,48,43,43,45,50,37,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,54,60,57,48,49,51,58],
[42,0,49,56,50,52,43,57,51],
[46,51,0,62,52,51,50,55,56],
[40,44,38,0,48,32,42,43,48],
[43,50,48,52,0,49,51,57,48],
[52,48,49,68,51,0,46,52,54],
[51,57,50,58,49,54,0,64,54],
[49,43,45,57,43,48,36,0,45],
[42,49,44,52,52,46,46,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,55,48,54,45,56,45,51],
[56,0,54,52,57,47,49,49,45],
[45,46,0,52,47,45,50,51,51],
[52,48,48,0,56,47,55,56,49],
[46,43,53,44,0,43,43,44,45],
[55,53,55,53,57,0,55,48,45],
[44,51,50,45,57,45,0,51,45],
[55,51,49,44,56,52,49,0,53],
[49,55,49,51,55,55,55,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,48,59,59,50,58,53,59],
[46,0,43,54,52,52,51,55,54],
[52,57,0,56,57,50,53,57,57],
[41,46,44,0,51,35,44,45,54],
[41,48,43,49,0,42,46,49,59],
[50,48,50,65,58,0,61,62,50],
[42,49,47,56,54,39,0,53,44],
[47,45,43,55,51,38,47,0,48],
[41,46,43,46,41,50,56,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,46,48,50,55,43,51],
[51,0,50,52,46,56,55,50,51],
[53,50,0,47,51,44,56,46,57],
[54,48,53,0,42,48,52,47,52],
[52,54,49,58,0,51,55,50,52],
[50,44,56,52,49,0,54,46,54],
[45,45,44,48,45,46,0,41,48],
[57,50,54,53,50,54,59,0,59],
[49,49,43,48,48,46,52,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,46,57,55,58,48,48,51],
[45,0,42,52,47,51,42,49,48],
[54,58,0,56,64,53,62,62,50],
[43,48,44,0,50,47,46,59,45],
[45,53,36,50,0,42,50,48,43],
[42,49,47,53,58,0,46,56,36],
[52,58,38,54,50,54,0,50,44],
[52,51,38,41,52,44,50,0,35],
[49,52,50,55,57,64,56,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,19,62,24,0,20,13,27],
[42,0,27,61,27,12,27,34,24],
[81,73,0,62,81,50,38,51,66],
[38,39,38,0,47,30,26,46,50],
[76,73,19,53,0,30,30,31,43],
[100,88,50,70,70,0,38,54,51],
[80,73,62,74,70,62,0,40,62],
[87,66,49,54,69,46,60,0,47],
[73,76,34,50,57,49,38,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,48,42,50,50,45,42,51],
[56,0,54,54,57,50,46,52,48],
[52,46,0,49,55,53,48,51,44],
[58,46,51,0,53,54,50,40,45],
[50,43,45,47,0,46,47,45,46],
[50,50,47,46,54,0,50,42,47],
[55,54,52,50,53,50,0,45,44],
[58,48,49,60,55,58,55,0,43],
[49,52,56,55,54,53,56,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,29,19,16,34,28,14,22],
[51,0,33,39,32,47,58,46,46],
[71,67,0,43,45,50,57,49,45],
[81,61,57,0,50,62,74,56,67],
[84,68,55,50,0,64,79,52,69],
[66,53,50,38,36,0,62,36,35],
[72,42,43,26,21,38,0,22,42],
[86,54,51,44,48,64,78,0,70],
[78,54,55,33,31,65,58,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,18,45,40,42,55,51,40],
[63,0,25,51,50,58,56,49,75],
[82,75,0,46,57,73,49,60,69],
[55,49,54,0,56,61,62,50,69],
[60,50,43,44,0,64,74,49,75],
[58,42,27,39,36,0,55,37,58],
[45,44,51,38,26,45,0,46,46],
[49,51,40,50,51,63,54,0,67],
[60,25,31,31,25,42,54,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,44,56,58,55,67,49,53],
[40,0,39,66,40,37,46,30,36],
[56,61,0,63,67,48,56,47,46],
[44,34,37,0,34,38,51,37,37],
[42,60,33,66,0,54,51,42,41],
[45,63,52,62,46,0,59,40,39],
[33,54,44,49,49,41,0,35,39],
[51,70,53,63,58,60,65,0,45],
[47,64,54,63,59,61,61,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,45,57,56,51,75,73,36],
[52,0,54,50,65,54,78,64,54],
[55,46,0,43,51,67,64,67,46],
[43,50,57,0,66,44,68,68,51],
[44,35,49,34,0,55,75,70,47],
[49,46,33,56,45,0,59,65,40],
[25,22,36,32,25,41,0,36,36],
[27,36,33,32,30,35,64,0,37],
[64,46,54,49,53,60,64,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,60,73,65,83,59,68,33],
[39,0,42,64,59,85,29,54,49],
[40,58,0,51,62,96,51,65,52],
[27,36,49,0,45,80,34,65,30],
[35,41,38,55,0,76,26,33,28],
[17,15,4,20,24,0,13,41,8],
[41,71,49,66,74,87,0,48,29],
[32,46,35,35,67,59,52,0,51],
[67,51,48,70,72,92,71,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,36,28,33,40,39,24,21],
[49,0,43,36,21,49,49,27,36],
[64,57,0,31,33,44,46,51,44],
[72,64,69,0,53,56,74,60,45],
[67,79,67,47,0,58,63,52,54],
[60,51,56,44,42,0,48,35,41],
[61,51,54,26,37,52,0,41,32],
[76,73,49,40,48,65,59,0,37],
[79,64,56,55,46,59,68,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,59,54,40,62,62,54,40],
[34,0,49,39,40,59,48,45,37],
[41,51,0,52,39,50,46,53,45],
[46,61,48,0,40,61,52,58,41],
[60,60,61,60,0,49,57,54,51],
[38,41,50,39,51,0,51,47,43],
[38,52,54,48,43,49,0,35,40],
[46,55,47,42,46,53,65,0,44],
[60,63,55,59,49,57,60,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,45,50,51,41,44,46,52],
[52,0,46,54,54,40,49,44,52],
[55,54,0,50,56,48,52,50,53],
[50,46,50,0,63,45,55,42,51],
[49,46,44,37,0,41,48,52,49],
[59,60,52,55,59,0,54,50,57],
[56,51,48,45,52,46,0,47,44],
[54,56,50,58,48,50,53,0,53],
[48,48,47,49,51,43,56,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,46,56,64,61,66,50,57],
[50,0,45,51,66,62,64,53,50],
[54,55,0,55,64,61,67,47,57],
[44,49,45,0,69,59,50,38,44],
[36,34,36,31,0,46,42,44,44],
[39,38,39,41,54,0,41,31,47],
[34,36,33,50,58,59,0,44,39],
[50,47,53,62,56,69,56,0,42],
[43,50,43,56,56,53,61,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,52,49,38,53,64,38,40],
[57,0,50,55,57,69,60,56,61],
[48,50,0,48,56,58,72,54,68],
[51,45,52,0,47,44,58,44,52],
[62,43,44,53,0,50,59,50,48],
[47,31,42,56,50,0,56,28,35],
[36,40,28,42,41,44,0,47,43],
[62,44,46,56,50,72,53,0,67],
[60,39,32,48,52,65,57,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,32,50,32,32,39,47,32],
[89,0,39,74,32,74,39,54,32],
[68,61,0,85,44,89,51,25,58],
[50,26,15,0,15,47,44,18,47],
[68,68,56,85,0,100,100,36,100],
[68,26,11,53,0,0,47,33,14],
[61,61,49,56,0,53,0,29,14],
[53,46,75,82,64,67,71,0,78],
[68,68,42,53,0,86,86,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,50,57,63,55,68,60,54],
[39,0,55,51,43,46,61,53,39],
[50,45,0,52,53,43,61,59,47],
[43,49,48,0,52,55,64,51,41],
[37,57,47,48,0,48,66,51,42],
[45,54,57,45,52,0,60,58,46],
[32,39,39,36,34,40,0,45,32],
[40,47,41,49,49,42,55,0,39],
[46,61,53,59,58,54,68,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,33,42,45,45,31,47,49],
[86,0,60,67,61,46,59,58,61],
[67,40,0,53,73,53,50,45,61],
[58,33,47,0,45,46,56,45,61],
[55,39,27,55,0,53,50,40,68],
[55,54,47,54,47,0,46,48,48],
[69,41,50,44,50,54,0,47,62],
[53,42,55,55,60,52,53,0,41],
[51,39,39,39,32,52,38,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,66,36,39,38,60,39,53],
[44,0,47,41,25,37,55,38,42],
[34,53,0,45,39,35,44,44,37],
[64,59,55,0,46,51,62,44,48],
[61,75,61,54,0,53,68,50,53],
[62,63,65,49,47,0,50,53,59],
[40,45,56,38,32,50,0,41,31],
[61,62,56,56,50,47,59,0,48],
[47,58,63,52,47,41,69,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,59,54,52,53,42,56,63],
[44,0,45,44,43,51,39,54,54],
[41,55,0,47,41,43,40,43,49],
[46,56,53,0,57,45,47,54,62],
[48,57,59,43,0,46,39,48,64],
[47,49,57,55,54,0,51,54,58],
[58,61,60,53,61,49,0,52,66],
[44,46,57,46,52,46,48,0,56],
[37,46,51,38,36,42,34,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,65,57,69,51,61,43,59],
[39,0,35,34,42,35,49,33,48],
[35,65,0,44,44,50,54,43,44],
[43,66,56,0,50,44,56,54,50],
[31,58,56,50,0,46,48,38,58],
[49,65,50,56,54,0,53,39,47],
[39,51,46,44,52,47,0,41,57],
[57,67,57,46,62,61,59,0,54],
[41,52,56,50,42,53,43,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,52,48,50,61,50,58],
[50,0,50,50,50,51,56,58,59],
[43,50,0,45,48,48,53,54,46],
[48,50,55,0,52,54,56,55,52],
[52,50,52,48,0,53,55,51,56],
[50,49,52,46,47,0,64,56,57],
[39,44,47,44,45,36,0,46,55],
[50,42,46,45,49,44,54,0,52],
[42,41,54,48,44,43,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,52,51,43,47,48,56,51],
[38,0,51,48,46,45,40,51,49],
[48,49,0,54,46,52,43,52,49],
[49,52,46,0,46,53,48,46,47],
[57,54,54,54,0,56,49,56,53],
[53,55,48,47,44,0,51,53,45],
[52,60,57,52,51,49,0,60,54],
[44,49,48,54,44,47,40,0,44],
[49,51,51,53,47,55,46,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,69,73,41,53,24,88,72],
[63,0,57,75,35,56,56,69,81],
[31,43,0,24,29,71,43,88,50],
[27,25,76,0,54,53,20,70,60],
[59,65,71,46,0,48,65,83,72],
[47,44,29,47,52,0,39,55,39],
[76,44,57,80,35,61,0,74,80],
[12,31,12,30,17,45,26,0,49],
[28,19,50,40,28,61,20,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,69,48,57,51,59,71,67],
[47,0,47,41,57,41,61,39,77],
[31,53,0,56,39,42,49,66,69],
[52,59,44,0,52,54,56,51,78],
[43,43,61,48,0,39,59,65,54],
[49,59,58,46,61,0,63,46,88],
[41,39,51,44,41,37,0,45,69],
[29,61,34,49,35,54,55,0,63],
[33,23,31,22,46,12,31,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,53,61,47,55,51,53],
[44,0,50,41,56,40,47,37,38],
[47,50,0,43,53,37,51,34,57],
[47,59,57,0,61,43,56,41,53],
[39,44,47,39,0,45,37,37,44],
[53,60,63,57,55,0,58,48,54],
[45,53,49,44,63,42,0,39,48],
[49,63,66,59,63,52,61,0,61],
[47,62,43,47,56,46,52,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,38,49,51,65,40,36,63],
[55,0,38,54,44,55,39,43,41],
[62,62,0,43,57,61,41,39,43],
[51,46,57,0,59,51,50,46,46],
[49,56,43,41,0,54,47,31,39],
[35,45,39,49,46,0,35,27,34],
[60,61,59,50,53,65,0,54,41],
[64,57,61,54,69,73,46,0,42],
[37,59,57,54,61,66,59,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,55,46,46,37,53,46],
[51,0,43,52,55,51,44,42,48],
[47,57,0,48,47,46,44,41,44],
[45,48,52,0,37,49,42,46,59],
[54,45,53,63,0,47,48,52,47],
[54,49,54,51,53,0,49,54,55],
[63,56,56,58,52,51,0,47,41],
[47,58,59,54,48,46,53,0,47],
[54,52,56,41,53,45,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,44,41,40,44,47,44,39],
[54,0,52,50,46,45,49,49,51],
[56,48,0,43,49,45,54,55,53],
[59,50,57,0,53,54,53,54,55],
[60,54,51,47,0,46,50,48,53],
[56,55,55,46,54,0,53,53,51],
[53,51,46,47,50,47,0,48,51],
[56,51,45,46,52,47,52,0,52],
[61,49,47,45,47,49,49,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,41,39,44,45,52,45,38],
[56,0,40,50,59,52,57,51,46],
[59,60,0,56,52,50,58,56,59],
[61,50,44,0,49,53,57,50,43],
[56,41,48,51,0,45,55,54,51],
[55,48,50,47,55,0,51,46,44],
[48,43,42,43,45,49,0,38,42],
[55,49,44,50,46,54,62,0,51],
[62,54,41,57,49,56,58,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,51,46,47,57,52,51,44],
[52,0,56,51,53,57,59,49,51],
[49,44,0,45,39,45,45,39,49],
[54,49,55,0,44,58,52,49,52],
[53,47,61,56,0,59,53,48,51],
[43,43,55,42,41,0,41,41,41],
[48,41,55,48,47,59,0,43,44],
[49,51,61,51,52,59,57,0,54],
[56,49,51,48,49,59,56,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,33,41,49,44,34,35],
[71,0,43,48,40,82,49,43,50],
[71,57,0,46,46,74,62,54,48],
[67,52,54,0,43,56,82,48,53],
[59,60,54,57,0,92,67,54,36],
[51,18,26,44,8,0,59,43,25],
[56,51,38,18,33,41,0,11,18],
[66,57,46,52,46,57,89,0,18],
[65,50,52,47,64,75,82,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,51,49,58,52,50,49,52],
[40,0,42,45,54,47,44,56,47],
[49,58,0,52,59,60,59,59,52],
[51,55,48,0,51,45,51,50,53],
[42,46,41,49,0,42,45,54,46],
[48,53,40,55,58,0,44,56,50],
[50,56,41,49,55,56,0,46,46],
[51,44,41,50,46,44,54,0,44],
[48,53,48,47,54,50,54,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,57,65,54,60,44,52,60],
[45,0,59,55,56,60,51,45,58],
[43,41,0,42,43,49,37,41,50],
[35,45,58,0,45,56,36,45,50],
[46,44,57,55,0,55,42,58,54],
[40,40,51,44,45,0,29,37,42],
[56,49,63,64,58,71,0,58,51],
[48,55,59,55,42,63,42,0,50],
[40,42,50,50,46,58,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,39,33,28,27,35,50,36],
[54,0,41,25,40,42,37,50,41],
[61,59,0,47,48,59,46,65,54],
[67,75,53,0,42,53,56,65,59],
[72,60,52,58,0,56,45,50,52],
[73,58,41,47,44,0,50,57,44],
[65,63,54,44,55,50,0,57,58],
[50,50,35,35,50,43,43,0,49],
[64,59,46,41,48,56,42,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,49,49,51,48,47,43],
[54,0,45,53,56,53,53,53,46],
[55,55,0,60,48,50,48,48,46],
[51,47,40,0,50,51,49,50,41],
[51,44,52,50,0,52,47,43,50],
[49,47,50,49,48,0,45,42,45],
[52,47,52,51,53,55,0,50,40],
[53,47,52,50,57,58,50,0,51],
[57,54,54,59,50,55,60,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,49,67,59,61,60,65,54],
[42,0,42,53,43,50,47,55,50],
[51,58,0,59,58,50,50,62,51],
[33,47,41,0,39,39,45,59,47],
[41,57,42,61,0,52,49,59,53],
[39,50,50,61,48,0,46,53,50],
[40,53,50,55,51,54,0,52,59],
[35,45,38,41,41,47,48,0,47],
[46,50,49,53,47,50,41,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,60,46,52,55,51,56,58],
[58,0,62,50,65,62,56,61,54],
[40,38,0,52,53,42,49,48,43],
[54,50,48,0,54,51,48,49,50],
[48,35,47,46,0,47,49,46,44],
[45,38,58,49,53,0,53,45,49],
[49,44,51,52,51,47,0,44,46],
[44,39,52,51,54,55,56,0,47],
[42,46,57,50,56,51,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,57,52,53,46,56,61,51],
[47,0,52,45,57,48,63,56,51],
[43,48,0,48,49,46,49,45,47],
[48,55,52,0,58,44,53,56,46],
[47,43,51,42,0,45,48,52,49],
[54,52,54,56,55,0,57,57,46],
[44,37,51,47,52,43,0,49,48],
[39,44,55,44,48,43,51,0,50],
[49,49,53,54,51,54,52,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,36,64,39,53,47,44,41],
[34,0,27,43,30,39,36,45,48],
[64,73,0,58,35,76,43,54,67],
[36,57,42,0,46,65,49,36,62],
[61,70,65,54,0,82,46,59,64],
[47,61,24,35,18,0,37,31,45],
[53,64,57,51,54,63,0,44,60],
[56,55,46,64,41,69,56,0,56],
[59,52,33,38,36,55,40,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,42,63,62,74,57,61,68],
[42,0,48,53,48,73,62,55,47],
[58,52,0,59,74,50,42,53,70],
[37,47,41,0,50,45,44,22,53],
[38,52,26,50,0,47,47,53,60],
[26,27,50,55,53,0,47,57,51],
[43,38,58,56,53,53,0,58,75],
[39,45,47,78,47,43,42,0,50],
[32,53,30,47,40,49,25,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,49,43,55,46,44,44],
[44,0,50,48,50,53,52,45,48],
[51,50,0,52,46,47,50,45,52],
[51,52,48,0,47,45,47,48,51],
[57,50,54,53,0,56,56,52,50],
[45,47,53,55,44,0,46,38,53],
[54,48,50,53,44,54,0,42,52],
[56,55,55,52,48,62,58,0,51],
[56,52,48,49,50,47,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,41,46,41,48,56,55],
[48,0,62,49,40,38,51,44,48],
[44,38,0,44,35,33,44,48,43],
[59,51,56,0,45,45,46,57,43],
[54,60,65,55,0,48,50,57,54],
[59,62,67,55,52,0,55,61,45],
[52,49,56,54,50,45,0,50,51],
[44,56,52,43,43,39,50,0,47],
[45,52,57,57,46,55,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,30,54,38,41,54,48,49],
[46,0,44,52,40,48,50,53,43],
[70,56,0,56,65,45,54,61,57],
[46,48,44,0,47,42,39,47,46],
[62,60,35,53,0,50,56,51,49],
[59,52,55,58,50,0,58,47,55],
[46,50,46,61,44,42,0,51,47],
[52,47,39,53,49,53,49,0,44],
[51,57,43,54,51,45,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,52,51,50,54,46,41],
[53,0,52,47,50,54,53,47,46],
[51,48,0,44,55,49,60,51,50],
[48,53,56,0,48,50,50,47,47],
[49,50,45,52,0,48,58,44,45],
[50,46,51,50,52,0,56,42,45],
[46,47,40,50,42,44,0,42,42],
[54,53,49,53,56,58,58,0,50],
[59,54,50,53,55,55,58,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,47,38,42,41,59,53,38],
[56,0,43,50,35,42,59,49,51],
[53,57,0,42,43,35,52,36,46],
[62,50,58,0,41,55,61,61,47],
[58,65,57,59,0,49,58,56,53],
[59,58,65,45,51,0,42,56,44],
[41,41,48,39,42,58,0,46,42],
[47,51,64,39,44,44,54,0,49],
[62,49,54,53,47,56,58,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,47,48,47,52,46,47,55],
[58,0,56,49,54,50,58,59,60],
[53,44,0,46,46,53,50,46,46],
[52,51,54,0,50,49,56,52,56],
[53,46,54,50,0,51,56,48,57],
[48,50,47,51,49,0,56,53,54],
[54,42,50,44,44,44,0,47,54],
[53,41,54,48,52,47,53,0,53],
[45,40,54,44,43,46,46,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,49,36,35,51,34,54],
[54,0,58,48,53,59,56,46,50],
[58,42,0,47,47,48,60,41,60],
[51,52,53,0,41,45,56,49,53],
[64,47,53,59,0,45,61,52,60],
[65,41,52,55,55,0,55,43,64],
[49,44,40,44,39,45,0,39,53],
[66,54,59,51,48,57,61,0,62],
[46,50,40,47,40,36,47,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,53,51,57,46,56,44,56],
[35,0,41,67,45,61,57,70,54],
[47,59,0,66,38,70,58,67,67],
[49,33,34,0,26,31,36,18,53],
[43,55,62,74,0,66,48,79,53],
[54,39,30,69,34,0,65,49,47],
[44,43,42,64,52,35,0,43,47],
[56,30,33,82,21,51,57,0,66],
[44,46,33,47,47,53,53,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,63,49,21,56,63,51],
[52,0,50,67,67,40,70,80,54],
[54,50,0,39,68,54,45,60,55],
[37,33,61,0,50,25,69,73,60],
[51,33,32,50,0,36,53,58,45],
[79,60,46,75,64,0,73,76,57],
[44,30,55,31,47,27,0,45,35],
[37,20,40,27,42,24,55,0,42],
[49,46,45,40,55,43,65,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,51,57,56,51,58,52],
[46,0,46,45,50,39,35,52,41],
[54,54,0,63,54,49,50,65,50],
[49,55,37,0,50,52,43,65,32],
[43,50,46,50,0,42,33,53,49],
[44,61,51,48,58,0,47,45,55],
[49,65,50,57,67,53,0,65,61],
[42,48,35,35,47,55,35,0,43],
[48,59,50,68,51,45,39,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,49,54,51,51,50,52],
[47,0,40,50,57,41,45,44,39],
[56,60,0,57,64,49,49,46,51],
[51,50,43,0,59,43,45,42,48],
[46,43,36,41,0,47,41,41,48],
[49,59,51,57,53,0,48,48,53],
[49,55,51,55,59,52,0,48,51],
[50,56,54,58,59,52,52,0,51],
[48,61,49,52,52,47,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,50,41,47,47,57,56,46],
[46,0,40,43,46,52,39,48,51],
[50,60,0,36,52,49,49,51,44],
[59,57,64,0,47,59,52,53,52],
[53,54,48,53,0,44,54,53,49],
[53,48,51,41,56,0,51,52,53],
[43,61,51,48,46,49,0,46,48],
[44,52,49,47,47,48,54,0,46],
[54,49,56,48,51,47,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,43,40,62,51,51,55,53],
[52,0,53,50,63,55,43,41,54],
[57,47,0,42,62,52,50,52,48],
[60,50,58,0,63,55,53,58,55],
[38,37,38,37,0,34,34,37,49],
[49,45,48,45,66,0,51,48,56],
[49,57,50,47,66,49,0,50,53],
[45,59,48,42,63,52,50,0,48],
[47,46,52,45,51,44,47,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,60,27,73,59,73,72,54],
[47,0,60,28,46,20,60,33,33],
[40,40,0,54,54,40,54,32,14],
[73,72,46,0,46,46,46,45,46],
[27,54,46,54,0,46,40,19,0],
[41,80,60,54,54,0,41,45,14],
[27,40,46,54,60,59,0,32,14],
[28,67,68,55,81,55,68,0,41],
[46,67,86,54,100,86,86,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,56,41,50,46,45,56],
[44,0,55,57,53,57,55,54,37],
[49,45,0,50,53,42,42,55,45],
[44,43,50,0,47,53,40,55,51],
[59,47,47,53,0,54,41,41,43],
[50,43,58,47,46,0,41,57,40],
[54,45,58,60,59,59,0,55,57],
[55,46,45,45,59,43,45,0,49],
[44,63,55,49,57,60,43,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,52,52,50,41,40,55,40],
[57,0,62,48,58,46,57,56,50],
[48,38,0,49,51,44,47,52,55],
[48,52,51,0,53,36,46,61,60],
[50,42,49,47,0,40,51,59,48],
[59,54,56,64,60,0,55,64,50],
[60,43,53,54,49,45,0,56,45],
[45,44,48,39,41,36,44,0,42],
[60,50,45,40,52,50,55,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,52,38,48,49,46,49,47],
[55,0,55,41,42,57,53,54,46],
[48,45,0,45,48,57,57,45,48],
[62,59,55,0,57,66,58,57,49],
[52,58,52,43,0,65,56,44,49],
[51,43,43,34,35,0,46,43,51],
[54,47,43,42,44,54,0,62,43],
[51,46,55,43,56,57,38,0,42],
[53,54,52,51,51,49,57,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,38,44,23,22,38,38,19],
[60,0,38,62,22,44,37,38,50],
[62,62,0,55,37,33,44,53,36],
[56,38,45,0,38,16,44,26,38],
[77,78,63,62,0,60,44,72,63],
[78,56,67,84,40,0,48,48,60],
[62,63,56,56,56,52,0,45,41],
[62,62,47,74,28,52,55,0,28],
[81,50,64,62,37,40,59,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,54,61,59,57,56,55,64],
[50,0,51,70,53,65,53,56,62],
[46,49,0,55,41,57,53,54,51],
[39,30,45,0,45,49,45,54,47],
[41,47,59,55,0,58,58,64,55],
[43,35,43,51,42,0,48,49,47],
[44,47,47,55,42,52,0,54,54],
[45,44,46,46,36,51,46,0,48],
[36,38,49,53,45,53,46,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,45,52,58,53,50,45,41],
[42,0,47,52,48,47,52,47,48],
[55,53,0,57,46,48,58,48,45],
[48,48,43,0,46,45,49,47,39],
[42,52,54,54,0,47,54,43,51],
[47,53,52,55,53,0,52,51,47],
[50,48,42,51,46,48,0,46,42],
[55,53,52,53,57,49,54,0,54],
[59,52,55,61,49,53,58,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,41,47,50,44,53,51,51],
[55,0,48,47,42,53,46,40,47],
[59,52,0,52,46,54,59,51,52],
[53,53,48,0,56,56,49,54,52],
[50,58,54,44,0,53,50,53,50],
[56,47,46,44,47,0,55,47,52],
[47,54,41,51,50,45,0,42,47],
[49,60,49,46,47,53,58,0,54],
[49,53,48,48,50,48,53,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,57,44,36,55,54,45,45],
[65,0,51,52,41,57,64,45,45],
[43,49,0,41,36,54,56,46,43],
[56,48,59,0,42,57,64,54,56],
[64,59,64,58,0,57,56,44,44],
[45,43,46,43,43,0,57,44,47],
[46,36,44,36,44,43,0,35,47],
[55,55,54,46,56,56,65,0,61],
[55,55,57,44,56,53,53,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,32,60,31,45,23,34,25],
[87,0,52,77,54,64,50,64,66],
[68,48,0,50,35,65,45,68,49],
[40,23,50,0,25,63,41,48,55],
[69,46,65,75,0,72,43,53,67],
[55,36,35,37,28,0,30,27,34],
[77,50,55,59,57,70,0,85,59],
[66,36,32,52,47,73,15,0,29],
[75,34,51,45,33,66,41,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,51,50,63,48,65,55],
[47,0,47,43,46,63,46,58,53],
[47,53,0,51,42,55,45,52,48],
[49,57,49,0,41,52,41,58,41],
[50,54,58,59,0,59,50,66,57],
[37,37,45,48,41,0,38,56,46],
[52,54,55,59,50,62,0,62,59],
[35,42,48,42,34,44,38,0,46],
[45,47,52,59,43,54,41,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,38,39,28,44,43,51,42],
[52,0,51,39,39,45,45,47,47],
[62,49,0,50,38,42,53,51,53],
[61,61,50,0,58,50,54,55,45],
[72,61,62,42,0,54,56,58,59],
[56,55,58,50,46,0,50,59,52],
[57,55,47,46,44,50,0,56,59],
[49,53,49,45,42,41,44,0,44],
[58,53,47,55,41,48,41,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,53,55,54,55,53,48,57],
[43,0,46,51,38,45,53,45,54],
[47,54,0,53,47,39,52,47,53],
[45,49,47,0,50,47,51,49,52],
[46,62,53,50,0,51,60,47,54],
[45,55,61,53,49,0,54,50,53],
[47,47,48,49,40,46,0,42,48],
[52,55,53,51,53,50,58,0,59],
[43,46,47,48,46,47,52,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,48,44,55,56,55,49,54],
[49,0,46,43,50,46,51,50,53],
[52,54,0,47,50,48,47,49,43],
[56,57,53,0,54,56,56,57,48],
[45,50,50,46,0,49,48,46,50],
[44,54,52,44,51,0,49,52,42],
[45,49,53,44,52,51,0,53,44],
[51,50,51,43,54,48,47,0,43],
[46,47,57,52,50,58,56,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,39,49,63,52,45,55,45],
[54,0,54,57,56,54,48,56,45],
[61,46,0,50,52,51,37,46,46],
[51,43,50,0,57,53,45,44,39],
[37,44,48,43,0,49,45,56,49],
[48,46,49,47,51,0,55,57,50],
[55,52,63,55,55,45,0,52,48],
[45,44,54,56,44,43,48,0,51],
[55,55,54,61,51,50,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,62,57,61,53,49,55,43],
[51,0,56,49,53,55,48,47,43],
[38,44,0,52,57,53,43,45,41],
[43,51,48,0,49,49,35,43,36],
[39,47,43,51,0,46,39,33,39],
[47,45,47,51,54,0,42,38,39],
[51,52,57,65,61,58,0,46,42],
[45,53,55,57,67,62,54,0,52],
[57,57,59,64,61,61,58,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,50,56,52,68,46,54,59],
[55,0,54,60,43,64,39,52,49],
[50,46,0,49,44,58,53,62,50],
[44,40,51,0,55,61,52,44,54],
[48,57,56,45,0,67,47,49,52],
[32,36,42,39,33,0,43,54,41],
[54,61,47,48,53,57,0,53,51],
[46,48,38,56,51,46,47,0,51],
[41,51,50,46,48,59,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,46,45,51,49,46,46],
[54,0,55,54,50,54,50,46,49],
[50,45,0,52,48,45,51,47,42],
[54,46,48,0,53,54,53,48,44],
[55,50,52,47,0,55,47,52,48],
[49,46,55,46,45,0,44,37,39],
[51,50,49,47,53,56,0,46,44],
[54,54,53,52,48,63,54,0,50],
[54,51,58,56,52,61,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,45,47,56,50,53,43],
[45,0,48,56,50,43,46,51,51],
[44,52,0,51,44,40,45,49,45],
[55,44,49,0,46,42,46,48,47],
[53,50,56,54,0,49,49,51,48],
[44,57,60,58,51,0,44,57,47],
[50,54,55,54,51,56,0,53,54],
[47,49,51,52,49,43,47,0,54],
[57,49,55,53,52,53,46,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,0,43,43,44,0,57,100],
[56,0,13,56,56,57,56,57,100],
[100,87,0,56,43,57,56,57,100],
[57,44,44,0,87,44,13,57,100],
[57,44,57,13,0,57,13,57,57],
[56,43,43,56,43,0,56,100,100],
[100,44,44,87,87,44,0,57,100],
[43,43,43,43,43,0,43,0,100],
[0,0,0,0,43,0,0,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,45,48,41,46,51,44],
[49,0,51,44,47,45,44,43,44],
[54,49,0,49,49,45,46,51,51],
[55,56,51,0,53,47,52,53,51],
[52,53,51,47,0,40,44,44,49],
[59,55,55,53,60,0,53,43,54],
[54,56,54,48,56,47,0,46,55],
[49,57,49,47,56,57,54,0,51],
[56,56,49,49,51,46,45,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,46,49,48,44,57,46],
[51,0,41,51,52,51,54,66,52],
[50,59,0,63,58,46,52,60,49],
[54,49,37,0,49,42,44,65,42],
[51,48,42,51,0,43,52,63,47],
[52,49,54,58,57,0,54,67,51],
[56,46,48,56,48,46,0,64,49],
[43,34,40,35,37,33,36,0,39],
[54,48,51,58,53,49,51,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,53,54,65,52,52,56],
[49,0,47,51,43,55,49,53,54],
[50,53,0,45,48,56,53,56,50],
[47,49,55,0,52,59,56,51,58],
[46,57,52,48,0,61,58,61,55],
[35,45,44,41,39,0,47,50,50],
[48,51,47,44,42,53,0,47,52],
[48,47,44,49,39,50,53,0,51],
[44,46,50,42,45,50,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,43,47,57,58,54,60],
[47,0,42,49,50,56,49,46,52],
[55,58,0,49,53,60,55,52,53],
[57,51,51,0,62,66,44,58,63],
[53,50,47,38,0,63,45,42,54],
[43,44,40,34,37,0,49,42,46],
[42,51,45,56,55,51,0,49,51],
[46,54,48,42,58,58,51,0,56],
[40,48,47,37,46,54,49,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,61,43,58,54,47,56,57],
[50,0,70,57,62,60,62,58,74],
[39,30,0,37,40,46,43,38,52],
[57,43,63,0,63,60,50,64,65],
[42,38,60,37,0,47,58,53,59],
[46,40,54,40,53,0,41,58,61],
[53,38,57,50,42,59,0,45,57],
[44,42,62,36,47,42,55,0,54],
[43,26,48,35,41,39,43,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,0,26,0,0,24,10,0],
[81,0,30,50,24,40,81,67,64],
[100,70,0,50,24,86,100,86,83],
[74,50,50,0,57,74,50,36,57],
[100,76,76,43,0,76,76,62,83],
[100,60,14,26,24,0,57,46,64],
[76,19,0,50,24,43,0,46,24],
[90,33,14,64,38,54,54,0,54],
[100,36,17,43,17,36,76,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,55,54,55,59,51,46],
[49,0,56,61,56,53,58,46,47],
[48,44,0,53,52,42,46,45,38],
[45,39,47,0,48,43,57,39,38],
[46,44,48,52,0,42,58,36,47],
[45,47,58,57,58,0,56,44,46],
[41,42,54,43,42,44,0,38,33],
[49,54,55,61,64,56,62,0,53],
[54,53,62,62,53,54,67,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,61,50,67,58,49,44,58],
[42,0,54,53,69,49,46,38,45],
[39,46,0,53,53,43,45,46,39],
[50,47,47,0,58,42,51,41,35],
[33,31,47,42,0,47,35,33,31],
[42,51,57,58,53,0,55,55,39],
[51,54,55,49,65,45,0,53,42],
[56,62,54,59,67,45,47,0,47],
[42,55,61,65,69,61,58,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,40,59,51,35,40,52,46],
[60,0,51,55,41,55,53,72,54],
[60,49,0,50,47,52,49,70,50],
[41,45,50,0,50,39,30,63,41],
[49,59,53,50,0,55,41,60,40],
[65,45,48,61,45,0,55,74,51],
[60,47,51,70,59,45,0,62,72],
[48,28,30,37,40,26,38,0,34],
[54,46,50,59,60,49,28,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,58,43,58,63,57,42],
[41,0,47,84,69,63,42,83,68],
[52,53,0,37,43,37,37,52,21],
[42,16,63,0,47,42,42,78,42],
[57,31,57,53,0,63,58,52,21],
[42,37,63,58,37,0,58,73,42],
[37,58,63,58,42,42,0,73,42],
[43,17,48,22,48,27,27,0,22],
[58,32,79,58,79,58,58,78,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,52,43,40,50,50,47],
[48,0,51,59,43,50,45,45,52],
[54,49,0,65,48,41,49,58,49],
[48,41,35,0,40,30,41,43,45],
[57,57,52,60,0,49,50,49,55],
[60,50,59,70,51,0,55,51,62],
[50,55,51,59,50,45,0,60,48],
[50,55,42,57,51,49,40,0,55],
[53,48,51,55,45,38,52,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,54,59,56,49,44,54,53],
[48,0,56,54,48,49,52,49,46],
[46,44,0,48,52,43,42,46,59],
[41,46,52,0,48,43,51,48,47],
[44,52,48,52,0,42,47,47,53],
[51,51,57,57,58,0,53,48,49],
[56,48,58,49,53,47,0,46,51],
[46,51,54,52,53,52,54,0,51],
[47,54,41,53,47,51,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,38,35,37,30,31,39],
[68,0,49,49,38,54,45,34,49],
[70,51,0,56,51,60,62,45,58],
[62,51,44,0,43,48,45,56,44],
[65,62,49,57,0,64,57,51,65],
[63,46,40,52,36,0,48,48,52],
[70,55,38,55,43,52,0,62,67],
[69,66,55,44,49,52,38,0,52],
[61,51,42,56,35,48,33,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,49,44,46,53,41,55,53],
[56,0,52,53,44,63,51,55,41],
[51,48,0,48,37,59,39,43,40],
[56,47,52,0,54,59,44,53,53],
[54,56,63,46,0,55,50,53,60],
[47,37,41,41,45,0,32,42,39],
[59,49,61,56,50,68,0,53,47],
[45,45,57,47,47,58,47,0,50],
[47,59,60,47,40,61,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,47,53,54,59,58,56,52],
[58,0,61,52,50,63,65,71,57],
[53,39,0,55,54,51,61,46,50],
[47,48,45,0,62,54,57,52,61],
[46,50,46,38,0,55,64,50,51],
[41,37,49,46,45,0,58,62,72],
[42,35,39,43,36,42,0,48,52],
[44,29,54,48,50,38,52,0,53],
[48,43,50,39,49,28,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,44,52,46,47,45,39,48],
[56,0,54,54,56,51,56,46,56],
[56,46,0,48,46,52,45,48,48],
[48,46,52,0,48,51,43,49,55],
[54,44,54,52,0,52,46,50,51],
[53,49,48,49,48,0,47,44,45],
[55,44,55,57,54,53,0,51,51],
[61,54,52,51,50,56,49,0,54],
[52,44,52,45,49,55,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,58,40,47,41,40,46,44],
[54,0,58,55,48,51,48,49,54],
[42,42,0,51,48,49,33,49,45],
[60,45,49,0,54,57,50,52,51],
[53,52,52,46,0,45,41,38,48],
[59,49,51,43,55,0,50,49,48],
[60,52,67,50,59,50,0,47,55],
[54,51,51,48,62,51,53,0,53],
[56,46,55,49,52,52,45,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,36,59,43,40,46,54,58],
[46,0,42,46,48,41,45,53,58],
[64,58,0,58,45,44,61,50,59],
[41,54,42,0,40,48,56,49,63],
[57,52,55,60,0,48,58,57,53],
[60,59,56,52,52,0,61,48,61],
[54,55,39,44,42,39,0,45,66],
[46,47,50,51,43,52,55,0,63],
[42,42,41,37,47,39,34,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,58,49,51,53,51,56,46],
[50,0,49,44,39,42,52,45,48],
[42,51,0,43,42,45,46,48,43],
[51,56,57,0,57,50,62,56,58],
[49,61,58,43,0,51,58,59,46],
[47,58,55,50,49,0,46,49,48],
[49,48,54,38,42,54,0,53,53],
[44,55,52,44,41,51,47,0,56],
[54,52,57,42,54,52,47,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,34,50,62,42,42,41,46],
[51,0,55,51,56,50,43,57,39],
[66,45,0,63,63,56,56,53,49],
[50,49,37,0,47,45,45,44,48],
[38,44,37,53,0,55,54,49,46],
[58,50,44,55,45,0,58,55,49],
[58,57,44,55,46,42,0,52,44],
[59,43,47,56,51,45,48,0,50],
[54,61,51,52,54,51,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,58,55,51,52,54,56],
[55,0,50,57,62,36,43,60,49],
[57,50,0,63,47,42,48,62,68],
[42,43,37,0,38,23,32,53,48],
[45,38,53,62,0,42,38,56,67],
[49,64,58,77,58,0,48,65,57],
[48,57,52,68,62,52,0,59,68],
[46,40,38,47,44,35,41,0,52],
[44,51,32,52,33,43,32,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,51,57,51,53,62,58],
[44,0,54,55,52,57,55,58,56],
[50,46,0,61,47,52,48,52,49],
[49,45,39,0,51,46,41,55,42],
[43,48,53,49,0,53,51,59,48],
[49,43,48,54,47,0,52,59,40],
[47,45,52,59,49,48,0,52,50],
[38,42,48,45,41,41,48,0,53],
[42,44,51,58,52,60,50,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,54,50,55,60,46,61,65],
[46,0,45,51,61,54,48,53,52],
[46,55,0,52,58,63,49,55,62],
[50,49,48,0,52,58,57,47,65],
[45,39,42,48,0,45,49,48,52],
[40,46,37,42,55,0,58,44,58],
[54,52,51,43,51,42,0,63,67],
[39,47,45,53,52,56,37,0,54],
[35,48,38,35,48,42,33,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,55,59,53,50,49,52,48],
[45,0,53,58,43,48,48,50,42],
[45,47,0,52,44,42,43,45,44],
[41,42,48,0,43,55,47,48,41],
[47,57,56,57,0,51,51,52,58],
[50,52,58,45,49,0,42,46,43],
[51,52,57,53,49,58,0,55,44],
[48,50,55,52,48,54,45,0,43],
[52,58,56,59,42,57,56,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,54,58,66,49,61,59,50],
[57,0,40,50,56,51,50,49,51],
[46,60,0,58,70,50,60,54,61],
[42,50,42,0,47,48,51,48,60],
[34,44,30,53,0,45,38,47,53],
[51,49,50,52,55,0,54,49,51],
[39,50,40,49,62,46,0,46,53],
[41,51,46,52,53,51,54,0,52],
[50,49,39,40,47,49,47,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,61,55,50,47,51,67,59],
[62,0,70,65,48,50,50,64,64],
[39,30,0,41,39,36,32,59,53],
[45,35,59,0,41,36,53,48,56],
[50,52,61,59,0,51,48,69,65],
[53,50,64,64,49,0,50,62,59],
[49,50,68,47,52,50,0,67,66],
[33,36,41,52,31,38,33,0,46],
[41,36,47,44,35,41,34,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,52,42,73,42,40,61],
[50,0,60,51,42,64,53,64,70],
[45,40,0,34,27,55,40,55,58],
[48,49,66,0,55,61,53,58,66],
[58,58,73,45,0,62,61,58,73],
[27,36,45,39,38,0,43,40,50],
[58,47,60,47,39,57,0,48,83],
[60,36,45,42,42,60,52,0,63],
[39,30,42,34,27,50,17,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,37,55,44,41,35,35,36],
[65,0,58,57,59,51,39,45,43],
[63,42,0,67,41,35,39,44,56],
[45,43,33,0,30,26,35,29,41],
[56,41,59,70,0,54,36,54,57],
[59,49,65,74,46,0,56,52,55],
[65,61,61,65,64,44,0,58,72],
[65,55,56,71,46,48,42,0,66],
[64,57,44,59,43,45,28,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,48,53,47,53,45,53],
[52,0,54,52,56,55,59,48,55],
[54,46,0,46,56,51,50,56,57],
[52,48,54,0,57,53,61,48,52],
[47,44,44,43,0,46,50,45,49],
[53,45,49,47,54,0,52,46,46],
[47,41,50,39,50,48,0,42,50],
[55,52,44,52,55,54,58,0,49],
[47,45,43,48,51,54,50,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,45,39,49,59,67,52],
[49,0,55,57,45,52,64,68,51],
[54,45,0,52,49,48,51,61,48],
[55,43,48,0,37,40,59,65,49],
[61,55,51,63,0,47,66,65,66],
[51,48,52,60,53,0,56,61,65],
[41,36,49,41,34,44,0,52,53],
[33,32,39,35,35,39,48,0,49],
[48,49,52,51,34,35,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,42,62,50,42,62,31,31],
[27,0,39,58,58,39,89,58,0],
[58,61,0,50,58,50,58,19,0],
[38,42,50,0,58,50,89,19,0],
[50,42,42,42,0,11,39,0,11],
[58,61,50,50,89,0,58,19,50],
[38,11,42,11,61,42,0,11,11],
[69,42,81,81,100,81,89,0,42],
[69,100,100,100,89,50,89,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,43,46,46,39,51,47,40],
[57,0,46,56,54,42,48,46,46],
[57,54,0,60,53,65,53,62,48],
[54,44,40,0,52,42,40,50,47],
[54,46,47,48,0,44,38,42,50],
[61,58,35,58,56,0,56,53,44],
[49,52,47,60,62,44,0,58,48],
[53,54,38,50,58,47,42,0,40],
[60,54,52,53,50,56,52,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,53,52,56,61,51,38,60],
[57,0,54,59,56,67,54,50,71],
[47,46,0,50,47,50,51,36,54],
[48,41,50,0,45,55,35,52,49],
[44,44,53,55,0,46,40,39,55],
[39,33,50,45,54,0,29,43,46],
[49,46,49,65,60,71,0,51,58],
[62,50,64,48,61,57,49,0,67],
[40,29,46,51,45,54,42,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,65,53,65,55,49,53,59],
[43,0,52,49,51,48,45,52,50],
[35,48,0,49,51,51,45,48,43],
[47,51,51,0,56,51,46,52,48],
[35,49,49,44,0,45,45,54,45],
[45,52,49,49,55,0,47,54,49],
[51,55,55,54,55,53,0,50,55],
[47,48,52,48,46,46,50,0,41],
[41,50,57,52,55,51,45,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,62,51,48,52,61,52,54],
[51,0,50,46,45,51,50,56,60],
[38,50,0,42,46,51,47,56,53],
[49,54,58,0,51,56,63,58,57],
[52,55,54,49,0,55,56,55,57],
[48,49,49,44,45,0,51,52,57],
[39,50,53,37,44,49,0,54,45],
[48,44,44,42,45,48,46,0,52],
[46,40,47,43,43,43,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,64,47,68,72,67,68,68],
[56,0,52,53,56,53,43,68,63],
[36,48,0,54,66,47,43,64,55],
[53,47,46,0,72,42,42,67,60],
[32,44,34,28,0,31,47,59,22],
[28,47,53,58,69,0,53,63,54],
[33,57,57,58,53,47,0,66,52],
[32,32,36,33,41,37,34,0,38],
[32,37,45,40,78,46,48,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,53,49,51,47,49,48,58],
[56,0,56,49,55,63,51,51,61],
[47,44,0,54,48,50,42,56,52],
[51,51,46,0,52,58,49,53,60],
[49,45,52,48,0,53,40,49,52],
[53,37,50,42,47,0,49,51,53],
[51,49,58,51,60,51,0,54,60],
[52,49,44,47,51,49,46,0,47],
[42,39,48,40,48,47,40,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,42,50,48,49,59,53,55],
[38,0,30,39,50,32,37,38,41],
[58,70,0,60,67,49,57,63,55],
[50,61,40,0,54,44,46,42,44],
[52,50,33,46,0,51,48,47,54],
[51,68,51,56,49,0,60,58,45],
[41,63,43,54,52,40,0,58,51],
[47,62,37,58,53,42,42,0,40],
[45,59,45,56,46,55,49,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,40,43,51,43,46,35,42],
[58,0,55,53,53,41,43,45,53],
[60,45,0,68,56,52,56,49,54],
[57,47,32,0,49,39,38,52,51],
[49,47,44,51,0,45,52,44,46],
[57,59,48,61,55,0,47,45,54],
[54,57,44,62,48,53,0,51,51],
[65,55,51,48,56,55,49,0,49],
[58,47,46,49,54,46,49,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,51,54,49,62,53,57,56],
[40,0,45,49,47,48,44,44,46],
[49,55,0,52,55,59,51,58,52],
[46,51,48,0,53,50,50,56,47],
[51,53,45,47,0,55,52,54,48],
[38,52,41,50,45,0,42,48,41],
[47,56,49,50,48,58,0,59,58],
[43,56,42,44,46,52,41,0,45],
[44,54,48,53,52,59,42,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,33,40,43,38,43,33,34],
[65,0,54,50,45,62,51,55,58],
[67,46,0,46,46,50,53,55,59],
[60,50,54,0,41,42,52,47,51],
[57,55,54,59,0,51,50,51,49],
[62,38,50,58,49,0,41,34,45],
[57,49,47,48,50,59,0,43,49],
[67,45,45,53,49,66,57,0,61],
[66,42,41,49,51,55,51,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,61,59,57,57,77,45,62],
[37,0,37,41,28,38,49,40,41],
[39,63,0,37,53,52,52,57,56],
[41,59,63,0,43,45,52,55,56],
[43,72,47,57,0,59,58,57,62],
[43,62,48,55,41,0,61,56,50],
[23,51,48,48,42,39,0,45,47],
[55,60,43,45,43,44,55,0,58],
[38,59,44,44,38,50,53,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,42,61,50,33,55,47,51],
[67,0,24,59,47,39,47,42,64],
[58,76,0,77,75,50,68,68,83],
[39,41,23,0,25,35,24,21,46],
[50,53,25,75,0,52,38,46,60],
[67,61,50,65,48,0,52,47,70],
[45,53,32,76,62,48,0,51,72],
[53,58,32,79,54,53,49,0,54],
[49,36,17,54,40,30,28,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,49,42,45,25,49,66,66],
[28,0,46,42,47,25,33,35,31],
[51,54,0,31,56,35,39,43,37],
[58,58,69,0,68,56,49,53,56],
[55,53,44,32,0,29,40,42,48],
[75,75,65,44,71,0,43,51,66],
[51,67,61,51,60,57,0,48,62],
[34,65,57,47,58,49,52,0,61],
[34,69,63,44,52,34,38,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,60,60,59,46,56,51,60],
[52,0,52,45,49,41,59,46,58],
[40,48,0,40,41,44,39,36,41],
[40,55,60,0,45,47,51,49,45],
[41,51,59,55,0,50,42,55,47],
[54,59,56,53,50,0,50,48,57],
[44,41,61,49,58,50,0,54,50],
[49,54,64,51,45,52,46,0,56],
[40,42,59,55,53,43,50,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,51,54,48,44,49,53],
[47,0,47,51,60,47,49,54,63],
[53,53,0,61,57,54,50,59,60],
[49,49,39,0,56,45,54,51,52],
[46,40,43,44,0,50,41,48,45],
[52,53,46,55,50,0,45,53,55],
[56,51,50,46,59,55,0,48,54],
[51,46,41,49,52,47,52,0,50],
[47,37,40,48,55,45,46,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,58,46,60,53,61,59,60],
[50,0,38,43,56,55,67,51,45],
[42,62,0,56,55,56,62,59,50],
[54,57,44,0,59,55,56,50,50],
[40,44,45,41,0,42,61,45,57],
[47,45,44,45,58,0,65,54,53],
[39,33,38,44,39,35,0,38,46],
[41,49,41,50,55,46,62,0,50],
[40,55,50,50,43,47,54,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,57,62,45,61,48,55,44],
[55,0,39,57,57,55,45,38,40],
[43,61,0,65,62,65,55,51,61],
[38,43,35,0,45,56,39,38,45],
[55,43,38,55,0,60,48,47,34],
[39,45,35,44,40,0,35,38,35],
[52,55,45,61,52,65,0,44,46],
[45,62,49,62,53,62,56,0,54],
[56,60,39,55,66,65,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 100, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_9_100.csv", index=False, header=False)