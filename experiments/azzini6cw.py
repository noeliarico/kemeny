
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
results6 = np.zeros(0).reshape(0,8+rep)

##############################################################
om = np.array([
[0,6,2,3,8,5],
[4,0,4,7,3,5],
[8,6,0,7,9,9],
[7,3,3,0,6,3],
[2,7,1,4,0,4],
[5,5,1,7,6,0]])


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
result = np.append(np.array([6, 1, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,8,8,6,9,8],
[2,0,4,4,5,7],
[2,6,0,6,5,3],
[4,6,4,0,4,6],
[1,5,5,6,0,3],
[2,3,7,4,7,0]])


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
result = np.append(np.array([6, 1, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,2,3,4,3,4],
[8,0,8,8,8,8],
[7,2,0,5,6,4],
[6,2,5,0,4,5],
[7,2,4,6,0,5],
[6,2,6,5,5,0]])


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
result = np.append(np.array([6, 1, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,4,4,6,5,4],
[6,0,7,6,10,8],
[6,3,0,6,5,3],
[4,4,4,0,5,4],
[5,0,5,5,0,7],
[6,2,7,6,3,0]])


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
result = np.append(np.array([6, 1, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,6,6,5,4],
[7,0,5,5,4,3],
[4,5,0,6,5,2],
[4,5,4,0,5,1],
[5,6,5,5,0,2],
[6,7,8,9,8,0]])


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
result = np.append(np.array([6, 1, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 1, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,8,8,6,4,5],
[2,0,6,6,3,4],
[2,4,0,6,3,6],
[4,4,4,0,1,4],
[6,7,7,9,0,8],
[5,6,4,6,2,0]])


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
result = np.append(np.array([6, 2, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,0,4,6,6,6],
[10,0,6,10,6,6],
[6,4,0,6,2,6],
[4,0,4,0,0,4],
[4,4,8,10,0,6],
[4,4,4,6,4,0]])


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
result = np.append(np.array([6, 2, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,0,3,5,8,3],
[10,0,8,10,9,7],
[7,2,0,5,5,4],
[5,0,5,0,3,4],
[2,1,5,7,0,4],
[7,3,6,6,6,0]])


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
result = np.append(np.array([6, 2, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,2,0,5,5],
[7,0,7,2,2,5],
[8,3,0,0,5,5],
[10,8,10,0,10,10],
[5,8,5,0,0,10],
[5,5,5,0,0,0]])


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
result = np.append(np.array([6, 2, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,6,5,5,5],
[7,0,9,6,8,7],
[4,1,0,2,5,4],
[5,4,8,0,5,6],
[5,2,5,5,0,6],
[5,3,6,4,4,0]])


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
result = np.append(np.array([6, 2, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 2, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,4,6,4,3,4],
[6,0,8,8,5,4],
[4,2,0,6,3,1],
[6,2,4,0,2,2],
[7,5,7,8,0,3],
[6,6,9,8,7,0]])


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
result = np.append(np.array([6, 3, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,7,7,6,4,5],
[3,0,5,6,3,4],
[3,5,0,7,3,7],
[4,4,3,0,1,3],
[6,7,7,9,0,8],
[5,6,3,7,2,0]])


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
result = np.append(np.array([6, 3, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,5,0,5,10,0],
[5,0,5,10,10,0],
[10,5,0,5,10,0],
[5,0,5,0,5,0],
[0,0,0,5,0,0],
[10,10,10,10,10,0]])


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
result = np.append(np.array([6, 3, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,0,3,6,4],
[7,0,3,10,10,4],
[10,7,0,7,10,4],
[7,0,3,0,3,4],
[4,0,0,7,0,4],
[6,6,6,6,6,0]])


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
result = np.append(np.array([6, 3, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,5,3,4,5],
[7,0,6,8,8,8],
[5,4,0,4,5,5],
[7,2,6,0,6,8],
[6,2,5,4,0,8],
[5,2,5,2,2,0]])


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
result = np.append(np.array([6, 3, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 3, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,3,9,6,2,7],
[7,0,8,8,3,6],
[1,2,0,2,1,1],
[4,2,8,0,0,5],
[8,7,9,10,0,6],
[3,4,9,5,4,0]])


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
result = np.append(np.array([6, 4, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,5,4,6,8,8],
[5,0,3,5,8,7],
[6,7,0,6,6,6],
[4,5,4,0,6,7],
[2,2,4,4,0,3],
[2,3,4,3,7,0]])


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
result = np.append(np.array([6, 4, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,0,0,4,4,0],
[10,0,6,6,6,6],
[10,4,0,4,4,4],
[6,4,6,0,2,6],
[6,4,6,8,0,4],
[10,4,6,4,6,0]])


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
result = np.append(np.array([6, 4, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,6,4,10,2,2],
[4,0,6,10,4,4],
[6,4,0,10,6,4],
[0,0,0,0,0,2],
[8,6,4,10,0,4],
[8,6,6,8,6,0]])


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
result = np.append(np.array([6, 4, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,5,4,8,2,1],
[5,0,7,10,6,3],
[6,3,0,10,6,3],
[2,0,0,0,0,1],
[8,4,4,10,0,3],
[9,7,7,9,7,0]])


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
result = np.append(np.array([6, 4, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 4, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,0,2,2,4,2],
[10,0,8,6,6,6],
[8,2,0,5,5,5],
[8,4,5,0,4,5],
[6,4,5,6,0,4],
[8,4,5,5,6,0]])


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
result = np.append(np.array([6, 5, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,4,8,4,4,6],
[6,0,10,6,6,6],
[2,0,0,0,0,2],
[6,4,10,0,4,6],
[6,4,10,6,0,2],
[4,4,8,4,8,0]])


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
result = np.append(np.array([6, 5, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,4,6,6,4,5],
[6,0,6,8,6,6],
[4,4,0,7,5,6],
[4,2,3,0,2,2],
[6,4,5,8,0,6],
[5,4,4,8,4,0]])


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
result = np.append(np.array([6, 5, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,6,8,5,4,2],
[4,0,8,5,4,4],
[2,2,0,4,2,1],
[5,5,6,0,6,3],
[6,6,8,4,0,2],
[8,6,9,7,8,0]])


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
result = np.append(np.array([6, 5, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

##############################################################
om = np.array([
[0,6,9,7,3,6],
[4,0,9,5,3,4],
[1,1,0,0,0,1],
[3,5,10,0,4,3],
[7,7,10,6,0,7],
[4,6,9,7,3,0]])


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
result = np.append(np.array([6, 5, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))


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
result = np.append(np.array([6, 5, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results6 = np.vstack((results6, result))

 
pd.DataFrame(results6).to_csv("results6cw_azzini.csv")