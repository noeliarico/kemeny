
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,46,64,43,42,59,47,40,69,48],
[54,0,69,65,55,66,53,59,75,48],
[36,31,0,45,32,50,45,40,53,37],
[57,35,55,0,46,58,55,54,60,54],
[58,45,68,54,0,60,53,53,71,58],
[41,34,50,42,40,0,38,33,73,48],
[53,47,55,45,47,62,0,44,57,50],
[60,41,60,46,47,67,56,0,77,55],
[31,25,47,40,29,27,43,23,0,29],
[52,52,63,46,42,52,50,45,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,50,53,56,61,60,50,47],
[44,0,59,55,53,60,59,53,51,49],
[47,41,0,43,34,50,61,45,50,42],
[50,45,57,0,58,49,62,63,54,49],
[47,47,66,42,0,49,66,57,53,48],
[44,40,50,51,51,0,57,45,50,49],
[39,41,39,38,34,43,0,38,37,40],
[40,47,55,37,43,55,62,0,45,50],
[50,49,50,46,47,50,63,55,0,48],
[53,51,58,51,52,51,60,50,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,49,49,46,41,46,52,51],
[51,0,47,49,49,51,41,46,52,48],
[55,53,0,45,50,54,42,51,56,54],
[51,51,55,0,43,54,46,44,53,49],
[51,51,50,57,0,57,53,47,51,48],
[54,49,46,46,43,0,47,42,49,45],
[59,59,58,54,47,53,0,45,55,52],
[54,54,49,56,53,58,55,0,57,56],
[48,48,44,47,49,51,45,43,0,49],
[49,52,46,51,52,55,48,44,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,44,52,42,32,53,43,72,69],
[70,0,72,71,46,60,76,62,90,75],
[56,28,0,49,56,35,47,46,85,58],
[48,29,51,0,57,48,39,45,84,75],
[58,54,44,43,0,45,62,39,81,62],
[68,40,65,52,55,0,40,62,70,65],
[47,24,53,61,38,60,0,44,81,51],
[57,38,54,55,61,38,56,0,76,56],
[28,10,15,16,19,30,19,24,0,29],
[31,25,42,25,38,35,49,44,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,73,53,38,45,39,78,43,51],
[39,0,57,55,34,54,33,63,31,28],
[27,43,0,34,25,25,19,35,35,33],
[47,45,66,0,37,44,33,72,41,33],
[62,66,75,63,0,65,54,64,58,46],
[55,46,75,56,35,0,64,65,59,36],
[61,67,81,67,46,36,0,80,80,42],
[22,37,65,28,36,35,20,0,29,11],
[57,69,65,59,42,41,20,71,0,28],
[49,72,67,67,54,64,58,89,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,41,52,51,46,59,44,52,42],
[53,0,50,51,46,45,53,47,53,52],
[59,50,0,55,56,43,55,52,52,50],
[48,49,45,0,54,55,56,50,48,51],
[49,54,44,46,0,50,58,44,49,52],
[54,55,57,45,50,0,57,50,50,54],
[41,47,45,44,42,43,0,43,47,49],
[56,53,48,50,56,50,57,0,48,52],
[48,47,48,52,51,50,53,52,0,52],
[58,48,50,49,48,46,51,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,50,54,54,44,39,62,44,54],
[56,0,20,19,47,31,66,68,46,63],
[50,80,0,50,71,41,66,80,41,80],
[46,81,50,0,91,31,56,99,81,54],
[46,53,29,9,0,14,56,39,46,53],
[56,69,59,69,86,0,66,68,85,49],
[61,34,34,44,44,34,0,82,51,63],
[38,32,20,1,61,32,18,0,37,24],
[56,54,59,19,54,15,49,63,0,63],
[46,37,20,46,47,51,37,76,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,35,33,49,20,51,41,54,53],
[65,0,59,59,66,42,71,62,75,61],
[65,41,0,62,66,51,64,71,61,54],
[67,41,38,0,64,35,58,61,52,51],
[51,34,34,36,0,30,50,57,42,38],
[80,58,49,65,70,0,74,65,60,55],
[49,29,36,42,50,26,0,49,42,37],
[59,38,29,39,43,35,51,0,44,34],
[46,25,39,48,58,40,58,56,0,40],
[47,39,46,49,62,45,63,66,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,60,70,62,48,44,30,45,46],
[48,0,60,70,73,63,70,38,40,53],
[40,40,0,60,41,37,55,33,42,46],
[30,30,40,0,51,59,46,18,34,34],
[38,27,59,49,0,42,38,25,42,46],
[52,37,63,41,58,0,44,29,35,38],
[56,30,45,54,62,56,0,24,48,53],
[70,62,67,82,75,71,76,0,53,49],
[55,60,58,66,58,65,52,47,0,52],
[54,47,54,66,54,62,47,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,63,51,47,58,49,71,53,47],
[48,0,52,47,40,30,40,60,53,33],
[37,48,0,43,36,40,50,52,50,46],
[49,53,57,0,59,37,51,48,54,56],
[53,60,64,41,0,53,56,52,43,28],
[42,70,60,63,47,0,44,45,47,38],
[51,60,50,49,44,56,0,49,59,44],
[29,40,48,52,48,55,51,0,42,28],
[47,47,50,46,57,53,41,58,0,41],
[53,67,54,44,72,62,56,72,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,57,0,34,34,43,34,57,39],
[43,0,34,43,43,43,43,43,100,43],
[43,66,0,43,43,43,43,43,100,43],
[100,57,57,0,72,34,77,34,57,39],
[66,57,57,28,0,23,66,62,57,62],
[66,57,57,66,77,0,43,77,95,77],
[57,57,57,23,34,57,0,57,57,62],
[66,57,57,66,38,23,43,0,95,77],
[43,0,0,43,43,5,43,5,0,43],
[61,57,57,61,38,23,38,23,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,64,39,41,35,53,55,51,39],
[54,0,56,34,46,43,51,57,56,35],
[36,44,0,40,33,27,44,58,58,30],
[61,66,60,0,58,41,57,55,62,42],
[59,54,67,42,0,52,50,59,56,37],
[65,57,73,59,48,0,56,62,57,47],
[47,49,56,43,50,44,0,53,55,50],
[45,43,42,45,41,38,47,0,43,37],
[49,44,42,38,44,43,45,57,0,40],
[61,65,70,58,63,53,50,63,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,57,35,42,37,47,37,47],
[51,0,42,57,41,48,43,45,40,45],
[52,58,0,56,38,46,36,44,36,50],
[43,43,44,0,37,47,32,44,39,47],
[65,59,62,63,0,55,51,54,47,49],
[58,52,54,53,45,0,40,50,47,53],
[63,57,64,68,49,60,0,59,50,54],
[53,55,56,56,46,50,41,0,48,48],
[63,60,64,61,53,53,50,52,0,53],
[53,55,50,53,51,47,46,52,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,52,50,53,41,64,45,59],
[48,0,45,41,40,50,38,39,33,51],
[49,55,0,45,55,45,39,52,39,48],
[48,59,55,0,43,48,41,57,46,61],
[50,60,45,57,0,53,50,54,48,69],
[47,50,55,52,47,0,48,50,47,53],
[59,62,61,59,50,52,0,67,52,64],
[36,61,48,43,46,50,33,0,44,60],
[55,67,61,54,52,53,48,56,0,62],
[41,49,52,39,31,47,36,40,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,35,49,45,51,40,29,36,49],
[43,0,37,46,35,48,37,44,43,45],
[65,63,0,58,51,50,51,47,47,54],
[51,54,42,0,52,55,51,49,43,50],
[55,65,49,48,0,57,47,43,42,52],
[49,52,50,45,43,0,49,41,49,47],
[60,63,49,49,53,51,0,42,52,48],
[71,56,53,51,57,59,58,0,51,49],
[64,57,53,57,58,51,48,49,0,58],
[51,55,46,50,48,53,52,51,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,83,61,52,67,30,63,60,49,63],
[17,0,46,48,40,24,45,43,42,41],
[39,54,0,46,38,25,53,36,42,45],
[48,52,54,0,54,40,45,54,47,52],
[33,60,62,46,0,25,83,42,50,52],
[70,76,75,60,75,0,77,60,48,69],
[37,55,47,55,17,23,0,39,35,44],
[40,57,64,46,58,40,61,0,53,38],
[51,58,58,53,50,52,65,47,0,35],
[37,59,55,48,48,31,56,62,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,47,52,52,59,50,55,63],
[44,0,44,43,46,42,54,38,46,52],
[50,56,0,49,54,57,50,46,56,54],
[53,57,51,0,51,49,51,46,50,60],
[48,54,46,49,0,46,50,43,54,54],
[48,58,43,51,54,0,49,48,54,51],
[41,46,50,49,50,51,0,55,55,56],
[50,62,54,54,57,52,45,0,60,58],
[45,54,44,50,46,46,45,40,0,56],
[37,48,46,40,46,49,44,42,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,51,48,46,35,40,40,37,26],
[57,0,53,59,63,43,68,49,44,48],
[49,47,0,50,48,46,37,56,56,46],
[52,41,50,0,52,45,43,44,45,35],
[54,37,52,48,0,49,42,46,43,22],
[65,57,54,55,51,0,50,64,47,53],
[60,32,63,57,58,50,0,51,44,30],
[60,51,44,56,54,36,49,0,43,34],
[63,56,44,55,57,53,56,57,0,39],
[74,52,54,65,78,47,70,66,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,52,51,52,57,42,43,46,43],
[58,0,56,57,50,54,53,52,51,62],
[48,44,0,48,40,50,43,48,46,51],
[49,43,52,0,44,48,37,48,42,50],
[48,50,60,56,0,54,49,61,44,61],
[43,46,50,52,46,0,41,44,41,49],
[58,47,57,63,51,59,0,53,48,59],
[57,48,52,52,39,56,47,0,51,60],
[54,49,54,58,56,59,52,49,0,62],
[57,38,49,50,39,51,41,40,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,42,46,61,43,62,39,53],
[50,0,53,60,54,52,43,57,54,50],
[45,47,0,49,43,44,39,55,44,54],
[58,40,51,0,44,50,50,61,51,49],
[54,46,57,56,0,50,56,59,56,54],
[39,48,56,50,50,0,51,47,50,57],
[57,57,61,50,44,49,0,65,52,58],
[38,43,45,39,41,53,35,0,45,42],
[61,46,56,49,44,50,48,55,0,55],
[47,50,46,51,46,43,42,58,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,45,47,32,36,41,48,31],
[74,0,45,63,55,49,41,57,63,55],
[70,55,0,50,50,52,32,47,66,54],
[55,37,50,0,61,50,51,72,60,51],
[53,45,50,39,0,48,36,53,55,43],
[68,51,48,50,52,0,41,50,57,59],
[64,59,68,49,64,59,0,64,64,62],
[59,43,53,28,47,50,36,0,60,45],
[52,37,34,40,45,43,36,40,0,42],
[69,45,46,49,57,41,38,55,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,57,36,46,51,59,29,51],
[52,0,38,65,43,31,57,42,42,57],
[48,62,0,62,53,50,56,50,46,68],
[43,35,38,0,45,41,51,36,46,35],
[64,57,47,55,0,33,56,47,28,45],
[54,69,50,59,67,0,45,42,52,68],
[49,43,44,49,44,55,0,44,51,52],
[41,58,50,64,53,58,56,0,57,65],
[71,58,54,54,72,48,49,43,0,56],
[49,43,32,65,55,32,48,35,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,49,40,40,61,53,40,50,37],
[36,0,45,26,52,56,33,35,51,39],
[51,55,0,42,53,64,51,39,56,34],
[60,74,58,0,62,61,57,62,54,42],
[60,48,47,38,0,57,39,51,52,34],
[39,44,36,39,43,0,53,40,43,38],
[47,67,49,43,61,47,0,53,56,40],
[60,65,61,38,49,60,47,0,59,54],
[50,49,44,46,48,57,44,41,0,37],
[63,61,66,58,66,62,60,46,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,43,50,44,43,44,48,53,45],
[56,0,45,57,46,52,50,59,51,52],
[57,55,0,57,50,48,50,59,59,52],
[50,43,43,0,50,38,45,55,58,49],
[56,54,50,50,0,48,55,53,62,48],
[57,48,52,62,52,0,55,65,57,53],
[56,50,50,55,45,45,0,61,58,51],
[52,41,41,45,47,35,39,0,52,43],
[47,49,41,42,38,43,42,48,0,44],
[55,48,48,51,52,47,49,57,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,62,54,55,46,54,56,50,52],
[46,0,57,55,51,51,45,47,51,43],
[38,43,0,44,50,49,33,42,46,44],
[46,45,56,0,61,54,50,44,55,49],
[45,49,50,39,0,51,43,42,49,51],
[54,49,51,46,49,0,48,43,48,45],
[46,55,67,50,57,52,0,50,61,54],
[44,53,58,56,58,57,50,0,59,49],
[50,49,54,45,51,52,39,41,0,46],
[48,57,56,51,49,55,46,51,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,70,49,73,49,55,55,67,62],
[42,0,50,63,53,33,34,40,61,55],
[30,50,0,59,60,40,38,63,70,62],
[51,37,41,0,45,38,51,40,49,43],
[27,47,40,55,0,43,41,30,48,47],
[51,67,60,62,57,0,56,47,62,65],
[45,66,62,49,59,44,0,40,48,51],
[45,60,37,60,70,53,60,0,78,56],
[33,39,30,51,52,38,52,22,0,48],
[38,45,38,57,53,35,49,44,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,56,53,49,44,47,56,46],
[50,0,47,55,45,48,54,50,56,55],
[50,53,0,58,55,49,54,53,55,55],
[44,45,42,0,44,39,38,44,49,35],
[47,55,45,56,0,44,53,43,58,49],
[51,52,51,61,56,0,57,49,58,52],
[56,46,46,62,47,43,0,52,57,49],
[53,50,47,56,57,51,48,0,49,52],
[44,44,45,51,42,42,43,51,0,38],
[54,45,45,65,51,48,51,48,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,29,55,51,32,44,45,44],
[74,0,42,51,70,57,41,55,61,53],
[70,58,0,39,71,64,53,52,59,55],
[71,49,61,0,87,66,64,61,58,56],
[45,30,29,13,0,39,26,35,34,39],
[49,43,36,34,61,0,36,37,48,53],
[68,59,47,36,74,64,0,48,50,50],
[56,45,48,39,65,63,52,0,54,59],
[55,39,41,42,66,52,50,46,0,43],
[56,47,45,44,61,47,50,41,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,50,64,37,50,55,46,61,57],
[67,0,57,63,47,52,63,57,65,58],
[50,43,0,54,48,41,66,46,67,71],
[36,37,46,0,28,38,40,42,62,49],
[63,53,52,72,0,66,71,50,68,74],
[50,48,59,62,34,0,62,65,69,61],
[45,37,34,60,29,38,0,47,63,53],
[54,43,54,58,50,35,53,0,57,50],
[39,35,33,38,32,31,37,43,0,44],
[43,42,29,51,26,39,47,50,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,62,100,67,60,68,44,100,77],
[0,0,36,21,20,21,43,21,19,44],
[38,64,0,54,43,38,64,60,40,82],
[0,79,46,0,38,39,43,39,19,45],
[33,80,57,62,0,22,59,39,51,61],
[40,79,62,61,78,0,43,47,59,44],
[32,57,36,57,41,57,0,58,53,76],
[56,79,40,61,61,53,42,0,58,60],
[0,81,60,81,49,41,47,42,0,60],
[23,56,18,55,39,56,24,40,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,35,49,47,42,41,52,41],
[49,0,38,45,47,48,49,36,43,37],
[54,62,0,54,55,62,48,61,57,45],
[65,55,46,0,55,51,56,47,51,55],
[51,53,45,45,0,51,52,49,50,32],
[53,52,38,49,49,0,48,35,43,49],
[58,51,52,44,48,52,0,49,46,48],
[59,64,39,53,51,65,51,0,51,47],
[48,57,43,49,50,57,54,49,0,52],
[59,63,55,45,68,51,52,53,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,49,47,50,50,53,46,51,44],
[48,0,51,54,60,54,47,54,55,53],
[51,49,0,52,56,52,48,50,51,41],
[53,46,48,0,49,47,48,50,47,44],
[50,40,44,51,0,48,52,41,43,44],
[50,46,48,53,52,0,47,50,53,43],
[47,53,52,52,48,53,0,51,50,46],
[54,46,50,50,59,50,49,0,47,38],
[49,45,49,53,57,47,50,53,0,47],
[56,47,59,56,56,57,54,62,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,48,41,54,57,51,45,53],
[48,0,45,44,40,51,55,49,49,46],
[54,55,0,48,48,49,51,44,46,50],
[52,56,52,0,47,57,57,48,47,53],
[59,60,52,53,0,48,51,51,51,59],
[46,49,51,43,52,0,51,46,41,54],
[43,45,49,43,49,49,0,44,50,52],
[49,51,56,52,49,54,56,0,49,51],
[55,51,54,53,49,59,50,51,0,56],
[47,54,50,47,41,46,48,49,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,64,55,48,44,55,40,43,60],
[44,0,49,51,44,49,60,58,48,56],
[36,51,0,33,36,40,48,36,31,53],
[45,49,67,0,56,61,61,50,51,60],
[52,56,64,44,0,44,50,54,41,56],
[56,51,60,39,56,0,64,47,56,53],
[45,40,52,39,50,36,0,49,40,58],
[60,42,64,50,46,53,51,0,29,49],
[57,52,69,49,59,44,60,71,0,67],
[40,44,47,40,44,47,42,51,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,45,56,59,50,59,55,51],
[45,0,47,49,40,52,47,52,50,41],
[44,53,0,47,47,51,48,38,43,46],
[55,51,53,0,59,63,62,48,61,53],
[44,60,53,41,0,55,51,58,58,42],
[41,48,49,37,45,0,50,49,50,31],
[50,53,52,38,49,50,0,45,49,44],
[41,48,62,52,42,51,55,0,56,41],
[45,50,57,39,42,50,51,44,0,45],
[49,59,54,47,58,69,56,59,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,50,44,46,53,56,54,55,61],
[61,0,58,51,55,49,56,62,55,59],
[50,42,0,42,47,49,49,50,46,50],
[56,49,58,0,49,53,47,56,55,57],
[54,45,53,51,0,55,47,58,49,55],
[47,51,51,47,45,0,45,51,49,57],
[44,44,51,53,53,55,0,56,54,54],
[46,38,50,44,42,49,44,0,48,50],
[45,45,54,45,51,51,46,52,0,55],
[39,41,50,43,45,43,46,50,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,54,52,55,46,55,54,56],
[47,0,42,43,57,52,46,46,43,60],
[50,58,0,50,52,57,47,54,56,65],
[46,57,50,0,57,55,52,54,54,52],
[48,43,48,43,0,53,48,46,49,51],
[45,48,43,45,47,0,50,51,43,52],
[54,54,53,48,52,50,0,55,56,55],
[45,54,46,46,54,49,45,0,51,55],
[46,57,44,46,51,57,44,49,0,47],
[44,40,35,48,49,48,45,45,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,35,45,22,13,34,20,26,33],
[55,0,63,64,52,52,48,50,62,63],
[65,37,0,60,36,33,46,33,38,58],
[55,36,40,0,37,37,42,41,52,51],
[78,48,64,63,0,60,55,45,56,61],
[87,48,67,63,40,0,50,55,50,67],
[66,52,54,58,45,50,0,56,55,61],
[80,50,67,59,55,45,44,0,56,68],
[74,38,62,48,44,50,45,44,0,63],
[67,37,42,49,39,33,39,32,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,44,37,35,42,45,39,34,54],
[58,0,38,41,56,39,50,42,39,57],
[56,62,0,36,51,44,66,48,40,48],
[63,59,64,0,55,54,36,64,69,68],
[65,44,49,45,0,25,35,37,27,39],
[58,61,56,46,75,0,56,39,61,46],
[55,50,34,64,65,44,0,46,64,49],
[61,58,52,36,63,61,54,0,41,47],
[66,61,60,31,73,39,36,59,0,50],
[46,43,52,32,61,54,51,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,47,60,47,32,35,44,50,65],
[42,0,49,41,36,35,36,43,55,54],
[53,51,0,55,60,36,55,52,48,55],
[40,59,45,0,50,31,32,52,46,63],
[53,64,40,50,0,34,46,53,53,59],
[68,65,64,69,66,0,49,66,61,72],
[65,64,45,68,54,51,0,56,53,63],
[56,57,48,48,47,34,44,0,45,57],
[50,45,52,54,47,39,47,55,0,60],
[35,46,45,37,41,28,37,43,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,72,100,44,29,72,100,57,57],
[0,0,0,0,15,0,15,56,29,0],
[28,100,0,100,72,57,43,85,57,28],
[0,100,0,0,44,0,15,85,57,28],
[56,85,28,56,0,28,56,56,85,28],
[71,100,43,100,72,0,43,100,100,28],
[28,85,57,85,44,57,0,85,57,57],
[0,44,15,15,44,0,15,0,29,0],
[43,71,43,43,15,0,43,71,0,28],
[43,100,72,72,72,72,43,100,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,40,56,87,65,52,53,48,53],
[50,0,38,63,68,62,50,46,36,78],
[60,62,0,68,72,65,75,48,45,76],
[44,37,32,0,62,40,37,35,40,58],
[13,32,28,38,0,46,39,24,35,42],
[35,38,35,60,54,0,49,33,52,71],
[48,50,25,63,61,51,0,35,52,66],
[47,54,52,65,76,67,65,0,57,70],
[52,64,55,60,65,48,48,43,0,63],
[47,22,24,42,58,29,34,30,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,49,58,50,59,63,62,54,61],
[42,0,42,43,49,51,50,57,48,56],
[51,58,0,52,56,53,60,54,49,61],
[42,57,48,0,46,58,58,61,50,53],
[50,51,44,54,0,50,57,65,57,53],
[41,49,47,42,50,0,56,47,50,48],
[37,50,40,42,43,44,0,53,49,49],
[38,43,46,39,35,53,47,0,44,57],
[46,52,51,50,43,50,51,56,0,53],
[39,44,39,47,47,52,51,43,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,61,64,50,40,57,42,46,58],
[51,0,52,50,54,40,45,52,45,46],
[39,48,0,56,36,39,47,43,41,51],
[36,50,44,0,39,45,47,40,38,60],
[50,46,64,61,0,48,48,50,44,55],
[60,60,61,55,52,0,53,50,56,61],
[43,55,53,53,52,47,0,48,48,62],
[58,48,57,60,50,50,52,0,37,49],
[54,55,59,62,56,44,52,63,0,57],
[42,54,49,40,45,39,38,51,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,66,52,57,46,55,74,45,66],
[53,0,66,40,66,46,51,75,56,64],
[34,34,0,20,43,32,45,62,39,51],
[48,60,80,0,53,59,49,63,47,62],
[43,34,57,47,0,35,36,61,55,46],
[54,54,68,41,65,0,68,73,73,65],
[45,49,55,51,64,32,0,54,55,53],
[26,25,38,37,39,27,46,0,36,45],
[55,44,61,53,45,27,45,64,0,55],
[34,36,49,38,54,35,47,55,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,68,26,33,47,74,31,27,43],
[71,0,79,40,17,73,58,58,47,56],
[32,21,0,37,30,39,62,28,30,37],
[74,60,63,0,50,67,62,63,66,63],
[67,83,70,50,0,81,58,61,67,61],
[53,27,61,33,19,0,44,55,35,44],
[26,42,38,38,42,56,0,23,23,54],
[69,42,72,37,39,45,77,0,67,77],
[73,53,70,34,33,65,77,33,0,48],
[57,44,63,37,39,56,46,23,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,44,47,48,44,37,44,46],
[54,0,52,52,56,56,50,44,50,52],
[58,48,0,57,58,57,55,54,61,55],
[56,48,43,0,55,49,48,41,50,50],
[53,44,42,45,0,46,50,43,47,49],
[52,44,43,51,54,0,47,34,49,45],
[56,50,45,52,50,53,0,47,47,48],
[63,56,46,59,57,66,53,0,56,49],
[56,50,39,50,53,51,53,44,0,54],
[54,48,45,50,51,55,52,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,57,58,52,49,57,66,66,46],
[42,0,58,51,49,45,56,64,57,45],
[43,42,0,51,43,47,46,70,65,53],
[42,49,49,0,54,43,55,67,70,44],
[48,51,57,46,0,52,56,69,62,47],
[51,55,53,57,48,0,52,69,59,51],
[43,44,54,45,44,48,0,69,57,51],
[34,36,30,33,31,31,31,0,49,26],
[34,43,35,30,38,41,43,51,0,36],
[54,55,47,56,53,49,49,74,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,54,59,52,54,48,47,45],
[50,0,45,50,55,45,52,39,43,43],
[49,55,0,50,54,54,52,51,47,49],
[46,50,50,0,54,51,44,44,44,42],
[41,45,46,46,0,43,39,39,41,34],
[48,55,46,49,57,0,45,45,42,44],
[46,48,48,56,61,55,0,52,46,40],
[52,61,49,56,61,55,48,0,52,55],
[53,57,53,56,59,58,54,48,0,48],
[55,57,51,58,66,56,60,45,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,60,43,48,69,44,38,75,41],
[72,0,66,47,58,88,77,55,77,58],
[40,34,0,54,47,65,36,35,68,57],
[57,53,46,0,55,72,62,36,53,63],
[52,42,53,45,0,79,56,24,56,60],
[31,12,35,28,21,0,40,21,41,27],
[56,23,64,38,44,60,0,30,68,46],
[62,45,65,64,76,79,70,0,70,73],
[25,23,32,47,44,59,32,30,0,43],
[59,42,43,37,40,73,54,27,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,46,51,46,44,48,54,52,46],
[53,0,56,49,52,52,49,53,53,50],
[54,44,0,52,56,54,52,54,56,56],
[49,51,48,0,57,61,47,51,51,51],
[54,48,44,43,0,47,45,49,51,46],
[56,48,46,39,53,0,45,52,50,45],
[52,51,48,53,55,55,0,47,58,51],
[46,47,46,49,51,48,53,0,48,50],
[48,47,44,49,49,50,42,52,0,45],
[54,50,44,49,54,55,49,50,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,59,67,69,61,54,55,55],
[51,0,51,50,64,71,60,57,59,48],
[45,49,0,47,70,69,59,37,61,38],
[41,50,53,0,84,71,58,42,43,55],
[33,36,30,16,0,53,41,27,34,37],
[31,29,31,29,47,0,42,29,39,31],
[39,40,41,42,59,58,0,46,60,32],
[46,43,63,58,73,71,54,0,83,52],
[45,41,39,57,66,61,40,17,0,52],
[45,52,62,45,63,69,68,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,68,63,63,63,63,25,62,100],
[5,0,30,30,63,25,30,25,62,62],
[32,70,0,63,95,32,70,57,62,75],
[37,70,37,0,95,32,37,57,62,75],
[37,37,5,5,0,37,37,32,37,37],
[37,75,68,68,63,0,68,25,62,75],
[37,70,30,63,63,32,0,25,62,75],
[75,75,43,43,68,75,75,0,62,75],
[38,38,38,38,63,38,38,38,0,75],
[0,38,25,25,63,25,25,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,55,45,42,45,48,50,48,54],
[48,0,54,49,50,43,44,54,47,50],
[45,46,0,39,51,49,47,49,49,56],
[55,51,61,0,55,54,45,55,49,63],
[58,50,49,45,0,54,49,63,50,60],
[55,57,51,46,46,0,54,53,46,55],
[52,56,53,55,51,46,0,60,46,52],
[50,46,51,45,37,47,40,0,45,60],
[52,53,51,51,50,54,54,55,0,52],
[46,50,44,37,40,45,48,40,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,58,56,58,58,38,38,100,58],
[42,0,84,64,46,82,38,64,80,58],
[42,16,0,18,40,40,16,0,58,38],
[44,36,82,0,60,82,16,38,100,58],
[42,54,60,40,0,76,56,40,100,76],
[42,18,60,18,24,0,18,18,64,60],
[62,62,84,84,44,82,0,84,84,58],
[62,36,100,62,60,82,16,0,100,58],
[0,20,42,0,0,36,16,0,0,58],
[42,42,62,42,24,40,42,42,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,43,48,35,50,60,57,45,59],
[62,0,45,49,60,64,69,75,69,68],
[57,55,0,57,51,56,56,46,49,61],
[52,51,43,0,54,45,62,55,50,56],
[65,40,49,46,0,54,65,56,61,63],
[50,36,44,55,46,0,65,60,44,66],
[40,31,44,38,35,35,0,50,36,56],
[43,25,54,45,44,40,50,0,45,56],
[55,31,51,50,39,56,64,55,0,69],
[41,32,39,44,37,34,44,44,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,34,54,44,42,54,48,46,48],
[50,0,49,68,44,50,46,59,58,57],
[66,51,0,57,52,55,49,61,55,63],
[46,32,43,0,44,34,40,47,42,49],
[56,56,48,56,0,55,51,58,54,59],
[58,50,45,66,45,0,47,58,55,54],
[46,54,51,60,49,53,0,53,58,53],
[52,41,39,53,42,42,47,0,46,49],
[54,42,45,58,46,45,42,54,0,54],
[52,43,37,51,41,46,47,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,52,52,50,42,55,52,49,54],
[57,0,47,60,52,50,59,54,46,58],
[48,53,0,56,51,51,55,58,49,57],
[48,40,44,0,42,44,45,50,50,51],
[50,48,49,58,0,56,51,58,46,58],
[58,50,49,56,44,0,51,54,44,58],
[45,41,45,55,49,49,0,53,50,53],
[48,46,42,50,42,46,47,0,48,53],
[51,54,51,50,54,56,50,52,0,52],
[46,42,43,49,42,42,47,47,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,58,65,55,64,50,56,59,55],
[46,0,54,47,56,55,43,48,50,59],
[42,46,0,45,45,48,40,42,50,57],
[35,53,55,0,52,49,46,41,45,51],
[45,44,55,48,0,51,52,50,48,65],
[36,45,52,51,49,0,41,51,51,60],
[50,57,60,54,48,59,0,44,59,59],
[44,52,58,59,50,49,56,0,53,61],
[41,50,50,55,52,49,41,47,0,57],
[45,41,43,49,35,40,41,39,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,42,54,53,48,49,49,37],
[44,0,53,46,47,58,48,48,51,46],
[54,47,0,45,48,60,48,57,53,49],
[58,54,55,0,55,64,52,62,56,49],
[46,53,52,45,0,49,50,56,55,52],
[47,42,40,36,51,0,50,46,51,40],
[52,52,52,48,50,50,0,44,49,50],
[51,52,43,38,44,54,56,0,55,40],
[51,49,47,44,45,49,51,45,0,48],
[63,54,51,51,48,60,50,60,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,42,26,50,43,41,33,50,43],
[59,0,49,45,56,43,73,41,50,56],
[58,51,0,60,79,53,66,58,71,37],
[74,55,40,0,62,50,45,23,58,33],
[50,44,21,38,0,27,41,19,35,25],
[57,57,47,50,73,0,44,26,31,40],
[59,27,34,55,59,56,0,33,34,59],
[67,59,42,77,81,74,67,0,61,42],
[50,50,29,42,65,69,66,39,0,52],
[57,44,63,67,75,60,41,58,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,51,58,57,52,52,47,51,51],
[49,0,57,55,53,52,49,42,50,47],
[49,43,0,49,55,51,47,48,47,54],
[42,45,51,0,43,44,45,44,46,46],
[43,47,45,57,0,50,49,49,52,48],
[48,48,49,56,50,0,49,53,53,53],
[48,51,53,55,51,51,0,53,46,52],
[53,58,52,56,51,47,47,0,49,53],
[49,50,53,54,48,47,54,51,0,46],
[49,53,46,54,52,47,48,47,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,53,44,54,53,49,53,46],
[47,0,51,42,46,43,51,41,47,35],
[45,49,0,39,40,41,42,33,37,42],
[47,58,61,0,39,40,52,47,51,43],
[56,54,60,61,0,47,47,50,54,50],
[46,57,59,60,53,0,52,46,52,52],
[47,49,58,48,53,48,0,48,55,44],
[51,59,67,53,50,54,52,0,54,49],
[47,53,63,49,46,48,45,46,0,39],
[54,65,58,57,50,48,56,51,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,47,50,39,43,49,44,56],
[54,0,53,46,54,41,49,50,44,51],
[52,47,0,44,51,43,45,49,38,50],
[53,54,56,0,53,46,47,57,43,58],
[50,46,49,47,0,43,54,54,42,57],
[61,59,57,54,57,0,53,57,50,60],
[57,51,55,53,46,47,0,56,47,62],
[51,50,51,43,46,43,44,0,45,51],
[56,56,62,57,58,50,53,55,0,62],
[44,49,50,42,43,40,38,49,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,59,44,63,70,56,58,52,61],
[53,0,77,55,55,59,65,56,55,48],
[41,23,0,43,32,46,37,51,50,43],
[56,45,57,0,60,58,47,73,69,54],
[37,45,68,40,0,46,43,54,57,41],
[30,41,54,42,54,0,31,52,55,48],
[44,35,63,53,57,69,0,70,55,62],
[42,44,49,27,46,48,30,0,38,48],
[48,45,50,31,43,45,45,62,0,32],
[39,52,57,46,59,52,38,52,68,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,43,44,45,62,48,36,45],
[48,0,47,46,40,43,53,48,41,57],
[53,53,0,42,51,43,64,48,43,60],
[57,54,58,0,50,49,55,54,47,51],
[56,60,49,50,0,51,55,54,50,52],
[55,57,57,51,49,0,55,48,44,55],
[38,47,36,45,45,45,0,42,39,52],
[52,52,52,46,46,52,58,0,46,51],
[64,59,57,53,50,56,61,54,0,63],
[55,43,40,49,48,45,48,49,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,48,48,42,53,48,50,52,47],
[66,0,42,55,45,55,62,61,63,56],
[52,58,0,47,39,52,44,46,50,53],
[52,45,53,0,39,56,52,50,46,44],
[58,55,61,61,0,62,49,68,61,47],
[47,45,48,44,38,0,37,50,46,50],
[52,38,56,48,51,63,0,59,54,49],
[50,39,54,50,32,50,41,0,47,47],
[48,37,50,54,39,54,46,53,0,50],
[53,44,47,56,53,50,51,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,56,27,25,42,47,50,39,33],
[67,0,39,39,25,53,25,50,39,47],
[44,61,0,30,50,25,30,44,64,66],
[73,61,70,0,34,84,20,73,62,81],
[75,75,50,66,0,64,50,75,75,61],
[58,47,75,16,36,0,16,30,64,52],
[53,75,70,80,50,84,0,53,73,61],
[50,50,56,27,25,70,47,0,61,36],
[61,61,36,38,25,36,27,39,0,47],
[67,53,34,19,39,48,39,64,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,51,57,51,51,51,51,46,50],
[41,0,47,54,48,45,48,41,40,46],
[49,53,0,55,48,44,49,49,47,53],
[43,46,45,0,45,43,48,40,46,50],
[49,52,52,55,0,46,45,50,47,53],
[49,55,56,57,54,0,56,50,53,52],
[49,52,51,52,55,44,0,48,49,55],
[49,59,51,60,50,50,52,0,51,55],
[54,60,53,54,53,47,51,49,0,49],
[50,54,47,50,47,48,45,45,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,62,60,69,43,43,50,69,69],
[57,0,76,81,45,64,64,50,83,59],
[38,24,0,24,69,24,24,74,43,83],
[40,19,76,0,45,57,38,50,83,59],
[31,55,31,55,0,38,38,50,55,31],
[57,36,76,43,62,0,26,50,62,76],
[57,36,76,62,62,74,0,50,86,76],
[50,50,26,50,50,50,50,0,50,50],
[31,17,57,17,45,38,14,50,0,59],
[31,41,17,41,69,24,24,50,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,60,61,54,41,35,33,54],
[59,0,48,72,70,72,56,65,49,58],
[55,52,0,78,68,66,54,61,50,59],
[40,28,22,0,45,39,41,37,23,33],
[39,30,32,55,0,57,42,43,33,39],
[46,28,34,61,43,0,49,44,31,50],
[59,44,46,59,58,51,0,47,37,57],
[65,35,39,63,57,56,53,0,39,58],
[67,51,50,77,67,69,63,61,0,72],
[46,42,41,67,61,50,43,42,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,47,43,44,50,52,54,54],
[54,0,59,36,38,52,47,61,56,67],
[47,41,0,38,49,52,59,54,57,45],
[53,64,62,0,67,46,66,55,67,49],
[57,62,51,33,0,44,53,53,66,57],
[56,48,48,54,56,0,58,60,55,56],
[50,53,41,34,47,42,0,54,57,47],
[48,39,46,45,47,40,46,0,56,37],
[46,44,43,33,34,45,43,44,0,40],
[46,33,55,51,43,44,53,63,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,63,35,41,39,47,35,45,44],
[52,0,48,40,35,42,54,32,50,38],
[37,52,0,26,28,38,48,33,40,49],
[65,60,74,0,45,49,55,54,54,61],
[59,65,72,55,0,53,55,33,51,58],
[61,58,62,51,47,0,54,42,56,55],
[53,46,52,45,45,46,0,34,41,52],
[65,68,67,46,67,58,66,0,50,65],
[55,50,60,46,49,44,59,50,0,48],
[56,62,51,39,42,45,48,35,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,80,59,51,68,81,69,73,50,45],
[20,0,47,46,55,48,59,81,46,31],
[41,53,0,76,52,59,93,76,64,70],
[49,54,24,0,43,66,47,52,64,35],
[32,45,48,57,0,59,60,56,41,28],
[19,52,41,34,41,0,47,50,60,17],
[31,41,7,53,40,53,0,62,41,35],
[27,19,24,48,44,50,38,0,38,6],
[50,54,36,36,59,40,59,62,0,30],
[55,69,30,65,72,83,65,94,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,40,40,13,90,13,63,40,63],
[47,0,47,47,60,100,47,60,87,23],
[60,53,0,50,50,90,60,100,90,23],
[60,53,50,0,50,90,23,100,40,23],
[87,40,50,50,0,77,10,50,40,50],
[10,0,10,10,23,0,10,23,0,10],
[87,53,40,77,90,90,0,100,40,63],
[37,40,0,0,50,77,0,0,40,10],
[60,13,10,60,60,100,60,60,0,23],
[37,77,77,77,50,90,37,90,77,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,58,58,60,63,59,53,68],
[53,0,50,46,42,54,53,53,50,59],
[55,50,0,49,48,50,47,46,44,55],
[42,54,51,0,43,49,48,46,50,60],
[42,58,52,57,0,62,56,58,62,54],
[40,46,50,51,38,0,43,45,54,44],
[37,47,53,52,44,57,0,49,54,56],
[41,47,54,54,42,55,51,0,51,55],
[47,50,56,50,38,46,46,49,0,59],
[32,41,45,40,46,56,44,45,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,60,59,54,47,64,61,51,51],
[43,0,53,61,41,49,60,52,47,52],
[40,47,0,48,41,48,60,42,53,60],
[41,39,52,0,51,41,49,44,49,47],
[46,59,59,49,0,44,52,62,57,48],
[53,51,52,59,56,0,53,50,71,47],
[36,40,40,51,48,47,0,48,56,53],
[39,48,58,56,38,50,52,0,54,52],
[49,53,47,51,43,29,44,46,0,48],
[49,48,40,53,52,53,47,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,50,46,43,44,50,55,44],
[55,0,59,52,53,48,49,46,57,55],
[47,41,0,45,39,40,44,39,44,45],
[50,48,55,0,56,42,49,47,53,44],
[54,47,61,44,0,50,48,51,56,50],
[57,52,60,58,50,0,52,42,52,53],
[56,51,56,51,52,48,0,47,48,41],
[50,54,61,53,49,58,53,0,51,50],
[45,43,56,47,44,48,52,49,0,51],
[56,45,55,56,50,47,59,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,49,50,52,57,60,53,57,63],
[48,0,52,54,48,45,53,54,57,53],
[51,48,0,51,53,44,56,50,53,55],
[50,46,49,0,48,45,51,48,49,45],
[48,52,47,52,0,56,64,52,55,52],
[43,55,56,55,44,0,60,59,52,51],
[40,47,44,49,36,40,0,57,46,50],
[47,46,50,52,48,41,43,0,54,59],
[43,43,47,51,45,48,54,46,0,51],
[37,47,45,55,48,49,50,41,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,44,70,58,87,54,66,56,60],
[29,0,38,63,52,59,57,54,54,22],
[56,62,0,56,39,68,48,58,44,49],
[30,37,44,0,32,58,46,40,46,36],
[42,48,61,68,0,65,61,50,47,53],
[13,41,32,42,35,0,22,39,26,30],
[46,43,52,54,39,78,0,51,53,31],
[34,46,42,60,50,61,49,0,51,32],
[44,46,56,54,53,74,47,49,0,49],
[40,78,51,64,47,70,69,68,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,44,45,45,43,53,44,45,46],
[48,0,41,48,47,44,50,49,49,45],
[56,59,0,47,52,46,58,45,54,55],
[55,52,53,0,41,40,52,47,48,52],
[55,53,48,59,0,52,57,51,54,56],
[57,56,54,60,48,0,54,57,64,55],
[47,50,42,48,43,46,0,49,50,46],
[56,51,55,53,49,43,51,0,55,48],
[55,51,46,52,46,36,50,45,0,43],
[54,55,45,48,44,45,54,52,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,63,64,48,60,51,55,59,59],
[49,0,59,58,47,60,50,45,49,63],
[37,41,0,51,39,50,37,38,44,57],
[36,42,49,0,31,54,39,33,47,57],
[52,53,61,69,0,60,47,55,55,64],
[40,40,50,46,40,0,31,39,40,49],
[49,50,63,61,53,69,0,49,47,63],
[45,55,62,67,45,61,51,0,56,64],
[41,51,56,53,45,60,53,44,0,54],
[41,37,43,43,36,51,37,36,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,64,57,51,47,61,78,81,70],
[22,0,44,54,32,44,38,54,57,61],
[36,56,0,45,52,47,48,66,61,63],
[43,46,55,0,29,32,38,45,58,66],
[49,68,48,71,0,50,67,69,67,69],
[53,56,53,68,50,0,37,62,56,68],
[39,62,52,62,33,63,0,55,69,79],
[22,46,34,55,31,38,45,0,38,57],
[19,43,39,42,33,44,31,62,0,43],
[30,39,37,34,31,32,21,43,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,52,62,54,44,60,43,52,52],
[58,0,49,57,36,40,58,44,41,53],
[48,51,0,56,48,40,58,37,52,46],
[38,43,44,0,42,42,53,49,52,45],
[46,64,52,58,0,53,63,49,58,45],
[56,60,60,58,47,0,51,59,52,49],
[40,42,42,47,37,49,0,44,54,47],
[57,56,63,51,51,41,56,0,51,44],
[48,59,48,48,42,48,46,49,0,40],
[48,47,54,55,55,51,53,56,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,59,47,59,50,49,59,55,61],
[57,0,62,59,71,49,55,65,72,70],
[41,38,0,56,68,40,49,53,54,58],
[53,41,44,0,54,49,55,45,61,60],
[41,29,32,46,0,42,41,36,41,48],
[50,51,60,51,58,0,48,53,56,60],
[51,45,51,45,59,52,0,58,46,62],
[41,35,47,55,64,47,42,0,47,56],
[45,28,46,39,59,44,54,53,0,55],
[39,30,42,40,52,40,38,44,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,50,41,64,57,42,43,43,61],
[56,0,53,63,56,53,53,59,42,56],
[50,47,0,45,59,68,49,41,60,52],
[59,37,55,0,57,58,43,44,62,57],
[36,44,41,43,0,48,33,32,51,48],
[43,47,32,42,52,0,42,39,44,52],
[58,47,51,57,67,58,0,57,54,61],
[57,41,59,56,68,61,43,0,62,65],
[57,58,40,38,49,56,46,38,0,56],
[39,44,48,43,52,48,39,35,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,57,37,48,50,40,40,53,49],
[45,0,47,59,40,55,49,38,62,46],
[43,53,0,40,39,56,43,40,56,49],
[63,41,60,0,53,61,50,37,49,40],
[52,60,61,47,0,58,47,51,50,49],
[50,45,44,39,42,0,32,33,47,38],
[60,51,57,50,53,68,0,41,51,48],
[60,62,60,63,49,67,59,0,57,56],
[47,38,44,51,50,53,49,43,0,47],
[51,54,51,60,51,62,52,44,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,39,51,51,33,65,53,49],
[55,0,44,49,48,50,41,54,43,38],
[41,56,0,49,50,64,53,45,60,66],
[61,51,51,0,59,71,48,61,57,62],
[49,52,50,41,0,44,35,47,44,52],
[49,50,36,29,56,0,42,45,39,46],
[67,59,47,52,65,58,0,70,59,55],
[35,46,55,39,53,55,30,0,46,44],
[47,57,40,43,56,61,41,54,0,57],
[51,62,34,38,48,54,45,56,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,63,71,60,55,56,39,70,58],
[35,0,47,48,47,46,46,34,59,26],
[37,53,0,47,52,45,60,19,49,39],
[29,52,53,0,44,35,48,40,65,27],
[40,53,48,56,0,36,42,24,55,38],
[45,54,55,65,64,0,48,29,54,41],
[44,54,40,52,58,52,0,41,57,47],
[61,66,81,60,76,71,59,0,71,47],
[30,41,51,35,45,46,43,29,0,35],
[42,74,61,73,62,59,53,53,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,39,33,47,41,42,55,49,55],
[50,0,37,40,47,48,49,59,72,59],
[61,63,0,33,50,32,42,46,74,50],
[67,60,67,0,53,54,47,74,88,74],
[53,53,50,47,0,43,36,64,65,69],
[59,52,68,46,57,0,51,61,73,64],
[58,51,58,53,64,49,0,79,64,61],
[45,41,54,26,36,39,21,0,49,41],
[51,28,26,12,35,27,36,51,0,41],
[45,41,50,26,31,36,39,59,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,48,55,75,73,72,56,72,76],
[22,0,36,58,38,59,61,61,67,36],
[52,64,0,79,46,68,57,46,62,55],
[45,42,21,0,39,65,50,60,80,64],
[25,62,54,61,0,81,72,53,69,59],
[27,41,32,35,19,0,39,45,61,52],
[28,39,43,50,28,61,0,36,63,38],
[44,39,54,40,47,55,64,0,52,66],
[28,33,38,20,31,39,37,48,0,43],
[24,64,45,36,41,48,62,34,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,40,65,41,43,48,36,36,47],
[48,0,47,67,46,46,44,41,34,42],
[60,53,0,62,48,50,55,47,46,51],
[35,33,38,0,31,32,40,37,33,32],
[59,54,52,69,0,49,59,51,38,51],
[57,54,50,68,51,0,52,43,45,51],
[52,56,45,60,41,48,0,41,38,37],
[64,59,53,63,49,57,59,0,51,58],
[64,66,54,67,62,55,62,49,0,61],
[53,58,49,68,49,49,63,42,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,36,55,46,36,42,40,51,42],
[33,0,40,45,42,39,42,42,41,35],
[64,60,0,52,61,51,52,47,57,50],
[45,55,48,0,42,44,42,32,57,44],
[54,58,39,58,0,45,44,37,50,47],
[64,61,49,56,55,0,52,54,62,49],
[58,58,48,58,56,48,0,45,52,55],
[60,58,53,68,63,46,55,0,67,54],
[49,59,43,43,50,38,48,33,0,38],
[58,65,50,56,53,51,45,46,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,55,35,43,55,55,58,36,56],
[37,0,50,46,38,47,50,44,31,40],
[45,50,0,41,23,47,48,53,38,37],
[65,54,59,0,47,57,51,67,53,60],
[57,62,77,53,0,50,61,58,47,43],
[45,53,53,43,50,0,47,49,41,53],
[45,50,52,49,39,53,0,52,26,40],
[42,56,47,33,42,51,48,0,40,33],
[64,69,62,47,53,59,74,60,0,63],
[44,60,63,40,57,47,60,67,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,54,54,43,53,53,50,43,54],
[54,0,57,59,53,58,53,49,53,53],
[46,43,0,57,44,56,53,45,37,54],
[46,41,43,0,44,51,51,40,38,50],
[57,47,56,56,0,58,57,46,53,55],
[47,42,44,49,42,0,49,46,43,49],
[47,47,47,49,43,51,0,53,41,50],
[50,51,55,60,54,54,47,0,50,65],
[57,47,63,62,47,57,59,50,0,57],
[46,47,46,50,45,51,50,35,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,51,50,59,43,60,57,50],
[55,0,56,55,61,56,49,58,57,46],
[41,44,0,43,51,53,41,44,49,47],
[49,45,57,0,49,52,46,48,52,47],
[50,39,49,51,0,53,41,49,52,40],
[41,44,47,48,47,0,42,45,52,41],
[57,51,59,54,59,58,0,51,56,48],
[40,42,56,52,51,55,49,0,52,49],
[43,43,51,48,48,48,44,48,0,42],
[50,54,53,53,60,59,52,51,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,39,48,52,60,38,53,65,64],
[47,0,23,31,83,42,70,34,47,15],
[61,77,0,47,96,58,50,65,76,76],
[52,69,53,0,69,33,55,52,53,49],
[48,17,4,31,0,29,36,35,47,29],
[40,58,42,67,71,0,57,60,74,49],
[62,30,50,45,64,43,0,52,30,30],
[47,66,35,48,65,40,48,0,78,39],
[35,53,24,47,53,26,70,22,0,44],
[36,85,24,51,71,51,70,61,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,46,50,45,56,49,54,59],
[50,0,53,50,57,48,53,50,54,63],
[51,47,0,48,60,54,56,54,60,53],
[54,50,52,0,60,51,56,47,60,56],
[50,43,40,40,0,41,39,45,57,45],
[55,52,46,49,59,0,54,48,51,54],
[44,47,44,44,61,46,0,47,59,52],
[51,50,46,53,55,52,53,0,62,52],
[46,46,40,40,43,49,41,38,0,45],
[41,37,47,44,55,46,48,48,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,66,97,44,40,34,45,56,63],
[78,0,78,83,83,55,86,49,74,78],
[34,22,0,50,34,16,37,47,48,44],
[3,17,50,0,26,24,3,27,40,27],
[56,17,66,74,0,40,43,29,40,51],
[60,45,84,76,60,0,60,73,81,84],
[66,14,63,97,57,40,0,45,40,74],
[55,51,53,73,71,27,55,0,30,63],
[44,26,52,60,60,19,60,70,0,70],
[37,22,56,73,49,16,26,37,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,41,49,46,51,43,51,51,50],
[59,0,51,53,40,59,42,58,51,55],
[59,49,0,58,43,57,44,45,55,55],
[51,47,42,0,37,41,41,48,46,50],
[54,60,57,63,0,53,50,63,63,57],
[49,41,43,59,47,0,40,53,59,48],
[57,58,56,59,50,60,0,50,53,60],
[49,42,55,52,37,47,50,0,60,56],
[49,49,45,54,37,41,47,40,0,53],
[50,45,45,50,43,52,40,44,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,47,48,47,50,39,50,43,47],
[54,0,42,60,59,64,58,50,41,66],
[53,58,0,57,60,67,42,51,47,58],
[52,40,43,0,46,62,44,52,38,59],
[53,41,40,54,0,51,48,51,56,67],
[50,36,33,38,49,0,38,37,31,48],
[61,42,58,56,52,62,0,52,47,71],
[50,50,49,48,49,63,48,0,34,58],
[57,59,53,62,44,69,53,66,0,63],
[53,34,42,41,33,52,29,42,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,31,46,56,31,38,37,37,48],
[54,0,69,45,76,58,51,40,50,58],
[69,31,0,61,77,55,57,53,31,73],
[54,55,39,0,69,35,57,61,42,57],
[44,24,23,31,0,27,32,42,27,54],
[69,42,45,65,73,0,47,54,53,72],
[62,49,43,43,68,53,0,49,44,61],
[63,60,47,39,58,46,51,0,51,62],
[63,50,69,58,73,47,56,49,0,58],
[52,42,27,43,46,28,39,38,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,38,49,56,51,55,53,54],
[52,0,54,47,46,60,53,65,54,59],
[46,46,0,38,42,51,45,53,50,49],
[62,53,62,0,50,57,52,63,53,55],
[51,54,58,50,0,57,55,58,50,46],
[44,40,49,43,43,0,44,54,44,51],
[49,47,55,48,45,56,0,58,49,52],
[45,35,47,37,42,46,42,0,43,49],
[47,46,50,47,50,56,51,57,0,49],
[46,41,51,45,54,49,48,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,62,40,59,45,49,53,57,45],
[55,0,62,60,55,54,60,49,69,62],
[38,38,0,41,56,31,48,46,47,50],
[60,40,59,0,81,50,63,59,59,44],
[41,45,44,19,0,31,34,36,40,40],
[55,46,69,50,69,0,43,53,67,55],
[51,40,52,37,66,57,0,60,60,48],
[47,51,54,41,64,47,40,0,62,57],
[43,31,53,41,60,33,40,38,0,47],
[55,38,50,56,60,45,52,43,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,56,57,49,52,61,50,49,58],
[40,0,42,53,53,48,57,47,50,50],
[44,58,0,55,54,49,54,43,56,53],
[43,47,45,0,49,44,49,42,47,52],
[51,47,46,51,0,49,57,40,47,43],
[48,52,51,56,51,0,52,51,53,50],
[39,43,46,51,43,48,0,41,47,49],
[50,53,57,58,60,49,59,0,55,57],
[51,50,44,53,53,47,53,45,0,56],
[42,50,47,48,57,50,51,43,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,49,70,54,65,65,68,46,44],
[39,0,36,47,46,47,50,53,35,56],
[51,64,0,72,63,73,51,61,59,44],
[30,53,28,0,36,35,41,54,40,31],
[46,54,37,64,0,46,55,50,43,40],
[35,53,27,65,54,0,48,57,49,45],
[35,50,49,59,45,52,0,42,40,48],
[32,47,39,46,50,43,58,0,38,42],
[54,65,41,60,57,51,60,62,0,50],
[56,44,56,69,60,55,52,58,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,50,52,53,58,47,54,50],
[44,0,48,49,48,47,50,46,51,50],
[54,52,0,60,49,48,46,55,49,51],
[50,51,40,0,41,48,47,48,48,43],
[48,52,51,59,0,59,58,46,50,57],
[47,53,52,52,41,0,51,46,49,48],
[42,50,54,53,42,49,0,46,42,51],
[53,54,45,52,54,54,54,0,53,49],
[46,49,51,52,50,51,58,47,0,53],
[50,50,49,57,43,52,49,51,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,61,55,56,51,38,64,51,51],
[49,0,59,51,48,63,32,53,46,56],
[39,41,0,43,42,47,36,49,42,50],
[45,49,57,0,43,56,34,49,54,56],
[44,52,58,57,0,53,39,51,55,47],
[49,37,53,44,47,0,32,44,36,34],
[62,68,64,66,61,68,0,61,53,50],
[36,47,51,51,49,56,39,0,49,42],
[49,54,58,46,45,64,47,51,0,60],
[49,44,50,44,53,66,50,58,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,64,27,36,72,48,54,49,57],
[45,0,54,50,29,53,57,48,50,62],
[36,46,0,18,40,33,43,33,27,29],
[73,50,82,0,54,57,51,63,55,59],
[64,71,60,46,0,78,68,61,82,65],
[28,47,67,43,22,0,48,54,39,55],
[52,43,57,49,32,52,0,51,49,65],
[46,52,67,37,39,46,49,0,27,46],
[51,50,73,45,18,61,51,73,0,77],
[43,38,71,41,35,45,35,54,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,51,45,43,44,50,49,56,51],
[56,0,47,42,45,53,34,46,49,42],
[49,53,0,45,46,44,49,47,51,47],
[55,58,55,0,56,43,50,51,55,50],
[57,55,54,44,0,50,48,58,54,50],
[56,47,56,57,50,0,51,55,50,54],
[50,66,51,50,52,49,0,54,52,42],
[51,54,53,49,42,45,46,0,52,49],
[44,51,49,45,46,50,48,48,0,50],
[49,58,53,50,50,46,58,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,49,60,48,63,41,23,28],
[53,0,48,40,65,41,53,35,26,45],
[44,52,0,72,62,37,53,16,35,31],
[51,60,28,0,69,37,50,24,42,28],
[40,35,38,31,0,42,53,32,36,25],
[52,59,63,63,58,0,78,37,35,33],
[37,47,47,50,47,22,0,27,38,22],
[59,65,84,76,68,63,73,0,43,44],
[77,74,65,58,64,65,62,57,0,50],
[72,55,69,72,75,67,78,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,62,57,50,57,65,39,36,63],
[35,0,65,55,53,51,40,51,35,70],
[38,35,0,36,37,42,53,45,40,62],
[43,45,64,0,41,52,51,43,53,74],
[50,47,63,59,0,64,51,50,50,58],
[43,49,58,48,36,0,50,40,39,50],
[35,60,47,49,49,50,0,33,36,66],
[61,49,55,57,50,60,67,0,49,65],
[64,65,60,47,50,61,64,51,0,70],
[37,30,38,26,42,50,34,35,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,61,52,56,55,52,57,44,42],
[49,0,65,61,51,54,51,57,58,53],
[39,35,0,38,43,40,44,47,41,38],
[48,39,62,0,51,58,53,52,44,44],
[44,49,57,49,0,46,50,51,44,44],
[45,46,60,42,54,0,47,52,52,41],
[48,49,56,47,50,53,0,56,45,48],
[43,43,53,48,49,48,44,0,42,40],
[56,42,59,56,56,48,55,58,0,42],
[58,47,62,56,56,59,52,60,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,43,48,40,49,55,47,47,49],
[57,0,46,42,45,41,46,46,47,40],
[57,54,0,47,42,51,44,62,68,59],
[52,58,53,0,44,40,45,55,63,42],
[60,55,58,56,0,40,48,59,48,57],
[51,59,49,60,60,0,52,68,56,56],
[45,54,56,55,52,48,0,71,54,48],
[53,54,38,45,41,32,29,0,48,50],
[53,53,32,37,52,44,46,52,0,60],
[51,60,41,58,43,44,52,50,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,40,50,29,32,37,38,34,33],
[69,0,43,68,56,52,50,59,58,46],
[60,57,0,69,55,55,41,59,54,59],
[50,32,31,0,28,44,37,51,43,37],
[71,44,45,72,0,51,52,61,53,39],
[68,48,45,56,49,0,49,50,65,46],
[63,50,59,63,48,51,0,69,53,48],
[62,41,41,49,39,50,31,0,42,40],
[66,42,46,57,47,35,47,58,0,55],
[67,54,41,63,61,54,52,60,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,66,49,39,47,63,49,52],
[47,0,53,54,40,50,41,58,43,46],
[48,47,0,53,36,53,41,52,37,37],
[34,46,47,0,40,53,36,50,34,32],
[51,60,64,60,0,56,51,54,42,47],
[61,50,47,47,44,0,44,64,38,52],
[53,59,59,64,49,56,0,45,55,47],
[37,42,48,50,46,36,55,0,49,57],
[51,57,63,66,58,62,45,51,0,46],
[48,54,63,68,53,48,53,43,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,82,72,56,48,43,44,60,45,47],
[18,0,46,39,37,51,39,60,44,34],
[28,54,0,37,55,51,28,68,25,42],
[44,61,63,0,56,77,70,77,70,69],
[52,63,45,44,0,60,56,72,49,51],
[57,49,49,23,40,0,60,69,57,74],
[56,61,72,30,44,40,0,90,53,44],
[40,40,32,23,28,31,10,0,53,28],
[55,56,75,30,51,43,47,47,0,35],
[53,66,58,31,49,26,56,72,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,52,46,42,47,43,37,44,46],
[62,0,61,67,57,56,64,51,49,66],
[48,39,0,43,39,39,41,40,42,27],
[54,33,57,0,49,42,42,42,45,48],
[58,43,61,51,0,55,38,48,56,57],
[53,44,61,58,45,0,38,47,51,54],
[57,36,59,58,62,62,0,51,46,52],
[63,49,60,58,52,53,49,0,54,62],
[56,51,58,55,44,49,54,46,0,54],
[54,34,73,52,43,46,48,38,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,61,47,52,48,52,56,46],
[43,0,65,43,49,44,36,42,41,50],
[41,35,0,53,53,40,43,38,40,43],
[39,57,47,0,48,34,40,37,40,44],
[53,51,47,52,0,54,45,46,42,52],
[48,56,60,66,46,0,47,41,51,47],
[52,64,57,60,55,53,0,51,46,59],
[48,58,62,63,54,59,49,0,51,50],
[44,59,60,60,58,49,54,49,0,59],
[54,50,57,56,48,53,41,50,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,43,38,47,51,55,52,51],
[48,0,55,55,50,57,47,61,55,60],
[53,45,0,59,51,51,53,68,51,49],
[57,45,41,0,46,59,55,73,48,53],
[62,50,49,54,0,52,60,58,56,53],
[53,43,49,41,48,0,51,57,50,56],
[49,53,47,45,40,49,0,42,48,43],
[45,39,32,27,42,43,58,0,43,47],
[48,45,49,52,44,50,52,57,0,47],
[49,40,51,47,47,44,57,53,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,63,60,52,64,52,63,60,48],
[44,0,52,74,58,65,46,63,50,58],
[37,48,0,67,55,71,55,52,41,50],
[40,26,33,0,48,52,36,39,37,37],
[48,42,45,52,0,53,46,48,52,41],
[36,35,29,48,47,0,41,48,40,41],
[48,54,45,64,54,59,0,50,47,52],
[37,37,48,61,52,52,50,0,55,48],
[40,50,59,63,48,60,53,45,0,54],
[52,42,50,63,59,59,48,52,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,43,56,49,57,53,57,55,50],
[47,0,42,56,53,49,53,57,54,48],
[57,58,0,60,50,58,55,60,55,55],
[44,44,40,0,48,47,51,54,47,52],
[51,47,50,52,0,51,46,50,47,53],
[43,51,42,53,49,0,47,55,48,46],
[47,47,45,49,54,53,0,52,46,50],
[43,43,40,46,50,45,48,0,46,45],
[45,46,45,53,53,52,54,54,0,48],
[50,52,45,48,47,54,50,55,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,53,61,45,57,62,55,49,66],
[37,0,47,49,41,46,45,55,44,51],
[47,53,0,41,49,61,53,61,49,58],
[39,51,59,0,42,53,53,62,51,65],
[55,59,51,58,0,58,49,52,32,57],
[43,54,39,47,42,0,55,57,40,59],
[38,55,47,47,51,45,0,47,52,56],
[45,45,39,38,48,43,53,0,48,66],
[51,56,51,49,68,60,48,52,0,68],
[34,49,42,35,43,41,44,34,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,45,15,61,54,61,61,45,31],
[69,0,30,0,30,39,61,46,45,39],
[55,70,0,16,16,55,31,16,15,55],
[85,100,84,0,46,70,100,100,84,70],
[39,70,84,54,0,54,100,100,84,54],
[46,61,45,30,46,0,61,46,45,16],
[39,39,69,0,0,39,0,16,30,39],
[39,54,84,0,0,54,84,0,84,54],
[55,55,85,16,16,55,70,16,0,55],
[69,61,45,30,46,84,61,46,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,54,33,52,48,42,34,48,45],
[56,0,55,42,56,49,55,59,52,48],
[46,45,0,37,49,47,37,38,54,43],
[67,58,63,0,68,53,59,46,60,50],
[48,44,51,32,0,43,41,42,52,52],
[52,51,53,47,57,0,42,47,56,45],
[58,45,63,41,59,58,0,48,49,52],
[66,41,62,54,58,53,52,0,54,52],
[52,48,46,40,48,44,51,46,0,48],
[55,52,57,50,48,55,48,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,45,60,54,53,52,55,41,55],
[50,0,56,52,58,58,52,54,52,55],
[55,44,0,50,55,54,54,58,46,50],
[40,48,50,0,51,43,45,51,41,43],
[46,42,45,49,0,47,39,43,47,47],
[47,42,46,57,53,0,48,42,40,47],
[48,48,46,55,61,52,0,52,45,42],
[45,46,42,49,57,58,48,0,40,38],
[59,48,54,59,53,60,55,60,0,53],
[45,45,50,57,53,53,58,62,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,51,43,39,40,47,44,53,40],
[58,0,58,53,53,52,54,50,58,55],
[49,42,0,40,41,40,52,42,55,44],
[57,47,60,0,47,55,53,50,56,52],
[61,47,59,53,0,47,58,47,62,56],
[60,48,60,45,53,0,55,37,62,49],
[53,46,48,47,42,45,0,45,52,45],
[56,50,58,50,53,63,55,0,65,58],
[47,42,45,44,38,38,48,35,0,49],
[60,45,56,48,44,51,55,42,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,40,28,31,43,29,40,51,31],
[66,0,51,36,51,54,39,45,70,57],
[60,49,0,38,48,47,40,41,53,51],
[72,64,62,0,70,78,55,49,64,71],
[69,49,52,30,0,66,43,45,67,57],
[57,46,53,22,34,0,37,43,64,57],
[71,61,60,45,57,63,0,62,73,63],
[60,55,59,51,55,57,38,0,46,58],
[49,30,47,36,33,36,27,54,0,46],
[69,43,49,29,43,43,37,42,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,77,50,73,72,53,52,65],
[43,0,43,70,55,57,43,27,45,51],
[52,57,0,67,57,66,62,50,43,55],
[23,30,33,0,30,36,40,24,23,27],
[50,45,43,70,0,48,66,36,46,48],
[27,43,34,64,52,0,56,48,24,39],
[28,57,38,60,34,44,0,42,34,47],
[47,73,50,76,64,52,58,0,47,53],
[48,55,57,77,54,76,66,53,0,58],
[35,49,45,73,52,61,53,47,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,48,55,53,49,49,45,48],
[49,0,59,48,52,54,46,52,50,48],
[50,41,0,46,54,55,46,48,47,48],
[52,52,54,0,58,57,54,55,44,53],
[45,48,46,42,0,49,48,51,53,47],
[47,46,45,43,51,0,45,50,44,47],
[51,54,54,46,52,55,0,48,50,53],
[51,48,52,45,49,50,52,0,49,48],
[55,50,53,56,47,56,50,51,0,58],
[52,52,52,47,53,53,47,52,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,80,80,100,80,45,80,80,80],
[55,0,100,100,55,55,80,55,35,80],
[20,0,0,35,55,35,45,35,35,80],
[20,0,65,0,20,0,45,0,0,45],
[0,45,45,80,0,0,45,45,80,45],
[20,45,65,100,100,0,45,45,80,45],
[55,20,55,55,55,55,0,55,35,55],
[20,45,65,100,55,55,45,0,80,80],
[20,65,65,100,20,20,65,20,0,65],
[20,20,20,55,55,55,45,20,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,39,41,27,32,48,38,42,42],
[65,0,61,52,46,49,57,41,53,56],
[61,39,0,50,38,43,41,46,48,42],
[59,48,50,0,38,46,37,39,44,44],
[73,54,62,62,0,57,61,50,43,53],
[68,51,57,54,43,0,54,51,45,55],
[52,43,59,63,39,46,0,44,49,54],
[62,59,54,61,50,49,56,0,61,52],
[58,47,52,56,57,55,51,39,0,49],
[58,44,58,56,47,45,46,48,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,46,53,51,58,46,48,46,48],
[59,0,54,69,49,57,54,66,51,52],
[54,46,0,75,38,59,50,48,69,50],
[47,31,25,0,31,30,35,38,43,41],
[49,51,62,69,0,67,49,70,69,55],
[42,43,41,70,33,0,55,43,44,42],
[54,46,50,65,51,45,0,55,41,46],
[52,34,52,62,30,57,45,0,49,52],
[54,49,31,57,31,56,59,51,0,46],
[52,48,50,59,45,58,54,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,47,46,51,47,38,54,40,33],
[54,0,51,46,60,62,47,62,43,35],
[53,49,0,35,35,51,44,55,37,43],
[54,54,65,0,57,48,54,67,44,46],
[49,40,65,43,0,47,46,53,43,36],
[53,38,49,52,53,0,40,59,42,38],
[62,53,56,46,54,60,0,60,50,42],
[46,38,45,33,47,41,40,0,37,29],
[60,57,63,56,57,58,50,63,0,50],
[67,65,57,54,64,62,58,71,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,57,50,39,59,57,55,54,51],
[61,0,68,57,50,71,62,66,59,57],
[43,32,0,48,39,47,48,48,37,50],
[50,43,52,0,34,46,50,56,51,53],
[61,50,61,66,0,68,63,63,78,72],
[41,29,53,54,32,0,45,53,51,46],
[43,38,52,50,37,55,0,56,52,59],
[45,34,52,44,37,47,44,0,54,51],
[46,41,63,49,22,49,48,46,0,51],
[49,43,50,47,28,54,41,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,55,56,45,58,38,64,57,54],
[32,0,49,51,44,34,38,47,42,54],
[45,51,0,52,44,19,41,59,41,52],
[44,49,48,0,48,38,37,66,40,62],
[55,56,56,52,0,44,47,57,52,64],
[42,66,81,62,56,0,59,66,48,66],
[62,62,59,63,53,41,0,73,61,62],
[36,53,41,34,43,34,27,0,36,48],
[43,58,59,60,48,52,39,64,0,69],
[46,46,48,38,36,34,38,52,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,58,51,51,63,55,60,54,50],
[38,0,45,41,44,49,50,43,41,36],
[42,55,0,41,46,53,53,45,48,39],
[49,59,59,0,49,56,55,49,55,42],
[49,56,54,51,0,53,53,53,58,45],
[37,51,47,44,47,0,55,46,47,39],
[45,50,47,45,47,45,0,47,55,46],
[40,57,55,51,47,54,53,0,52,44],
[46,59,52,45,42,53,45,48,0,41],
[50,64,61,58,55,61,54,56,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,44,49,38,49,56,41,56,40],
[60,0,50,51,50,50,59,53,51,44],
[56,50,0,55,48,58,54,45,51,49],
[51,49,45,0,55,37,54,38,45,38],
[62,50,52,45,0,47,48,52,59,48],
[51,50,42,63,53,0,46,47,50,43],
[44,41,46,46,52,54,0,42,47,44],
[59,47,55,62,48,53,58,0,61,57],
[44,49,49,55,41,50,53,39,0,36],
[60,56,51,62,52,57,56,43,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,51,56,54,47,43,46,48],
[52,0,55,47,52,52,52,48,53,49],
[50,45,0,47,50,48,50,43,51,47],
[49,53,53,0,52,50,49,45,45,42],
[44,48,50,48,0,49,44,43,43,45],
[46,48,52,50,51,0,48,47,45,49],
[53,48,50,51,56,52,0,49,47,51],
[57,52,57,55,57,53,51,0,51,49],
[54,47,49,55,57,55,53,49,0,50],
[52,51,53,58,55,51,49,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,49,60,55,47,48,52,48,41],
[54,0,39,47,52,41,40,51,45,41],
[51,61,0,58,57,50,42,58,49,50],
[40,53,42,0,48,41,39,49,40,49],
[45,48,43,52,0,43,42,55,39,39],
[53,59,50,59,57,0,50,62,55,52],
[52,60,58,61,58,50,0,45,48,50],
[48,49,42,51,45,38,55,0,37,41],
[52,55,51,60,61,45,52,63,0,42],
[59,59,50,51,61,48,50,59,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,33,0,13,13,13,0,57,37],
[100,0,100,50,63,63,63,67,87,100],
[67,0,0,30,43,13,13,67,87,37],
[100,50,70,0,33,33,33,37,57,70],
[87,37,57,67,0,20,20,67,87,57],
[87,37,87,67,80,0,100,67,87,87],
[87,37,87,67,80,0,0,67,87,57],
[100,33,33,63,33,33,33,0,87,70],
[43,13,13,43,13,13,13,13,0,50],
[63,0,63,30,43,13,43,30,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,56,51,55,53,56,63,61],
[48,0,47,54,49,49,53,51,53,46],
[50,53,0,55,51,53,52,57,57,55],
[44,46,45,0,40,52,51,45,51,52],
[49,51,49,60,0,47,53,51,49,53],
[45,51,47,48,53,0,48,55,51,53],
[47,47,48,49,47,52,0,46,57,50],
[44,49,43,55,49,45,54,0,63,46],
[37,47,43,49,51,49,43,37,0,47],
[39,54,45,48,47,47,50,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,64,62,59,50,60,61,47,58],
[48,0,58,60,45,60,68,57,42,61],
[36,42,0,42,40,34,27,38,36,60],
[38,40,58,0,47,46,53,33,41,49],
[41,55,60,53,0,47,56,40,35,43],
[50,40,66,54,53,0,34,52,51,59],
[40,32,73,47,44,66,0,44,32,57],
[39,43,62,67,60,48,56,0,44,48],
[53,58,64,59,65,49,68,56,0,66],
[42,39,40,51,57,41,43,52,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,46,49,47,40,43,41,38,37],
[45,0,44,45,49,39,33,43,37,42],
[54,56,0,59,58,43,45,45,39,40],
[51,55,41,0,45,46,41,48,38,35],
[53,51,42,55,0,51,42,41,43,51],
[60,61,57,54,49,0,50,45,53,46],
[57,67,55,59,58,50,0,49,58,47],
[59,57,55,52,59,55,51,0,56,49],
[62,63,61,62,57,47,42,44,0,42],
[63,58,60,65,49,54,53,51,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,61,56,53,45,57,50,56,62],
[50,0,50,47,48,49,48,44,44,56],
[39,50,0,55,44,43,49,38,48,54],
[44,53,45,0,44,48,48,42,46,53],
[47,52,56,56,0,52,57,48,54,61],
[55,51,57,52,48,0,50,41,50,57],
[43,52,51,52,43,50,0,40,54,49],
[50,56,62,58,52,59,60,0,56,60],
[44,56,52,54,46,50,46,44,0,59],
[38,44,46,47,39,43,51,40,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,58,48,56,47,51,54,65],
[52,0,50,44,43,55,43,57,57,54],
[46,50,0,48,51,49,42,55,61,54],
[42,56,52,0,47,52,53,58,53,44],
[52,57,49,53,0,69,44,54,58,50],
[44,45,51,48,31,0,43,49,50,42],
[53,57,58,47,56,57,0,56,59,58],
[49,43,45,42,46,51,44,0,47,52],
[46,43,39,47,42,50,41,53,0,57],
[35,46,46,56,50,58,42,48,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,56,54,44,44,44,49,54],
[54,0,37,56,50,48,50,44,48,44],
[58,63,0,71,58,49,57,54,54,61],
[44,44,29,0,50,42,47,47,41,43],
[46,50,42,50,0,44,47,43,43,49],
[56,52,51,58,56,0,58,56,48,49],
[56,50,43,53,53,42,0,40,36,47],
[56,56,46,53,57,44,60,0,49,57],
[51,52,46,59,57,52,64,51,0,56],
[46,56,39,57,51,51,53,43,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,64,63,61,51,36,57,65,48],
[52,0,61,68,41,43,36,55,62,41],
[36,39,0,57,42,43,35,41,53,38],
[37,32,43,0,23,32,30,33,45,39],
[39,59,58,77,0,72,43,54,57,48],
[49,57,57,68,28,0,38,40,60,47],
[64,64,65,70,57,62,0,48,62,46],
[43,45,59,67,46,60,52,0,58,51],
[35,38,47,55,43,40,38,42,0,51],
[52,59,62,61,52,53,54,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,70,45,60,49,55,53,63],
[53,0,59,56,29,43,51,59,58,50],
[46,41,0,45,33,45,44,53,33,50],
[30,44,55,0,30,44,45,45,52,43],
[55,71,67,70,0,55,46,53,68,61],
[40,57,55,56,45,0,44,51,53,45],
[51,49,56,55,54,56,0,45,52,51],
[45,41,47,55,47,49,55,0,58,58],
[47,42,67,48,32,47,48,42,0,54],
[37,50,50,57,39,55,49,42,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,55,59,65,47,57,62,51,64],
[35,0,41,41,56,31,44,42,35,46],
[45,59,0,61,48,50,55,62,38,54],
[41,59,39,0,46,52,44,50,51,49],
[35,44,52,54,0,35,48,39,40,36],
[53,69,50,48,65,0,47,65,57,54],
[43,56,45,56,52,53,0,53,45,50],
[38,58,38,50,61,35,47,0,26,45],
[49,65,62,49,60,43,55,74,0,67],
[36,54,46,51,64,46,50,55,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,55,59,52,52,68,72,52,44],
[32,0,47,63,59,36,52,45,48,47],
[45,53,0,55,65,57,50,54,59,46],
[41,37,45,0,58,40,51,42,65,43],
[48,41,35,42,0,40,43,41,57,29],
[48,64,43,60,60,0,63,64,54,47],
[32,48,50,49,57,37,0,50,48,49],
[28,55,46,58,59,36,50,0,44,50],
[48,52,41,35,43,46,52,56,0,41],
[56,53,54,57,71,53,51,50,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,60,53,48,50,48,50,45,58],
[50,0,54,45,43,44,43,41,46,47],
[40,46,0,47,44,52,46,51,53,50],
[47,55,53,0,46,53,40,46,49,51],
[52,57,56,54,0,56,46,41,51,59],
[50,56,48,47,44,0,41,43,46,52],
[52,57,54,60,54,59,0,46,55,58],
[50,59,49,54,59,57,54,0,56,56],
[55,54,47,51,49,54,45,44,0,51],
[42,53,50,49,41,48,42,44,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,55,48,58,51,57,57,52],
[51,0,49,56,48,57,51,58,48,49],
[55,51,0,61,50,58,55,61,59,53],
[45,44,39,0,48,52,52,53,49,49],
[52,52,50,52,0,54,50,60,60,53],
[42,43,42,48,46,0,45,47,54,46],
[49,49,45,48,50,55,0,55,57,47],
[43,42,39,47,40,53,45,0,52,47],
[43,52,41,51,40,46,43,48,0,52],
[48,51,47,51,47,54,53,53,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,51,47,52,47,51,45,54,48],
[52,0,41,46,54,45,48,52,49,48],
[49,59,0,54,51,49,50,53,45,54],
[53,54,46,0,56,44,40,47,49,50],
[48,46,49,44,0,37,43,46,44,43],
[53,55,51,56,63,0,47,55,48,57],
[49,52,50,60,57,53,0,52,50,51],
[55,48,47,53,54,45,48,0,51,47],
[46,51,55,51,56,52,50,49,0,52],
[52,52,46,50,57,43,49,53,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,47,49,43,43,53,42,48],
[53,0,53,51,46,53,51,51,45,46],
[42,47,0,47,45,46,46,51,44,43],
[53,49,53,0,48,48,57,51,50,51],
[51,54,55,52,0,48,48,56,50,51],
[57,47,54,52,52,0,48,57,49,47],
[57,49,54,43,52,52,0,53,54,48],
[47,49,49,49,44,43,47,0,39,49],
[58,55,56,50,50,51,46,61,0,50],
[52,54,57,49,49,53,52,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,42,49,48,38,45,34,47,45],
[58,0,60,51,56,51,51,49,66,67],
[58,40,0,51,48,41,59,43,59,57],
[51,49,49,0,53,38,51,52,58,54],
[52,44,52,47,0,37,37,47,59,59],
[62,49,59,62,63,0,55,52,64,57],
[55,49,41,49,63,45,0,41,54,53],
[66,51,57,48,53,48,59,0,65,63],
[53,34,41,42,41,36,46,35,0,52],
[55,33,43,46,41,43,47,37,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,53,53,45,52,40,50,45],
[47,0,49,54,59,47,49,50,53,51],
[52,51,0,47,50,45,50,51,48,47],
[47,46,53,0,52,40,43,47,45,40],
[47,41,50,48,0,43,49,48,46,50],
[55,53,55,60,57,0,54,43,47,52],
[48,51,50,57,51,46,0,45,46,53],
[60,50,49,53,52,57,55,0,50,50],
[50,47,52,55,54,53,54,50,0,59],
[55,49,53,60,50,48,47,50,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,52,58,51,43,45,48,48],
[51,0,40,55,52,56,48,48,55,44],
[59,60,0,58,62,53,50,60,58,55],
[48,45,42,0,48,49,47,39,53,45],
[42,48,38,52,0,44,37,47,49,44],
[49,44,47,51,56,0,46,53,50,44],
[57,52,50,53,63,54,0,59,58,57],
[55,52,40,61,53,47,41,0,48,50],
[52,45,42,47,51,50,42,52,0,40],
[52,56,45,55,56,56,43,50,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,57,56,58,52,63,42,55,46],
[41,0,43,53,50,55,47,45,48,35],
[43,57,0,56,58,57,57,46,47,47],
[44,47,44,0,45,51,57,50,39,53],
[42,50,42,55,0,60,50,30,39,50],
[48,45,43,49,40,0,36,38,40,37],
[37,53,43,43,50,64,0,43,41,57],
[58,55,54,50,70,62,57,0,51,60],
[45,52,53,61,61,60,59,49,0,47],
[54,65,53,47,50,63,43,40,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,57,44,54,56,48,53,50],
[55,0,56,56,48,54,56,53,45,51],
[53,44,0,56,50,57,53,50,44,51],
[43,44,44,0,46,56,50,52,51,46],
[56,52,50,54,0,59,54,55,50,49],
[46,46,43,44,41,0,47,44,50,43],
[44,44,47,50,46,53,0,50,48,46],
[52,47,50,48,45,56,50,0,49,46],
[47,55,56,49,50,50,52,51,0,47],
[50,49,49,54,51,57,54,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,39,43,63,39,33,45,46,39],
[63,0,39,41,53,42,34,53,50,43],
[61,61,0,55,61,47,50,64,64,58],
[57,59,45,0,63,52,51,49,57,48],
[37,47,39,37,0,28,37,39,45,37],
[61,58,53,48,72,0,55,53,63,57],
[67,66,50,49,63,45,0,51,57,46],
[55,47,36,51,61,47,49,0,51,60],
[54,50,36,43,55,37,43,49,0,50],
[61,57,42,52,63,43,54,40,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,57,62,47,54,45,49,52,51],
[49,0,60,56,46,53,52,56,55,48],
[43,40,0,54,40,52,44,42,51,46],
[38,44,46,0,35,53,38,46,43,44],
[53,54,60,65,0,59,49,60,55,49],
[46,47,48,47,41,0,44,48,50,38],
[55,48,56,62,51,56,0,55,54,52],
[51,44,58,54,40,52,45,0,51,50],
[48,45,49,57,45,50,46,49,0,41],
[49,52,54,56,51,62,48,50,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,47,43,43,42,41,42,53],
[51,0,45,50,47,47,53,49,43,51],
[59,55,0,54,50,51,51,49,53,59],
[53,50,46,0,42,42,49,50,49,51],
[57,53,50,58,0,48,50,46,47,59],
[57,53,49,58,52,0,56,50,51,61],
[58,47,49,51,50,44,0,49,47,56],
[59,51,51,50,54,50,51,0,53,63],
[58,57,47,51,53,49,53,47,0,52],
[47,49,41,49,41,39,44,37,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,56,49,55,48,44,49,58],
[43,0,41,45,47,44,42,42,39,48],
[52,59,0,60,47,47,40,49,46,60],
[44,55,40,0,45,49,40,39,44,58],
[51,53,53,55,0,49,41,50,48,68],
[45,56,53,51,51,0,40,48,52,53],
[52,58,60,60,59,60,0,57,50,65],
[56,58,51,61,50,52,43,0,51,57],
[51,61,54,56,52,48,50,49,0,61],
[42,52,40,42,32,47,35,43,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,49,48,44,46,44,65,50,55],
[42,0,56,51,48,48,53,52,48,44],
[51,44,0,40,42,48,36,48,53,49],
[52,49,60,0,43,43,47,59,49,50],
[56,52,58,57,0,55,52,59,47,45],
[54,52,52,57,45,0,48,66,58,44],
[56,47,64,53,48,52,0,62,46,59],
[35,48,52,41,41,34,38,0,32,43],
[50,52,47,51,53,42,54,68,0,59],
[45,56,51,50,55,56,41,57,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,60,46,58,48,43,49,45,50],
[53,0,58,39,49,38,41,41,49,39],
[40,42,0,45,40,31,51,39,37,36],
[54,61,55,0,64,45,58,48,47,52],
[42,51,60,36,0,41,48,41,45,44],
[52,62,69,55,59,0,60,47,55,42],
[57,59,49,42,52,40,0,49,46,43],
[51,59,61,52,59,53,51,0,54,50],
[55,51,63,53,55,45,54,46,0,45],
[50,61,64,48,56,58,57,50,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,44,51,58,46,56,51,53,47],
[53,0,37,50,46,50,50,46,49,43],
[56,63,0,53,59,52,50,60,55,49],
[49,50,47,0,53,45,55,53,57,47],
[42,54,41,47,0,52,61,53,54,46],
[54,50,48,55,48,0,53,51,47,51],
[44,50,50,45,39,47,0,49,47,53],
[49,54,40,47,47,49,51,0,51,40],
[47,51,45,43,46,53,53,49,0,54],
[53,57,51,53,54,49,47,60,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,49,39,45,43,31,41,44],
[46,0,58,47,37,47,34,45,35,36],
[49,42,0,56,43,44,40,52,49,45],
[51,53,44,0,45,46,24,41,32,43],
[61,63,57,55,0,61,40,63,52,58],
[55,53,56,54,39,0,54,44,51,44],
[57,66,60,76,60,46,0,50,52,45],
[69,55,48,59,37,56,50,0,44,36],
[59,65,51,68,48,49,48,56,0,52],
[56,64,55,57,42,56,55,64,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,48,44,49,49,37,42,44,48],
[60,0,52,55,57,54,56,49,53,57],
[52,48,0,57,61,51,52,55,54,48],
[56,45,43,0,51,47,43,50,51,38],
[51,43,39,49,0,42,39,45,53,33],
[51,46,49,53,58,0,55,49,46,50],
[63,44,48,57,61,45,0,47,55,52],
[58,51,45,50,55,51,53,0,50,46],
[56,47,46,49,47,54,45,50,0,52],
[52,43,52,62,67,50,48,54,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,53,62,28,66,54,54,49,57],
[38,0,46,50,36,63,48,35,51,70],
[47,54,0,59,34,57,31,45,41,65],
[38,50,41,0,31,69,45,41,34,73],
[72,64,66,69,0,80,63,50,50,73],
[34,37,43,31,20,0,37,37,23,49],
[46,52,69,55,37,63,0,32,44,55],
[46,65,55,59,50,63,68,0,57,80],
[51,49,59,66,50,77,56,43,0,78],
[43,30,35,27,27,51,45,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,54,52,54,66,62,64,51],
[51,0,42,40,46,41,54,51,58,51],
[47,58,0,56,67,49,68,49,50,48],
[46,60,44,0,58,62,52,50,59,51],
[48,54,33,42,0,38,56,36,46,42],
[46,59,51,38,62,0,56,52,56,46],
[34,46,32,48,44,44,0,48,57,29],
[38,49,51,50,64,48,52,0,70,48],
[36,42,50,41,54,44,43,30,0,49],
[49,49,52,49,58,54,71,52,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,53,55,53,52,60,56,50],
[49,0,50,53,49,48,50,54,48,47],
[47,50,0,45,49,51,44,55,52,47],
[47,47,55,0,51,53,49,62,53,52],
[45,51,51,49,0,54,47,58,46,51],
[47,52,49,47,46,0,47,54,50,55],
[48,50,56,51,53,53,0,59,51,48],
[40,46,45,38,42,46,41,0,48,44],
[44,52,48,47,54,50,49,52,0,49],
[50,53,53,48,49,45,52,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,56,54,55,50,53,58,46,47],
[57,0,55,55,54,50,51,56,43,52],
[44,45,0,47,51,45,47,43,43,51],
[46,45,53,0,53,52,51,53,40,48],
[45,46,49,47,0,52,50,56,40,56],
[50,50,55,48,48,0,50,55,50,51],
[47,49,53,49,50,50,0,54,42,51],
[42,44,57,47,44,45,46,0,47,47],
[54,57,57,60,60,50,58,53,0,61],
[53,48,49,52,44,49,49,53,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,43,46,49,55,47,53,47,54],
[43,0,43,48,43,53,45,46,44,47],
[57,57,0,54,52,61,52,60,56,50],
[54,52,46,0,51,53,54,54,52,53],
[51,57,48,49,0,57,54,53,52,54],
[45,47,39,47,43,0,49,52,48,48],
[53,55,48,46,46,51,0,52,46,47],
[47,54,40,46,47,48,48,0,48,49],
[53,56,44,48,48,52,54,52,0,50],
[46,53,50,47,46,52,53,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,49,51,49,44,53,47,42],
[50,0,48,51,53,56,49,56,48,45],
[52,52,0,47,56,50,49,60,52,50],
[51,49,53,0,61,60,55,61,50,51],
[49,47,44,39,0,52,45,58,47,47],
[51,44,50,40,48,0,48,48,44,48],
[56,51,51,45,55,52,0,55,48,45],
[47,44,40,39,42,52,45,0,36,44],
[53,52,48,50,53,56,52,64,0,53],
[58,55,50,49,53,52,55,56,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,52,35,37,54,21,53,51,73],
[62,0,71,46,31,63,47,73,49,68],
[48,29,0,46,26,43,56,68,46,63],
[65,54,54,0,61,48,52,56,52,64],
[63,69,74,39,0,70,60,71,74,58],
[46,37,57,52,30,0,41,55,45,48],
[79,53,44,48,40,59,0,78,56,63],
[47,27,32,44,29,45,22,0,36,32],
[49,51,54,48,26,55,44,64,0,51],
[27,32,37,36,42,52,37,68,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,68,39,60,43,51,57,58,40],
[45,0,70,50,70,71,63,68,75,47],
[32,30,0,35,52,31,35,24,40,37],
[61,50,65,0,38,63,38,63,57,43],
[40,30,48,62,0,37,35,43,45,34],
[57,29,69,37,63,0,55,68,74,49],
[49,37,65,62,65,45,0,57,54,71],
[43,32,76,37,57,32,43,0,52,36],
[42,25,60,43,55,26,46,48,0,45],
[60,53,63,57,66,51,29,64,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,77,85,44,48,48,89,59,63,36],
[23,0,45,21,49,37,37,36,51,37],
[15,55,0,29,36,24,37,44,51,46],
[56,79,71,0,60,48,76,71,37,34],
[52,51,64,40,0,55,58,66,31,35],
[52,63,76,52,45,0,72,66,43,47],
[11,63,63,24,42,28,0,39,61,46],
[41,64,56,29,34,34,61,0,22,22],
[37,49,49,63,69,57,39,78,0,61],
[64,63,54,66,65,53,54,78,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,66,52,58,54,55,60,47,66],
[51,0,51,39,54,54,51,52,60,64],
[34,49,0,49,53,38,41,55,53,44],
[48,61,51,0,57,55,52,52,62,62],
[42,46,47,43,0,45,44,55,55,58],
[46,46,62,45,55,0,45,55,52,64],
[45,49,59,48,56,55,0,55,50,59],
[40,48,45,48,45,45,45,0,55,56],
[53,40,47,38,45,48,50,45,0,66],
[34,36,56,38,42,36,41,44,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,71,59,66,31,39,37,66,45],
[44,0,31,37,19,21,34,16,31,31],
[29,69,0,37,43,12,32,15,55,18],
[41,63,63,0,54,31,40,29,61,12],
[34,81,57,46,0,18,45,20,46,33],
[69,79,88,69,82,0,80,43,91,56],
[61,66,68,60,55,20,0,43,67,66],
[63,84,85,71,80,57,57,0,97,42],
[34,69,45,39,54,9,33,3,0,21],
[55,69,82,88,67,44,34,58,79,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,34,42,55,44,26,46,45,56],
[47,0,52,39,38,35,26,43,31,45],
[66,48,0,59,49,40,32,44,45,58],
[58,61,41,0,55,45,45,43,46,45],
[45,62,51,45,0,41,44,55,29,50],
[56,65,60,55,59,0,55,63,49,57],
[74,74,68,55,56,45,0,61,51,55],
[54,57,56,57,45,37,39,0,40,56],
[55,69,55,54,71,51,49,60,0,59],
[44,55,42,55,50,43,45,44,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,44,42,46,54,45,51,42,43],
[54,0,58,53,43,62,52,55,50,50],
[56,42,0,48,49,57,45,52,50,53],
[58,47,52,0,44,57,49,53,43,49],
[54,57,51,56,0,63,47,56,58,58],
[46,38,43,43,37,0,36,41,48,45],
[55,48,55,51,53,64,0,57,56,49],
[49,45,48,47,44,59,43,0,54,46],
[58,50,50,57,42,52,44,46,0,52],
[57,50,47,51,42,55,51,54,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,31,58,41,55,43,40,40,50],
[61,0,34,48,37,47,57,37,46,41],
[69,66,0,65,51,53,58,50,57,55],
[42,52,35,0,50,40,41,36,35,51],
[59,63,49,50,0,54,53,55,55,44],
[45,53,47,60,46,0,31,44,41,49],
[57,43,42,59,47,69,0,39,51,57],
[60,63,50,64,45,56,61,0,57,68],
[60,54,43,65,45,59,49,43,0,66],
[50,59,45,49,56,51,43,32,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,49,56,44,39,56,43,43,45],
[60,0,44,53,42,61,60,54,44,45],
[51,56,0,55,53,51,59,49,52,53],
[44,47,45,0,48,47,61,45,48,38],
[56,58,47,52,0,57,62,52,47,47],
[61,39,49,53,43,0,49,42,43,43],
[44,40,41,39,38,51,0,39,50,45],
[57,46,51,55,48,58,61,0,52,40],
[57,56,48,52,53,57,50,48,0,44],
[55,55,47,62,53,57,55,60,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,52,50,53,50,47,43,49,55],
[59,0,47,59,53,58,51,51,59,57],
[48,53,0,50,51,58,46,48,49,52],
[50,41,50,0,48,45,54,46,51,59],
[47,47,49,52,0,51,52,44,49,57],
[50,42,42,55,49,0,51,50,53,55],
[53,49,54,46,48,49,0,47,53,53],
[57,49,52,54,56,50,53,0,56,59],
[51,41,51,49,51,47,47,44,0,49],
[45,43,48,41,43,45,47,41,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,45,36,35,34,49,47,36,57],
[61,0,53,51,52,66,58,57,43,64],
[55,47,0,44,52,51,53,58,57,60],
[64,49,56,0,50,63,58,53,52,58],
[65,48,48,50,0,58,57,47,51,60],
[66,34,49,37,42,0,41,52,36,63],
[51,42,47,42,43,59,0,40,35,48],
[53,43,42,47,53,48,60,0,40,61],
[64,57,43,48,49,64,65,60,0,67],
[43,36,40,42,40,37,52,39,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,41,33,32,48,36,30,60,43],
[75,0,58,52,61,47,55,55,68,65],
[59,42,0,37,44,39,40,49,65,47],
[67,48,63,0,56,57,62,53,68,54],
[68,39,56,44,0,46,67,39,63,51],
[52,53,61,43,54,0,56,50,64,64],
[64,45,60,38,33,44,0,42,59,46],
[70,45,51,47,61,50,58,0,68,66],
[40,32,35,32,37,36,41,32,0,38],
[57,35,53,46,49,36,54,34,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,51,48,45,51,56,59,50],
[50,0,60,36,45,59,63,53,65,53],
[49,40,0,40,52,40,55,43,58,41],
[49,64,60,0,52,47,69,57,63,50],
[52,55,48,48,0,43,55,49,55,44],
[55,41,60,53,57,0,50,50,58,48],
[49,37,45,31,45,50,0,42,52,48],
[44,47,57,43,51,50,58,0,60,54],
[41,35,42,37,45,42,48,40,0,34],
[50,47,59,50,56,52,52,46,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,21,56,56,56,51,3,56],
[49,0,43,40,63,47,43,73,43,40],
[44,57,0,34,57,62,60,39,19,57],
[79,60,66,0,51,67,65,42,54,69],
[44,37,43,49,0,44,49,38,38,62],
[44,53,38,33,56,0,56,26,15,56],
[44,57,40,35,51,44,0,30,35,56],
[49,27,61,58,62,74,70,0,43,67],
[97,57,81,46,62,85,65,57,0,69],
[44,60,43,31,38,44,44,33,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,60,61,30,38,46,61,64,52],
[59,0,60,64,53,41,49,52,65,57],
[40,40,0,47,43,37,33,30,52,53],
[39,36,53,0,38,59,43,49,58,62],
[70,47,57,62,0,52,51,48,75,62],
[62,59,63,41,48,0,43,58,66,57],
[54,51,67,57,49,57,0,50,66,53],
[39,48,70,51,52,42,50,0,58,67],
[36,35,48,42,25,34,34,42,0,51],
[48,43,47,38,38,43,47,33,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,54,54,62,50,60,66,52,51],
[38,0,57,53,59,57,51,67,48,46],
[46,43,0,48,54,57,55,49,65,49],
[46,47,52,0,69,54,55,57,41,58],
[38,41,46,31,0,38,49,50,41,37],
[50,43,43,46,62,0,61,52,50,44],
[40,49,45,45,51,39,0,48,49,54],
[34,33,51,43,50,48,52,0,39,52],
[48,52,35,59,59,50,51,61,0,58],
[49,54,51,42,63,56,46,48,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,73,51,44,44,39,48,47,45],
[55,0,61,41,47,38,51,53,52,53],
[27,39,0,41,50,51,42,39,55,45],
[49,59,59,0,44,29,37,54,55,47],
[56,53,50,56,0,57,51,49,58,46],
[56,62,49,71,43,0,53,47,64,58],
[61,49,58,63,49,47,0,51,62,48],
[52,47,61,46,51,53,49,0,61,33],
[53,48,45,45,42,36,38,39,0,48],
[55,47,55,53,54,42,52,67,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,43,46,40,33,28,51,43,37],
[58,0,43,46,56,36,53,59,50,38],
[57,57,0,61,58,38,38,52,53,40],
[54,54,39,0,29,45,29,49,50,38],
[60,44,42,71,0,28,50,64,52,46],
[67,64,62,55,72,0,55,74,54,46],
[72,47,62,71,50,45,0,80,59,62],
[49,41,48,51,36,26,20,0,47,31],
[57,50,47,50,48,46,41,53,0,39],
[63,62,60,62,54,54,38,69,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,38,37,43,40,51,56,38,44],
[66,0,64,60,64,63,61,65,50,60],
[62,36,0,51,57,45,53,57,43,56],
[63,40,49,0,59,53,58,61,52,54],
[57,36,43,41,0,41,59,52,43,44],
[60,37,55,47,59,0,58,52,40,48],
[49,39,47,42,41,42,0,53,46,51],
[44,35,43,39,48,48,47,0,40,47],
[62,50,57,48,57,60,54,60,0,63],
[56,40,44,46,56,52,49,53,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,88,64,77,40,69,71,69,67],
[42,0,58,49,67,32,34,57,44,52],
[12,42,0,39,44,42,40,58,55,51],
[36,51,61,0,49,61,58,66,46,76],
[23,33,56,51,0,38,28,39,48,54],
[60,68,58,39,62,0,69,76,62,81],
[31,66,60,42,72,31,0,60,46,63],
[29,43,42,34,61,24,40,0,46,68],
[31,56,45,54,52,38,54,54,0,43],
[33,48,49,24,46,19,37,32,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,41,50,56,48,47,46,52,63],
[57,0,51,51,46,56,55,44,47,59],
[59,49,0,53,52,53,61,50,47,56],
[50,49,47,0,55,46,54,54,44,62],
[44,54,48,45,0,47,45,47,46,55],
[52,44,47,54,53,0,53,49,46,61],
[53,45,39,46,55,47,0,48,44,45],
[54,56,50,46,53,51,52,0,50,61],
[48,53,53,56,54,54,56,50,0,59],
[37,41,44,38,45,39,55,39,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,60,54,56,37,61,64,55,77],
[48,0,57,58,55,54,63,63,46,78],
[40,43,0,40,68,33,45,35,40,57],
[46,42,60,0,72,56,54,48,38,72],
[44,45,32,28,0,43,46,44,35,60],
[63,46,67,44,57,0,64,62,45,63],
[39,37,55,46,54,36,0,41,39,59],
[36,37,65,52,56,38,59,0,34,70],
[45,54,60,62,65,55,61,66,0,83],
[23,22,43,28,40,37,41,30,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,52,52,55,52,45,52,42],
[50,0,54,49,58,57,49,55,58,49],
[45,46,0,51,47,49,47,42,52,50],
[48,51,49,0,56,53,52,47,56,47],
[48,42,53,44,0,61,41,42,54,48],
[45,43,51,47,39,0,41,34,55,40],
[48,51,53,48,59,59,0,50,47,44],
[55,45,58,53,58,66,50,0,61,56],
[48,42,48,44,46,45,53,39,0,44],
[58,51,50,53,52,60,56,44,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,59,43,54,71,37,53,58,47],
[40,0,55,21,44,65,37,35,47,38],
[41,45,0,23,42,78,22,44,45,37],
[57,79,77,0,69,74,53,64,63,48],
[46,56,58,31,0,68,53,50,71,45],
[29,35,22,26,32,0,38,45,46,35],
[63,63,78,47,47,62,0,72,68,55],
[47,65,56,36,50,55,28,0,53,41],
[42,53,55,37,29,54,32,47,0,34],
[53,62,63,52,55,65,45,59,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,54,50,57,53,53,40,44],
[51,0,49,43,34,47,48,47,40,46],
[49,51,0,45,42,50,49,44,42,50],
[46,57,55,0,44,47,52,56,53,46],
[50,66,58,56,0,60,59,55,53,60],
[43,53,50,53,40,0,49,44,42,44],
[47,52,51,48,41,51,0,54,51,41],
[47,53,56,44,45,56,46,0,46,51],
[60,60,58,47,47,58,49,54,0,48],
[56,54,50,54,40,56,59,49,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 100, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_100.csv", index=False, header=False)