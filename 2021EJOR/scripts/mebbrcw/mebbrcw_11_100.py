
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,67,30,43,48,55,62,44,43,37,39],
[33,0,27,31,31,44,46,33,32,35,30],
[70,73,0,61,54,60,62,43,35,54,40],
[57,69,39,0,66,50,58,54,55,39,44],
[52,69,46,34,0,51,49,42,51,49,39],
[45,56,40,50,49,0,50,32,56,52,36],
[38,54,38,42,51,50,0,42,42,50,39],
[56,67,57,46,58,68,58,0,52,60,46],
[57,68,65,45,49,44,58,48,0,48,38],
[63,65,46,61,51,48,50,40,52,0,50],
[61,70,60,56,61,64,61,54,62,50,0]])



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
result = np.append(np.array([11, 100, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,53,61,68,84,46,74,80,55,47],
[38,0,27,27,54,88,46,59,68,35,49],
[47,73,0,50,68,83,65,83,83,82,50],
[39,73,50,0,68,83,65,82,54,68,56],
[32,46,32,32,0,55,32,47,46,20,56],
[16,12,17,17,45,0,32,35,30,27,35],
[54,54,35,35,68,68,0,61,62,50,64],
[26,41,17,18,53,65,39,0,59,26,61],
[20,32,17,46,54,70,38,41,0,41,41],
[45,65,18,32,80,73,50,74,59,0,56],
[53,51,50,44,44,65,36,39,59,44,0]])



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
result = np.append(np.array([11, 100, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,65,55,65,45,49,59,47,52,58],
[34,0,54,41,40,37,45,42,42,39,47],
[35,46,0,41,38,36,41,46,45,39,47],
[45,59,59,0,52,51,51,58,50,46,59],
[35,60,62,48,0,49,46,57,40,52,57],
[55,63,64,49,51,0,51,65,53,59,53],
[51,55,59,49,54,49,0,55,44,58,54],
[41,58,54,42,43,35,45,0,37,52,48],
[53,58,55,50,60,47,56,63,0,58,47],
[48,61,61,54,48,41,42,48,42,0,57],
[42,53,53,41,43,47,46,52,53,43,0]])



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
result = np.append(np.array([11, 100, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,63,54,44,51,43,47,49,57],
[54,0,51,64,62,50,56,62,48,50,58],
[52,49,0,61,56,50,60,44,47,54,44],
[37,36,39,0,55,45,38,50,40,38,52],
[46,38,44,45,0,31,45,49,39,41,49],
[56,50,50,55,69,0,60,59,51,49,57],
[49,44,40,62,55,40,0,51,45,46,55],
[57,38,56,50,51,41,49,0,43,53,52],
[53,52,53,60,61,49,55,57,0,63,55],
[51,50,46,62,59,51,54,47,37,0,59],
[43,42,56,48,51,43,45,48,45,41,0]])



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
result = np.append(np.array([11, 100, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,53,32,46,38,26,36,28,65,40],
[62,0,61,55,63,63,46,49,41,72,59],
[47,39,0,44,43,40,40,40,44,41,40],
[68,45,56,0,61,63,50,56,57,60,62],
[54,37,57,39,0,49,47,41,37,49,37],
[62,37,60,37,51,0,18,42,40,55,41],
[74,54,60,50,53,82,0,44,67,57,47],
[64,51,60,44,59,58,56,0,44,63,59],
[72,59,56,43,63,60,33,56,0,48,59],
[35,28,59,40,51,45,43,37,52,0,53],
[60,41,60,38,63,59,53,41,41,47,0]])



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
result = np.append(np.array([11, 100, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,55,48,46,38,33,35,45,49,47],
[44,0,54,46,36,34,35,38,49,41,39],
[45,46,0,36,33,28,34,32,47,44,40],
[52,54,64,0,43,43,48,41,55,61,47],
[54,64,67,57,0,38,48,39,54,59,44],
[62,66,72,57,62,0,52,51,60,63,46],
[67,65,66,52,52,48,0,54,54,65,51],
[65,62,68,59,61,49,46,0,61,62,47],
[55,51,53,45,46,40,46,39,0,52,44],
[51,59,56,39,41,37,35,38,48,0,40],
[53,61,60,53,56,54,49,53,56,60,0]])



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
result = np.append(np.array([11, 100, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,28,18,25,29,9,18,14,13,51],
[82,0,61,58,36,46,54,63,34,58,58],
[72,39,0,29,33,34,62,38,50,35,46],
[82,42,71,0,67,56,61,58,56,37,76],
[75,64,67,33,0,45,29,40,36,37,48],
[71,54,66,44,55,0,71,66,53,54,76],
[91,46,38,39,71,29,0,49,30,34,51],
[82,37,62,42,60,34,51,0,26,21,63],
[86,66,50,44,64,47,70,74,0,50,65],
[87,42,65,63,63,46,66,79,50,0,73],
[49,42,54,24,52,24,49,37,35,27,0]])



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
result = np.append(np.array([11, 100, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,56,71,62,56,56,59,50,61,56],
[42,0,50,57,60,58,53,51,54,55,59],
[44,50,0,61,53,48,52,43,39,50,41],
[29,43,39,0,52,50,43,47,41,60,54],
[38,40,47,48,0,49,46,57,46,52,46],
[44,42,52,50,51,0,38,43,40,51,45],
[44,47,48,57,54,62,0,42,55,52,54],
[41,49,57,53,43,57,58,0,49,62,56],
[50,46,61,59,54,60,45,51,0,57,48],
[39,45,50,40,48,49,48,38,43,0,49],
[44,41,59,46,54,55,46,44,52,51,0]])



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
result = np.append(np.array([11, 100, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,46,53,41,37,48,48,51,43],
[50,0,54,52,44,52,39,46,47,57,39],
[48,46,0,43,49,43,39,37,46,59,43],
[54,48,57,0,48,48,38,48,50,50,44],
[47,56,51,52,0,48,38,47,50,52,46],
[59,48,57,52,52,0,46,48,53,56,49],
[63,61,61,62,62,54,0,49,59,64,57],
[52,54,63,52,53,52,51,0,56,59,48],
[52,53,54,50,50,47,41,44,0,52,48],
[49,43,41,50,48,44,36,41,48,0,46],
[57,61,57,56,54,51,43,52,52,54,0]])



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
result = np.append(np.array([11, 100, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,45,51,64,60,51,48,61,48,52],
[40,0,45,24,48,39,53,38,46,52,37],
[55,55,0,41,50,51,62,49,52,48,48],
[49,76,59,0,75,71,61,55,67,65,56],
[36,52,50,25,0,48,48,36,43,48,47],
[40,61,49,29,52,0,50,45,52,50,54],
[49,47,38,39,52,50,0,49,54,44,50],
[52,62,51,45,64,55,51,0,54,50,46],
[39,54,48,33,57,48,46,46,0,48,49],
[52,48,52,35,52,50,56,50,52,0,44],
[48,63,52,44,53,46,50,54,51,56,0]])



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
result = np.append(np.array([11, 100, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,43,50,47,46,51,52,48,47],
[53,0,49,49,50,55,56,56,55,50,47],
[55,51,0,52,49,53,57,54,52,57,44],
[57,51,48,0,52,48,57,54,52,55,52],
[50,50,51,48,0,54,56,54,47,56,39],
[53,45,47,52,46,0,49,53,51,54,46],
[54,44,43,43,44,51,0,51,55,50,47],
[49,44,46,46,46,47,49,0,48,47,47],
[48,45,48,48,53,49,45,52,0,49,46],
[52,50,43,45,44,46,50,53,51,0,49],
[53,53,56,48,61,54,53,53,54,51,0]])



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
result = np.append(np.array([11, 100, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,58,58,44,33,42,51,49,52,29],
[49,0,48,65,49,45,50,45,56,49,36],
[42,52,0,58,51,41,34,49,61,45,37],
[42,35,42,0,46,32,27,34,45,43,41],
[56,51,49,54,0,45,41,46,44,53,40],
[67,55,59,68,55,0,54,60,57,52,42],
[58,50,66,73,59,46,0,66,62,62,52],
[49,55,51,66,54,40,34,0,53,44,26],
[51,44,39,55,56,43,38,47,0,40,29],
[48,51,55,57,47,48,38,56,60,0,41],
[71,64,63,59,60,58,48,74,71,59,0]])



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
result = np.append(np.array([11, 100, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,46,49,47,43,46,52,54,46,53],
[47,0,52,54,48,46,47,52,50,48,49],
[54,48,0,50,44,49,45,54,51,39,62],
[51,46,50,0,47,48,45,49,47,46,52],
[53,52,56,53,0,57,56,52,57,44,52],
[57,54,51,52,43,0,51,50,54,51,60],
[54,53,55,55,44,49,0,52,58,47,59],
[48,48,46,51,48,50,48,0,49,39,51],
[46,50,49,53,43,46,42,51,0,44,53],
[54,52,61,54,56,49,53,61,56,0,55],
[47,51,38,48,48,40,41,49,47,45,0]])



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
result = np.append(np.array([11, 100, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,53,48,42,54,53,48,53,52],
[51,0,45,51,48,43,51,49,43,54,47],
[51,55,0,58,58,52,57,51,47,57,56],
[47,49,42,0,49,50,51,53,49,57,51],
[52,52,42,51,0,49,49,57,46,52,52],
[58,57,48,50,51,0,55,55,54,52,50],
[46,49,43,49,51,45,0,51,49,48,46],
[47,51,49,47,43,45,49,0,47,54,52],
[52,57,53,51,54,46,51,53,0,57,56],
[47,46,43,43,48,48,52,46,43,0,48],
[48,53,44,49,48,50,54,48,44,52,0]])



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
result = np.append(np.array([11, 100, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,55,48,71,74,72,80,62,53,73],
[28,0,61,43,41,46,25,44,41,47,43],
[45,39,0,39,58,65,56,65,58,38,58],
[52,57,61,0,59,79,57,79,69,40,55],
[29,59,42,41,0,70,33,51,88,66,71],
[26,54,35,21,30,0,55,32,38,23,20],
[28,75,44,43,67,45,0,50,63,50,43],
[20,56,35,21,49,68,50,0,64,48,73],
[38,59,42,31,12,62,37,36,0,45,42],
[47,53,62,60,34,77,50,52,55,0,75],
[27,57,42,45,29,80,57,27,58,25,0]])



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
result = np.append(np.array([11, 100, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,44,46,53,51,46,53,44,39,58],
[52,0,44,55,50,53,51,57,56,53,57],
[56,56,0,58,52,52,51,60,50,43,53],
[54,45,42,0,56,53,47,54,47,41,48],
[47,50,48,44,0,52,53,49,52,44,64],
[49,47,48,47,48,0,56,53,54,48,56],
[54,49,49,53,47,44,0,53,58,50,55],
[47,43,40,46,51,47,47,0,57,42,51],
[56,44,50,53,48,46,42,43,0,51,51],
[61,47,57,59,56,52,50,58,49,0,57],
[42,43,47,52,36,44,45,49,49,43,0]])



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
result = np.append(np.array([11, 100, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,36,44,62,28,40,61,47,39,42],
[50,0,49,49,59,49,37,57,47,52,46],
[64,51,0,50,61,48,45,67,39,56,52],
[56,51,50,0,60,38,56,62,44,51,55],
[38,41,39,40,0,37,27,60,39,45,40],
[72,51,52,62,63,0,34,72,56,48,50],
[60,63,55,44,73,66,0,72,64,64,52],
[39,43,33,38,40,28,28,0,35,36,44],
[53,53,61,56,61,44,36,65,0,54,57],
[61,48,44,49,55,52,36,64,46,0,48],
[58,54,48,45,60,50,48,56,43,52,0]])



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
result = np.append(np.array([11, 100, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,38,42,55,43,43,46,49,43,59],
[46,0,46,35,50,46,41,43,51,41,55],
[62,54,0,45,59,51,47,57,54,45,61],
[58,65,55,0,62,47,53,52,57,53,66],
[45,50,41,38,0,37,31,44,44,37,53],
[57,54,49,53,63,0,50,59,46,50,62],
[57,59,53,47,69,50,0,51,65,48,59],
[54,57,43,48,56,41,49,0,51,43,66],
[51,49,46,43,56,54,35,49,0,42,55],
[57,59,55,47,63,50,52,57,58,0,61],
[41,45,39,34,47,38,41,34,45,39,0]])



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
result = np.append(np.array([11, 100, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,41,45,50,43,37,37,47,47],
[53,0,53,58,46,59,47,51,56,43,51],
[51,47,0,60,53,56,51,47,51,51,50],
[59,42,40,0,47,53,52,41,48,51,54],
[55,54,47,53,0,55,48,45,51,48,46],
[50,41,44,47,45,0,41,43,50,39,49],
[57,53,49,48,52,59,0,49,49,54,53],
[63,49,53,59,55,57,51,0,55,50,47],
[63,44,49,52,49,50,51,45,0,50,53],
[53,57,49,49,52,61,46,50,50,0,50],
[53,49,50,46,54,51,47,53,47,50,0]])



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
result = np.append(np.array([11, 100, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,61,59,49,53,56,50,55,49,46],
[41,0,56,51,51,42,50,40,52,47,36],
[39,44,0,55,38,50,46,38,49,41,37],
[41,49,45,0,41,45,52,44,46,41,39],
[51,49,62,59,0,52,57,51,57,61,44],
[47,58,50,55,48,0,53,45,49,55,51],
[44,50,54,48,43,47,0,39,47,42,45],
[50,60,62,56,49,55,61,0,56,59,52],
[45,48,51,54,43,51,53,44,0,46,41],
[51,53,59,59,39,45,58,41,54,0,47],
[54,64,63,61,56,49,55,48,59,53,0]])



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
result = np.append(np.array([11, 100, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,44,55,51,60,52,54,61,56],
[48,0,57,37,42,51,57,40,51,49,56],
[48,43,0,40,44,50,51,44,52,58,59],
[56,63,60,0,51,59,64,48,49,54,56],
[45,58,56,49,0,63,55,56,55,51,66],
[49,49,50,41,37,0,66,44,51,50,51],
[40,43,49,36,45,34,0,35,41,43,55],
[48,60,56,52,44,56,65,0,49,61,64],
[46,49,48,51,45,49,59,51,0,57,66],
[39,51,42,46,49,50,57,39,43,0,57],
[44,44,41,44,34,49,45,36,34,43,0]])



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
result = np.append(np.array([11, 100, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,57,52,48,50,61,51,50,52],
[55,0,57,55,53,52,41,56,52,50,55],
[41,43,0,57,48,59,37,62,45,54,55],
[43,45,43,0,51,45,41,45,44,42,50],
[48,47,52,49,0,57,36,61,45,50,53],
[52,48,41,55,43,0,38,55,43,49,46],
[50,59,63,59,64,62,0,63,56,64,60],
[39,44,38,55,39,45,37,0,51,50,54],
[49,48,55,56,55,57,44,49,0,56,50],
[50,50,46,58,50,51,36,50,44,0,51],
[48,45,45,50,47,54,40,46,50,49,0]])



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
result = np.append(np.array([11, 100, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,53,54,44,66,58,63,47,41,61],
[29,0,51,46,37,55,43,51,57,27,39],
[47,49,0,45,51,54,37,58,52,60,56],
[46,54,55,0,39,50,48,58,48,47,50],
[56,63,49,61,0,64,49,60,59,49,56],
[34,45,46,50,36,0,22,48,49,41,51],
[42,57,63,52,51,78,0,62,51,45,52],
[37,49,42,42,40,52,38,0,57,31,51],
[53,43,48,52,41,51,49,43,0,39,47],
[59,73,40,53,51,59,55,69,61,0,53],
[39,61,44,50,44,49,48,49,53,47,0]])



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
result = np.append(np.array([11, 100, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,50,53,54,57,50,52,44,53],
[48,0,52,55,48,46,53,44,44,43,47],
[47,48,0,53,55,48,51,50,44,53,50],
[50,45,47,0,46,47,50,52,49,47,44],
[47,52,45,54,0,57,55,50,54,48,48],
[46,54,52,53,43,0,54,46,46,48,45],
[43,47,49,50,45,46,0,44,47,47,48],
[50,56,50,48,50,54,56,0,47,49,45],
[48,56,56,51,46,54,53,53,0,43,48],
[56,57,47,53,52,52,53,51,57,0,54],
[47,53,50,56,52,55,52,55,52,46,0]])



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
result = np.append(np.array([11, 100, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,58,49,61,56,66,50,47,54,46],
[58,0,50,50,53,55,52,53,53,51,47],
[42,50,0,42,48,53,55,34,47,59,36],
[51,50,58,0,66,63,68,57,49,62,61],
[39,47,52,34,0,50,57,38,40,53,44],
[44,45,47,37,50,0,52,39,52,52,48],
[34,48,45,32,43,48,0,24,46,53,34],
[50,47,66,43,62,61,76,0,44,61,42],
[53,47,53,51,60,48,54,56,0,56,43],
[46,49,41,38,47,48,47,39,44,0,39],
[54,53,64,39,56,52,66,58,57,61,0]])



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
result = np.append(np.array([11, 100, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,37,42,49,36,51,51,56,55,43],
[54,0,51,52,54,51,55,42,54,47,53],
[63,49,0,45,60,50,50,44,57,49,57],
[58,48,55,0,62,50,43,57,51,54,63],
[51,46,40,38,0,47,50,42,45,36,43],
[64,49,50,50,53,0,41,46,41,57,47],
[49,45,50,57,50,59,0,47,61,47,51],
[49,58,56,43,58,54,53,0,57,60,46],
[44,46,43,49,55,59,39,43,0,54,54],
[45,53,51,46,64,43,53,40,46,0,54],
[57,47,43,37,57,53,49,54,46,46,0]])



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
result = np.append(np.array([11, 100, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,50,48,37,50,48,41,40,42,47],
[65,0,57,61,63,50,63,48,49,53,63],
[50,43,0,62,52,60,52,49,59,53,55],
[52,39,38,0,41,52,40,38,40,38,49],
[63,37,48,59,0,56,54,41,51,44,49],
[50,50,40,48,44,0,48,45,49,55,49],
[52,37,48,60,46,52,0,54,52,54,54],
[59,52,51,62,59,55,46,0,52,53,49],
[60,51,41,60,49,51,48,48,0,60,52],
[58,47,47,62,56,45,46,47,40,0,50],
[53,37,45,51,51,51,46,51,48,50,0]])



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
result = np.append(np.array([11, 100, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,38,47,49,60,49,39,42,46,50],
[47,0,41,47,42,54,40,37,51,57,49],
[62,59,0,50,58,64,54,41,49,55,60],
[53,53,50,0,51,62,59,35,44,50,53],
[51,58,42,49,0,56,54,50,50,51,51],
[40,46,36,38,44,0,46,41,34,50,42],
[51,60,46,41,46,54,0,49,43,49,53],
[61,63,59,65,50,59,51,0,55,57,54],
[58,49,51,56,50,66,57,45,0,53,53],
[54,43,45,50,49,50,51,43,47,0,54],
[50,51,40,47,49,58,47,46,47,46,0]])



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
result = np.append(np.array([11, 100, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,67,62,59,56,61,53,46,62],
[41,0,34,49,47,48,51,51,39,42,45],
[50,66,0,58,53,54,64,57,51,53,54],
[33,51,42,0,53,53,56,59,45,40,46],
[38,53,47,47,0,55,50,49,45,44,48],
[41,52,46,47,45,0,49,46,52,43,50],
[44,49,36,44,50,51,0,59,49,37,56],
[39,49,43,41,51,54,41,0,47,43,47],
[47,61,49,55,55,48,51,53,0,44,53],
[54,58,47,60,56,57,63,57,56,0,53],
[38,55,46,54,52,50,44,53,47,47,0]])



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
result = np.append(np.array([11, 100, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,52,55,49,56,51,46,49,50,52],
[43,0,50,51,55,58,53,49,56,49,58],
[48,50,0,60,51,54,55,54,52,53,55],
[45,49,40,0,42,54,48,38,49,45,50],
[51,45,49,58,0,52,51,44,46,45,54],
[44,42,46,46,48,0,46,49,48,51,50],
[49,47,45,52,49,54,0,47,48,52,57],
[54,51,46,62,56,51,53,0,58,47,59],
[51,44,48,51,54,52,52,42,0,48,52],
[50,51,47,55,55,49,48,53,52,0,49],
[48,42,45,50,46,50,43,41,48,51,0]])



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
result = np.append(np.array([11, 100, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,43,36,50,48,41,52,49,48,47],
[51,0,49,45,56,48,41,58,41,52,49],
[57,51,0,54,55,54,55,55,50,54,49],
[64,55,46,0,51,54,48,53,50,61,50],
[50,44,45,49,0,52,45,52,44,53,52],
[52,52,46,46,48,0,42,55,47,55,45],
[59,59,45,52,55,58,0,55,48,56,53],
[48,42,45,47,48,45,45,0,41,50,41],
[51,59,50,50,56,53,52,59,0,49,58],
[52,48,46,39,47,45,44,50,51,0,49],
[53,51,51,50,48,55,47,59,42,51,0]])



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
result = np.append(np.array([11, 100, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,58,56,51,49,52,51,49,54,49],
[41,0,46,46,43,49,43,43,38,44,45],
[42,54,0,53,45,49,41,46,49,52,43],
[44,54,47,0,35,48,43,44,46,38,44],
[49,57,55,65,0,56,48,51,56,49,48],
[51,51,51,52,44,0,47,47,47,50,52],
[48,57,59,57,52,53,0,44,47,57,51],
[49,57,54,56,49,53,56,0,51,50,50],
[51,62,51,54,44,53,53,49,0,48,50],
[46,56,48,62,51,50,43,50,52,0,51],
[51,55,57,56,52,48,49,50,50,49,0]])



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
result = np.append(np.array([11, 100, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,42,57,40,52,54,58,52,46,48],
[49,0,43,59,44,52,51,57,53,52,52],
[58,57,0,67,50,63,56,63,67,52,56],
[43,41,33,0,29,39,37,55,45,40,31],
[60,56,50,71,0,54,51,61,58,55,50],
[48,48,37,61,46,0,52,60,55,41,44],
[46,49,44,63,49,48,0,56,53,49,48],
[42,43,37,45,39,40,44,0,42,46,44],
[48,47,33,55,42,45,47,58,0,40,43],
[54,48,48,60,45,59,51,54,60,0,49],
[52,48,44,69,50,56,52,56,57,51,0]])



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
result = np.append(np.array([11, 100, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,77,68,61,53,52,58,50,66,68],
[49,0,57,51,57,49,49,61,59,52,73],
[23,43,0,44,44,40,22,39,26,49,54],
[32,49,56,0,56,63,40,69,50,52,63],
[39,43,56,44,0,54,47,53,48,57,61],
[47,51,60,37,46,0,30,61,46,40,64],
[48,51,78,60,53,70,0,59,42,59,66],
[42,39,61,31,47,39,41,0,31,49,60],
[50,41,74,50,52,54,58,69,0,69,86],
[34,48,51,48,43,60,41,51,31,0,46],
[32,27,46,37,39,36,34,40,14,54,0]])



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
result = np.append(np.array([11, 100, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,45,53,29,43,38,51,42,44,44],
[61,0,50,65,51,50,55,67,57,59,59],
[55,50,0,56,42,57,52,63,53,52,55],
[47,35,44,0,32,46,36,56,38,41,45],
[71,49,58,68,0,44,53,58,59,65,61],
[57,50,43,54,56,0,42,58,52,53,57],
[62,45,48,64,47,58,0,65,67,57,61],
[49,33,37,44,42,42,35,0,44,49,62],
[58,43,47,62,41,48,33,56,0,57,47],
[56,41,48,59,35,47,43,51,43,0,45],
[56,41,45,55,39,43,39,38,53,55,0]])



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
result = np.append(np.array([11, 100, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,48,58,60,50,60,53,51,45,56],
[52,0,55,55,57,41,58,56,58,46,58],
[52,45,0,50,55,40,49,53,52,42,47],
[42,45,50,0,56,47,54,52,56,47,45],
[40,43,45,44,0,36,48,48,50,46,45],
[50,59,60,53,64,0,57,53,65,53,53],
[40,42,51,46,52,43,0,47,47,41,49],
[47,44,47,48,52,47,53,0,50,45,51],
[49,42,48,44,50,35,53,50,0,49,50],
[55,54,58,53,54,47,59,55,51,0,55],
[44,42,53,55,55,47,51,49,50,45,0]])



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
result = np.append(np.array([11, 100, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,41,47,53,55,46,48,57,55],
[49,0,48,42,44,48,48,48,41,50,43],
[46,52,0,41,52,53,53,50,46,48,46],
[59,58,59,0,52,56,63,58,50,49,52],
[53,56,48,48,0,56,52,48,44,51,45],
[47,52,47,44,44,0,49,44,42,43,42],
[45,52,47,37,48,51,0,47,46,47,40],
[54,52,50,42,52,56,53,0,47,45,51],
[52,59,54,50,56,58,54,53,0,50,41],
[43,50,52,51,49,57,53,55,50,0,48],
[45,57,54,48,55,58,60,49,59,52,0]])



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
result = np.append(np.array([11, 100, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,60,43,59,51,45,56,49,52,46],
[44,0,65,46,49,52,53,73,59,55,59],
[40,35,0,46,41,42,39,56,34,46,36],
[57,54,54,0,50,57,58,55,63,58,53],
[41,51,59,50,0,57,54,58,55,53,45],
[49,48,58,43,43,0,53,61,46,51,37],
[55,47,61,42,46,47,0,60,42,48,50],
[44,27,44,45,42,39,40,0,38,51,54],
[51,41,66,37,45,54,58,62,0,63,54],
[48,45,54,42,47,49,52,49,37,0,51],
[54,41,64,47,55,63,50,46,46,49,0]])



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
result = np.append(np.array([11, 100, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,50,57,44,57,55,49,46,46],
[45,0,47,44,51,47,58,56,46,46,44],
[46,53,0,44,58,54,65,62,50,51,55],
[50,56,56,0,59,53,61,55,50,50,48],
[43,49,42,41,0,47,53,51,42,37,44],
[56,53,46,47,53,0,61,58,50,43,48],
[43,42,35,39,47,39,0,45,45,40,36],
[45,44,38,45,49,42,55,0,45,41,44],
[51,54,50,50,58,50,55,55,0,51,45],
[54,54,49,50,63,57,60,59,49,0,53],
[54,56,45,52,56,52,64,56,55,47,0]])



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
result = np.append(np.array([11, 100, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,33,61,27,38,38,63,54,43,55],
[49,0,36,67,35,35,40,31,37,30,54],
[67,64,0,58,76,45,37,51,59,38,69],
[39,33,42,0,21,21,24,32,24,29,34],
[73,65,24,79,0,61,43,60,52,39,78],
[62,65,55,79,39,0,52,68,33,51,54],
[62,60,63,76,57,48,0,58,60,62,57],
[37,69,49,68,40,32,42,0,34,34,46],
[46,63,41,76,48,67,40,66,0,44,58],
[57,70,62,71,61,49,38,66,56,0,66],
[45,46,31,66,22,46,43,54,42,34,0]])



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
result = np.append(np.array([11, 100, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,48,51,54,52,41,47,45,52],
[47,0,50,52,43,47,46,47,44,51,53],
[47,50,0,44,50,51,48,45,47,46,46],
[52,48,56,0,48,52,49,49,47,46,58],
[49,57,50,52,0,53,48,46,45,44,54],
[46,53,49,48,47,0,41,45,47,46,49],
[48,54,52,51,52,59,0,45,47,51,53],
[59,53,55,51,54,55,55,0,51,49,57],
[53,56,53,53,55,53,53,49,0,56,53],
[55,49,54,54,56,54,49,51,44,0,51],
[48,47,54,42,46,51,47,43,47,49,0]])



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
result = np.append(np.array([11, 100, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,48,49,35,30,39,37,43,53,42],
[63,0,63,50,60,52,54,46,61,58,57],
[52,37,0,45,48,43,41,38,50,57,47],
[51,50,55,0,55,44,39,38,55,64,58],
[65,40,52,45,0,33,31,30,61,55,38],
[70,48,57,56,67,0,39,48,61,61,56],
[61,46,59,61,69,61,0,57,58,59,61],
[63,54,62,62,70,52,43,0,57,74,60],
[57,39,50,45,39,39,42,43,0,60,57],
[47,42,43,36,45,39,41,26,40,0,36],
[58,43,53,42,62,44,39,40,43,64,0]])



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
result = np.append(np.array([11, 100, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,52,65,47,46,49,53,45,55,58],
[44,0,44,48,39,43,43,61,40,49,55],
[48,56,0,50,48,42,46,55,44,57,66],
[35,52,50,0,40,45,47,48,43,57,54],
[53,61,52,60,0,47,46,57,56,50,63],
[54,57,58,55,53,0,51,56,49,61,59],
[51,57,54,53,54,49,0,62,46,61,64],
[47,39,45,52,43,44,38,0,45,49,52],
[55,60,56,57,44,51,54,55,0,57,58],
[45,51,43,43,50,39,39,51,43,0,52],
[42,45,34,46,37,41,36,48,42,48,0]])



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
result = np.append(np.array([11, 100, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,54,53,54,52,50,56,59,35,60],
[61,0,63,55,66,39,55,60,68,46,67],
[46,37,0,52,43,41,40,38,37,33,45],
[47,45,48,0,49,34,49,44,43,31,43],
[46,34,57,51,0,40,42,46,45,42,62],
[48,61,59,66,60,0,58,65,57,52,64],
[50,45,60,51,58,42,0,47,56,40,54],
[44,40,62,56,54,35,53,0,49,46,61],
[41,32,63,57,55,43,44,51,0,42,54],
[65,54,67,69,58,48,60,54,58,0,59],
[40,33,55,57,38,36,46,39,46,41,0]])



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
result = np.append(np.array([11, 100, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,63,56,58,54,58,59,46,61,57],
[47,0,47,59,53,48,61,49,51,53,53],
[37,53,0,53,52,50,61,58,49,49,56],
[44,41,47,0,50,47,53,55,45,44,35],
[42,47,48,50,0,57,50,57,46,52,44],
[46,52,50,53,43,0,46,55,42,46,47],
[42,39,39,47,50,54,0,51,42,49,52],
[41,51,42,45,43,45,49,0,47,44,51],
[54,49,51,55,54,58,58,53,0,55,58],
[39,47,51,56,48,54,51,56,45,0,47],
[43,47,44,65,56,53,48,49,42,53,0]])



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
result = np.append(np.array([11, 100, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,57,72,76,50,62,71,47,80,62],
[25,0,29,48,50,39,40,75,32,30,52],
[43,71,0,67,64,70,47,89,59,57,77],
[28,52,33,0,34,50,45,65,27,45,25],
[24,50,36,66,0,60,45,77,33,51,48],
[50,61,30,50,40,0,62,69,31,62,42],
[38,60,53,55,55,38,0,60,47,45,53],
[29,25,11,35,23,31,40,0,15,26,20],
[53,68,41,73,67,69,53,85,0,83,59],
[20,70,43,55,49,38,55,74,17,0,46],
[38,48,23,75,52,58,47,80,41,54,0]])



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
result = np.append(np.array([11, 100, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,36,48,45,42,46,43,49,44,43],
[49,0,41,44,43,46,46,37,47,47,43],
[64,59,0,57,47,53,51,51,56,58,54],
[52,56,43,0,52,51,45,48,52,47,49],
[55,57,53,48,0,56,54,50,54,55,45],
[58,54,47,49,44,0,46,50,51,53,47],
[54,54,49,55,46,54,0,52,54,57,51],
[57,63,49,52,50,50,48,0,54,54,53],
[51,53,44,48,46,49,46,46,0,51,44],
[56,53,42,53,45,47,43,46,49,0,47],
[57,57,46,51,55,53,49,47,56,53,0]])



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
result = np.append(np.array([11, 100, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,53,55,50,53,52,47,54,57,56],
[56,0,55,54,50,58,55,51,49,55,60],
[47,45,0,48,54,53,51,52,53,54,59],
[45,46,52,0,46,48,49,47,44,35,56],
[50,50,46,54,0,55,46,50,44,49,57],
[47,42,47,52,45,0,49,45,49,48,54],
[48,45,49,51,54,51,0,56,48,46,53],
[53,49,48,53,50,55,44,0,50,52,53],
[46,51,47,56,56,51,52,50,0,50,53],
[43,45,46,65,51,52,54,48,50,0,56],
[44,40,41,44,43,46,47,47,47,44,0]])



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
result = np.append(np.array([11, 100, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,53,56,47,59,51,46,49,55,61],
[33,0,40,47,42,51,33,41,37,56,51],
[47,60,0,54,58,51,42,40,55,60,58],
[44,53,46,0,54,41,35,47,57,58,54],
[53,58,42,46,0,57,38,39,51,67,45],
[41,49,49,59,43,0,43,53,55,59,49],
[49,67,58,65,62,57,0,64,60,63,65],
[54,59,60,53,61,47,36,0,53,59,58],
[51,63,45,43,49,45,40,47,0,52,63],
[45,44,40,42,33,41,37,41,48,0,49],
[39,49,42,46,55,51,35,42,37,51,0]])



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
result = np.append(np.array([11, 100, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,63,54,53,34,44,40,53,57,56],
[68,0,70,54,67,67,55,61,50,64,51],
[37,30,0,54,46,44,39,47,37,48,46],
[46,46,46,0,54,52,43,45,54,55,50],
[47,33,54,46,0,58,50,53,32,51,59],
[66,33,56,48,42,0,46,58,46,43,58],
[56,45,61,57,50,54,0,64,39,56,59],
[60,39,53,55,47,42,36,0,45,33,57],
[47,50,63,46,68,54,61,55,0,58,60],
[43,36,52,45,49,57,44,67,42,0,48],
[44,49,54,50,41,42,41,43,40,52,0]])



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
result = np.append(np.array([11, 100, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,54,44,50,53,52,74,51,56,54],
[61,0,38,47,51,52,60,63,60,55,45],
[46,62,0,60,67,66,63,75,60,71,68],
[56,53,40,0,52,65,55,88,62,63,51],
[50,49,33,48,0,50,63,85,49,72,58],
[47,48,34,35,50,0,56,82,52,51,53],
[48,40,37,45,37,44,0,64,62,51,51],
[26,37,25,12,15,18,36,0,23,19,21],
[49,40,40,38,51,48,38,77,0,69,40],
[44,45,29,37,28,49,49,81,31,0,40],
[46,55,32,49,42,47,49,79,60,60,0]])



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
result = np.append(np.array([11, 100, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,48,66,74,63,52,77,70,69,65],
[24,0,37,47,55,43,32,46,48,34,66],
[52,63,0,81,65,65,50,78,59,30,76],
[34,53,19,0,66,54,49,78,60,40,46],
[26,45,35,34,0,40,60,52,55,54,57],
[37,57,35,46,60,0,40,46,49,44,59],
[48,68,50,51,40,60,0,59,52,38,51],
[23,54,22,22,48,54,41,0,34,13,55],
[30,52,41,40,45,51,48,66,0,27,52],
[31,66,70,60,46,56,62,87,73,0,66],
[35,34,24,54,43,41,49,45,48,34,0]])



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
result = np.append(np.array([11, 100, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,48,14,64,0,30,14,64,16,50],
[52,0,84,52,100,16,66,50,64,52,86],
[52,16,0,16,50,16,52,66,50,16,16],
[86,48,84,0,100,50,100,84,64,86,86],
[36,0,50,0,0,0,50,50,48,36,36],
[100,84,84,50,100,0,66,50,64,52,100],
[70,34,48,0,50,34,0,14,34,34,34],
[86,50,34,16,50,50,86,0,50,50,50],
[36,36,50,36,52,36,66,50,0,52,52],
[84,48,84,14,64,48,66,50,48,0,48],
[50,14,84,14,64,0,66,50,48,52,0]])



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
result = np.append(np.array([11, 100, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,51,43,43,50,55,45,53,51],
[55,0,52,45,54,40,51,47,46,41,45],
[41,48,0,36,44,40,41,45,39,41,41],
[49,55,64,0,58,53,51,57,52,53,55],
[57,46,56,42,0,50,46,55,51,52,42],
[57,60,60,47,50,0,57,55,49,54,46],
[50,49,59,49,54,43,0,53,47,53,47],
[45,53,55,43,45,45,47,0,38,45,48],
[55,54,61,48,49,51,53,62,0,48,49],
[47,59,59,47,48,46,47,55,52,0,50],
[49,55,59,45,58,54,53,52,51,50,0]])



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
result = np.append(np.array([11, 100, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,59,49,45,53,66,43,43,48,55],
[59,0,61,47,52,55,50,45,52,43,53],
[41,39,0,56,59,58,53,48,57,45,60],
[51,53,44,0,56,61,57,54,57,48,59],
[55,48,41,44,0,60,50,57,49,45,51],
[47,45,42,39,40,0,47,46,40,36,40],
[34,50,47,43,50,53,0,44,55,32,47],
[57,55,52,46,43,54,56,0,60,57,62],
[57,48,43,43,51,60,45,40,0,39,61],
[52,57,55,52,55,64,68,43,61,0,55],
[45,47,40,41,49,60,53,38,39,45,0]])



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
result = np.append(np.array([11, 100, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,50,44,47,52,56,49,42,60],
[53,0,57,50,51,45,52,61,52,54,50],
[53,43,0,47,44,47,50,42,54,43,48],
[50,50,53,0,44,52,58,45,50,45,50],
[56,49,56,56,0,58,60,56,52,49,50],
[53,55,53,48,42,0,53,49,49,48,51],
[48,48,50,42,40,47,0,50,53,47,47],
[44,39,58,55,44,51,50,0,48,47,55],
[51,48,46,50,48,51,47,52,0,47,50],
[58,46,57,55,51,52,53,53,53,0,55],
[40,50,52,50,50,49,53,45,50,45,0]])



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
result = np.append(np.array([11, 100, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,46,47,53,48,48,49,46,52,46],
[50,0,41,51,48,48,54,52,56,49,42],
[54,59,0,54,56,61,59,49,57,51,52],
[53,49,46,0,50,52,54,54,49,44,48],
[47,52,44,50,0,48,60,50,56,48,51],
[52,52,39,48,52,0,51,48,45,40,44],
[52,46,41,46,40,49,0,46,45,45,47],
[51,48,51,46,50,52,54,0,57,51,49],
[54,44,43,51,44,55,55,43,0,42,48],
[48,51,49,56,52,60,55,49,58,0,46],
[54,58,48,52,49,56,53,51,52,54,0]])



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
result = np.append(np.array([11, 100, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,66,47,58,54,38,57,53,46,52],
[52,0,62,47,55,56,51,53,63,52,58],
[34,38,0,43,41,44,34,32,48,40,50],
[53,53,57,0,49,53,48,54,56,56,48],
[42,45,59,51,0,51,40,55,58,53,52],
[46,44,56,47,49,0,40,51,55,47,50],
[62,49,66,52,60,60,0,58,66,52,54],
[43,47,68,46,45,49,42,0,57,46,50],
[47,37,52,44,42,45,34,43,0,43,47],
[54,48,60,44,47,53,48,54,57,0,63],
[48,42,50,52,48,50,46,50,53,37,0]])



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
result = np.append(np.array([11, 100, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,56,49,50,64,50,51,49,46],
[47,0,46,54,54,49,50,48,44,55,39],
[48,54,0,49,56,48,49,50,46,51,42],
[44,46,51,0,45,42,53,50,40,43,38],
[51,46,44,55,0,46,53,47,40,48,39],
[50,51,52,58,54,0,53,55,47,55,46],
[36,50,51,47,47,47,0,52,41,42,40],
[50,52,50,50,53,45,48,0,42,51,46],
[49,56,54,60,60,53,59,58,0,56,50],
[51,45,49,57,52,45,58,49,44,0,44],
[54,61,58,62,61,54,60,54,50,56,0]])



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
result = np.append(np.array([11, 100, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,62,36,35,34,50,44,42,61,41],
[47,0,52,40,31,38,31,50,38,57,22],
[38,48,0,46,38,40,47,42,40,53,44],
[64,60,54,0,41,35,44,46,40,58,42],
[65,69,62,59,0,49,41,64,50,73,53],
[66,62,60,65,51,0,38,54,45,68,50],
[50,69,53,56,59,62,0,55,55,55,50],
[56,50,58,54,36,46,45,0,46,50,47],
[58,62,60,60,50,55,45,54,0,57,45],
[39,43,47,42,27,32,45,50,43,0,28],
[59,78,56,58,47,50,50,53,55,72,0]])



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
result = np.append(np.array([11, 100, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,41,40,43,54,48,49,43,36,48],
[60,0,53,50,60,60,61,57,53,53,63],
[59,47,0,51,59,59,56,56,53,59,63],
[60,50,49,0,53,52,60,49,58,53,59],
[57,40,41,47,0,50,60,50,51,43,52],
[46,40,41,48,50,0,56,41,48,48,52],
[52,39,44,40,40,44,0,46,44,49,52],
[51,43,44,51,50,59,54,0,46,47,57],
[57,47,47,42,49,52,56,54,0,57,50],
[64,47,41,47,57,52,51,53,43,0,51],
[52,37,37,41,48,48,48,43,50,49,0]])



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
result = np.append(np.array([11, 100, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,53,60,61,70,44,68,57,48,51],
[45,0,50,40,58,63,43,58,49,56,32],
[47,50,0,47,70,55,45,64,62,55,41],
[40,60,53,0,59,55,56,65,52,68,42],
[39,42,30,41,0,50,28,44,40,48,25],
[30,37,45,45,50,0,45,43,49,53,25],
[56,57,55,44,72,55,0,69,56,64,42],
[32,42,36,35,56,57,31,0,48,42,30],
[43,51,38,48,60,51,44,52,0,48,42],
[52,44,45,32,52,47,36,58,52,0,28],
[49,68,59,58,75,75,58,70,58,72,0]])



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
result = np.append(np.array([11, 100, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,59,45,50,53,54,58,62,62,53],
[39,0,55,47,37,37,47,45,48,41,46],
[41,45,0,32,36,32,38,41,42,37,36],
[55,53,68,0,61,52,51,47,63,51,57],
[50,63,64,39,0,45,49,47,46,45,52],
[47,63,68,48,55,0,55,68,55,53,49],
[46,53,62,49,51,45,0,53,68,48,54],
[42,55,59,53,53,32,47,0,58,47,49],
[38,52,58,37,54,45,32,42,0,39,46],
[38,59,63,49,55,47,52,53,61,0,53],
[47,54,64,43,48,51,46,51,54,47,0]])



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
result = np.append(np.array([11, 100, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,39,61,53,46,46,44,47,31],
[50,0,53,38,56,58,47,37,40,54,40],
[48,47,0,42,54,56,49,46,38,45,38],
[61,62,58,0,63,51,61,52,45,62,52],
[39,44,46,37,0,52,34,42,37,43,30],
[47,42,44,49,48,0,42,45,38,44,38],
[54,53,51,39,66,58,0,40,45,59,49],
[54,63,54,48,58,55,60,0,51,57,50],
[56,60,62,55,63,62,55,49,0,66,48],
[53,46,55,38,57,56,41,43,34,0,48],
[69,60,62,48,70,62,51,50,52,52,0]])



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
result = np.append(np.array([11, 100, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,31,41,50,52,46,42,44,58,52],
[61,0,47,44,57,66,63,51,52,62,66],
[69,53,0,46,55,64,61,53,63,67,57],
[59,56,54,0,61,55,61,59,48,71,62],
[50,43,45,39,0,38,69,42,41,47,47],
[48,34,36,45,62,0,50,46,53,61,56],
[54,37,39,39,31,50,0,38,43,48,44],
[58,49,47,41,58,54,62,0,55,58,68],
[56,48,37,52,59,47,57,45,0,64,45],
[42,38,33,29,53,39,52,42,36,0,46],
[48,34,43,38,53,44,56,32,55,54,0]])



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
result = np.append(np.array([11, 100, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,42,46,49,53,51,49,54,49,42],
[52,0,43,54,52,50,51,54,61,57,48],
[58,57,0,55,56,47,54,53,51,51,51],
[54,46,45,0,56,47,44,53,57,51,48],
[51,48,44,44,0,56,52,47,52,53,50],
[47,50,53,53,44,0,54,48,50,51,42],
[49,49,46,56,48,46,0,47,58,47,47],
[51,46,47,47,53,52,53,0,58,47,49],
[46,39,49,43,48,50,42,42,0,53,49],
[51,43,49,49,47,49,53,53,47,0,45],
[58,52,49,52,50,58,53,51,51,55,0]])



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
result = np.append(np.array([11, 100, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,48,75,55,63,40,54,53,47],
[45,0,56,39,67,53,36,34,40,46,54],
[46,44,0,47,71,61,46,44,53,45,50],
[52,61,53,0,65,54,48,48,58,51,69],
[25,33,29,35,0,40,20,28,27,32,33],
[45,47,39,46,60,0,53,47,42,43,40],
[37,64,54,52,80,47,0,55,43,36,46],
[60,66,56,52,72,53,45,0,55,47,55],
[46,60,47,42,73,58,57,45,0,39,54],
[47,54,55,49,68,57,64,53,61,0,60],
[53,46,50,31,67,60,54,45,46,40,0]])



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
result = np.append(np.array([11, 100, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,46,52,62,61,52,63,51,65,47],
[47,0,33,41,44,61,44,49,39,48,42],
[54,67,0,51,60,69,51,64,61,64,50],
[48,59,49,0,60,67,45,60,60,60,51],
[38,56,40,40,0,60,37,50,51,41,41],
[39,39,31,33,40,0,32,49,32,47,47],
[48,56,49,55,63,68,0,66,52,55,55],
[37,51,36,40,50,51,34,0,54,38,40],
[49,61,39,40,49,68,48,46,0,49,45],
[35,52,36,40,59,53,45,62,51,0,47],
[53,58,50,49,59,53,45,60,55,53,0]])



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
result = np.append(np.array([11, 100, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,39,58,36,41,51,53,72,48,41],
[63,0,57,68,51,69,65,41,77,66,59],
[61,43,0,55,13,45,50,53,70,42,42],
[42,32,45,0,29,50,41,35,66,42,52],
[64,49,87,71,0,59,59,60,80,62,70],
[59,31,55,50,41,0,57,47,59,57,55],
[49,35,50,59,41,43,0,41,72,45,52],
[47,59,47,65,40,53,59,0,59,43,48],
[28,23,30,34,20,41,28,41,0,28,30],
[52,34,58,58,38,43,55,57,72,0,46],
[59,41,58,48,30,45,48,52,70,54,0]])



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
result = np.append(np.array([11, 100, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,45,39,44,48,42,47,47,49],
[54,0,63,51,47,56,62,60,50,54,54],
[50,37,0,49,44,41,56,51,50,51,56],
[55,49,51,0,48,49,54,56,49,57,49],
[61,53,56,52,0,60,64,55,48,63,57],
[56,44,59,51,40,0,52,54,53,52,51],
[52,38,44,46,36,48,0,45,36,41,47],
[58,40,49,44,45,46,55,0,47,49,44],
[53,50,50,51,52,47,64,53,0,54,54],
[53,46,49,43,37,48,59,51,46,0,42],
[51,46,44,51,43,49,53,56,46,58,0]])



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
result = np.append(np.array([11, 100, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,61,52,57,48,61,67,59,57,56],
[42,0,56,47,62,45,50,56,50,49,43],
[39,44,0,43,43,38,44,54,48,52,43],
[48,53,57,0,51,46,44,57,45,47,46],
[43,38,57,49,0,43,46,53,49,49,47],
[52,55,62,54,57,0,50,64,59,52,52],
[39,50,56,56,54,50,0,66,51,60,53],
[33,44,46,43,47,36,34,0,40,38,46],
[41,50,52,55,51,41,49,60,0,55,55],
[43,51,48,53,51,48,40,62,45,0,51],
[44,57,57,54,53,48,47,54,45,49,0]])



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
result = np.append(np.array([11, 100, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,38,43,38,37,49,43,41,45,28],
[63,0,49,37,45,45,53,43,51,46,45],
[62,51,0,52,51,49,64,54,45,47,38],
[57,63,48,0,51,60,66,54,50,59,51],
[62,55,49,49,0,59,70,55,56,56,49],
[63,55,51,40,41,0,55,45,47,45,41],
[51,47,36,34,30,45,0,43,41,36,30],
[57,57,46,46,45,55,57,0,49,54,41],
[59,49,55,50,44,53,59,51,0,50,40],
[55,54,53,41,44,55,64,46,50,0,43],
[72,55,62,49,51,59,70,59,60,57,0]])



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
result = np.append(np.array([11, 100, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,54,50,59,67,46,67,37,40,55],
[43,0,49,44,46,55,48,55,32,37,50],
[46,51,0,49,64,62,47,65,40,29,53],
[50,56,51,0,62,56,54,67,45,54,45],
[41,54,36,38,0,38,44,63,37,43,50],
[33,45,38,44,62,0,35,54,41,31,41],
[54,52,53,46,56,65,0,65,50,50,60],
[33,45,35,33,37,46,35,0,45,39,41],
[63,68,60,55,63,59,50,55,0,64,49],
[60,63,71,46,57,69,50,61,36,0,60],
[45,50,47,55,50,59,40,59,51,40,0]])



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
result = np.append(np.array([11, 100, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,56,51,58,52,57,49,52,51,51],
[51,0,48,53,53,67,73,43,50,43,48],
[44,52,0,54,51,61,60,53,54,45,54],
[49,47,46,0,40,54,58,44,42,48,52],
[42,47,49,60,0,67,62,57,44,46,55],
[48,33,39,46,33,0,55,51,43,49,39],
[43,27,40,42,38,45,0,38,41,40,34],
[51,57,47,56,43,49,62,0,49,47,50],
[48,50,46,58,56,57,59,51,0,51,46],
[49,57,55,52,54,51,60,53,49,0,43],
[49,52,46,48,45,61,66,50,54,57,0]])



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
result = np.append(np.array([11, 100, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,35,40,48,32,47,61,42,44,52],
[61,0,52,47,72,51,39,44,45,56,46],
[65,48,0,42,40,58,43,48,52,52,45],
[60,53,58,0,53,56,59,66,50,55,50],
[52,28,60,47,0,47,54,48,49,47,33],
[68,49,42,44,53,0,58,58,51,68,61],
[53,61,57,41,46,42,0,49,45,46,45],
[39,56,52,34,52,42,51,0,49,46,38],
[58,55,48,50,51,49,55,51,0,61,49],
[56,44,48,45,53,32,54,54,39,0,51],
[48,54,55,50,67,39,55,62,51,49,0]])



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
result = np.append(np.array([11, 100, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,49,56,49,59,63,51,61,48,69],
[55,0,50,57,41,49,57,52,49,41,51],
[51,50,0,57,47,50,58,45,47,43,58],
[44,43,43,0,45,42,56,48,49,36,59],
[51,59,53,55,0,54,53,49,44,50,63],
[41,51,50,58,46,0,51,46,42,43,55],
[37,43,42,44,47,49,0,56,52,43,57],
[49,48,55,52,51,54,44,0,51,41,56],
[39,51,53,51,56,58,48,49,0,53,58],
[52,59,57,64,50,57,57,59,47,0,61],
[31,49,42,41,37,45,43,44,42,39,0]])



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
result = np.append(np.array([11, 100, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,34,53,37,36,41,51,30,47,40],
[51,0,54,50,40,44,47,39,34,44,43],
[66,46,0,45,50,59,51,50,47,46,58],
[47,50,55,0,39,37,48,42,33,44,41],
[63,60,50,61,0,48,52,58,45,64,52],
[64,56,41,63,52,0,53,44,40,49,54],
[59,53,49,52,48,47,0,55,45,57,46],
[49,61,50,58,42,56,45,0,36,43,45],
[70,66,53,67,55,60,55,64,0,62,48],
[53,56,54,56,36,51,43,57,38,0,38],
[60,57,42,59,48,46,54,55,52,62,0]])



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
result = np.append(np.array([11, 100, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,49,42,53,41,51,33,56,54],
[54,0,56,61,46,56,56,61,49,54,48],
[49,44,0,41,43,44,45,54,43,50,44],
[51,39,59,0,33,42,45,49,54,52,41],
[58,54,57,67,0,54,49,55,54,60,53],
[47,44,56,58,46,0,53,55,54,50,45],
[59,44,55,55,51,47,0,48,49,53,43],
[49,39,46,51,45,45,52,0,48,51,43],
[67,51,57,46,46,46,51,52,0,55,45],
[44,46,50,48,40,50,47,49,45,0,44],
[46,52,56,59,47,55,57,57,55,56,0]])



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
result = np.append(np.array([11, 100, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,49,52,52,41,54,52,44,55],
[50,0,40,57,48,49,46,45,47,38,52],
[51,60,0,57,59,53,53,59,47,48,59],
[51,43,43,0,48,49,47,58,40,43,59],
[48,52,41,52,0,51,42,51,48,42,62],
[48,51,47,51,49,0,38,47,47,46,56],
[59,54,47,53,58,62,0,55,56,48,62],
[46,55,41,42,49,53,45,0,54,53,58],
[48,53,53,60,52,53,44,46,0,45,62],
[56,62,52,57,58,54,52,47,55,0,55],
[45,48,41,41,38,44,38,42,38,45,0]])



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
result = np.append(np.array([11, 100, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,78,48,92,86,52,56,100,92,86],
[34,0,78,48,78,78,78,34,78,92,78],
[22,22,0,48,92,100,8,56,100,100,66],
[52,52,52,0,52,86,52,42,86,52,52],
[8,22,8,48,0,42,8,42,42,100,8],
[14,22,0,14,58,0,8,48,92,58,8],
[48,22,92,48,92,92,0,48,92,92,100],
[44,66,44,58,58,52,52,0,52,58,52],
[0,22,0,14,58,8,8,48,0,58,8],
[8,8,0,48,0,42,8,42,42,0,8],
[14,22,34,48,92,92,0,48,92,92,0]])



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
result = np.append(np.array([11, 100, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,50,45,51,40,53,47,59,48,43],
[42,0,32,39,44,34,40,42,54,44,49],
[50,68,0,55,47,51,51,47,53,59,59],
[55,61,45,0,56,53,43,41,62,63,64],
[49,56,53,44,0,45,42,51,53,59,63],
[60,66,49,47,55,0,56,58,69,62,67],
[47,60,49,57,58,44,0,32,52,67,48],
[53,58,53,59,49,42,68,0,64,68,57],
[41,46,47,38,47,31,48,36,0,40,45],
[52,56,41,37,41,38,33,32,60,0,50],
[57,51,41,36,37,33,52,43,55,50,0]])



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
result = np.append(np.array([11, 100, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,80,62,73,73,75,73,65,91,47,80],
[20,0,0,0,29,31,27,16,18,16,25],
[38,100,0,58,49,69,58,65,76,65,67],
[27,100,42,0,80,75,80,36,53,47,91],
[27,71,51,20,0,44,51,47,51,27,80],
[25,69,31,25,56,0,49,54,60,45,69],
[27,73,42,20,49,51,0,36,49,36,67],
[35,84,35,64,53,46,64,0,46,29,64],
[9,82,24,47,49,40,51,54,0,36,49],
[53,84,35,53,73,55,64,71,64,0,84],
[20,75,33,9,20,31,33,36,51,16,0]])



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
result = np.append(np.array([11, 100, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,52,54,53,48,54,50,53,54],
[53,0,55,56,48,55,53,58,45,55,53],
[44,45,0,52,44,49,51,56,47,56,57],
[48,44,48,0,46,51,59,56,51,51,52],
[46,52,56,54,0,56,56,58,43,57,50],
[47,45,51,49,44,0,52,58,43,55,50],
[52,47,49,41,44,48,0,53,46,56,50],
[46,42,44,44,42,42,47,0,41,54,46],
[50,55,53,49,57,57,54,59,0,56,56],
[47,45,44,49,43,45,44,46,44,0,48],
[46,47,43,48,50,50,50,54,44,52,0]])



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
result = np.append(np.array([11, 100, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,41,49,43,46,45,44,45,45,40],
[48,0,34,48,42,45,38,38,45,38,45],
[59,66,0,53,55,56,57,57,59,56,48],
[51,52,47,0,49,49,50,46,45,51,53],
[57,58,45,51,0,50,53,50,52,52,52],
[54,55,44,51,50,0,52,42,45,47,40],
[55,62,43,50,47,48,0,48,42,52,40],
[56,62,43,54,50,58,52,0,49,50,43],
[55,55,41,55,48,55,58,51,0,48,54],
[55,62,44,49,48,53,48,50,52,0,51],
[60,55,52,47,48,60,60,57,46,49,0]])



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
result = np.append(np.array([11, 100, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,47,53,53,48,49,42,58,53,45],
[58,0,52,55,55,48,53,51,53,57,51],
[53,48,0,52,50,47,44,43,47,51,50],
[47,45,48,0,52,43,37,40,48,47,50],
[47,45,50,48,0,43,41,33,43,52,46],
[52,52,53,57,57,0,50,50,50,55,49],
[51,47,56,63,59,50,0,45,47,52,57],
[58,49,57,60,67,50,55,0,57,53,56],
[42,47,53,52,57,50,53,43,0,56,51],
[47,43,49,53,48,45,48,47,44,0,44],
[55,49,50,50,54,51,43,44,49,56,0]])



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
result = np.append(np.array([11, 100, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,57,45,49,51,45,51,47,54,51],
[53,0,54,51,43,55,53,48,41,56,44],
[43,46,0,38,45,46,40,40,38,48,40],
[55,49,62,0,57,50,46,57,60,58,49],
[51,57,55,43,0,47,49,49,47,63,47],
[49,45,54,50,53,0,49,41,45,58,45],
[55,47,60,54,51,51,0,45,46,51,53],
[49,52,60,43,51,59,55,0,48,62,50],
[53,59,62,40,53,55,54,52,0,68,48],
[46,44,52,42,37,42,49,38,32,0,38],
[49,56,60,51,53,55,47,50,52,62,0]])



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
result = np.append(np.array([11, 100, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,50,55,33,40,57,58,59,51,69],
[30,0,37,22,25,26,42,37,31,35,66],
[50,63,0,42,51,26,52,46,50,36,48],
[45,78,58,0,52,53,40,38,49,45,58],
[67,75,49,48,0,49,63,58,63,49,59],
[60,74,74,47,51,0,57,50,68,70,81],
[43,58,48,60,37,43,0,57,62,57,49],
[42,63,54,62,42,50,43,0,64,63,74],
[41,69,50,51,37,32,38,36,0,63,48],
[49,65,64,55,51,30,43,37,37,0,58],
[31,34,52,42,41,19,51,26,52,42,0]])



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
result = np.append(np.array([11, 100, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,54,46,50,55,52,51,46,47,42],
[43,0,45,42,46,53,42,53,46,46,41],
[46,55,0,45,47,51,45,54,49,51,44],
[54,58,55,0,50,57,48,56,54,44,53],
[50,54,53,50,0,60,53,46,52,44,39],
[45,47,49,43,40,0,39,52,47,47,44],
[48,58,55,52,47,61,0,49,53,56,45],
[49,47,46,44,54,48,51,0,54,42,40],
[54,54,51,46,48,53,47,46,0,42,44],
[53,54,49,56,56,53,44,58,58,0,48],
[58,59,56,47,61,56,55,60,56,52,0]])



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
result = np.append(np.array([11, 100, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,51,47,55,42,40,41,50,43],
[50,0,42,46,46,49,46,46,39,41,37],
[57,58,0,55,44,57,46,52,47,48,45],
[49,54,45,0,34,64,47,44,39,43,49],
[53,54,56,66,0,59,57,48,53,55,52],
[45,51,43,36,41,0,49,43,40,39,41],
[58,54,54,53,43,51,0,46,43,47,51],
[60,54,48,56,52,57,54,0,45,45,48],
[59,61,53,61,47,60,57,55,0,58,54],
[50,59,52,57,45,61,53,55,42,0,50],
[57,63,55,51,48,59,49,52,46,50,0]])



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
result = np.append(np.array([11, 100, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,45,40,34,51,46,32,37,50,39],
[66,0,47,62,59,68,50,51,68,66,58],
[55,53,0,66,48,58,63,48,55,62,45],
[60,38,34,0,44,64,38,23,56,48,52],
[66,41,52,56,0,56,59,36,59,62,58],
[49,32,42,36,44,0,42,42,49,41,40],
[54,50,37,62,41,58,0,31,54,59,48],
[68,49,52,77,64,58,69,0,55,58,49],
[63,32,45,44,41,51,46,45,0,40,42],
[50,34,38,52,38,59,41,42,60,0,39],
[61,42,55,48,42,60,52,51,58,61,0]])



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
result = np.append(np.array([11, 100, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,50,50,50,55,54,51,51,59,56],
[36,0,43,33,33,35,41,46,24,37,44],
[50,57,0,52,44,56,51,50,39,49,53],
[50,67,48,0,48,52,56,49,45,45,50],
[50,67,56,52,0,55,66,62,51,46,61],
[45,65,44,48,45,0,53,53,43,52,48],
[46,59,49,44,34,47,0,52,31,42,51],
[49,54,50,51,38,47,48,0,47,52,56],
[49,76,61,55,49,57,69,53,0,59,62],
[41,63,51,55,54,48,58,48,41,0,51],
[44,56,47,50,39,52,49,44,38,49,0]])



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
result = np.append(np.array([11, 100, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,54,43,48,57,48,46,47,54,57],
[44,0,57,42,56,60,44,49,50,52,52],
[46,43,0,38,46,57,46,40,44,46,57],
[57,58,62,0,51,56,52,45,49,56,50],
[52,44,54,49,0,66,46,45,50,50,63],
[43,40,43,44,34,0,41,41,45,42,41],
[52,56,54,48,54,59,0,55,53,57,57],
[54,51,60,55,55,59,45,0,54,54,61],
[53,50,56,51,50,55,47,46,0,54,54],
[46,48,54,44,50,58,43,46,46,0,55],
[43,48,43,50,37,59,43,39,46,45,0]])



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
result = np.append(np.array([11, 100, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,59,55,56,52,55,49,53,50,54],
[56,0,63,67,52,55,57,49,52,50,62],
[41,37,0,51,42,43,48,36,46,42,48],
[45,33,49,0,39,40,49,39,45,35,49],
[44,48,58,61,0,57,54,53,61,48,52],
[48,45,57,60,43,0,56,45,45,50,44],
[45,43,52,51,46,44,0,43,53,39,40],
[51,51,64,61,47,55,57,0,46,47,58],
[47,48,54,55,39,55,47,54,0,39,55],
[50,50,58,65,52,50,61,53,61,0,57],
[46,38,52,51,48,56,60,42,45,43,0]])



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
result = np.append(np.array([11, 100, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,77,36,75,66,63,59,53,74,46],
[60,0,74,60,71,66,52,49,56,74,36],
[23,26,0,39,57,66,38,39,53,15,38],
[64,40,61,0,57,56,57,65,55,56,28],
[25,29,43,43,0,42,29,35,29,43,29],
[34,34,34,44,58,0,40,34,58,41,58],
[37,48,62,43,71,60,0,47,55,33,40],
[41,51,61,35,65,66,53,0,60,56,36],
[47,44,47,45,71,42,45,40,0,42,28],
[26,26,85,44,57,59,67,44,58,0,50],
[54,64,62,72,71,42,60,64,72,50,0]])



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
result = np.append(np.array([11, 100, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,50,57,46,49,49,43,48,51,50],
[46,0,43,47,47,43,54,42,50,46,49],
[50,57,0,53,49,45,50,49,41,54,51],
[43,53,47,0,51,52,50,45,48,45,50],
[54,53,51,49,0,51,60,48,50,53,58],
[51,57,55,48,49,0,56,53,45,50,46],
[51,46,50,50,40,44,0,47,41,51,48],
[57,58,51,55,52,47,53,0,49,55,57],
[52,50,59,52,50,55,59,51,0,55,54],
[49,54,46,55,47,50,49,45,45,0,49],
[50,51,49,50,42,54,52,43,46,51,0]])



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
result = np.append(np.array([11, 100, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,41,49,49,64,48,52,70,58,64],
[52,0,41,58,54,45,53,57,63,61,70],
[59,59,0,63,54,45,51,49,83,66,76],
[51,42,37,0,52,37,51,53,66,73,52],
[51,46,46,48,0,39,39,52,69,62,65],
[36,55,55,63,61,0,52,58,71,63,61],
[52,47,49,49,61,48,0,71,59,64,60],
[48,43,51,47,48,42,29,0,60,38,63],
[30,37,17,34,31,29,41,40,0,46,42],
[42,39,34,27,38,37,36,62,54,0,53],
[36,30,24,48,35,39,40,37,58,47,0]])



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
result = np.append(np.array([11, 100, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,42,41,49,38,53,46,43,51,42],
[60,0,50,51,56,54,51,51,50,57,51],
[58,50,0,56,56,53,57,49,52,63,56],
[59,49,44,0,50,51,57,58,54,53,57],
[51,44,44,50,0,38,52,48,57,50,47],
[62,46,47,49,62,0,56,52,51,60,54],
[47,49,43,43,48,44,0,37,51,50,41],
[54,49,51,42,52,48,63,0,54,54,55],
[57,50,48,46,43,49,49,46,0,60,53],
[49,43,37,47,50,40,50,46,40,0,46],
[58,49,44,43,53,46,59,45,47,54,0]])



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
result = np.append(np.array([11, 100, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,34,33,49,57,58,47,48,36,51],
[60,0,48,49,53,58,64,79,67,52,74],
[66,52,0,47,61,70,69,88,59,75,80],
[67,51,53,0,57,49,50,73,69,55,56],
[51,47,39,43,0,65,57,75,52,58,65],
[43,42,30,51,35,0,35,60,47,49,65],
[42,36,31,50,43,65,0,55,69,59,78],
[53,21,12,27,25,40,45,0,44,37,41],
[52,33,41,31,48,53,31,56,0,58,56],
[64,48,25,45,42,51,41,63,42,0,59],
[49,26,20,44,35,35,22,59,44,41,0]])



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
result = np.append(np.array([11, 100, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,40,43,46,41,44,52,47,51,46],
[38,0,39,43,42,46,40,53,48,56,38],
[60,61,0,58,58,63,61,67,50,61,51],
[57,57,42,0,49,60,48,55,55,59,45],
[54,58,42,51,0,53,45,58,58,54,45],
[59,54,37,40,47,0,44,49,50,50,40],
[56,60,39,52,55,56,0,54,56,51,47],
[48,47,33,45,42,51,46,0,45,56,34],
[53,52,50,45,42,50,44,55,0,47,48],
[49,44,39,41,46,50,49,44,53,0,36],
[54,62,49,55,55,60,53,66,52,64,0]])



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
result = np.append(np.array([11, 100, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,51,54,48,59,49,50,53,53],
[49,0,53,50,51,44,50,45,44,50,55],
[55,47,0,53,58,49,58,56,53,51,56],
[49,50,47,0,49,44,55,46,42,44,50],
[46,49,42,51,0,47,53,54,56,52,55],
[52,56,51,56,53,0,57,50,51,51,58],
[41,50,42,45,47,43,0,44,52,52,48],
[51,55,44,54,46,50,56,0,50,50,50],
[50,56,47,58,44,49,48,50,0,51,50],
[47,50,49,56,48,49,48,50,49,0,50],
[47,45,44,50,45,42,52,50,50,50,0]])



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
result = np.append(np.array([11, 100, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,68,57,58,46,48,48,49,53,50],
[40,0,51,52,54,52,56,33,52,51,57],
[32,49,0,41,52,44,45,40,36,46,28],
[43,48,59,0,59,61,58,43,46,67,46],
[42,46,48,41,0,42,45,40,41,35,46],
[54,48,56,39,58,0,35,49,39,38,34],
[52,44,55,42,55,65,0,43,38,53,42],
[52,67,60,57,60,51,57,0,49,56,50],
[51,48,64,54,59,61,62,51,0,52,46],
[47,49,54,33,65,62,47,44,48,0,45],
[50,43,72,54,54,66,58,50,54,55,0]])



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
result = np.append(np.array([11, 100, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,61,61,54,59,44,59,51,62,52],
[47,0,51,55,56,62,38,55,43,57,52],
[39,49,0,52,48,57,44,52,45,52,40],
[39,45,48,0,54,47,41,49,39,49,43],
[46,44,52,46,0,55,43,48,45,51,38],
[41,38,43,53,45,0,37,40,40,51,38],
[56,62,56,59,57,63,0,52,44,68,49],
[41,45,48,51,52,60,48,0,50,65,46],
[49,57,55,61,55,60,56,50,0,59,48],
[38,43,48,51,49,49,32,35,41,0,36],
[48,48,60,57,62,62,51,54,52,64,0]])



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
result = np.append(np.array([11, 100, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,47,35,40,43,53,39,46,38],
[49,0,45,51,46,47,42,50,47,53,46],
[55,55,0,63,54,61,50,61,52,65,48],
[53,49,37,0,41,43,43,51,47,48,43],
[65,54,46,59,0,52,42,45,47,64,38],
[60,53,39,57,48,0,44,46,46,56,46],
[57,58,50,57,58,56,0,55,58,62,57],
[47,50,39,49,55,54,45,0,37,64,43],
[61,53,48,53,53,54,42,63,0,60,47],
[54,47,35,52,36,44,38,36,40,0,31],
[62,54,52,57,62,54,43,57,53,69,0]])



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
result = np.append(np.array([11, 100, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,46,51,52,45,57,44,59,46,53],
[54,0,50,59,65,59,58,60,57,57,58],
[54,50,0,58,60,59,53,50,55,54,58],
[49,41,42,0,54,59,53,50,58,52,55],
[48,35,40,46,0,45,52,47,54,52,54],
[55,41,41,41,55,0,55,53,53,54,54],
[43,42,47,47,48,45,0,57,53,48,49],
[56,40,50,50,53,47,43,0,62,48,59],
[41,43,45,42,46,47,47,38,0,36,45],
[54,43,46,48,48,46,52,52,64,0,61],
[47,42,42,45,46,46,51,41,55,39,0]])



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
result = np.append(np.array([11, 100, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,43,45,39,37,49,49,43,53,40],
[67,0,52,54,51,48,57,61,56,57,49],
[57,48,0,46,41,40,40,48,47,52,55],
[55,46,54,0,49,40,42,52,47,59,46],
[61,49,59,51,0,43,60,61,50,64,51],
[63,52,60,60,57,0,55,57,49,61,54],
[51,43,60,58,40,45,0,65,51,48,57],
[51,39,52,48,39,43,35,0,44,44,51],
[57,44,53,53,50,51,49,56,0,55,54],
[47,43,48,41,36,39,52,56,45,0,51],
[60,51,45,54,49,46,43,49,46,49,0]])



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
result = np.append(np.array([11, 100, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,51,47,48,37,40,49,37,43,51],
[56,0,52,46,55,47,54,57,44,49,50],
[49,48,0,48,49,35,39,49,43,49,49],
[53,54,52,0,54,44,43,54,42,46,49],
[52,45,51,46,0,37,34,50,42,53,48],
[63,53,65,56,63,0,54,60,47,52,52],
[60,46,61,57,66,46,0,61,53,61,54],
[51,43,51,46,50,40,39,0,35,45,44],
[63,56,57,58,58,53,47,65,0,55,55],
[57,51,51,54,47,48,39,55,45,0,53],
[49,50,51,51,52,48,46,56,45,47,0]])



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
result = np.append(np.array([11, 100, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,57,48,67,65,40,66,76,71,55],
[55,0,41,71,54,51,37,59,70,67,44],
[43,59,0,51,37,61,59,54,61,62,54],
[52,29,49,0,52,48,38,32,55,58,54],
[33,46,63,48,0,54,50,45,57,52,47],
[35,49,39,52,46,0,40,40,71,59,66],
[60,63,41,62,50,60,0,50,68,72,41],
[34,41,46,68,55,60,50,0,52,68,65],
[24,30,39,45,43,29,32,48,0,59,23],
[29,33,38,42,48,41,28,32,41,0,42],
[45,56,46,46,53,34,59,35,77,58,0]])



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
result = np.append(np.array([11, 100, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,48,56,51,45,42,54,50,47,45],
[62,0,49,53,52,54,48,46,52,52,46],
[52,51,0,48,53,43,38,51,44,51,45],
[44,47,52,0,54,44,40,48,47,50,39],
[49,48,47,46,0,45,46,48,50,52,43],
[55,46,57,56,55,0,42,54,54,54,46],
[58,52,62,60,54,58,0,55,58,61,44],
[46,54,49,52,52,46,45,0,48,48,51],
[50,48,56,53,50,46,42,52,0,56,46],
[53,48,49,50,48,46,39,52,44,0,46],
[55,54,55,61,57,54,56,49,54,54,0]])



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
result = np.append(np.array([11, 100, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,45,48,44,50,47,42,34,45,42],
[46,0,52,48,50,47,53,47,43,47,47],
[55,48,0,49,46,45,49,47,40,43,47],
[52,52,51,0,46,45,48,45,45,44,49],
[56,50,54,54,0,52,52,48,45,47,56],
[50,53,55,55,48,0,56,49,43,46,50],
[53,47,51,52,48,44,0,48,43,43,49],
[58,53,53,55,52,51,52,0,50,49,53],
[66,57,60,55,55,57,57,50,0,54,55],
[55,53,57,56,53,54,57,51,46,0,54],
[58,53,53,51,44,50,51,47,45,46,0]])



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
result = np.append(np.array([11, 100, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,38,41,51,52,48,54,61,56,54],
[47,0,48,53,54,51,55,48,58,60,41],
[62,52,0,62,49,50,50,47,52,61,52],
[59,47,38,0,31,43,52,48,57,52,52],
[49,46,51,69,0,52,55,45,56,50,53],
[48,49,50,57,48,0,51,50,59,60,53],
[52,45,50,48,45,49,0,51,47,46,53],
[46,52,53,52,55,50,49,0,58,55,46],
[39,42,48,43,44,41,53,42,0,42,42],
[44,40,39,48,50,40,54,45,58,0,47],
[46,59,48,48,47,47,47,54,58,53,0]])



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
result = np.append(np.array([11, 100, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,47,44,46,44,56,44,70,40],
[53,0,44,43,51,45,53,48,41,57,44],
[53,56,0,66,56,50,42,52,41,75,51],
[53,57,34,0,35,50,48,45,41,66,52],
[56,49,44,65,0,46,43,51,39,73,45],
[54,55,50,50,54,0,57,53,50,70,58],
[56,47,58,52,57,43,0,55,40,59,52],
[44,52,48,55,49,47,45,0,49,64,44],
[56,59,59,59,61,50,60,51,0,70,66],
[30,43,25,34,27,30,41,36,30,0,37],
[60,56,49,48,55,42,48,56,34,63,0]])



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
result = np.append(np.array([11, 100, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,31,40,41,44,40,36,51,46,41],
[57,0,47,64,34,55,52,38,56,60,42],
[69,53,0,53,39,60,40,36,55,58,55],
[60,36,47,0,41,53,52,42,54,47,44],
[59,66,61,59,0,59,60,48,68,70,57],
[56,45,40,47,41,0,42,49,65,65,57],
[60,48,60,48,40,58,0,50,52,61,55],
[64,62,64,58,52,51,50,0,52,61,56],
[49,44,45,46,32,35,48,48,0,56,44],
[54,40,42,53,30,35,39,39,44,0,41],
[59,58,45,56,43,43,45,44,56,59,0]])



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
result = np.append(np.array([11, 100, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,25,47,42,52,60,58,47,40],
[49,0,61,44,57,60,64,72,55,54,47],
[48,39,0,41,59,42,54,54,50,49,38],
[75,56,59,0,51,44,56,67,61,46,67],
[53,43,41,49,0,22,57,48,48,31,41],
[58,40,58,56,78,0,55,84,54,59,66],
[48,36,46,44,43,45,0,57,59,48,40],
[40,28,46,33,52,16,43,0,56,40,34],
[42,45,50,39,52,46,41,44,0,60,53],
[53,46,51,54,69,41,52,60,40,0,56],
[60,53,62,33,59,34,60,66,47,44,0]])



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
result = np.append(np.array([11, 100, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,58,53,53,53,49,61,55,53,48],
[47,0,54,54,54,57,54,55,49,50,54],
[42,46,0,56,54,38,53,48,46,53,45],
[47,46,44,0,47,39,45,45,52,46,40],
[47,46,46,53,0,47,56,49,48,43,35],
[47,43,62,61,53,0,58,60,44,50,56],
[51,46,47,55,44,42,0,51,46,43,39],
[39,45,52,55,51,40,49,0,46,51,45],
[45,51,54,48,52,56,54,54,0,47,55],
[47,50,47,54,57,50,57,49,53,0,51],
[52,46,55,60,65,44,61,55,45,49,0]])



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
result = np.append(np.array([11, 100, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,43,51,41,59,47,59,51,53,50],
[47,0,48,44,43,59,41,51,56,69,52],
[57,52,0,45,44,71,47,56,54,51,54],
[49,56,55,0,52,62,51,57,56,60,53],
[59,57,56,48,0,65,47,53,60,70,50],
[41,41,29,38,35,0,37,45,42,55,40],
[53,59,53,49,53,63,0,56,67,63,50],
[41,49,44,43,47,55,44,0,58,54,47],
[49,44,46,44,40,58,33,42,0,61,51],
[47,31,49,40,30,45,37,46,39,0,39],
[50,48,46,47,50,60,50,53,49,61,0]])



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
result = np.append(np.array([11, 100, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,46,53,48,50,50,44,51,50,41],
[54,0,50,51,56,52,53,50,62,57,52],
[54,50,0,52,51,54,54,45,55,49,53],
[47,49,48,0,49,49,49,51,55,54,52],
[52,44,49,51,0,48,54,50,53,45,47],
[50,48,46,51,52,0,54,47,57,52,48],
[50,47,46,51,46,46,0,53,54,53,44],
[56,50,55,49,50,53,47,0,50,50,44],
[49,38,45,45,47,43,46,50,0,48,46],
[50,43,51,46,55,48,47,50,52,0,51],
[59,48,47,48,53,52,56,56,54,49,0]])



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
result = np.append(np.array([11, 100, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,55,48,52,47,52,53,42,46,74],
[55,0,54,49,55,57,62,64,53,41,78],
[45,46,0,39,43,55,50,56,48,50,66],
[52,51,61,0,61,66,51,64,50,45,74],
[48,45,57,39,0,58,55,55,44,43,59],
[53,43,45,34,42,0,48,55,29,43,61],
[48,38,50,49,45,52,0,62,48,43,61],
[47,36,44,36,45,45,38,0,32,34,64],
[58,47,52,50,56,71,52,68,0,43,70],
[54,59,50,55,57,57,57,66,57,0,66],
[26,22,34,26,41,39,39,36,30,34,0]])



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
result = np.append(np.array([11, 100, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,61,62,57,53,50,56,58,54,48],
[50,0,43,52,51,47,42,53,53,43,44],
[39,57,0,49,49,41,45,53,45,41,40],
[38,48,51,0,47,49,48,45,54,50,44],
[43,49,51,53,0,39,40,45,47,50,43],
[47,53,59,51,61,0,50,54,56,46,55],
[50,58,55,52,60,50,0,56,45,51,47],
[44,47,47,55,55,46,44,0,49,42,41],
[42,47,55,46,53,44,55,51,0,44,38],
[46,57,59,50,50,54,49,58,56,0,42],
[52,56,60,56,57,45,53,59,62,58,0]])



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
result = np.append(np.array([11, 100, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,55,50,52,50,51,40,46,42,64],
[54,0,43,42,48,36,53,54,43,42,59],
[45,57,0,47,47,48,59,46,41,52,59],
[50,58,53,0,61,53,51,50,50,44,57],
[48,52,53,39,0,43,61,49,52,41,53],
[50,64,52,47,57,0,55,55,51,59,61],
[49,47,41,49,39,45,0,41,41,42,56],
[60,46,54,50,51,45,59,0,45,50,63],
[54,57,59,50,48,49,59,55,0,51,62],
[58,58,48,56,59,41,58,50,49,0,53],
[36,41,41,43,47,39,44,37,38,47,0]])



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
result = np.append(np.array([11, 100, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,43,45,47,42,43,35,44,37,46],
[47,0,46,49,57,51,57,40,48,47,46],
[57,54,0,55,61,49,52,49,51,48,53],
[55,51,45,0,52,46,50,45,44,51,51],
[53,43,39,48,0,48,51,44,41,40,57],
[58,49,51,54,52,0,50,41,53,57,53],
[57,43,48,50,49,50,0,44,50,44,45],
[65,60,51,55,56,59,56,0,57,49,65],
[56,52,49,56,59,47,50,43,0,60,55],
[63,53,52,49,60,43,56,51,40,0,54],
[54,54,47,49,43,47,55,35,45,46,0]])



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
result = np.append(np.array([11, 100, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,40,49,43,47,41,50,41,54],
[56,0,55,51,56,48,57,45,55,55,61],
[54,45,0,46,48,45,52,46,54,44,55],
[60,49,54,0,53,43,55,49,53,50,60],
[51,44,52,47,0,46,57,49,50,50,64],
[57,52,55,57,54,0,58,48,55,50,54],
[53,43,48,45,43,42,0,46,52,46,54],
[59,55,54,51,51,52,54,0,51,45,61],
[50,45,46,47,50,45,48,49,0,47,52],
[59,45,56,50,50,50,54,55,53,0,57],
[46,39,45,40,36,46,46,39,48,43,0]])



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
result = np.append(np.array([11, 100, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,52,40,45,41,44,51,45,58],
[48,0,42,53,38,53,54,46,55,43,41],
[48,58,0,58,40,45,51,55,50,46,50],
[48,47,42,0,36,51,53,45,53,42,57],
[60,62,60,64,0,67,62,64,64,46,57],
[55,47,55,49,33,0,52,47,58,52,52],
[59,46,49,47,38,48,0,54,52,52,54],
[56,54,45,55,36,53,46,0,52,43,39],
[49,45,50,47,36,42,48,48,0,44,48],
[55,57,54,58,54,48,48,57,56,0,62],
[42,59,50,43,43,48,46,61,52,38,0]])



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
result = np.append(np.array([11, 100, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,47,53,53,55,53,55,40,48],
[47,0,41,43,48,43,52,48,47,37,48],
[55,59,0,51,46,58,53,52,58,50,55],
[53,57,49,0,48,51,51,47,57,47,51],
[47,52,54,52,0,51,56,57,58,51,52],
[47,57,42,49,49,0,48,37,57,52,55],
[45,48,47,49,44,52,0,61,50,51,45],
[47,52,48,53,43,63,39,0,49,53,44],
[45,53,42,43,42,43,50,51,0,49,53],
[60,63,50,53,49,48,49,47,51,0,50],
[52,52,45,49,48,45,55,56,47,50,0]])



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
result = np.append(np.array([11, 100, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,48,48,46,50,44,53,50,47,42],
[59,0,53,52,57,51,49,55,55,50,52],
[52,47,0,51,46,52,44,47,45,50,49],
[52,48,49,0,48,55,48,47,52,47,49],
[54,43,54,52,0,55,50,50,52,47,49],
[50,49,48,45,45,0,47,49,53,56,49],
[56,51,56,52,50,53,0,51,55,47,48],
[47,45,53,53,50,51,49,0,56,50,49],
[50,45,55,48,48,47,45,44,0,55,47],
[53,50,50,53,53,44,53,50,45,0,45],
[58,48,51,51,51,51,52,51,53,55,0]])



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
result = np.append(np.array([11, 100, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,66,50,53,58,47,59,43,45,43],
[50,0,52,43,51,53,41,61,47,48,46],
[34,48,0,42,40,38,29,50,33,36,27],
[50,57,58,0,51,57,53,65,46,41,53],
[47,49,60,49,0,49,58,45,50,47,49],
[42,47,62,43,51,0,44,52,45,52,50],
[53,59,71,47,42,56,0,51,48,45,53],
[41,39,50,35,55,48,49,0,37,41,34],
[57,53,67,54,50,55,52,63,0,51,50],
[55,52,64,59,53,48,55,59,49,0,60],
[57,54,73,47,51,50,47,66,50,40,0]])



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
result = np.append(np.array([11, 100, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,31,48,42,44,36,51,34,50,53],
[57,0,43,45,50,47,37,54,43,56,76],
[69,57,0,66,72,60,57,60,50,64,73],
[52,55,34,0,71,64,51,58,40,59,71],
[58,50,28,29,0,59,36,50,37,55,64],
[56,53,40,36,41,0,50,49,40,59,56],
[64,63,43,49,64,50,0,48,51,56,72],
[49,46,40,42,50,51,52,0,35,51,55],
[66,57,50,60,63,60,49,65,0,62,66],
[50,44,36,41,45,41,44,49,38,0,59],
[47,24,27,29,36,44,28,45,34,41,0]])



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
result = np.append(np.array([11, 100, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,57,49,49,54,49,49,54,51,56],
[48,0,49,44,46,55,50,52,52,49,52],
[43,51,0,50,51,57,56,49,55,55,52],
[51,56,50,0,49,54,52,52,48,45,52],
[51,54,49,51,0,60,52,49,54,55,43],
[46,45,43,46,40,0,50,46,49,45,50],
[51,50,44,48,48,50,0,45,52,49,43],
[51,48,51,48,51,54,55,0,56,53,50],
[46,48,45,52,46,51,48,44,0,46,50],
[49,51,45,55,45,55,51,47,54,0,42],
[44,48,48,48,57,50,57,50,50,58,0]])



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
result = np.append(np.array([11, 100, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,52,34,45,57,42,45,48,64],
[45,0,46,43,36,30,54,42,47,30,40],
[46,54,0,34,40,28,35,40,43,45,49],
[48,57,66,0,44,44,47,34,49,50,45],
[66,64,60,56,0,46,49,53,55,53,62],
[55,70,72,56,54,0,61,45,55,62,48],
[43,46,65,53,51,39,0,36,41,45,52],
[58,58,60,66,47,55,64,0,54,44,63],
[55,53,57,51,45,45,59,46,0,48,55],
[52,70,55,50,47,38,55,56,52,0,58],
[36,60,51,55,38,52,48,37,45,42,0]])



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
result = np.append(np.array([11, 100, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,39,35,32,60,55,61,46,42,59],
[53,0,41,56,53,45,46,42,46,38,55],
[61,59,0,46,47,51,65,62,52,61,71],
[65,44,54,0,41,66,60,57,49,44,61],
[68,47,53,59,0,63,63,58,58,62,68],
[40,55,49,34,37,0,52,49,49,45,50],
[45,54,35,40,37,48,0,43,41,49,50],
[39,58,38,43,42,51,57,0,46,45,58],
[54,54,48,51,42,51,59,54,0,58,63],
[58,62,39,56,38,55,51,55,42,0,47],
[41,45,29,39,32,50,50,42,37,53,0]])



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
result = np.append(np.array([11, 100, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,52,40,50,51,55,48,54,50,59],
[43,0,42,51,57,50,50,47,44,50,61],
[48,58,0,40,61,50,51,46,40,52,65],
[60,49,60,0,57,52,49,51,45,53,68],
[50,43,39,43,0,38,51,29,37,44,51],
[49,50,50,48,62,0,58,43,45,47,68],
[45,50,49,51,49,42,0,39,43,44,60],
[52,53,54,49,71,57,61,0,56,51,63],
[46,56,60,55,63,55,57,44,0,56,65],
[50,50,48,47,56,53,56,49,44,0,59],
[41,39,35,32,49,32,40,37,35,41,0]])



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
result = np.append(np.array([11, 100, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,40,51,51,57,47,45,50,43,48],
[56,0,47,49,60,55,46,53,53,55,57],
[60,53,0,59,54,53,50,57,56,47,52],
[49,51,41,0,52,56,43,48,54,41,52],
[49,40,46,48,0,53,41,43,46,43,47],
[43,45,47,44,47,0,41,54,49,40,44],
[53,54,50,57,59,59,0,49,60,45,50],
[55,47,43,52,57,46,51,0,51,48,48],
[50,47,44,46,54,51,40,49,0,48,44],
[57,45,53,59,57,60,55,52,52,0,52],
[52,43,48,48,53,56,50,52,56,48,0]])



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
result = np.append(np.array([11, 100, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,58,51,50,56,47,53,44,50,55],
[55,0,52,59,51,52,51,50,57,59,51],
[42,48,0,50,51,45,41,42,44,49,38],
[49,41,50,0,50,51,42,36,44,52,53],
[50,49,49,50,0,49,44,50,49,49,47],
[44,48,55,49,51,0,50,51,47,57,54],
[53,49,59,58,56,50,0,48,50,55,45],
[47,50,58,64,50,49,52,0,45,54,48],
[56,43,56,56,51,53,50,55,0,56,60],
[50,41,51,48,51,43,45,46,44,0,39],
[45,49,62,47,53,46,55,52,40,61,0]])



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
result = np.append(np.array([11, 100, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,50,51,59,56,39,46,61,56],
[48,0,54,44,30,52,44,28,42,66,49],
[54,46,0,54,44,53,54,43,46,50,47],
[50,56,46,0,41,47,47,44,50,55,60],
[49,70,56,59,0,57,51,45,57,65,73],
[41,48,47,53,43,0,43,31,47,52,53],
[44,56,46,53,49,57,0,45,45,54,58],
[61,72,57,56,55,69,55,0,49,71,72],
[54,58,54,50,43,53,55,51,0,65,62],
[39,34,50,45,35,48,46,29,35,0,42],
[44,51,53,40,27,47,42,28,38,58,0]])



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
result = np.append(np.array([11, 100, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,52,50,55,58,55,61,61,50,58],
[55,0,46,52,52,54,54,55,57,41,55],
[48,54,0,49,51,51,54,52,56,44,58],
[50,48,51,0,60,63,73,69,52,56,53],
[45,48,49,40,0,56,41,59,35,42,43],
[42,46,49,37,44,0,43,47,46,42,47],
[45,46,46,27,59,57,0,58,51,41,59],
[39,45,48,31,41,53,42,0,49,46,47],
[39,43,44,48,65,54,49,51,0,37,42],
[50,59,56,44,58,58,59,54,63,0,61],
[42,45,42,47,57,53,41,53,58,39,0]])



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
result = np.append(np.array([11, 100, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,54,55,47,45,52,53,52,52,59],
[50,0,53,51,53,53,58,56,58,58,55],
[46,47,0,49,49,51,50,47,52,45,54],
[45,49,51,0,50,50,47,49,51,50,56],
[53,47,51,50,0,50,52,52,48,53,48],
[55,47,49,50,50,0,47,53,50,46,50],
[48,42,50,53,48,53,0,50,49,46,54],
[47,44,53,51,48,47,50,0,48,41,50],
[48,42,48,49,52,50,51,52,0,56,57],
[48,42,55,50,47,54,54,59,44,0,55],
[41,45,46,44,52,50,46,50,43,45,0]])



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
result = np.append(np.array([11, 100, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,49,50,52,52,45,43,56,57],
[46,0,49,45,48,47,57,51,48,56,49],
[51,51,0,50,52,51,50,53,51,55,51],
[51,55,50,0,57,57,53,57,53,50,55],
[50,52,48,43,0,48,54,53,48,59,51],
[48,53,49,43,52,0,61,52,45,51,50],
[48,43,50,47,46,39,0,57,43,48,53],
[55,49,47,43,47,48,43,0,39,58,49],
[57,52,49,47,52,55,57,61,0,56,56],
[44,44,45,50,41,49,52,42,44,0,50],
[43,51,49,45,49,50,47,51,44,50,0]])



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
result = np.append(np.array([11, 100, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,43,49,53,45,48,44,36,43,43],
[59,0,58,60,55,54,51,57,47,46,57],
[57,42,0,56,55,59,49,64,53,51,59],
[51,40,44,0,48,51,41,48,47,44,38],
[47,45,45,52,0,43,55,52,41,38,44],
[55,46,41,49,57,0,50,54,51,41,57],
[52,49,51,59,45,50,0,54,44,47,60],
[56,43,36,52,48,46,46,0,37,48,44],
[64,53,47,53,59,49,56,63,0,51,62],
[57,54,49,56,62,59,53,52,49,0,56],
[57,43,41,62,56,43,40,56,38,44,0]])



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
result = np.append(np.array([11, 100, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,38,57,44,46,60,40,45,51,52],
[52,0,47,53,43,50,54,51,47,45,42],
[62,53,0,60,56,47,59,49,48,58,52],
[43,47,40,0,44,40,52,41,42,45,43],
[56,57,44,56,0,55,60,53,47,54,52],
[54,50,53,60,45,0,51,46,45,53,46],
[40,46,41,48,40,49,0,37,44,48,37],
[60,49,51,59,47,54,63,0,48,56,54],
[55,53,52,58,53,55,56,52,0,55,46],
[49,55,42,55,46,47,52,44,45,0,45],
[48,58,48,57,48,54,63,46,54,55,0]])



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
result = np.append(np.array([11, 100, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,35,67,54,60,71,38,55,52,47],
[43,0,63,47,56,40,44,38,25,19,40],
[65,37,0,70,74,77,66,58,55,42,70],
[33,53,30,0,39,42,36,39,51,29,28],
[46,44,26,61,0,67,47,52,62,46,34],
[40,60,23,58,33,0,30,61,33,37,23],
[29,56,34,64,53,70,0,50,55,49,34],
[62,62,42,61,48,39,50,0,55,39,55],
[45,75,45,49,38,67,45,45,0,27,50],
[48,81,58,71,54,63,51,61,73,0,56],
[53,60,30,72,66,77,66,45,50,44,0]])



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
result = np.append(np.array([11, 100, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,71,58,46,41,37,48,38,47,56],
[42,0,40,37,32,36,37,34,35,30,41],
[29,60,0,53,28,31,34,49,27,29,49],
[42,63,47,0,50,42,39,47,35,52,39],
[54,68,72,50,0,60,41,73,47,57,54],
[59,64,69,58,40,0,50,62,50,54,52],
[63,63,66,61,59,50,0,53,32,58,58],
[52,66,51,53,27,38,47,0,27,56,48],
[62,65,73,65,53,50,68,73,0,65,69],
[53,70,71,48,43,46,42,44,35,0,63],
[44,59,51,61,46,48,42,52,31,37,0]])



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
result = np.append(np.array([11, 100, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,48,49,51,59,46,43,51,51,46],
[57,0,44,50,57,60,48,56,57,57,37],
[52,56,0,52,51,54,48,46,47,52,45],
[51,50,48,0,57,59,46,46,43,54,45],
[49,43,49,43,0,62,51,39,44,41,43],
[41,40,46,41,38,0,40,32,32,43,32],
[54,52,52,54,49,60,0,51,62,48,50],
[57,44,54,54,61,68,49,0,54,43,47],
[49,43,53,57,56,68,38,46,0,60,45],
[49,43,48,46,59,57,52,57,40,0,38],
[54,63,55,55,57,68,50,53,55,62,0]])



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
result = np.append(np.array([11, 100, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,48,35,57,51,51,44,44,51,49],
[58,0,58,42,57,58,57,61,56,59,69],
[52,42,0,50,54,60,55,51,47,50,53],
[65,58,50,0,62,65,64,55,62,50,70],
[43,43,46,38,0,62,51,48,55,47,56],
[49,42,40,35,38,0,54,37,50,58,51],
[49,43,45,36,49,46,0,33,43,45,42],
[56,39,49,45,52,63,67,0,65,44,59],
[56,44,53,38,45,50,57,35,0,53,50],
[49,41,50,50,53,42,55,56,47,0,73],
[51,31,47,30,44,49,58,41,50,27,0]])



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
result = np.append(np.array([11, 100, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,51,55,48,42,49,56,49,53,50],
[47,0,45,49,42,46,41,43,47,40,42],
[49,55,0,54,49,54,54,50,48,56,51],
[45,51,46,0,49,46,50,52,41,44,41],
[52,58,51,51,0,47,48,56,53,52,49],
[58,54,46,54,53,0,50,52,55,55,49],
[51,59,46,50,52,50,0,53,53,52,50],
[44,57,50,48,44,48,47,0,54,51,43],
[51,53,52,59,47,45,47,46,0,52,47],
[47,60,44,56,48,45,48,49,48,0,44],
[50,58,49,59,51,51,50,57,53,56,0]])



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
result = np.append(np.array([11, 100, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,52,56,56,61,52,50,53,52],
[51,0,49,49,49,57,58,43,46,44,55],
[46,51,0,46,56,51,59,42,44,48,41],
[48,51,54,0,58,54,55,50,48,51,49],
[44,51,44,42,0,51,49,39,43,50,41],
[44,43,49,46,49,0,50,39,47,50,39],
[39,42,41,45,51,50,0,34,39,43,41],
[48,57,58,50,61,61,66,0,56,53,44],
[50,54,56,52,57,53,61,44,0,51,53],
[47,56,52,49,50,50,57,47,49,0,52],
[48,45,59,51,59,61,59,56,47,48,0]])



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
result = np.append(np.array([11, 100, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,45,59,40,45,44,44,55,46,54],
[52,0,60,56,44,45,45,49,57,45,46],
[55,40,0,52,41,44,48,44,50,43,53],
[41,44,48,0,33,39,42,43,49,38,34],
[60,56,59,67,0,47,49,51,64,48,55],
[55,55,56,61,53,0,44,51,62,46,53],
[56,55,52,58,51,56,0,50,56,56,52],
[56,51,56,57,49,49,50,0,66,53,56],
[45,43,50,51,36,38,44,34,0,40,43],
[54,55,57,62,52,54,44,47,60,0,57],
[46,54,47,66,45,47,48,44,57,43,0]])



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
result = np.append(np.array([11, 100, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,59,45,62,56,52,57,60,62,75],
[52,0,53,64,66,69,50,47,58,57,70],
[41,47,0,44,63,48,49,35,57,60,54],
[55,36,56,0,57,58,67,38,46,55,66],
[38,34,37,43,0,54,47,42,59,46,59],
[44,31,52,42,46,0,39,42,58,51,67],
[48,50,51,33,53,61,0,38,61,60,61],
[43,53,65,62,58,58,62,0,56,56,64],
[40,42,43,54,41,42,39,44,0,43,53],
[38,43,40,45,54,49,40,44,57,0,54],
[25,30,46,34,41,33,39,36,47,46,0]])



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
result = np.append(np.array([11, 100, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,42,53,53,52,45,61,44,34,36],
[59,0,53,55,56,50,59,64,58,59,53],
[58,47,0,53,57,51,57,65,43,64,46],
[47,45,47,0,58,48,48,65,52,65,43],
[47,44,43,42,0,46,51,61,34,50,15],
[48,50,49,52,54,0,59,68,42,55,49],
[55,41,43,52,49,41,0,54,47,45,48],
[39,36,35,35,39,32,46,0,33,27,22],
[56,42,57,48,66,58,53,67,0,52,47],
[66,41,36,35,50,45,55,73,48,0,37],
[64,47,54,57,85,51,52,78,53,63,0]])



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
result = np.append(np.array([11, 100, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,67,54,61,47,53,52,54,54],
[48,0,43,56,62,50,53,53,47,51,52],
[55,57,0,58,58,58,47,46,63,39,56],
[33,44,42,0,50,47,45,52,43,43,41],
[46,38,42,50,0,43,50,55,46,51,55],
[39,50,42,53,57,0,34,51,43,52,51],
[53,47,53,55,50,66,0,55,55,56,59],
[47,47,54,48,45,49,45,0,55,42,48],
[48,53,37,57,54,57,45,45,0,44,56],
[46,49,61,57,49,48,44,58,56,0,62],
[46,48,44,59,45,49,41,52,44,38,0]])



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
result = np.append(np.array([11, 100, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,47,57,54,51,62,48,43,35,46],
[46,0,50,34,41,55,41,24,34,17,43],
[53,50,0,50,54,46,46,39,44,33,48],
[43,66,50,0,50,52,52,40,30,28,41],
[46,59,46,50,0,47,50,42,44,35,44],
[49,45,54,48,53,0,68,34,48,34,55],
[38,59,54,48,50,32,0,39,40,30,37],
[52,76,61,60,58,66,61,0,53,33,60],
[57,66,56,70,56,52,60,47,0,57,51],
[65,83,67,72,65,66,70,67,43,0,65],
[54,57,52,59,56,45,63,40,49,35,0]])



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
result = np.append(np.array([11, 100, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,52,53,42,51,54,41,50,46],
[53,0,52,56,51,47,55,57,49,52,54],
[51,48,0,49,52,44,49,52,53,46,51],
[48,44,51,0,50,50,54,52,50,49,54],
[47,49,48,50,0,52,56,54,46,48,53],
[58,53,56,50,48,0,53,55,51,58,50],
[49,45,51,46,44,47,0,52,42,46,50],
[46,43,48,48,46,45,48,0,42,55,50],
[59,51,47,50,54,49,58,58,0,61,58],
[50,48,54,51,52,42,54,45,39,0,46],
[54,46,49,46,47,50,50,50,42,54,0]])



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
result = np.append(np.array([11, 100, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,23,36,29,40,33,33,33,29,56],
[47,0,41,47,44,43,41,38,39,50,65],
[77,59,0,50,52,50,54,53,60,53,67],
[64,53,50,0,42,44,42,38,50,40,52],
[71,56,48,58,0,49,56,50,51,74,64],
[60,57,50,56,51,0,48,51,45,42,57],
[67,59,46,58,44,52,0,53,45,59,58],
[67,62,47,62,50,49,47,0,57,64,62],
[67,61,40,50,49,55,55,43,0,53,58],
[71,50,47,60,26,58,41,36,47,0,59],
[44,35,33,48,36,43,42,38,42,41,0]])



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
result = np.append(np.array([11, 100, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,52,58,49,49,62,56,53,55],
[48,0,51,42,47,45,44,54,50,45,40],
[44,49,0,34,49,52,47,49,44,37,35],
[48,58,66,0,56,50,52,61,52,48,45],
[42,53,51,44,0,49,55,55,53,51,39],
[51,55,48,50,51,0,46,53,58,49,42],
[51,56,53,48,45,54,0,57,48,44,37],
[38,46,51,39,45,47,43,0,47,38,35],
[44,50,56,48,47,42,52,53,0,45,39],
[47,55,63,52,49,51,56,62,55,0,50],
[45,60,65,55,61,58,63,65,61,50,0]])



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
result = np.append(np.array([11, 100, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,60,58,60,58,42,54,47,56,56],
[51,0,58,53,54,64,55,52,47,51,57],
[40,42,0,38,46,48,39,49,31,43,51],
[42,47,62,0,52,69,55,55,48,48,51],
[40,46,54,48,0,65,46,54,43,50,58],
[42,36,52,31,35,0,42,44,43,45,45],
[58,45,61,45,54,58,0,67,52,53,51],
[46,48,51,45,46,56,33,0,45,47,39],
[53,53,69,52,57,57,48,55,0,54,59],
[44,49,57,52,50,55,47,53,46,0,49],
[44,43,49,49,42,55,49,61,41,51,0]])



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
result = np.append(np.array([11, 100, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,61,61,55,55,57,54,55,58,56],
[50,0,56,61,59,53,60,48,59,55,50],
[39,44,0,52,42,47,37,47,44,47,41],
[39,39,48,0,44,49,47,41,42,40,41],
[45,41,58,56,0,53,52,47,58,50,50],
[45,47,53,51,47,0,52,51,57,57,50],
[43,40,63,53,48,48,0,52,51,49,54],
[46,52,53,59,53,49,48,0,48,53,50],
[45,41,56,58,42,43,49,52,0,50,47],
[42,45,53,60,50,43,51,47,50,0,59],
[44,50,59,59,50,50,46,50,53,41,0]])



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
result = np.append(np.array([11, 100, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,48,72,56,43,59,53,62,55,67],
[29,0,52,51,22,39,40,16,38,31,24],
[52,48,0,72,45,51,45,42,57,59,46],
[28,49,28,0,32,28,22,16,34,22,29],
[44,78,55,68,0,43,66,46,55,50,55],
[57,61,49,72,57,0,53,36,50,54,46],
[41,60,55,78,34,47,0,58,67,56,48],
[47,84,58,84,54,64,42,0,53,64,40],
[38,62,43,66,45,50,33,47,0,32,43],
[45,69,41,78,50,46,44,36,68,0,52],
[33,76,54,71,45,54,52,60,57,48,0]])



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
result = np.append(np.array([11, 100, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,60,54,62,66,48,48,55,50,50],
[48,0,58,56,45,52,47,58,48,53,67],
[40,42,0,53,43,43,37,41,50,49,50],
[46,44,47,0,44,47,40,44,49,56,51],
[38,55,57,56,0,52,50,58,57,52,64],
[34,48,57,53,48,0,33,44,52,40,40],
[52,53,63,60,50,67,0,64,50,56,58],
[52,42,59,56,42,56,36,0,52,50,42],
[45,52,50,51,43,48,50,48,0,56,59],
[50,47,51,44,48,60,44,50,44,0,55],
[50,33,50,49,36,60,42,58,41,45,0]])



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
result = np.append(np.array([11, 100, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,54,24,48,59,65,78,95,78,83],
[22,0,54,28,65,52,46,83,76,100,83],
[46,46,0,46,64,52,46,52,76,76,82],
[76,72,54,0,78,35,89,83,89,100,83],
[52,35,36,22,0,52,52,41,52,52,41],
[41,48,48,65,48,0,59,48,65,95,53],
[35,54,54,11,48,41,0,59,76,83,59],
[22,17,48,17,59,52,41,0,65,94,58],
[5,24,24,11,48,35,24,35,0,65,35],
[22,0,24,0,48,5,17,6,35,0,11],
[17,17,18,17,59,47,41,42,65,89,0]])



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
result = np.append(np.array([11, 100, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,45,47,54,38,50,52,46,47,53],
[50,0,51,46,45,48,48,50,58,37,47],
[55,49,0,55,52,45,48,60,52,50,47],
[53,54,45,0,48,50,54,54,58,44,55],
[46,55,48,52,0,39,54,54,61,42,56],
[62,52,55,50,61,0,55,63,58,53,55],
[50,52,52,46,46,45,0,50,57,50,51],
[48,50,40,46,46,37,50,0,55,43,45],
[54,42,48,42,39,42,43,45,0,38,51],
[53,63,50,56,58,47,50,57,62,0,52],
[47,53,53,45,44,45,49,55,49,48,0]])



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
result = np.append(np.array([11, 100, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,63,36,52,58,51,46,58,53,46],
[39,0,53,47,56,49,49,34,44,51,41],
[37,47,0,45,46,48,44,56,44,57,39],
[64,53,55,0,49,66,55,53,61,66,51],
[48,44,54,51,0,61,49,56,57,54,38],
[42,51,52,34,39,0,58,42,54,46,44],
[49,51,56,45,51,42,0,64,46,40,55],
[54,66,44,47,44,58,36,0,43,43,48],
[42,56,56,39,43,46,54,57,0,53,50],
[47,49,43,34,46,54,60,57,47,0,45],
[54,59,61,49,62,56,45,52,50,55,0]])



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
result = np.append(np.array([11, 100, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,42,54,51,61,56,54,49,51],
[51,0,51,42,42,51,60,52,39,49,49],
[50,49,0,40,44,40,50,51,44,49,47],
[58,58,60,0,57,54,65,54,67,50,63],
[46,58,56,43,0,50,47,45,43,57,55],
[49,49,60,46,50,0,58,48,52,51,58],
[39,40,50,35,53,42,0,45,52,40,39],
[44,48,49,46,55,52,55,0,55,53,55],
[46,61,56,33,57,48,48,45,0,49,46],
[51,51,51,50,43,49,60,47,51,0,59],
[49,51,53,37,45,42,61,45,54,41,0]])



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
result = np.append(np.array([11, 100, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,39,35,30,38,41,31,23,37,29],
[67,0,40,60,59,46,59,39,66,44,50],
[61,60,0,64,47,44,60,47,50,65,52],
[65,40,36,0,45,52,49,40,48,34,46],
[70,41,53,55,0,41,48,39,36,41,48],
[62,54,56,48,59,0,51,50,51,55,50],
[59,41,40,51,52,49,0,60,46,56,43],
[69,61,53,60,61,50,40,0,55,40,50],
[77,34,50,52,64,49,54,45,0,41,51],
[63,56,35,66,59,45,44,60,59,0,46],
[71,50,48,54,52,50,57,50,49,54,0]])



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
result = np.append(np.array([11, 100, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,46,49,37,42,58,61,63,62],
[59,0,58,60,61,58,48,60,65,55,63],
[55,42,0,49,59,37,53,58,59,54,48],
[54,40,51,0,57,45,46,57,57,67,54],
[51,39,41,43,0,35,38,51,43,52,45],
[63,42,63,55,65,0,51,62,57,59,56],
[58,52,47,54,62,49,0,66,59,62,51],
[42,40,42,43,49,38,34,0,46,48,44],
[39,35,41,43,57,43,41,54,0,50,55],
[37,45,46,33,48,41,38,52,50,0,43],
[38,37,52,46,55,44,49,56,45,57,0]])



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
result = np.append(np.array([11, 100, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,16,0,53,38,26,43,81,69,43],
[19,0,19,0,26,38,0,16,54,0,0],
[84,81,0,0,53,38,38,69,81,69,81],
[100,100,100,0,65,38,81,81,81,81,100],
[47,74,47,35,0,12,28,28,28,47,74],
[62,62,62,62,88,0,43,43,81,62,62],
[74,100,62,19,72,57,0,62,81,62,62],
[57,84,31,19,72,57,38,0,38,57,84],
[19,46,19,19,72,19,19,62,0,19,46],
[31,100,31,19,53,38,38,43,81,0,74],
[57,100,19,0,26,38,38,16,54,26,0]])



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
result = np.append(np.array([11, 100, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,57,59,50,58,53,62,53,57,59],
[53,0,43,56,49,58,53,52,52,48,52],
[43,57,0,56,48,59,54,47,45,46,59],
[41,44,44,0,43,55,42,43,37,46,47],
[50,51,52,57,0,57,61,64,54,51,59],
[42,42,41,45,43,0,51,55,45,49,48],
[47,47,46,58,39,49,0,50,43,41,61],
[38,48,53,57,36,45,50,0,36,40,53],
[47,48,55,63,46,55,57,64,0,48,54],
[43,52,54,54,49,51,59,60,52,0,55],
[41,48,41,53,41,52,39,47,46,45,0]])



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
result = np.append(np.array([11, 100, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,58,57,52,53,53,49,57,51,54],
[58,0,55,57,53,52,45,47,58,52,58],
[42,45,0,53,51,49,54,42,52,47,44],
[43,43,47,0,52,43,45,49,50,48,43],
[48,47,49,48,0,46,39,46,52,51,51],
[47,48,51,57,54,0,50,47,55,53,52],
[47,55,46,55,61,50,0,51,55,52,53],
[51,53,58,51,54,53,49,0,66,52,54],
[43,42,48,50,48,45,45,34,0,37,45],
[49,48,53,52,49,47,48,48,63,0,53],
[46,42,56,57,49,48,47,46,55,47,0]])



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
result = np.append(np.array([11, 100, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,45,45,47,51,48,41,46,48,56],
[46,0,48,45,43,51,47,47,44,47,54],
[55,52,0,55,50,54,53,48,54,49,55],
[55,55,45,0,46,58,50,48,48,46,58],
[53,57,50,54,0,59,59,56,52,54,57],
[49,49,46,42,41,0,37,42,50,45,44],
[52,53,47,50,41,63,0,53,46,51,57],
[59,53,52,52,44,58,47,0,58,55,55],
[54,56,46,52,48,50,54,42,0,54,53],
[52,53,51,54,46,55,49,45,46,0,52],
[44,46,45,42,43,56,43,45,47,48,0]])



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
result = np.append(np.array([11, 100, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,51,50,56,44,51,46,56,43],
[54,0,53,53,55,61,56,57,44,66,51],
[50,47,0,57,62,56,58,59,47,56,57],
[49,47,43,0,47,51,37,54,35,55,43],
[50,45,38,53,0,45,48,49,52,50,40],
[44,39,44,49,55,0,51,51,44,51,42],
[56,44,42,63,52,49,0,50,45,55,58],
[49,43,41,46,51,49,50,0,52,50,50],
[54,56,53,65,48,56,55,48,0,64,49],
[44,34,44,45,50,49,45,50,36,0,46],
[57,49,43,57,60,58,42,50,51,54,0]])



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
result = np.append(np.array([11, 100, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,54,48,49,44,55,48,57,48,59],
[48,0,46,47,51,45,47,50,56,53,50],
[46,54,0,39,39,49,35,51,46,48,52],
[52,53,61,0,45,47,51,49,58,54,59],
[51,49,61,55,0,50,50,55,56,53,48],
[56,55,51,53,50,0,53,52,63,57,55],
[45,53,65,49,50,47,0,56,49,51,57],
[52,50,49,51,45,48,44,0,55,54,49],
[43,44,54,42,44,37,51,45,0,50,50],
[52,47,52,46,47,43,49,46,50,0,51],
[41,50,48,41,52,45,43,51,50,49,0]])



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
result = np.append(np.array([11, 100, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,62,46,56,53,63,56,63,56,61],
[46,0,53,58,54,53,55,50,53,57,59],
[38,47,0,45,56,48,61,53,40,56,63],
[54,42,55,0,42,58,67,55,61,63,59],
[44,46,44,58,0,58,52,45,56,67,57],
[47,47,52,42,42,0,56,56,47,53,55],
[37,45,39,33,48,44,0,43,50,51,47],
[44,50,47,45,55,44,57,0,50,56,53],
[37,47,60,39,44,53,50,50,0,61,50],
[44,43,44,37,33,47,49,44,39,0,48],
[39,41,37,41,43,45,53,47,50,52,0]])



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
result = np.append(np.array([11, 100, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,54,62,69,62,75,63,33,71],
[48,0,33,31,66,44,42,67,56,29,53],
[54,67,0,66,56,69,44,76,62,45,61],
[46,69,34,0,67,56,53,56,55,53,64],
[38,34,44,33,0,49,32,67,37,32,71],
[31,56,31,44,51,0,26,51,54,31,56],
[38,58,56,47,68,74,0,78,50,40,67],
[25,33,24,44,33,49,22,0,44,16,28],
[37,44,38,45,63,46,50,56,0,39,42],
[67,71,55,47,68,69,60,84,61,0,80],
[29,47,39,36,29,44,33,72,58,20,0]])



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
result = np.append(np.array([11, 100, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,39,54,51,52,59,61,47,44,46],
[39,0,51,47,38,39,57,57,46,39,54],
[61,49,0,32,50,38,49,66,46,49,40],
[46,53,68,0,43,49,55,55,49,56,41],
[49,62,50,57,0,54,54,66,60,43,45],
[48,61,62,51,46,0,66,60,55,54,64],
[41,43,51,45,46,34,0,41,51,45,59],
[39,43,34,45,34,40,59,0,45,44,47],
[53,54,54,51,40,45,49,55,0,59,49],
[56,61,51,44,57,46,55,56,41,0,49],
[54,46,60,59,55,36,41,53,51,51,0]])



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
result = np.append(np.array([11, 100, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,60,56,51,44,56,46,60,63],
[45,0,49,56,49,54,40,53,47,55,56],
[46,51,0,63,50,46,40,50,43,56,55],
[40,44,37,0,46,35,32,43,40,47,50],
[44,51,50,54,0,44,49,48,48,54,57],
[49,46,54,65,56,0,48,59,53,55,57],
[56,60,60,68,51,52,0,49,57,52,67],
[44,47,50,57,52,41,51,0,46,50,59],
[54,53,57,60,52,47,43,54,0,60,55],
[40,45,44,53,46,45,48,50,40,0,59],
[37,44,45,50,43,43,33,41,45,41,0]])



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
result = np.append(np.array([11, 100, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,43,49,53,48,53,39,50,45,50],
[51,0,54,46,54,47,51,55,48,44,48],
[57,46,0,48,51,60,55,58,56,53,62],
[51,54,52,0,52,45,61,57,57,56,61],
[47,46,49,48,0,53,59,54,58,50,46],
[52,53,40,55,47,0,52,56,46,56,49],
[47,49,45,39,41,48,0,43,46,46,46],
[61,45,42,43,46,44,57,0,49,46,53],
[50,52,44,43,42,54,54,51,0,52,58],
[55,56,47,44,50,44,54,54,48,0,56],
[50,52,38,39,54,51,54,47,42,44,0]])



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
result = np.append(np.array([11, 100, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,49,51,54,43,50,42,50,44],
[44,0,44,51,41,54,42,44,48,50,38],
[54,56,0,53,54,53,44,55,45,56,42],
[51,49,47,0,53,59,59,52,51,60,51],
[49,59,46,47,0,51,37,46,50,46,42],
[46,46,47,41,49,0,46,47,39,44,39],
[57,58,56,41,63,54,0,52,49,60,51],
[50,56,45,48,54,53,48,0,44,43,49],
[58,52,55,49,50,61,51,56,0,55,41],
[50,50,44,40,54,56,40,57,45,0,40],
[56,62,58,49,58,61,49,51,59,60,0]])



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
result = np.append(np.array([11, 100, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,70,62,62,60,51,50,49,55,61],
[50,0,55,61,63,55,50,51,52,51,62],
[30,45,0,49,49,45,42,46,48,41,48],
[38,39,51,0,42,52,48,40,40,42,48],
[38,37,51,58,0,50,54,38,48,43,51],
[40,45,55,48,50,0,55,46,56,43,64],
[49,50,58,52,46,45,0,44,54,48,55],
[50,49,54,60,62,54,56,0,44,57,55],
[51,48,52,60,52,44,46,56,0,48,60],
[45,49,59,58,57,57,52,43,52,0,56],
[39,38,52,52,49,36,45,45,40,44,0]])



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
result = np.append(np.array([11, 100, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,54,55,45,48,52,59,49,61,47],
[46,0,57,46,47,48,45,53,45,62,52],
[46,43,0,50,37,36,40,48,49,54,50],
[45,54,50,0,50,44,45,59,43,52,60],
[55,53,63,50,0,51,47,58,52,51,55],
[52,52,64,56,49,0,49,51,61,57,53],
[48,55,60,55,53,51,0,56,52,66,61],
[41,47,52,41,42,49,44,0,48,52,58],
[51,55,51,57,48,39,48,52,0,60,49],
[39,38,46,48,49,43,34,48,40,0,47],
[53,48,50,40,45,47,39,42,51,53,0]])



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
result = np.append(np.array([11, 100, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,51,47,45,48,49,49,52,46],
[51,0,44,49,53,41,50,55,54,51,60],
[55,56,0,56,52,52,50,55,61,59,56],
[49,51,44,0,51,46,45,48,51,49,47],
[53,47,48,49,0,36,50,42,46,51,44],
[55,59,48,54,64,0,57,60,62,63,60],
[52,50,50,55,50,43,0,55,52,51,55],
[51,45,45,52,58,40,45,0,49,57,54],
[51,46,39,49,54,38,48,51,0,53,58],
[48,49,41,51,49,37,49,43,47,0,44],
[54,40,44,53,56,40,45,46,42,56,0]])



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
result = np.append(np.array([11, 100, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,36,38,48,36,36,60,32,38,38],
[70,0,42,59,60,49,60,70,51,65,43],
[64,58,0,60,63,53,54,64,68,66,50],
[62,41,40,0,57,37,30,65,33,51,46],
[52,40,37,43,0,46,58,60,46,49,54],
[64,51,47,63,54,0,55,67,57,59,42],
[64,40,46,70,42,45,0,69,53,59,49],
[40,30,36,35,40,33,31,0,44,43,46],
[68,49,32,67,54,43,47,56,0,65,53],
[62,35,34,49,51,41,41,57,35,0,40],
[62,57,50,54,46,58,51,54,47,60,0]])



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
result = np.append(np.array([11, 100, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,45,40,66,33,30,37,44,50],
[56,0,62,47,46,63,44,45,45,48,53],
[54,38,0,59,42,76,43,53,50,34,62],
[55,53,41,0,41,70,53,35,57,44,56],
[60,54,58,59,0,61,46,49,44,59,44],
[34,37,24,30,39,0,28,18,23,25,28],
[67,56,57,47,54,72,0,58,52,54,56],
[70,55,47,65,51,82,42,0,56,39,50],
[63,55,50,43,56,77,48,44,0,53,56],
[56,52,66,56,41,75,46,61,47,0,58],
[50,47,38,44,56,72,44,50,44,42,0]])



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
result = np.append(np.array([11, 100, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,76,49,88,68,67,100,22,40,71],
[33,0,50,62,65,70,48,80,2,50,53],
[24,50,0,61,65,80,32,83,32,35,65],
[51,38,39,0,81,41,38,81,2,33,71],
[12,35,35,19,0,58,17,67,2,17,38],
[32,30,20,59,42,0,30,42,22,32,32],
[33,52,68,62,83,70,0,98,14,50,73],
[0,20,17,19,33,58,2,0,2,21,23],
[78,98,68,98,98,78,86,98,0,50,98],
[60,50,65,67,83,68,50,79,50,0,62],
[29,47,35,29,62,68,27,77,2,38,0]])



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
result = np.append(np.array([11, 100, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,58,51,36,44,46,37,43,46,43],
[45,0,50,55,43,38,29,41,45,47,48],
[42,50,0,56,48,38,48,64,54,46,53],
[49,45,44,0,48,41,37,45,43,39,46],
[64,57,52,52,0,41,45,55,51,49,54],
[56,62,62,59,59,0,58,50,51,50,52],
[54,71,52,63,55,42,0,60,57,43,57],
[63,59,36,55,45,50,40,0,42,47,59],
[57,55,46,57,49,49,43,58,0,50,64],
[54,53,54,61,51,50,57,53,50,0,51],
[57,52,47,54,46,48,43,41,36,49,0]])



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
result = np.append(np.array([11, 100, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,55,34,49,54,41,36,43,45,62],
[58,0,63,43,50,63,51,44,66,44,51],
[45,37,0,42,49,48,27,40,35,24,46],
[66,57,58,0,71,66,39,52,53,56,67],
[51,50,51,29,0,58,32,46,42,50,63],
[46,37,52,34,42,0,37,41,44,40,38],
[59,49,73,61,68,63,0,49,45,72,64],
[64,56,60,48,54,59,51,0,50,60,70],
[57,34,65,47,58,56,55,50,0,48,48],
[55,56,76,44,50,60,28,40,52,0,72],
[38,49,54,33,37,62,36,30,52,28,0]])



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
result = np.append(np.array([11, 100, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,48,47,49,60,48,49,41,51,46],
[42,0,42,54,55,45,62,53,52,58,57],
[52,58,0,54,61,52,54,42,43,58,58],
[53,46,46,0,58,46,53,54,48,51,54],
[51,45,39,42,0,53,49,47,48,47,49],
[40,55,48,54,47,0,51,49,45,56,49],
[52,38,46,47,51,49,0,48,49,47,59],
[51,47,58,46,53,51,52,0,43,47,46],
[59,48,57,52,52,55,51,57,0,57,59],
[49,42,42,49,53,44,53,53,43,0,45],
[54,43,42,46,51,51,41,54,41,55,0]])



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
result = np.append(np.array([11, 100, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,49,54,54,48,54,66,60,51],
[50,0,56,48,44,64,48,56,56,55,49],
[52,44,0,50,48,50,47,45,56,57,48],
[51,52,50,0,53,50,43,47,57,61,55],
[46,56,52,47,0,54,55,52,64,60,52],
[46,36,50,50,46,0,42,44,43,58,45],
[52,52,53,57,45,58,0,48,59,61,60],
[46,44,55,53,48,56,52,0,58,59,49],
[34,44,44,43,36,57,41,42,0,58,44],
[40,45,43,39,40,42,39,41,42,0,39],
[49,51,52,45,48,55,40,51,56,61,0]])



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
result = np.append(np.array([11, 100, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,36,67,31,67,12,33,47,45,76],
[53,0,41,72,36,53,53,17,60,17,53],
[64,59,0,36,59,59,31,64,47,64,40],
[33,28,64,0,47,64,0,33,47,33,64],
[69,64,41,53,0,81,36,33,83,69,64],
[33,47,41,36,19,0,0,33,47,33,28],
[88,47,69,100,64,100,0,33,88,52,69],
[67,83,36,67,67,67,67,0,83,100,48],
[53,40,53,53,17,53,12,17,0,17,53],
[55,83,36,67,31,67,48,0,83,0,48],
[24,47,60,36,36,72,31,52,47,52,0]])



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
result = np.append(np.array([11, 100, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,52,60,58,52,59,49,48,60,64],
[41,0,56,57,55,63,60,48,56,53,64],
[48,44,0,45,46,49,52,45,40,53,52],
[40,43,55,0,48,53,50,41,47,56,59],
[42,45,54,52,0,50,49,47,46,59,52],
[48,37,51,47,50,0,44,55,50,54,55],
[41,40,48,50,51,56,0,39,44,49,59],
[51,52,55,59,53,45,61,0,46,62,61],
[52,44,60,53,54,50,56,54,0,58,54],
[40,47,47,44,41,46,51,38,42,0,53],
[36,36,48,41,48,45,41,39,46,47,0]])



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
result = np.append(np.array([11, 100, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,52,45,60,44,64,54,48,43],
[48,0,38,44,31,48,33,44,43,49,43],
[49,62,0,42,35,42,58,66,69,51,43],
[48,56,58,0,50,61,46,60,55,60,50],
[55,69,65,50,0,62,51,63,61,60,49],
[40,52,58,39,38,0,56,61,47,51,27],
[56,67,42,54,49,44,0,52,63,59,53],
[36,56,34,40,37,39,48,0,50,42,42],
[46,57,31,45,39,53,37,50,0,53,35],
[52,51,49,40,40,49,41,58,47,0,54],
[57,57,57,50,51,73,47,58,65,46,0]])



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
result = np.append(np.array([11, 100, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,55,52,36,40,42,50,45,41,55],
[56,0,75,49,59,56,55,61,57,56,60],
[45,25,0,33,33,38,34,45,35,40,45],
[48,51,67,0,52,56,56,58,52,55,61],
[64,41,67,48,0,51,43,60,49,52,54],
[60,44,62,44,49,0,37,55,40,52,48],
[58,45,66,44,57,63,0,56,50,57,57],
[50,39,55,42,40,45,44,0,48,48,63],
[55,43,65,48,51,60,50,52,0,46,47],
[59,44,60,45,48,48,43,52,54,0,50],
[45,40,55,39,46,52,43,37,53,50,0]])



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
result = np.append(np.array([11, 100, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,74,84,77,63,67,59,61,47,68],
[25,0,60,58,72,49,55,45,48,54,50],
[26,40,0,55,58,51,56,39,32,39,48],
[16,42,45,0,49,36,57,34,38,29,28],
[23,28,42,51,0,40,55,41,37,26,49],
[37,51,49,64,60,0,66,50,41,39,44],
[33,45,44,43,45,34,0,37,34,37,30],
[41,55,61,66,59,50,63,0,52,38,50],
[39,52,68,62,63,59,66,48,0,28,58],
[53,46,61,71,74,61,63,62,72,0,65],
[32,50,52,72,51,56,70,50,42,35,0]])



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
result = np.append(np.array([11, 100, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,60,46,48,54,57,57,55,48],
[50,0,57,53,53,55,44,57,45,55,49],
[47,43,0,58,43,53,40,57,49,44,48],
[40,47,42,0,35,37,45,42,46,48,32],
[54,47,57,65,0,55,47,62,56,56,53],
[52,45,47,63,45,0,42,54,45,54,45],
[46,56,60,55,53,58,0,57,59,53,54],
[43,43,43,58,38,46,43,0,45,48,42],
[43,55,51,54,44,55,41,55,0,55,47],
[45,45,56,52,44,46,47,52,45,0,43],
[52,51,52,68,47,55,46,58,53,57,0]])



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
result = np.append(np.array([11, 100, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,41,50,57,49,48,60,44,43,57],
[52,0,48,50,55,56,59,54,47,52,62],
[59,52,0,50,58,60,59,58,49,52,54],
[50,50,50,0,54,54,56,53,54,52,56],
[43,45,42,46,0,48,51,51,41,45,48],
[51,44,40,46,52,0,53,54,42,48,53],
[52,41,41,44,49,47,0,49,43,38,55],
[40,46,42,47,49,46,51,0,48,44,51],
[56,53,51,46,59,58,57,52,0,47,60],
[57,48,48,48,55,52,62,56,53,0,58],
[43,38,46,44,52,47,45,49,40,42,0]])



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
result = np.append(np.array([11, 100, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,74,64,72,65,55,59,73,65,49],
[41,0,65,54,50,47,64,41,64,66,54],
[26,35,0,56,51,44,36,30,65,65,53],
[36,46,44,0,54,30,45,29,61,47,57],
[28,50,49,46,0,51,50,38,62,56,46],
[35,53,56,70,49,0,47,28,59,68,39],
[45,36,64,55,50,53,0,40,57,55,55],
[41,59,70,71,62,72,60,0,72,86,72],
[27,36,35,39,38,41,43,28,0,34,29],
[35,34,35,53,44,32,45,14,66,0,30],
[51,46,47,43,54,61,45,28,71,70,0]])



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
result = np.append(np.array([11, 100, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,72,48,58,45,55,54,48,54],
[48,0,58,67,39,58,46,40,56,56,57],
[41,42,0,56,34,64,52,48,48,46,49],
[28,33,44,0,37,37,39,36,30,36,35],
[52,61,66,63,0,47,49,64,53,53,53],
[42,42,36,63,53,0,39,35,49,50,47],
[55,54,48,61,51,61,0,51,64,52,61],
[45,60,52,64,36,65,49,0,56,56,42],
[46,44,52,70,47,51,36,44,0,46,57],
[52,44,54,64,47,50,48,44,54,0,48],
[46,43,51,65,47,53,39,58,43,52,0]])



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
result = np.append(np.array([11, 100, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,50,58,36,64,54,48,50,59],
[46,0,44,50,57,50,63,62,44,55,43],
[54,56,0,56,52,57,60,58,50,57,56],
[50,50,44,0,56,46,65,57,46,61,56],
[42,43,48,44,0,48,49,51,45,47,47],
[64,50,43,54,52,0,62,56,42,56,50],
[36,37,40,35,51,38,0,56,44,40,46],
[46,38,42,43,49,44,44,0,51,53,37],
[52,56,50,54,55,58,56,49,0,57,56],
[50,45,43,39,53,44,60,47,43,0,49],
[41,57,44,44,53,50,54,63,44,51,0]])



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
result = np.append(np.array([11, 100, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,91,83,100,49,74,75,85,94,74],
[34,0,74,57,57,68,65,55,65,68,48],
[9,26,0,28,34,58,36,26,17,85,42],
[17,43,72,0,49,49,42,43,17,85,42],
[0,43,66,51,0,49,45,52,26,94,51],
[51,32,42,51,51,0,42,32,42,51,42],
[26,35,64,58,55,58,0,58,26,68,32],
[25,45,74,57,48,68,42,0,36,76,42],
[15,35,83,83,74,58,74,64,0,77,65],
[6,32,15,15,6,49,32,24,23,0,23],
[26,52,58,58,49,58,68,58,35,77,0]])



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
result = np.append(np.array([11, 100, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,59,37,39,45,49,47,33,34,47],
[59,0,56,64,41,50,58,55,60,51,48],
[41,44,0,43,27,54,58,51,29,35,31],
[63,36,57,0,47,42,57,54,48,47,41],
[61,59,73,53,0,56,50,48,47,46,55],
[55,50,46,58,44,0,56,57,37,50,44],
[51,42,42,43,50,44,0,56,41,42,43],
[53,45,49,46,52,43,44,0,30,47,52],
[67,40,71,52,53,63,59,70,0,46,51],
[66,49,65,53,54,50,58,53,54,0,50],
[53,52,69,59,45,56,57,48,49,50,0]])



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
result = np.append(np.array([11, 100, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,53,60,37,46,56,38,46,45,55],
[56,0,52,65,55,59,57,50,62,61,51],
[47,48,0,61,48,49,58,40,50,44,66],
[40,35,39,0,36,50,51,30,41,39,42],
[63,45,52,64,0,56,56,46,52,50,58],
[54,41,51,50,44,0,50,44,56,50,53],
[44,43,42,49,44,50,0,45,48,39,50],
[62,50,60,70,54,56,55,0,50,58,45],
[54,38,50,59,48,44,52,50,0,47,48],
[55,39,56,61,50,50,61,42,53,0,43],
[45,49,34,58,42,47,50,55,52,57,0]])



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
result = np.append(np.array([11, 100, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,47,39,38,47,34,40,36,31,42],
[56,0,44,46,46,41,43,48,43,48,43],
[53,56,0,42,48,47,42,47,41,42,43],
[61,54,58,0,56,47,49,53,49,50,51],
[62,54,52,44,0,45,42,46,47,48,44],
[53,59,53,53,55,0,48,49,47,57,52],
[66,57,58,51,58,52,0,48,54,54,52],
[60,52,53,47,54,51,52,0,52,51,53],
[64,57,59,51,53,53,46,48,0,53,51],
[69,52,58,50,52,43,46,49,47,0,46],
[58,57,57,49,56,48,48,47,49,54,0]])



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
result = np.append(np.array([11, 100, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,50,45,46,41,40,57,53,42,52],
[54,0,65,61,41,40,52,60,59,37,49],
[50,35,0,41,50,27,49,51,48,33,46],
[55,39,59,0,46,54,58,57,56,50,53],
[54,59,50,54,0,36,58,58,57,44,42],
[59,60,73,46,64,0,59,53,68,49,58],
[60,48,51,42,42,41,0,54,54,48,44],
[43,40,49,43,42,47,46,0,51,47,48],
[47,41,52,44,43,32,46,49,0,36,48],
[58,63,67,50,56,51,52,53,64,0,61],
[48,51,54,47,58,42,56,52,52,39,0]])



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
result = np.append(np.array([11, 100, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,61,60,53,69,84,48,63,55,57],
[54,0,48,72,55,65,71,61,60,64,58],
[39,52,0,54,59,59,69,49,58,53,53],
[40,28,46,0,46,49,55,31,39,37,48],
[47,45,41,54,0,49,53,40,47,56,53],
[31,35,41,51,51,0,61,48,55,44,42],
[16,29,31,45,47,39,0,40,42,40,38],
[52,39,51,69,60,52,60,0,63,61,58],
[37,40,42,61,53,45,58,37,0,44,55],
[45,36,47,63,44,56,60,39,56,0,60],
[43,42,47,52,47,58,62,42,45,40,0]])



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
result = np.append(np.array([11, 100, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_11_100.csv", index=False, header=False)