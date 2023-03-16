
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,28,22,34,22,31,29,28,23],
[22,0,27,26,27,28,29,27,28],
[28,23,0,31,22,24,19,27,28],
[16,24,19,0,19,23,25,22,20],
[28,23,28,31,0,28,24,30,29],
[19,22,26,27,22,0,21,27,23],
[21,21,31,25,26,29,0,32,30],
[22,23,23,28,20,23,18,0,23],
[27,22,22,30,21,27,20,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,21,26,19,27,29,30],
[25,0,20,23,26,21,25,34,25],
[22,30,0,21,23,22,23,34,20],
[29,27,29,0,26,25,24,34,24],
[24,24,27,24,0,28,30,28,20],
[31,29,28,25,22,0,29,33,18],
[23,25,27,26,20,21,0,32,23],
[21,16,16,16,22,17,18,0,14],
[20,25,30,26,30,32,27,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,25,29,25,29,22,28],
[24,0,23,33,31,27,25,23,23],
[26,27,0,32,25,29,24,24,28],
[25,17,18,0,27,27,32,25,24],
[21,19,25,23,0,22,29,19,27],
[25,23,21,23,28,0,24,21,28],
[21,25,26,18,21,26,0,23,27],
[28,27,26,25,31,29,27,0,24],
[22,27,22,26,23,22,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,31,26,30,19,17,31],
[20,0,19,25,24,16,16,15,25],
[23,31,0,21,19,32,29,29,30],
[19,25,29,0,29,18,29,26,34],
[24,26,31,21,0,20,26,31,35],
[20,34,18,32,30,0,26,19,32],
[31,34,21,21,24,24,0,23,28],
[33,35,21,24,19,31,27,0,26],
[19,25,20,16,15,18,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,32,31,25,29,31,34],
[25,0,17,27,32,27,30,28,33],
[24,33,0,32,20,24,24,28,32],
[18,23,18,0,27,27,26,25,36],
[19,18,30,23,0,24,26,37,32],
[25,23,26,23,26,0,24,23,32],
[21,20,26,24,24,26,0,22,27],
[19,22,22,25,13,27,28,0,33],
[16,17,18,14,18,18,23,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,21,36,27,27,34,25,29],
[17,0,20,19,24,24,27,21,22],
[29,30,0,32,32,23,39,31,24],
[14,31,18,0,27,26,27,27,32],
[23,26,18,23,0,22,31,20,31],
[23,26,27,24,28,0,35,31,21],
[16,23,11,23,19,15,0,25,18],
[25,29,19,23,30,19,25,0,24],
[21,28,26,18,19,29,32,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,30,29,32,26,31,32,29],
[33,0,36,35,33,33,30,24,31],
[20,14,0,32,30,9,19,9,26],
[21,15,18,0,26,18,28,18,24],
[18,17,20,24,0,4,23,26,11],
[24,17,41,32,46,0,38,30,45],
[19,20,31,22,27,12,0,18,20],
[18,26,41,32,24,20,32,0,26],
[21,19,24,26,39,5,30,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,23,29,26,26,28,26,27],
[20,0,18,25,23,26,21,19,22],
[27,32,0,30,28,25,26,31,27],
[21,25,20,0,20,26,22,17,18],
[24,27,22,30,0,29,23,26,20],
[24,24,25,24,21,0,22,24,31],
[22,29,24,28,27,28,0,26,22],
[24,31,19,33,24,26,24,0,23],
[23,28,23,32,30,19,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,21,14,15,21,6,0,29],
[50,0,29,25,44,50,35,36,40],
[29,21,0,35,29,44,35,21,35],
[36,25,15,0,36,36,42,25,34],
[35,6,21,14,0,39,24,0,14],
[29,0,6,14,11,0,14,0,14],
[44,15,15,8,26,36,0,15,23],
[50,14,29,25,50,50,35,0,40],
[21,10,15,16,36,36,27,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,25,28,26,31,22,26],
[24,0,19,24,24,25,26,21,22],
[25,31,0,24,29,23,30,26,24],
[25,26,26,0,30,27,26,26,27],
[22,26,21,20,0,24,24,24,25],
[24,25,27,23,26,0,23,27,28],
[19,24,20,24,26,27,0,19,25],
[28,29,24,24,26,23,31,0,18],
[24,28,26,23,25,22,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,28,26,34,24,27,35,19],
[20,0,31,31,29,30,22,33,22],
[22,19,0,29,23,22,23,23,21],
[24,19,21,0,27,20,21,32,25],
[16,21,27,23,0,25,22,31,16],
[26,20,28,30,25,0,25,26,20],
[23,28,27,29,28,25,0,29,31],
[15,17,27,18,19,24,21,0,14],
[31,28,29,25,34,30,19,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,29,25,24,22,27,24],
[27,0,24,25,22,22,25,25,22],
[26,26,0,22,19,24,22,26,24],
[21,25,28,0,22,28,22,20,22],
[25,28,31,28,0,25,28,27,21],
[26,28,26,22,25,0,24,28,24],
[28,25,28,28,22,26,0,24,25],
[23,25,24,30,23,22,26,0,22],
[26,28,26,28,29,26,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,24,25,26,23,26,26,19],
[35,0,29,30,28,25,31,27,26],
[26,21,0,32,25,27,30,25,25],
[25,20,18,0,25,23,30,24,23],
[24,22,25,25,0,28,26,28,32],
[27,25,23,27,22,0,29,29,23],
[24,19,20,20,24,21,0,26,22],
[24,23,25,26,22,21,24,0,27],
[31,24,25,27,18,27,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,33,32,32,32,27,25],
[18,0,34,30,30,32,32,25,34],
[24,16,0,23,22,22,25,7,27],
[17,20,27,0,25,21,29,15,28],
[18,20,28,25,0,37,25,31,21],
[18,18,28,29,13,0,30,20,23],
[18,18,25,21,25,20,0,17,12],
[23,25,43,35,19,30,33,0,30],
[25,16,23,22,29,27,38,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,45,33,32,28,28,28,32],
[35,0,36,46,22,35,19,41,35],
[5,14,0,27,18,23,19,27,28],
[17,4,23,0,23,23,15,20,32],
[18,28,32,27,0,18,15,23,31],
[22,15,27,27,32,0,6,31,23],
[22,31,31,35,35,44,0,31,34],
[22,9,23,30,27,19,19,0,18],
[18,15,22,18,19,27,16,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,33,32,26,29,18,17,18],
[26,0,30,33,29,31,24,23,26],
[17,20,0,27,25,24,19,16,19],
[18,17,23,0,23,22,19,14,14],
[24,21,25,27,0,25,21,17,26],
[21,19,26,28,25,0,23,15,14],
[32,26,31,31,29,27,0,24,26],
[33,27,34,36,33,35,26,0,20],
[32,24,31,36,24,36,24,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,35,28,31,28,28,23,25],
[23,0,23,26,24,27,30,21,25],
[15,27,0,21,22,20,26,21,20],
[22,24,29,0,24,23,28,24,21],
[19,26,28,26,0,23,26,20,22],
[22,23,30,27,27,0,27,23,25],
[22,20,24,22,24,23,0,20,16],
[27,29,29,26,30,27,30,0,23],
[25,25,30,29,28,25,34,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,16,27,22,24,24,36,20],
[6,0,12,12,10,19,19,20,15],
[34,38,0,38,29,35,20,40,31],
[23,38,12,0,18,28,24,32,19],
[28,40,21,32,0,28,20,36,17],
[26,31,15,22,22,0,24,36,12],
[26,31,30,26,30,26,0,31,11],
[14,30,10,18,14,14,19,0,23],
[30,35,19,31,33,38,39,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,24,21,36,43,28,37,25],
[11,0,17,12,28,25,35,26,22],
[26,33,0,29,36,38,31,29,25],
[29,38,21,0,27,28,36,23,20],
[14,22,14,23,0,36,28,24,22],
[7,25,12,22,14,0,27,18,9],
[22,15,19,14,22,23,0,25,13],
[13,24,21,27,26,32,25,0,26],
[25,28,25,30,28,41,37,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,25,24,21,25,23,19],
[31,0,29,29,29,22,28,25,22],
[28,21,0,28,25,25,22,27,21],
[25,21,22,0,24,20,29,25,17],
[26,21,25,26,0,23,26,22,19],
[29,28,25,30,27,0,31,27,27],
[25,22,28,21,24,19,0,23,19],
[27,25,23,25,28,23,27,0,20],
[31,28,29,33,31,23,31,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,32,10,17,24,17,38,24],
[18,0,14,18,17,12,18,21,17],
[18,36,0,24,25,25,16,32,21],
[40,32,26,0,23,27,27,42,26],
[33,33,25,27,0,39,17,37,38],
[26,38,25,23,11,0,26,38,27],
[33,32,34,23,33,24,0,33,37],
[12,29,18,8,13,12,17,0,9],
[26,33,29,24,12,23,13,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,22,26,23,22,26,32,26],
[35,0,25,32,23,29,28,34,26],
[28,25,0,29,26,26,23,30,25],
[24,18,21,0,25,25,19,24,17],
[27,27,24,25,0,25,26,29,24],
[28,21,24,25,25,0,24,29,28],
[24,22,27,31,24,26,0,29,24],
[18,16,20,26,21,21,21,0,23],
[24,24,25,33,26,22,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,14,29,20,27,26,26,32],
[17,0,8,18,4,15,17,14,26],
[36,42,0,30,31,22,39,21,33],
[21,32,20,0,19,32,20,18,37],
[30,46,19,31,0,26,31,19,40],
[23,35,28,18,24,0,28,20,35],
[24,33,11,30,19,22,0,15,22],
[24,36,29,32,31,30,35,0,35],
[18,24,17,13,10,15,28,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,17,11,18,20,15,13],
[31,0,14,14,24,26,24,18,21],
[32,36,0,26,26,30,37,25,30],
[33,36,24,0,23,28,30,28,23],
[39,26,24,27,0,26,25,13,24],
[32,24,20,22,24,0,27,20,23],
[30,26,13,20,25,23,0,15,12],
[35,32,25,22,37,30,35,0,30],
[37,29,20,27,26,27,38,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,25,32,26,33,32,27],
[19,0,22,27,27,24,26,23,22],
[23,28,0,24,31,28,30,34,29],
[25,23,26,0,32,27,29,28,28],
[18,23,19,18,0,17,23,24,20],
[24,26,22,23,33,0,30,32,26],
[17,24,20,21,27,20,0,26,26],
[18,27,16,22,26,18,24,0,23],
[23,28,21,22,30,24,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,20,23,24,22,14,26,33],
[18,0,26,9,13,16,11,12,29],
[30,24,0,18,24,35,21,11,32],
[27,41,32,0,18,29,31,21,37],
[26,37,26,32,0,32,22,19,29],
[28,34,15,21,18,0,21,21,31],
[36,39,29,19,28,29,0,24,32],
[24,38,39,29,31,29,26,0,32],
[17,21,18,13,21,19,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,38,19,30,21,39,23,36],
[12,0,27,8,6,20,21,12,12],
[12,23,0,23,18,13,24,23,12],
[31,42,27,0,43,20,43,31,38],
[20,44,32,7,0,21,21,22,12],
[29,30,37,30,29,0,45,22,35],
[11,29,26,7,29,5,0,22,24],
[27,38,27,19,28,28,28,0,24],
[14,38,38,12,38,15,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,10,18,13,18,21,17,18],
[31,0,15,30,26,21,29,29,24],
[40,35,0,33,29,26,34,22,35],
[32,20,17,0,20,19,22,19,17],
[37,24,21,30,0,25,33,25,22],
[32,29,24,31,25,0,28,28,25],
[29,21,16,28,17,22,0,16,29],
[33,21,28,31,25,22,34,0,26],
[32,26,15,33,28,25,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,36,28,28,30,32,22,32],
[11,0,23,19,26,13,28,12,28],
[14,27,0,14,29,14,37,15,22],
[22,31,36,0,41,24,38,27,38],
[22,24,21,9,0,15,19,17,31],
[20,37,36,26,35,0,39,26,32],
[18,22,13,12,31,11,0,18,22],
[28,38,35,23,33,24,32,0,29],
[18,22,28,12,19,18,28,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,29,22,22,36,30,26],
[16,0,15,24,28,15,33,24,25],
[16,35,0,27,28,24,36,28,25],
[21,26,23,0,25,28,33,22,18],
[28,22,22,25,0,26,37,21,29],
[28,35,26,22,24,0,36,27,30],
[14,17,14,17,13,14,0,17,19],
[20,26,22,28,29,23,33,0,27],
[24,25,25,32,21,20,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,31,37,44,24,39,27,27],
[26,0,8,19,37,21,28,9,22],
[19,42,0,25,38,38,33,17,26],
[13,31,25,0,32,29,24,26,22],
[6,13,12,18,0,7,20,7,22],
[26,29,12,21,43,0,36,21,26],
[11,22,17,26,30,14,0,24,26],
[23,41,33,24,43,29,26,0,27],
[23,28,24,28,28,24,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,26,31,20,28,30,29],
[23,0,28,24,23,26,20,26,30],
[22,22,0,19,24,21,27,27,33],
[24,26,31,0,26,22,30,34,23],
[19,27,26,24,0,17,19,31,20],
[30,24,29,28,33,0,28,34,31],
[22,30,23,20,31,22,0,33,21],
[20,24,23,16,19,16,17,0,21],
[21,20,17,27,30,19,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,23,20,20,22,21,17],
[28,0,29,22,21,25,23,25,21],
[28,21,0,20,21,20,15,24,19],
[27,28,30,0,28,23,20,26,22],
[30,29,29,22,0,23,27,24,21],
[30,25,30,27,27,0,23,30,24],
[28,27,35,30,23,27,0,28,27],
[29,25,26,24,26,20,22,0,24],
[33,29,31,28,29,26,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,23,22,25,24,25,30],
[23,0,21,22,19,18,24,21,24],
[23,29,0,20,17,24,29,22,29],
[27,28,30,0,24,24,26,24,26],
[28,31,33,26,0,30,27,24,31],
[25,32,26,26,20,0,24,25,30],
[26,26,21,24,23,26,0,23,28],
[25,29,28,26,26,25,27,0,29],
[20,26,21,24,19,20,22,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,29,28,28,36,28,26,34],
[30,0,25,32,23,31,27,31,32],
[21,25,0,24,24,28,21,25,31],
[22,18,26,0,19,32,25,21,29],
[22,27,26,31,0,37,31,21,28],
[14,19,22,18,13,0,16,13,24],
[22,23,29,25,19,34,0,23,33],
[24,19,25,29,29,37,27,0,30],
[16,18,19,21,22,26,17,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,10,15,24,13,20,9],
[38,0,32,19,20,38,32,28,40],
[43,18,0,23,32,31,31,37,34],
[40,31,27,0,24,36,37,35,38],
[35,30,18,26,0,26,37,25,39],
[26,12,19,14,24,0,18,14,25],
[37,18,19,13,13,32,0,16,27],
[30,22,13,15,25,36,34,0,25],
[41,10,16,12,11,25,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,22,28,27,29,25,28],
[25,0,25,30,30,35,33,28,32],
[26,25,0,28,27,29,31,29,33],
[28,20,22,0,26,30,29,26,28],
[22,20,23,24,0,29,27,29,29],
[23,15,21,20,21,0,23,22,28],
[21,17,19,21,23,27,0,24,31],
[25,22,21,24,21,28,26,0,31],
[22,18,17,22,21,22,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,25,25,24,21,25,26],
[25,0,16,21,27,15,16,14,18],
[28,34,0,29,27,23,24,25,24],
[25,29,21,0,24,21,22,20,24],
[25,23,23,26,0,24,18,22,23],
[26,35,27,29,26,0,22,27,26],
[29,34,26,28,32,28,0,23,25],
[25,36,25,30,28,23,27,0,22],
[24,32,26,26,27,24,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,31,30,21,27,33,26],
[24,0,26,25,23,21,26,19,23],
[30,24,0,30,30,26,28,32,26],
[19,25,20,0,21,19,16,17,16],
[20,27,20,29,0,18,21,25,20],
[29,29,24,31,32,0,23,30,27],
[23,24,22,34,29,27,0,28,30],
[17,31,18,33,25,20,22,0,29],
[24,27,24,34,30,23,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,30,12,9,16,17,25,18],
[34,0,42,33,30,21,33,41,24],
[20,8,0,20,12,24,20,28,5],
[38,17,30,0,25,19,23,34,20],
[41,20,38,25,0,21,29,33,36],
[34,29,26,31,29,0,29,34,21],
[33,17,30,27,21,21,0,27,19],
[25,9,22,16,17,16,23,0,25],
[32,26,45,30,14,29,31,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,22,28,29,25,28,25],
[22,0,28,18,24,21,20,20,22],
[21,22,0,18,21,25,21,24,22],
[28,32,32,0,30,22,25,30,27],
[22,26,29,20,0,26,23,24,23],
[21,29,25,28,24,0,22,31,25],
[25,30,29,25,27,28,0,30,26],
[22,30,26,20,26,19,20,0,27],
[25,28,28,23,27,25,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,22,21,15,6,32,19,12],
[45,0,31,39,24,20,42,27,26],
[28,19,0,40,31,27,32,20,19],
[29,11,10,0,9,17,31,4,9],
[35,26,19,41,0,33,32,11,26],
[44,30,23,33,17,0,34,19,28],
[18,8,18,19,18,16,0,2,8],
[31,23,30,46,39,31,48,0,31],
[38,24,31,41,24,22,42,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,16,33,26,32,33,26,39],
[17,0,33,23,26,32,32,43,39],
[34,17,0,27,37,36,37,33,33],
[17,27,23,0,27,33,43,33,39],
[24,24,13,23,0,23,33,33,29],
[18,18,14,17,27,0,27,33,19],
[17,18,13,7,17,23,0,27,23],
[24,7,17,17,17,17,23,0,23],
[11,11,17,11,21,31,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,30,25,27,27,31,24,26],
[23,0,20,25,23,24,28,19,22],
[20,30,0,25,32,26,29,27,29],
[25,25,25,0,33,28,30,22,28],
[23,27,18,17,0,23,26,21,26],
[23,26,24,22,27,0,24,21,23],
[19,22,21,20,24,26,0,18,23],
[26,31,23,28,29,29,32,0,28],
[24,28,21,22,24,27,27,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,29,21,30,32,28,22],
[19,0,28,21,26,24,31,33,33],
[20,22,0,25,18,26,26,24,29],
[21,29,25,0,19,25,28,28,18],
[29,24,32,31,0,35,33,39,30],
[20,26,24,25,15,0,24,25,26],
[18,19,24,22,17,26,0,28,21],
[22,17,26,22,11,25,22,0,21],
[28,17,21,32,20,24,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,25,28,31,29,28,29],
[24,0,27,23,25,25,23,29,22],
[22,23,0,16,29,32,26,30,24],
[25,27,34,0,24,31,28,30,19],
[22,25,21,26,0,26,26,25,20],
[19,25,18,19,24,0,20,23,18],
[21,27,24,22,24,30,0,30,22],
[22,21,20,20,25,27,20,0,19],
[21,28,26,31,30,32,28,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,17,21,4,18,11,14,15],
[27,0,18,35,14,35,23,27,17],
[33,32,0,39,19,22,23,31,24],
[29,15,11,0,3,17,12,19,19],
[46,36,31,47,0,26,25,33,25],
[32,15,28,33,24,0,19,32,24],
[39,27,27,38,25,31,0,36,30],
[36,23,19,31,17,18,14,0,26],
[35,33,26,31,25,26,20,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,23,21,24,23,21,20],
[26,0,28,31,26,27,26,27,25],
[27,22,0,27,20,25,21,25,23],
[27,19,23,0,24,23,19,21,19],
[29,24,30,26,0,20,26,25,22],
[26,23,25,27,30,0,23,22,22],
[27,24,29,31,24,27,0,24,24],
[29,23,25,29,25,28,26,0,27],
[30,25,27,31,28,28,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,34,16,0,16,16,16,16],
[34,0,24,24,34,40,40,24,40],
[16,26,0,32,16,22,22,32,32],
[34,26,18,0,10,22,22,34,32],
[50,16,34,40,0,40,22,40,40],
[34,10,28,28,10,0,6,34,26],
[34,10,28,28,28,44,0,28,44],
[34,26,18,16,10,16,22,0,16],
[34,10,18,18,10,24,6,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,25,23,24,29,21,30],
[27,0,26,28,29,28,30,25,29],
[26,24,0,29,24,25,26,18,25],
[25,22,21,0,23,24,20,19,23],
[27,21,26,27,0,23,28,22,24],
[26,22,25,26,27,0,22,22,25],
[21,20,24,30,22,28,0,24,22],
[29,25,32,31,28,28,26,0,26],
[20,21,25,27,26,25,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,37,36,31,23,18,31,37],
[14,0,45,50,31,31,26,45,45],
[13,5,0,36,23,31,26,36,29],
[14,0,14,0,18,26,26,24,24],
[19,19,27,32,0,31,8,45,32],
[27,19,19,24,19,0,13,37,37],
[32,24,24,24,42,37,0,42,42],
[19,5,14,26,5,13,8,0,32],
[13,5,21,26,18,13,8,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,21,26,27,24,27,20],
[30,0,22,26,31,28,31,27,24],
[28,28,0,25,32,26,32,31,23],
[29,24,25,0,30,30,32,30,29],
[24,19,18,20,0,26,27,23,17],
[23,22,24,20,24,0,27,26,20],
[26,19,18,18,23,23,0,25,20],
[23,23,19,20,27,24,25,0,19],
[30,26,27,21,33,30,30,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,21,26,30,32,29,26],
[19,0,21,17,20,22,22,24,17],
[23,29,0,19,15,22,25,23,17],
[29,33,31,0,29,31,36,35,18],
[24,30,35,21,0,25,28,32,20],
[20,28,28,19,25,0,29,24,22],
[18,28,25,14,22,21,0,25,17],
[21,26,27,15,18,26,25,0,15],
[24,33,33,32,30,28,33,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,21,25,27,20,15,26,14],
[34,0,27,29,25,30,24,22,25],
[29,23,0,36,30,32,25,31,23],
[25,21,14,0,22,19,27,19,11],
[23,25,20,28,0,23,23,23,15],
[30,20,18,31,27,0,25,33,18],
[35,26,25,23,27,25,0,30,20],
[24,28,19,31,27,17,20,0,5],
[36,25,27,39,35,32,30,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,22,27,25,25,20,12,19],
[37,0,31,26,35,38,25,31,32],
[28,19,0,21,24,31,23,20,18],
[23,24,29,0,29,28,23,14,29],
[25,15,26,21,0,32,25,20,22],
[25,12,19,22,18,0,15,11,13],
[30,25,27,27,25,35,0,14,22],
[38,19,30,36,30,39,36,0,35],
[31,18,32,21,28,37,28,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,35,37,35,21,28,36,31],
[23,0,30,25,30,25,32,35,28],
[15,20,0,29,30,19,23,30,32],
[13,25,21,0,27,16,29,30,22],
[15,20,20,23,0,21,26,25,21],
[29,25,31,34,29,0,26,27,25],
[22,18,27,21,24,24,0,30,25],
[14,15,20,20,25,23,20,0,17],
[19,22,18,28,29,25,25,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,27,28,33,26,35,27,25],
[17,0,23,28,20,23,22,19,20],
[23,27,0,31,29,29,24,27,27],
[22,22,19,0,31,24,24,23,19],
[17,30,21,19,0,23,18,14,20],
[24,27,21,26,27,0,24,28,26],
[15,28,26,26,32,26,0,21,20],
[23,31,23,27,36,22,29,0,26],
[25,30,23,31,30,24,30,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,27,25,24,27,21,21],
[26,0,20,33,31,16,29,18,24],
[25,30,0,33,27,23,20,21,24],
[23,17,17,0,26,20,23,18,15],
[25,19,23,24,0,22,26,20,14],
[26,34,27,30,28,0,25,19,26],
[23,21,30,27,24,25,0,18,18],
[29,32,29,32,30,31,32,0,22],
[29,26,26,35,36,24,32,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,21,27,23,23,23,17],
[27,0,29,27,28,27,27,26,20],
[25,21,0,22,20,21,23,18,19],
[29,23,28,0,27,27,24,24,22],
[23,22,30,23,0,23,20,21,20],
[27,23,29,23,27,0,27,23,16],
[27,23,27,26,30,23,0,24,24],
[27,24,32,26,29,27,26,0,26],
[33,30,31,28,30,34,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,31,26,30,27,23,28,29],
[20,0,29,20,25,25,25,26,21],
[19,21,0,21,21,26,20,30,25],
[24,30,29,0,28,26,29,26,23],
[20,25,29,22,0,24,21,23,21],
[23,25,24,24,26,0,22,31,23],
[27,25,30,21,29,28,0,27,21],
[22,24,20,24,27,19,23,0,23],
[21,29,25,27,29,27,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,29,23,25,28,27,30],
[23,0,23,27,24,22,24,25,22],
[29,27,0,31,28,24,31,26,26],
[21,23,19,0,23,19,25,22,22],
[27,26,22,27,0,24,26,28,24],
[25,28,26,31,26,0,29,25,24],
[22,26,19,25,24,21,0,24,23],
[23,25,24,28,22,25,26,0,22],
[20,28,24,28,26,26,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,19,24,21,23,21,26,26],
[25,0,25,24,23,20,23,30,27],
[31,25,0,28,29,27,25,31,28],
[26,26,22,0,27,23,28,33,27],
[29,27,21,23,0,24,22,33,23],
[27,30,23,27,26,0,25,33,27],
[29,27,25,22,28,25,0,29,21],
[24,20,19,17,17,17,21,0,27],
[24,23,22,23,27,23,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,29,29,26,24,17,22,33],
[30,0,29,38,29,20,24,25,32],
[21,21,0,27,26,26,23,19,26],
[21,12,23,0,14,18,23,16,20],
[24,21,24,36,0,24,24,16,31],
[26,30,24,32,26,0,27,22,25],
[33,26,27,27,26,23,0,20,33],
[28,25,31,34,34,28,30,0,39],
[17,18,24,30,19,25,17,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,20,29,29,20,18,32,19],
[18,0,24,24,24,26,26,31,21],
[30,26,0,34,40,23,23,26,28],
[21,26,16,0,26,25,15,31,20],
[21,26,10,24,0,23,13,24,24],
[30,24,27,25,27,0,20,28,19],
[32,24,27,35,37,30,0,25,26],
[18,19,24,19,26,22,25,0,13],
[31,29,22,30,26,31,24,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,26,28,26,23,30,28],
[22,0,21,29,26,27,26,24,21],
[19,29,0,22,23,29,22,23,18],
[24,21,28,0,28,31,22,30,20],
[22,24,27,22,0,30,23,23,19],
[24,23,21,19,20,0,23,21,18],
[27,24,28,28,27,27,0,27,28],
[20,26,27,20,27,29,23,0,23],
[22,29,32,30,31,32,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,25,25,26,24,33,24],
[29,0,26,24,27,29,22,31,24],
[26,24,0,24,27,27,21,28,23],
[25,26,26,0,26,28,20,24,29],
[25,23,23,24,0,23,27,25,22],
[24,21,23,22,27,0,20,27,24],
[26,28,29,30,23,30,0,30,27],
[17,19,22,26,25,23,20,0,19],
[26,26,27,21,28,26,23,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,28,30,23,21,27,28],
[24,0,21,20,23,21,18,20,21],
[22,29,0,27,26,27,22,30,21],
[22,30,23,0,26,24,20,24,25],
[20,27,24,24,0,24,20,28,24],
[27,29,23,26,26,0,25,27,26],
[29,32,28,30,30,25,0,27,25],
[23,30,20,26,22,23,23,0,19],
[22,29,29,25,26,24,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,32,34,33,31,37,35,32],
[26,0,33,32,25,23,33,25,29],
[18,17,0,17,21,13,22,27,21],
[16,18,33,0,21,19,22,20,15],
[17,25,29,29,0,22,28,23,27],
[19,27,37,31,28,0,27,30,28],
[13,17,28,28,22,23,0,25,25],
[15,25,23,30,27,20,25,0,28],
[18,21,29,35,23,22,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,30,27,27,29,22,30],
[25,0,27,28,22,33,26,26,28],
[22,23,0,26,21,32,25,15,29],
[20,22,24,0,23,24,27,17,30],
[23,28,29,27,0,30,27,16,31],
[23,17,18,26,20,0,21,18,27],
[21,24,25,23,23,29,0,17,29],
[28,24,35,33,34,32,33,0,35],
[20,22,21,20,19,23,21,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,28,27,22,33,27,29],
[23,0,21,19,17,18,27,19,24],
[27,29,0,27,23,27,33,22,26],
[22,31,23,0,24,19,30,24,26],
[23,33,27,26,0,23,32,28,34],
[28,32,23,31,27,0,34,24,29],
[17,23,17,20,18,16,0,24,23],
[23,31,28,26,22,26,26,0,27],
[21,26,24,24,16,21,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,37,31,23,28,34,16],
[27,0,15,28,24,25,17,28,26],
[25,35,0,36,32,28,35,32,27],
[13,22,14,0,19,18,23,19,14],
[19,26,18,31,0,27,31,25,19],
[27,25,22,32,23,0,22,28,20],
[22,33,15,27,19,28,0,29,25],
[16,22,18,31,25,22,21,0,17],
[34,24,23,36,31,30,25,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,29,27,24,26,33,26],
[25,0,23,28,21,25,29,28,26],
[25,27,0,25,22,19,29,27,24],
[21,22,25,0,20,19,25,31,18],
[23,29,28,30,0,22,28,30,26],
[26,25,31,31,28,0,24,34,32],
[24,21,21,25,22,26,0,37,26],
[17,22,23,19,20,16,13,0,17],
[24,24,26,32,24,18,24,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,34,28,21,17,29,19],
[31,0,30,19,27,14,27,20,30],
[28,20,0,35,27,29,25,24,39],
[16,31,15,0,24,21,17,11,19],
[22,23,23,26,0,20,10,22,28],
[29,36,21,29,30,0,22,19,24],
[33,23,25,33,40,28,0,30,34],
[21,30,26,39,28,31,20,0,21],
[31,20,11,31,22,26,16,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,26,29,25,28,21,25],
[24,0,29,22,23,22,26,20,20],
[24,21,0,17,24,22,26,17,25],
[24,28,33,0,26,26,26,23,22],
[21,27,26,24,0,26,26,22,24],
[25,28,28,24,24,0,25,18,21],
[22,24,24,24,24,25,0,18,22],
[29,30,33,27,28,32,32,0,25],
[25,30,25,28,26,29,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,28,24,25,28,21,25],
[27,0,26,26,26,26,28,24,29],
[26,24,0,28,29,25,31,30,28],
[22,24,22,0,22,27,28,23,19],
[26,24,21,28,0,26,26,27,23],
[25,24,25,23,24,0,28,23,26],
[22,22,19,22,24,22,0,23,23],
[29,26,20,27,23,27,27,0,25],
[25,21,22,31,27,24,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,25,23,24,23,22,25],
[28,0,18,28,20,27,23,23,22],
[24,32,0,29,31,30,25,26,28],
[25,22,21,0,22,24,25,24,22],
[27,30,19,28,0,23,23,20,24],
[26,23,20,26,27,0,26,21,25],
[27,27,25,25,27,24,0,27,27],
[28,27,24,26,30,29,23,0,24],
[25,28,22,28,26,25,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,22,26,25,24,29,24,31],
[20,0,14,23,31,16,20,16,26],
[28,36,0,23,28,21,33,28,32],
[24,27,27,0,29,25,28,28,33],
[25,19,22,21,0,15,25,20,26],
[26,34,29,25,35,0,22,27,34],
[21,30,17,22,25,28,0,21,29],
[26,34,22,22,30,23,29,0,37],
[19,24,18,17,24,16,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,23,28,25,32,21,20,26],
[20,0,25,24,24,24,22,22,18],
[27,25,0,24,23,26,29,22,23],
[22,26,26,0,23,27,24,19,23],
[25,26,27,27,0,27,29,25,21],
[18,26,24,23,23,0,21,24,21],
[29,28,21,26,21,29,0,21,26],
[30,28,28,31,25,26,29,0,22],
[24,32,27,27,29,29,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,17,21,19,26,26,22,20],
[27,0,21,23,27,31,32,27,24],
[33,29,0,26,24,32,33,31,28],
[29,27,24,0,23,27,30,26,28],
[31,23,26,27,0,25,35,23,26],
[24,19,18,23,25,0,31,25,22],
[24,18,17,20,15,19,0,20,18],
[28,23,19,24,27,25,30,0,27],
[30,26,22,22,24,28,32,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,31,16,31,22,22,16,25],
[14,0,30,26,15,14,20,18,14],
[19,20,0,17,20,11,11,11,16],
[34,24,33,0,24,31,33,26,33],
[19,35,30,26,0,26,32,35,26],
[28,36,39,19,24,0,38,32,44],
[28,30,39,17,18,12,0,23,32],
[34,32,39,24,15,18,27,0,33],
[25,36,34,17,24,6,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,37,41,21,40,36,33,27],
[28,0,28,34,25,35,32,21,22],
[13,22,0,27,19,27,25,12,18],
[9,16,23,0,16,17,12,12,12],
[29,25,31,34,0,33,37,28,24],
[10,15,23,33,17,0,20,11,17],
[14,18,25,38,13,30,0,20,20],
[17,29,38,38,22,39,30,0,22],
[23,28,32,38,26,33,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,14,21,19,4,11,19],
[39,0,23,24,30,26,17,28,26],
[35,27,0,29,29,24,27,14,23],
[36,26,21,0,35,26,15,23,32],
[29,20,21,15,0,25,14,27,14],
[31,24,26,24,25,0,19,21,26],
[46,33,23,35,36,31,0,24,33],
[39,22,36,27,23,29,26,0,23],
[31,24,27,18,36,24,17,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,21,25,21,22,24,15],
[28,0,26,26,30,24,23,24,19],
[28,24,0,22,30,23,21,27,19],
[29,24,28,0,32,27,21,29,17],
[25,20,20,18,0,23,13,22,11],
[29,26,27,23,27,0,21,27,24],
[28,27,29,29,37,29,0,33,25],
[26,26,23,21,28,23,17,0,14],
[35,31,31,33,39,26,25,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,32,27,23,27,23,29],
[25,0,23,29,34,25,27,28,20],
[25,27,0,28,31,21,29,26,24],
[18,21,22,0,24,17,20,21,18],
[23,16,19,26,0,18,25,24,21],
[27,25,29,33,32,0,36,27,26],
[23,23,21,30,25,14,0,23,24],
[27,22,24,29,26,23,27,0,22],
[21,30,26,32,29,24,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,20,25,28,31,18,17],
[24,0,24,24,32,27,25,27,25],
[18,26,0,30,21,33,25,22,22],
[30,26,20,0,23,31,28,20,20],
[25,18,29,27,0,25,27,18,15],
[22,23,17,19,25,0,28,20,18],
[19,25,25,22,23,22,0,14,15],
[32,23,28,30,32,30,36,0,21],
[33,25,28,30,35,32,35,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,24,11,24,20,17,21,21],
[7,0,7,11,20,7,17,11,21],
[26,43,0,21,20,20,17,21,21],
[39,39,29,0,13,20,17,21,14],
[26,30,30,37,0,23,33,37,37],
[30,43,30,30,27,0,21,14,14],
[33,33,33,33,17,29,0,33,17],
[29,39,29,29,13,36,17,0,23],
[29,29,29,36,13,36,33,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,29,31,33,32,17,35,27],
[27,0,22,32,22,22,25,37,26],
[21,28,0,28,24,32,19,35,23],
[19,18,22,0,24,14,27,30,13],
[17,28,26,26,0,19,21,31,19],
[18,28,18,36,31,0,21,32,20],
[33,25,31,23,29,29,0,36,24],
[15,13,15,20,19,18,14,0,21],
[23,24,27,37,31,30,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,22,24,21,27,28,23],
[26,0,24,22,24,25,25,28,27],
[26,26,0,24,25,28,23,29,27],
[28,28,26,0,25,32,28,28,29],
[26,26,25,25,0,26,29,25,27],
[29,25,22,18,24,0,25,26,28],
[23,25,27,22,21,25,0,25,29],
[22,22,21,22,25,24,25,0,28],
[27,23,23,21,23,22,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,27,22,22,24,20,26],
[24,0,25,27,22,27,25,25,27],
[22,25,0,25,18,19,24,22,27],
[23,23,25,0,21,22,22,22,23],
[28,28,32,29,0,25,27,26,26],
[28,23,31,28,25,0,30,21,28],
[26,25,26,28,23,20,0,21,23],
[30,25,28,28,24,29,29,0,27],
[24,23,23,27,24,22,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,22,26,17,16,17,22,11],
[37,0,30,35,27,28,27,35,24],
[28,20,0,26,22,26,22,24,17],
[24,15,24,0,21,22,20,29,16],
[33,23,28,29,0,26,28,35,22],
[34,22,24,28,24,0,23,31,17],
[33,23,28,30,22,27,0,34,25],
[28,15,26,21,15,19,16,0,13],
[39,26,33,34,28,33,25,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,22,18,20,32,26,27],
[28,0,24,22,22,19,32,23,25],
[31,26,0,26,26,24,29,23,25],
[28,28,24,0,22,22,34,24,28],
[32,28,24,28,0,24,33,28,26],
[30,31,26,28,26,0,34,24,27],
[18,18,21,16,17,16,0,19,20],
[24,27,27,26,22,26,31,0,28],
[23,25,25,22,24,23,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,23,22,21,20,20,20],
[29,0,12,27,20,18,22,23,22],
[29,38,0,31,32,27,25,31,29],
[27,23,19,0,22,12,18,20,21],
[28,30,18,28,0,15,22,25,24],
[29,32,23,38,35,0,25,28,29],
[30,28,25,32,28,25,0,24,26],
[30,27,19,30,25,22,26,0,30],
[30,28,21,29,26,21,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,26,34,23,28,18,29],
[23,0,27,31,28,27,28,22,28],
[26,23,0,27,31,27,30,25,26],
[24,19,23,0,29,23,21,22,27],
[16,22,19,21,0,22,20,15,22],
[27,23,23,27,28,0,25,22,24],
[22,22,20,29,30,25,0,25,28],
[32,28,25,28,35,28,25,0,33],
[21,22,24,23,28,26,22,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,23,25,28,25,28,32],
[27,0,29,24,20,31,30,33,32],
[24,21,0,22,17,27,25,27,24],
[27,26,28,0,17,28,32,31,35],
[25,30,33,33,0,29,28,29,29],
[22,19,23,22,21,0,24,18,31],
[25,20,25,18,22,26,0,25,24],
[22,17,23,19,21,32,25,0,23],
[18,18,26,15,21,19,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,21,21,21,20,20,18],
[31,0,24,32,29,28,27,24,23],
[32,26,0,32,28,17,26,22,18],
[29,18,18,0,31,27,18,29,19],
[29,21,22,19,0,27,28,21,15],
[29,22,33,23,23,0,26,26,18],
[30,23,24,32,22,24,0,33,25],
[30,26,28,21,29,24,17,0,24],
[32,27,32,31,35,32,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,18,20,23,27,26,12,7],
[22,0,17,23,35,22,26,23,23],
[32,33,0,20,40,40,24,29,24],
[30,27,30,0,26,26,31,32,19],
[27,15,10,24,0,10,18,17,10],
[23,28,10,24,40,0,19,24,24],
[24,24,26,19,32,31,0,24,25],
[38,27,21,18,33,26,26,0,19],
[43,27,26,31,40,26,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,27,25,32,29,25,28],
[24,0,24,27,30,38,20,30,24],
[22,26,0,23,21,30,25,22,30],
[23,23,27,0,26,33,30,28,24],
[25,20,29,24,0,32,29,33,30],
[18,12,20,17,18,0,17,25,20],
[21,30,25,20,21,33,0,27,23],
[25,20,28,22,17,25,23,0,29],
[22,26,20,26,20,30,27,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,25,28,31,27,32,28,34],
[18,0,17,21,23,19,22,23,28],
[25,33,0,32,28,30,25,30,35],
[22,29,18,0,21,28,23,22,30],
[19,27,22,29,0,25,22,27,22],
[23,31,20,22,25,0,23,25,27],
[18,28,25,27,28,27,0,29,27],
[22,27,20,28,23,25,21,0,28],
[16,22,15,20,28,23,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,18,29,25,31,35,33,27],
[24,0,19,19,15,27,21,31,18],
[32,31,0,21,22,29,27,32,30],
[21,31,29,0,19,32,25,24,24],
[25,35,28,31,0,35,25,27,27],
[19,23,21,18,15,0,15,27,12],
[15,29,23,25,25,35,0,27,21],
[17,19,18,26,23,23,23,0,18],
[23,32,20,26,23,38,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,29,30,29,33,21,27],
[22,0,21,29,27,26,31,28,23],
[24,29,0,22,19,17,26,24,26],
[21,21,28,0,31,30,29,27,24],
[20,23,31,19,0,22,28,15,24],
[21,24,33,20,28,0,21,26,22],
[17,19,24,21,22,29,0,20,24],
[29,22,26,23,35,24,30,0,24],
[23,27,24,26,26,28,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,25,31,32,27,22,25],
[19,0,24,23,22,28,22,21,26],
[20,26,0,22,27,30,27,25,25],
[25,27,28,0,25,31,28,26,26],
[19,28,23,25,0,28,29,21,22],
[18,22,20,19,22,0,23,18,18],
[23,28,23,22,21,27,0,22,25],
[28,29,25,24,29,32,28,0,27],
[25,24,25,24,28,32,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,25,29,27,25,25,32,28],
[17,0,23,21,20,19,23,24,17],
[25,27,0,27,24,29,26,25,28],
[21,29,23,0,28,25,23,27,28],
[23,30,26,22,0,20,23,30,28],
[25,31,21,25,30,0,24,28,26],
[25,27,24,27,27,26,0,29,29],
[18,26,25,23,20,22,21,0,25],
[22,33,22,22,22,24,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,26,31,28,36,25,26],
[28,0,29,25,34,30,37,25,37],
[22,21,0,31,26,22,32,23,23],
[24,25,19,0,20,26,30,20,23],
[19,16,24,30,0,16,33,19,24],
[22,20,28,24,34,0,32,24,27],
[14,13,18,20,17,18,0,14,19],
[25,25,27,30,31,26,36,0,24],
[24,13,27,27,26,23,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,25,23,25,22,25,26],
[31,0,26,29,26,22,29,23,24],
[27,24,0,27,25,19,25,25,18],
[25,21,23,0,25,22,21,19,20],
[27,24,25,25,0,30,25,23,25],
[25,28,31,28,20,0,24,24,19],
[28,21,25,29,25,26,0,25,25],
[25,27,25,31,27,26,25,0,19],
[24,26,32,30,25,31,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,21,24,30,24,26,24],
[26,0,30,25,26,28,28,29,26],
[24,20,0,25,23,25,22,26,22],
[29,25,25,0,27,28,26,31,29],
[26,24,27,23,0,29,23,28,29],
[20,22,25,22,21,0,23,27,23],
[26,22,28,24,27,27,0,29,24],
[24,21,24,19,22,23,21,0,26],
[26,24,28,21,21,27,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,29,12,24,20,18,13,12],
[31,0,30,23,27,22,23,20,20],
[21,20,0,10,19,16,23,17,15],
[38,27,40,0,29,34,33,27,22],
[26,23,31,21,0,23,22,16,16],
[30,28,34,16,27,0,23,19,15],
[32,27,27,17,28,27,0,25,19],
[37,30,33,23,34,31,25,0,26],
[38,30,35,28,34,35,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,30,28,28,25,28,27,30],
[28,0,25,31,29,30,24,31,30],
[20,25,0,27,22,20,24,25,25],
[22,19,23,0,25,24,22,24,27],
[22,21,28,25,0,23,24,22,28],
[25,20,30,26,27,0,26,25,30],
[22,26,26,28,26,24,0,29,32],
[23,19,25,26,28,25,21,0,27],
[20,20,25,23,22,20,18,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,23,27,21,24,21,27],
[27,0,26,24,31,25,23,23,30],
[27,24,0,26,31,25,25,23,27],
[27,26,24,0,27,24,27,23,28],
[23,19,19,23,0,20,17,18,24],
[29,25,25,26,30,0,28,26,28],
[26,27,25,23,33,22,0,24,28],
[29,27,27,27,32,24,26,0,28],
[23,20,23,22,26,22,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,25,28,23,23,33,29],
[25,0,30,26,33,34,23,32,28],
[17,20,0,33,30,23,31,30,20],
[25,24,17,0,33,27,29,28,23],
[22,17,20,17,0,19,23,25,20],
[27,16,27,23,31,0,26,32,22],
[27,27,19,21,27,24,0,29,25],
[17,18,20,22,25,18,21,0,16],
[21,22,30,27,30,28,25,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,35,26,25,27,33,29],
[21,0,24,29,20,26,23,28,28],
[25,26,0,30,32,26,22,31,27],
[15,21,20,0,26,19,21,29,21],
[24,30,18,24,0,25,26,25,26],
[25,24,24,31,25,0,23,31,21],
[23,27,28,29,24,27,0,30,25],
[17,22,19,21,25,19,20,0,20],
[21,22,23,29,24,29,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,28,30,8,26,14,24,26],
[36,0,48,43,29,37,28,24,38],
[22,2,0,28,17,37,22,19,27],
[20,7,22,0,1,26,7,18,26],
[42,21,33,49,0,37,28,31,46],
[24,13,13,24,13,0,13,12,32],
[36,22,28,43,22,37,0,26,39],
[26,26,31,32,19,38,24,0,32],
[24,12,23,24,4,18,11,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,26,35,28,19,26,17],
[23,0,17,16,9,19,24,43,24],
[23,33,0,25,23,33,16,35,23],
[24,34,25,0,26,19,18,35,18],
[15,41,27,24,0,25,25,35,31],
[22,31,17,31,25,0,23,26,14],
[31,26,34,32,25,27,0,34,34],
[24,7,15,15,15,24,16,0,15],
[33,26,27,32,19,36,16,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,25,28,26,29,30,29],
[19,0,17,26,22,22,15,28,22],
[26,33,0,28,29,26,21,32,26],
[25,24,22,0,28,26,25,29,21],
[22,28,21,22,0,28,21,24,25],
[24,28,24,24,22,0,23,27,26],
[21,35,29,25,29,27,0,30,28],
[20,22,18,21,26,23,20,0,21],
[21,28,24,29,25,24,22,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,24,24,30,24,23,19],
[24,0,25,17,25,20,32,24,22],
[29,25,0,22,27,27,25,28,21],
[26,33,28,0,35,32,35,34,25],
[26,25,23,15,0,22,25,27,19],
[20,30,23,18,28,0,29,20,19],
[26,18,25,15,25,21,0,18,11],
[27,26,22,16,23,30,32,0,19],
[31,28,29,25,31,31,39,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,21,16,16,18,19,27],
[34,0,24,23,33,33,28,25,31],
[38,26,0,31,37,32,23,30,38],
[29,27,19,0,25,25,28,21,30],
[34,17,13,25,0,18,22,21,34],
[34,17,18,25,32,0,12,22,19],
[32,22,27,22,28,38,0,27,30],
[31,25,20,29,29,28,23,0,29],
[23,19,12,20,16,31,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,22,24,20,21,21,22],
[25,0,20,26,30,26,28,25,31],
[24,30,0,25,27,25,24,26,27],
[28,24,25,0,23,26,22,18,26],
[26,20,23,27,0,28,31,22,29],
[30,24,25,24,22,0,29,24,31],
[29,22,26,28,19,21,0,23,19],
[29,25,24,32,28,26,27,0,28],
[28,19,23,24,21,19,31,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,26,26,20,22,21,26],
[25,0,30,28,24,24,24,22,28],
[24,20,0,25,22,23,23,20,22],
[24,22,25,0,25,22,23,16,26],
[24,26,28,25,0,24,25,22,29],
[30,26,27,28,26,0,25,25,27],
[28,26,27,27,25,25,0,17,26],
[29,28,30,34,28,25,33,0,35],
[24,22,28,24,21,23,24,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,30,27,26,27,30,31],
[23,0,30,20,22,21,35,30,14],
[26,20,0,29,27,26,38,34,22],
[20,30,21,0,21,16,23,14,23],
[23,28,23,29,0,23,25,33,26],
[24,29,24,34,27,0,36,30,27],
[23,15,12,27,25,14,0,24,14],
[20,20,16,36,17,20,26,0,17],
[19,36,28,27,24,23,36,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,32,28,20,22,25,28],
[32,0,18,38,29,32,29,35,32],
[27,32,0,31,24,21,35,29,26],
[18,12,19,0,11,14,21,23,19],
[22,21,26,39,0,18,32,27,32],
[30,18,29,36,32,0,29,29,23],
[28,21,15,29,18,21,0,26,25],
[25,15,21,27,23,21,24,0,22],
[22,18,24,31,18,27,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,19,22,24,22,28,28],
[27,0,24,26,32,20,28,32,29],
[27,26,0,30,23,29,30,29,33],
[31,24,20,0,23,27,28,30,34],
[28,18,27,27,0,26,28,31,32],
[26,30,21,23,24,0,32,28,33],
[28,22,20,22,22,18,0,24,30],
[22,18,21,20,19,22,26,0,30],
[22,21,17,16,18,17,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,34,29,30,22,29,36],
[22,0,22,33,25,22,20,28,25],
[22,28,0,34,26,28,25,31,26],
[16,17,16,0,14,24,14,23,21],
[21,25,24,36,0,31,12,31,30],
[20,28,22,26,19,0,16,30,26],
[28,30,25,36,38,34,0,36,28],
[21,22,19,27,19,20,14,0,25],
[14,25,24,29,20,24,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,33,24,27,22,31,19,20],
[19,0,22,14,28,26,25,23,23],
[17,28,0,13,18,26,26,20,15],
[26,36,37,0,30,29,32,25,16],
[23,22,32,20,0,15,24,18,17],
[28,24,24,21,35,0,28,15,12],
[19,25,24,18,26,22,0,16,20],
[31,27,30,25,32,35,34,0,27],
[30,27,35,34,33,38,30,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,39,21,19,20,21,21,31],
[26,0,30,23,21,23,25,23,29],
[11,20,0,20,16,15,20,20,20],
[29,27,30,0,22,23,24,30,22],
[31,29,34,28,0,21,22,29,27],
[30,27,35,27,29,0,28,25,26],
[29,25,30,26,28,22,0,23,22],
[29,27,30,20,21,25,27,0,30],
[19,21,30,28,23,24,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,24,16,17,18,21,13,30],
[37,0,29,27,31,28,32,23,34],
[26,21,0,28,15,23,27,27,28],
[34,23,22,0,27,29,29,33,31],
[33,19,35,23,0,31,34,24,32],
[32,22,27,21,19,0,29,22,28],
[29,18,23,21,16,21,0,20,27],
[37,27,23,17,26,28,30,0,28],
[20,16,22,19,18,22,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,24,23,20,22,26,27],
[28,0,20,24,23,27,25,26,19],
[26,30,0,22,25,28,27,32,25],
[26,26,28,0,25,22,22,25,27],
[27,27,25,25,0,28,21,28,25],
[30,23,22,28,22,0,23,30,25],
[28,25,23,28,29,27,0,25,21],
[24,24,18,25,22,20,25,0,24],
[23,31,25,23,25,25,29,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,25,37,24,28,29,17],
[25,0,32,16,25,20,17,21,12],
[29,18,0,23,37,21,30,18,25],
[25,34,27,0,34,32,22,32,23],
[13,25,13,16,0,19,18,24,28],
[26,30,29,18,31,0,28,28,24],
[22,33,20,28,32,22,0,33,33],
[21,29,32,18,26,22,17,0,18],
[33,38,25,27,22,26,17,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,20,17,25,20,18,22],
[28,0,27,26,20,25,26,25,25],
[27,23,0,24,19,23,26,23,24],
[30,24,26,0,21,27,26,22,25],
[33,30,31,29,0,27,27,23,27],
[25,25,27,23,23,0,25,23,23],
[30,24,24,24,23,25,0,23,25],
[32,25,27,28,27,27,27,0,27],
[28,25,26,25,23,27,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,27,25,27,25,25,27],
[28,0,30,25,27,30,30,27,19],
[21,20,0,24,22,24,21,20,19],
[23,25,26,0,25,26,19,26,27],
[25,23,28,25,0,28,23,28,24],
[23,20,26,24,22,0,22,23,21],
[25,20,29,31,27,28,0,23,21],
[25,23,30,24,22,27,27,0,21],
[23,31,31,23,26,29,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,26,27,33,27,27,25],
[22,0,25,23,27,25,28,22,22],
[25,25,0,24,25,31,27,28,20],
[24,27,26,0,29,29,24,24,25],
[23,23,25,21,0,23,17,27,19],
[17,25,19,21,27,0,21,26,16],
[23,22,23,26,33,29,0,26,25],
[23,28,22,26,23,24,24,0,20],
[25,28,30,25,31,34,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,25,28,22,25,35,28],
[24,0,14,14,22,14,16,26,26],
[20,36,0,19,24,18,18,35,24],
[25,36,31,0,30,27,30,35,26],
[22,28,26,20,0,17,11,31,24],
[28,36,32,23,33,0,17,29,27],
[25,34,32,20,39,33,0,31,39],
[15,24,15,15,19,21,19,0,22],
[22,24,26,24,26,23,11,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,20,27,24,32,25,23],
[26,0,21,26,23,20,29,20,20],
[27,29,0,28,23,26,31,28,25],
[30,24,22,0,24,29,31,25,27],
[23,27,27,26,0,29,31,22,25],
[26,30,24,21,21,0,33,22,23],
[18,21,19,19,19,17,0,18,22],
[25,30,22,25,28,28,32,0,30],
[27,30,25,23,25,27,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,13,18,24,26,16,30],
[22,0,15,18,17,22,20,17,25],
[30,35,0,25,29,25,29,27,30],
[37,32,25,0,25,30,28,36,37],
[32,33,21,25,0,24,28,28,33],
[26,28,25,20,26,0,23,24,27],
[24,30,21,22,22,27,0,23,32],
[34,33,23,14,22,26,27,0,33],
[20,25,20,13,17,23,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,21,23,34,18,27,23],
[27,0,24,29,23,36,25,28,27],
[22,26,0,18,23,28,23,29,21],
[29,21,32,0,29,30,21,28,30],
[27,27,27,21,0,29,27,27,24],
[16,14,22,20,21,0,19,19,18],
[32,25,27,29,23,31,0,29,20],
[23,22,21,22,23,31,21,0,25],
[27,23,29,20,26,32,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,25,29,28,25,23,24],
[26,0,26,30,28,24,25,25,27],
[30,24,0,32,30,25,25,32,29],
[25,20,18,0,26,20,24,24,23],
[21,22,20,24,0,18,23,23,21],
[22,26,25,30,32,0,29,26,27],
[25,25,25,26,27,21,0,24,30],
[27,25,18,26,27,24,26,0,30],
[26,23,21,27,29,23,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,15,35,16,32,25,30],
[26,0,30,28,32,25,26,29,35],
[30,20,0,19,32,18,23,28,36],
[35,22,31,0,33,25,23,22,30],
[15,18,18,17,0,24,22,21,32],
[34,25,32,25,26,0,23,19,27],
[18,24,27,27,28,27,0,25,31],
[25,21,22,28,29,31,25,0,31],
[20,15,14,20,18,23,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,31,24,20,22,25,30,24],
[27,0,28,29,21,28,20,31,25],
[19,22,0,21,23,26,18,24,24],
[26,21,29,0,26,25,24,27,24],
[30,29,27,24,0,33,28,33,20],
[28,22,24,25,17,0,24,33,17],
[25,30,32,26,22,26,0,29,27],
[20,19,26,23,17,17,21,0,19],
[26,25,26,26,30,33,23,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,22,22,25,19,22,23],
[32,0,24,32,25,29,26,28,27],
[27,26,0,25,22,25,28,20,24],
[28,18,25,0,27,29,25,26,28],
[28,25,28,23,0,34,24,28,26],
[25,21,25,21,16,0,19,19,21],
[31,24,22,25,26,31,0,27,22],
[28,22,30,24,22,31,23,0,24],
[27,23,26,22,24,29,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,29,24,21,24,27,25],
[25,0,30,33,24,30,30,30,26],
[29,20,0,26,26,24,24,28,24],
[21,17,24,0,18,25,17,23,22],
[26,26,24,32,0,32,22,31,31],
[29,20,26,25,18,0,24,30,23],
[26,20,26,33,28,26,0,30,27],
[23,20,22,27,19,20,20,0,18],
[25,24,26,28,19,27,23,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,23,23,22,27,24,20],
[28,0,24,29,28,27,30,26,27],
[25,26,0,21,28,25,26,29,26],
[27,21,29,0,25,24,29,28,31],
[27,22,22,25,0,25,26,23,23],
[28,23,25,26,25,0,25,25,31],
[23,20,24,21,24,25,0,22,27],
[26,24,21,22,27,25,28,0,25],
[30,23,24,19,27,19,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,31,25,27,34,27,22,28],
[16,0,28,19,25,29,17,26,21],
[19,22,0,18,18,20,21,32,17],
[25,31,32,0,27,28,20,37,27],
[23,25,32,23,0,33,18,22,32],
[16,21,30,22,17,0,17,20,23],
[23,33,29,30,32,33,0,31,31],
[28,24,18,13,28,30,19,0,25],
[22,29,33,23,18,27,19,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,36,16,20,16,17,17,20],
[31,0,27,28,31,28,25,19,31],
[14,23,0,12,20,18,20,15,26],
[34,22,38,0,28,36,32,21,41],
[30,19,30,22,0,24,27,27,24],
[34,22,32,14,26,0,20,31,32],
[33,25,30,18,23,30,0,23,27],
[33,31,35,29,23,19,27,0,30],
[30,19,24,9,26,18,23,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,33,33,24,33,41,26,33],
[21,0,27,17,15,15,28,22,18],
[17,23,0,19,17,21,22,14,18],
[17,33,31,0,11,25,29,18,18],
[26,35,33,39,0,35,36,25,24],
[17,35,29,25,15,0,31,25,19],
[9,22,28,21,14,19,0,15,15],
[24,28,36,32,25,25,35,0,27],
[17,32,32,32,26,31,35,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,14,9,18,19,18,18,18],
[30,0,14,27,18,4,9,18,27],
[36,36,0,35,41,25,35,29,33],
[41,23,15,0,28,19,15,22,18],
[32,32,9,22,0,19,15,22,29],
[31,46,25,31,31,0,31,25,31],
[32,41,15,35,35,19,0,31,35],
[32,32,21,28,28,25,19,0,26],
[32,23,17,32,21,19,15,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,17,19,22,29,19,22],
[34,0,23,21,26,25,28,32,33],
[33,27,0,27,28,25,31,32,33],
[33,29,23,0,29,27,33,25,30],
[31,24,22,21,0,25,24,25,29],
[28,25,25,23,25,0,33,24,27],
[21,22,19,17,26,17,0,26,28],
[31,18,18,25,25,26,24,0,26],
[28,17,17,20,21,23,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,18,18,24,24,14,19,18],
[29,0,25,23,27,25,26,29,23],
[32,25,0,25,26,28,23,25,22],
[32,27,25,0,29,32,28,32,29],
[26,23,24,21,0,22,22,27,26],
[26,25,22,18,28,0,22,25,22],
[36,24,27,22,28,28,0,29,23],
[31,21,25,18,23,25,21,0,22],
[32,27,28,21,24,28,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,38,46,40,38,34,34,26],
[34,0,38,46,36,36,22,48,24],
[12,12,0,32,24,26,22,22,24],
[4,4,18,0,40,18,2,12,16],
[10,14,26,10,0,26,12,22,12],
[12,14,24,32,24,0,12,22,26],
[16,28,28,48,38,38,0,48,24],
[16,2,28,38,28,28,2,0,24],
[24,26,26,34,38,24,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,10,34,29,20,25,22,15],
[19,0,20,20,25,20,32,18,14],
[40,30,0,30,30,20,34,20,24],
[16,30,20,0,35,15,14,15,20],
[21,25,20,15,0,11,25,22,15],
[30,30,30,35,39,0,14,13,30],
[25,18,16,36,25,36,0,34,22],
[28,32,30,35,28,37,16,0,32],
[35,36,26,30,35,20,28,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,17,23,22,22,20,21],
[26,0,21,21,22,29,23,22,25],
[29,29,0,27,31,25,26,29,24],
[33,29,23,0,25,25,30,29,30],
[27,28,19,25,0,27,21,20,27],
[28,21,25,25,23,0,28,18,25],
[28,27,24,20,29,22,0,23,23],
[30,28,21,21,30,32,27,0,26],
[29,25,26,20,23,25,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,25,20,29,26,30,25],
[20,0,17,23,23,25,18,20,23],
[24,33,0,28,23,31,21,29,26],
[25,27,22,0,26,30,22,28,24],
[30,27,27,24,0,32,29,31,29],
[21,25,19,20,18,0,20,20,23],
[24,32,29,28,21,30,0,28,26],
[20,30,21,22,19,30,22,0,22],
[25,27,24,26,21,27,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,23,21,27,25,32,22,17],
[19,0,32,26,25,27,30,26,17],
[27,18,0,31,24,29,27,23,26],
[29,24,19,0,29,27,32,29,20],
[23,25,26,21,0,26,27,26,16],
[25,23,21,23,24,0,27,20,21],
[18,20,23,18,23,23,0,24,16],
[28,24,27,21,24,30,26,0,19],
[33,33,24,30,34,29,34,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,30,28,23,28,23,21,23],
[17,0,16,18,19,16,23,13,17],
[20,34,0,22,22,24,30,18,27],
[22,32,28,0,28,19,35,23,20],
[27,31,28,22,0,20,27,25,19],
[22,34,26,31,30,0,24,28,24],
[27,27,20,15,23,26,0,17,21],
[29,37,32,27,25,22,33,0,21],
[27,33,23,30,31,26,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,23,25,29,26,23,28],
[19,0,15,21,31,34,18,28,22],
[25,35,0,24,31,35,24,29,26],
[27,29,26,0,33,33,21,29,29],
[25,19,19,17,0,20,23,24,22],
[21,16,15,17,30,0,24,23,21],
[24,32,26,29,27,26,0,31,30],
[27,22,21,21,26,27,19,0,25],
[22,28,24,21,28,29,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,23,30,29,27,32,29],
[23,0,27,25,27,30,32,31,27],
[29,23,0,26,24,28,26,33,32],
[27,25,24,0,24,28,26,25,27],
[20,23,26,26,0,22,25,27,27],
[21,20,22,22,28,0,28,26,26],
[23,18,24,24,25,22,0,25,26],
[18,19,17,25,23,24,25,0,23],
[21,23,18,23,23,24,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,24,26,24,23,24,23],
[26,0,24,28,23,22,28,26,24],
[30,26,0,25,30,27,25,29,28],
[26,22,25,0,32,29,26,25,26],
[24,27,20,18,0,22,27,22,25],
[26,28,23,21,28,0,27,31,20],
[27,22,25,24,23,23,0,28,27],
[26,24,21,25,28,19,22,0,25],
[27,26,22,24,25,30,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,18,24,19,24,31,20],
[24,0,20,19,25,25,20,22,20],
[25,30,0,21,27,23,21,22,24],
[32,31,29,0,29,26,24,27,26],
[26,25,23,21,0,16,24,27,24],
[31,25,27,24,34,0,24,28,28],
[26,30,29,26,26,26,0,23,23],
[19,28,28,23,23,22,27,0,27],
[30,30,26,24,26,22,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,28,27,24,23,32,21],
[20,0,18,24,18,27,20,22,21],
[23,32,0,23,25,32,26,33,24],
[22,26,27,0,23,20,15,26,13],
[23,32,25,27,0,23,23,25,23],
[26,23,18,30,27,0,28,24,21],
[27,30,24,35,27,22,0,34,26],
[18,28,17,24,25,26,16,0,20],
[29,29,26,37,27,29,24,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,27,21,26,23,27,21],
[19,0,24,23,23,14,17,21,23],
[25,26,0,25,19,19,26,15,21],
[23,27,25,0,17,22,21,17,20],
[29,27,31,33,0,28,23,23,24],
[24,36,31,28,22,0,21,25,22],
[27,33,24,29,27,29,0,29,28],
[23,29,35,33,27,25,21,0,26],
[29,27,29,30,26,28,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,24,28,27,23,34,25],
[28,0,26,25,20,26,20,22,10],
[25,24,0,24,22,23,23,29,13],
[26,25,26,0,23,26,18,31,11],
[22,30,28,27,0,33,20,30,18],
[23,24,27,24,17,0,13,21,17],
[27,30,27,32,30,37,0,31,23],
[16,28,21,19,20,29,19,0,19],
[25,40,37,39,32,33,27,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,29,29,27,28,21,32],
[23,0,21,21,34,24,17,23,26],
[21,29,0,23,26,29,15,21,25],
[21,29,27,0,30,28,24,28,28],
[21,16,24,20,0,20,15,16,21],
[23,26,21,22,30,0,26,25,18],
[22,33,35,26,35,24,0,27,29],
[29,27,29,22,34,25,23,0,28],
[18,24,25,22,29,32,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,27,36,21,9,28,26,24],
[34,0,32,36,29,16,28,27,30],
[23,18,0,25,23,18,26,21,21],
[14,14,25,0,5,8,22,20,11],
[29,21,27,45,0,25,29,39,28],
[41,34,32,42,25,0,29,36,28],
[22,22,24,28,21,21,0,34,8],
[24,23,29,30,11,14,16,0,13],
[26,20,29,39,22,22,42,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,29,26,24,28,27,26],
[24,0,18,25,24,24,22,26,24],
[27,32,0,30,27,22,26,28,26],
[21,25,20,0,21,18,24,25,26],
[24,26,23,29,0,23,23,27,27],
[26,26,28,32,27,0,29,29,23],
[22,28,24,26,27,21,0,26,25],
[23,24,22,25,23,21,24,0,20],
[24,26,24,24,23,27,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,33,41,22,41,22,36],
[25,0,37,32,34,36,34,35,21],
[20,13,0,13,40,13,14,35,27],
[17,18,37,0,34,36,34,32,17],
[9,16,10,16,0,7,3,9,24],
[28,14,37,14,43,0,37,43,23],
[9,16,36,16,47,13,0,31,30],
[28,15,15,18,41,7,19,0,24],
[14,29,23,33,26,27,20,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,19,28,31,28,34,27,24],
[26,0,26,21,18,22,32,23,22],
[31,24,0,28,21,32,37,31,20],
[22,29,22,0,23,23,29,29,25],
[19,32,29,27,0,25,36,26,26],
[22,28,18,27,25,0,28,29,20],
[16,18,13,21,14,22,0,18,14],
[23,27,19,21,24,21,32,0,18],
[26,28,30,25,24,30,36,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,25,31,31,29,23,29],
[20,0,24,22,24,25,26,20,23],
[26,26,0,20,26,29,30,28,25],
[25,28,30,0,31,30,30,35,27],
[19,26,24,19,0,22,26,23,22],
[19,25,21,20,28,0,25,28,19],
[21,24,20,20,24,25,0,24,25],
[27,30,22,15,27,22,26,0,21],
[21,27,25,23,28,31,25,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,40,20,25,14,27,20,20],
[25,0,36,31,50,39,44,39,39],
[10,14,0,16,35,22,21,24,24],
[30,19,34,0,34,42,21,34,34],
[25,0,15,16,0,22,16,25,22],
[36,11,28,8,28,0,13,23,13],
[23,6,29,29,34,37,0,29,37],
[30,11,26,16,25,27,21,0,19],
[30,11,26,16,28,37,13,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,31,23,33,25,30,31],
[22,0,22,28,22,23,23,25,29],
[20,28,0,22,13,20,17,28,26],
[19,22,28,0,22,23,11,31,26],
[27,28,37,28,0,23,18,37,30],
[17,27,30,27,27,0,18,35,28],
[25,27,33,39,32,32,0,37,31],
[20,25,22,19,13,15,13,0,26],
[19,21,24,24,20,22,19,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,36,30,30,29,39,17],
[28,0,25,28,29,30,20,30,25],
[22,25,0,22,29,22,15,25,17],
[14,22,28,0,27,28,27,20,22],
[20,21,21,23,0,23,23,28,16],
[20,20,28,22,27,0,21,24,28],
[21,30,35,23,27,29,0,28,31],
[11,20,25,30,22,26,22,0,17],
[33,25,33,28,34,22,19,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,25,27,25,18,21,34],
[25,0,28,24,26,25,21,25,25],
[20,22,0,19,21,20,12,17,32],
[25,26,31,0,28,28,21,25,31],
[23,24,29,22,0,24,22,18,33],
[25,25,30,22,26,0,21,18,30],
[32,29,38,29,28,29,0,20,39],
[29,25,33,25,32,32,30,0,36],
[16,25,18,19,17,20,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,16,21,27,29,28,31],
[19,0,23,20,21,24,25,16,22],
[25,27,0,23,17,35,26,29,27],
[34,30,27,0,23,32,32,25,33],
[29,29,33,27,0,35,33,20,31],
[23,26,15,18,15,0,20,15,26],
[21,25,24,18,17,30,0,20,29],
[22,34,21,25,30,35,30,0,30],
[19,28,23,17,19,24,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,30,32,29,30,38,24],
[21,0,20,27,32,16,25,27,24],
[21,30,0,16,26,29,30,26,22],
[20,23,34,0,30,21,34,30,26],
[18,18,24,20,0,28,24,29,28],
[21,34,21,29,22,0,23,23,22],
[20,25,20,16,26,27,0,28,28],
[12,23,24,20,21,27,22,0,20],
[26,26,28,24,22,28,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,27,27,26,25,24,30],
[29,0,26,29,25,24,28,22,25],
[21,24,0,24,21,19,22,25,27],
[23,21,26,0,22,21,23,19,28],
[23,25,29,28,0,21,21,18,23],
[24,26,31,29,29,0,19,26,26],
[25,22,28,27,29,31,0,24,27],
[26,28,25,31,32,24,26,0,31],
[20,25,23,22,27,24,23,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,19,31,24,29,26,23,30],
[25,0,25,30,28,26,27,26,27],
[31,25,0,30,27,27,20,24,28],
[19,20,20,0,20,23,22,23,25],
[26,22,23,30,0,25,22,23,24],
[21,24,23,27,25,0,19,28,23],
[24,23,30,28,28,31,0,28,27],
[27,24,26,27,27,22,22,0,26],
[20,23,22,25,26,27,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,25,25,28,21,18,17],
[28,0,28,24,23,25,19,23,26],
[26,22,0,23,23,25,17,24,19],
[25,26,27,0,22,27,22,20,21],
[25,27,27,28,0,29,21,23,26],
[22,25,25,23,21,0,19,20,16],
[29,31,33,28,29,31,0,25,25],
[32,27,26,30,27,30,25,0,25],
[33,24,31,29,24,34,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,16,35,27,41,34,28,23],
[14,0,18,29,20,33,28,23,20],
[34,32,0,29,27,46,39,24,27],
[15,21,21,0,20,29,25,32,21],
[23,30,23,30,0,41,37,26,24],
[9,17,4,21,9,0,36,21,10],
[16,22,11,25,13,14,0,25,16],
[22,27,26,18,24,29,25,0,21],
[27,30,23,29,26,40,34,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,26,26,23,22,25,31],
[22,0,28,23,26,26,21,24,32],
[19,22,0,18,19,11,24,22,23],
[24,27,32,0,25,20,22,29,27],
[24,24,31,25,0,19,28,26,31],
[27,24,39,30,31,0,27,31,33],
[28,29,26,28,22,23,0,28,29],
[25,26,28,21,24,19,22,0,28],
[19,18,27,23,19,17,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,25,22,25,26,20,27],
[26,0,26,25,25,23,23,21,21],
[26,24,0,25,26,27,25,27,20],
[25,25,25,0,22,24,25,21,23],
[28,25,24,28,0,27,27,27,25],
[25,27,23,26,23,0,26,19,24],
[24,27,25,25,23,24,0,22,18],
[30,29,23,29,23,31,28,0,25],
[23,29,30,27,25,26,32,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,33,23,28,31,22,21,18],
[30,0,33,32,30,37,17,32,25],
[17,17,0,18,25,31,24,19,19],
[27,18,32,0,30,39,27,26,20],
[22,20,25,20,0,26,24,16,9],
[19,13,19,11,24,0,12,9,9],
[28,33,26,23,26,38,0,23,22],
[29,18,31,24,34,41,27,0,21],
[32,25,31,30,41,41,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,33,27,37,27,42,27],
[23,0,41,17,33,37,26,39,45],
[30,9,0,17,18,36,8,30,19],
[17,33,33,0,30,34,20,42,30],
[23,17,32,20,0,20,13,23,29],
[13,13,14,16,30,0,10,30,10],
[23,24,42,30,37,40,0,40,39],
[8,11,20,8,27,20,10,0,20],
[23,5,31,20,21,40,11,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,23,34,27,33,33,32],
[19,0,22,26,18,18,23,24,19],
[21,28,0,27,28,22,28,26,21],
[27,24,23,0,21,20,35,25,18],
[16,32,22,29,0,26,22,24,23],
[23,32,28,30,24,0,33,32,22],
[17,27,22,15,28,17,0,28,20],
[17,26,24,25,26,18,22,0,16],
[18,31,29,32,27,28,30,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,28,24,29,31,26,21],
[24,0,25,28,26,26,30,26,25],
[25,25,0,27,23,31,31,26,24],
[22,22,23,0,24,28,32,26,26],
[26,24,27,26,0,28,33,26,26],
[21,24,19,22,22,0,24,21,18],
[19,20,19,18,17,26,0,18,17],
[24,24,24,24,24,29,32,0,25],
[29,25,26,24,24,32,33,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,26,24,25,25,21,26],
[22,0,23,23,16,21,23,22,21],
[24,27,0,28,21,23,24,24,22],
[24,27,22,0,19,21,22,22,18],
[26,34,29,31,0,29,26,28,24],
[25,29,27,29,21,0,25,22,23],
[25,27,26,28,24,25,0,23,24],
[29,28,26,28,22,28,27,0,24],
[24,29,28,32,26,27,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,13,28,23,18,15,18,24],
[27,0,21,29,25,26,30,19,25],
[37,29,0,29,21,23,19,25,29],
[22,21,21,0,15,13,12,13,24],
[27,25,29,35,0,30,31,33,30],
[32,24,27,37,20,0,29,29,30],
[35,20,31,38,19,21,0,25,28],
[32,31,25,37,17,21,25,0,31],
[26,25,21,26,20,20,22,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,25,29,28,28,32,33],
[19,0,19,19,34,20,16,23,23],
[22,31,0,22,37,35,25,25,28],
[25,31,28,0,37,26,27,27,30],
[21,16,13,13,0,16,20,20,26],
[22,30,15,24,34,0,20,25,24],
[22,34,25,23,30,30,0,24,28],
[18,27,25,23,30,25,26,0,23],
[17,27,22,20,24,26,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,23,31,23,25,26,27],
[25,0,21,25,32,22,28,25,28],
[26,29,0,20,33,21,26,26,22],
[27,25,30,0,37,29,25,23,30],
[19,18,17,13,0,22,25,22,20],
[27,28,29,21,28,0,26,24,27],
[25,22,24,25,25,24,0,27,18],
[24,25,24,27,28,26,23,0,24],
[23,22,28,20,30,23,32,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,36,26,0,24,50,0,24],
[14,0,12,26,0,0,26,0,0],
[14,38,0,26,14,0,14,0,24],
[24,24,24,0,24,24,24,0,24],
[50,50,36,26,0,36,50,12,24],
[26,50,50,26,14,0,26,26,38],
[0,24,36,26,0,24,0,0,24],
[50,50,50,50,38,24,50,0,38],
[26,50,26,26,26,12,26,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,25,28,25,26,25,29],
[22,0,28,32,29,27,26,25,30],
[21,22,0,25,22,25,28,21,21],
[25,18,25,0,24,23,24,22,25],
[22,21,28,26,0,24,26,23,25],
[25,23,25,27,26,0,23,28,29],
[24,24,22,26,24,27,0,21,26],
[25,25,29,28,27,22,29,0,24],
[21,20,29,25,25,21,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,22,19,24,24,17,23],
[31,0,27,25,26,31,31,30,31],
[28,23,0,24,27,29,30,29,36],
[28,25,26,0,26,23,25,27,26],
[31,24,23,24,0,24,33,27,28],
[26,19,21,27,26,0,28,21,23],
[26,19,20,25,17,22,0,25,24],
[33,20,21,23,23,29,25,0,29],
[27,19,14,24,22,27,26,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,27,30,24,29,27,29],
[27,0,20,28,28,26,28,30,31],
[27,30,0,24,24,25,24,28,28],
[23,22,26,0,28,27,28,28,27],
[20,22,26,22,0,26,22,28,24],
[26,24,25,23,24,0,29,25,25],
[21,22,26,22,28,21,0,25,27],
[23,20,22,22,22,25,25,0,27],
[21,19,22,23,26,25,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,30,26,17,30,26,30,30],
[27,0,10,43,27,47,40,10,40],
[20,40,0,43,37,50,43,47,37],
[24,7,7,0,24,37,37,7,24],
[33,23,13,26,0,50,26,30,20],
[20,3,0,13,0,0,26,0,0],
[24,10,7,13,24,24,0,7,24],
[20,40,3,43,20,50,43,0,40],
[20,10,13,26,30,50,26,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,17,15,26,24,23,21],
[30,0,29,23,30,33,28,30,31],
[31,21,0,20,19,26,23,26,23],
[33,27,30,0,23,34,24,32,28],
[35,20,31,27,0,32,32,35,30],
[24,17,24,16,18,0,21,23,26],
[26,22,27,26,18,29,0,28,25],
[27,20,24,18,15,27,22,0,24],
[29,19,27,22,20,24,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,19,17,23,28,22,16],
[31,0,9,21,14,16,28,30,20],
[34,41,0,31,27,30,35,31,25],
[31,29,19,0,24,21,22,35,20],
[33,36,23,26,0,26,35,30,27],
[27,34,20,29,24,0,30,26,31],
[22,22,15,28,15,20,0,28,17],
[28,20,19,15,20,24,22,0,21],
[34,30,25,30,23,19,33,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,27,28,31,24,23,28],
[26,0,22,26,24,30,24,26,27],
[24,28,0,25,25,23,23,23,28],
[23,24,25,0,28,23,24,18,30],
[22,26,25,22,0,25,19,20,32],
[19,20,27,27,25,0,25,18,28],
[26,26,27,26,31,25,0,19,30],
[27,24,27,32,30,32,31,0,30],
[22,23,22,20,18,22,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,31,27,31,25,29,21,26],
[25,0,19,19,24,22,26,19,27],
[19,31,0,24,26,22,27,21,20],
[23,31,26,0,25,22,25,25,23],
[19,26,24,25,0,21,23,18,27],
[25,28,28,28,29,0,25,21,21],
[21,24,23,25,27,25,0,20,28],
[29,31,29,25,32,29,30,0,29],
[24,23,30,27,23,29,22,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,21,21,23,34,23,26],
[28,0,28,28,30,25,33,27,32],
[21,22,0,22,30,29,36,23,21],
[29,22,28,0,25,26,37,30,17],
[29,20,20,25,0,32,34,28,28],
[27,25,21,24,18,0,38,22,23],
[16,17,14,13,16,12,0,19,19],
[27,23,27,20,22,28,31,0,21],
[24,18,29,33,22,27,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,27,20,18,22,19,26],
[29,0,25,32,26,31,30,23,24],
[26,25,0,31,27,30,22,24,24],
[23,18,19,0,27,24,21,16,21],
[30,24,23,23,0,23,22,20,23],
[32,19,20,26,27,0,29,26,28],
[28,20,28,29,28,21,0,20,27],
[31,27,26,34,30,24,30,0,30],
[24,26,26,29,27,22,23,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,25,31,21,32,26,30,25],
[11,0,25,26,16,25,21,22,20],
[25,25,0,24,16,32,20,21,22],
[19,24,26,0,20,29,24,22,23],
[29,34,34,30,0,38,31,25,31],
[18,25,18,21,12,0,17,16,17],
[24,29,30,26,19,33,0,26,26],
[20,28,29,28,25,34,24,0,24],
[25,30,28,27,19,33,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,15,10,28,11,48,33],
[39,0,35,39,24,36,24,39,35],
[31,15,0,17,16,17,0,31,31],
[35,11,33,0,35,28,25,35,33],
[40,26,34,15,0,28,11,48,48],
[22,14,33,22,22,0,22,22,33],
[39,26,50,25,39,28,0,39,50],
[2,11,19,15,2,28,11,0,25],
[17,15,19,17,2,17,0,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,27,20,19,25,31,26],
[26,0,19,31,25,23,22,27,28],
[28,31,0,36,24,31,25,33,26],
[23,19,14,0,23,21,18,21,20],
[30,25,26,27,0,29,24,30,26],
[31,27,19,29,21,0,26,29,24],
[25,28,25,32,26,24,0,35,27],
[19,23,17,29,20,21,15,0,25],
[24,22,24,30,24,26,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,22,25,19,26,30,26],
[25,0,23,20,26,19,25,20,23],
[23,27,0,19,23,20,28,21,26],
[28,30,31,0,24,24,31,28,32],
[25,24,27,26,0,25,27,30,27],
[31,31,30,26,25,0,31,28,32],
[24,25,22,19,23,19,0,21,22],
[20,30,29,22,20,22,29,0,25],
[24,27,24,18,23,18,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,19,28,17,29,16,24],
[29,0,25,26,27,22,28,22,27],
[29,25,0,24,26,22,31,23,30],
[31,24,26,0,30,26,33,26,26],
[22,23,24,20,0,21,27,19,24],
[33,28,28,24,29,0,30,29,28],
[21,22,19,17,23,20,0,19,24],
[34,28,27,24,31,21,31,0,24],
[26,23,20,24,26,22,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 50, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_9_50.csv", index=False, header=False)