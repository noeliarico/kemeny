
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,47,54,63,53,77,70,67],
[53,0,36,55,43,53,45,43],
[46,64,0,52,57,70,76,65],
[37,45,48,0,24,52,52,44],
[47,57,43,76,0,82,70,46],
[23,47,30,48,18,0,35,43],
[30,55,24,48,30,65,0,46],
[33,57,35,56,54,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,52,48,54,57,42,44],
[55,0,60,51,45,42,36,40],
[48,40,0,49,40,40,44,46],
[52,49,51,0,49,48,39,51],
[46,55,60,51,0,49,43,56],
[43,58,60,52,51,0,51,55],
[58,64,56,61,57,49,0,60],
[56,60,54,49,44,45,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,41,44,46,46,43,51],
[50,0,50,54,53,47,45,52],
[59,50,0,54,52,52,47,50],
[56,46,46,0,48,49,42,52],
[54,47,48,52,0,48,45,47],
[54,53,48,51,52,0,50,44],
[57,55,53,58,55,50,0,60],
[49,48,50,48,53,56,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,59,48,56,52,54,57],
[47,0,46,58,49,54,43,53],
[41,54,0,52,54,57,50,52],
[52,42,48,0,44,51,50,38],
[44,51,46,56,0,52,48,59],
[48,46,43,49,48,0,36,46],
[46,57,50,50,52,64,0,55],
[43,47,48,62,41,54,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,39,40,54,53,53,48],
[50,0,51,45,42,47,50,56],
[61,49,0,53,47,53,51,55],
[60,55,47,0,53,62,55,64],
[46,58,53,47,0,54,55,54],
[47,53,47,38,46,0,54,49],
[47,50,49,45,45,46,0,48],
[52,44,45,36,46,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,66,62,53,48,70,69],
[37,0,59,47,46,41,59,67],
[34,41,0,35,35,44,46,62],
[38,53,65,0,41,55,55,65],
[47,54,65,59,0,55,67,76],
[52,59,56,45,45,0,59,65],
[30,41,54,45,33,41,0,49],
[31,33,38,35,24,35,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,46,48,63,61,53],
[50,0,46,53,49,52,51,40],
[47,54,0,45,50,62,54,33],
[54,47,55,0,58,62,43,47],
[52,51,50,42,0,47,43,49],
[37,48,38,38,53,0,47,48],
[39,49,46,57,57,53,0,57],
[47,60,67,53,51,52,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,40,37,40,53,40,47],
[67,0,59,49,59,58,56,59],
[60,41,0,55,61,54,58,52],
[63,51,45,0,46,53,49,62],
[60,41,39,54,0,55,42,50],
[47,42,46,47,45,0,57,57],
[60,44,42,51,58,43,0,42],
[53,41,48,38,50,43,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,44,46,47,50,53,48],
[46,0,31,44,44,40,45,35],
[56,69,0,59,56,46,57,54],
[54,56,41,0,51,48,58,52],
[53,56,44,49,0,41,51,49],
[50,60,54,52,59,0,53,54],
[47,55,43,42,49,47,0,45],
[52,65,46,48,51,46,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,53,79,56,41,79,41],
[21,0,21,24,45,21,68,39],
[47,79,0,65,65,23,65,41],
[21,76,35,0,21,44,44,62],
[44,55,35,79,0,44,44,41],
[59,79,77,56,56,0,100,18],
[21,32,35,56,56,0,0,18],
[59,61,59,38,59,82,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,50,53,52,54,43],
[53,0,53,55,52,47,42,50],
[50,47,0,55,54,51,49,39],
[50,45,45,0,52,46,48,44],
[47,48,46,48,0,46,49,47],
[48,53,49,54,54,0,49,49],
[46,58,51,52,51,51,0,49],
[57,50,61,56,53,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,49,53,51,50,46],
[47,0,46,46,50,46,38,42],
[55,54,0,52,59,50,54,54],
[51,54,48,0,51,46,42,42],
[47,50,41,49,0,50,46,42],
[49,54,50,54,50,0,52,50],
[50,62,46,58,54,48,0,48],
[54,58,46,58,58,50,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,50,52,56,54,56],
[49,0,45,47,49,64,51,58],
[48,55,0,55,57,64,53,58],
[50,53,45,0,56,63,60,64],
[48,51,43,44,0,59,50,56],
[44,36,36,37,41,0,41,42],
[46,49,47,40,50,59,0,54],
[44,42,42,36,44,58,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,65,41,57,55,54],
[55,0,42,58,36,45,67,45],
[47,58,0,69,32,44,67,54],
[35,42,31,0,28,53,68,52],
[59,64,68,72,0,76,49,52],
[43,55,56,47,24,0,65,60],
[45,33,33,32,51,35,0,40],
[46,55,46,48,48,40,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,46,41,52,51,51,36],
[57,0,49,51,47,54,44,63],
[54,51,0,46,39,49,64,46],
[59,49,54,0,52,52,55,54],
[48,53,61,48,0,62,58,56],
[49,46,51,48,38,0,52,45],
[49,56,36,45,42,48,0,46],
[64,37,54,46,44,55,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,56,57,51,38,49],
[48,0,56,50,51,47,48,52],
[53,44,0,48,45,57,33,41],
[44,50,52,0,48,56,39,44],
[43,49,55,52,0,48,61,34],
[49,53,43,44,52,0,40,47],
[62,52,67,61,39,60,0,45],
[51,48,59,56,66,53,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,52,44,50,44,43,42],
[59,0,54,52,59,50,48,56],
[48,46,0,47,53,44,43,49],
[56,48,53,0,57,47,44,48],
[50,41,47,43,0,42,35,42],
[56,50,56,53,58,0,50,46],
[57,52,57,56,65,50,0,50],
[58,44,51,52,58,54,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,67,54,68,72,44,69],
[40,0,46,22,61,45,36,32],
[33,54,0,46,57,55,45,57],
[46,78,54,0,64,66,53,50],
[32,39,43,36,0,52,31,42],
[28,55,45,34,48,0,38,35],
[56,64,55,47,69,62,0,61],
[31,68,43,50,58,65,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,37,35,43,45,39,38],
[60,0,62,58,51,52,54,44],
[63,38,0,46,47,55,50,44],
[65,42,54,0,51,48,58,51],
[57,49,53,49,0,51,64,50],
[55,48,45,52,49,0,61,44],
[61,46,50,42,36,39,0,48],
[62,56,56,49,50,56,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,56,67,57,58,84,53],
[59,0,77,73,42,42,68,42],
[44,23,0,65,53,56,82,51],
[33,27,35,0,25,26,38,21],
[43,58,47,75,0,40,84,43],
[42,58,44,74,60,0,72,74],
[16,32,18,62,16,28,0,14],
[47,58,49,79,57,26,86,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,52,56,58,68,53],
[50,0,56,51,50,56,60,53],
[48,44,0,49,51,51,57,48],
[48,49,51,0,50,50,57,51],
[44,50,49,50,0,56,58,51],
[42,44,49,50,44,0,54,43],
[32,40,43,43,42,46,0,45],
[47,47,52,49,49,57,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,38,41,51,47,60,46],
[56,0,53,48,54,43,53,52],
[62,47,0,50,52,49,57,50],
[59,52,50,0,54,55,58,47],
[49,46,48,46,0,48,62,37],
[53,57,51,45,52,0,59,46],
[40,47,43,42,38,41,0,37],
[54,48,50,53,63,54,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,37,48,43,45,64],
[48,0,58,48,46,67,63,65],
[47,42,0,44,53,53,52,56],
[63,52,56,0,52,39,47,61],
[52,54,47,48,0,54,56,72],
[57,33,47,61,46,0,61,63],
[55,37,48,53,44,39,0,55],
[36,35,44,39,28,37,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,49,42,45,59,53],
[48,0,48,52,50,50,58,53],
[50,52,0,55,51,51,53,54],
[51,48,45,0,43,44,43,47],
[58,50,49,57,0,50,53,58],
[55,50,49,56,50,0,57,53],
[41,42,47,57,47,43,0,45],
[47,47,46,53,42,47,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,52,55,51,49,55,54],
[41,0,39,43,40,33,36,44],
[48,61,0,52,46,35,49,39],
[45,57,48,0,49,46,44,46],
[49,60,54,51,0,60,40,44],
[51,67,65,54,40,0,46,51],
[45,64,51,56,60,54,0,51],
[46,56,61,54,56,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,55,47,53,53,51,41],
[59,0,55,52,48,53,52,51],
[45,45,0,42,52,50,51,45],
[53,48,58,0,47,65,53,52],
[47,52,48,53,0,57,61,45],
[47,47,50,35,43,0,51,51],
[49,48,49,47,39,49,0,47],
[59,49,55,48,55,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,63,60,54,46,51,57],
[50,0,44,57,52,44,51,57],
[37,56,0,59,67,58,55,59],
[40,43,41,0,52,34,35,47],
[46,48,33,48,0,40,52,54],
[54,56,42,66,60,0,44,54],
[49,49,45,65,48,56,0,53],
[43,43,41,53,46,46,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,60,50,46,52,50,58],
[52,0,57,51,45,47,47,50],
[40,43,0,47,52,53,54,50],
[50,49,53,0,44,48,52,57],
[54,55,48,56,0,62,60,60],
[48,53,47,52,38,0,45,60],
[50,53,46,48,40,55,0,45],
[42,50,50,43,40,40,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,48,44,54,54,59],
[52,0,54,47,51,51,50,50],
[46,46,0,48,52,56,52,54],
[52,53,52,0,47,53,47,42],
[56,49,48,53,0,52,50,49],
[46,49,44,47,48,0,47,46],
[46,50,48,53,50,53,0,54],
[41,50,46,58,51,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,41,40,38,41,39,47],
[49,0,36,46,38,41,39,39],
[59,64,0,49,42,40,47,49],
[60,54,51,0,48,52,36,43],
[62,62,58,52,0,46,53,55],
[59,59,60,48,54,0,51,61],
[61,61,53,64,47,49,0,57],
[53,61,51,57,45,39,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,52,63,58,58,61,58],
[60,0,48,57,56,52,56,47],
[48,52,0,56,60,47,55,56],
[37,43,44,0,51,26,42,40],
[42,44,40,49,0,42,51,52],
[42,48,53,74,58,0,56,58],
[39,44,45,58,49,44,0,45],
[42,53,44,60,48,42,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,41,50,50,56,54,60],
[49,0,48,40,51,58,51,57],
[59,52,0,52,50,64,49,53],
[50,60,48,0,52,56,55,59],
[50,49,50,48,0,59,65,50],
[44,42,36,44,41,0,42,48],
[46,49,51,45,35,58,0,43],
[40,43,47,41,50,52,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,35,41,53,35,47,46],
[67,0,52,54,52,43,50,52],
[65,48,0,40,61,51,46,67],
[59,46,60,0,71,51,48,50],
[47,48,39,29,0,35,53,38],
[65,57,49,49,65,0,63,56],
[53,50,54,52,47,37,0,51],
[54,48,33,50,62,44,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,53,59,49,63,75,55],
[41,0,58,45,42,55,59,55],
[47,42,0,43,46,56,56,44],
[41,55,57,0,45,52,64,52],
[51,58,54,55,0,59,58,50],
[37,45,44,48,41,0,61,58],
[25,41,44,36,42,39,0,44],
[45,45,56,48,50,42,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,55,43,41,54,29,63],
[60,0,74,56,31,56,62,86],
[45,26,0,62,36,25,30,64],
[57,44,38,0,53,52,50,48],
[59,69,64,47,0,58,51,66],
[46,44,75,48,42,0,44,53],
[71,38,70,50,49,56,0,62],
[37,14,36,52,34,47,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,37,52,44,48,62],
[42,0,35,35,43,39,29,56],
[48,65,0,49,51,37,41,60],
[63,65,51,0,39,39,53,53],
[48,57,49,61,0,43,54,54],
[56,61,63,61,57,0,40,48],
[52,71,59,47,46,60,0,55],
[38,44,40,47,46,52,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,49,55,44,59,52],
[53,0,53,49,56,52,58,49],
[48,47,0,47,43,52,55,48],
[51,51,53,0,49,51,51,62],
[45,44,57,51,0,52,54,49],
[56,48,48,49,48,0,50,53],
[41,42,45,49,46,50,0,47],
[48,51,52,38,51,47,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,39,53,36,61,43,56],
[53,0,49,51,50,61,44,55],
[61,51,0,59,53,56,44,50],
[47,49,41,0,44,59,46,52],
[64,50,47,56,0,63,50,51],
[39,39,44,41,37,0,26,42],
[57,56,56,54,50,74,0,58],
[44,45,50,48,49,58,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,43,53,55,48,51,45],
[45,0,59,67,52,43,53,43],
[57,41,0,57,50,46,45,53],
[47,33,43,0,49,39,46,39],
[45,48,50,51,0,36,47,45],
[52,57,54,61,64,0,49,41],
[49,47,55,54,53,51,0,53],
[55,57,47,61,55,59,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,55,66,58,43,58,62],
[53,0,42,46,47,43,52,52],
[45,58,0,66,64,56,61,58],
[34,54,34,0,54,48,55,45],
[42,53,36,46,0,49,58,51],
[57,57,44,52,51,0,69,58],
[42,48,39,45,42,31,0,42],
[38,48,42,55,49,42,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,47,61,53,44,50],
[48,0,58,52,52,58,37,41],
[55,42,0,23,54,56,46,54],
[53,48,77,0,53,49,61,74],
[39,48,46,47,0,32,68,61],
[47,42,44,51,68,0,43,42],
[56,63,54,39,32,57,0,62],
[50,59,46,26,39,58,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,52,64,52,58,43],
[50,0,51,59,62,52,50,51],
[47,49,0,47,54,46,28,50],
[48,41,53,0,58,49,47,54],
[36,38,46,42,0,40,32,49],
[48,48,54,51,60,0,37,49],
[42,50,72,53,68,63,0,60],
[57,49,50,46,51,51,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,55,57,46,55,50,35],
[62,0,61,63,55,67,47,43],
[45,39,0,44,49,60,44,33],
[43,37,56,0,43,64,41,39],
[54,45,51,57,0,51,45,45],
[45,33,40,36,49,0,51,33],
[50,53,56,59,55,49,0,52],
[65,57,67,61,55,67,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,70,65,48,67,51,73],
[46,0,52,71,33,60,35,56],
[30,48,0,51,47,72,29,66],
[35,29,49,0,45,58,32,48],
[52,67,53,55,0,47,41,52],
[33,40,28,42,53,0,30,52],
[49,65,71,68,59,70,0,67],
[27,44,34,52,48,48,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,57,57,65,68,69,61],
[55,0,39,12,61,71,48,47],
[43,61,0,51,60,58,58,42],
[43,88,49,0,81,80,68,49],
[35,39,40,19,0,46,49,48],
[32,29,42,20,54,0,38,35],
[31,52,42,32,51,62,0,37],
[39,53,58,51,52,65,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,57,42,64,57,59,53],
[47,0,56,49,56,65,51,58],
[43,44,0,49,61,52,44,58],
[58,51,51,0,59,59,54,48],
[36,44,39,41,0,43,38,32],
[43,35,48,41,57,0,49,50],
[41,49,56,46,62,51,0,46],
[47,42,42,52,68,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,75,49,45,58,47,41],
[46,0,45,33,38,48,37,51],
[25,55,0,51,29,39,38,44],
[51,67,49,0,42,42,32,51],
[55,62,71,58,0,45,47,54],
[42,52,61,58,55,0,33,42],
[53,63,62,68,53,67,0,44],
[59,49,56,49,46,58,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,48,68,47,65,49],
[55,0,47,52,67,50,62,55],
[55,53,0,40,65,54,58,58],
[52,48,60,0,63,50,64,58],
[32,33,35,37,0,37,40,50],
[53,50,46,50,63,0,64,68],
[35,38,42,36,60,36,0,49],
[51,45,42,42,50,32,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,41,46,46,52,58],
[53,0,58,41,53,50,58,61],
[44,42,0,41,50,43,47,59],
[59,59,59,0,48,45,55,66],
[54,47,50,52,0,47,44,59],
[54,50,57,55,53,0,47,61],
[48,42,53,45,56,53,0,52],
[42,39,41,34,41,39,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,57,52,43,56,53],
[53,0,67,53,57,44,53,47],
[42,33,0,39,46,40,44,46],
[43,47,61,0,55,44,48,42],
[48,43,54,45,0,39,45,44],
[57,56,60,56,61,0,56,47],
[44,47,56,52,55,44,0,40],
[47,53,54,58,56,53,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,46,54,42,44,50,49],
[61,0,53,54,48,50,56,54],
[54,47,0,50,50,50,50,56],
[46,46,50,0,48,53,55,53],
[58,52,50,52,0,47,55,54],
[56,50,50,47,53,0,57,55],
[50,44,50,45,45,43,0,51],
[51,46,44,47,46,45,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,43,56,54,56,48],
[51,0,46,59,57,47,56,58],
[55,54,0,43,58,55,44,49],
[57,41,57,0,51,55,58,58],
[44,43,42,49,0,55,45,48],
[46,53,45,45,45,0,53,53],
[44,44,56,42,55,47,0,54],
[52,42,51,42,52,47,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,43,63,51,59,46,50],
[68,0,59,54,43,55,52,48],
[57,41,0,56,54,65,47,54],
[37,46,44,0,50,60,43,53],
[49,57,46,50,0,64,58,64],
[41,45,35,40,36,0,54,49],
[54,48,53,57,42,46,0,51],
[50,52,46,47,36,51,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,47,42,52,44,43,47],
[49,0,53,38,44,44,45,46],
[53,47,0,45,53,45,43,51],
[58,62,55,0,56,49,51,44],
[48,56,47,44,0,54,47,49],
[56,56,55,51,46,0,55,50],
[57,55,57,49,53,45,0,48],
[53,54,49,56,51,50,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,60,46,54,43,43,54],
[39,0,41,43,49,48,43,47],
[40,59,0,48,50,57,54,56],
[54,57,52,0,47,44,52,62],
[46,51,50,53,0,40,54,61],
[57,52,43,56,60,0,56,56],
[57,57,46,48,46,44,0,64],
[46,53,44,38,39,44,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,46,40,52,46,40],
[50,0,49,45,50,56,52,45],
[53,51,0,54,56,58,32,50],
[54,55,46,0,41,46,39,50],
[60,50,44,59,0,53,45,48],
[48,44,42,54,47,0,37,40],
[54,48,68,61,55,63,0,57],
[60,55,50,50,52,60,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,58,42,56,45,54,61],
[49,0,46,43,47,36,50,57],
[42,54,0,52,52,40,62,56],
[58,57,48,0,52,53,46,53],
[44,53,48,48,0,39,44,54],
[55,64,60,47,61,0,59,66],
[46,50,38,54,56,41,0,53],
[39,43,44,47,46,34,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,50,58,61,51,50,52],
[40,0,40,57,51,42,46,39],
[50,60,0,64,54,58,56,50],
[42,43,36,0,56,47,50,38],
[39,49,46,44,0,44,47,42],
[49,58,42,53,56,0,49,48],
[50,54,44,50,53,51,0,43],
[48,61,50,62,58,52,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,43,44,42,48,42,41],
[51,0,46,55,51,61,50,52],
[57,54,0,51,63,57,48,52],
[56,45,49,0,48,58,50,47],
[58,49,37,52,0,55,42,56],
[52,39,43,42,45,0,41,47],
[58,50,52,50,58,59,0,55],
[59,48,48,53,44,53,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,36,33,16,27,31,34],
[56,0,35,42,37,43,29,33],
[64,65,0,52,40,48,41,54],
[67,58,48,0,28,37,46,46],
[84,63,60,72,0,42,54,36],
[73,57,52,63,58,0,50,42],
[69,71,59,54,46,50,0,53],
[66,67,46,54,64,58,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,57,59,71,50,52,55],
[26,0,45,41,49,35,40,36],
[43,55,0,58,59,39,48,50],
[41,59,42,0,60,44,44,48],
[29,51,41,40,0,32,31,33],
[50,65,61,56,68,0,53,56],
[48,60,52,56,69,47,0,54],
[45,64,50,52,67,44,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,44,48,53,55,59,48],
[51,0,45,49,54,50,58,51],
[56,55,0,47,57,48,56,49],
[52,51,53,0,60,50,57,50],
[47,46,43,40,0,41,45,39],
[45,50,52,50,59,0,64,44],
[41,42,44,43,55,36,0,38],
[52,49,51,50,61,56,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,59,60,49,57,53],
[49,0,43,52,64,34,54,40],
[46,57,0,48,61,41,58,40],
[41,48,52,0,59,44,52,46],
[40,36,39,41,0,40,43,35],
[51,66,59,56,60,0,70,43],
[43,46,42,48,57,30,0,46],
[47,60,60,54,65,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,64,65,64,60,67,50],
[41,0,57,53,47,56,49,42],
[36,43,0,49,36,52,52,47],
[35,47,51,0,46,51,55,42],
[36,53,64,54,0,61,63,56],
[40,44,48,49,39,0,52,41],
[33,51,48,45,37,48,0,40],
[50,58,53,58,44,59,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,43,47,50,42,43,54],
[51,0,46,52,62,33,58,52],
[57,54,0,49,59,53,63,62],
[53,48,51,0,61,48,57,42],
[50,38,41,39,0,33,57,47],
[58,67,47,52,67,0,66,62],
[57,42,37,43,43,34,0,45],
[46,48,38,58,53,38,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,51,45,53,59,52],
[46,0,41,45,46,44,50,57],
[54,59,0,45,54,43,55,57],
[49,55,55,0,40,55,56,63],
[55,54,46,60,0,44,51,70],
[47,56,57,45,56,0,52,61],
[41,50,45,44,49,48,0,56],
[48,43,43,37,30,39,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,39,38,28,26,37,28],
[64,0,49,75,61,58,55,60],
[61,51,0,64,41,37,57,56],
[62,25,36,0,37,67,53,54],
[72,39,59,63,0,45,54,61],
[74,42,63,33,55,0,53,66],
[63,45,43,47,46,47,0,58],
[72,40,44,46,39,34,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,45,27,33,46,49,51],
[63,0,62,44,47,62,38,50],
[55,38,0,33,38,57,49,43],
[73,56,67,0,50,58,57,64],
[67,53,62,50,0,66,57,63],
[54,38,43,42,34,0,48,51],
[51,62,51,43,43,52,0,51],
[49,50,57,36,37,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,51,65,53,53,57],
[51,0,53,49,55,52,55,57],
[49,47,0,43,60,47,50,51],
[49,51,57,0,65,58,41,53],
[35,45,40,35,0,43,46,45],
[47,48,53,42,57,0,40,49],
[47,45,50,59,54,60,0,54],
[43,43,49,47,55,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,41,47,60,47,42,47],
[48,0,58,42,68,46,44,58],
[59,42,0,58,40,38,28,35],
[53,58,42,0,61,51,47,44],
[40,32,60,39,0,39,44,48],
[53,54,62,49,61,0,52,57],
[58,56,72,53,56,48,0,57],
[53,42,65,56,52,43,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,52,51,53,46,53,46],
[41,0,51,41,64,50,45,55],
[48,49,0,53,62,59,59,52],
[49,59,47,0,52,54,52,39],
[47,36,38,48,0,59,39,62],
[54,50,41,46,41,0,29,53],
[47,55,41,48,61,71,0,59],
[54,45,48,61,38,47,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,59,59,50,57,53],
[44,0,45,49,41,44,44,48],
[44,55,0,56,51,47,57,49],
[41,51,44,0,49,46,47,41],
[41,59,49,51,0,48,48,52],
[50,56,53,54,52,0,59,50],
[43,56,43,53,52,41,0,46],
[47,52,51,59,48,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,61,63,45,42,50],
[49,0,49,51,51,57,48,37],
[44,51,0,57,54,35,40,53],
[39,49,43,0,44,43,32,38],
[37,49,46,56,0,48,40,42],
[55,43,65,57,52,0,51,56],
[58,52,60,68,60,49,0,55],
[50,63,47,62,58,44,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,48,50,51,60,52,57],
[42,0,54,46,47,51,45,46],
[52,46,0,50,54,56,49,53],
[50,54,50,0,53,47,50,51],
[49,53,46,47,0,52,47,54],
[40,49,44,53,48,0,41,45],
[48,55,51,50,53,59,0,58],
[43,54,47,49,46,55,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,40,64,49,36,41,44],
[49,0,45,64,57,37,42,37],
[60,55,0,72,66,53,55,46],
[36,36,28,0,38,31,30,29],
[51,43,34,62,0,41,42,26],
[64,63,47,69,59,0,67,50],
[59,58,45,70,58,33,0,33],
[56,63,54,71,74,50,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,48,55,54,62,54],
[46,0,40,51,46,52,52,43],
[49,60,0,62,66,72,62,55],
[52,49,38,0,51,55,62,45],
[45,54,34,49,0,59,53,44],
[46,48,28,45,41,0,51,46],
[38,48,38,38,47,49,0,43],
[46,57,45,55,56,54,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,53,64,52,51,39,56],
[59,0,50,53,73,62,41,54],
[47,50,0,51,60,56,50,53],
[36,47,49,0,54,45,46,49],
[48,27,40,46,0,47,39,45],
[49,38,44,55,53,0,44,52],
[61,59,50,54,61,56,0,54],
[44,46,47,51,55,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,38,44,42,44,42,46],
[58,0,55,37,47,48,41,50],
[62,45,0,49,49,49,45,55],
[56,63,51,0,50,51,50,62],
[58,53,51,50,0,51,51,55],
[56,52,51,49,49,0,50,60],
[58,59,55,50,49,50,0,58],
[54,50,45,38,45,40,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,44,35,45,34,58],
[68,0,49,65,60,73,62,72],
[70,51,0,64,53,48,70,52],
[56,35,36,0,44,60,50,66],
[65,40,47,56,0,41,65,62],
[55,27,52,40,59,0,62,59],
[66,38,30,50,35,38,0,47],
[42,28,48,34,38,41,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,51,50,50,53,52],
[48,0,51,48,55,46,50,40],
[57,49,0,52,51,52,55,49],
[49,52,48,0,57,45,49,47],
[50,45,49,43,0,41,45,40],
[50,54,48,55,59,0,58,52],
[47,50,45,51,55,42,0,45],
[48,60,51,53,60,48,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,40,52,47,50,48],
[54,0,57,50,58,52,55,53],
[52,43,0,36,47,46,48,46],
[60,50,64,0,57,58,57,51],
[48,42,53,43,0,44,53,44],
[53,48,54,42,56,0,55,49],
[50,45,52,43,47,45,0,47],
[52,47,54,49,56,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,48,50,41,56,46],
[51,0,39,45,44,43,60,53],
[59,61,0,55,48,48,56,50],
[52,55,45,0,59,54,54,45],
[50,56,52,41,0,52,62,45],
[59,57,52,46,48,0,57,46],
[44,40,44,46,38,43,0,34],
[54,47,50,55,55,54,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,57,50,53,46,58,43],
[53,0,59,51,44,39,37,44],
[43,41,0,52,47,49,51,39],
[50,49,48,0,50,48,62,45],
[47,56,53,50,0,50,49,59],
[54,61,51,52,50,0,53,52],
[42,63,49,38,51,47,0,46],
[57,56,61,55,41,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,48,51,46,45,44,44],
[49,0,51,40,57,51,49,46],
[52,49,0,41,56,48,41,49],
[49,60,59,0,51,52,52,52],
[54,43,44,49,0,45,44,48],
[55,49,52,48,55,0,48,53],
[56,51,59,48,56,52,0,52],
[56,54,51,48,52,47,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,91,84,100,84,100,57],
[50,0,91,84,91,75,84,64],
[9,9,0,16,66,16,16,23],
[16,16,84,0,100,57,50,57],
[0,9,34,0,0,9,34,34],
[16,25,84,43,91,0,50,64],
[0,16,84,50,66,50,0,48],
[43,36,77,43,66,36,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,45,47,52,58,55,45],
[41,0,55,44,43,46,48,50],
[55,45,0,47,50,53,50,42],
[53,56,53,0,54,62,48,52],
[48,57,50,46,0,53,58,50],
[42,54,47,38,47,0,50,43],
[45,52,50,52,42,50,0,53],
[55,50,58,48,50,57,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,42,45,53,58,80],
[50,0,61,50,61,67,63,49],
[44,39,0,56,62,56,59,54],
[58,50,44,0,74,72,49,56],
[55,39,38,26,0,81,43,53],
[47,33,44,28,19,0,56,37],
[42,37,41,51,57,44,0,48],
[20,51,46,44,47,63,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,17,17,32,12,8,28],
[97,0,58,42,81,58,53,60],
[83,42,0,76,92,60,43,47],
[83,58,24,0,65,19,41,49],
[68,19,8,35,0,6,28,52],
[88,42,40,81,94,0,46,49],
[92,47,57,59,72,54,0,47],
[72,40,53,51,48,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,47,49,58,53,53,54],
[60,0,48,48,53,55,49,66],
[53,52,0,63,58,45,48,52],
[51,52,37,0,55,48,45,50],
[42,47,42,45,0,38,42,47],
[47,45,55,52,62,0,49,52],
[47,51,52,55,58,51,0,46],
[46,34,48,50,53,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,50,56,55,48,50,57],
[46,0,47,61,49,48,54,53],
[50,53,0,59,47,53,54,55],
[44,39,41,0,43,39,43,41],
[45,51,53,57,0,50,58,56],
[52,52,47,61,50,0,57,55],
[50,46,46,57,42,43,0,52],
[43,47,45,59,44,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,58,51,21,52,57,41],
[51,0,51,56,49,59,49,40],
[42,49,0,45,49,51,62,40],
[49,44,55,0,42,51,69,39],
[79,51,51,58,0,68,49,51],
[48,41,49,49,32,0,51,41],
[43,51,38,31,51,49,0,43],
[59,60,60,61,49,59,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,66,60,35,48,48,58],
[32,0,55,40,42,62,53,43],
[34,45,0,47,42,49,37,36],
[40,60,53,0,42,44,44,36],
[65,58,58,58,0,45,47,35],
[52,38,51,56,55,0,59,47],
[52,47,63,56,53,41,0,48],
[42,57,64,64,65,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,46,52,40,49,49,53],
[61,0,50,50,49,54,55,54],
[54,50,0,55,53,54,49,54],
[48,50,45,0,43,51,51,56],
[60,51,47,57,0,53,57,55],
[51,46,46,49,47,0,46,44],
[51,45,51,49,43,54,0,49],
[47,46,46,44,45,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,51,55,51,48,58,52],
[47,0,38,50,39,42,48,50],
[49,62,0,60,49,50,60,50],
[45,50,40,0,38,44,53,38],
[49,61,51,62,0,50,56,48],
[52,58,50,56,50,0,54,50],
[42,52,40,47,44,46,0,43],
[48,50,50,62,52,50,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,49,37,48,53,38,26],
[29,0,30,21,28,48,7,37],
[51,70,0,56,48,60,55,58],
[63,79,44,0,53,54,60,40],
[52,72,52,47,0,65,50,27],
[47,52,40,46,35,0,28,41],
[62,93,45,40,50,72,0,50],
[74,63,42,60,73,59,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,52,48,52,56,56,63],
[37,0,40,46,46,47,47,56],
[48,60,0,54,52,50,49,63],
[52,54,46,0,54,55,57,66],
[48,54,48,46,0,53,51,57],
[44,53,50,45,47,0,52,58],
[44,53,51,43,49,48,0,60],
[37,44,37,34,43,42,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,62,59,49,53,57],
[43,0,50,52,52,49,50,46],
[52,50,0,54,47,48,55,50],
[38,48,46,0,52,56,54,50],
[41,48,53,48,0,40,57,46],
[51,51,52,44,60,0,57,53],
[47,50,45,46,43,43,0,51],
[43,54,50,50,54,47,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,54,55,58,48,59],
[50,0,63,47,48,60,51,60],
[47,37,0,51,48,48,39,52],
[46,53,49,0,47,56,40,57],
[45,52,52,53,0,51,55,60],
[42,40,52,44,49,0,52,46],
[52,49,61,60,45,48,0,60],
[41,40,48,43,40,54,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,71,46,56,63,55,67],
[45,0,63,37,59,52,37,55],
[29,37,0,33,48,35,28,42],
[54,63,67,0,56,54,44,62],
[44,41,52,44,0,49,46,48],
[37,48,65,46,51,0,49,47],
[45,63,72,56,54,51,0,58],
[33,45,58,38,52,53,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,59,50,52,57,52,54],
[42,0,44,37,46,51,49,48],
[41,56,0,42,45,52,58,49],
[50,63,58,0,59,64,58,64],
[48,54,55,41,0,61,56,51],
[43,49,48,36,39,0,44,42],
[48,51,42,42,44,56,0,54],
[46,52,51,36,49,58,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,52,58,54,50,52],
[47,0,40,57,52,45,45,42],
[56,60,0,54,50,54,49,52],
[48,43,46,0,51,45,41,51],
[42,48,50,49,0,50,45,50],
[46,55,46,55,50,0,47,43],
[50,55,51,59,55,53,0,58],
[48,58,48,49,50,57,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,55,51,45,48,49,51],
[48,0,60,51,49,55,49,49],
[45,40,0,48,40,48,50,53],
[49,49,52,0,51,53,45,50],
[55,51,60,49,0,50,47,50],
[52,45,52,47,50,0,53,46],
[51,51,50,55,53,47,0,54],
[49,51,47,50,50,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,63,50,56,57,56,57],
[41,0,57,40,38,54,46,44],
[37,43,0,42,43,47,49,50],
[50,60,58,0,55,53,51,54],
[44,62,57,45,0,59,54,53],
[43,46,53,47,41,0,44,50],
[44,54,51,49,46,56,0,56],
[43,56,50,46,47,50,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,53,50,47,53,50],
[48,0,56,55,55,48,55,46],
[48,44,0,46,49,44,52,47],
[47,45,54,0,41,44,49,45],
[50,45,51,59,0,54,54,48],
[53,52,56,56,46,0,58,52],
[47,45,48,51,46,42,0,48],
[50,54,53,55,52,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,80,54,52,50,88,65],
[45,0,80,69,75,86,87,62],
[20,20,0,8,36,47,73,31],
[46,31,92,0,62,73,86,69],
[48,25,64,38,0,61,73,48],
[50,14,53,27,39,0,61,44],
[12,13,27,14,27,39,0,14],
[35,38,69,31,52,56,86,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,34,40,39,41,59,44],
[52,0,33,59,39,30,77,28],
[66,67,0,60,48,51,94,47],
[60,41,40,0,59,24,73,46],
[61,61,52,41,0,35,74,47],
[59,70,49,76,65,0,97,63],
[41,23,6,27,26,3,0,14],
[56,72,53,54,53,37,86,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,49,46,55,47,53],
[50,0,46,55,52,50,48,54],
[52,54,0,60,54,52,50,53],
[51,45,40,0,43,44,40,50],
[54,48,46,57,0,46,52,54],
[45,50,48,56,54,0,55,50],
[53,52,50,60,48,45,0,54],
[47,46,47,50,46,50,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,47,46,55,43,45,51],
[41,0,41,42,47,39,49,42],
[53,59,0,47,43,48,55,50],
[54,58,53,0,42,58,49,46],
[45,53,57,58,0,52,68,55],
[57,61,52,42,48,0,50,36],
[55,51,45,51,32,50,0,43],
[49,58,50,54,45,64,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,54,56,56,59,47,55],
[46,0,50,50,50,54,51,43],
[46,50,0,50,51,51,48,46],
[44,50,50,0,47,55,42,47],
[44,50,49,53,0,58,48,42],
[41,46,49,45,42,0,37,44],
[53,49,52,58,52,63,0,47],
[45,57,54,53,58,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,46,47,39,41,48,46],
[59,0,57,66,46,53,53,56],
[54,43,0,55,46,43,42,46],
[53,34,45,0,48,42,39,43],
[61,54,54,52,0,49,43,52],
[59,47,57,58,51,0,56,58],
[52,47,58,61,57,44,0,46],
[54,44,54,57,48,42,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,41,43,49,40,44,50],
[49,0,43,49,49,46,42,49],
[59,57,0,54,52,55,47,56],
[57,51,46,0,50,57,46,56],
[51,51,48,50,0,52,47,54],
[60,54,45,43,48,0,50,64],
[56,58,53,54,53,50,0,54],
[50,51,44,44,46,36,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,50,58,58,56,55],
[47,0,45,43,54,43,61,54],
[50,55,0,56,51,60,68,63],
[50,57,44,0,49,51,56,52],
[42,46,49,51,0,47,55,50],
[42,57,40,49,53,0,61,52],
[44,39,32,44,45,39,0,47],
[45,46,37,48,50,48,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,57,55,56,52,72],
[51,0,39,57,51,56,49,53],
[52,61,0,53,44,58,55,54],
[43,43,47,0,49,47,46,53],
[45,49,56,51,0,54,44,52],
[44,44,42,53,46,0,49,48],
[48,51,45,54,56,51,0,58],
[28,47,46,47,48,52,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,34,32,48,34,47,49],
[58,0,48,46,62,49,62,40],
[66,52,0,61,73,54,58,50],
[68,54,39,0,51,62,44,38],
[52,38,27,49,0,42,46,45],
[66,51,46,38,58,0,63,48],
[53,38,42,56,54,37,0,37],
[51,60,50,62,55,52,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,47,43,49,56,60],
[48,0,51,48,48,44,52,56],
[44,49,0,52,43,51,49,57],
[53,52,48,0,50,47,54,57],
[57,52,57,50,0,51,60,67],
[51,56,49,53,49,0,58,60],
[44,48,51,46,40,42,0,56],
[40,44,43,43,33,40,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,50,47,37,51,46],
[49,0,54,43,49,48,48,47],
[54,46,0,45,47,41,46,42],
[50,57,55,0,60,52,55,55],
[53,51,53,40,0,47,49,49],
[63,52,59,48,53,0,53,53],
[49,52,54,45,51,47,0,49],
[54,53,58,45,51,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,62,49,51,58,53,49],
[29,0,57,40,50,57,33,47],
[38,43,0,31,51,54,44,48],
[51,60,69,0,59,68,38,53],
[49,50,49,41,0,53,36,40],
[42,43,46,32,47,0,37,44],
[47,67,56,62,64,63,0,63],
[51,53,52,47,60,56,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,53,51,44,57,50],
[49,0,57,48,46,47,51,56],
[48,43,0,51,53,42,51,62],
[47,52,49,0,58,48,48,54],
[49,54,47,42,0,50,51,52],
[56,53,58,52,50,0,55,61],
[43,49,49,52,49,45,0,54],
[50,44,38,46,48,39,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,42,41,40,52,60,44],
[35,0,49,53,46,45,51,51],
[58,51,0,54,44,41,54,53],
[59,47,46,0,38,47,60,51],
[60,54,56,62,0,51,49,71],
[48,55,59,53,49,0,64,55],
[40,49,46,40,51,36,0,48],
[56,49,47,49,29,45,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,55,40,53,48,47,50],
[56,0,57,44,49,50,46,46],
[45,43,0,45,48,42,42,45],
[60,56,55,0,63,43,54,64],
[47,51,52,37,0,48,49,53],
[52,50,58,57,52,0,54,54],
[53,54,58,46,51,46,0,56],
[50,54,55,36,47,46,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,55,57,60,34,44,37],
[36,0,56,53,51,46,37,50],
[45,44,0,46,55,38,58,48],
[43,47,54,0,51,48,52,54],
[40,49,45,49,0,35,42,40],
[66,54,62,52,65,0,69,47],
[56,63,42,48,58,31,0,34],
[63,50,52,46,60,53,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,54,49,51,43,46],
[52,0,59,61,52,52,50,58],
[48,41,0,45,47,50,41,48],
[46,39,55,0,49,55,33,55],
[51,48,53,51,0,57,48,51],
[49,48,50,45,43,0,38,43],
[57,50,59,67,52,62,0,51],
[54,42,52,45,49,57,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,39,17,28,44,50,33],
[61,0,45,51,56,59,35,40],
[61,55,0,45,48,60,45,21],
[83,49,55,0,38,49,43,40],
[72,44,52,62,0,67,40,56],
[56,41,40,51,33,0,36,39],
[50,65,55,57,60,64,0,45],
[67,60,79,60,44,61,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,53,46,60,56,54],
[50,0,54,58,53,62,62,40],
[43,46,0,50,45,47,48,38],
[47,42,50,0,53,51,62,40],
[54,47,55,47,0,56,54,41],
[40,38,53,49,44,0,47,38],
[44,38,52,38,46,53,0,44],
[46,60,62,60,59,62,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,55,25,19,32,54,35],
[56,0,68,46,46,65,60,69],
[45,32,0,13,4,13,51,41],
[75,54,87,0,42,58,67,74],
[81,54,96,58,0,39,71,91],
[68,35,87,42,61,0,60,52],
[46,40,49,33,29,40,0,64],
[65,31,59,26,9,48,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,53,44,57,50,54,44],
[59,0,67,50,50,56,52,50],
[47,33,0,31,44,44,45,42],
[56,50,69,0,63,53,53,48],
[43,50,56,37,0,47,47,45],
[50,44,56,47,53,0,44,49],
[46,48,55,47,53,56,0,47],
[56,50,58,52,55,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,55,43,53,57,53,56],
[53,0,50,47,48,50,58,41],
[45,50,0,45,43,46,46,51],
[57,53,55,0,52,47,48,46],
[47,52,57,48,0,52,47,52],
[43,50,54,53,48,0,54,51],
[47,42,54,52,53,46,0,50],
[44,59,49,54,48,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,45,34,26,48,47,44],
[70,0,70,43,51,53,64,52],
[55,30,0,38,39,37,59,53],
[66,57,62,0,47,37,44,57],
[74,49,61,53,0,50,68,53],
[52,47,63,63,50,0,62,60],
[53,36,41,56,32,38,0,47],
[56,48,47,43,47,40,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,48,57,52,53,51,54],
[52,0,54,58,55,53,49,55],
[52,46,0,57,51,46,40,55],
[43,42,43,0,42,48,38,47],
[48,45,49,58,0,50,49,51],
[47,47,54,52,50,0,44,47],
[49,51,60,62,51,56,0,58],
[46,45,45,53,49,53,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,44,55,18,39,42,27],
[38,0,43,53,27,48,36,25],
[56,57,0,62,53,40,45,42],
[45,47,38,0,30,47,36,27],
[82,73,47,70,0,64,52,47],
[61,52,60,53,36,0,48,52],
[58,64,55,64,48,52,0,43],
[73,75,58,73,53,48,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,49,46,63,63,57,48],
[40,0,46,46,42,64,55,55],
[51,54,0,44,41,65,43,53],
[54,54,56,0,49,69,51,42],
[37,58,59,51,0,72,50,52],
[37,36,35,31,28,0,45,29],
[43,45,57,49,50,55,0,41],
[52,45,47,58,48,71,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,42,43,50,51,39,49],
[61,0,57,50,70,59,61,61],
[58,43,0,45,47,50,48,45],
[57,50,55,0,55,59,52,51],
[50,30,53,45,0,42,33,38],
[49,41,50,41,58,0,48,47],
[61,39,52,48,67,52,0,46],
[51,39,55,49,62,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,4,80,45,20,30,6],
[27,0,4,54,41,20,26,6],
[96,96,0,96,74,47,74,74],
[20,46,4,0,45,20,24,26],
[55,59,26,55,0,28,79,33],
[80,80,53,80,72,0,57,37],
[70,74,26,76,21,43,0,33],
[94,94,26,74,67,63,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,62,52,54,63,57,50],
[47,0,66,49,53,51,58,45],
[38,34,0,41,45,41,40,36],
[48,51,59,0,58,50,61,47],
[46,47,55,42,0,46,46,40],
[37,49,59,50,54,0,56,46],
[43,42,60,39,54,44,0,47],
[50,55,64,53,60,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,50,66,61,59,56,57],
[43,0,50,50,46,45,55,48],
[50,50,0,62,47,53,52,51],
[34,50,38,0,46,44,48,51],
[39,54,53,54,0,55,53,52],
[41,55,47,56,45,0,52,51],
[44,45,48,52,47,48,0,52],
[43,52,49,49,48,49,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,45,49,29,54,43,39],
[42,0,13,49,25,30,34,34],
[55,87,0,73,50,72,57,64],
[51,51,27,0,41,29,50,36],
[71,75,50,59,0,60,38,57],
[46,70,28,71,40,0,48,54],
[57,66,43,50,62,52,0,47],
[61,66,36,64,43,46,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,57,60,43,46,50],
[51,0,59,56,70,36,53,61],
[52,41,0,50,55,42,57,57],
[43,44,50,0,53,42,51,57],
[40,30,45,47,0,38,43,54],
[57,64,58,58,62,0,47,59],
[54,47,43,49,57,53,0,56],
[50,39,43,43,46,41,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,42,46,49,51,53,35],
[48,0,62,51,67,61,76,55],
[58,38,0,34,38,46,50,44],
[54,49,66,0,64,57,70,63],
[51,33,62,36,0,37,73,44],
[49,39,54,43,63,0,61,51],
[47,24,50,30,27,39,0,38],
[65,45,56,37,56,49,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,55,44,51,57,45],
[53,0,44,56,50,50,54,48],
[53,56,0,58,58,50,54,48],
[45,44,42,0,44,44,47,48],
[56,50,42,56,0,55,56,59],
[49,50,50,56,45,0,49,51],
[43,46,46,53,44,51,0,43],
[55,52,52,52,41,49,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,61,50,47,49,42,47],
[50,0,49,46,43,52,45,49],
[39,51,0,45,43,48,44,49],
[50,54,55,0,45,49,49,46],
[53,57,57,55,0,58,50,58],
[51,48,52,51,42,0,41,52],
[58,55,56,51,50,59,0,54],
[53,51,51,54,42,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,52,50,45,50,51],
[49,0,42,45,44,46,52,47],
[47,58,0,47,50,45,47,54],
[48,55,53,0,53,50,54,56],
[50,56,50,47,0,47,52,51],
[55,54,55,50,53,0,57,53],
[50,48,53,46,48,43,0,50],
[49,53,46,44,49,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,58,59,57,56,53,47],
[47,0,52,50,53,55,46,46],
[42,48,0,53,52,49,52,46],
[41,50,47,0,63,50,55,45],
[43,47,48,37,0,43,42,47],
[44,45,51,50,57,0,50,46],
[47,54,48,45,58,50,0,50],
[53,54,54,55,53,54,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,45,51,57,52,59],
[51,0,52,51,49,60,48,55],
[46,48,0,43,47,55,48,48],
[55,49,57,0,56,61,47,51],
[49,51,53,44,0,51,46,50],
[43,40,45,39,49,0,39,40],
[48,52,52,53,54,61,0,48],
[41,45,52,49,50,60,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,57,50,54,56,60,56],
[42,0,48,38,47,47,45,37],
[43,52,0,42,42,39,49,49],
[50,62,58,0,54,52,53,52],
[46,53,58,46,0,52,52,47],
[44,53,61,48,48,0,62,51],
[40,55,51,47,48,38,0,42],
[44,63,51,48,53,49,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,46,53,56,56,60],
[53,0,55,50,49,54,62,59],
[46,45,0,50,48,54,55,53],
[54,50,50,0,61,52,56,55],
[47,51,52,39,0,56,53,57],
[44,46,46,48,44,0,46,58],
[44,38,45,44,47,54,0,53],
[40,41,47,45,43,42,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,49,53,44,52,45,50],
[56,0,50,52,55,52,54,53],
[51,50,0,42,50,49,50,57],
[47,48,58,0,49,56,51,54],
[56,45,50,51,0,51,60,51],
[48,48,51,44,49,0,55,57],
[55,46,50,49,40,45,0,52],
[50,47,43,46,49,43,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,55,53,48,51,46],
[47,0,50,50,45,56,51,44],
[44,50,0,44,44,48,42,47],
[45,50,56,0,53,53,49,43],
[47,55,56,47,0,55,44,50],
[52,44,52,47,45,0,47,43],
[49,49,58,51,56,53,0,49],
[54,56,53,57,50,57,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,37,41,48,46,35,44],
[54,0,39,41,55,50,45,49],
[63,61,0,50,62,55,51,61],
[59,59,50,0,54,43,41,47],
[52,45,38,46,0,52,51,45],
[54,50,45,57,48,0,45,52],
[65,55,49,59,49,55,0,52],
[56,51,39,53,55,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,46,53,38,43,54,57],
[61,0,54,59,47,54,50,49],
[54,46,0,61,50,53,59,53],
[47,41,39,0,41,51,45,47],
[62,53,50,59,0,61,54,54],
[57,46,47,49,39,0,46,55],
[46,50,41,55,46,54,0,42],
[43,51,47,53,46,45,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,55,49,53,56,49,49],
[45,0,49,54,43,38,43,44],
[45,51,0,48,43,56,48,46],
[51,46,52,0,46,48,43,52],
[47,57,57,54,0,49,51,52],
[44,62,44,52,51,0,50,42],
[51,57,52,57,49,50,0,52],
[51,56,54,48,48,58,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,50,58,46,46,51,50],
[42,0,46,77,52,48,67,63],
[50,54,0,81,53,52,70,62],
[42,23,19,0,27,36,38,46],
[54,48,47,73,0,43,67,68],
[54,52,48,64,57,0,64,60],
[49,33,30,62,33,36,0,53],
[50,37,38,54,32,40,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,49,53,45,60,46,53],
[39,0,42,41,47,47,41,47],
[51,58,0,48,56,64,56,55],
[47,59,52,0,52,61,49,49],
[55,53,44,48,0,56,50,39],
[40,53,36,39,44,0,49,50],
[54,59,44,51,50,51,0,48],
[47,53,45,51,61,50,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,55,49,55,54,56],
[50,0,48,54,52,43,50,55],
[48,52,0,39,42,41,53,52],
[45,46,61,0,49,54,56,55],
[51,48,58,51,0,53,56,48],
[45,57,59,46,47,0,54,47],
[46,50,47,44,44,46,0,44],
[44,45,48,45,52,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,52,50,54,47,56,44],
[45,0,44,48,51,51,43,35],
[48,56,0,54,60,47,51,52],
[50,52,46,0,48,58,51,47],
[46,49,40,52,0,40,43,47],
[53,49,53,42,60,0,45,50],
[44,57,49,49,57,55,0,40],
[56,65,48,53,53,50,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,46,46,47,49,40],
[55,0,28,50,50,56,50,49],
[57,72,0,52,46,52,62,58],
[54,50,48,0,52,54,55,61],
[54,50,54,48,0,60,52,59],
[53,44,48,46,40,0,40,28],
[51,50,38,45,48,60,0,49],
[60,51,42,39,41,72,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,48,54,52,46,43,38],
[60,0,53,61,49,52,52,55],
[52,47,0,68,55,46,57,33],
[46,39,32,0,45,44,43,33],
[48,51,45,55,0,41,54,43],
[54,48,54,56,59,0,51,45],
[57,48,43,57,46,49,0,47],
[62,45,67,67,57,55,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,62,38,49,55,51,43],
[45,0,55,42,34,46,49,44],
[38,45,0,34,35,44,43,35],
[62,58,66,0,56,60,59,50],
[51,66,65,44,0,59,47,52],
[45,54,56,40,41,0,44,44],
[49,51,57,41,53,56,0,40],
[57,56,65,50,48,56,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,0,45,23,43,24,24],
[73,0,59,56,34,43,59,42],
[100,41,0,83,61,69,64,61],
[55,44,17,0,4,24,21,4],
[77,66,39,96,0,63,63,86],
[57,57,31,76,37,0,40,54],
[76,41,36,79,37,60,0,63],
[76,58,39,96,14,46,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,56,33,57,38,55,50],
[32,0,52,57,30,33,30,50],
[44,48,0,49,43,49,63,50],
[67,43,51,0,30,53,56,70],
[43,70,57,70,0,59,77,45],
[62,67,51,47,41,0,72,65],
[45,70,37,44,23,28,0,45],
[50,50,50,30,55,35,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,51,44,76,55,60,62],
[67,0,74,50,67,85,38,62],
[49,26,0,35,76,53,49,57],
[56,50,65,0,74,41,65,45],
[24,33,24,26,0,41,43,45],
[45,15,47,59,59,0,49,40],
[40,62,51,35,57,51,0,40],
[38,38,43,55,55,60,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,54,49,43,53,57,54],
[58,0,57,50,58,41,51,56],
[46,43,0,32,55,38,39,55],
[51,50,68,0,62,54,61,49],
[57,42,45,38,0,47,45,37],
[47,59,62,46,53,0,53,53],
[43,49,61,39,55,47,0,43],
[46,44,45,51,63,47,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,43,46,50,46,56],
[52,0,50,48,49,51,44,46],
[48,50,0,45,47,53,46,44],
[57,52,55,0,53,50,49,53],
[54,51,53,47,0,45,45,46],
[50,49,47,50,55,0,48,54],
[54,56,54,51,55,52,0,48],
[44,54,56,47,54,46,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,70,63,53,65,59],
[53,0,60,85,68,34,45,61],
[44,40,0,62,51,43,43,55],
[30,15,38,0,39,13,36,25],
[37,32,49,61,0,36,51,51],
[47,66,57,87,64,0,39,51],
[35,55,57,64,49,61,0,46],
[41,39,45,75,49,49,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,44,56,49,49,65,59],
[52,0,36,53,45,49,54,57],
[56,64,0,62,50,59,58,64],
[44,47,38,0,41,53,63,61],
[51,55,50,59,0,51,55,60],
[51,51,41,47,49,0,56,56],
[35,46,42,37,45,44,0,62],
[41,43,36,39,40,44,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,43,39,49,45,39,52],
[58,0,44,43,31,48,43,55],
[57,56,0,46,34,61,53,56],
[61,57,54,0,50,57,60,54],
[51,69,66,50,0,52,57,58],
[55,52,39,43,48,0,50,55],
[61,57,47,40,43,50,0,50],
[48,45,44,46,42,45,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,41,52,68,59,45,39],
[55,0,44,44,64,62,43,49],
[59,56,0,50,65,59,43,49],
[48,56,50,0,62,63,56,50],
[32,36,35,38,0,57,37,35],
[41,38,41,37,43,0,39,42],
[55,57,57,44,63,61,0,48],
[61,51,51,50,65,58,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,61,59,50,51,73,58],
[45,0,56,61,54,51,61,46],
[39,44,0,50,48,33,68,38],
[41,39,50,0,47,43,56,44],
[50,46,52,53,0,45,66,49],
[49,49,67,57,55,0,78,62],
[27,39,32,44,34,22,0,41],
[42,54,62,56,51,38,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,48,47,45,42,49,65],
[49,0,55,68,56,60,60,61],
[52,45,0,51,53,53,57,50],
[53,32,49,0,60,47,50,63],
[55,44,47,40,0,44,56,59],
[58,40,47,53,56,0,52,54],
[51,40,43,50,44,48,0,46],
[35,39,50,37,41,46,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,54,50,49,52,50],
[46,0,37,39,37,45,45,41],
[51,63,0,49,42,51,51,48],
[46,61,51,0,50,56,48,54],
[50,63,58,50,0,55,53,53],
[51,55,49,44,45,0,51,53],
[48,55,49,52,47,49,0,55],
[50,59,52,46,47,47,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,51,49,53,58,77,59],
[35,0,45,51,50,45,69,51],
[49,55,0,63,55,55,66,55],
[51,49,37,0,45,54,60,52],
[47,50,45,55,0,49,64,59],
[42,55,45,46,51,0,57,44],
[23,31,34,40,36,43,0,27],
[41,49,45,48,41,56,73,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,54,51,53,54,61],
[41,0,47,60,64,56,47,54],
[52,53,0,48,54,61,50,54],
[46,40,52,0,52,45,49,56],
[49,36,46,48,0,58,56,57],
[47,44,39,55,42,0,47,49],
[46,53,50,51,44,53,0,52],
[39,46,46,44,43,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,48,48,53,53,56],
[53,0,52,54,47,46,48,43],
[50,48,0,55,50,54,57,49],
[52,46,45,0,43,52,51,52],
[52,53,50,57,0,49,54,51],
[47,54,46,48,51,0,48,49],
[47,52,43,49,46,52,0,46],
[44,57,51,48,49,51,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,59,59,50,53,49,54],
[35,0,55,48,40,46,45,37],
[41,45,0,52,50,39,44,36],
[41,52,48,0,45,57,42,40],
[50,60,50,55,0,48,44,44],
[47,54,61,43,52,0,54,53],
[51,55,56,58,56,46,0,58],
[46,63,64,60,56,47,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,58,59,49,46,47,49],
[48,0,58,54,49,54,40,43],
[42,42,0,39,43,50,34,45],
[41,46,61,0,36,50,39,43],
[51,51,57,64,0,55,42,48],
[54,46,50,50,45,0,37,51],
[53,60,66,61,58,63,0,50],
[51,57,55,57,52,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,35,0,47,47,18,100],
[65,0,35,18,65,65,18,100],
[65,65,0,18,65,65,18,100],
[100,82,82,0,65,65,18,100],
[53,35,35,35,0,47,53,53],
[53,35,35,35,53,0,53,53],
[82,82,82,82,47,47,0,82],
[0,0,0,0,47,47,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,47,46,68,45,55,51],
[54,0,47,57,62,44,63,51],
[53,53,0,63,70,39,77,59],
[54,43,37,0,56,55,55,40],
[32,38,30,44,0,39,53,50],
[55,56,61,45,61,0,70,57],
[45,37,23,45,47,30,0,42],
[49,49,41,60,50,43,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,56,50,50,48,52],
[50,0,46,57,45,50,48,45],
[51,54,0,47,53,49,55,50],
[44,43,53,0,50,49,46,47],
[50,55,47,50,0,54,50,45],
[50,50,51,51,46,0,43,47],
[52,52,45,54,50,57,0,47],
[48,55,50,53,55,53,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,53,51,51,55,49,57],
[45,0,45,46,46,49,42,46],
[47,55,0,46,46,53,52,52],
[49,54,54,0,55,52,50,53],
[49,54,54,45,0,53,45,52],
[45,51,47,48,47,0,47,51],
[51,58,48,50,55,53,0,57],
[43,54,48,47,48,49,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,49,51,47,53,56,43],
[54,0,47,53,50,48,53,52],
[51,53,0,56,57,46,60,50],
[49,47,44,0,47,54,55,49],
[53,50,43,53,0,49,63,49],
[47,52,54,46,51,0,55,51],
[44,47,40,45,37,45,0,44],
[57,48,50,51,51,49,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,47,37,47,44,45,51],
[52,0,53,57,53,54,44,60],
[53,47,0,42,58,60,42,61],
[63,43,58,0,47,59,55,52],
[53,47,42,53,0,40,46,55],
[56,46,40,41,60,0,53,53],
[55,56,58,45,54,47,0,63],
[49,40,39,48,45,47,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,55,35,43,39,46,30],
[46,0,37,33,39,46,50,32],
[45,63,0,53,47,34,33,22],
[65,67,47,0,69,49,38,44],
[57,61,53,31,0,41,56,25],
[61,54,66,51,59,0,50,54],
[54,50,67,62,44,50,0,33],
[70,68,78,56,75,46,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,58,54,39,56,61],
[49,0,64,54,57,65,52,59],
[46,36,0,41,47,41,48,46],
[42,46,59,0,59,46,45,57],
[46,43,53,41,0,52,42,48],
[61,35,59,54,48,0,55,60],
[44,48,52,55,58,45,0,64],
[39,41,54,43,52,40,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,59,52,42,53,47,32],
[62,0,55,61,47,54,57,57],
[41,45,0,50,46,33,39,39],
[48,39,50,0,28,46,48,33],
[58,53,54,72,0,48,68,50],
[47,46,67,54,52,0,48,36],
[53,43,61,52,32,52,0,53],
[68,43,61,67,50,64,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,49,51,66,42,46,43],
[47,0,44,53,58,56,47,46],
[51,56,0,62,59,48,43,48],
[49,47,38,0,50,50,46,45],
[34,42,41,50,0,37,35,42],
[58,44,52,50,63,0,52,53],
[54,53,57,54,65,48,0,47],
[57,54,52,55,58,47,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,51,48,51,51,49],
[44,0,52,45,45,45,52,46],
[44,48,0,46,49,44,46,43],
[49,55,54,0,49,53,50,54],
[52,55,51,51,0,51,53,48],
[49,55,56,47,49,0,50,49],
[49,48,54,50,47,50,0,47],
[51,54,57,46,52,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,59,66,50,62,58,51],
[45,0,52,55,59,53,59,56],
[41,48,0,53,46,48,57,41],
[34,45,47,0,40,38,51,41],
[50,41,54,60,0,55,50,46],
[38,47,52,62,45,0,46,42],
[42,41,43,49,50,54,0,52],
[49,44,59,59,54,58,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,50,53,53,44,47],
[53,0,54,49,50,54,52,49],
[46,46,0,49,48,53,43,51],
[50,51,51,0,57,56,54,49],
[47,50,52,43,0,53,42,50],
[47,46,47,44,47,0,46,51],
[56,48,57,46,58,54,0,53],
[53,51,49,51,50,49,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,68,40,42,55,52,63],
[41,0,58,42,41,57,41,61],
[32,42,0,44,35,44,43,37],
[60,58,56,0,49,57,50,61],
[58,59,65,51,0,63,46,68],
[45,43,56,43,37,0,40,58],
[48,59,57,50,54,60,0,55],
[37,39,63,39,32,42,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,38,42,45,43,45],
[54,0,46,43,42,41,47,41],
[58,54,0,46,48,53,51,56],
[62,57,54,0,60,52,48,53],
[58,58,52,40,0,44,48,46],
[55,59,47,48,56,0,55,47],
[57,53,49,52,52,45,0,50],
[55,59,44,47,54,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,54,45,58,45,45],
[51,0,52,57,61,68,62,41],
[52,48,0,57,60,61,45,51],
[46,43,43,0,55,64,44,46],
[55,39,40,45,0,63,40,51],
[42,32,39,36,37,0,41,45],
[55,38,55,56,60,59,0,53],
[55,59,49,54,49,55,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,47,55,50,55,41,55],
[44,0,37,40,47,48,44,53],
[53,63,0,50,52,58,56,55],
[45,60,50,0,56,52,50,57],
[50,53,48,44,0,54,49,56],
[45,52,42,48,46,0,45,52],
[59,56,44,50,51,55,0,58],
[45,47,45,43,44,48,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,51,53,58,60,53,49],
[59,0,45,49,65,52,48,48],
[49,55,0,54,71,56,58,40],
[47,51,46,0,61,40,54,45],
[42,35,29,39,0,51,34,31],
[40,48,44,60,49,0,54,44],
[47,52,42,46,66,46,0,51],
[51,52,60,55,69,56,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,56,47,49,47,47,52],
[52,0,50,47,57,54,45,53],
[44,50,0,49,42,39,44,50],
[53,53,51,0,53,55,47,55],
[51,43,58,47,0,43,52,52],
[53,46,61,45,57,0,54,54],
[53,55,56,53,48,46,0,58],
[48,47,50,45,48,46,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,54,50,41,64,54],
[44,0,37,49,47,41,66,33],
[50,63,0,55,55,53,63,48],
[46,51,45,0,42,42,58,49],
[50,53,45,58,0,43,68,49],
[59,59,47,58,57,0,61,43],
[36,34,37,42,32,39,0,38],
[46,67,52,51,51,57,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,24,24,24,56,24],
[76,0,24,24,68,24,56,68],
[76,76,0,68,68,68,32,44],
[76,76,32,0,100,100,32,44],
[76,32,32,0,0,32,32,0],
[76,76,32,0,68,0,32,44],
[44,44,68,68,68,68,0,68],
[76,32,56,56,100,56,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,55,54,56,46,44],
[53,0,50,41,54,48,45,42],
[50,50,0,51,52,46,44,49],
[45,59,49,0,61,51,52,51],
[46,46,48,39,0,48,46,42],
[44,52,54,49,52,0,55,50],
[54,55,56,48,54,45,0,54],
[56,58,51,49,58,50,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,52,57,52,53,50],
[43,0,52,49,51,48,48,52],
[41,48,0,57,58,52,41,45],
[48,51,43,0,53,44,57,48],
[43,49,42,47,0,47,51,37],
[48,52,48,56,53,0,52,42],
[47,52,59,43,49,48,0,56],
[50,48,55,52,63,58,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,38,50,40,37,43,50],
[54,0,45,53,46,48,45,47],
[62,55,0,55,49,56,54,58],
[50,47,45,0,47,41,44,52],
[60,54,51,53,0,49,48,56],
[63,52,44,59,51,0,48,48],
[57,55,46,56,52,52,0,61],
[50,53,42,48,44,52,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,44,57,61,37,57,49],
[38,0,39,50,58,46,41,45],
[56,61,0,52,61,52,44,59],
[43,50,48,0,57,44,49,51],
[39,42,39,43,0,33,42,44],
[63,54,48,56,67,0,60,64],
[43,59,56,51,58,40,0,48],
[51,55,41,49,56,36,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,51,45,42,47,39],
[53,0,56,56,38,45,55,45],
[53,44,0,54,59,41,54,45],
[49,44,46,0,48,52,47,40],
[55,62,41,52,0,46,52,54],
[58,55,59,48,54,0,60,42],
[53,45,46,53,48,40,0,49],
[61,55,55,60,46,58,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 100, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_8_100.csv", index=False, header=False)