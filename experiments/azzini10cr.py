
import pandas as pd
import numpy as np
from kemeny.scf.borda import *
from kemeny.scf.condorcet import *
import kemeny.scf.distance as dist
import kemeny.scf.initialization as init
import kemeny.azzinimunda.azzinimunda0 as am0
import kemeny.azzinimunda.azzinimunda1 as am1
import kemeny.azzinimunda.azzinimunda2 as am2
import kemeny.azzinimunda.azzinimunda3 as am3
import time


rep = 3
results10 = np.zeros(0).reshape(0,8+rep)

##############################################################
om = np.array([
[0,6,4,6,6,6,0,4,6,6],
[4,0,4,6,10,4,4,4,4,4],
[6,6,0,6,6,6,0,0,6,6],
[4,4,4,0,10,4,4,4,4,4],
[4,0,4,0,0,4,0,4,4,4],
[4,6,4,6,6,0,0,4,10,4],
[10,6,10,6,10,10,0,10,10,10],
[6,6,10,6,6,6,0,0,6,6],
[4,6,4,6,6,0,0,4,0,4],
[4,6,4,6,6,6,0,4,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,6,6,0,6,10,6,0,4],
[4,0,6,0,0,4,4,0,0,4],
[4,4,0,4,4,4,4,4,4,4],
[4,10,6,0,0,10,4,6,0,4],
[10,10,6,10,0,10,10,10,10,10],
[4,6,6,0,0,0,4,0,0,4],
[0,6,6,6,0,6,0,6,0,4],
[4,10,6,4,0,10,4,0,0,4],
[10,10,6,10,0,10,10,10,0,10],
[6,6,6,6,0,6,6,6,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,4,4,4,4,4,4,4,6,6],
[6,0,0,6,6,6,0,6,6,6],
[6,10,0,6,6,6,10,6,6,6],
[6,4,4,0,0,0,4,4,6,6],
[6,4,4,10,0,0,4,4,6,6],
[6,4,4,10,10,0,4,10,6,6],
[6,10,0,6,6,6,0,6,6,6],
[6,4,4,6,6,0,4,0,6,6],
[4,4,4,4,4,4,4,4,0,10],
[4,4,4,4,4,4,4,4,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,4,4,4,4,4,4,4,4,4],
[6,0,0,0,6,10,6,6,0,10],
[6,10,0,4,10,10,10,10,10,10],
[6,10,6,0,10,10,10,10,10,10],
[6,4,0,0,0,4,6,6,0,10],
[6,0,0,0,6,0,6,6,0,6],
[6,4,0,0,4,4,0,6,0,10],
[6,4,0,0,4,4,4,0,0,4],
[6,10,0,0,10,10,10,10,0,10],
[6,0,0,0,0,4,0,6,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,0,6,0,0,0,0,4,4,4],
[10,0,10,10,10,0,10,10,4,10],
[4,0,0,4,4,0,4,4,4,4],
[10,0,6,0,6,0,10,4,4,4],
[10,0,6,4,0,0,4,4,4,4],
[10,10,10,10,10,0,10,10,10,10],
[10,0,6,0,6,0,0,4,4,4],
[6,0,6,6,6,0,6,0,4,4],
[6,6,6,6,6,0,6,6,0,10],
[6,0,6,6,6,0,6,6,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,7,0,7,9,3,6,6,3,0],
[3,0,3,8,2,2,9,9,4,2],
[10,7,0,7,9,3,7,7,4,0],
[3,2,3,0,4,4,3,9,4,3],
[1,8,1,6,0,3,7,7,4,0],
[7,8,7,6,7,0,7,7,10,0],
[4,1,3,7,3,3,0,7,3,0],
[4,1,3,1,3,3,3,0,4,2],
[7,6,6,6,6,0,7,6,0,0],
[10,8,10,7,10,10,10,8,10,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,4,10,10,10,10,10,10,10,10],
[6,0,10,10,10,10,10,10,10,10],
[0,0,0,4,4,0,0,4,6,0],
[0,0,6,0,6,6,6,6,6,6],
[0,0,6,4,0,6,0,0,6,6],
[0,0,10,4,4,0,4,4,6,6],
[0,0,10,4,10,6,0,4,6,6],
[0,0,6,4,10,6,6,0,6,6],
[0,0,4,4,4,4,4,4,0,4],
[0,0,10,4,4,4,4,4,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 3, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,10,7,10,10,7,10,7,7],
[0,0,10,0,10,10,7,10,7,7],
[0,0,0,0,10,7,7,0,0,7],
[3,10,10,0,10,10,10,10,10,10],
[0,0,0,0,0,7,0,0,0,0],
[0,0,3,0,3,0,0,3,0,0],
[3,3,3,0,10,10,0,3,0,7],
[0,0,10,0,10,7,7,0,0,7],
[3,3,10,0,10,10,10,10,0,7],
[3,3,3,0,10,10,3,3,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,1,6,7,1,0,7,7,0,9],
[9,0,9,10,10,9,10,10,3,9],
[4,1,0,4,1,4,1,4,0,3],
[3,0,6,0,0,3,1,4,0,3],
[9,0,9,10,0,3,10,10,3,9],
[10,1,6,7,7,0,7,10,0,9],
[3,0,9,9,0,3,0,9,0,9],
[3,0,6,6,0,0,1,0,0,9],
[10,7,10,10,7,10,10,10,0,9],
[1,1,7,7,1,1,1,1,1,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,6,10,10,10,10,10,10,10],
[0,0,0,0,0,0,0,4,0,4],
[4,10,0,10,10,10,10,10,10,10],
[0,10,0,0,6,0,6,10,4,4],
[0,10,0,4,0,4,6,10,4,4],
[0,10,0,10,6,0,6,10,10,4],
[0,10,0,4,4,4,0,4,4,4],
[0,6,0,0,0,0,6,0,0,0],
[0,10,0,6,6,0,6,10,0,4],
[0,6,0,6,6,6,6,10,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,10,6,10,6,6,6,6,6],
[4,0,4,0,4,4,0,10,10,4],
[0,6,0,0,6,6,0,6,6,6],
[4,10,10,0,10,10,4,10,10,10],
[0,6,4,0,0,0,0,6,6,6],
[4,6,4,0,10,0,0,10,10,6],
[4,10,10,6,10,10,0,10,10,10],
[4,0,4,0,4,0,0,0,6,0],
[4,0,4,0,4,0,0,4,0,0],
[4,6,4,0,4,4,0,10,10,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,6,0,6,0,6,6,6,6],
[4,0,10,4,10,4,10,10,6,10],
[4,0,0,0,6,4,0,4,6,4],
[10,6,10,0,6,10,6,10,6,10],
[4,0,4,4,0,4,0,4,0,4],
[10,6,6,0,6,0,6,6,6,6],
[4,0,10,4,10,4,0,4,6,4],
[4,0,6,0,6,4,6,0,6,10],
[4,4,4,4,10,4,4,4,0,4],
[4,0,6,0,6,4,6,0,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 4, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,0,6,6,0,6,6,10,6,6],
[10,0,10,6,6,10,6,10,10,10],
[4,0,0,6,0,6,6,10,0,10],
[4,4,4,0,4,4,10,10,4,4],
[10,4,10,6,0,10,10,10,10,10],
[4,0,4,6,0,0,6,10,4,10],
[4,4,4,0,0,4,0,4,4,4],
[0,0,0,0,0,0,6,0,0,0],
[4,0,10,6,0,6,6,10,0,10],
[4,0,0,6,0,0,6,10,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,10,3,10,7,3,10,3,3],
[0,0,10,0,7,7,3,7,3,3],
[0,0,0,0,7,3,3,0,0,3],
[7,10,10,0,10,7,7,10,7,7],
[0,3,3,0,0,3,0,0,0,0],
[3,3,7,3,7,0,0,7,0,3],
[7,7,7,3,10,10,0,7,3,6],
[0,3,10,0,10,3,3,0,0,3],
[7,7,10,3,10,10,7,10,0,6],
[7,7,7,3,10,7,4,7,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,0,0,0,6,6,6,0,0],
[4,0,4,4,0,10,10,4,4,0],
[10,6,0,0,6,6,6,10,4,6],
[10,6,10,0,6,10,10,10,4,6],
[10,10,4,4,0,10,10,10,4,6],
[4,0,4,0,0,0,6,4,4,0],
[4,0,4,0,0,4,0,4,4,0],
[4,6,0,0,0,6,6,0,0,0],
[10,6,6,6,6,6,6,10,0,6],
[10,10,4,4,4,10,10,10,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,4,10,10,10,4,10,0,10],
[0,0,4,10,10,10,4,4,0,4],
[6,6,0,6,6,6,6,10,0,6],
[0,0,4,0,10,0,4,4,0,0],
[0,0,4,0,0,0,4,4,0,0],
[0,0,4,10,10,0,4,4,0,4],
[6,6,4,6,6,6,0,10,0,6],
[0,6,0,6,6,6,0,0,0,6],
[10,10,10,10,10,10,10,10,0,10],
[0,6,4,10,10,6,4,4,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,6,10,10,10,10,10,10,4],
[0,0,0,0,0,6,0,6,6,0],
[4,10,0,10,10,10,10,10,10,4],
[0,10,0,0,0,10,0,6,10,4],
[0,10,0,10,0,10,4,6,10,4],
[0,4,0,0,0,0,0,6,0,0],
[0,10,0,10,6,10,0,6,10,4],
[0,4,0,4,4,4,4,0,4,4],
[0,4,0,0,0,10,0,6,0,4],
[6,10,6,6,6,10,6,6,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 5, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,9,7,9,9,9,9,7,1,6],
[1,0,1,7,9,6,8,6,2,6],
[3,9,0,9,10,10,8,8,3,6],
[1,3,1,0,8,6,3,2,1,2],
[1,1,0,2,0,7,1,1,1,0],
[1,4,0,4,3,0,3,1,1,1],
[1,2,2,7,9,7,0,6,2,7],
[3,4,2,8,9,9,4,0,2,8],
[9,8,7,9,9,9,8,8,0,7],
[4,4,4,8,10,9,3,2,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,4,4,10,10,0,6,4,10],
[4,0,4,4,10,4,4,10,4,10],
[6,6,0,10,10,10,6,6,4,10],
[6,6,0,0,10,6,6,6,4,10],
[0,0,0,0,0,0,0,6,0,0],
[0,6,0,4,10,0,0,6,4,10],
[10,6,4,4,10,10,0,6,4,10],
[4,0,4,4,4,4,4,0,4,4],
[6,6,6,6,10,6,6,6,0,10],
[0,0,0,0,10,0,0,6,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,0,0,0,4,4,0,0,6,10],
[10,0,4,4,4,10,0,4,6,10],
[10,6,0,4,4,10,0,0,6,10],
[10,6,6,0,4,10,0,0,6,10],
[6,6,6,6,0,10,6,6,6,10],
[6,0,0,0,0,0,0,0,6,10],
[10,10,10,10,4,10,0,4,10,10],
[10,6,10,10,4,10,6,0,6,10],
[4,4,4,4,4,4,0,4,0,4],
[0,0,0,0,0,0,0,0,6,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,10,10,10,10,10,10,4,10],
[4,0,4,10,10,10,4,10,4,4],
[0,6,0,6,10,10,10,10,4,10],
[0,0,4,0,10,10,4,10,4,4],
[0,0,0,0,0,0,4,6,4,0],
[0,0,0,0,10,0,4,6,4,0],
[0,6,0,6,6,6,0,6,4,0],
[0,0,0,0,4,4,4,0,4,0],
[6,6,6,6,6,6,6,6,0,6],
[0,6,0,6,10,10,10,10,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,3,7,3,3,10,3,0,0],
[0,0,0,0,3,0,0,0,0,0],
[7,10,0,7,3,7,7,7,7,7],
[3,10,3,0,3,3,10,3,0,0],
[7,7,7,7,0,7,7,7,7,7],
[7,10,3,7,3,0,10,0,7,7],
[0,10,3,0,3,0,0,0,0,0],
[7,10,3,7,3,10,10,0,7,7],
[10,10,3,10,3,3,10,3,0,7],
[10,10,3,10,3,3,10,3,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 6, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,10,6,10,10,4,10,10,10,10],
[0,0,6,10,6,4,10,10,0,6],
[4,4,0,4,4,4,10,10,4,4],
[0,0,6,0,0,4,10,10,0,0],
[0,4,6,10,0,4,10,10,4,10],
[6,6,6,6,6,0,6,6,6,6],
[0,0,0,0,0,4,0,4,0,0],
[0,0,0,0,0,4,6,0,0,0],
[0,10,6,10,6,4,10,10,0,6],
[0,4,6,10,0,4,10,10,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,7,7,7,7,7,7,0,7,7],
[3,0,7,10,3,7,10,0,3,7],
[3,3,0,10,3,10,10,3,3,10],
[3,0,0,0,3,7,7,0,3,0],
[3,7,7,7,0,7,7,0,7,7],
[3,3,0,3,3,0,10,0,3,0],
[3,0,0,3,3,0,0,0,3,0],
[10,10,7,10,10,10,10,0,10,7],
[3,7,7,7,3,7,7,0,0,7],
[3,3,0,10,3,10,10,3,3,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,4,4,4,8,10,4,8,4,2],
[6,0,4,2,10,10,0,10,2,2],
[6,6,0,2,10,6,2,6,2,6],
[6,8,8,0,10,10,4,8,2,6],
[2,0,0,0,0,2,0,0,2,2],
[0,0,4,0,8,0,0,4,0,0],
[6,10,8,6,10,10,0,10,2,6],
[2,0,4,2,10,6,0,0,2,2],
[6,8,8,8,8,10,8,8,0,6],
[8,8,4,4,8,10,4,8,4,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,6,6,6,10,6,6,6,6,6],
[4,0,6,4,4,4,10,4,6,6],
[4,4,0,4,4,4,10,4,6,10],
[4,6,6,0,10,6,6,6,6,6],
[0,6,6,0,0,0,6,0,6,6],
[4,6,6,4,10,0,6,0,6,6],
[4,0,0,4,4,4,0,4,0,0],
[4,6,6,4,10,10,6,0,6,6],
[4,4,4,4,4,4,10,4,0,10],
[4,4,0,4,4,4,10,4,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

##############################################################
om = np.array([
[0,0,4,0,0,0,0,0,0,4],
[10,0,10,6,6,10,6,6,0,10],
[6,0,0,6,6,6,6,6,0,10],
[10,4,4,0,10,4,10,10,4,10],
[10,4,4,0,0,4,4,0,4,4],
[10,0,4,6,6,0,6,6,0,10],
[10,4,4,0,6,4,0,6,4,10],
[10,4,4,0,10,4,4,0,4,10],
[10,10,10,6,6,10,6,6,0,10],
[6,0,0,0,6,0,0,0,0,0]])


times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))


times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 7, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results10 = np.vstack((results10, result))

 
pd.DataFrame(results10).to_csv("results10cr_azzini.csv")