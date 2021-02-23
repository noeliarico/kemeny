
import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda1 as am1
import kemeny.azzinimunda.azzinimunda1rec as am1rec

rep = 3
results8 = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,3,5,5,5,6,4,2],
[7,0,8,5,7,6,7,4],
[5,2,0,4,5,5,6,5],
[5,5,6,0,5,5,6,2],
[5,3,5,5,0,4,5,5],
[4,4,5,5,6,0,5,3],
[6,3,4,4,5,5,0,4],
[8,6,5,8,5,7,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,3,4,4,6,6,4,4],
[7,0,5,8,8,8,8,8],
[6,5,0,8,6,5,6,7],
[6,2,2,0,4,5,4,5],
[4,2,4,6,0,6,5,6],
[4,2,5,5,4,0,3,4],
[6,2,4,6,5,7,0,4],
[6,2,3,5,4,6,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,9,7,5,2,9,9,8],
[1,0,5,5,3,6,4,6],
[3,5,0,3,5,3,5,4],
[5,5,7,0,2,5,7,3],
[8,7,5,8,0,7,7,8],
[1,4,7,5,3,0,6,4],
[1,6,5,3,3,4,0,4],
[2,4,6,7,2,6,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,3,5,5,0,6,3],
[3,0,0,5,5,0,6,3],
[7,10,0,8,10,5,6,8],
[5,5,2,0,5,0,6,3],
[5,5,0,5,0,2,6,5],
[10,10,5,10,8,0,8,7],
[4,4,4,4,4,2,0,7],
[7,7,2,7,5,3,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,4,4,5,3,5,5],
[3,0,2,5,6,3,7,3],
[6,8,0,6,7,5,6,6],
[6,5,4,0,6,2,5,4],
[5,4,3,4,0,2,5,5],
[7,7,5,8,8,0,7,7],
[5,3,4,5,5,3,0,6],
[5,7,4,6,5,3,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,2,3,6,6,4,5,7],
[8,0,5,7,7,6,7,9],
[7,5,0,6,6,4,6,8],
[4,3,4,0,7,2,7,7],
[4,3,4,3,0,3,4,4],
[6,4,6,8,7,0,7,6],
[5,3,4,3,6,3,0,6],
[3,1,2,3,6,4,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,6,4,4,4,4,6,6],
[4,0,6,7,3,6,8,5],
[6,4,0,5,3,8,6,7],
[6,3,5,0,0,4,5,4],
[6,7,7,10,0,6,5,9],
[6,4,2,6,4,0,4,8],
[4,2,4,5,5,6,0,7],
[4,5,3,6,1,2,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,3,4,4,3,4,4],
[3,0,5,6,3,5,6,3],
[7,5,0,6,3,8,4,6],
[6,4,4,0,0,4,4,2],
[6,7,7,10,0,7,4,8],
[7,5,2,6,3,0,3,7],
[6,4,6,6,6,7,0,6],
[6,7,4,8,2,3,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,9,8,7,1,5,8],
[3,0,6,6,4,1,3,6],
[1,4,0,3,2,1,2,3],
[2,4,7,0,8,1,4,8],
[3,6,8,2,0,1,5,8],
[9,9,9,9,9,0,5,9],
[5,7,8,6,5,5,0,6],
[2,4,7,2,2,1,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,8,8,3,7,7,8,8],
[2,0,4,2,7,5,4,7],
[2,6,0,5,8,5,7,7],
[7,8,5,0,7,8,8,8],
[3,3,2,3,0,3,2,7],
[3,5,5,2,7,0,4,5],
[2,6,3,2,8,6,0,7],
[2,3,3,2,3,5,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 3, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,4,5,6,4,6,7],
[3,0,3,1,6,5,6,6],
[6,7,0,6,5,6,9,6],
[5,9,4,0,8,5,5,6],
[4,4,5,2,0,4,7,6],
[6,5,4,5,6,0,7,7],
[4,4,1,5,3,3,0,2],
[3,4,4,4,4,3,8,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,3,5,7,6,5,6,8],
[7,0,6,6,5,6,6,8],
[5,4,0,5,4,4,4,7],
[3,4,5,0,6,3,7,6],
[4,5,6,4,0,5,5,6],
[5,4,6,7,5,0,7,5],
[4,4,6,3,5,3,0,6],
[2,2,3,4,4,5,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,2,4,5,6,4,5,6],
[8,0,5,7,7,5,7,9],
[6,5,0,5,6,3,5,7],
[5,3,5,0,7,2,7,7],
[4,3,4,3,0,3,4,4],
[6,5,7,8,7,0,7,6],
[5,3,5,3,6,3,0,5],
[4,1,3,3,6,4,5,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,6,4,5,4,3,4,2],
[4,0,6,5,6,5,2,3],
[6,4,0,5,1,4,1,3],
[5,5,5,0,2,2,2,3],
[6,4,9,8,0,4,4,5],
[7,5,6,8,6,0,4,5],
[6,8,9,8,6,6,0,4],
[8,7,7,7,5,5,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,6,4,6,4,3,4,2],
[4,0,5,5,5,4,3,4],
[6,5,0,6,2,4,2,4],
[4,5,4,0,2,2,2,3],
[6,5,8,8,0,4,5,6],
[7,6,6,8,6,0,5,6],
[6,7,8,8,5,5,0,5],
[8,6,6,7,4,4,5,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 4, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,8,6,5,10,6,6,8],
[2,0,4,2,8,7,8,8],
[4,6,0,4,6,4,9,6],
[5,8,6,0,10,6,6,8],
[0,2,4,0,0,2,6,5],
[4,3,6,4,8,0,8,8],
[4,2,1,4,4,2,0,2],
[2,2,4,2,5,2,8,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,5,6,7,5,6,7],
[3,0,4,3,5,6,7,7],
[5,6,0,5,5,5,9,5],
[4,7,5,0,7,6,6,7],
[3,5,5,3,0,5,7,6],
[5,4,5,4,5,0,7,5],
[4,3,1,4,3,3,0,2],
[3,3,5,3,4,5,8,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,6,9,5,7,8,3,5],
[4,0,7,5,7,8,5,5],
[1,3,0,3,7,4,3,3],
[5,5,7,0,5,8,3,5],
[3,3,3,5,0,6,3,4],
[2,2,6,2,4,0,1,0],
[7,5,7,7,7,9,0,9],
[5,5,7,5,6,10,1,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,8,5,8,5,4,4],
[3,0,7,4,7,5,3,4],
[2,3,0,4,7,3,3,4],
[5,6,6,0,7,6,5,5],
[2,3,3,3,0,4,2,4],
[5,5,7,4,6,0,4,4],
[6,7,7,5,8,6,0,7],
[6,6,6,5,6,6,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,3,4,5,3,4,2,8],
[7,0,6,6,4,6,5,10],
[6,4,0,5,3,3,2,9],
[5,4,5,0,7,4,5,7],
[7,6,7,3,0,4,4,8],
[6,4,7,6,6,0,5,6],
[8,5,8,5,6,5,0,8],
[2,0,1,3,2,4,2,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 5, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,8,7,5,8,7,5,5],
[2,0,4,5,8,7,5,5],
[3,6,0,5,8,5,5,5],
[5,5,5,0,3,8,6,5],
[2,2,2,7,0,7,5,5],
[3,3,5,2,3,0,3,0],
[5,5,5,4,5,7,0,7],
[5,5,5,5,5,10,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,9,7,5,7,8,5,5],
[1,0,5,5,7,8,5,5],
[3,5,0,5,7,7,5,5],
[5,5,5,0,4,8,5,5],
[3,3,3,6,0,8,4,6],
[2,2,3,2,2,0,3,0],
[5,5,5,5,6,7,0,7],
[5,5,5,5,4,10,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,6,6,6,4,6,4],
[3,0,7,5,7,5,3,5],
[4,3,0,5,2,4,1,3],
[4,5,5,0,3,3,2,4],
[4,3,8,7,0,4,5,5],
[6,5,6,7,6,0,5,5],
[4,7,9,8,5,5,0,5],
[6,5,7,6,5,5,5,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,7,7,3,7,3,7,7],
[3,0,4,3,7,6,4,10],
[3,6,0,6,6,6,7,10],
[7,7,4,0,7,7,7,7],
[3,3,4,3,0,3,4,10],
[7,4,4,3,7,0,4,7],
[3,6,3,3,6,6,0,10],
[3,0,0,3,0,3,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,5,7,4,6,6,4,5],
[5,0,7,6,3,5,6,7],
[3,3,0,3,3,1,1,4],
[6,4,7,0,5,4,6,7],
[4,7,7,5,0,7,5,5],
[4,5,9,6,3,0,6,7],
[6,4,9,4,5,4,0,7],
[5,3,6,3,5,3,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 6, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,6,3,4,5,6,6,5],
[4,0,5,4,7,5,7,4],
[7,5,0,4,4,5,6,5],
[6,6,6,0,4,4,7,5],
[5,3,6,6,0,6,4,6],
[4,5,5,6,4,0,6,6],
[4,3,4,3,6,4,0,4],
[5,6,5,5,4,4,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 1, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,5,5,6,7,7,5,3],
[5,0,7,6,5,4,3,5],
[5,3,0,2,3,4,3,2],
[4,4,8,0,4,5,6,7],
[3,5,7,6,0,6,7,5],
[3,6,6,5,4,0,7,4],
[5,7,7,4,3,3,0,6],
[7,5,8,3,5,6,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 2, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,10,5,5,5,5,5,5],
[0,0,0,0,0,0,0,0],
[5,10,0,5,0,5,5,5],
[5,10,5,0,0,5,5,5],
[5,10,10,10,0,5,5,10],
[5,10,5,5,5,0,5,5],
[5,10,5,5,5,5,0,5],
[5,10,5,5,0,5,5,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 3, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,10,5,5,5,5,5,5],
[0,0,5,5,5,0,0,0],
[5,5,0,5,5,5,5,5],
[5,5,5,0,5,5,5,5],
[5,5,5,5,0,5,5,5],
[5,10,5,5,5,0,5,0],
[5,10,5,5,5,5,0,5],
[5,10,5,5,5,10,5,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 4, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

##############################################################
om = np.array([
[0,4,4,5,7,4,6,6],
[6,0,4,3,4,6,6,8],
[6,6,0,4,5,3,5,7],
[5,7,6,0,5,5,6,6],
[3,6,5,5,0,7,4,5],
[6,4,7,5,3,0,5,8],
[4,4,5,4,6,5,0,7],
[4,2,3,4,5,2,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 5, 0, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 7, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results8 = np.vstack((results8, result))

 
pd.DataFrame(results8).to_csv("cwsinyconrec8nc_azzini.csv")