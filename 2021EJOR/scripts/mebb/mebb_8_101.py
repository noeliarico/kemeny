
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,60,54,49,56,56,54,52],
[41,0,44,57,43,56,37,42],
[47,57,0,57,55,58,48,50],
[52,44,44,0,40,52,41,36],
[45,58,46,61,0,63,49,57],
[45,45,43,49,38,0,35,36],
[47,64,53,60,52,66,0,48],
[49,59,51,65,44,65,53,0]])



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
result = np.append(np.array([8, 101, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,39,42,47,51,44,36],
[61,0,61,67,50,68,65,66],
[62,40,0,52,52,56,44,47],
[59,34,49,0,35,65,58,47],
[54,51,49,66,0,71,63,62],
[50,33,45,36,30,0,49,48],
[57,36,57,43,38,52,0,49],
[65,35,54,54,39,53,52,0]])



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
result = np.append(np.array([8, 101, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,49,46,57,53,57],
[51,0,45,48,55,49,50,51],
[52,56,0,50,56,58,57,50],
[52,53,51,0,52,51,49,54],
[55,46,45,49,0,49,52,47],
[44,52,43,50,52,0,53,58],
[48,51,44,52,49,48,0,46],
[44,50,51,47,54,43,55,0]])



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
result = np.append(np.array([8, 101, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,46,60,45,70,54,64],
[55,0,36,34,43,55,36,38],
[55,65,0,44,34,50,40,47],
[41,67,57,0,45,50,71,61],
[56,58,67,56,0,64,50,56],
[31,46,51,51,37,0,43,58],
[47,65,61,30,51,58,0,42],
[37,63,54,40,45,43,59,0]])



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
result = np.append(np.array([8, 101, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,51,45,58,51,50,53],
[48,0,54,49,55,56,59,53],
[50,47,0,52,45,50,55,55],
[56,52,49,0,49,48,47,51],
[43,46,56,52,0,49,53,57],
[50,45,51,53,52,0,51,45],
[51,42,46,54,48,50,0,54],
[48,48,46,50,44,56,47,0]])



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
result = np.append(np.array([8, 101, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,48,54,64,57,55],
[56,0,72,51,60,52,48,57],
[42,29,0,41,55,53,35,39],
[53,50,60,0,63,62,47,55],
[47,41,46,38,0,47,41,47],
[37,49,48,39,54,0,34,33],
[44,53,66,54,60,67,0,60],
[46,44,62,46,54,68,41,0]])



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
result = np.append(np.array([8, 101, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,68,41,59,47,56],
[48,0,56,55,46,57,44,59],
[51,45,0,53,57,51,40,51],
[33,46,48,0,48,42,42,42],
[60,55,44,53,0,57,52,45],
[42,44,50,59,44,0,40,52],
[54,57,61,59,49,61,0,53],
[45,42,50,59,56,49,48,0]])



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
result = np.append(np.array([8, 101, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,56,65,50,58,65],
[45,0,35,42,56,34,37,59],
[50,66,0,46,61,46,55,67],
[45,59,55,0,65,50,50,69],
[36,45,40,36,0,35,37,61],
[51,67,55,51,66,0,47,69],
[43,64,46,51,64,54,0,70],
[36,42,34,32,40,32,31,0]])



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
result = np.append(np.array([8, 101, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,57,50,51,66,48,62],
[50,0,37,58,62,54,50,57],
[44,64,0,61,58,70,54,63],
[51,43,40,0,51,62,42,54],
[50,39,43,50,0,44,54,51],
[35,47,31,39,57,0,48,54],
[53,51,47,59,47,53,0,61],
[39,44,38,47,50,47,40,0]])



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
result = np.append(np.array([8, 101, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,46,43,43,47,49],
[56,0,47,48,39,41,45,59],
[56,54,0,51,47,43,42,52],
[55,53,50,0,41,42,45,44],
[58,62,54,60,0,57,63,48],
[58,60,58,59,44,0,57,56],
[54,56,59,56,38,44,0,53],
[52,42,49,57,53,45,48,0]])



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
result = np.append(np.array([8, 101, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,52,54,52,48,56],
[49,0,60,57,59,48,54,50],
[48,41,0,41,49,50,44,42],
[49,44,60,0,49,53,52,49],
[47,42,52,52,0,46,51,52],
[49,53,51,48,55,0,52,51],
[53,47,57,49,50,49,0,48],
[45,51,59,52,49,50,53,0]])



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
result = np.append(np.array([8, 101, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,55,57,64,44,64,62],
[39,0,35,36,51,32,41,42],
[46,66,0,85,66,53,67,70],
[44,65,16,0,46,37,54,49],
[37,50,35,55,0,50,51,51],
[57,69,48,64,51,0,74,49],
[37,60,34,47,50,27,0,41],
[39,59,31,52,50,52,60,0]])



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
result = np.append(np.array([8, 101, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,52,48,49,52,57,53],
[45,0,47,44,49,58,56,52],
[49,54,0,51,54,63,58,49],
[53,57,50,0,52,46,49,52],
[52,52,47,49,0,51,57,51],
[49,43,38,55,50,0,56,45],
[44,45,43,52,44,45,0,45],
[48,49,52,49,50,56,56,0]])



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
result = np.append(np.array([8, 101, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,37,44,39,43,40,33],
[46,0,52,40,33,48,39,41],
[64,49,0,63,53,62,47,54],
[57,61,38,0,45,47,53,38],
[62,68,48,56,0,51,51,51],
[58,53,39,54,50,0,40,38],
[61,62,54,48,50,61,0,49],
[68,60,47,63,50,63,52,0]])



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
result = np.append(np.array([8, 101, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,60,72,61,58,30,58],
[34,0,44,66,61,42,23,45],
[41,57,0,58,68,54,57,64],
[29,35,43,0,52,48,35,30],
[40,40,33,49,0,31,17,34],
[43,59,47,53,70,0,32,55],
[71,78,44,66,84,69,0,41],
[43,56,37,71,67,46,60,0]])



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
result = np.append(np.array([8, 101, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,49,46,53,57,61],
[50,0,52,45,51,46,55,48],
[45,49,0,51,52,56,53,53],
[52,56,50,0,48,49,47,41],
[55,50,49,53,0,53,52,49],
[48,55,45,52,48,0,50,49],
[44,46,48,54,49,51,0,54],
[40,53,48,60,52,52,47,0]])



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
result = np.append(np.array([8, 101, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,38,53,47,51,45,51],
[59,0,57,46,52,53,48,46],
[63,44,0,44,44,41,40,46],
[48,55,57,0,47,45,47,46],
[54,49,57,54,0,59,53,47],
[50,48,60,56,42,0,51,45],
[56,53,61,54,48,50,0,44],
[50,55,55,55,54,56,57,0]])



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
result = np.append(np.array([8, 101, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,77,29,65,34,43,56],
[74,0,69,49,89,59,77,61],
[24,32,0,23,65,16,39,35],
[72,52,78,0,89,36,59,63],
[36,12,36,12,0,7,24,47],
[67,42,85,65,94,0,74,51],
[58,24,62,42,77,27,0,47],
[45,40,66,38,54,50,54,0]])



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
result = np.append(np.array([8, 101, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,53,48,58,53,48,59],
[42,0,42,50,48,48,52,47],
[48,59,0,53,43,50,61,52],
[53,51,48,0,57,40,51,57],
[43,53,58,44,0,47,44,53],
[48,53,51,61,54,0,52,63],
[53,49,40,50,57,49,0,52],
[42,54,49,44,48,38,49,0]])



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
result = np.append(np.array([8, 101, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,43,37,57,40,50,46],
[41,0,13,35,20,20,18,29],
[58,88,0,52,27,50,40,61],
[64,66,49,0,25,38,40,56],
[44,81,74,76,0,51,61,74],
[61,81,51,63,50,0,55,46],
[51,83,61,61,40,46,0,61],
[55,72,40,45,27,55,40,0]])



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
result = np.append(np.array([8, 101, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,41,50,45,54,47,45],
[46,0,47,50,45,47,54,44],
[60,54,0,55,57,49,57,44],
[51,51,46,0,53,38,44,37],
[56,56,44,48,0,40,39,43],
[47,54,52,63,61,0,57,54],
[54,47,44,57,62,44,0,49],
[56,57,57,64,58,47,52,0]])



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
result = np.append(np.array([8, 101, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,44,41,44,36,42,44],
[63,0,51,54,48,46,52,55],
[57,50,0,55,49,47,47,49],
[60,47,46,0,44,51,44,50],
[57,53,52,57,0,44,49,49],
[65,55,54,50,57,0,48,48],
[59,49,54,57,52,53,0,52],
[57,46,52,51,52,53,49,0]])



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
result = np.append(np.array([8, 101, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,59,43,60,46,52,46],
[46,0,56,40,55,44,48,38],
[42,45,0,35,46,37,46,34],
[58,61,66,0,59,47,60,54],
[41,46,55,42,0,35,45,40],
[55,57,64,54,66,0,59,45],
[49,53,55,41,56,42,0,39],
[55,63,67,47,61,56,62,0]])



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
result = np.append(np.array([8, 101, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,45,53,34,54,46,47],
[39,0,49,51,41,44,35,47],
[56,52,0,49,33,45,44,47],
[48,50,52,0,32,40,47,45],
[67,60,68,69,0,63,49,62],
[47,57,56,61,38,0,37,55],
[55,66,57,54,52,64,0,49],
[54,54,54,56,39,46,52,0]])



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
result = np.append(np.array([8, 101, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,33,53,24,39,42,36],
[40,0,41,37,24,42,42,29],
[68,60,0,50,44,56,50,52],
[48,64,51,0,42,59,45,45],
[77,77,57,59,0,70,67,39],
[62,59,45,42,31,0,51,35],
[59,59,51,56,34,50,0,45],
[65,72,49,56,62,66,56,0]])



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
result = np.append(np.array([8, 101, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,35,55,41,76,57,53],
[37,0,51,56,61,51,59,48],
[66,50,0,56,57,76,67,41],
[46,45,45,0,51,61,48,54],
[60,40,44,50,0,62,65,43],
[25,50,25,40,39,0,47,42],
[44,42,34,53,36,54,0,37],
[48,53,60,47,58,59,64,0]])



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
result = np.append(np.array([8, 101, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,49,43,50,52,46,56],
[59,0,56,51,49,53,48,56],
[52,45,0,43,50,53,45,55],
[58,50,58,0,51,55,49,62],
[51,52,51,50,0,51,56,65],
[49,48,48,46,50,0,46,54],
[55,53,56,52,45,55,0,58],
[45,45,46,39,36,47,43,0]])



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
result = np.append(np.array([8, 101, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,52,53,52,55,53,39],
[55,0,52,61,57,60,50,48],
[49,49,0,49,48,47,40,46],
[48,40,52,0,48,51,43,45],
[49,44,53,53,0,50,45,48],
[46,41,54,50,51,0,40,42],
[48,51,61,58,56,61,0,54],
[62,53,55,56,53,59,47,0]])



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
result = np.append(np.array([8, 101, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,55,61,66,62,58,64],
[56,0,53,61,64,61,50,58],
[46,48,0,53,53,51,51,58],
[40,40,48,0,56,56,51,54],
[35,37,48,45,0,33,46,44],
[39,40,50,45,68,0,50,49],
[43,51,50,50,55,51,0,51],
[37,43,43,47,57,52,50,0]])



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
result = np.append(np.array([8, 101, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,60,43,58,53,59,54],
[50,0,63,58,55,66,55,62],
[41,38,0,55,60,52,42,62],
[58,43,46,0,49,54,57,53],
[43,46,41,52,0,42,43,43],
[48,35,49,47,59,0,53,57],
[42,46,59,44,58,48,0,47],
[47,39,39,48,58,44,54,0]])



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
result = np.append(np.array([8, 101, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,40,47,26,46,49,64],
[48,0,61,44,47,38,51,55],
[61,40,0,53,52,54,54,77],
[54,57,48,0,31,33,58,70],
[75,54,49,70,0,57,48,76],
[55,63,47,68,44,0,51,77],
[52,50,47,43,53,50,0,57],
[37,46,24,31,25,24,44,0]])



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
result = np.append(np.array([8, 101, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,62,55,45,46,46,39],
[59,0,59,42,49,55,52,55],
[39,42,0,31,44,44,41,47],
[46,59,70,0,58,46,54,45],
[56,52,57,43,0,48,46,45],
[55,46,57,55,53,0,48,57],
[55,49,60,47,55,53,0,54],
[62,46,54,56,56,44,47,0]])



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
result = np.append(np.array([8, 101, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,51,49,47,50,51],
[45,0,50,50,51,48,44,47],
[52,51,0,51,58,55,52,50],
[50,51,50,0,57,54,57,48],
[52,50,43,44,0,36,44,45],
[54,53,46,47,65,0,46,52],
[51,57,49,44,57,55,0,51],
[50,54,51,53,56,49,50,0]])



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
result = np.append(np.array([8, 101, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,54,58,58,52,47],
[52,0,47,57,54,53,57,53],
[56,54,0,52,59,52,50,56],
[47,44,49,0,54,53,51,55],
[43,47,42,47,0,48,44,47],
[43,48,49,48,53,0,51,54],
[49,44,51,50,57,50,0,59],
[54,48,45,46,54,47,42,0]])



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
result = np.append(np.array([8, 101, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,57,45,39,43,43],
[52,0,49,53,56,42,39,37],
[52,52,0,58,50,36,35,51],
[44,48,43,0,37,43,27,33],
[56,45,51,64,0,42,55,54],
[62,59,65,58,59,0,40,61],
[58,62,66,74,46,61,0,54],
[58,64,50,68,47,40,47,0]])



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
result = np.append(np.array([8, 101, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,49,54,53,51,40,57],
[67,0,55,52,48,52,43,62],
[52,46,0,53,50,61,50,68],
[47,49,48,0,54,54,40,59],
[48,53,51,47,0,67,53,66],
[50,49,40,47,34,0,49,62],
[61,58,51,61,48,52,0,59],
[44,39,33,42,35,39,42,0]])



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
result = np.append(np.array([8, 101, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,66,29,59,53,57,59],
[50,0,45,39,38,51,45,51],
[35,56,0,33,54,46,45,56],
[72,62,68,0,46,52,63,65],
[42,63,47,55,0,66,56,49],
[48,50,55,49,35,0,29,42],
[44,56,56,38,45,72,0,39],
[42,50,45,36,52,59,62,0]])



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
result = np.append(np.array([8, 101, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,48,51,48,47,48],
[53,0,53,44,46,49,46,46],
[51,48,0,52,48,44,40,52],
[53,57,49,0,50,45,52,41],
[50,55,53,51,0,56,51,52],
[53,52,57,56,45,0,51,55],
[54,55,61,49,50,50,0,52],
[53,55,49,60,49,46,49,0]])



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
result = np.append(np.array([8, 101, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,48,53,48,51,46,52],
[49,0,44,54,48,53,52,55],
[53,57,0,49,57,50,57,54],
[48,47,52,0,48,43,52,58],
[53,53,44,53,0,47,39,53],
[50,48,51,58,54,0,57,63],
[55,49,44,49,62,44,0,54],
[49,46,47,43,48,38,47,0]])



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
result = np.append(np.array([8, 101, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,56,49,56,51,53],
[44,0,66,48,40,40,42,56],
[45,35,0,51,50,52,43,49],
[45,53,50,0,34,51,54,42],
[52,61,51,67,0,62,48,54],
[45,61,49,50,39,0,44,38],
[50,59,58,47,53,57,0,45],
[48,45,52,59,47,63,56,0]])



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
result = np.append(np.array([8, 101, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,58,56,60,49,50,57],
[47,0,52,54,58,55,53,55],
[43,49,0,51,55,52,47,49],
[45,47,50,0,57,51,45,50],
[41,43,46,44,0,44,38,44],
[52,46,49,50,57,0,48,56],
[51,48,54,56,63,53,0,53],
[44,46,52,51,57,45,48,0]])



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
result = np.append(np.array([8, 101, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,52,47,47,33,52,48],
[61,0,45,57,50,54,42,50],
[49,56,0,62,44,40,37,45],
[54,44,39,0,46,46,49,50],
[54,51,57,55,0,46,48,53],
[68,47,61,55,55,0,53,54],
[49,59,64,52,53,48,0,57],
[53,51,56,51,48,47,44,0]])



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
result = np.append(np.array([8, 101, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,75,50,56,71,56,44],
[20,0,78,46,33,46,37,21],
[26,23,0,65,31,44,31,19],
[51,55,36,0,44,38,44,51],
[45,68,70,57,0,50,32,85],
[30,55,57,63,51,0,55,51],
[45,64,70,57,69,46,0,64],
[57,80,82,50,16,50,37,0]])



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
result = np.append(np.array([8, 101, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,60,52,54,47,56,50],
[50,0,54,48,59,59,61,57],
[41,47,0,41,53,43,54,48],
[49,53,60,0,60,52,64,54],
[47,42,48,41,0,42,50,50],
[54,42,58,49,59,0,48,48],
[45,40,47,37,51,53,0,42],
[51,44,53,47,51,53,59,0]])



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
result = np.append(np.array([8, 101, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,36,37,37,37,38,36],
[56,0,54,51,50,53,58,53],
[65,47,0,36,47,32,44,52],
[64,50,65,0,49,41,48,43],
[64,51,54,52,0,45,55,51],
[64,48,69,60,56,0,64,51],
[63,43,57,53,46,37,0,50],
[65,48,49,58,50,50,51,0]])



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
result = np.append(np.array([8, 101, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,44,43,51,51,53,42],
[55,0,52,40,50,48,54,46],
[57,49,0,52,48,45,54,48],
[58,61,49,0,59,51,55,52],
[50,51,53,42,0,40,44,43],
[50,53,56,50,61,0,60,50],
[48,47,47,46,57,41,0,47],
[59,55,53,49,58,51,54,0]])



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
result = np.append(np.array([8, 101, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,48,45,36,46,38],
[60,0,54,53,49,52,56,52],
[56,47,0,63,47,50,43,45],
[53,48,38,0,43,36,38,46],
[56,52,54,58,0,50,50,42],
[65,49,51,65,51,0,60,55],
[55,45,58,63,51,41,0,57],
[63,49,56,55,59,46,44,0]])



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
result = np.append(np.array([8, 101, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,51,47,47,62,52],
[42,0,55,54,44,44,57,48],
[53,46,0,53,49,52,58,58],
[50,47,48,0,49,56,55,47],
[54,57,52,52,0,46,58,45],
[54,57,49,45,55,0,56,59],
[39,44,43,46,43,45,0,45],
[49,53,43,54,56,42,56,0]])



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
result = np.append(np.array([8, 101, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,40,41,49,40,42],
[60,0,63,50,68,43,56,51],
[56,38,0,52,55,52,53,53],
[61,51,49,0,59,47,57,40],
[60,33,46,42,0,42,49,51],
[52,58,49,54,59,0,57,54],
[61,45,48,44,52,44,0,45],
[59,50,48,61,50,47,56,0]])



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
result = np.append(np.array([8, 101, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,52,47,45,49,50,44],
[61,0,52,54,49,53,48,51],
[49,49,0,48,46,45,52,45],
[54,47,53,0,52,59,59,57],
[56,52,55,49,0,51,51,47],
[52,48,56,42,50,0,51,49],
[51,53,49,42,50,50,0,52],
[57,50,56,44,54,52,49,0]])



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
result = np.append(np.array([8, 101, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,62,67,65,45,65,63],
[43,0,59,58,57,42,62,61],
[39,42,0,47,47,39,47,60],
[34,43,54,0,52,43,46,54],
[36,44,54,49,0,52,57,48],
[56,59,62,58,49,0,62,62],
[36,39,54,55,44,39,0,54],
[38,40,41,47,53,39,47,0]])



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
result = np.append(np.array([8, 101, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,33,45,53,47,47,54],
[51,0,54,48,59,49,55,61],
[68,47,0,57,58,56,55,54],
[56,53,44,0,56,55,57,51],
[48,42,43,45,0,52,47,55],
[54,52,45,46,49,0,52,56],
[54,46,46,44,54,49,0,56],
[47,40,47,50,46,45,45,0]])



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
result = np.append(np.array([8, 101, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,52,55,48,61,54],
[51,0,54,43,51,41,49,57],
[57,47,0,57,54,47,55,52],
[49,58,44,0,71,65,63,54],
[46,50,47,30,0,42,40,51],
[53,60,54,36,59,0,58,56],
[40,52,46,38,61,43,0,59],
[47,44,49,47,50,45,42,0]])



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
result = np.append(np.array([8, 101, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,57,46,54,52,46],
[46,0,49,48,42,48,49,47],
[47,52,0,61,56,52,56,53],
[44,53,40,0,44,50,51,42],
[55,59,45,57,0,61,57,56],
[47,53,49,51,40,0,51,47],
[49,52,45,50,44,50,0,45],
[55,54,48,59,45,54,56,0]])



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
result = np.append(np.array([8, 101, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,52,53,39,46,53],
[51,0,57,48,51,53,50,44],
[44,44,0,51,54,44,42,50],
[49,53,50,0,52,40,47,51],
[48,50,47,49,0,47,49,47],
[62,48,57,61,54,0,51,59],
[55,51,59,54,52,50,0,53],
[48,57,51,50,54,42,48,0]])



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
result = np.append(np.array([8, 101, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,41,57,48,40,46,52],
[49,0,44,48,43,43,37,40],
[60,57,0,60,49,52,48,52],
[44,53,41,0,47,46,45,44],
[53,58,52,54,0,51,48,44],
[61,58,49,55,50,0,50,48],
[55,64,53,56,53,51,0,47],
[49,61,49,57,57,53,54,0]])



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
result = np.append(np.array([8, 101, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,58,60,53,49,56,49],
[39,0,41,41,36,53,33,45],
[43,60,0,46,52,50,47,52],
[41,60,55,0,49,55,48,59],
[48,65,49,52,0,50,48,44],
[52,48,51,46,51,0,51,50],
[45,68,54,53,53,50,0,40],
[52,56,49,42,57,51,61,0]])



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
result = np.append(np.array([8, 101, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,47,43,63,56,46,62],
[45,0,5,62,28,23,21,37],
[54,96,0,77,62,84,39,65],
[58,39,24,0,31,26,51,32],
[38,73,39,70,0,83,65,43],
[45,78,17,75,18,0,34,38],
[55,80,62,50,36,67,0,54],
[39,64,36,69,58,63,47,0]])



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
result = np.append(np.array([8, 101, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,30,63,87,8,100,87],
[44,0,30,63,56,37,75,45],
[71,71,0,48,100,52,71,101],
[38,38,53,0,67,24,67,68],
[14,45,1,34,0,7,45,32],
[93,64,49,77,94,0,93,94],
[1,26,30,34,56,8,0,45],
[14,56,0,33,69,7,56,0]])



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
result = np.append(np.array([8, 101, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,35,67,33,19,62,33],
[60,0,63,52,57,54,65,33],
[66,38,0,62,40,47,67,30],
[34,49,39,0,34,28,22,15],
[68,44,61,67,0,41,80,50],
[82,47,54,73,60,0,70,55],
[39,36,34,79,21,31,0,26],
[68,68,71,86,51,46,75,0]])



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
result = np.append(np.array([8, 101, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,57,58,66,54,57,47],
[53,0,61,58,72,47,53,52],
[44,40,0,44,52,47,51,45],
[43,43,57,0,59,48,46,43],
[35,29,49,42,0,43,49,38],
[47,54,54,53,58,0,43,49],
[44,48,50,55,52,58,0,43],
[54,49,56,58,63,52,58,0]])



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
result = np.append(np.array([8, 101, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,53,56,49,73,57,57],
[47,0,51,52,60,65,56,50],
[48,50,0,54,48,76,50,53],
[45,49,47,0,44,52,42,37],
[52,41,53,57,0,59,62,51],
[28,36,25,49,42,0,37,35],
[44,45,51,59,39,64,0,51],
[44,51,48,64,50,66,50,0]])



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
result = np.append(np.array([8, 101, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,77,100,100,55,100,76,46],
[24,0,100,100,55,85,69,55],
[1,1,0,101,32,32,1,0],
[1,1,0,0,32,31,1,0],
[46,46,69,69,0,100,45,15],
[1,16,69,70,1,0,46,0],
[25,32,100,100,56,55,0,31],
[55,46,101,101,86,101,70,0]])



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
result = np.append(np.array([8, 101, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,40,40,57,48,47,53],
[58,0,50,39,72,51,53,43],
[61,51,0,40,67,37,43,58],
[61,62,61,0,83,44,64,69],
[44,29,34,18,0,20,34,26],
[53,50,64,57,81,0,55,58],
[54,48,58,37,67,46,0,42],
[48,58,43,32,75,43,59,0]])



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
result = np.append(np.array([8, 101, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,36,55,57,52,50],
[53,0,52,51,61,60,49,53],
[55,49,0,53,57,53,57,56],
[65,50,48,0,54,59,58,55],
[46,40,44,47,0,49,49,47],
[44,41,48,42,52,0,46,54],
[49,52,44,43,52,55,0,51],
[51,48,45,46,54,47,50,0]])



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
result = np.append(np.array([8, 101, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,59,57,49,52,47,55],
[52,0,61,48,53,54,47,50],
[42,40,0,37,45,43,40,45],
[44,53,64,0,50,50,52,56],
[52,48,56,51,0,59,48,54],
[49,47,58,51,42,0,53,57],
[54,54,61,49,53,48,0,51],
[46,51,56,45,47,44,50,0]])



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
result = np.append(np.array([8, 101, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,49,56,63,63,66,45],
[44,0,64,38,33,36,44,37],
[52,37,0,58,51,46,45,45],
[45,63,43,0,42,56,32,55],
[38,68,50,59,0,48,54,48],
[38,65,55,45,53,0,52,42],
[35,57,56,69,47,49,0,69],
[56,64,56,46,53,59,32,0]])



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
result = np.append(np.array([8, 101, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,51,50,52,51,43,51],
[43,0,47,52,50,53,47,41],
[50,54,0,53,52,47,46,48],
[51,49,48,0,44,53,43,53],
[49,51,49,57,0,50,52,50],
[50,48,54,48,51,0,48,52],
[58,54,55,58,49,53,0,55],
[50,60,53,48,51,49,46,0]])



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
result = np.append(np.array([8, 101, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,44,46,52,46,47,52],
[58,0,50,47,51,46,46,63],
[57,51,0,57,54,46,48,54],
[55,54,44,0,61,51,51,54],
[49,50,47,40,0,46,42,46],
[55,55,55,50,55,0,51,56],
[54,55,53,50,59,50,0,57],
[49,38,47,47,55,45,44,0]])



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
result = np.append(np.array([8, 101, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,60,64,66,52,47,69],
[60,0,61,56,57,50,46,78],
[41,40,0,40,38,53,45,52],
[37,45,61,0,47,45,50,57],
[35,44,63,54,0,51,48,59],
[49,51,48,56,50,0,53,61],
[54,55,56,51,53,48,0,63],
[32,23,49,44,42,40,38,0]])



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
result = np.append(np.array([8, 101, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,35,30,46,20,25,50],
[44,0,36,37,16,36,32,50],
[66,65,0,42,38,36,25,63],
[71,64,59,0,55,54,47,60],
[55,85,63,46,0,53,75,52],
[81,65,65,47,48,0,57,65],
[76,69,76,54,26,44,0,60],
[51,51,38,41,49,36,41,0]])



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
result = np.append(np.array([8, 101, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,45,45,49,49,57,39],
[51,0,42,47,57,50,58,59],
[56,59,0,55,68,62,47,49],
[56,54,46,0,66,59,60,57],
[52,44,33,35,0,56,48,48],
[52,51,39,42,45,0,56,52],
[44,43,54,41,53,45,0,55],
[62,42,52,44,53,49,46,0]])



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
result = np.append(np.array([8, 101, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,55,57,56,55,49],
[45,0,47,43,44,53,45,42],
[50,54,0,53,59,54,56,53],
[46,58,48,0,55,63,49,47],
[44,57,42,46,0,56,50,46],
[45,48,47,38,45,0,52,41],
[46,56,45,52,51,49,0,47],
[52,59,48,54,55,60,54,0]])



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
result = np.append(np.array([8, 101, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,46,53,54,49,43,43],
[51,0,53,48,52,54,50,48],
[55,48,0,46,48,49,49,43],
[48,53,55,0,51,61,57,54],
[47,49,53,50,0,44,53,43],
[52,47,52,40,57,0,54,45],
[58,51,52,44,48,47,0,45],
[58,53,58,47,58,56,56,0]])



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
result = np.append(np.array([8, 101, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,58,49,52,51,51,51],
[46,0,64,55,52,46,47,55],
[43,37,0,43,40,39,46,57],
[52,46,58,0,43,51,50,52],
[49,49,61,58,0,46,48,54],
[50,55,62,50,55,0,56,54],
[50,54,55,51,53,45,0,61],
[50,46,44,49,47,47,40,0]])



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
result = np.append(np.array([8, 101, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,59,56,48,48,41,52],
[29,0,48,36,47,34,42,41],
[42,53,0,46,47,42,38,42],
[45,65,55,0,63,56,52,54],
[53,54,54,38,0,50,52,46],
[53,67,59,45,51,0,48,58],
[60,59,63,49,49,53,0,51],
[49,60,59,47,55,43,50,0]])



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
result = np.append(np.array([8, 101, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,61,47,54,42,62,58],
[49,0,61,57,58,53,58,58],
[40,40,0,52,47,44,54,51],
[54,44,49,0,60,45,44,50],
[47,43,54,41,0,33,49,52],
[59,48,57,56,68,0,63,62],
[39,43,47,57,52,38,0,48],
[43,43,50,51,49,39,53,0]])



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
result = np.append(np.array([8, 101, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,48,50,54,59,54,51],
[45,0,54,58,55,51,47,49],
[53,47,0,42,57,51,46,52],
[51,43,59,0,54,50,45,49],
[47,46,44,47,0,44,49,45],
[42,50,50,51,57,0,45,55],
[47,54,55,56,52,56,0,48],
[50,52,49,52,56,46,53,0]])



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
result = np.append(np.array([8, 101, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,48,49,47,46,50],
[56,0,59,53,57,54,49,54],
[53,42,0,50,45,48,51,55],
[53,48,51,0,59,54,45,50],
[52,44,56,42,0,44,42,50],
[54,47,53,47,57,0,48,47],
[55,52,50,56,59,53,0,54],
[51,47,46,51,51,54,47,0]])



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
result = np.append(np.array([8, 101, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,67,43,64,51,67,61],
[37,0,58,56,48,71,56,51],
[34,43,0,41,36,31,52,51],
[58,45,60,0,62,40,61,65],
[37,53,65,39,0,34,63,46],
[50,30,70,61,67,0,53,49],
[34,45,49,40,38,48,0,45],
[40,50,50,36,55,52,56,0]])



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
result = np.append(np.array([8, 101, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,56,54,49,67,43],
[51,0,49,39,42,42,69,35],
[45,52,0,41,45,46,53,49],
[45,62,60,0,60,61,56,57],
[47,59,56,41,0,55,65,48],
[52,59,55,40,46,0,70,40],
[34,32,48,45,36,31,0,30],
[58,66,52,44,53,61,71,0]])



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
result = np.append(np.array([8, 101, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,47,52,43,50,48],
[51,0,51,45,57,51,54,58],
[48,50,0,41,51,37,46,51],
[54,56,60,0,53,49,53,56],
[49,44,50,48,0,44,45,46],
[58,50,64,52,57,0,60,51],
[51,47,55,48,56,41,0,51],
[53,43,50,45,55,50,50,0]])



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
result = np.append(np.array([8, 101, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,34,50,54,53,49,51],
[50,0,38,48,44,53,46,35],
[67,63,0,49,56,55,67,51],
[51,53,52,0,55,55,51,38],
[47,57,45,46,0,62,47,43],
[48,48,46,46,39,0,51,43],
[52,55,34,50,54,50,0,40],
[50,66,50,63,58,58,61,0]])



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
result = np.append(np.array([8, 101, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,47,55,52,53,59,53],
[43,0,51,51,45,45,49,50],
[54,50,0,49,57,44,48,55],
[46,50,52,0,49,40,45,57],
[49,56,44,52,0,40,54,49],
[48,56,57,61,61,0,59,55],
[42,52,53,56,47,42,0,51],
[48,51,46,44,52,46,50,0]])



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
result = np.append(np.array([8, 101, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,62,67,67,56,77,63],
[56,0,89,80,54,101,45,83],
[39,12,0,67,51,53,32,43],
[34,21,34,0,17,53,60,47],
[34,47,50,84,0,58,49,87],
[45,0,48,48,43,0,32,43],
[24,56,69,41,52,69,0,70],
[38,18,58,54,14,58,31,0]])



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
result = np.append(np.array([8, 101, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,51,48,60,61,48,53],
[42,0,44,47,44,43,37,44],
[50,57,0,54,52,55,48,57],
[53,54,47,0,48,51,38,49],
[41,57,49,53,0,43,43,43],
[40,58,46,50,58,0,51,46],
[53,64,53,63,58,50,0,47],
[48,57,44,52,58,55,54,0]])



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
result = np.append(np.array([8, 101, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,62,57,51,52,53],
[60,0,69,48,66,67,50,45],
[56,32,0,63,72,49,40,49],
[39,53,38,0,52,44,21,44],
[44,35,29,49,0,30,37,49],
[50,34,52,57,71,0,41,41],
[49,51,61,80,64,60,0,76],
[48,56,52,57,52,60,25,0]])



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
result = np.append(np.array([8, 101, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,54,49,41,52,57],
[45,0,40,49,50,45,49,52],
[55,61,0,53,57,49,59,55],
[47,52,48,0,46,49,46,53],
[52,51,44,55,0,53,55,57],
[60,56,52,52,48,0,53,54],
[49,52,42,55,46,48,0,61],
[44,49,46,48,44,47,40,0]])



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
result = np.append(np.array([8, 101, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,52,49,59,47,51],
[46,0,52,46,52,59,49,38],
[45,49,0,50,46,55,53,43],
[49,55,51,0,41,57,45,43],
[52,49,55,60,0,57,53,42],
[42,42,46,44,44,0,37,44],
[54,52,48,56,48,64,0,48],
[50,63,58,58,59,57,53,0]])



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
result = np.append(np.array([8, 101, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,43,43,59,52,56],
[57,0,61,49,50,55,49,61],
[49,40,0,51,47,47,47,56],
[58,52,50,0,48,61,50,58],
[58,51,54,53,0,58,44,61],
[42,46,54,40,43,0,41,49],
[49,52,54,51,57,60,0,51],
[45,40,45,43,40,52,50,0]])



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
result = np.append(np.array([8, 101, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,29,51,55,73,39],
[44,0,37,11,24,48,39,9],
[42,64,0,49,47,42,47,25],
[72,90,52,0,49,48,60,55],
[50,77,54,52,0,56,56,67],
[46,53,59,53,45,0,45,40],
[28,62,54,41,45,56,0,37],
[62,92,76,46,34,61,64,0]])



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
result = np.append(np.array([8, 101, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,55,48,50,45,54,49],
[43,0,52,54,53,49,54,46],
[46,49,0,55,48,51,53,44],
[53,47,46,0,46,46,45,42],
[51,48,53,55,0,49,60,49],
[56,52,50,55,52,0,51,48],
[47,47,48,56,41,50,0,51],
[52,55,57,59,52,53,50,0]])



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
result = np.append(np.array([8, 101, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,52,38,50,45,46,56],
[52,0,48,40,53,51,44,48],
[49,53,0,45,53,55,41,49],
[63,61,56,0,57,53,48,60],
[51,48,48,44,0,52,44,45],
[56,50,46,48,49,0,46,52],
[55,57,60,53,57,55,0,49],
[45,53,52,41,56,49,52,0]])



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
result = np.append(np.array([8, 101, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,74,54,60,33,51,57],
[29,0,68,44,50,41,48,53],
[27,33,0,39,35,26,34,44],
[47,57,62,0,76,52,73,71],
[41,51,66,25,0,29,50,50],
[68,60,75,49,72,0,80,59],
[50,53,67,28,51,21,0,41],
[44,48,57,30,51,42,60,0]])



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
result = np.append(np.array([8, 101, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,53,51,44,49,50],
[49,0,56,52,49,51,57,57],
[56,45,0,49,58,52,48,46],
[48,49,52,0,60,47,48,50],
[50,52,43,41,0,41,46,45],
[57,50,49,54,60,0,67,50],
[52,44,53,53,55,34,0,49],
[51,44,55,51,56,51,52,0]])



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
result = np.append(np.array([8, 101, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,42,37,58,34,51],
[51,0,54,41,52,66,50,64],
[51,47,0,40,59,51,33,60],
[59,60,61,0,48,51,54,66],
[64,49,42,53,0,53,43,68],
[43,35,50,50,48,0,29,49],
[67,51,68,47,58,72,0,74],
[50,37,41,35,33,52,27,0]])



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
result = np.append(np.array([8, 101, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,51,40,51,47,46,37],
[64,0,49,47,55,55,52,49],
[50,52,0,47,54,55,47,42],
[61,54,54,0,61,60,54,47],
[50,46,47,40,0,45,42,44],
[54,46,46,41,56,0,48,38],
[55,49,54,47,59,53,0,51],
[64,52,59,54,57,63,50,0]])



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
result = np.append(np.array([8, 101, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,49,50,51,58,59],
[49,0,57,60,46,53,64,47],
[45,44,0,42,38,41,48,38],
[52,41,59,0,49,41,64,46],
[51,55,63,52,0,50,52,49],
[50,48,60,60,51,0,53,52],
[43,37,53,37,49,48,0,54],
[42,54,63,55,52,49,47,0]])



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
result = np.append(np.array([8, 101, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,43,46,47,50,51],
[49,0,63,54,48,59,56,55],
[54,38,0,48,42,51,50,56],
[58,47,53,0,53,60,51,44],
[55,53,59,48,0,57,57,57],
[54,42,50,41,44,0,42,51],
[51,45,51,50,44,59,0,55],
[50,46,45,57,44,50,46,0]])



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
result = np.append(np.array([8, 101, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,38,48,54,46,37],
[55,0,58,54,66,65,45,53],
[61,43,0,52,53,42,49,41],
[63,47,49,0,56,53,49,51],
[53,35,48,45,0,54,50,38],
[47,36,59,48,47,0,57,49],
[55,56,52,52,51,44,0,43],
[64,48,60,50,63,52,58,0]])



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
result = np.append(np.array([8, 101, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,58,58,63,37,53,51],
[47,0,49,59,48,46,79,64],
[43,52,0,45,54,39,58,48],
[43,42,56,0,55,55,63,57],
[38,53,47,46,0,39,62,52],
[64,55,62,46,62,0,65,58],
[48,22,43,38,39,36,0,42],
[50,37,53,44,49,43,59,0]])



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
result = np.append(np.array([8, 101, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,37,54,38,51,51,53],
[52,0,42,49,51,52,61,54],
[64,59,0,48,64,50,57,61],
[47,52,53,0,42,45,53,47],
[63,50,37,59,0,55,51,59],
[50,49,51,56,46,0,61,71],
[50,40,44,48,50,40,0,46],
[48,47,40,54,42,30,55,0]])



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
result = np.append(np.array([8, 101, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,41,47,58,32,49,47],
[44,0,37,45,63,28,63,18],
[60,64,0,55,60,41,71,55],
[54,56,46,0,54,38,64,49],
[43,38,41,47,0,29,57,39],
[69,73,60,63,72,0,81,47],
[52,38,30,37,44,20,0,31],
[54,83,46,52,62,54,70,0]])



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
result = np.append(np.array([8, 101, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,70,65,64,52,52],
[51,0,53,67,53,65,52,45],
[50,48,0,58,66,61,53,57],
[31,34,43,0,50,40,46,45],
[36,48,35,51,0,52,43,45],
[37,36,40,61,49,0,49,32],
[49,49,48,55,58,52,0,44],
[49,56,44,56,56,69,57,0]])



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
result = np.append(np.array([8, 101, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,47,60,60,58,48],
[43,0,50,45,57,55,55,51],
[49,51,0,41,52,55,55,42],
[54,56,60,0,58,57,55,48],
[41,44,49,43,0,45,41,37],
[41,46,46,44,56,0,49,44],
[43,46,46,46,60,52,0,45],
[53,50,59,53,64,57,56,0]])



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
result = np.append(np.array([8, 101, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,47,47,56,51,44,50],
[41,0,50,42,54,42,49,51],
[54,51,0,51,52,45,44,49],
[54,59,50,0,60,47,51,54],
[45,47,49,41,0,45,41,44],
[50,59,56,54,56,0,59,51],
[57,52,57,50,60,42,0,58],
[51,50,52,47,57,50,43,0]])



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
result = np.append(np.array([8, 101, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,47,45,46,43,51,44],
[62,0,54,54,47,56,58,58],
[54,47,0,51,48,54,52,52],
[56,47,50,0,51,50,59,57],
[55,54,53,50,0,54,55,56],
[58,45,47,51,47,0,57,54],
[50,43,49,42,46,44,0,55],
[57,43,49,44,45,47,46,0]])



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
result = np.append(np.array([8, 101, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,63,56,48,59,57,54],
[46,0,61,56,41,52,56,48],
[38,40,0,36,38,42,53,49],
[45,45,65,0,66,43,63,67],
[53,60,63,35,0,45,49,54],
[42,49,59,58,56,0,72,52],
[44,45,48,38,52,29,0,43],
[47,53,52,34,47,49,58,0]])



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
result = np.append(np.array([8, 101, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,54,53,50,39,47,37],
[39,0,50,37,46,36,47,45],
[47,51,0,44,40,34,54,40],
[48,64,57,0,60,51,66,56],
[51,55,61,41,0,39,49,52],
[62,65,67,50,62,0,56,47],
[54,54,47,35,52,45,0,46],
[64,56,61,45,49,54,55,0]])



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
result = np.append(np.array([8, 101, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,51,51,47,45,59,21],
[37,0,46,44,52,29,57,41],
[50,55,0,72,44,36,51,52],
[50,57,29,0,44,43,58,27],
[54,49,57,57,0,58,57,38],
[56,72,65,58,43,0,53,38],
[42,44,50,43,44,48,0,36],
[80,60,49,74,63,63,65,0]])



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
result = np.append(np.array([8, 101, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,46,51,53,47,53],
[49,0,40,43,45,51,49,45],
[49,61,0,52,56,60,50,55],
[55,58,49,0,60,55,59,55],
[50,56,45,41,0,58,53,51],
[48,50,41,46,43,0,46,43],
[54,52,51,42,48,55,0,48],
[48,56,46,46,50,58,53,0]])



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
result = np.append(np.array([8, 101, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,43,29,34,45,56,34],
[38,0,53,13,44,59,61,39],
[58,48,0,39,52,47,59,59],
[72,88,62,0,43,64,71,55],
[67,57,49,58,0,45,50,50],
[56,42,54,37,56,0,74,43],
[45,40,42,30,51,27,0,33],
[67,62,42,46,51,58,68,0]])



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
result = np.append(np.array([8, 101, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,69,67,82,58,64,54,47],
[32,0,48,76,59,42,53,45],
[34,53,0,83,54,56,60,31],
[19,25,18,0,51,34,17,34],
[43,42,47,50,0,40,37,53],
[37,59,45,67,61,0,37,50],
[47,48,41,84,64,64,0,59],
[54,56,70,67,48,51,42,0]])



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
result = np.append(np.array([8, 101, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,55,48,54,57,62,60],
[43,0,50,39,45,42,55,52],
[46,51,0,44,41,42,54,57],
[53,62,57,0,58,49,51,55],
[47,56,60,43,0,51,52,53],
[44,59,59,52,50,0,57,49],
[39,46,47,50,49,44,0,48],
[41,49,44,46,48,52,53,0]])



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
result = np.append(np.array([8, 101, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,51,44,55,48,47,52],
[53,0,48,51,56,52,54,55],
[50,53,0,37,51,50,50,56],
[57,50,64,0,60,58,54,61],
[46,45,50,41,0,41,51,43],
[53,49,51,43,60,0,53,50],
[54,47,51,47,50,48,0,48],
[49,46,45,40,58,51,53,0]])



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
result = np.append(np.array([8, 101, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,58,55,52,56,47,59],
[40,0,49,41,40,42,50,42],
[43,52,0,42,41,46,44,57],
[46,60,59,0,45,53,36,48],
[49,61,60,56,0,48,49,59],
[45,59,55,48,53,0,39,54],
[54,51,57,65,52,62,0,46],
[42,59,44,53,42,47,55,0]])



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
result = np.append(np.array([8, 101, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,57,53,42,69,59,51],
[50,0,48,45,41,65,60,47],
[44,53,0,41,31,49,54,62],
[48,56,60,0,53,58,68,59],
[59,60,70,48,0,68,62,59],
[32,36,52,43,33,0,45,43],
[42,41,47,33,39,56,0,42],
[50,54,39,42,42,58,59,0]])



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
result = np.append(np.array([8, 101, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,47,50,41,43,41,37],
[63,0,56,64,43,50,48,60],
[54,45,0,45,45,56,46,50],
[51,37,56,0,30,48,40,44],
[60,58,56,71,0,58,59,49],
[58,51,45,53,43,0,46,54],
[60,53,55,61,42,55,0,51],
[64,41,51,57,52,47,50,0]])



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
result = np.append(np.array([8, 101, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,39,52,42,36,42],
[56,0,49,37,58,46,49,48],
[58,52,0,47,60,45,51,55],
[62,64,54,0,59,50,48,53],
[49,43,41,42,0,45,46,37],
[59,55,56,51,56,0,48,58],
[65,52,50,53,55,53,0,50],
[59,53,46,48,64,43,51,0]])



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
result = np.append(np.array([8, 101, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,53,50,53,56,51,54],
[47,0,51,53,49,49,47,52],
[48,50,0,44,47,47,50,46],
[51,48,57,0,47,50,49,52],
[48,52,54,54,0,56,48,52],
[45,52,54,51,45,0,47,43],
[50,54,51,52,53,54,0,46],
[47,49,55,49,49,58,55,0]])



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
result = np.append(np.array([8, 101, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,68,80,40,79,84,95],
[23,0,40,61,39,45,23,83],
[33,61,0,77,56,59,39,94],
[21,40,24,0,11,68,11,57],
[61,62,45,90,0,73,62,91],
[22,56,42,33,28,0,22,56],
[17,78,62,90,39,79,0,95],
[6,18,7,44,10,45,6,0]])



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
result = np.append(np.array([8, 101, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,51,58,58,52,57],
[47,0,47,44,55,55,51,52],
[52,54,0,47,57,61,51,51],
[50,57,54,0,61,61,47,56],
[43,46,44,40,0,47,42,39],
[43,46,40,40,54,0,47,50],
[49,50,50,54,59,54,0,59],
[44,49,50,45,62,51,42,0]])



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
result = np.append(np.array([8, 101, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,52,46,45,48,52],
[52,0,48,49,45,40,49,43],
[46,53,0,50,40,43,46,43],
[49,52,51,0,47,45,48,41],
[55,56,61,54,0,48,53,49],
[56,61,58,56,53,0,60,50],
[53,52,55,53,48,41,0,46],
[49,58,58,60,52,51,55,0]])



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
result = np.append(np.array([8, 101, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,46,44,47,48,45],
[52,0,50,49,41,44,50,53],
[51,51,0,54,49,45,52,48],
[55,52,47,0,47,56,57,49],
[57,60,52,54,0,52,49,60],
[54,57,56,45,49,0,47,51],
[53,51,49,44,52,54,0,43],
[56,48,53,52,41,50,58,0]])



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
result = np.append(np.array([8, 101, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,62,49,47,59,53,59],
[42,0,52,53,47,47,46,45],
[39,49,0,48,44,55,45,41],
[52,48,53,0,52,55,51,46],
[54,54,57,49,0,53,51,50],
[42,54,46,46,48,0,48,51],
[48,55,56,50,50,53,0,47],
[42,56,60,55,51,50,54,0]])



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
result = np.append(np.array([8, 101, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,37,39,62,42,38],
[50,0,45,44,44,44,43,37],
[46,56,0,42,30,57,30,37],
[64,57,59,0,51,64,39,53],
[62,57,71,50,0,68,66,41],
[39,57,44,37,33,0,29,20],
[59,58,71,62,35,72,0,53],
[63,64,64,48,60,81,48,0]])



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
result = np.append(np.array([8, 101, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,60,50,54,54,46],
[46,0,50,55,47,51,40,44],
[45,51,0,47,41,52,42,42],
[41,46,54,0,40,49,43,44],
[51,54,60,61,0,60,50,54],
[47,50,49,52,41,0,46,46],
[47,61,59,58,51,55,0,50],
[55,57,59,57,47,55,51,0]])



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
result = np.append(np.array([8, 101, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,64,49,48,63,47,61],
[43,0,39,49,45,49,33,56],
[37,62,0,44,37,47,46,47],
[52,52,57,0,47,55,43,46],
[53,56,64,54,0,58,50,60],
[38,52,54,46,43,0,56,56],
[54,68,55,58,51,45,0,59],
[40,45,54,55,41,45,42,0]])



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
result = np.append(np.array([8, 101, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,46,48,61,44,50,46],
[35,0,45,47,48,48,55,42],
[55,56,0,43,69,54,48,45],
[53,54,58,0,58,57,41,47],
[40,53,32,43,0,46,38,46],
[57,53,47,44,55,0,56,45],
[51,46,53,60,63,45,0,51],
[55,59,56,54,55,56,50,0]])



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
result = np.append(np.array([8, 101, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,62,54,47,43,36],
[51,0,49,64,55,56,61,53],
[49,52,0,67,63,52,45,41],
[39,37,34,0,47,45,41,39],
[47,46,38,54,0,55,46,40],
[54,45,49,56,46,0,49,44],
[58,40,56,60,55,52,0,51],
[65,48,60,62,61,57,50,0]])



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
result = np.append(np.array([8, 101, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,53,53,50,46,50,51],
[42,0,49,43,44,40,45,46],
[48,52,0,53,53,45,52,57],
[48,58,48,0,56,43,42,44],
[51,57,48,45,0,51,47,52],
[55,61,56,58,50,0,51,62],
[51,56,49,59,54,50,0,57],
[50,55,44,57,49,39,44,0]])



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
result = np.append(np.array([8, 101, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,48,48,41,45,61,50],
[65,0,53,52,48,54,61,68],
[53,48,0,57,46,40,62,43],
[53,49,44,0,49,45,55,52],
[60,53,55,52,0,53,70,49],
[56,47,61,56,48,0,68,55],
[40,40,39,46,31,33,0,45],
[51,33,58,49,52,46,56,0]])



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
result = np.append(np.array([8, 101, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,46,44,43,43,44,39],
[58,0,46,51,59,52,49,46],
[55,55,0,53,48,48,52,47],
[57,50,48,0,53,49,49,53],
[58,42,53,48,0,44,52,41],
[58,49,53,52,57,0,54,44],
[57,52,49,52,49,47,0,41],
[62,55,54,48,60,57,60,0]])



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
result = np.append(np.array([8, 101, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,56,75,33,65,73,65],
[35,0,56,51,37,37,49,51],
[45,45,0,45,53,56,45,35],
[26,50,56,0,37,42,54,42],
[68,64,48,64,0,75,73,40],
[36,64,45,59,26,0,82,49],
[28,52,56,47,28,19,0,51],
[36,50,66,59,61,52,50,0]])



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
result = np.append(np.array([8, 101, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,57,50,56,50,52],
[48,0,48,43,43,50,51,44],
[45,53,0,52,51,52,49,47],
[44,58,49,0,51,50,51,49],
[51,58,50,50,0,50,54,51],
[45,51,49,51,51,0,52,42],
[51,50,52,50,47,49,0,45],
[49,57,54,52,50,59,56,0]])



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
result = np.append(np.array([8, 101, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,52,58,57,45,60],
[49,0,53,65,54,49,54,67],
[45,48,0,46,48,50,47,58],
[49,36,55,0,56,51,58,54],
[43,47,53,45,0,58,44,69],
[44,52,51,50,43,0,52,71],
[56,47,54,43,57,49,0,67],
[41,34,43,47,32,30,34,0]])



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
result = np.append(np.array([8, 101, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,44,51,47,52,46],
[51,0,47,60,52,53,50,45],
[54,54,0,48,52,54,53,49],
[57,41,53,0,56,52,48,45],
[50,49,49,45,0,49,52,37],
[54,48,47,49,52,0,53,37],
[49,51,48,53,49,48,0,51],
[55,56,52,56,64,64,50,0]])



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
result = np.append(np.array([8, 101, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,66,41,51,55,40,61],
[53,0,58,44,46,35,52,38],
[35,43,0,34,36,31,43,45],
[60,57,67,0,64,46,60,53],
[50,55,65,37,0,33,44,49],
[46,66,70,55,68,0,61,53],
[61,49,58,41,57,40,0,50],
[40,63,56,48,52,48,51,0]])



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
result = np.append(np.array([8, 101, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,31,59,43,93,54,51],
[47,0,28,22,51,39,14,28],
[70,73,0,37,43,70,37,37],
[42,79,64,0,46,42,60,39],
[58,50,58,55,0,50,50,47],
[8,62,31,59,51,0,59,22],
[47,87,64,41,51,42,0,47],
[50,73,64,62,54,79,54,0]])



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
result = np.append(np.array([8, 101, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,57,53,49,48,52,51],
[57,0,56,50,51,52,51,64],
[44,45,0,43,44,40,46,51],
[48,51,58,0,51,50,52,63],
[52,50,57,50,0,49,50,69],
[53,49,61,51,52,0,58,64],
[49,50,55,49,51,43,0,54],
[50,37,50,38,32,37,47,0]])



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
result = np.append(np.array([8, 101, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,56,50,39,47,50,65],
[55,0,39,47,40,59,46,51],
[45,62,0,55,53,42,50,57],
[51,54,46,0,56,45,44,49],
[62,61,48,45,0,50,40,54],
[54,42,59,56,51,0,63,55],
[51,55,51,57,61,38,0,58],
[36,50,44,52,47,46,43,0]])



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
result = np.append(np.array([8, 101, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,46,52,57,57,44,47],
[55,0,49,48,51,60,46,52],
[55,52,0,46,50,65,51,48],
[49,53,55,0,53,55,48,55],
[44,50,51,48,0,53,44,53],
[44,41,36,46,48,0,40,45],
[57,55,50,53,57,61,0,56],
[54,49,53,46,48,56,45,0]])



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
result = np.append(np.array([8, 101, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,47,49,54,51,47],
[52,0,53,52,63,59,50,50],
[48,48,0,49,56,50,52,44],
[54,49,52,0,56,51,55,47],
[52,38,45,45,0,53,52,42],
[47,42,51,50,48,0,52,45],
[50,51,49,46,49,49,0,54],
[54,51,57,54,59,56,47,0]])



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
result = np.append(np.array([8, 101, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,49,47,57,51,45,48],
[61,0,56,50,55,60,57,59],
[52,45,0,46,52,48,44,47],
[54,51,55,0,49,55,44,57],
[44,46,49,52,0,52,48,54],
[50,41,53,46,49,0,47,52],
[56,44,57,57,53,54,0,57],
[53,42,54,44,47,49,44,0]])



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
result = np.append(np.array([8, 101, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,56,46,49,66,55],
[47,0,50,32,48,33,42,34],
[52,51,0,52,54,39,55,41],
[45,69,49,0,61,58,42,55],
[55,53,47,40,0,38,39,36],
[52,68,62,43,63,0,51,52],
[35,59,46,59,62,50,0,51],
[46,67,60,46,65,49,50,0]])



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
result = np.append(np.array([8, 101, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,58,44,70,63,69,44],
[57,0,50,48,84,58,72,36],
[43,51,0,54,64,61,60,39],
[57,53,47,0,73,68,72,57],
[31,17,37,28,0,34,42,29],
[38,43,40,33,67,0,66,38],
[32,29,41,29,59,35,0,42],
[57,65,62,44,72,63,59,0]])



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
result = np.append(np.array([8, 101, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,51,52,47,58,54],
[53,0,56,49,58,51,54,60],
[47,45,0,58,57,57,48,55],
[50,52,43,0,50,51,63,51],
[49,43,44,51,0,49,55,45],
[54,50,44,50,52,0,53,46],
[43,47,53,38,46,48,0,57],
[47,41,46,50,56,55,44,0]])



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
result = np.append(np.array([8, 101, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,54,61,59,53,60,50],
[30,0,42,35,55,39,45,51],
[47,59,0,47,65,63,49,65],
[40,66,54,0,49,54,59,57],
[42,46,36,52,0,48,54,59],
[48,62,38,47,53,0,51,55],
[41,56,52,42,47,50,0,53],
[51,50,36,44,42,46,48,0]])



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
result = np.append(np.array([8, 101, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,53,46,53,46,45],
[45,0,59,47,45,48,46,48],
[45,42,0,41,47,44,45,45],
[48,54,60,0,51,48,53,60],
[55,56,54,50,0,46,55,54],
[48,53,57,53,55,0,59,53],
[55,55,56,48,46,42,0,50],
[56,53,56,41,47,48,51,0]])



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
result = np.append(np.array([8, 101, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,59,44,43,46,45,46],
[51,0,51,45,50,49,53,50],
[42,50,0,46,49,55,52,50],
[57,56,55,0,42,58,54,53],
[58,51,52,59,0,49,52,55],
[55,52,46,43,52,0,46,53],
[56,48,49,47,49,55,0,46],
[55,51,51,48,46,48,55,0]])



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
result = np.append(np.array([8, 101, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,78,67,50,78,64,58],
[39,0,56,46,36,72,30,50],
[23,45,0,17,39,50,28,26],
[34,55,84,0,54,59,42,35],
[51,65,62,47,0,59,45,48],
[23,29,51,42,42,0,30,29],
[37,71,73,59,56,71,0,41],
[43,51,75,66,53,72,60,0]])



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
result = np.append(np.array([8, 101, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,50,42,45,59,63],
[72,0,45,58,56,46,64,63],
[71,56,0,56,47,57,65,57],
[51,43,45,0,53,41,61,62],
[59,45,54,48,0,55,49,67],
[56,55,44,60,46,0,70,50],
[42,37,36,40,52,31,0,54],
[38,38,44,39,34,51,47,0]])



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
result = np.append(np.array([8, 101, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,48,51,46,47,51,56],
[54,0,44,58,53,51,49,53],
[53,57,0,63,50,52,57,53],
[50,43,38,0,45,48,42,47],
[55,48,51,56,0,49,54,61],
[54,50,49,53,52,0,45,50],
[50,52,44,59,47,56,0,53],
[45,48,48,54,40,51,48,0]])



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
result = np.append(np.array([8, 101, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,53,51,44,59,48],
[47,0,43,45,48,42,46,40],
[50,58,0,61,59,54,61,57],
[48,56,40,0,53,48,52,43],
[50,53,42,48,0,36,52,46],
[57,59,47,53,65,0,60,43],
[42,55,40,49,49,41,0,46],
[53,61,44,58,55,58,55,0]])



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
result = np.append(np.array([8, 101, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,45,45,56,66,44,61],
[41,0,37,22,41,32,24,53],
[56,64,0,64,58,41,56,52],
[56,79,37,0,58,38,47,51],
[45,60,43,43,0,51,31,68],
[35,69,60,63,50,0,55,65],
[57,77,45,54,70,46,0,63],
[40,48,49,50,33,36,38,0]])



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
result = np.append(np.array([8, 101, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,46,54,61,60,57,59],
[46,0,46,49,51,48,52,50],
[55,55,0,51,61,58,50,51],
[47,52,50,0,61,52,57,48],
[40,50,40,40,0,61,51,50],
[41,53,43,49,40,0,46,44],
[44,49,51,44,50,55,0,50],
[42,51,50,53,51,57,51,0]])



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
result = np.append(np.array([8, 101, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,47,54,49,54,50,54],
[50,0,53,59,57,53,52,57],
[54,48,0,51,56,50,60,57],
[47,42,50,0,47,49,52,56],
[52,44,45,54,0,55,47,53],
[47,48,51,52,46,0,57,55],
[51,49,41,49,54,44,0,52],
[47,44,44,45,48,46,49,0]])



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
result = np.append(np.array([8, 101, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,67,48,52,43,53,63],
[33,0,50,35,53,55,58,36],
[34,51,0,34,35,46,46,40],
[53,66,67,0,58,45,56,49],
[49,48,66,43,0,55,58,55],
[58,46,55,56,46,0,61,48],
[48,43,55,45,43,40,0,45],
[38,65,61,52,46,53,56,0]])



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
result = np.append(np.array([8, 101, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,63,54,49,58,58,57],
[37,0,51,42,51,48,45,49],
[38,50,0,46,41,45,50,39],
[47,59,55,0,45,66,53,58],
[52,50,60,56,0,58,61,51],
[43,53,56,35,43,0,41,48],
[43,56,51,48,40,60,0,60],
[44,52,62,43,50,53,41,0]])



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
result = np.append(np.array([8, 101, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,49,49,54,48,43],
[45,0,50,41,51,51,47,54],
[45,51,0,47,53,40,46,40],
[52,60,54,0,53,49,52,51],
[52,50,48,48,0,51,57,46],
[47,50,61,52,50,0,53,48],
[53,54,55,49,44,48,0,47],
[58,47,61,50,55,53,54,0]])



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
result = np.append(np.array([8, 101, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,44,44,49,44,42,48],
[40,0,53,46,50,41,46,49],
[57,48,0,51,54,52,49,55],
[57,55,50,0,60,48,46,50],
[52,51,47,41,0,45,52,51],
[57,60,49,53,56,0,55,59],
[59,55,52,55,49,46,0,54],
[53,52,46,51,50,42,47,0]])



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
result = np.append(np.array([8, 101, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,56,49,46,52,53,47],
[47,0,53,52,53,54,54,54],
[45,48,0,45,52,42,51,45],
[52,49,56,0,51,50,58,49],
[55,48,49,50,0,46,55,51],
[49,47,59,51,55,0,51,45],
[48,47,50,43,46,50,0,48],
[54,47,56,52,50,56,53,0]])



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
result = np.append(np.array([8, 101, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,48,46,56,46,36,46],
[54,0,50,44,55,55,38,40],
[53,51,0,50,56,64,49,55],
[55,57,51,0,53,62,52,48],
[45,46,45,48,0,59,45,46],
[55,46,37,39,42,0,39,51],
[65,63,52,49,56,62,0,58],
[55,61,46,53,55,50,43,0]])



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
result = np.append(np.array([8, 101, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,45,67,53,60,44,48],
[42,0,48,58,50,62,48,67],
[56,53,0,61,71,56,50,70],
[34,43,40,0,49,42,38,50],
[48,51,30,52,0,52,64,61],
[41,39,45,59,49,0,55,56],
[57,53,51,63,37,46,0,51],
[53,34,31,51,40,45,50,0]])



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
result = np.append(np.array([8, 101, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,92,58,80,29,73,51,58],
[9,0,55,51,21,70,51,38],
[43,46,0,25,48,46,25,41],
[21,50,76,0,33,67,21,56],
[72,80,53,68,0,61,71,32],
[28,31,55,34,40,0,31,38],
[50,50,76,80,30,70,0,52],
[43,63,60,45,69,63,49,0]])



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
result = np.append(np.array([8, 101, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,35,43,57,49,47,49],
[64,0,45,44,57,52,47,43],
[66,56,0,51,55,61,56,50],
[58,57,50,0,60,61,61,62],
[44,44,46,41,0,52,49,51],
[52,49,40,40,49,0,48,50],
[54,54,45,40,52,53,0,39],
[52,58,51,39,50,51,62,0]])



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
result = np.append(np.array([8, 101, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,40,50,46,43,44,46],
[53,0,45,52,55,50,44,46],
[61,56,0,59,58,52,54,45],
[51,49,42,0,51,44,44,43],
[55,46,43,50,0,41,38,44],
[58,51,49,57,60,0,44,51],
[57,57,47,57,63,57,0,56],
[55,55,56,58,57,50,45,0]])



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
result = np.append(np.array([8, 101, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,58,58,44,47,53,45],
[64,0,67,53,64,51,71,50],
[43,34,0,32,44,21,37,23],
[43,48,69,0,43,44,40,66],
[57,37,57,58,0,51,57,61],
[54,50,80,57,50,0,58,70],
[48,30,64,61,44,43,0,48],
[56,51,78,35,40,31,53,0]])



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
result = np.append(np.array([8, 101, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,68,54,47,57,64],
[52,0,46,56,46,41,48,38],
[47,55,0,71,61,56,56,49],
[33,45,30,0,47,33,45,42],
[47,55,40,54,0,43,43,51],
[54,60,45,68,58,0,51,45],
[44,53,45,56,58,50,0,57],
[37,63,52,59,50,56,44,0]])



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
result = np.append(np.array([8, 101, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,54,59,46,54,57,51],
[49,0,49,56,54,54,56,53],
[47,52,0,56,45,50,49,48],
[42,45,45,0,42,45,44,42],
[55,47,56,59,0,49,59,60],
[47,47,51,56,52,0,49,56],
[44,45,52,57,42,52,0,53],
[50,48,53,59,41,45,48,0]])



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
result = np.append(np.array([8, 101, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,59,37,54,58,58,52],
[43,0,66,45,48,66,43,38],
[42,35,0,38,55,37,44,36],
[64,56,63,0,48,72,56,34],
[47,53,46,53,0,64,37,42],
[43,35,64,29,37,0,35,18],
[43,58,57,45,64,66,0,27],
[49,63,65,67,59,83,74,0]])



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
result = np.append(np.array([8, 101, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,48,54,53,58,48],
[54,0,55,45,60,53,55,54],
[50,46,0,46,47,52,56,53],
[53,56,55,0,52,59,51,43],
[47,41,54,49,0,58,53,45],
[48,48,49,42,43,0,50,51],
[43,46,45,50,48,51,0,45],
[53,47,48,58,56,50,56,0]])



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
result = np.append(np.array([8, 101, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,46,51,45,50,56,56],
[48,0,44,48,48,47,58,54],
[55,57,0,47,54,49,61,59],
[50,53,54,0,54,53,60,65],
[56,53,47,47,0,60,59,63],
[51,54,52,48,41,0,50,57],
[45,43,40,41,42,51,0,53],
[45,47,42,36,38,44,48,0]])



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
result = np.append(np.array([8, 101, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,59,32,33,46,60,36],
[66,0,63,52,68,55,49,43],
[42,38,0,29,51,41,45,47],
[69,49,72,0,68,58,62,53],
[68,33,50,33,0,51,50,43],
[55,46,60,43,50,0,52,43],
[41,52,56,39,51,49,0,50],
[65,58,54,48,58,58,51,0]])



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
result = np.append(np.array([8, 101, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,43,42,42,63,40],
[52,0,57,53,52,43,53,45],
[53,44,0,37,39,48,55,39],
[58,48,64,0,47,52,62,44],
[59,49,62,54,0,56,58,50],
[59,58,53,49,45,0,67,53],
[38,48,46,39,43,34,0,42],
[61,56,62,57,51,48,59,0]])



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
result = np.append(np.array([8, 101, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,67,85,75,53,70,47],
[31,0,42,55,63,36,39,29],
[34,59,0,57,68,47,67,52],
[16,46,44,0,80,45,66,40],
[26,38,33,21,0,38,37,41],
[48,65,54,56,63,0,73,48],
[31,62,34,35,64,28,0,36],
[54,72,49,61,60,53,65,0]])



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
result = np.append(np.array([8, 101, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,75,47,32,75,77,21],
[54,0,95,41,50,71,47,69],
[26,6,0,4,4,56,19,41],
[54,60,97,0,52,101,47,71],
[69,51,97,49,0,101,77,71],
[26,30,45,0,0,0,19,41],
[24,54,82,54,24,82,0,39],
[80,32,60,30,30,60,62,0]])



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
result = np.append(np.array([8, 101, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,71,71,79,50,71,71],
[30,0,54,71,84,50,54,29],
[30,47,0,76,84,55,54,51],
[30,30,25,0,59,8,33,37],
[22,17,17,42,0,50,25,29],
[51,51,46,93,51,0,54,51],
[30,47,47,68,76,47,0,76],
[30,72,50,64,72,50,25,0]])



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
result = np.append(np.array([8, 101, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,51,48,47,55,40],
[49,0,52,49,44,54,47,40],
[54,49,0,39,51,55,52,47],
[50,52,62,0,54,63,56,51],
[53,57,50,47,0,54,46,40],
[54,47,46,38,47,0,47,41],
[46,54,49,45,55,54,0,46],
[61,61,54,50,61,60,55,0]])



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
result = np.append(np.array([8, 101, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,49,57,57,59,58,55],
[42,0,44,48,42,49,44,40],
[52,57,0,52,47,43,51,46],
[44,53,49,0,48,45,43,54],
[44,59,54,53,0,49,64,54],
[42,52,58,56,52,0,58,55],
[43,57,50,58,37,43,0,58],
[46,61,55,47,47,46,43,0]])



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
result = np.append(np.array([8, 101, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,39,54,62,56,41,60],
[60,0,50,53,57,56,54,52],
[62,51,0,57,54,56,57,46],
[47,48,44,0,60,62,58,49],
[39,44,47,41,0,38,47,42],
[45,45,45,39,63,0,40,45],
[60,47,44,43,54,61,0,45],
[41,49,55,52,59,56,56,0]])



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
result = np.append(np.array([8, 101, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,44,52,50,53,51,66],
[53,0,39,54,44,48,43,50],
[57,62,0,43,52,47,44,64],
[49,47,58,0,40,48,46,60],
[51,57,49,61,0,49,47,63],
[48,53,54,53,52,0,59,67],
[50,58,57,55,54,42,0,58],
[35,51,37,41,38,34,43,0]])



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
result = np.append(np.array([8, 101, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,47,45,48,46,54],
[44,0,49,54,46,48,54,56],
[53,52,0,56,46,52,48,47],
[54,47,45,0,46,52,48,54],
[56,55,55,55,0,48,52,55],
[53,53,49,49,53,0,50,53],
[55,47,53,53,49,51,0,49],
[47,45,54,47,46,48,52,0]])



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
result = np.append(np.array([8, 101, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,55,39,71,55,69],
[48,0,42,61,69,60,72,44],
[45,59,0,46,56,62,57,46],
[46,40,55,0,38,70,71,38],
[62,32,45,63,0,47,72,31],
[30,41,39,31,54,0,55,41],
[46,29,44,30,29,46,0,44],
[32,57,55,63,70,60,57,0]])



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
result = np.append(np.array([8, 101, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,53,41,54,38,55,50],
[58,0,67,50,61,53,57,59],
[48,34,0,44,45,36,53,47],
[60,51,57,0,56,50,63,52],
[47,40,56,45,0,49,59,45],
[63,48,65,51,52,0,65,64],
[46,44,48,38,42,36,0,46],
[51,42,54,49,56,37,55,0]])



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
result = np.append(np.array([8, 101, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,69,52,49,55,49],
[47,0,45,71,42,60,58,54],
[50,56,0,68,37,43,45,47],
[32,30,33,0,20,43,52,44],
[49,59,64,81,0,63,69,63],
[52,41,58,58,38,0,51,52],
[46,43,56,49,32,50,0,39],
[52,47,54,57,38,49,62,0]])



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
result = np.append(np.array([8, 101, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,41,59,56,52,48,51],
[53,0,44,59,50,53,36,51],
[60,57,0,66,52,53,49,57],
[42,42,35,0,40,50,38,54],
[45,51,49,61,0,58,54,51],
[49,48,48,51,43,0,46,47],
[53,65,52,63,47,55,0,61],
[50,50,44,47,50,54,40,0]])



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
result = np.append(np.array([8, 101, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,47,43,49,47,44],
[45,0,46,55,49,47,47,55],
[45,55,0,49,51,49,47,48],
[54,46,52,0,46,50,43,50],
[58,52,50,55,0,47,53,50],
[52,54,52,51,54,0,48,55],
[54,54,54,58,48,53,0,57],
[57,46,53,51,51,46,44,0]])



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
result = np.append(np.array([8, 101, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,74,70,74,69,41,74],
[68,0,79,85,71,59,50,84],
[27,22,0,68,33,31,31,39],
[31,16,33,0,41,47,26,34],
[27,30,68,60,0,47,45,54],
[32,42,70,54,54,0,57,64],
[60,51,70,75,56,44,0,71],
[27,17,62,67,47,37,30,0]])



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
result = np.append(np.array([8, 101, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,49,50,44,53,45],
[54,0,50,51,49,54,52,52],
[56,51,0,48,53,55,49,48],
[52,50,53,0,51,52,56,47],
[51,52,48,50,0,54,53,54],
[57,47,46,49,47,0,56,50],
[48,49,52,45,48,45,0,51],
[56,49,53,54,47,51,50,0]])



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
result = np.append(np.array([8, 101, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,17,17,57,38,38,38],
[0,0,17,17,57,0,21,21],
[84,84,0,80,57,48,21,57],
[84,84,21,0,57,21,21,21],
[44,44,44,44,0,44,65,17],
[63,101,53,80,57,0,38,57],
[63,80,80,80,36,63,0,36],
[63,80,44,80,84,44,65,0]])



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
result = np.append(np.array([8, 101, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,68,54,63,63,54,53],
[51,0,55,60,59,56,62,44],
[33,46,0,47,52,50,42,38],
[47,41,54,0,50,51,43,38],
[38,42,49,51,0,66,58,44],
[38,45,51,50,35,0,44,57],
[47,39,59,58,43,57,0,54],
[48,57,63,63,57,44,47,0]])



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
result = np.append(np.array([8, 101, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,37,31,38,32,40,33],
[63,0,52,50,53,41,54,40],
[64,49,0,42,47,41,58,45],
[70,51,59,0,53,57,57,47],
[63,48,54,48,0,36,46,50],
[69,60,60,44,65,0,60,51],
[61,47,43,44,55,41,0,40],
[68,61,56,54,51,50,61,0]])



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
result = np.append(np.array([8, 101, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,45,52,46,50,49,42],
[59,0,54,57,52,60,50,53],
[56,47,0,63,71,59,49,48],
[49,44,38,0,52,61,40,41],
[55,49,30,49,0,54,47,50],
[51,41,42,40,47,0,41,36],
[52,51,52,61,54,60,0,50],
[59,48,53,60,51,65,51,0]])



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
result = np.append(np.array([8, 101, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,52,51,56,55,59],
[44,0,49,49,41,53,47,52],
[53,52,0,55,55,48,53,54],
[49,52,46,0,57,60,59,55],
[50,60,46,44,0,55,54,58],
[45,48,53,41,46,0,55,46],
[46,54,48,42,47,46,0,51],
[42,49,47,46,43,55,50,0]])



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
result = np.append(np.array([8, 101, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,48,57,57,60,51,55],
[39,0,40,44,53,47,40,48],
[53,61,0,61,56,71,54,49],
[44,57,40,0,63,57,50,56],
[44,48,45,38,0,54,34,49],
[41,54,30,44,47,0,34,38],
[50,61,47,51,67,67,0,57],
[46,53,52,45,52,63,44,0]])



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
result = np.append(np.array([8, 101, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,45,53,49,60,64,47],
[47,0,51,58,61,56,60,39],
[56,50,0,45,60,55,58,42],
[48,43,56,0,56,49,60,45],
[52,40,41,45,0,49,52,39],
[41,45,46,52,52,0,53,53],
[37,41,43,41,49,48,0,42],
[54,62,59,56,62,48,59,0]])



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
result = np.append(np.array([8, 101, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,51,56,39,49,56],
[48,0,55,56,63,40,58,58],
[56,46,0,55,63,63,64,70],
[50,45,46,0,45,45,47,47],
[45,38,38,56,0,41,43,45],
[62,61,38,56,60,0,62,60],
[52,43,37,54,58,39,0,53],
[45,43,31,54,56,41,48,0]])



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
result = np.append(np.array([8, 101, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,42,56,46,36,41,50],
[65,0,44,68,54,49,61,67],
[59,57,0,60,55,55,49,74],
[45,33,41,0,48,39,44,35],
[55,47,46,53,0,43,53,49],
[65,52,46,62,58,0,59,68],
[60,40,52,57,48,42,0,54],
[51,34,27,66,52,33,47,0]])



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
result = np.append(np.array([8, 101, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,45,46,52,47,54],
[57,0,55,47,51,58,43,57],
[49,46,0,55,44,55,43,54],
[56,54,46,0,54,51,49,52],
[55,50,57,47,0,46,39,56],
[49,43,46,50,55,0,45,46],
[54,58,58,52,62,56,0,49],
[47,44,47,49,45,55,52,0]])



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
result = np.append(np.array([8, 101, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_101.csv", index=False, header=False)