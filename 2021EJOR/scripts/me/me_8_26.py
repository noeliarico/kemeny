
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,18,8,10,14,11,18,12],
[8,0,12,7,12,5,14,10],
[18,14,0,13,15,16,20,16],
[16,19,13,0,19,19,21,17],
[12,14,11,7,0,6,18,11],
[15,21,10,7,20,0,22,15],
[8,12,6,5,8,4,0,10],
[14,16,10,9,15,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,8,5,5,20,14],
[11,0,5,5,7,5,21,5],
[16,21,0,14,11,11,25,10],
[18,21,12,0,16,16,26,16],
[21,19,15,10,0,20,19,15],
[21,21,15,10,6,0,25,9],
[6,5,1,0,7,1,0,4],
[12,21,16,10,11,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,8,13,15,20,15],
[13,0,11,13,19,18,16,16],
[18,15,0,13,15,18,17,20],
[18,13,13,0,13,23,20,16],
[13,7,11,13,0,20,10,9],
[11,8,8,3,6,0,13,12],
[6,10,9,6,16,13,0,13],
[11,10,6,10,17,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,11,9,12,15,7],
[13,0,14,9,10,15,9,11],
[13,12,0,9,9,12,11,10],
[15,17,17,0,13,20,18,12],
[17,16,17,13,0,12,15,11],
[14,11,14,6,14,0,10,13],
[11,17,15,8,11,16,0,13],
[19,15,16,14,15,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,14,10,11,11,15],
[9,0,15,14,7,11,9,13],
[13,11,0,11,8,14,14,10],
[12,12,15,0,9,11,10,11],
[16,19,18,17,0,14,15,12],
[15,15,12,15,12,0,14,14],
[15,17,12,16,11,12,0,14],
[11,13,16,15,14,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,16,13,11,12,12],
[14,0,13,13,13,13,14,13],
[15,13,0,14,16,12,13,12],
[10,13,12,0,12,11,9,12],
[13,13,10,14,0,9,10,13],
[15,13,14,15,17,0,12,16],
[14,12,13,17,16,14,0,14],
[14,13,14,14,13,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,14,14,15,12,13],
[14,0,13,15,14,12,13,12],
[14,13,0,14,13,13,13,9],
[12,11,12,0,16,9,11,10],
[12,12,13,10,0,12,10,10],
[11,14,13,17,14,0,11,12],
[14,13,13,15,16,15,0,13],
[13,14,17,16,16,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,0,0,6,26,0,3],
[19,0,19,13,19,26,13,19],
[26,7,0,0,13,26,10,3],
[26,13,26,0,26,26,16,26],
[20,7,13,0,0,26,10,13],
[0,0,0,0,0,0,0,0],
[26,13,16,10,16,26,0,19],
[23,7,23,0,13,26,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,14,12,15,8,8],
[16,0,13,13,19,15,12,13],
[13,13,0,15,14,11,8,8],
[12,13,11,0,15,17,10,11],
[14,7,12,11,0,10,8,7],
[11,11,15,9,16,0,11,6],
[18,14,18,16,18,15,0,10],
[18,13,18,15,19,20,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,3,10,4,7,7,4],
[17,0,14,17,13,14,20,17],
[23,12,0,10,13,15,8,11],
[16,9,16,0,16,11,13,15],
[22,13,13,10,0,11,11,11],
[19,12,11,15,15,0,18,14],
[19,6,18,13,15,8,0,16],
[22,9,15,11,15,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,8,11,16,15,12],
[14,0,12,14,13,22,13,11],
[11,14,0,10,10,20,14,14],
[18,12,16,0,15,20,16,9],
[15,13,16,11,0,20,13,14],
[10,4,6,6,6,0,8,5],
[11,13,12,10,13,18,0,11],
[14,15,12,17,12,21,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,5,0,1,10,0],
[21,0,21,21,9,9,22,21],
[21,5,0,21,9,0,22,12],
[21,5,5,0,9,0,10,0],
[26,17,17,17,0,5,22,16],
[25,17,26,26,21,0,22,12],
[16,4,4,16,4,4,0,4],
[26,5,14,26,10,14,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,8,15,14,10,10],
[13,0,12,14,13,16,6,10],
[14,14,0,12,18,16,13,12],
[18,12,14,0,13,18,9,9],
[11,13,8,13,0,14,11,10],
[12,10,10,8,12,0,9,7],
[16,20,13,17,15,17,0,13],
[16,16,14,17,16,19,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,12,15,11,18,16],
[13,0,13,14,15,11,18,13],
[12,13,0,12,12,11,13,17],
[14,12,14,0,10,11,11,20],
[11,11,14,16,0,16,18,16],
[15,15,15,15,10,0,10,21],
[8,8,13,15,8,16,0,16],
[10,13,9,6,10,5,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,11,11,15,16,12],
[11,0,10,6,8,8,13,7],
[15,16,0,11,8,16,16,15],
[15,20,15,0,13,19,15,15],
[15,18,18,13,0,14,16,13],
[11,18,10,7,12,0,15,10],
[10,13,10,11,10,11,0,9],
[14,19,11,11,13,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,14,16,18,15,9],
[12,0,15,13,9,16,12,14],
[16,11,0,15,14,15,14,16],
[12,13,11,0,13,17,13,15],
[10,17,12,13,0,17,16,15],
[8,10,11,9,9,0,13,10],
[11,14,12,13,10,13,0,11],
[17,12,10,11,11,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,13,10,11,17,13],
[18,0,16,17,16,13,18,16],
[12,10,0,17,7,12,15,13],
[13,9,9,0,5,11,12,9],
[16,10,19,21,0,13,16,14],
[15,13,14,15,13,0,13,13],
[9,8,11,14,10,13,0,9],
[13,10,13,17,12,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,20,14,16,8,26,16],
[12,0,9,12,8,8,12,5],
[6,17,0,11,10,14,10,14],
[12,14,15,0,14,9,12,16],
[10,18,16,12,0,14,21,20],
[18,18,12,17,12,0,18,12],
[0,14,16,14,5,8,0,16],
[10,21,12,10,6,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,13,11,14,13,12],
[12,0,12,13,15,14,18,17],
[17,14,0,16,12,17,19,18],
[13,13,10,0,10,15,14,14],
[15,11,14,16,0,14,15,16],
[12,12,9,11,12,0,15,15],
[13,8,7,12,11,11,0,13],
[14,9,8,12,10,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,14,14,16,12,16],
[9,0,9,13,10,13,11,15],
[12,17,0,14,14,17,15,19],
[12,13,12,0,13,13,10,16],
[12,16,12,13,0,13,11,16],
[10,13,9,13,13,0,10,14],
[14,15,11,16,15,16,0,20],
[10,11,7,10,10,12,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,22,17,13,16,15],
[11,0,11,18,17,14,18,15],
[9,15,0,16,11,13,10,17],
[4,8,10,0,9,9,10,14],
[9,9,15,17,0,14,16,15],
[13,12,13,17,12,0,15,16],
[10,8,16,16,10,11,0,14],
[11,11,9,12,11,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,10,15,12,15],
[15,0,12,13,15,9,16,17],
[12,14,0,12,14,13,16,14],
[15,13,14,0,14,11,14,17],
[16,11,12,12,0,13,13,15],
[11,17,13,15,13,0,17,15],
[14,10,10,12,13,9,0,11],
[11,9,12,9,11,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,11,11,7,10,10],
[15,0,7,12,13,9,11,15],
[17,19,0,15,22,11,13,19],
[15,14,11,0,16,12,12,18],
[15,13,4,10,0,9,9,14],
[19,17,15,14,17,0,9,17],
[16,15,13,14,17,17,0,14],
[16,11,7,8,12,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,5,15,13,14,10,22],
[12,0,13,13,14,9,8,18],
[21,13,0,16,15,12,9,18],
[11,13,10,0,14,9,12,20],
[13,12,11,12,0,8,10,20],
[12,17,14,17,18,0,15,20],
[16,18,17,14,16,11,0,22],
[4,8,8,6,6,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,9,16,17,20,18],
[11,0,8,8,9,10,10,17],
[14,18,0,12,10,17,13,16],
[17,18,14,0,9,14,20,17],
[10,17,16,17,0,19,16,19],
[9,16,9,12,7,0,7,12],
[6,16,13,6,10,19,0,13],
[8,9,10,9,7,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,12,0,6,19,0,6],
[20,0,25,13,6,19,6,6],
[14,1,0,0,6,19,0,0],
[26,13,26,0,13,26,13,7],
[20,20,20,13,0,13,19,13],
[7,7,7,0,13,0,6,0],
[26,20,26,13,7,20,0,6],
[20,20,26,19,13,26,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,15,15,19,14,13],
[11,0,16,14,11,14,7,11],
[10,10,0,11,7,14,5,9],
[11,12,15,0,14,15,10,13],
[11,15,19,12,0,15,10,10],
[7,12,12,11,11,0,12,12],
[12,19,21,16,16,14,0,16],
[13,15,17,13,16,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,12,17,14,10,13],
[8,0,18,15,13,15,12,13],
[12,8,0,14,13,16,10,12],
[14,11,12,0,12,14,13,10],
[9,13,13,14,0,14,10,15],
[12,11,10,12,12,0,10,9],
[16,14,16,13,16,16,0,19],
[13,13,14,16,11,17,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,12,13,13,16,13],
[10,0,11,10,13,14,16,10],
[13,15,0,13,9,8,17,10],
[14,16,13,0,15,12,13,14],
[13,13,17,11,0,15,17,15],
[13,12,18,14,11,0,17,14],
[10,10,9,13,9,9,0,11],
[13,16,16,12,11,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,16,12,15,12,17,10],
[19,0,12,14,18,18,22,15],
[10,14,0,11,17,12,12,10],
[14,12,15,0,14,9,15,16],
[11,8,9,12,0,8,14,9],
[14,8,14,17,18,0,20,9],
[9,4,14,11,12,6,0,6],
[16,11,16,10,17,17,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,13,15,8,19,14],
[17,0,16,16,18,13,18,16],
[11,10,0,13,16,7,14,8],
[13,10,13,0,14,10,15,12],
[11,8,10,12,0,13,12,13],
[18,13,19,16,13,0,19,10],
[7,8,12,11,14,7,0,9],
[12,10,18,14,13,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,10,12,8,12,8],
[11,0,5,10,11,9,8,10],
[16,21,0,15,15,14,12,12],
[16,16,11,0,16,12,15,14],
[14,15,11,10,0,11,13,14],
[18,17,12,14,15,0,14,14],
[14,18,14,11,13,12,0,15],
[18,16,14,12,12,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,15,14,14,20,14,11],
[21,0,15,14,9,20,21,15],
[11,11,0,11,11,17,20,17],
[12,12,15,0,6,6,21,6],
[12,17,15,20,0,11,21,6],
[6,6,9,20,15,0,15,6],
[12,5,6,5,5,11,0,11],
[15,11,9,20,20,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,16,18,17,17,13],
[6,0,14,12,14,14,11,12],
[6,12,0,10,11,11,15,12],
[10,14,16,0,15,14,10,11],
[8,12,15,11,0,13,11,9],
[9,12,15,12,13,0,13,8],
[9,15,11,16,15,13,0,8],
[13,14,14,15,17,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,14,9,11,9,9],
[17,0,13,17,7,10,10,19],
[16,13,0,18,9,13,12,14],
[12,9,8,0,5,5,7,7],
[17,19,17,21,0,11,15,17],
[15,16,13,21,15,0,13,13],
[17,16,14,19,11,13,0,14],
[17,7,12,19,9,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,13,6,16,9,13,16],
[19,0,9,6,12,6,9,9],
[13,17,0,10,20,13,13,13],
[20,20,16,0,23,26,13,16],
[10,14,6,3,0,13,3,3],
[17,20,13,0,13,0,13,13],
[13,17,13,13,23,13,0,14],
[10,17,13,10,23,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,11,12,18,14],
[14,0,15,13,13,18,19,17],
[12,11,0,12,12,11,18,14],
[12,13,14,0,12,8,16,17],
[15,13,14,14,0,15,19,19],
[14,8,15,18,11,0,17,20],
[8,7,8,10,7,9,0,8],
[12,9,12,9,7,6,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,14,14,16,9,14],
[15,0,15,17,12,14,12,13],
[11,11,0,16,11,14,13,17],
[12,9,10,0,12,11,14,12],
[12,14,15,14,0,17,15,19],
[10,12,12,15,9,0,13,10],
[17,14,13,12,11,13,0,13],
[12,13,9,14,7,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,15,18,12,18,17],
[6,0,10,7,10,7,10,9],
[3,16,0,7,10,10,10,9],
[11,19,19,0,14,23,23,14],
[8,16,16,12,0,13,18,11],
[14,19,16,3,13,0,16,10],
[8,16,16,3,8,10,0,5],
[9,17,17,12,15,16,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,14,14,14,17,16],
[12,0,12,10,12,11,12,15],
[13,14,0,10,12,7,10,11],
[12,16,16,0,12,8,11,15],
[12,14,14,14,0,13,20,11],
[12,15,19,18,13,0,16,12],
[9,14,16,15,6,10,0,12],
[10,11,15,11,15,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,10,13,9,22,13],
[13,0,9,22,13,21,21,16],
[8,17,0,17,17,17,26,17],
[16,4,9,0,4,4,13,13],
[13,13,9,22,0,18,22,22],
[17,5,9,22,8,0,22,17],
[4,5,0,13,4,4,0,8],
[13,10,9,13,4,9,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,14,14,14,15,16,13],
[6,0,9,8,13,9,12,11],
[12,17,0,12,15,11,13,12],
[12,18,14,0,14,13,11,12],
[12,13,11,12,0,11,14,14],
[11,17,15,13,15,0,14,13],
[10,14,13,15,12,12,0,9],
[13,15,14,14,12,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,12,12,13,15,12],
[13,0,15,17,13,16,8,15],
[16,11,0,8,14,17,10,12],
[14,9,18,0,17,13,12,19],
[14,13,12,9,0,8,18,17],
[13,10,9,13,18,0,12,12],
[11,18,16,14,8,14,0,16],
[14,11,14,7,9,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,21,9,18,15,10,13],
[16,0,19,13,17,16,13,15],
[5,7,0,8,8,9,8,6],
[17,13,18,0,15,17,12,12],
[8,9,18,11,0,15,9,8],
[11,10,17,9,11,0,10,5],
[16,13,18,14,17,16,0,13],
[13,11,20,14,18,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,12,5,11,9,16],
[15,0,9,9,11,4,6,9],
[17,17,0,9,13,14,12,15],
[14,17,17,0,6,18,14,14],
[21,15,13,20,0,15,10,21],
[15,22,12,8,11,0,17,15],
[17,20,14,12,16,9,0,15],
[10,17,11,12,5,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,14,18,17,12,8],
[15,0,13,12,17,16,14,12],
[12,13,0,12,15,15,14,13],
[12,14,14,0,13,17,13,12],
[8,9,11,13,0,13,13,9],
[9,10,11,9,13,0,9,9],
[14,12,12,13,13,17,0,9],
[18,14,13,14,17,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,14,13,11,10,12],
[13,0,8,12,11,11,14,13],
[17,18,0,17,10,19,15,11],
[12,14,9,0,10,11,13,11],
[13,15,16,16,0,14,18,13],
[15,15,7,15,12,0,14,13],
[16,12,11,13,8,12,0,10],
[14,13,15,15,13,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,9,16,12,17,10],
[8,0,9,10,12,10,7,6],
[9,17,0,14,10,13,10,9],
[17,16,12,0,12,14,13,12],
[10,14,16,14,0,13,11,10],
[14,16,13,12,13,0,15,14],
[9,19,16,13,15,11,0,7],
[16,20,17,14,16,12,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,11,17,12,11,13],
[17,0,13,15,20,13,17,13],
[11,13,0,8,17,10,13,14],
[15,11,18,0,20,13,13,15],
[9,6,9,6,0,11,11,11],
[14,13,16,13,15,0,16,9],
[15,9,13,13,15,10,0,12],
[13,13,12,11,15,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,12,8,13,8,9],
[14,0,16,13,14,16,10,13],
[15,10,0,10,9,10,11,8],
[14,13,16,0,13,13,10,11],
[18,12,17,13,0,17,10,10],
[13,10,16,13,9,0,11,12],
[18,16,15,16,16,15,0,13],
[17,13,18,15,16,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,14,14,14,13,15],
[12,0,9,16,16,14,10,14],
[14,17,0,17,16,16,13,15],
[12,10,9,0,13,14,11,13],
[12,10,10,13,0,12,13,13],
[12,12,10,12,14,0,12,15],
[13,16,13,15,13,14,0,16],
[11,12,11,13,13,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,14,8,16,7,8],
[10,0,7,9,6,15,8,7],
[18,19,0,12,9,17,13,10],
[12,17,14,0,10,20,11,15],
[18,20,17,16,0,18,13,12],
[10,11,9,6,8,0,10,10],
[19,18,13,15,13,16,0,10],
[18,19,16,11,14,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,19,10,23,19,18],
[10,0,14,10,9,14,16,9],
[13,12,0,14,13,19,15,14],
[7,16,12,0,9,17,14,17],
[16,17,13,17,0,23,19,18],
[3,12,7,9,3,0,8,7],
[7,10,11,12,7,18,0,15],
[8,17,12,9,8,19,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,8,12,13,16,12],
[14,0,14,12,13,11,15,11],
[8,12,0,7,11,7,12,8],
[18,14,19,0,17,12,18,16],
[14,13,15,9,0,12,14,13],
[13,15,19,14,14,0,19,11],
[10,11,14,8,12,7,0,12],
[14,15,18,10,13,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,4,1,10,26,10,10],
[25,0,4,12,13,26,13,13],
[22,22,0,22,9,23,23,23],
[25,14,4,0,13,26,13,26],
[16,13,17,13,0,17,17,17],
[0,0,3,0,9,0,10,9],
[16,13,3,13,9,16,0,16],
[16,13,3,0,9,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,18,15,16,22,14],
[15,0,20,19,11,11,17,11],
[12,6,0,17,14,15,21,13],
[8,7,9,0,6,7,9,5],
[11,15,12,20,0,11,22,11],
[10,15,11,19,15,0,18,19],
[4,9,5,17,4,8,0,4],
[12,15,13,21,15,7,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,13,12,12,16,16],
[14,0,18,14,13,14,16,17],
[13,8,0,10,13,8,11,14],
[13,12,16,0,10,10,11,15],
[14,13,13,16,0,14,16,17],
[14,12,18,16,12,0,16,16],
[10,10,15,15,10,10,0,15],
[10,9,12,11,9,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,12,12,19,14,13],
[17,0,10,13,10,15,11,13],
[13,16,0,20,13,12,15,16],
[14,13,6,0,16,17,10,16],
[14,16,13,10,0,15,19,11],
[7,11,14,9,11,0,12,5],
[12,15,11,16,7,14,0,13],
[13,13,10,10,15,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,0,13,2,23,13,14],
[14,0,1,13,6,13,13,4],
[26,25,0,13,15,25,26,26],
[13,13,13,0,5,13,15,13],
[24,20,11,21,0,23,23,24],
[3,13,1,13,3,0,13,11],
[13,13,0,11,3,13,0,13],
[12,22,0,13,2,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,15,17,14,13,13],
[12,0,15,12,12,9,10,11],
[16,11,0,13,14,11,14,13],
[11,14,13,0,10,14,12,15],
[9,14,12,16,0,16,13,14],
[12,17,15,12,10,0,10,15],
[13,16,12,14,13,16,0,12],
[13,15,13,11,12,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,15,13,16,17,17],
[11,0,12,13,14,14,16,15],
[10,14,0,11,14,14,12,13],
[11,13,15,0,14,13,14,16],
[13,12,12,12,0,14,14,17],
[10,12,12,13,12,0,13,15],
[9,10,14,12,12,13,0,11],
[9,11,13,10,9,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,9,8,8,17,8],
[13,0,12,12,13,14,14,9],
[18,14,0,16,15,7,15,12],
[17,14,10,0,12,10,21,19],
[18,13,11,14,0,11,14,16],
[18,12,19,16,15,0,20,12],
[9,12,11,5,12,6,0,10],
[18,17,14,7,10,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,17,17,12,20,19],
[10,0,14,14,15,11,11,16],
[9,12,0,11,13,10,12,15],
[9,12,15,0,13,14,13,14],
[9,11,13,13,0,7,14,13],
[14,15,16,12,19,0,15,17],
[6,15,14,13,12,11,0,14],
[7,10,11,12,13,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,10,9,10,12,12],
[19,0,18,13,13,12,15,14],
[14,8,0,12,11,9,15,12],
[16,13,14,0,15,12,12,10],
[17,13,15,11,0,13,12,9],
[16,14,17,14,13,0,15,12],
[14,11,11,14,14,11,0,10],
[14,12,14,16,17,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,13,13,13,14,12],
[8,0,5,9,4,7,7,10],
[12,21,0,11,12,9,12,13],
[13,17,15,0,9,8,9,13],
[13,22,14,17,0,10,18,16],
[13,19,17,18,16,0,17,18],
[12,19,14,17,8,9,0,15],
[14,16,13,13,10,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,18,13,14,12,16],
[9,0,8,10,13,11,8,12],
[13,18,0,15,18,14,13,18],
[8,16,11,0,10,14,11,14],
[13,13,8,16,0,12,12,13],
[12,15,12,12,14,0,13,16],
[14,18,13,15,14,13,0,15],
[10,14,8,12,13,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,13,22,22,22,16,22],
[4,0,2,2,6,2,2,15],
[13,24,0,16,20,17,16,26],
[4,24,10,0,18,6,5,21],
[4,20,6,8,0,6,0,21],
[4,24,9,20,20,0,14,20],
[10,24,10,21,26,12,0,21],
[4,11,0,5,5,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,15,15,17,14,13],
[15,0,19,14,14,13,12,12],
[12,7,0,10,12,15,12,10],
[11,12,16,0,13,18,13,12],
[11,12,14,13,0,15,11,11],
[9,13,11,8,11,0,6,7],
[12,14,14,13,15,20,0,12],
[13,14,16,14,15,19,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,0,2,13,0,0,15],
[26,0,13,13,15,13,0,26],
[26,13,0,15,15,15,13,15],
[24,13,11,0,13,13,13,24],
[13,11,11,13,0,11,11,26],
[26,13,11,13,15,0,13,26],
[26,26,13,13,15,13,0,26],
[11,0,11,2,0,0,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,9,17,20,7,8],
[19,0,20,20,22,20,19,10],
[12,6,0,13,13,16,8,13],
[17,6,13,0,16,19,12,12],
[9,4,13,10,0,15,9,8],
[6,6,10,7,11,0,6,9],
[19,7,18,14,17,20,0,10],
[18,16,13,14,18,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,15,15,14,12,15],
[14,0,12,14,12,13,14,12],
[13,14,0,19,15,17,15,13],
[11,12,7,0,10,18,10,13],
[11,14,11,16,0,14,12,13],
[12,13,9,8,12,0,11,12],
[14,12,11,16,14,15,0,11],
[11,14,13,13,13,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,12,12,12,11,12],
[8,0,9,9,8,9,9,10],
[12,17,0,11,14,10,10,11],
[14,17,15,0,16,9,12,15],
[14,18,12,10,0,14,10,13],
[14,17,16,17,12,0,12,12],
[15,17,16,14,16,14,0,13],
[14,16,15,11,13,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,13,12,13,15,14],
[13,0,13,11,9,13,16,12],
[11,13,0,10,9,15,15,12],
[13,15,16,0,14,12,16,13],
[14,17,17,12,0,15,19,16],
[13,13,11,14,11,0,17,13],
[11,10,11,10,7,9,0,9],
[12,14,14,13,10,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,14,14,17,15],
[14,0,15,14,15,15,18,10],
[12,11,0,15,14,16,18,12],
[12,12,11,0,9,12,9,12],
[12,11,12,17,0,12,16,11],
[12,11,10,14,14,0,19,12],
[9,8,8,17,10,7,0,10],
[11,16,14,14,15,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,14,15,12,18,14],
[9,0,8,16,7,10,15,14],
[13,18,0,17,15,15,15,17],
[12,10,9,0,4,9,15,15],
[11,19,11,22,0,16,20,19],
[14,16,11,17,10,0,18,14],
[8,11,11,11,6,8,0,11],
[12,12,9,11,7,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,16,11,14,22,13],
[10,0,11,15,9,13,17,8],
[18,15,0,16,10,13,21,12],
[10,11,10,0,10,9,12,7],
[15,17,16,16,0,12,20,14],
[12,13,13,17,14,0,17,13],
[4,9,5,14,6,9,0,6],
[13,18,14,19,12,13,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,11,8,8,16,11],
[12,0,11,15,11,12,15,12],
[12,15,0,19,15,14,17,17],
[15,11,7,0,9,9,13,13],
[18,15,11,17,0,12,15,16],
[18,14,12,17,14,0,21,12],
[10,11,9,13,11,5,0,12],
[15,14,9,13,10,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,11,11,12,16,15],
[10,0,11,14,13,14,15,12],
[16,15,0,13,13,15,13,13],
[15,12,13,0,15,11,10,15],
[15,13,13,11,0,14,15,18],
[14,12,11,15,12,0,19,16],
[10,11,13,16,11,7,0,13],
[11,14,13,11,8,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,13,13,9,13,16],
[8,0,9,7,11,7,10,8],
[15,17,0,16,13,13,17,12],
[13,19,10,0,17,8,15,14],
[13,15,13,9,0,11,14,14],
[17,19,13,18,15,0,17,15],
[13,16,9,11,12,9,0,9],
[10,18,14,12,12,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,14,13,10,14,13],
[11,0,9,13,9,8,6,14],
[17,17,0,10,12,10,11,12],
[12,13,16,0,10,13,11,15],
[13,17,14,16,0,12,9,13],
[16,18,16,13,14,0,12,15],
[12,20,15,15,17,14,0,18],
[13,12,14,11,13,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,15,15,16,13,17],
[8,0,17,14,15,16,11,17],
[11,9,0,12,14,17,12,14],
[11,12,14,0,15,18,15,15],
[11,11,12,11,0,13,13,14],
[10,10,9,8,13,0,11,13],
[13,15,14,11,13,15,0,17],
[9,9,12,11,12,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,10,15,17,20,5],
[21,0,5,21,11,21,20,11],
[22,21,0,21,22,22,22,12],
[16,5,5,0,6,16,10,16],
[11,15,4,20,0,21,26,11],
[9,5,4,10,5,0,9,5],
[6,6,4,16,0,17,0,6],
[21,15,14,10,15,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,15,17,14,13,10],
[14,0,14,10,13,15,12,11],
[10,12,0,8,13,13,10,8],
[11,16,18,0,13,18,16,12],
[9,13,13,13,0,15,13,9],
[12,11,13,8,11,0,9,12],
[13,14,16,10,13,17,0,13],
[16,15,18,14,17,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,12,19,17,9,16],
[8,0,6,5,17,8,8,16],
[15,20,0,15,22,9,13,24],
[14,21,11,0,22,13,14,17],
[7,9,4,4,0,6,7,11],
[9,18,17,13,20,0,14,24],
[17,18,13,12,19,12,0,16],
[10,10,2,9,15,2,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,17,14,12,7,14],
[18,0,10,18,24,22,17,21],
[16,16,0,13,17,12,9,17],
[9,8,13,0,18,15,13,15],
[12,2,9,8,0,8,9,5],
[14,4,14,11,18,0,12,10],
[19,9,17,13,17,14,0,14],
[12,5,9,11,21,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,21,16,13,10,11,19],
[8,0,17,10,9,11,13,16],
[5,9,0,8,12,10,12,16],
[10,16,18,0,13,10,11,19],
[13,17,14,13,0,8,18,18],
[16,15,16,16,18,0,13,19],
[15,13,14,15,8,13,0,19],
[7,10,10,7,8,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,11,15,15,13,15],
[14,0,9,10,14,12,10,11],
[15,17,0,13,15,14,14,16],
[15,16,13,0,14,17,15,16],
[11,12,11,12,0,11,10,13],
[11,14,12,9,15,0,15,11],
[13,16,12,11,16,11,0,11],
[11,15,10,10,13,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,0,9,7,8,10,7],
[15,0,2,15,9,15,10,15],
[26,24,0,26,18,17,10,24],
[17,11,0,0,0,8,8,11],
[19,17,8,26,0,10,10,17],
[18,11,9,18,16,0,17,18],
[16,16,16,18,16,9,0,16],
[19,11,2,15,9,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,16,15,14,10,10],
[13,0,17,16,18,17,13,13],
[14,9,0,13,16,14,12,10],
[10,10,13,0,15,15,11,10],
[11,8,10,11,0,12,12,9],
[12,9,12,11,14,0,12,10],
[16,13,14,15,14,14,0,10],
[16,13,16,16,17,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,13,13,11,11,13],
[9,0,8,9,11,8,10,9],
[12,18,0,12,18,13,15,10],
[13,17,14,0,14,10,13,13],
[13,15,8,12,0,10,13,9],
[15,18,13,16,16,0,12,13],
[15,16,11,13,13,14,0,10],
[13,17,16,13,17,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,22,1,4,11,17],
[22,0,13,23,11,15,21,24],
[22,13,0,21,15,11,11,20],
[4,3,5,0,2,5,9,17],
[25,15,11,24,0,11,19,21],
[22,11,15,21,15,0,17,25],
[15,5,15,17,7,9,0,17],
[9,2,6,9,5,1,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,11,10,11,12,6],
[16,0,13,13,13,12,13,10],
[14,13,0,16,12,13,12,14],
[15,13,10,0,15,10,13,10],
[16,13,14,11,0,14,11,13],
[15,14,13,16,12,0,11,9],
[14,13,14,13,15,15,0,12],
[20,16,12,16,13,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,12,12,15,14,15],
[10,0,17,11,9,12,11,11],
[9,9,0,9,10,6,10,12],
[14,15,17,0,11,12,12,15],
[14,17,16,15,0,11,16,17],
[11,14,20,14,15,0,16,14],
[12,15,16,14,10,10,0,17],
[11,15,14,11,9,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,15,15,16,16,13],
[14,0,14,10,14,12,15,14],
[12,12,0,15,16,12,17,16],
[11,16,11,0,13,12,14,14],
[11,12,10,13,0,13,11,15],
[10,14,14,14,13,0,15,16],
[10,11,9,12,15,11,0,16],
[13,12,10,12,11,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,9,8,12,11],
[15,0,18,16,13,11,15,11],
[14,8,0,9,10,12,17,10],
[13,10,17,0,12,14,12,11],
[17,13,16,14,0,13,13,13],
[18,15,14,12,13,0,13,13],
[14,11,9,14,13,13,0,15],
[15,15,16,15,13,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,15,17,12,12,11],
[15,0,19,19,19,13,14,17],
[10,7,0,16,12,13,9,10],
[11,7,10,0,9,12,8,8],
[9,7,14,17,0,9,9,14],
[14,13,13,14,17,0,13,10],
[14,12,17,18,17,13,0,15],
[15,9,16,18,12,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,13,13,13,14,14],
[15,0,15,16,10,8,8,7],
[7,11,0,14,9,9,8,3],
[13,10,12,0,11,8,9,7],
[13,16,17,15,0,10,10,9],
[13,18,17,18,16,0,17,14],
[12,18,18,17,16,9,0,12],
[12,19,23,19,17,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,9,14,10,15,9],
[12,0,12,12,15,11,16,7],
[15,14,0,11,17,10,14,8],
[17,14,15,0,18,13,15,13],
[12,11,9,8,0,5,10,9],
[16,15,16,13,21,0,20,14],
[11,10,12,11,16,6,0,8],
[17,19,18,13,17,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,10,20,15,15,12],
[15,0,7,7,12,12,9,11],
[14,19,0,15,19,20,15,12],
[16,19,11,0,17,15,14,10],
[6,14,7,9,0,8,8,6],
[11,14,6,11,18,0,11,13],
[11,17,11,12,18,15,0,10],
[14,15,14,16,20,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,13,15,11,13,14],
[11,0,11,12,9,12,10,12],
[12,15,0,11,10,9,9,13],
[13,14,15,0,18,18,15,19],
[11,17,16,8,0,11,12,15],
[15,14,17,8,15,0,12,15],
[13,16,17,11,14,14,0,18],
[12,14,13,7,11,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,0,3,14,14,5,5],
[26,0,8,11,22,22,13,13],
[26,18,0,24,18,26,15,5],
[23,15,2,0,15,21,7,2],
[12,4,8,11,0,10,15,2],
[12,4,0,5,16,0,7,5],
[21,13,11,19,11,19,0,2],
[21,13,21,24,24,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,17,13,15,14,13],
[13,0,12,14,12,18,13,8],
[17,14,0,14,16,16,17,13],
[9,12,12,0,10,15,16,8],
[13,14,10,16,0,17,18,9],
[11,8,10,11,9,0,12,5],
[12,13,9,10,8,14,0,5],
[13,18,13,18,17,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,15,14,14,17],
[13,0,7,12,13,10,12,15],
[13,19,0,13,14,18,15,15],
[13,14,13,0,17,14,14,11],
[11,13,12,9,0,11,13,13],
[12,16,8,12,15,0,14,11],
[12,14,11,12,13,12,0,13],
[9,11,11,15,13,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,16,14,18,12,19],
[12,0,12,11,13,10,13,12],
[12,14,0,15,17,17,12,16],
[10,15,11,0,10,12,9,7],
[12,13,9,16,0,16,13,13],
[8,16,9,14,10,0,11,11],
[14,13,14,17,13,15,0,14],
[7,14,10,19,13,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,21,13,13,13,13],
[5,0,19,7,6,11,11,0],
[0,7,0,7,13,8,8,7],
[5,19,19,0,11,6,6,11],
[13,20,13,15,0,13,11,0],
[13,15,18,20,13,0,6,5],
[13,15,18,20,15,20,0,13],
[13,26,19,15,26,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,16,6,5,17,16],
[10,0,17,16,6,11,10,6],
[10,9,0,15,4,4,10,4],
[10,10,11,0,0,11,6,11],
[20,20,22,26,0,11,21,22],
[21,15,22,15,15,0,21,11],
[9,16,16,20,5,5,0,10],
[10,20,22,15,4,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,12,11,8,10,10],
[15,0,11,14,12,12,12,9],
[17,15,0,16,15,14,12,15],
[14,12,10,0,12,10,12,10],
[15,14,11,14,0,8,13,12],
[18,14,12,16,18,0,13,12],
[16,14,14,14,13,13,0,12],
[16,17,11,16,14,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,13,15,13,13,16],
[12,0,12,16,14,14,9,13],
[17,14,0,19,15,12,12,14],
[13,10,7,0,11,10,8,5],
[11,12,11,15,0,13,9,13],
[13,12,14,16,13,0,14,14],
[13,17,14,18,17,12,0,18],
[10,13,12,21,13,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,9,14,7,11],
[16,0,15,14,14,14,11,16],
[15,11,0,14,11,14,12,13],
[16,12,12,0,11,10,10,14],
[17,12,15,15,0,16,13,15],
[12,12,12,16,10,0,9,9],
[19,15,14,16,13,17,0,16],
[15,10,13,12,11,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,23,24,0,10,12,13],
[13,0,10,24,11,11,13,24],
[3,16,0,26,3,13,3,16],
[2,2,0,0,2,12,2,13],
[26,15,23,24,0,13,26,23],
[16,15,13,14,13,0,16,13],
[14,13,23,24,0,10,0,13],
[13,2,10,13,3,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,21,17,18,14],
[12,0,11,12,15,16,9,12],
[13,15,0,15,17,12,15,14],
[11,14,11,0,16,6,9,10],
[5,11,9,10,0,12,10,14],
[9,10,14,20,14,0,16,10],
[8,17,11,17,16,10,0,7],
[12,14,12,16,12,16,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,14,11,14,10,12],
[13,0,3,9,8,11,8,10],
[14,23,0,21,16,17,13,13],
[12,17,5,0,11,8,10,10],
[15,18,10,15,0,15,13,15],
[12,15,9,18,11,0,15,12],
[16,18,13,16,13,11,0,16],
[14,16,13,16,11,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,17,15,17,17,19],
[8,0,8,10,13,12,17,12],
[13,18,0,17,15,15,16,17],
[9,16,9,0,13,16,17,12],
[11,13,11,13,0,12,15,14],
[9,14,11,10,14,0,12,10],
[9,9,10,9,11,14,0,14],
[7,14,9,14,12,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,14,11,15,12,13],
[13,0,7,14,12,16,10,10],
[16,19,0,21,17,23,13,22],
[12,12,5,0,11,14,7,12],
[15,14,9,15,0,19,17,13],
[11,10,3,12,7,0,6,11],
[14,16,13,19,9,20,0,15],
[13,16,4,14,13,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,9,15,11,9,14],
[15,0,15,12,12,13,14,17],
[13,11,0,8,14,12,10,13],
[17,14,18,0,16,13,16,14],
[11,14,12,10,0,14,9,17],
[15,13,14,13,12,0,11,13],
[17,12,16,10,17,15,0,17],
[12,9,13,12,9,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,13,19,18,17,16],
[5,0,19,13,12,11,13,9],
[7,7,0,5,14,11,10,9],
[13,13,21,0,12,19,15,17],
[7,14,12,14,0,18,14,12],
[8,15,15,7,8,0,7,1],
[9,13,16,11,12,19,0,9],
[10,17,17,9,14,25,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,19,18,13,11,8],
[16,0,9,13,16,18,14,3],
[13,17,0,15,19,15,17,12],
[7,13,11,0,6,13,9,13],
[8,10,7,20,0,11,10,11],
[13,8,11,13,15,0,9,2],
[15,12,9,17,16,17,0,6],
[18,23,14,13,15,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,12,16,21,18,20],
[16,0,7,17,11,18,18,15],
[11,19,0,20,19,21,21,21],
[14,9,6,0,17,18,24,14],
[10,15,7,9,0,10,8,9],
[5,8,5,8,16,0,10,8],
[8,8,5,2,18,16,0,15],
[6,11,5,12,17,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,17,13,17,18,22],
[13,0,14,18,12,16,18,19],
[15,12,0,19,13,15,18,18],
[9,8,7,0,10,14,11,15],
[13,14,13,16,0,20,15,15],
[9,10,11,12,6,0,14,15],
[8,8,8,15,11,12,0,15],
[4,7,8,11,11,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,11,10,17,12,15],
[15,0,12,15,8,19,16,15],
[13,14,0,14,7,16,13,11],
[15,11,12,0,13,10,12,18],
[16,18,19,13,0,20,13,12],
[9,7,10,16,6,0,6,15],
[14,10,13,14,13,20,0,14],
[11,11,15,8,14,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,19,10,13,7,16],
[14,0,8,13,17,8,11,12],
[13,18,0,15,15,9,11,14],
[7,13,11,0,11,14,8,10],
[16,9,11,15,0,9,10,12],
[13,18,17,12,17,0,15,13],
[19,15,15,18,16,11,0,17],
[10,14,12,16,14,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,16,13,23,16,13],
[12,0,18,10,7,17,10,18],
[8,8,0,8,2,12,3,8],
[10,16,18,0,8,18,3,13],
[13,19,24,18,0,18,9,21],
[3,9,14,8,8,0,6,14],
[10,16,23,23,17,20,0,18],
[13,8,18,13,5,12,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,14,9,10,10,11],
[14,0,15,13,12,10,6,13],
[11,11,0,12,12,8,8,9],
[12,13,14,0,10,10,9,8],
[17,14,14,16,0,9,13,13],
[16,16,18,16,17,0,12,13],
[16,20,18,17,13,14,0,14],
[15,13,17,18,13,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,24,17,14,23,15,23],
[20,0,26,12,18,19,25,24],
[2,0,0,8,2,11,6,15],
[9,14,18,0,9,9,17,23],
[12,8,24,17,0,13,17,23],
[3,7,15,17,13,0,8,24],
[11,1,20,9,9,18,0,16],
[3,2,11,3,3,2,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,11,11,18,18],
[19,0,17,12,11,17,18,17],
[19,9,0,6,17,18,12,13],
[20,14,20,0,18,12,12,14],
[15,15,9,8,0,16,16,15],
[15,9,8,14,10,0,19,19],
[8,8,14,14,10,7,0,8],
[8,9,13,12,11,7,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,14,13,11,13,10],
[18,0,14,12,15,18,12,8],
[13,12,0,14,11,8,11,8],
[12,14,12,0,14,13,15,11],
[13,11,15,12,0,9,12,9],
[15,8,18,13,17,0,14,14],
[13,14,15,11,14,12,0,11],
[16,18,18,15,17,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,13,18,19,18,15],
[10,0,13,10,15,14,14,13],
[11,13,0,13,16,17,11,14],
[13,16,13,0,15,15,15,12],
[8,11,10,11,0,15,14,10],
[7,12,9,11,11,0,10,11],
[8,12,15,11,12,16,0,11],
[11,13,12,14,16,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,14,14,13,20,15],
[14,0,9,13,10,6,15,8],
[11,17,0,20,6,18,19,15],
[12,13,6,0,9,11,16,15],
[12,16,20,17,0,17,20,18],
[13,20,8,15,9,0,14,16],
[6,11,7,10,6,12,0,10],
[11,18,11,11,8,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,15,10,14,11,14],
[9,0,6,9,13,7,7,7],
[12,20,0,12,15,15,13,14],
[11,17,14,0,19,14,12,15],
[16,13,11,7,0,13,10,10],
[12,19,11,12,13,0,14,9],
[15,19,13,14,16,12,0,15],
[12,19,12,11,16,17,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,14,12,16,8,8],
[15,0,15,16,13,18,13,15],
[13,11,0,12,6,12,11,11],
[12,10,14,0,14,15,14,3],
[14,13,20,12,0,13,16,10],
[10,8,14,11,13,0,16,8],
[18,13,15,12,10,10,0,11],
[18,11,15,23,16,18,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,14,13,12,17,14],
[16,0,19,16,9,9,17,13],
[9,7,0,8,12,8,9,12],
[12,10,18,0,14,14,9,15],
[13,17,14,12,0,16,18,12],
[14,17,18,12,10,0,14,14],
[9,9,17,17,8,12,0,13],
[12,13,14,11,14,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,14,9,13,15,20,17],
[7,0,7,10,4,8,8,13],
[12,19,0,13,9,11,18,15],
[17,16,13,0,12,14,13,16],
[13,22,17,14,0,12,17,17],
[11,18,15,12,14,0,16,22],
[6,18,8,13,9,10,0,18],
[9,13,11,10,9,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,15,17,14,12,16],
[14,0,13,17,14,12,15,18],
[11,13,0,16,14,13,14,16],
[11,9,10,0,15,8,10,11],
[9,12,12,11,0,9,8,16],
[12,14,13,18,17,0,15,17],
[14,11,12,16,18,11,0,15],
[10,8,10,15,10,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,12,12,13,13,13],
[14,0,17,15,12,13,11,10],
[16,9,0,15,9,14,10,10],
[14,11,11,0,7,9,12,10],
[14,14,17,19,0,14,12,15],
[13,13,12,17,12,0,15,14],
[13,15,16,14,14,11,0,9],
[13,16,16,16,11,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,9,10,10,8,12],
[15,0,13,13,11,11,12,15],
[15,13,0,15,14,9,12,14],
[17,13,11,0,13,12,13,14],
[16,15,12,13,0,14,12,12],
[16,15,17,14,12,0,11,13],
[18,14,14,13,14,15,0,13],
[14,11,12,12,14,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,12,9,11,9,12],
[15,0,13,12,9,11,12,15],
[14,13,0,14,12,14,13,14],
[14,14,12,0,9,17,12,11],
[17,17,14,17,0,13,15,17],
[15,15,12,9,13,0,13,10],
[17,14,13,14,11,13,0,13],
[14,11,12,15,9,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,14,17,14,11,15],
[13,0,12,13,11,12,13,11],
[16,14,0,17,14,12,10,14],
[12,13,9,0,12,9,7,10],
[9,15,12,14,0,10,10,11],
[12,14,14,17,16,0,14,12],
[15,13,16,19,16,12,0,16],
[11,15,12,16,15,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,9,25,8,14,12,12],
[8,0,14,25,8,12,13,18],
[17,12,0,19,10,14,19,18],
[1,1,7,0,1,5,6,11],
[18,18,16,25,0,13,18,16],
[12,14,12,21,13,0,20,15],
[14,13,7,20,8,6,0,12],
[14,8,8,15,10,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,13,6,15,18,21],
[15,0,10,10,10,18,17,22],
[17,16,0,11,10,18,17,21],
[13,16,15,0,13,17,18,18],
[20,16,16,13,0,18,19,20],
[11,8,8,9,8,0,14,17],
[8,9,9,8,7,12,0,12],
[5,4,5,8,6,9,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,13,11,14,13,11],
[16,0,19,16,14,13,15,15],
[8,7,0,10,11,12,11,8],
[13,10,16,0,11,13,12,14],
[15,12,15,15,0,13,13,14],
[12,13,14,13,13,0,12,10],
[13,11,15,14,13,14,0,11],
[15,11,18,12,12,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,8,16,14,9,15],
[8,0,11,5,10,12,5,11],
[16,15,0,15,14,16,12,17],
[18,21,11,0,16,17,15,15],
[10,16,12,10,0,12,9,13],
[12,14,10,9,14,0,11,10],
[17,21,14,11,17,15,0,18],
[11,15,9,11,13,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,13,9,11,12,11],
[10,0,12,13,10,15,14,10],
[14,14,0,13,10,12,13,11],
[13,13,13,0,8,13,15,9],
[17,16,16,18,0,17,15,13],
[15,11,14,13,9,0,13,8],
[14,12,13,11,11,13,0,9],
[15,16,15,17,13,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,12,6,14,7,8],
[15,0,15,15,12,18,13,13],
[15,11,0,14,8,13,7,6],
[14,11,12,0,7,13,5,8],
[20,14,18,19,0,12,9,9],
[12,8,13,13,14,0,7,5],
[19,13,19,21,17,19,0,14],
[18,13,20,18,17,21,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,15,14,17,17,13],
[15,0,15,15,11,21,19,13],
[14,11,0,16,11,13,21,9],
[11,11,10,0,10,15,16,13],
[12,15,15,16,0,19,26,8],
[9,5,13,11,7,0,12,10],
[9,7,5,10,0,14,0,7],
[13,13,17,13,18,16,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,12,11,14,11,12],
[12,0,12,11,13,15,16,13],
[14,14,0,11,14,13,14,11],
[14,15,15,0,14,17,14,13],
[15,13,12,12,0,17,14,13],
[12,11,13,9,9,0,15,14],
[15,10,12,12,12,11,0,10],
[14,13,15,13,13,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,13,18,16,19,17],
[12,0,11,10,15,12,16,15],
[11,15,0,14,16,15,19,15],
[13,16,12,0,14,14,18,16],
[8,11,10,12,0,10,16,13],
[10,14,11,12,16,0,17,15],
[7,10,7,8,10,9,0,9],
[9,11,11,10,13,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,17,17,12,16,13],
[10,0,18,12,17,15,14,14],
[9,8,0,9,12,9,11,6],
[9,14,17,0,16,11,17,12],
[9,9,14,10,0,9,14,10],
[14,11,17,15,17,0,14,14],
[10,12,15,9,12,12,0,10],
[13,12,20,14,16,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,11,12,16,14,15],
[12,0,14,12,12,15,13,11],
[15,12,0,12,14,14,13,16],
[15,14,14,0,9,13,10,12],
[14,14,12,17,0,11,9,14],
[10,11,12,13,15,0,15,17],
[12,13,13,16,17,11,0,9],
[11,15,10,14,12,9,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,15,15,12,15,13],
[15,0,15,13,14,16,12,16],
[11,11,0,15,14,17,14,14],
[11,13,11,0,16,12,13,12],
[11,12,12,10,0,13,12,13],
[14,10,9,14,13,0,13,9],
[11,14,12,13,14,13,0,11],
[13,10,12,14,13,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,17,13,14,20,10],
[14,0,9,14,12,14,19,10],
[9,17,0,13,8,13,13,10],
[9,12,13,0,13,13,19,14],
[13,14,18,13,0,14,19,10],
[12,12,13,13,12,0,17,9],
[6,7,13,7,7,9,0,7],
[16,16,16,12,16,17,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,10,11,17,12,19],
[14,0,15,12,16,16,14,20],
[10,11,0,10,15,15,14,13],
[16,14,16,0,13,19,16,19],
[15,10,11,13,0,12,14,15],
[9,10,11,7,14,0,14,16],
[14,12,12,10,12,12,0,14],
[7,6,13,7,11,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,14,10,14,10,13],
[18,0,21,15,13,12,11,10],
[12,5,0,15,6,11,10,13],
[12,11,11,0,16,17,16,15],
[16,13,20,10,0,14,14,16],
[12,14,15,9,12,0,16,11],
[16,15,16,10,12,10,0,19],
[13,16,13,11,10,15,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,19,13,25,19,22],
[8,0,5,8,12,12,14,15],
[11,21,0,14,9,15,14,15],
[7,18,12,0,11,16,15,16],
[13,14,17,15,0,16,18,22],
[1,14,11,10,10,0,15,12],
[7,12,12,11,8,11,0,17],
[4,11,11,10,4,14,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,12,8,14,16,13],
[13,0,16,10,8,12,10,10],
[8,10,0,10,6,5,12,8],
[14,16,16,0,14,14,16,12],
[18,18,20,12,0,13,15,14],
[12,14,21,12,13,0,13,12],
[10,16,14,10,11,13,0,14],
[13,16,18,14,12,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,17,16,7,14,9],
[14,0,15,19,15,14,16,10],
[14,11,0,17,13,11,13,14],
[9,7,9,0,11,9,13,9],
[10,11,13,15,0,5,15,12],
[19,12,15,17,21,0,17,11],
[12,10,13,13,11,9,0,12],
[17,16,12,17,14,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,15,20,12,15,14],
[14,0,14,14,14,16,11,11],
[8,12,0,7,11,7,6,10],
[11,12,19,0,17,10,12,20],
[6,12,15,9,0,7,6,11],
[14,10,19,16,19,0,15,15],
[11,15,20,14,20,11,0,20],
[12,15,16,6,15,11,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,19,15,12,18,14,9],
[16,0,19,21,15,22,13,12],
[7,7,0,13,10,12,7,7],
[11,5,13,0,9,17,8,6],
[14,11,16,17,0,17,11,11],
[8,4,14,9,9,0,8,5],
[12,13,19,18,15,18,0,13],
[17,14,19,20,15,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,16,12,14,11],
[14,0,13,11,15,13,13,14],
[12,13,0,10,15,14,14,13],
[12,15,16,0,16,13,14,15],
[10,11,11,10,0,10,10,15],
[14,13,12,13,16,0,18,16],
[12,13,12,12,16,8,0,15],
[15,12,13,11,11,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,19,19,19,21,13,24],
[8,0,19,17,10,17,8,13],
[7,7,0,8,10,10,8,10],
[7,9,18,0,12,10,10,15],
[7,16,16,14,0,16,11,8],
[5,9,16,16,10,0,10,10],
[13,18,18,16,15,16,0,16],
[2,13,16,11,18,16,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,16,14,18,14,16],
[13,0,12,11,9,11,7,12],
[11,14,0,12,13,14,13,13],
[10,15,14,0,12,12,13,12],
[12,17,13,14,0,9,12,12],
[8,15,12,14,17,0,13,14],
[12,19,13,13,14,13,0,14],
[10,14,13,14,14,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,14,16,18,15,16],
[19,0,13,17,20,18,16,20],
[14,13,0,20,18,18,11,17],
[12,9,6,0,20,17,11,12],
[10,6,8,6,0,9,10,8],
[8,8,8,9,17,0,9,10],
[11,10,15,15,16,17,0,16],
[10,6,9,14,18,16,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,6,6,11,9,10],
[17,0,9,10,10,9,6,12],
[17,17,0,13,17,12,9,13],
[20,16,13,0,13,13,11,14],
[20,16,9,13,0,17,8,13],
[15,17,14,13,9,0,16,19],
[17,20,17,15,18,10,0,23],
[16,14,13,12,13,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,10,18,16,15,18],
[13,0,16,15,17,20,16,19],
[8,10,0,12,19,14,16,17],
[16,11,14,0,16,13,20,16],
[8,9,7,10,0,13,12,11],
[10,6,12,13,13,0,14,16],
[11,10,10,6,14,12,0,8],
[8,7,9,10,15,10,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,12,15,12,13,12],
[11,0,12,15,14,14,12,12],
[13,14,0,16,14,14,10,14],
[14,11,10,0,13,15,10,12],
[11,12,12,13,0,11,11,10],
[14,12,12,11,15,0,11,11],
[13,14,16,16,15,15,0,13],
[14,14,12,14,16,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,18,16,20,21,11],
[3,0,6,7,12,6,6,14],
[5,20,0,15,21,11,19,11],
[8,19,11,0,17,11,16,11],
[10,14,5,9,0,10,5,11],
[6,20,15,15,16,0,11,8],
[5,20,7,10,21,15,0,11],
[15,12,15,15,15,18,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,14,21,17,13,17,14],
[7,0,11,11,16,15,12,3],
[12,15,0,14,15,15,16,6],
[5,15,12,0,12,14,15,3],
[9,10,11,14,0,10,14,2],
[13,11,11,12,16,0,13,10],
[9,14,10,11,12,13,0,9],
[12,23,20,23,24,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,9,11,8,11,13],
[16,0,20,16,13,21,20,16],
[13,6,0,9,12,11,14,15],
[17,10,17,0,13,14,21,13],
[15,13,14,13,0,19,17,11],
[18,5,15,12,7,0,16,16],
[15,6,12,5,9,10,0,14],
[13,10,11,13,15,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,16,21,15,21,14],
[11,0,16,14,17,10,18,11],
[15,10,0,12,21,16,20,16],
[10,12,14,0,18,13,18,14],
[5,9,5,8,0,9,16,12],
[11,16,10,13,17,0,19,18],
[5,8,6,8,10,7,0,5],
[12,15,10,12,14,8,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,12,16,13,14,13],
[15,0,14,17,14,13,12,17],
[12,12,0,18,14,11,12,15],
[14,9,8,0,15,10,11,16],
[10,12,12,11,0,10,12,12],
[13,13,15,16,16,0,13,20],
[12,14,14,15,14,13,0,14],
[13,9,11,10,14,6,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,10,12,11,13,17],
[11,0,15,8,14,12,14,13],
[13,11,0,13,17,13,18,18],
[16,18,13,0,13,11,15,18],
[14,12,9,13,0,13,11,14],
[15,14,13,15,13,0,14,19],
[13,12,8,11,15,12,0,13],
[9,13,8,8,12,7,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,15,12,16,12,15],
[11,0,12,13,12,13,11,16],
[12,14,0,14,15,15,15,14],
[11,13,12,0,12,15,15,14],
[14,14,11,14,0,14,12,15],
[10,13,11,11,12,0,14,15],
[14,15,11,11,14,12,0,13],
[11,10,12,12,11,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,11,11,10,12,13],
[13,0,13,12,6,11,11,9],
[11,13,0,12,11,13,12,13],
[15,14,14,0,14,13,18,12],
[15,20,15,12,0,10,13,11],
[16,15,13,13,16,0,12,10],
[14,15,14,8,13,14,0,15],
[13,17,13,14,15,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,14,7,12,18],
[13,0,24,5,12,12,12,18],
[13,2,0,7,12,13,12,12],
[13,21,19,0,12,12,12,18],
[12,14,14,14,0,8,11,17],
[19,14,13,14,18,0,12,11],
[14,14,14,14,15,14,0,8],
[8,8,14,8,9,15,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,10,11,12,9,11],
[14,0,20,12,9,14,10,15],
[7,6,0,2,3,7,9,9],
[16,14,24,0,8,12,10,15],
[15,17,23,18,0,14,10,18],
[14,12,19,14,12,0,15,14],
[17,16,17,16,16,11,0,15],
[15,11,17,11,8,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,16,8,16,13,13],
[17,0,8,15,12,20,21,17],
[18,18,0,15,13,16,19,21],
[10,11,11,0,16,20,14,13],
[18,14,13,10,0,19,20,16],
[10,6,10,6,7,0,13,10],
[13,5,7,12,6,13,0,17],
[13,9,5,13,10,16,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,13,14,18,13,17],
[12,0,13,9,16,21,13,16],
[13,13,0,17,14,16,13,16],
[13,17,9,0,13,16,14,17],
[12,10,12,13,0,15,11,14],
[8,5,10,10,11,0,8,14],
[13,13,13,12,15,18,0,15],
[9,10,10,9,12,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,11,11,14,13,13],
[12,0,12,11,13,13,13,15],
[17,14,0,12,12,15,13,15],
[15,15,14,0,12,15,13,12],
[15,13,14,14,0,13,13,11],
[12,13,11,11,13,0,14,13],
[13,13,13,13,13,12,0,15],
[13,11,11,14,15,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,20,23,13,17,15],
[19,0,5,20,23,13,19,14],
[19,21,0,19,23,13,21,14],
[6,6,7,0,6,3,6,14],
[3,3,3,20,0,13,13,11],
[13,13,13,23,13,0,13,14],
[9,7,5,20,13,13,0,15],
[11,12,12,12,15,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,20,17,9,12,16,11],
[11,0,15,15,13,10,8,12],
[6,11,0,11,3,10,7,10],
[9,11,15,0,9,13,8,10],
[17,13,23,17,0,16,14,14],
[14,16,16,13,10,0,11,11],
[10,18,19,18,12,15,0,16],
[15,14,16,16,12,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,16,0,11,17,11],
[9,0,9,15,9,9,9,8],
[8,17,0,11,1,12,17,12],
[10,11,15,0,9,14,19,6],
[26,17,25,17,0,17,25,13],
[15,17,14,12,9,0,18,13],
[9,17,9,7,1,8,0,12],
[15,18,14,20,13,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,19,21,11,20,16,16],
[9,0,13,10,11,13,17,17],
[7,13,0,14,11,14,15,15],
[5,16,12,0,13,13,12,14],
[15,15,15,13,0,13,14,17],
[6,13,12,13,13,0,11,11],
[10,9,11,14,12,15,0,13],
[10,9,11,12,9,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,14,12,16,18,15],
[13,0,18,15,17,13,18,16],
[10,8,0,13,15,10,14,16],
[12,11,13,0,14,12,15,14],
[14,9,11,12,0,11,12,13],
[10,13,16,14,15,0,14,13],
[8,8,12,11,14,12,0,15],
[11,10,10,12,13,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,19,12,19,22,16,18],
[9,0,17,14,19,22,14,19],
[7,9,0,12,12,14,11,15],
[14,12,14,0,16,20,15,19],
[7,7,14,10,0,19,10,16],
[4,4,12,6,7,0,8,14],
[10,12,15,11,16,18,0,16],
[8,7,11,7,10,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,12,13,12,8,12],
[14,0,15,13,18,14,13,13],
[12,11,0,9,8,13,9,7],
[14,13,17,0,15,14,10,10],
[13,8,18,11,0,10,12,10],
[14,12,13,12,16,0,13,11],
[18,13,17,16,14,13,0,11],
[14,13,19,16,16,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,16,15,15,14,15],
[18,0,14,13,12,14,12,16],
[15,12,0,15,15,18,15,18],
[10,13,11,0,14,14,10,15],
[11,14,11,12,0,18,13,15],
[11,12,8,12,8,0,14,13],
[12,14,11,16,13,12,0,16],
[11,10,8,11,11,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,17,18,15,16,13],
[13,0,14,11,14,16,14,16],
[14,12,0,15,15,13,11,16],
[9,15,11,0,15,18,13,17],
[8,12,11,11,0,15,11,15],
[11,10,13,8,11,0,12,15],
[10,12,15,13,15,14,0,16],
[13,10,10,9,11,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,8,13,11,14,14],
[15,0,17,11,9,14,13,16],
[10,9,0,6,8,11,10,13],
[18,15,20,0,15,12,17,21],
[13,17,18,11,0,14,14,14],
[15,12,15,14,12,0,12,12],
[12,13,16,9,12,14,0,13],
[12,10,13,5,12,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,7,9,6,5,8],
[14,0,6,7,12,8,9,8],
[19,20,0,9,14,6,13,7],
[19,19,17,0,14,10,14,13],
[17,14,12,12,0,7,12,10],
[20,18,20,16,19,0,16,10],
[21,17,13,12,14,10,0,10],
[18,18,19,13,16,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,6,9,12,14,11],
[16,0,12,8,12,14,18,13],
[19,14,0,14,16,11,19,18],
[20,18,12,0,17,16,14,14],
[17,14,10,9,0,17,14,18],
[14,12,15,10,9,0,13,13],
[12,8,7,12,12,13,0,12],
[15,13,8,12,8,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,5,1,9,5,9],
[15,0,16,13,9,11,11,10],
[17,10,0,11,14,9,14,11],
[21,13,15,0,14,19,16,16],
[25,17,12,12,0,17,20,16],
[17,15,17,7,9,0,10,12],
[21,15,12,10,6,16,0,12],
[17,16,15,10,10,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,5,9,5,11,9],
[14,0,13,11,12,11,14,12],
[14,13,0,14,10,14,13,15],
[21,15,12,0,10,13,14,15],
[17,14,16,16,0,12,14,15],
[21,15,12,13,14,0,20,11],
[15,12,13,12,12,6,0,9],
[17,14,11,11,11,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,7,13,17,13,22,17],
[11,0,13,20,12,18,20,14],
[19,13,0,15,19,13,23,13],
[13,6,11,0,15,21,21,15],
[9,14,7,11,0,10,15,12],
[13,8,13,5,16,0,17,14],
[4,6,3,5,11,9,0,5],
[9,12,13,11,14,12,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,14,12,17,14,17],
[17,0,18,15,13,18,19,13],
[12,8,0,13,11,13,16,14],
[12,11,13,0,13,17,14,14],
[14,13,15,13,0,17,13,13],
[9,8,13,9,9,0,17,13],
[12,7,10,12,13,9,0,13],
[9,13,12,12,13,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,11,11,10,12,11],
[17,0,19,15,14,14,15,13],
[12,7,0,13,9,9,12,7],
[15,11,13,0,11,12,11,11],
[15,12,17,15,0,13,10,14],
[16,12,17,14,13,0,12,12],
[14,11,14,15,16,14,0,12],
[15,13,19,15,12,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,15,16,11,14,14],
[11,0,14,13,15,13,16,14],
[12,12,0,13,13,17,13,13],
[11,13,13,0,9,8,12,16],
[10,11,13,17,0,12,16,16],
[15,13,9,18,14,0,17,14],
[12,10,13,14,10,9,0,15],
[12,12,13,10,10,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,14,9,15,19,11],
[13,0,13,14,14,14,17,13],
[8,13,0,8,7,12,13,7],
[12,12,18,0,7,9,15,10],
[17,12,19,19,0,10,21,16],
[11,12,14,17,16,0,17,14],
[7,9,13,11,5,9,0,5],
[15,13,19,16,10,12,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,8,20,12,17,17],
[8,0,11,12,14,13,11,15],
[10,15,0,14,15,12,11,17],
[18,14,12,0,22,13,18,15],
[6,12,11,4,0,8,7,13],
[14,13,14,13,18,0,17,19],
[9,15,15,8,19,9,0,14],
[9,11,9,11,13,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,13,12,10,12],
[15,0,12,18,13,14,9,15],
[14,14,0,19,10,13,13,13],
[13,8,7,0,8,10,9,11],
[13,13,16,18,0,15,13,11],
[14,12,13,16,11,0,12,13],
[16,17,13,17,13,14,0,14],
[14,11,13,15,15,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,13,11,11,9,10],
[17,0,13,12,15,16,17,16],
[16,13,0,10,18,13,15,18],
[13,14,16,0,12,15,17,16],
[15,11,8,14,0,10,12,11],
[15,10,13,11,16,0,15,14],
[17,9,11,9,14,11,0,15],
[16,10,8,10,15,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,15,14,17,12,22],
[8,0,9,15,13,10,13,20],
[6,17,0,15,20,8,14,14],
[11,11,11,0,14,7,10,17],
[12,13,6,12,0,8,13,16],
[9,16,18,19,18,0,15,22],
[14,13,12,16,13,11,0,13],
[4,6,12,9,10,4,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 26, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_8_26.csv", index=False, header=False)