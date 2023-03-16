
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,17,14,15,24,23,13,16],
[34,0,19,26,22,35,28,27],
[37,32,0,32,25,36,30,28],
[36,25,19,0,28,30,28,27],
[27,29,26,23,0,29,27,21],
[28,16,15,21,22,0,20,20],
[38,23,21,23,24,31,0,29],
[35,24,23,24,30,31,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,25,24,25,21,19],
[31,0,26,29,29,27,25,29],
[26,25,0,24,22,25,23,18],
[26,22,27,0,25,26,21,27],
[27,22,29,26,0,28,28,27],
[26,24,26,25,23,0,23,21],
[30,26,28,30,23,28,0,25],
[32,22,33,24,24,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,17,21,17,20,26],
[29,0,20,25,26,19,24,26],
[30,31,0,22,27,26,27,28],
[34,26,29,0,31,22,29,29],
[30,25,24,20,0,20,21,32],
[34,32,25,29,31,0,29,28],
[31,27,24,22,30,22,0,26],
[25,25,23,22,19,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,20,26,26,22,23],
[25,0,22,28,22,29,18,20],
[25,29,0,28,27,28,23,23],
[31,23,23,0,21,28,22,17],
[25,29,24,30,0,33,22,28],
[25,22,23,23,18,0,14,15],
[29,33,28,29,29,37,0,23],
[28,31,28,34,23,36,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,8,26,21,37,18,20],
[27,0,23,31,26,37,24,35],
[43,28,0,33,38,33,25,36],
[25,20,18,0,22,28,18,25],
[30,25,13,29,0,40,27,28],
[14,14,18,23,11,0,22,17],
[33,27,26,33,24,29,0,31],
[31,16,15,26,23,34,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,23,33,23,16,31],
[29,0,36,27,22,28,28,31],
[24,15,0,25,24,16,11,31],
[28,24,26,0,39,31,17,38],
[18,29,27,12,0,15,17,39],
[28,23,35,20,36,0,23,35],
[35,23,40,34,34,28,0,29],
[20,20,20,13,12,16,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,32,27,25,28,20],
[26,0,16,26,27,27,34,28],
[23,35,0,31,24,25,30,30],
[19,25,20,0,24,21,26,16],
[24,24,27,27,0,26,27,26],
[26,24,26,30,25,0,26,27],
[23,17,21,25,24,25,0,22],
[31,23,21,35,25,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,23,25,32,30,28],
[27,0,22,27,26,27,26,22],
[25,29,0,23,28,31,27,20],
[28,24,28,0,31,32,22,26],
[26,25,23,20,0,22,20,24],
[19,24,20,19,29,0,22,26],
[21,25,24,29,31,29,0,31],
[23,29,31,25,27,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,22,22,30,25,27],
[29,0,27,25,29,28,27,30],
[28,24,0,29,30,28,31,28],
[29,26,22,0,24,26,24,30],
[29,22,21,27,0,28,24,27],
[21,23,23,25,23,0,28,30],
[26,24,20,27,27,23,0,22],
[24,21,23,21,24,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,34,23,19,27,28,31],
[27,0,26,14,21,30,19,36],
[17,25,0,20,21,24,22,21],
[28,37,31,0,21,23,23,40],
[32,30,30,30,0,32,22,35],
[24,21,27,28,19,0,27,26],
[23,32,29,28,29,24,0,29],
[20,15,30,11,16,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,22,13,23,16,29,25],
[34,0,27,23,24,19,20,28],
[29,24,0,18,21,17,18,28],
[38,28,33,0,28,21,26,22],
[28,27,30,23,0,22,35,38],
[35,32,34,30,29,0,25,18],
[22,31,33,25,16,26,0,30],
[26,23,23,29,13,33,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,38,33,30,27,34],
[25,0,31,29,24,24,27,24],
[28,20,0,29,24,23,24,30],
[13,22,22,0,21,12,20,20],
[18,27,27,30,0,33,28,28],
[21,27,28,39,18,0,26,38],
[24,24,27,31,23,25,0,29],
[17,27,21,31,23,13,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,13,29,34,42,12],
[23,0,20,10,22,36,36,18],
[22,31,0,14,21,27,37,17],
[38,41,37,0,24,47,47,29],
[22,29,30,27,0,26,40,14],
[17,15,24,4,25,0,42,16],
[9,15,14,4,11,9,0,13],
[39,33,34,22,37,35,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,19,21,18,27,27],
[29,0,27,20,25,31,33,27],
[31,24,0,25,31,23,32,29],
[32,31,26,0,29,21,30,33],
[30,26,20,22,0,23,28,28],
[33,20,28,30,28,0,30,35],
[24,18,19,21,23,21,0,23],
[24,24,22,18,23,16,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,42,21,21,5,21,26],
[9,0,19,19,19,3,19,24],
[9,32,0,19,19,5,19,24],
[30,32,32,0,24,35,35,24],
[30,32,32,27,0,14,14,23],
[46,48,46,16,37,0,46,37],
[30,32,32,16,37,5,0,21],
[25,27,27,27,28,14,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,28,25,28,35,28,30],
[10,0,12,22,9,25,21,16],
[23,39,0,30,23,42,22,22],
[26,29,21,0,27,34,34,34],
[23,42,28,24,0,30,31,27],
[16,26,9,17,21,0,14,14],
[23,30,29,17,20,37,0,18],
[21,35,29,17,24,37,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,26,25,25,30,30],
[23,0,24,26,22,29,29,27],
[22,27,0,20,25,25,25,26],
[25,25,31,0,28,30,28,28],
[26,29,26,23,0,28,23,27],
[26,22,26,21,23,0,26,24],
[21,22,26,23,28,25,0,28],
[21,24,25,23,24,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,26,26,20,29,20],
[25,0,15,25,27,23,26,25],
[23,36,0,26,30,27,28,25],
[25,26,25,0,23,25,26,22],
[25,24,21,28,0,28,24,29],
[31,28,24,26,23,0,26,28],
[22,25,23,25,27,25,0,24],
[31,26,26,29,22,23,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,37,35,19,13,12],
[38,0,39,31,34,17,37,11],
[37,12,0,27,33,19,17,13],
[14,20,24,0,16,28,22,22],
[16,17,18,35,0,17,17,15],
[32,34,32,23,34,0,36,38],
[38,14,34,29,34,15,0,16],
[39,40,38,29,36,13,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,33,29,42,27,22,36],
[25,0,24,30,24,21,25,28],
[18,27,0,31,28,20,25,34],
[22,21,20,0,28,24,27,32],
[9,27,23,23,0,19,23,27],
[24,30,31,27,32,0,28,27],
[29,26,26,24,28,23,0,32],
[15,23,17,19,24,24,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,23,31,23,37,31],
[32,0,29,30,24,27,24,32],
[24,22,0,15,14,25,31,25],
[28,21,36,0,26,25,26,45],
[20,27,37,25,0,36,30,38],
[28,24,26,26,15,0,32,37],
[14,27,20,25,21,19,0,45],
[20,19,26,6,13,14,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,26,27,32,26,35],
[21,0,27,23,24,23,23,30],
[26,24,0,26,28,28,20,29],
[25,28,25,0,26,25,27,32],
[24,27,23,25,0,31,26,30],
[19,28,23,26,20,0,19,30],
[25,28,31,24,25,32,0,24],
[16,21,22,19,21,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,26,26,24,34,24],
[28,0,22,24,28,26,32,23],
[31,29,0,29,26,28,35,24],
[25,27,22,0,21,29,30,23],
[25,23,25,30,0,28,36,27],
[27,25,23,22,23,0,29,27],
[17,19,16,21,15,22,0,17],
[27,28,27,28,24,24,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,18,23,23,26,24],
[24,0,27,21,20,22,21,27],
[23,24,0,16,21,23,20,24],
[33,30,35,0,26,25,25,25],
[28,31,30,25,0,25,31,23],
[28,29,28,26,26,0,27,25],
[25,30,31,26,20,24,0,26],
[27,24,27,26,28,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,12,26,14,18,15,29],
[26,0,15,17,24,20,13,24],
[39,36,0,29,28,27,21,36],
[25,34,22,0,25,24,21,32],
[37,27,23,26,0,25,22,22],
[33,31,24,27,26,0,30,32],
[36,38,30,30,29,21,0,29],
[22,27,15,19,29,19,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,18,30,31,30,28,28],
[22,0,30,26,16,22,35,25],
[33,21,0,28,26,22,45,45],
[21,25,23,0,26,36,18,23],
[20,35,25,25,0,25,34,34],
[21,29,29,15,26,0,24,29],
[23,16,6,33,17,27,0,26],
[23,26,6,28,17,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,27,26,31,21,26],
[20,0,26,25,30,29,18,20],
[27,25,0,22,28,28,26,25],
[24,26,29,0,27,29,25,32],
[25,21,23,24,0,24,25,26],
[20,22,23,22,27,0,23,24],
[30,33,25,26,26,28,0,24],
[25,31,26,19,25,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,23,24,25,24,29],
[23,0,26,24,26,25,23,27],
[22,25,0,23,30,28,28,26],
[28,27,28,0,26,22,27,29],
[27,25,21,25,0,28,29,29],
[26,26,23,29,23,0,23,26],
[27,28,23,24,22,28,0,22],
[22,24,25,22,22,25,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,25,23,22,22,14],
[27,0,20,20,21,25,24,19],
[28,31,0,26,27,24,23,27],
[26,31,25,0,29,27,25,22],
[28,30,24,22,0,21,23,21],
[29,26,27,24,30,0,21,22],
[29,27,28,26,28,30,0,23],
[37,32,24,29,30,29,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,22,22,29,32,25],
[27,0,28,21,25,25,21,21],
[25,23,0,25,26,25,24,18],
[29,30,26,0,26,24,27,22],
[29,26,25,25,0,26,27,24],
[22,26,26,27,25,0,27,27],
[19,30,27,24,24,24,0,20],
[26,30,33,29,27,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,31,26,23,29,29,31],
[27,0,30,25,25,26,30,24],
[20,21,0,22,25,28,28,25],
[25,26,29,0,23,25,21,21],
[28,26,26,28,0,30,27,21],
[22,25,23,26,21,0,26,24],
[22,21,23,30,24,25,0,26],
[20,27,26,30,30,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,37,26,36,32,26],
[26,0,28,32,29,25,27,22],
[22,23,0,32,22,26,26,26],
[14,19,19,0,21,20,24,22],
[25,22,29,30,0,23,30,23],
[15,26,25,31,28,0,32,23],
[19,24,25,27,21,19,0,25],
[25,29,25,29,28,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,31,36,34,23,29,44],
[17,0,25,30,21,23,28,40],
[20,26,0,35,25,23,25,36],
[15,21,16,0,18,17,19,34],
[17,30,26,33,0,24,26,44],
[28,28,28,34,27,0,22,34],
[22,23,26,32,25,29,0,36],
[7,11,15,17,7,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,24,27,20,26,22],
[32,0,31,29,31,27,31,25],
[25,20,0,19,26,22,25,22],
[27,22,32,0,29,18,28,19],
[24,20,25,22,0,20,15,24],
[31,24,29,33,31,0,29,22],
[25,20,26,23,36,22,0,28],
[29,26,29,32,27,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,23,31,34,27,28],
[20,0,23,29,27,33,26,27],
[26,28,0,21,30,33,25,27],
[28,22,30,0,25,31,25,26],
[20,24,21,26,0,30,24,21],
[17,18,18,20,21,0,18,13],
[24,25,26,26,27,33,0,29],
[23,24,24,25,30,38,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,29,25,28,29,29,30],
[25,0,23,21,28,26,28,27],
[22,28,0,22,23,21,26,30],
[26,30,29,0,25,35,26,26],
[23,23,28,26,0,30,30,26],
[22,25,30,16,21,0,28,25],
[22,23,25,25,21,23,0,32],
[21,24,21,25,25,26,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,28,33,28,31,29],
[23,0,25,26,29,24,27,27],
[27,26,0,28,29,29,23,30],
[23,25,23,0,26,26,28,24],
[18,22,22,25,0,27,30,25],
[23,27,22,25,24,0,23,26],
[20,24,28,23,21,28,0,29],
[22,24,21,27,26,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,16,13,5,16,15,14],
[31,0,16,13,4,21,15,15],
[35,35,0,10,4,18,15,16],
[38,38,41,0,19,16,15,22],
[46,47,47,32,0,35,32,23],
[35,30,33,35,16,0,30,21],
[36,36,36,36,19,21,0,27],
[37,36,35,29,28,30,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,28,27,27,30,20],
[29,0,24,34,29,14,39,20],
[28,27,0,43,32,25,27,31],
[23,17,8,0,18,8,16,14],
[24,22,19,33,0,16,14,23],
[24,37,26,43,35,0,37,34],
[21,12,24,35,37,14,0,24],
[31,31,20,37,28,17,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,24,17,18,22,26],
[29,0,25,23,25,20,23,24],
[28,26,0,26,25,24,27,27],
[27,28,25,0,23,23,22,27],
[34,26,26,28,0,26,25,25],
[33,31,27,28,25,0,25,23],
[29,28,24,29,26,26,0,27],
[25,27,24,24,26,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,29,21,12,15,18],
[36,0,16,43,35,20,29,27],
[37,35,0,34,28,24,25,35],
[22,8,17,0,23,16,13,20],
[30,16,23,28,0,9,21,23],
[39,31,27,35,42,0,25,31],
[36,22,26,38,30,26,0,44],
[33,24,16,31,28,20,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,36,32,30,21,27],
[28,0,25,29,29,31,26,18],
[24,26,0,37,34,30,30,27],
[15,22,14,0,21,20,15,20],
[19,22,17,30,0,37,23,25],
[21,20,21,31,14,0,14,27],
[30,25,21,36,28,37,0,26],
[24,33,24,31,26,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,32,31,30,29,25,28],
[18,0,27,30,28,26,27,21],
[19,24,0,25,29,24,21,19],
[20,21,26,0,23,25,20,22],
[21,23,22,28,0,22,22,18],
[22,25,27,26,29,0,26,15],
[26,24,30,31,29,25,0,22],
[23,30,32,29,33,36,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,12,12,18,12,12,27],
[24,0,12,24,6,0,0,33],
[39,39,0,30,6,9,0,39],
[39,27,21,0,27,9,9,51],
[33,45,45,24,0,33,33,33],
[39,51,42,42,18,0,42,51],
[39,51,51,42,18,9,0,51],
[24,18,12,0,18,0,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,16,7,21,21,12,22],
[25,0,29,25,27,40,30,25],
[35,22,0,22,27,27,12,35],
[44,26,29,0,21,32,22,39],
[30,24,24,30,0,35,30,30],
[30,11,24,19,16,0,35,35],
[39,21,39,29,21,16,0,28],
[29,26,16,12,21,16,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,30,30,26,33,24],
[20,0,22,29,26,23,31,22],
[26,29,0,36,30,24,28,28],
[21,22,15,0,22,23,31,25],
[21,25,21,29,0,25,30,21],
[25,28,27,28,26,0,32,28],
[18,20,23,20,21,19,0,17],
[27,29,23,26,30,23,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,25,32,27,26,28],
[24,0,26,26,28,23,23,30],
[22,25,0,27,26,23,28,29],
[26,25,24,0,27,25,25,26],
[19,23,25,24,0,21,28,31],
[24,28,28,26,30,0,29,23],
[25,28,23,26,23,22,0,27],
[23,21,22,25,20,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,26,32,25,22,25],
[25,0,28,23,26,31,24,26],
[23,23,0,25,25,27,28,22],
[25,28,26,0,28,23,26,23],
[19,25,26,23,0,23,20,21],
[26,20,24,28,28,0,25,25],
[29,27,23,25,31,26,0,22],
[26,25,29,28,30,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,32,12,33,22,17,6],
[33,0,20,37,34,36,23,29],
[19,31,0,31,31,24,24,19],
[39,14,20,0,29,26,25,8],
[18,17,20,22,0,21,17,5],
[29,15,27,25,30,0,24,3],
[34,28,27,26,34,27,0,15],
[45,22,32,43,46,48,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,36,25,35,39,26],
[20,0,26,16,11,13,19,8],
[29,25,0,33,22,27,25,25],
[15,35,18,0,25,28,36,27],
[26,40,29,26,0,32,24,38],
[16,38,24,23,19,0,30,22],
[12,32,26,15,27,21,0,37],
[25,43,26,24,13,29,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,21,26,32,29,34],
[26,0,21,31,16,28,25,30],
[25,30,0,22,23,33,34,24],
[30,20,29,0,17,29,37,28],
[25,35,28,34,0,30,32,30],
[19,23,18,22,21,0,28,21],
[22,26,17,14,19,23,0,21],
[17,21,27,23,21,30,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,30,26,32,23,32,30],
[28,0,32,28,27,25,34,31],
[21,19,0,21,21,28,29,26],
[25,23,30,0,23,22,31,25],
[19,24,30,28,0,26,37,24],
[28,26,23,29,25,0,28,26],
[19,17,22,20,14,23,0,21],
[21,20,25,26,27,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,25,23,25,25,26,20],
[34,0,26,29,27,35,28,25],
[26,25,0,21,16,28,23,19],
[28,22,30,0,26,26,25,32],
[26,24,35,25,0,29,25,27],
[26,16,23,25,22,0,18,17],
[25,23,28,26,26,33,0,23],
[31,26,32,19,24,34,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,23,19,33,22,21,8],
[39,0,38,31,45,18,30,24],
[28,13,0,20,26,21,5,24],
[32,20,31,0,34,24,23,23],
[18,6,25,17,0,14,16,15],
[29,33,30,27,37,0,22,20],
[30,21,46,28,35,29,0,27],
[43,27,27,28,36,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,31,31,32,30,32],
[26,0,23,27,25,29,19,27],
[21,28,0,26,29,28,27,28],
[20,24,25,0,24,29,23,25],
[20,26,22,27,0,22,24,21],
[19,22,23,22,29,0,25,24],
[21,32,24,28,27,26,0,24],
[19,24,23,26,30,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,22,30,31,30,26],
[22,0,28,25,25,32,25,26],
[20,23,0,26,29,27,25,29],
[29,26,25,0,27,29,28,25],
[21,26,22,24,0,27,23,21],
[20,19,24,22,24,0,24,25],
[21,26,26,23,28,27,0,22],
[25,25,22,26,30,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,37,24,22,29,23,21],
[23,0,22,18,19,25,19,26],
[14,29,0,27,16,21,20,23],
[27,33,24,0,21,21,16,26],
[29,32,35,30,0,23,24,28],
[22,26,30,30,28,0,17,22],
[28,32,31,35,27,34,0,23],
[30,25,28,25,23,29,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,7,13,38,15,31,8],
[25,0,29,17,34,15,25,11],
[44,22,0,9,34,21,34,17],
[38,34,42,0,41,28,25,38],
[13,17,17,10,0,25,17,13],
[36,36,30,23,26,0,26,39],
[20,26,17,26,34,25,0,25],
[43,40,34,13,38,12,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,31,33,34,32,30,29],
[29,0,21,27,29,27,32,27],
[20,30,0,25,26,26,29,27],
[18,24,26,0,28,23,28,30],
[17,22,25,23,0,21,21,29],
[19,24,25,28,30,0,28,33],
[21,19,22,23,30,23,0,26],
[22,24,24,21,22,18,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,24,28,28,32,36],
[22,0,24,21,28,21,24,31],
[25,27,0,24,24,23,26,34],
[27,30,27,0,25,19,27,35],
[23,23,27,26,0,26,21,32],
[23,30,28,32,25,0,22,40],
[19,27,25,24,30,29,0,30],
[15,20,17,16,19,11,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,36,38,16,38,34,34],
[17,0,25,10,3,25,23,41],
[15,26,0,10,5,10,23,26],
[13,41,41,0,19,37,37,37],
[35,48,46,32,0,42,24,42],
[13,26,41,14,9,0,24,39],
[17,28,28,14,27,27,0,24],
[17,10,25,14,9,12,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,30,23,32,20,23,21],
[31,0,36,34,31,26,29,21],
[21,15,0,19,27,22,26,23],
[28,17,32,0,28,26,25,19],
[19,20,24,23,0,23,17,16],
[31,25,29,25,28,0,21,28],
[28,22,25,26,34,30,0,20],
[30,30,28,32,35,23,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,24,23,22,23,24],
[28,0,27,26,25,25,22,25],
[27,24,0,24,27,26,25,24],
[27,25,27,0,28,29,31,28],
[28,26,24,23,0,22,24,22],
[29,26,25,22,29,0,26,25],
[28,29,26,20,27,25,0,28],
[27,26,27,23,29,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,24,17,24,29,21],
[33,0,27,26,23,26,31,24],
[28,24,0,19,20,22,29,27],
[27,25,32,0,26,28,29,31],
[34,28,31,25,0,28,35,27],
[27,25,29,23,23,0,35,30],
[22,20,22,22,16,16,0,23],
[30,27,24,20,24,21,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,28,32,24,29,32],
[27,0,28,18,24,20,22,20],
[22,23,0,17,22,20,12,17],
[23,33,34,0,24,27,33,34],
[19,27,29,27,0,17,33,21],
[27,31,31,24,34,0,28,31],
[22,29,39,18,18,23,0,17],
[19,31,34,17,30,20,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,35,26,16,23,24,20],
[31,0,37,24,27,28,26,25],
[16,14,0,16,19,17,20,20],
[25,27,35,0,31,23,29,24],
[35,24,32,20,0,20,28,31],
[28,23,34,28,31,0,25,23],
[27,25,31,22,23,26,0,24],
[31,26,31,27,20,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,26,27,24,22,23],
[21,0,23,21,27,23,18,22],
[27,28,0,26,27,24,20,24],
[25,30,25,0,27,32,20,23],
[24,24,24,24,0,25,26,25],
[27,28,27,19,26,0,22,24],
[29,33,31,31,25,29,0,27],
[28,29,27,28,26,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,20,18,21,17,20,21],
[40,0,27,26,20,25,27,29],
[31,24,0,25,31,29,30,36],
[33,25,26,0,30,31,32,31],
[30,31,20,21,0,29,36,30],
[34,26,22,20,22,0,35,28],
[31,24,21,19,15,16,0,16],
[30,22,15,20,21,23,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,31,40,27,31,23],
[23,0,27,29,24,36,31,40],
[24,24,0,29,36,24,37,30],
[20,22,22,0,26,25,27,30],
[11,27,15,25,0,24,27,23],
[24,15,27,26,27,0,25,23],
[20,20,14,24,24,26,0,27],
[28,11,21,21,28,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,25,26,27,36,33],
[22,0,21,25,13,21,14,16],
[27,30,0,24,28,32,25,28],
[26,26,27,0,19,22,20,18],
[25,38,23,32,0,29,28,23],
[24,30,19,29,22,0,26,31],
[15,37,26,31,23,25,0,17],
[18,35,23,33,28,20,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,6,27,3,14,16],
[39,0,23,27,32,24,24,29],
[33,28,0,22,31,14,24,16],
[45,24,29,0,36,26,26,31],
[24,19,20,15,0,9,23,20],
[48,27,37,25,42,0,24,25],
[37,27,27,25,28,27,0,26],
[35,22,35,20,31,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,29,21,33,24,31],
[26,0,25,31,23,32,26,25],
[26,26,0,27,26,28,24,33],
[22,20,24,0,19,28,19,24],
[30,28,25,32,0,34,20,28],
[18,19,23,23,17,0,25,26],
[27,25,27,32,31,26,0,32],
[20,26,18,27,23,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,26,29,23,21,24],
[25,0,22,27,25,23,23,27],
[25,29,0,29,27,26,28,27],
[25,24,22,0,23,22,23,28],
[22,26,24,28,0,20,22,23],
[28,28,25,29,31,0,30,31],
[30,28,23,28,29,21,0,25],
[27,24,24,23,28,20,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,36,21,28,31,23,23],
[23,0,28,20,16,18,19,19],
[15,23,0,26,23,13,1,20],
[30,31,25,0,16,20,16,8],
[23,35,28,35,0,28,24,24],
[20,33,38,31,23,0,29,20],
[28,32,50,35,27,22,0,32],
[28,32,31,43,27,31,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,13,26,19,25,16],
[23,0,28,16,23,28,35,19],
[31,23,0,18,32,29,41,28],
[38,35,33,0,30,19,31,34],
[25,28,19,21,0,26,27,20],
[32,23,22,32,25,0,31,29],
[26,16,10,20,24,20,0,27],
[35,32,23,17,31,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,22,31,24,29,28],
[20,0,21,20,23,18,22,27],
[22,30,0,27,26,26,33,30],
[29,31,24,0,27,29,27,30],
[20,28,25,24,0,22,25,27],
[27,33,25,22,29,0,30,30],
[22,29,18,24,26,21,0,25],
[23,24,21,21,24,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,30,27,24,26,29],
[22,0,15,29,23,16,19,22],
[26,36,0,32,29,34,24,28],
[21,22,19,0,22,19,17,24],
[24,28,22,29,0,24,22,27],
[27,35,17,32,27,0,24,32],
[25,32,27,34,29,27,0,27],
[22,29,23,27,24,19,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,28,32,31,22,33],
[18,0,21,32,26,21,21,26],
[23,30,0,29,29,22,28,23],
[23,19,22,0,30,27,23,21],
[19,25,22,21,0,22,21,26],
[20,30,29,24,29,0,22,23],
[29,30,23,28,30,29,0,25],
[18,25,28,30,25,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,30,33,26,35,31,24],
[16,0,21,25,20,26,27,20],
[21,30,0,29,21,33,30,23],
[18,26,22,0,27,24,27,32],
[25,31,30,24,0,32,39,39],
[16,25,18,27,19,0,22,21],
[20,24,21,24,12,29,0,23],
[27,31,28,19,12,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,20,31,28,31,23],
[29,0,22,19,25,26,24,21],
[27,29,0,19,26,22,21,26],
[31,32,32,0,35,24,33,30],
[20,26,25,16,0,31,30,25],
[23,25,29,27,20,0,31,20],
[20,27,30,18,21,20,0,22],
[28,30,25,21,26,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,28,36,19,28,11],
[40,0,14,31,31,31,17,14],
[40,37,0,23,40,46,32,38],
[23,20,28,0,28,34,15,34],
[15,20,11,23,0,26,32,11],
[32,20,5,17,25,0,17,5],
[23,34,19,36,19,34,0,19],
[40,37,13,17,40,46,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,22,32,23,17,21],
[32,0,26,24,30,35,32,35],
[27,25,0,25,26,24,26,29],
[29,27,26,0,29,23,22,23],
[19,21,25,22,0,18,12,27],
[28,16,27,28,33,0,24,25],
[34,19,25,29,39,27,0,26],
[30,16,22,28,24,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,24,20,28,20,20,19],
[35,0,28,29,25,31,25,29],
[27,23,0,27,32,30,31,19],
[31,22,24,0,30,29,28,20],
[23,26,19,21,0,22,17,18],
[31,20,21,22,29,0,23,20],
[31,26,20,23,34,28,0,18],
[32,22,32,31,33,31,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,20,22,24,24,28],
[30,0,30,20,25,34,31,31],
[27,21,0,23,27,24,17,25],
[31,31,28,0,29,30,23,28],
[29,26,24,22,0,26,20,25],
[27,17,27,21,25,0,30,27],
[27,20,34,28,31,21,0,28],
[23,20,26,23,26,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,23,29,21,27,25],
[27,0,27,21,29,27,33,27],
[29,24,0,25,33,24,31,25],
[28,30,26,0,31,25,25,24],
[22,22,18,20,0,16,18,22],
[30,24,27,26,35,0,35,25],
[24,18,20,26,33,16,0,26],
[26,24,26,27,29,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,16,24,18,21,21],
[32,0,24,23,26,18,21,32],
[27,27,0,25,20,19,20,21],
[35,28,26,0,27,31,27,24],
[27,25,31,24,0,26,19,32],
[33,33,32,20,25,0,26,27],
[30,30,31,24,32,25,0,22],
[30,19,30,27,19,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,23,19,25,23,22],
[30,0,24,27,28,27,22,28],
[29,27,0,34,21,31,24,33],
[28,24,17,0,22,22,19,24],
[32,23,30,29,0,26,22,24],
[26,24,20,29,25,0,27,30],
[28,29,27,32,29,24,0,28],
[29,23,18,27,27,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,34,16,16,12,14,16],
[23,0,37,26,19,22,21,31],
[17,14,0,18,19,12,17,23],
[35,25,33,0,26,23,25,35],
[35,32,32,25,0,32,26,33],
[39,29,39,28,19,0,18,33],
[37,30,34,26,25,33,0,34],
[35,20,28,16,18,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,11,31,50,31,50,30],
[20,0,0,31,20,20,31,0],
[40,51,0,51,39,20,50,50],
[20,20,0,0,39,0,39,19],
[1,31,12,12,0,11,12,12],
[20,31,31,51,40,0,51,31],
[1,20,1,12,39,0,0,20],
[21,51,1,32,39,20,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,23,22,23,23,23],
[27,0,26,26,25,22,27,26],
[27,25,0,24,22,27,28,26],
[28,25,27,0,29,29,29,25],
[29,26,29,22,0,23,27,25],
[28,29,24,22,28,0,27,29],
[28,24,23,22,24,24,0,27],
[28,25,25,26,26,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,28,33,26,29,20],
[26,0,32,30,33,17,25,22],
[25,19,0,21,27,17,27,19],
[23,21,30,0,29,14,27,25],
[18,18,24,22,0,15,23,21],
[25,34,34,37,36,0,28,30],
[22,26,24,24,28,23,0,18],
[31,29,32,26,30,21,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,24,26,21,28,24],
[30,0,31,29,31,27,36,23],
[22,20,0,25,31,23,29,21],
[27,22,26,0,26,23,24,23],
[25,20,20,25,0,23,25,20],
[30,24,28,28,28,0,29,26],
[23,15,22,27,26,22,0,19],
[27,28,30,28,31,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,26,22,23,21,23],
[31,0,28,24,35,24,32,28],
[32,23,0,25,35,27,32,33],
[25,27,26,0,31,22,27,24],
[29,16,16,20,0,20,26,27],
[28,27,24,29,31,0,31,32],
[30,19,19,24,25,20,0,27],
[28,23,18,27,24,19,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,28,29,32,34,28],
[20,0,22,28,28,24,28,25],
[26,29,0,30,26,32,25,30],
[23,23,21,0,25,23,19,29],
[22,23,25,26,0,24,26,29],
[19,27,19,28,27,0,19,28],
[17,23,26,32,25,32,0,28],
[23,26,21,22,22,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,23,27,23,24,24],
[28,0,26,24,27,28,27,24],
[24,25,0,20,22,23,25,23],
[28,27,31,0,30,32,25,27],
[24,24,29,21,0,27,19,25],
[28,23,28,19,24,0,21,25],
[27,24,26,26,32,30,0,28],
[27,27,28,24,26,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,4,23,27,8,27,8],
[28,0,23,35,28,28,16,21],
[47,28,0,36,33,21,40,24],
[28,16,15,0,27,27,8,20],
[24,23,18,24,0,24,7,19],
[43,23,30,24,27,0,23,31],
[24,35,11,43,44,28,0,12],
[43,30,27,31,32,20,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,19,27,35,33,27,26],
[24,0,19,32,49,23,41,32],
[32,32,0,32,32,15,32,32],
[24,19,19,0,34,23,34,16],
[16,2,19,17,0,23,15,16],
[18,28,36,28,28,0,28,28],
[24,10,19,17,36,23,0,1],
[25,19,19,35,35,23,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,25,26,26,25,22],
[27,0,22,23,26,30,23,25],
[27,29,0,20,29,29,27,29],
[26,28,31,0,32,32,27,24],
[25,25,22,19,0,25,27,20],
[25,21,22,19,26,0,22,17],
[26,28,24,24,24,29,0,26],
[29,26,22,27,31,34,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,17,28,29,25,21,22],
[26,0,30,28,32,20,26,23],
[34,21,0,30,21,22,19,22],
[23,23,21,0,25,23,23,18],
[22,19,30,26,0,26,24,20],
[26,31,29,28,25,0,30,27],
[30,25,32,28,27,21,0,27],
[29,28,29,33,31,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,26,25,25,27,33],
[24,0,29,28,24,26,22,37],
[31,22,0,29,24,30,31,31],
[25,23,22,0,22,25,23,24],
[26,27,27,29,0,22,29,35],
[26,25,21,26,29,0,25,30],
[24,29,20,28,22,26,0,35],
[18,14,20,27,16,21,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,26,23,21,27,25],
[29,0,29,25,26,25,30,30],
[28,22,0,26,26,23,28,29],
[25,26,25,0,27,28,31,30],
[28,25,25,24,0,24,23,33],
[30,26,28,23,27,0,25,32],
[24,21,23,20,28,26,0,33],
[26,21,22,21,18,19,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,28,33,27,25],
[23,0,26,27,24,29,25,27],
[21,25,0,32,30,29,31,25],
[22,24,19,0,20,25,22,18],
[23,27,21,31,0,30,23,28],
[18,22,22,26,21,0,23,17],
[24,26,20,29,28,28,0,21],
[26,24,26,33,23,34,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,26,40,22,26,45],
[25,0,25,16,29,16,18,46],
[26,26,0,30,26,30,9,33],
[25,35,21,0,19,12,15,35],
[11,22,25,32,0,15,26,21],
[29,35,21,39,36,0,19,30],
[25,33,42,36,25,32,0,42],
[6,5,18,16,30,21,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,22,25,33,24,26],
[23,0,27,27,25,26,24,24],
[26,24,0,23,29,32,26,25],
[29,24,28,0,30,28,25,25],
[26,26,22,21,0,27,22,25],
[18,25,19,23,24,0,19,19],
[27,27,25,26,29,32,0,31],
[25,27,26,26,26,32,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,29,24,22,23,26],
[27,0,24,28,23,22,22,22],
[31,27,0,33,24,29,26,26],
[22,23,18,0,24,23,25,23],
[27,28,27,27,0,27,28,25],
[29,29,22,28,24,0,26,25],
[28,29,25,26,23,25,0,24],
[25,29,25,28,26,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,28,21,20,26,23],
[22,0,20,18,20,25,21,22],
[24,31,0,25,27,27,29,27],
[23,33,26,0,26,26,29,29],
[30,31,24,25,0,26,25,25],
[31,26,24,25,25,0,29,22],
[25,30,22,22,26,22,0,19],
[28,29,24,22,26,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,26,23,25,28,28,34],
[18,0,15,13,20,18,18,26],
[25,36,0,25,28,26,29,37],
[28,38,26,0,19,28,34,36],
[26,31,23,32,0,28,29,31],
[23,33,25,23,23,0,19,31],
[23,33,22,17,22,32,0,32],
[17,25,14,15,20,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,26,25,28,31,31],
[25,0,25,27,21,25,22,35],
[21,26,0,26,24,21,25,33],
[25,24,25,0,26,20,25,32],
[26,30,27,25,0,18,29,34],
[23,26,30,31,33,0,26,34],
[20,29,26,26,22,25,0,29],
[20,16,18,19,17,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,23,21,20,22,28],
[31,0,33,31,37,31,25,33],
[30,18,0,28,27,26,27,32],
[28,20,23,0,29,29,29,29],
[30,14,24,22,0,19,19,25],
[31,20,25,22,32,0,22,25],
[29,26,24,22,32,29,0,27],
[23,18,19,22,26,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,31,27,35,28,34,30],
[33,0,35,25,34,28,25,25],
[20,16,0,17,27,23,27,20],
[24,26,34,0,33,25,29,27],
[16,17,24,18,0,16,24,17],
[23,23,28,26,35,0,29,26],
[17,26,24,22,27,22,0,21],
[21,26,31,24,34,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,24,16,23,20,24],
[30,0,23,36,27,28,33,34],
[30,28,0,30,18,24,32,24],
[27,15,21,0,20,27,23,29],
[35,24,33,31,0,27,32,32],
[28,23,27,24,24,0,31,30],
[31,18,19,28,19,20,0,23],
[27,17,27,22,19,21,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,25,21,28,23,27],
[24,0,25,23,19,24,24,21],
[29,26,0,29,24,29,30,30],
[26,28,22,0,31,22,22,26],
[30,32,27,20,0,24,21,24],
[23,27,22,29,27,0,26,26],
[28,27,21,29,30,25,0,25],
[24,30,21,25,27,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,23,27,30,28,30],
[21,0,28,22,26,28,27,26],
[21,23,0,23,21,26,26,22],
[28,29,28,0,27,32,26,25],
[24,25,30,24,0,27,32,22],
[21,23,25,19,24,0,27,24],
[23,24,25,25,19,24,0,26],
[21,25,29,26,29,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,34,29,32,26,26,26],
[28,0,24,26,31,30,25,24],
[17,27,0,28,31,23,25,27],
[22,25,23,0,28,25,26,26],
[19,20,20,23,0,18,20,18],
[25,21,28,26,33,0,27,28],
[25,26,26,25,31,24,0,26],
[25,27,24,25,33,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,25,17,18,19,28,27],
[16,0,23,18,25,25,27,20],
[26,28,0,19,25,21,26,30],
[34,33,32,0,25,27,27,26],
[33,26,26,26,0,27,31,25],
[32,26,30,24,24,0,26,28],
[23,24,25,24,20,25,0,23],
[24,31,21,25,26,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,21,19,17,23,18],
[31,0,24,28,26,30,32,30],
[31,27,0,26,25,26,25,28],
[30,23,25,0,23,23,17,17],
[32,25,26,28,0,27,25,23],
[34,21,25,28,24,0,29,24],
[28,19,26,34,26,22,0,25],
[33,21,23,34,28,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,24,43,14,46,26],
[28,0,27,32,27,19,39,36],
[29,24,0,24,21,14,25,17],
[27,19,27,0,42,27,38,34],
[8,24,30,9,0,9,30,12],
[37,32,37,24,42,0,46,34],
[5,12,26,13,21,5,0,16],
[25,15,34,17,39,17,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,7,25,20,16,18],
[39,0,23,17,37,40,25,26],
[36,28,0,31,38,24,33,40],
[44,34,20,0,31,31,38,23],
[26,14,13,20,0,9,25,24],
[31,11,27,20,42,0,27,29],
[35,26,18,13,26,24,0,22],
[33,25,11,28,27,22,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,27,23,30,27,24,31],
[17,0,15,15,25,20,10,28],
[24,36,0,24,34,31,30,32],
[28,36,27,0,31,24,28,35],
[21,26,17,20,0,23,25,27],
[24,31,20,27,28,0,30,35],
[27,41,21,23,26,21,0,40],
[20,23,19,16,24,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,21,18,27,25,18,30],
[35,0,27,27,41,35,24,35],
[30,24,0,20,31,30,23,36],
[33,24,31,0,32,33,35,38],
[24,10,20,19,0,20,14,36],
[26,16,21,18,31,0,32,35],
[33,27,28,16,37,19,0,37],
[21,16,15,13,15,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,24,29,28,26,25],
[25,0,32,20,17,20,17,19],
[27,19,0,27,25,22,18,20],
[27,31,24,0,21,28,14,25],
[22,34,26,30,0,32,27,24],
[23,31,29,23,19,0,23,21],
[25,34,33,37,24,28,0,34],
[26,32,31,26,27,30,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,30,18,17,16,34,12],
[35,0,22,18,22,36,37,33],
[21,29,0,31,23,22,34,18],
[33,33,20,0,23,22,33,18],
[34,29,28,28,0,18,45,15],
[35,15,29,29,33,0,48,18],
[17,14,17,18,6,3,0,0],
[39,18,33,33,36,33,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,25,25,26,25,26],
[27,0,25,24,26,32,25,24],
[29,26,0,30,22,32,33,20],
[26,27,21,0,26,24,26,24],
[26,25,29,25,0,25,25,23],
[25,19,19,27,26,0,23,21],
[26,26,18,25,26,28,0,21],
[25,27,31,27,28,30,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,48,7,34,17,23,35],
[31,0,43,25,43,40,31,42],
[3,8,0,3,26,3,3,36],
[44,26,48,0,37,20,32,47],
[17,8,25,14,0,16,14,41],
[34,11,48,31,35,0,34,45],
[28,20,48,19,37,17,0,33],
[16,9,15,4,10,6,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,24,34,28,33,27],
[24,0,27,26,30,25,34,28],
[23,24,0,28,36,32,33,23],
[27,25,23,0,35,22,28,28],
[17,21,15,16,0,20,26,19],
[23,26,19,29,31,0,36,23],
[18,17,18,23,25,15,0,16],
[24,23,28,23,32,28,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,13,10,18,15,10],
[23,0,34,29,29,33,26,26],
[27,17,0,23,27,30,23,23],
[38,22,28,0,25,41,32,34],
[41,22,24,26,0,31,18,19],
[33,18,21,10,20,0,20,23],
[36,25,28,19,33,31,0,19],
[41,25,28,17,32,28,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,29,24,34,28,34,22],
[11,0,20,16,26,27,25,23],
[22,31,0,33,36,31,28,29],
[27,35,18,0,29,26,34,20],
[17,25,15,22,0,18,21,16],
[23,24,20,25,33,0,21,9],
[17,26,23,17,30,30,0,21],
[29,28,22,31,35,42,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,24,24,26,30,26],
[28,0,24,27,24,24,33,29],
[28,27,0,26,24,28,28,24],
[27,24,25,0,27,24,29,23],
[27,27,27,24,0,27,29,26],
[25,27,23,27,24,0,29,21],
[21,18,23,22,22,22,0,22],
[25,22,27,28,25,30,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,23,28,23,21,31],
[25,0,26,28,32,29,25,33],
[28,25,0,33,30,28,28,28],
[28,23,18,0,30,26,27,28],
[23,19,21,21,0,24,20,26],
[28,22,23,25,27,0,27,29],
[30,26,23,24,31,24,0,31],
[20,18,23,23,25,22,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,37,38,26,23,26,32],
[16,0,33,29,16,15,17,22],
[14,18,0,24,14,19,12,17],
[13,22,27,0,23,15,12,15],
[25,35,37,28,0,16,23,31],
[28,36,32,36,35,0,20,34],
[25,34,39,39,28,31,0,33],
[19,29,34,36,20,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,28,25,29,28,22],
[24,0,22,22,20,22,21,21],
[22,29,0,25,27,27,31,23],
[23,29,26,0,30,25,27,25],
[26,31,24,21,0,24,20,23],
[22,29,24,26,27,0,29,26],
[23,30,20,24,31,22,0,25],
[29,30,28,26,28,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,23,21,19,22,19],
[24,0,21,25,26,28,25,23],
[30,30,0,27,26,31,28,19],
[28,26,24,0,20,23,20,23],
[30,25,25,31,0,26,21,17],
[32,23,20,28,25,0,23,26],
[29,26,23,31,30,28,0,21],
[32,28,32,28,34,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,28,46,28,25,28],
[29,0,25,21,30,18,16,35],
[29,26,0,25,31,28,18,39],
[23,30,26,0,35,19,25,28],
[5,21,20,16,0,13,19,22],
[23,33,23,32,38,0,27,36],
[26,35,33,26,32,24,0,35],
[23,16,12,23,29,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,27,39,27,32,25,32],
[16,0,22,28,26,27,22,28],
[24,29,0,33,28,30,24,24],
[12,23,18,0,16,25,20,22],
[24,25,23,35,0,28,25,29],
[19,24,21,26,23,0,26,22],
[26,29,27,31,26,25,0,28],
[19,23,27,29,22,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,22,24,24,21,23],
[20,0,20,23,27,20,17,29],
[29,31,0,32,30,26,25,30],
[29,28,19,0,30,24,26,24],
[27,24,21,21,0,24,22,20],
[27,31,25,27,27,0,22,32],
[30,34,26,25,29,29,0,29],
[28,22,21,27,31,19,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,15,25,29,21,28,27],
[25,0,28,29,27,33,33,28],
[36,23,0,28,21,28,34,25],
[26,22,23,0,29,36,34,28],
[22,24,30,22,0,23,27,21],
[30,18,23,15,28,0,24,24],
[23,18,17,17,24,27,0,24],
[24,23,26,23,30,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,30,24,27,30,24],
[25,0,16,18,22,22,24,10],
[27,35,0,20,33,33,30,23],
[21,33,31,0,21,21,30,21],
[27,29,18,30,0,29,34,32],
[24,29,18,30,22,0,31,26],
[21,27,21,21,17,20,0,21],
[27,41,28,30,19,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,15,28,29,33,16],
[27,0,29,33,30,22,30,22],
[30,22,0,28,27,30,35,27],
[36,18,23,0,30,35,32,18],
[23,21,24,21,0,20,26,18],
[22,29,21,16,31,0,31,17],
[18,21,16,19,25,20,0,15],
[35,29,24,33,33,34,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,30,30,41,37,21],
[27,0,23,33,27,46,38,32],
[21,28,0,23,27,37,31,17],
[21,18,28,0,27,39,26,31],
[21,24,24,24,0,38,34,31],
[10,5,14,12,13,0,12,13],
[14,13,20,25,17,39,0,26],
[30,19,34,20,20,38,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,28,27,28,28,25],
[22,0,26,33,29,24,30,22],
[29,25,0,25,27,24,29,25],
[23,18,26,0,23,20,24,18],
[24,22,24,28,0,22,31,24],
[23,27,27,31,29,0,26,27],
[23,21,22,27,20,25,0,19],
[26,29,26,33,27,24,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,26,33,33,26,23],
[29,0,33,31,31,25,26,16],
[22,18,0,26,17,23,18,16],
[25,20,25,0,28,25,22,24],
[18,20,34,23,0,23,23,23],
[18,26,28,26,28,0,25,19],
[25,25,33,29,28,26,0,30],
[28,35,35,27,28,32,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,37,26,26,25,28,30],
[24,0,34,27,26,29,26,28],
[14,17,0,24,24,25,23,29],
[25,24,27,0,28,29,21,32],
[25,25,27,23,0,28,20,25],
[26,22,26,22,23,0,26,29],
[23,25,28,30,31,25,0,34],
[21,23,22,19,26,22,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,31,29,18,29,23],
[27,0,37,24,36,25,29,32],
[31,14,0,28,25,27,28,28],
[20,27,23,0,28,14,23,16],
[22,15,26,23,0,6,21,13],
[33,26,24,37,45,0,29,20],
[22,22,23,28,30,22,0,16],
[28,19,23,35,38,31,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,19,26,22,29,24],
[25,0,34,18,21,30,22,24],
[20,17,0,14,19,15,23,15],
[32,33,37,0,30,23,36,39],
[25,30,32,21,0,23,31,25],
[29,21,36,28,28,0,26,27],
[22,29,28,15,20,25,0,27],
[27,27,36,12,26,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,29,19,25,23,23],
[25,0,23,23,27,31,21,26],
[30,28,0,29,26,31,29,25],
[22,28,22,0,27,28,22,28],
[32,24,25,24,0,29,28,29],
[26,20,20,23,22,0,26,21],
[28,30,22,29,23,25,0,26],
[28,25,26,23,22,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,35,25,34,26,34,28],
[25,0,25,20,25,19,32,24],
[16,26,0,19,16,15,22,19],
[26,31,32,0,35,24,30,31],
[17,26,35,16,0,19,24,23],
[25,32,36,27,32,0,42,30],
[17,19,29,21,27,9,0,22],
[23,27,32,20,28,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,15,30,34,14,22,18],
[18,0,20,12,33,17,24,27],
[36,31,0,20,34,21,28,33],
[21,39,31,0,44,29,29,25],
[17,18,17,7,0,11,11,15],
[37,34,30,22,40,0,34,28],
[29,27,23,22,40,17,0,26],
[33,24,18,26,36,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,27,13,23,19,14,17],
[36,0,24,24,25,22,24,21],
[24,27,0,17,25,23,13,23],
[38,27,34,0,30,25,23,30],
[28,26,26,21,0,30,16,30],
[32,29,28,26,21,0,27,23],
[37,27,38,28,35,24,0,21],
[34,30,28,21,21,28,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,27,25,23,30,29],
[25,0,29,29,28,27,28,26],
[21,22,0,22,24,21,24,22],
[24,22,29,0,19,18,20,25],
[26,23,27,32,0,29,30,23],
[28,24,30,33,22,0,26,23],
[21,23,27,31,21,25,0,24],
[22,25,29,26,28,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,29,25,21,26,25],
[23,0,37,27,25,27,33,26],
[22,14,0,23,20,18,23,25],
[22,24,28,0,19,23,30,33],
[26,26,31,32,0,19,30,31],
[30,24,33,28,32,0,34,31],
[25,18,28,21,21,17,0,27],
[26,25,26,18,20,20,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,26,23,27,26,26],
[26,0,28,30,27,19,23,24],
[23,23,0,30,20,20,21,21],
[25,21,21,0,19,21,21,17],
[28,24,31,32,0,24,22,21],
[24,32,31,30,27,0,24,26],
[25,28,30,30,29,27,0,28],
[25,27,30,34,30,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,22,28,28,34,30],
[30,0,21,12,25,13,35,26],
[30,30,0,10,25,21,44,26],
[29,39,41,0,37,21,39,26],
[23,26,26,14,0,9,44,26],
[23,38,30,30,42,0,44,26],
[17,16,7,12,7,7,0,16],
[21,25,25,25,25,25,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,30,28,27,22,21,21],
[29,0,32,32,29,22,18,24],
[21,19,0,24,19,21,19,23],
[23,19,27,0,22,23,15,19],
[24,22,32,29,0,26,27,21],
[29,29,30,28,25,0,27,29],
[30,33,32,36,24,24,0,23],
[30,27,28,32,30,22,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,24,26,29,24,28],
[28,0,23,24,24,27,25,28],
[27,28,0,26,27,26,24,30],
[27,27,25,0,22,29,28,34],
[25,27,24,29,0,27,27,31],
[22,24,25,22,24,0,27,30],
[27,26,27,23,24,24,0,32],
[23,23,21,17,20,21,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,30,33,21,21,27],
[29,0,30,35,24,24,28,23],
[27,21,0,32,29,22,22,23],
[21,16,19,0,22,18,15,22],
[18,27,22,29,0,31,21,24],
[30,27,29,33,20,0,20,26],
[30,23,29,36,30,31,0,33],
[24,28,28,29,27,25,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,20,38,26,33,29],
[18,0,28,9,32,17,26,29],
[20,23,0,15,30,27,35,19],
[31,42,36,0,34,23,35,36],
[13,19,21,17,0,11,22,25],
[25,34,24,28,40,0,26,30],
[18,25,16,16,29,25,0,23],
[22,22,32,15,26,21,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,33,28,21,36,18,29],
[20,0,21,21,23,28,20,22],
[18,30,0,25,22,29,22,24],
[23,30,26,0,18,32,18,25],
[30,28,29,33,0,33,27,25],
[15,23,22,19,18,0,14,21],
[33,31,29,33,24,37,0,28],
[22,29,27,26,26,30,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,34,27,26,31,25],
[19,0,19,25,23,22,23,13],
[25,32,0,31,32,26,26,18],
[17,26,20,0,20,25,24,19],
[24,28,19,31,0,24,25,18],
[25,29,25,26,27,0,25,27],
[20,28,25,27,26,26,0,19],
[26,38,33,32,33,24,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,23,26,29,27,29],
[27,0,26,27,27,26,24,31],
[28,25,0,28,26,26,26,34],
[28,24,23,0,24,29,27,27],
[25,24,25,27,0,24,24,33],
[22,25,25,22,27,0,24,27],
[24,27,25,24,27,27,0,26],
[22,20,17,24,18,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,21,25,26,30,27],
[30,0,20,21,22,20,22,14],
[28,31,0,18,33,32,31,18],
[30,30,33,0,33,24,38,22],
[26,29,18,18,0,17,21,10],
[25,31,19,27,34,0,29,21],
[21,29,20,13,30,22,0,16],
[24,37,33,29,41,30,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,18,19,17,27,23,31],
[27,0,21,20,25,20,28,20],
[33,30,0,35,28,31,28,24],
[32,31,16,0,19,29,22,26],
[34,26,23,32,0,27,26,35],
[24,31,20,22,24,0,28,27],
[28,23,23,29,25,23,0,25],
[20,31,27,25,16,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,16,30,37,37,14],
[22,0,29,9,23,34,25,9],
[22,22,0,26,35,35,35,10],
[35,42,25,0,23,37,37,28],
[21,28,16,28,0,41,41,16],
[14,17,16,14,10,0,25,14],
[14,26,16,14,10,26,0,14],
[37,42,41,23,35,37,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,16,24,23,26,26],
[21,0,24,19,28,21,31,24],
[22,27,0,24,24,25,31,20],
[35,32,27,0,30,25,27,27],
[27,23,27,21,0,22,33,26],
[28,30,26,26,29,0,25,26],
[25,20,20,24,18,26,0,20],
[25,27,31,24,25,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,30,25,29,31,17],
[25,0,27,42,34,31,30,26],
[28,24,0,38,27,28,28,14],
[21,9,13,0,29,18,24,12],
[26,17,24,22,0,28,27,14],
[22,20,23,33,23,0,26,21],
[20,21,23,27,24,25,0,15],
[34,25,37,39,37,30,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,27,25,19,33,34],
[29,0,24,25,32,24,31,34],
[28,27,0,26,27,19,31,41],
[24,26,25,0,23,28,27,30],
[26,19,24,28,0,16,29,33],
[32,27,32,23,35,0,28,37],
[18,20,20,24,22,23,0,30],
[17,17,10,21,18,14,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,24,22,23,26,38],
[19,0,20,22,18,22,22,26],
[21,31,0,26,18,18,23,30],
[27,29,25,0,30,24,24,36],
[29,33,33,21,0,30,31,38],
[28,29,33,27,21,0,29,33],
[25,29,28,27,20,22,0,32],
[13,25,21,15,13,18,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,20,19,22,34,24],
[30,0,26,22,34,27,37,31],
[29,25,0,33,27,27,30,24],
[31,29,18,0,29,29,38,31],
[32,17,24,22,0,23,35,16],
[29,24,24,22,28,0,35,35],
[17,14,21,13,16,16,0,12],
[27,20,27,20,35,16,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,38,36,42,38,47],
[28,0,28,40,19,30,42,30],
[27,23,0,38,36,42,38,38],
[13,11,13,0,24,30,51,26],
[15,32,15,27,0,30,42,26],
[9,21,9,21,21,0,21,9],
[13,9,13,0,9,30,0,26],
[4,21,13,25,25,42,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,34,36,29,26,28],
[28,0,19,18,27,26,21,15],
[27,32,0,27,28,27,22,16],
[17,33,24,0,36,30,20,24],
[15,24,23,15,0,18,20,18],
[22,25,24,21,33,0,19,27],
[25,30,29,31,31,32,0,25],
[23,36,35,27,33,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,24,28,32,28,34],
[30,0,26,29,32,27,25,32],
[24,25,0,18,27,23,28,31],
[27,22,33,0,37,32,29,41],
[23,19,24,14,0,25,20,27],
[19,24,28,19,26,0,28,35],
[23,26,23,22,31,23,0,26],
[17,19,20,10,24,16,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,37,33,30,28,26],
[27,0,36,31,33,34,25,31],
[27,15,0,25,30,23,26,19],
[14,20,26,0,27,19,21,19],
[18,18,21,24,0,25,17,13],
[21,17,28,32,26,0,24,19],
[23,26,25,30,34,27,0,15],
[25,20,32,32,38,32,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,26,25,26,22,26,25],
[18,0,25,22,22,20,19,24],
[25,26,0,27,26,22,23,29],
[26,29,24,0,31,24,22,27],
[25,29,25,20,0,25,24,28],
[29,31,29,27,26,0,25,31],
[25,32,28,29,27,26,0,32],
[26,27,22,24,23,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,26,0,20,12,23,17],
[34,0,26,26,34,12,14,21],
[25,25,0,8,37,9,17,17],
[51,25,43,0,51,21,31,17],
[31,17,14,0,0,0,23,9],
[39,39,42,30,51,0,31,25],
[28,37,34,20,28,20,0,37],
[34,30,34,34,42,26,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,24,27,27,27,30],
[23,0,23,19,23,20,21,24],
[21,28,0,24,26,26,21,26],
[27,32,27,0,30,24,26,31],
[24,28,25,21,0,25,23,25],
[24,31,25,27,26,0,24,27],
[24,30,30,25,28,27,0,29],
[21,27,25,20,26,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,31,34,32,29,27,30],
[28,0,29,26,27,25,21,36],
[20,22,0,25,31,29,27,34],
[17,25,26,0,26,25,19,29],
[19,24,20,25,0,19,27,26],
[22,26,22,26,32,0,27,24],
[24,30,24,32,24,24,0,32],
[21,15,17,22,25,27,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,24,31,23,28,28],
[27,0,24,30,32,23,29,32],
[25,27,0,24,26,24,25,30],
[27,21,27,0,29,31,19,29],
[20,19,25,22,0,25,19,27],
[28,28,27,20,26,0,23,27],
[23,22,26,32,32,28,0,27],
[23,19,21,22,24,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,14,0,0,11,11],
[41,0,41,36,29,14,26,26],
[34,10,0,31,34,19,21,22],
[37,15,20,0,18,19,11,35],
[51,22,17,33,0,31,17,34],
[51,37,32,32,20,0,17,41],
[40,25,30,40,34,34,0,37],
[40,25,29,16,17,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,19,25,19,20,19],
[32,0,21,26,25,23,28,27],
[26,30,0,25,28,27,26,25],
[32,25,26,0,27,26,23,25],
[26,26,23,24,0,27,21,24],
[32,28,24,25,24,0,24,27],
[31,23,25,28,30,27,0,27],
[32,24,26,26,27,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,32,34,29,29,33,23],
[26,0,33,32,30,28,25,33],
[19,18,0,24,26,17,22,19],
[17,19,27,0,35,30,28,19],
[22,21,25,16,0,16,21,11],
[22,23,34,21,35,0,34,21],
[18,26,29,23,30,17,0,25],
[28,18,32,32,40,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,18,20,29,26,29],
[28,0,30,25,21,26,30,19],
[23,21,0,16,18,18,26,16],
[33,26,35,0,26,26,37,24],
[31,30,33,25,0,30,25,21],
[22,25,33,25,21,0,24,21],
[25,21,25,14,26,27,0,21],
[22,32,35,27,30,30,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,28,20,17,24,17],
[27,0,21,26,24,17,33,18],
[21,30,0,29,21,20,37,21],
[23,25,22,0,14,21,27,17],
[31,27,30,37,0,29,38,23],
[34,34,31,30,22,0,33,31],
[27,18,14,24,13,18,0,13],
[34,33,30,34,28,20,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,28,22,29,30,26],
[23,0,19,24,26,24,29,25],
[27,32,0,29,25,29,31,27],
[23,27,22,0,25,25,31,23],
[29,25,26,26,0,28,30,25],
[22,27,22,26,23,0,28,19],
[21,22,20,20,21,23,0,20],
[25,26,24,28,26,32,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,18,19,20,21,22],
[25,0,26,23,21,22,20,24],
[32,25,0,30,23,20,24,32],
[33,28,21,0,28,27,27,32],
[32,30,28,23,0,29,24,25],
[31,29,31,24,22,0,25,28],
[30,31,27,24,27,26,0,28],
[29,27,19,19,26,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,25,23,28,24,25],
[29,0,29,26,21,26,25,27],
[22,22,0,19,20,21,20,21],
[26,25,32,0,27,27,28,30],
[28,30,31,24,0,27,24,26],
[23,25,30,24,24,0,20,27],
[27,26,31,23,27,31,0,26],
[26,24,30,21,25,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,12,18,23,19,37],
[32,0,26,21,26,28,21,34],
[33,25,0,23,24,20,23,41],
[39,30,28,0,30,17,28,41],
[33,25,27,21,0,25,28,35],
[28,23,31,34,26,0,37,35],
[32,30,28,23,23,14,0,40],
[14,17,10,10,16,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,19,32,37,36,19,32],
[20,0,15,7,23,21,12,19],
[32,36,0,24,34,32,36,29],
[19,44,27,0,27,25,23,29],
[14,28,17,24,0,20,17,25],
[15,30,19,26,31,0,21,32],
[32,39,15,28,34,30,0,29],
[19,32,22,22,26,19,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,33,30,31,24,29],
[22,0,26,31,35,32,29,24],
[28,25,0,34,31,31,26,22],
[18,20,17,0,27,19,21,27],
[21,16,20,24,0,20,15,20],
[20,19,20,32,31,0,30,26],
[27,22,25,30,36,21,0,29],
[22,27,29,24,31,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,25,24,28,16,18],
[30,0,26,33,21,31,23,25],
[29,25,0,29,27,31,26,22],
[26,18,22,0,20,28,19,18],
[27,30,24,31,0,29,24,26],
[23,20,20,23,22,0,22,18],
[35,28,25,32,27,29,0,26],
[33,26,29,33,25,33,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,20,23,21,21,23],
[29,0,30,28,27,23,27,31],
[28,21,0,29,29,23,25,23],
[31,23,22,0,27,26,27,29],
[28,24,22,24,0,32,30,28],
[30,28,28,25,19,0,24,29],
[30,24,26,24,21,27,0,29],
[28,20,28,22,23,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,36,24,41,45,40],
[23,0,23,31,28,25,23,38],
[22,28,0,21,24,31,27,40],
[15,20,30,0,20,15,30,39],
[27,23,27,31,0,27,27,40],
[10,26,20,36,24,0,40,28],
[6,28,24,21,24,11,0,30],
[11,13,11,12,11,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,29,26,27,34,25],
[32,0,25,35,32,32,35,29],
[24,26,0,27,24,27,26,25],
[22,16,24,0,25,25,27,23],
[25,19,27,26,0,28,24,26],
[24,19,24,26,23,0,27,23],
[17,16,25,24,27,24,0,22],
[26,22,26,28,25,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,29,22,27,26,23,24],
[17,0,17,18,22,17,15,20],
[22,34,0,25,25,22,22,26],
[29,33,26,0,29,20,22,30],
[24,29,26,22,0,19,23,24],
[25,34,29,31,32,0,28,32],
[28,36,29,29,28,23,0,31],
[27,31,25,21,27,19,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,26,28,38,27,24],
[27,0,21,19,34,26,34,30],
[24,30,0,23,34,28,36,30],
[25,32,28,0,37,27,35,30],
[23,17,17,14,0,24,24,23],
[13,25,23,24,27,0,28,18],
[24,17,15,16,27,23,0,23],
[27,21,21,21,28,33,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,15,34,22,29,26,23],
[26,0,15,28,19,24,32,20],
[36,36,0,28,27,32,36,25],
[17,23,23,0,16,19,17,21],
[29,32,24,35,0,32,39,31],
[22,27,19,32,19,0,25,20],
[25,19,15,34,12,26,0,22],
[28,31,26,30,20,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,27,17,28,24,30,27],
[34,0,33,28,30,32,23,30],
[24,18,0,21,21,32,28,23],
[34,23,30,0,27,33,27,34],
[23,21,30,24,0,27,25,37],
[27,19,19,18,24,0,23,27],
[21,28,23,24,26,28,0,29],
[24,21,28,17,14,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,25,24,26,25,17,31],
[17,0,17,3,22,31,13,20],
[26,34,0,12,15,34,27,37],
[27,48,39,0,31,34,22,35],
[25,29,36,20,0,28,15,25],
[26,20,17,17,23,0,20,26],
[34,38,24,29,36,31,0,32],
[20,31,14,16,26,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,19,28,41,34,33,34],
[26,0,10,13,41,27,26,27],
[32,41,0,24,42,23,30,30],
[23,38,27,0,48,31,30,38],
[10,10,9,3,0,1,8,1],
[17,24,28,20,50,0,40,37],
[18,25,21,21,43,11,0,22],
[17,24,21,13,50,14,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,17,27,21,18,26],
[26,0,26,24,33,24,28,28],
[29,25,0,22,29,22,24,26],
[34,27,29,0,33,28,24,28],
[24,18,22,18,0,19,15,20],
[30,27,29,23,32,0,31,29],
[33,23,27,27,36,20,0,26],
[25,23,25,23,31,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,27,32,27,26,22],
[22,0,31,25,30,23,30,25],
[24,20,0,26,27,17,23,21],
[24,26,25,0,30,15,23,22],
[19,21,24,21,0,21,22,18],
[24,28,34,36,30,0,32,26],
[25,21,28,28,29,19,0,23],
[29,26,30,29,33,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,28,35,34,30,28],
[26,0,21,19,27,29,29,20],
[23,30,0,23,24,26,27,26],
[23,32,28,0,31,36,30,25],
[16,24,27,20,0,29,26,21],
[17,22,25,15,22,0,24,18],
[21,22,24,21,25,27,0,16],
[23,31,25,26,30,33,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 51, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_51.csv", index=False, header=False)