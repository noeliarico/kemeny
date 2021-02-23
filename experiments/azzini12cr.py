
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
results12 = np.zeros(0).reshape(0,8+rep)

##############################################################
om = np.array([
[0,4,4,4,0,4,4,4,4,6,6,6],
[6,0,6,0,0,6,4,10,6,6,6,6],
[6,4,0,4,0,4,4,10,4,6,6,6],
[6,10,6,0,6,10,10,10,10,6,6,6],
[10,10,10,4,0,10,10,10,10,10,10,10],
[6,4,6,0,0,0,4,10,6,6,6,6],
[6,6,6,0,0,6,0,6,6,6,6,6],
[6,0,0,0,0,0,4,0,0,6,6,6],
[6,4,6,0,0,4,4,10,0,6,6,6],
[4,4,4,4,0,4,4,4,4,0,6,0],
[4,4,4,4,0,4,4,4,4,4,0,4],
[4,4,4,4,0,4,4,4,4,10,6,0]])


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
result = np.append(np.array([12, 3, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,4,10,10,10,4,4,4,4,10,4],
[0,0,0,10,6,6,4,4,4,4,10,0],
[6,10,0,10,6,10,10,10,10,10,10,6],
[0,0,0,0,6,6,4,4,4,4,0,0],
[0,4,4,4,0,4,4,4,4,4,4,0],
[0,4,0,4,6,0,4,4,4,4,4,0],
[6,6,0,6,6,6,0,6,6,6,6,0],
[6,6,0,6,6,6,4,0,6,6,6,0],
[6,6,0,6,6,6,4,4,0,4,6,0],
[6,6,0,6,6,6,4,4,6,0,6,0],
[0,0,0,10,6,6,4,4,4,4,0,0],
[6,10,4,10,10,10,10,10,10,10,10,0]])


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
result = np.append(np.array([12, 3, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,6,6,0,6,6,6,6,6,0,6],
[4,0,6,6,0,6,6,6,6,6,0,6],
[4,4,0,6,4,4,6,10,4,0,4,6],
[4,4,4,0,4,4,0,4,4,0,4,0],
[10,10,6,6,0,10,6,10,10,6,4,6],
[4,4,6,6,0,0,6,6,4,6,4,6],
[4,4,4,10,4,4,0,4,4,0,4,6],
[4,4,0,6,0,4,6,0,4,0,4,6],
[4,4,6,6,0,6,6,6,0,6,0,6],
[4,4,10,10,4,4,10,10,4,0,4,10],
[10,10,6,6,6,6,6,6,10,6,0,6],
[4,4,4,10,4,4,4,4,4,0,4,0]])


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
result = np.append(np.array([12, 3, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,4,0,4,4,4,4,4,4,4,4],
[10,0,4,10,10,10,10,10,10,10,10,10],
[6,6,0,6,10,10,10,10,10,10,10,10],
[10,0,4,0,4,4,4,4,4,4,4,4],
[6,0,0,6,0,10,0,4,6,4,6,6],
[6,0,0,6,0,0,0,4,6,4,6,6],
[6,0,0,6,10,10,0,4,10,10,6,6],
[6,0,0,6,6,6,6,0,6,6,6,6],
[6,0,0,6,4,4,0,4,0,4,6,6],
[6,0,0,6,6,6,0,4,6,0,6,6],
[6,0,0,6,4,4,4,4,4,4,0,0],
[6,0,0,6,4,4,4,4,4,4,10,0]])


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
result = np.append(np.array([12, 3, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,0,6,4,6,4,4,6,4,0,10],
[4,0,0,0,4,10,4,4,4,4,0,4],
[10,10,0,10,10,10,10,10,10,10,4,10],
[4,10,0,0,4,10,4,4,4,4,0,10],
[6,6,0,6,0,6,4,6,6,4,0,10],
[4,0,0,0,4,0,4,4,0,4,0,4],
[6,6,0,6,6,6,0,6,6,0,0,10],
[6,6,0,6,4,6,4,0,6,4,0,10],
[4,6,0,6,4,10,4,4,0,4,0,10],
[6,6,0,6,6,6,10,6,6,0,0,10],
[10,10,6,10,10,10,10,10,10,10,0,10],
[0,6,0,0,0,6,0,0,0,0,0,0]])


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
result = np.append(np.array([12, 3, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 3, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,6,10,0,10,6,10,6,10,10,6],
[0,0,0,6,0,0,0,4,6,0,0,6],
[4,10,0,10,0,10,6,10,6,10,10,10],
[0,4,0,0,0,0,0,4,0,0,4,6],
[10,10,10,10,0,10,10,10,10,10,10,10],
[0,10,0,10,0,0,0,4,6,6,10,6],
[4,10,4,10,0,10,0,10,6,10,10,10],
[0,6,0,6,0,6,0,0,6,6,6,6],
[4,4,4,10,0,4,4,4,0,4,4,10],
[0,10,0,10,0,4,0,4,6,0,4,6],
[0,10,0,6,0,0,0,4,6,6,0,6],
[4,4,0,4,0,4,0,4,0,4,4,0]])


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
result = np.append(np.array([12, 4, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,6,6,0,0,0,0,6,0,6,6],
[4,0,6,6,0,4,4,0,6,4,6,6],
[4,4,0,10,0,4,4,4,0,4,10,6],
[4,4,0,0,0,4,4,4,0,4,4,6],
[10,10,10,10,0,10,10,10,10,10,10,6],
[10,6,6,6,0,0,4,0,6,4,6,6],
[10,6,6,6,0,6,0,0,6,0,6,6],
[10,10,6,6,0,10,10,0,6,4,6,6],
[4,4,10,10,0,4,4,4,0,4,10,6],
[10,6,6,6,0,6,10,6,6,0,6,6],
[4,4,0,6,0,4,4,4,0,4,0,6],
[4,4,4,4,4,4,4,4,4,4,4,0]])


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
result = np.append(np.array([12, 4, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,0,10,10,0,0,6,10,10,10,10],
[0,0,0,4,4,0,0,6,6,10,6,4],
[10,10,0,10,10,4,10,10,10,10,10,10],
[0,6,0,0,4,0,0,6,6,10,6,6],
[0,6,0,6,0,0,0,6,6,10,6,6],
[10,10,6,10,10,0,10,10,10,10,10,10],
[10,10,0,10,10,0,0,10,10,10,10,10],
[4,4,0,4,4,0,0,0,10,10,10,4],
[0,4,0,4,4,0,0,0,0,10,6,4],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,4,0,4,4,0,0,0,4,10,0,4],
[0,6,0,4,4,0,0,6,6,10,6,0]])


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
result = np.append(np.array([12, 4, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,4,0,0,4,4,4,0,0,0,0],
[6,0,0,0,0,0,4,0,0,6,0,0],
[6,10,0,6,6,10,4,6,0,6,0,0],
[10,10,4,0,10,10,4,10,4,6,4,4],
[10,10,4,0,0,10,4,4,4,6,0,0],
[6,10,0,0,0,0,4,0,0,6,0,0],
[6,6,6,6,6,6,0,6,0,6,0,0],
[6,10,4,0,6,10,4,0,0,6,0,0],
[10,10,10,6,6,10,10,10,0,6,0,0],
[10,4,4,4,4,4,4,4,4,0,4,4],
[10,10,10,6,10,10,10,10,10,6,0,0],
[10,10,10,6,10,10,10,10,10,6,10,0]])


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
result = np.append(np.array([12, 4, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,0,10,0,4,6,6,4,4,4,4],
[10,0,4,10,4,4,10,10,10,4,10,10],
[10,6,0,10,10,10,10,6,10,4,10,10],
[0,0,0,0,0,4,6,6,4,0,4,4],
[10,6,0,10,0,10,10,6,10,4,10,10],
[6,6,0,6,0,0,6,6,10,0,6,6],
[4,0,0,4,0,4,0,6,4,4,4,4],
[4,0,4,4,4,4,4,0,4,4,4,4],
[6,0,0,6,0,0,6,6,0,0,0,0],
[6,6,6,10,6,10,6,6,10,0,10,10],
[6,0,0,6,0,4,6,6,10,0,0,4],
[6,0,0,6,0,4,6,6,10,0,6,0]])


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
result = np.append(np.array([12, 4, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 4, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,4,10,0,10,0,6,4,10,10,10],
[0,0,0,6,0,0,0,6,0,0,0,0],
[6,10,0,10,6,10,6,6,0,10,10,10],
[0,4,0,0,0,0,0,0,0,4,4,4],
[10,10,4,10,0,10,6,10,4,10,10,10],
[0,10,0,10,0,0,0,6,0,10,10,4],
[10,10,4,10,4,10,0,10,4,10,10,10],
[4,4,4,10,0,4,0,0,4,4,4,4],
[6,10,10,10,6,10,6,6,0,10,10,10],
[0,10,0,6,0,0,0,6,0,0,0,0],
[0,10,0,6,0,0,0,6,0,10,0,0],
[0,10,0,6,0,6,0,6,0,10,10,0]])


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
result = np.append(np.array([12, 5, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,4,4,4,4,4,4,4,4,4,4],
[6,0,0,0,6,6,10,6,6,6,0,6],
[6,10,0,0,6,6,10,10,10,6,6,6],
[6,10,10,0,6,6,10,10,10,6,6,6],
[6,4,4,4,0,10,4,10,10,10,0,10],
[6,4,4,4,0,0,4,10,10,0,0,6],
[6,0,0,0,6,6,0,6,6,6,0,6],
[6,4,0,0,0,0,4,0,6,0,0,6],
[6,4,0,0,0,0,4,4,0,0,0,0],
[6,4,4,4,0,10,4,10,10,0,0,10],
[6,10,4,4,10,10,10,10,10,10,0,10],
[6,4,4,4,0,4,4,4,10,0,0,0]])


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
result = np.append(np.array([12, 5, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,4,0,0,0,0,4,0,0,6,6],
[10,0,10,0,6,0,6,4,0,0,6,6],
[6,0,0,0,0,0,6,4,0,0,6,6],
[10,10,10,0,6,6,10,10,6,10,10,6],
[10,4,10,4,0,4,10,4,4,4,10,10],
[10,10,10,4,6,0,10,10,0,10,10,10],
[10,4,4,0,0,0,0,4,0,4,10,6],
[6,6,6,0,6,0,6,0,0,0,6,6],
[10,10,10,4,6,10,10,10,0,10,10,10],
[10,10,10,0,6,0,6,10,0,0,10,6],
[4,4,4,0,0,0,0,4,0,0,0,0],
[4,4,4,4,0,0,4,4,0,4,10,0]])


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
result = np.append(np.array([12, 5, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,4,4,0,0,4,6,4,4,6,6],
[4,0,4,4,4,4,4,10,4,4,6,4],
[6,6,0,0,0,0,0,6,0,4,6,6],
[6,6,10,0,0,6,4,6,4,4,6,6],
[10,6,10,10,0,10,10,6,4,10,6,6],
[10,6,10,4,0,0,4,6,4,4,6,6],
[6,6,10,6,0,6,0,6,4,4,6,6],
[4,0,4,4,4,4,4,0,4,4,0,4],
[6,6,10,6,6,6,6,6,0,10,6,6],
[6,6,6,6,0,6,6,6,0,0,6,6],
[4,4,4,4,4,4,4,10,4,4,0,4],
[4,6,4,4,4,4,4,6,4,4,6,0]])


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
result = np.append(np.array([12, 5, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,10,6,10,6,0,4,6,6,0,6],
[10,0,10,10,10,10,10,4,10,10,4,10],
[0,0,0,0,6,6,0,0,0,6,0,0],
[4,0,10,0,10,6,0,4,0,10,0,0],
[0,0,4,0,0,6,0,0,0,0,0,0],
[4,0,4,4,4,0,0,4,0,4,0,4],
[10,0,10,10,10,10,0,4,6,10,0,10],
[6,6,10,6,10,6,6,0,6,6,6,6],
[4,0,10,10,10,10,4,4,0,10,4,10],
[4,0,4,0,10,6,0,4,0,0,0,0],
[10,6,10,10,10,10,10,4,6,10,0,10],
[4,0,10,10,10,6,0,4,0,10,0,0]])


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
result = np.append(np.array([12, 5, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 5, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,6,0,6,0,0,0,10,6,6,6],
[4,0,4,4,0,4,4,0,10,10,4,4],
[4,6,0,4,6,4,4,0,10,10,4,0],
[10,6,6,0,6,0,4,0,10,10,6,6],
[4,10,4,4,0,4,4,4,10,10,4,4],
[10,6,6,10,6,0,4,0,10,10,10,6],
[10,6,6,6,6,6,0,6,10,10,6,6],
[10,10,10,10,6,10,4,0,10,10,10,10],
[0,0,0,0,0,0,0,0,0,0,0,0],
[4,0,0,0,0,0,0,0,10,0,0,0],
[4,6,6,4,6,0,4,0,10,10,0,0],
[4,6,10,4,6,4,4,0,10,10,10,0]])


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
result = np.append(np.array([12, 6, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,0,6,0,6,0,0,4,0,6,6],
[10,0,4,6,0,6,0,0,4,0,6,6],
[10,6,0,6,0,6,0,0,4,0,6,6],
[4,4,4,0,4,0,0,0,4,0,6,0],
[10,10,10,6,0,6,0,6,4,6,6,6],
[4,4,4,10,4,0,0,0,4,0,6,0],
[10,10,10,10,10,10,0,6,4,10,10,6],
[10,10,10,10,4,10,4,0,4,4,10,6],
[6,6,6,6,6,6,6,6,0,6,6,6],
[10,10,10,10,4,10,0,6,4,0,6,6],
[4,4,4,4,4,4,0,0,4,4,0,0],
[4,4,4,10,4,10,4,4,4,4,10,0]])


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
result = np.append(np.array([12, 6, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,4,10,10,4,10,10,4,4,10,10],
[0,0,4,4,0,4,10,4,4,0,6,4],
[6,6,0,6,6,4,6,6,6,6,6,6],
[0,6,4,0,0,4,10,0,4,0,6,4],
[0,10,4,10,0,4,10,10,4,4,10,10],
[6,6,6,6,6,0,6,6,6,6,6,6],
[0,0,4,0,0,4,0,0,4,0,0,4],
[0,6,4,10,0,4,10,0,4,0,6,10],
[6,6,4,6,6,4,6,6,0,0,6,10],
[6,10,4,10,6,4,10,10,10,0,6,10],
[0,4,4,4,0,4,10,4,4,4,0,4],
[0,6,4,6,0,4,6,0,0,0,6,0]])


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
result = np.append(np.array([12, 6, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,0,0,6,4,4,0,4,10,4,4],
[10,0,6,6,10,10,10,6,10,10,10,10],
[10,4,0,10,10,10,10,10,10,10,10,10],
[10,4,0,0,10,4,4,10,10,10,10,4],
[4,0,0,0,0,4,4,0,4,10,4,4],
[6,0,0,6,6,0,0,6,10,10,10,10],
[6,0,0,6,6,10,0,6,10,10,10,10],
[10,4,0,0,10,4,4,0,10,10,10,4],
[6,0,0,0,6,0,0,0,0,10,10,0],
[0,0,0,0,0,0,0,0,0,0,4,0],
[6,0,0,0,6,0,0,0,0,6,0,0],
[6,0,0,6,6,0,0,6,10,10,10,0]])


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
result = np.append(np.array([12, 6, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,4,4,10,4,4,4,4,4,4,4],
[6,0,10,4,10,10,10,6,10,10,10,10],
[6,0,0,0,10,6,6,6,10,6,6,10],
[6,6,10,0,10,10,6,6,10,10,10,10],
[0,0,0,0,0,0,0,0,0,0,0,4],
[6,0,4,0,10,0,6,0,10,0,6,4],
[6,0,4,4,10,4,0,0,10,4,10,4],
[6,4,4,4,10,10,10,0,10,10,10,4],
[6,0,0,0,10,0,0,0,0,0,0,4],
[6,0,4,0,10,10,6,0,10,0,10,4],
[6,0,4,0,10,4,0,0,10,0,0,4],
[6,0,0,0,6,6,6,6,6,6,6,0]])


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
result = np.append(np.array([12, 6, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 6, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,10,10,4,6,6,6,6,10,10,10],
[0,0,4,0,0,0,0,0,0,10,0,0],
[0,6,0,6,0,0,0,0,0,6,0,0],
[0,10,4,0,0,0,0,0,0,10,0,0],
[6,10,10,10,0,6,6,6,6,10,10,10],
[4,10,10,10,4,0,6,0,6,10,4,10],
[4,10,10,10,4,4,0,0,6,10,4,10],
[4,10,10,10,4,10,10,0,6,10,10,10],
[4,10,10,10,4,4,4,4,0,10,4,10],
[0,0,4,0,0,0,0,0,0,0,0,0],
[0,10,10,10,0,6,6,0,6,10,0,6],
[0,10,10,10,0,0,0,0,0,10,4,0]])


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
result = np.append(np.array([12, 7, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,10,10,7,7,7,7,7,10,10,10],
[0,0,3,0,0,0,0,0,0,10,0,4],
[0,7,0,7,0,0,0,0,4,7,4,4],
[0,10,3,0,0,0,0,0,4,10,0,4],
[3,10,10,10,0,7,3,3,7,10,10,10],
[3,10,10,10,3,0,3,0,7,10,7,10],
[3,10,10,10,7,7,0,0,7,10,7,10],
[3,10,10,10,7,10,10,0,7,10,10,10],
[3,10,6,6,3,3,3,3,0,10,3,10],
[0,0,3,0,0,0,0,0,0,0,0,0],
[0,10,6,10,0,3,3,0,7,10,0,7],
[0,6,6,6,0,0,0,0,0,10,3,0]])


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
result = np.append(np.array([12, 7, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,0,4,10,0,0,4,10,0,4,0],
[10,0,6,10,10,0,6,10,10,6,10,10],
[10,4,0,10,10,0,0,4,10,4,4,4],
[6,0,0,0,6,0,0,0,6,0,0,0],
[0,0,0,4,0,0,0,0,0,0,0,0],
[10,10,10,10,10,0,6,10,10,10,10,10],
[10,4,10,10,10,4,0,4,10,10,10,4],
[6,0,6,10,10,0,6,0,6,6,6,0],
[0,0,0,4,10,0,0,4,0,0,4,0],
[10,4,6,10,10,0,0,4,10,0,4,4],
[6,0,6,10,10,0,0,4,6,6,0,0],
[10,0,6,10,10,0,6,10,10,6,10,0]])


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
result = np.append(np.array([12, 7, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,4,0,6,6,0,6,0,10,0,0],
[10,0,10,6,6,6,6,10,6,10,0,4],
[6,0,0,6,6,6,0,6,6,10,0,0],
[10,4,4,0,6,6,4,10,6,10,0,4],
[4,4,4,4,0,0,4,4,0,4,0,4],
[4,4,4,4,10,0,4,10,4,10,4,4],
[10,4,10,6,6,6,0,10,6,10,0,4],
[4,0,4,0,6,0,0,0,0,10,0,0],
[10,4,4,4,10,6,4,10,0,10,0,4],
[0,0,0,0,6,0,0,0,0,0,0,0],
[10,10,10,10,10,6,10,10,10,10,0,10],
[10,6,10,6,6,6,6,10,6,10,0,0]])


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
result = np.append(np.array([12, 7, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,6,6,6,6,6,6,6,6,6,6],
[4,0,0,4,0,10,0,0,0,10,6,6],
[4,10,0,4,6,10,10,6,4,10,10,10],
[4,6,6,0,6,6,6,6,0,6,6,6],
[4,10,4,4,0,10,10,4,4,10,10,10],
[4,0,0,4,0,0,0,0,0,0,6,0],
[4,10,0,4,0,10,0,0,0,10,10,10],
[4,10,4,4,6,10,10,0,4,10,10,10],
[4,10,6,10,6,10,10,6,0,10,10,10],
[4,0,0,4,0,10,0,0,0,0,6,0],
[4,4,0,4,0,4,0,0,0,4,0,0],
[4,4,0,4,0,10,0,0,0,10,10,0]])


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
result = np.append(np.array([12, 7, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 7, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,10,4,6,4,4,4,4,4,6,10,4],
[0,0,0,6,0,0,0,0,0,6,6,0],
[6,10,0,6,10,4,6,0,0,6,10,0],
[4,4,4,0,4,4,4,4,4,0,10,4],
[6,10,0,6,0,0,0,0,0,6,10,0],
[6,10,6,6,10,0,6,0,6,6,10,0],
[6,10,4,6,10,4,0,4,4,6,10,4],
[6,10,10,6,10,10,6,0,6,6,10,10],
[6,10,10,6,10,4,6,4,0,6,10,4],
[4,4,4,10,4,4,4,4,4,0,10,4],
[0,4,0,0,0,0,0,0,0,0,0,0],
[6,10,10,6,10,10,6,0,6,6,10,0]])


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
result = np.append(np.array([12, 8, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,10,4,10,6,10,6,6,6,10,10],
[4,0,4,4,10,0,10,6,0,6,10,10],
[0,6,0,4,10,6,6,6,0,6,10,10],
[6,6,6,0,6,6,6,6,6,6,6,6],
[0,0,0,4,0,0,0,0,0,0,0,6],
[4,10,4,4,10,0,10,6,4,10,10,10],
[0,0,4,4,10,0,0,6,0,6,10,10],
[4,4,4,4,10,4,4,0,4,4,10,10],
[4,10,10,4,10,6,10,6,0,6,10,10],
[4,4,4,4,10,0,4,6,4,0,10,10],
[0,0,0,4,10,0,0,0,0,0,0,10],
[0,0,0,4,4,0,0,0,0,0,0,0]])


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
result = np.append(np.array([12, 8, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,2,1,8,1,1,1,1,7,7,1,2],
[8,0,8,10,3,2,7,3,9,9,3,4],
[9,2,0,10,3,3,1,3,9,9,4,4],
[2,0,0,0,0,0,1,2,8,2,3,2],
[9,7,7,10,0,6,8,9,10,8,10,3],
[9,8,7,10,4,0,8,4,10,10,10,4],
[9,3,9,9,2,2,0,2,9,8,3,3],
[9,7,7,8,1,6,8,0,8,7,8,2],
[3,1,1,2,0,0,1,2,0,2,2,1],
[3,1,1,8,2,0,2,3,8,0,2,1],
[9,7,6,7,0,0,7,2,8,8,0,1],
[8,6,6,8,7,6,7,8,9,9,9,0]])


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
result = np.append(np.array([12, 8, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,4,10,4,0,4,4,4,10,4,10],
[6,0,6,10,6,6,4,10,4,6,10,10],
[6,4,0,10,4,0,4,10,4,6,4,10],
[0,0,0,0,0,0,4,0,0,6,0,0],
[6,4,6,10,0,0,4,10,4,6,4,10],
[10,4,10,10,10,0,4,10,4,10,4,10],
[6,6,6,6,6,6,0,6,0,6,6,6],
[6,0,0,10,0,0,4,0,4,6,0,6],
[6,6,6,10,6,6,10,6,0,6,6,6],
[0,4,4,4,4,0,4,4,4,0,4,4],
[6,0,6,10,6,6,4,10,4,6,0,10],
[0,0,0,10,0,0,4,4,4,6,0,0]])


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
result = np.append(np.array([12, 8, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,4,4,4,4,4,4,4,4,0,0],
[6,0,4,4,4,10,10,10,4,4,6,0],
[6,6,0,6,10,10,6,10,6,0,6,6],
[6,6,4,0,4,10,10,10,4,4,6,0],
[6,6,0,6,0,10,6,10,6,0,6,6],
[6,0,0,0,0,0,6,6,0,0,0,0],
[6,0,4,0,4,4,0,10,0,0,0,0],
[6,0,0,0,0,4,0,0,0,0,0,0],
[6,6,4,6,4,10,10,10,0,4,6,6],
[6,6,10,6,10,10,10,10,6,0,6,6],
[10,4,4,4,4,10,10,10,4,4,0,4],
[10,10,4,10,4,10,10,10,4,4,6,0]])


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
result = np.append(np.array([12, 8, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 8, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,6,6,4,6,6,6,6,10,6,4],
[4,0,10,4,4,4,4,10,6,10,4,4],
[4,0,0,4,4,4,4,10,0,4,4,4],
[4,6,6,0,4,6,6,10,6,10,10,4],
[6,6,6,6,0,6,6,6,6,10,6,10],
[4,6,6,4,4,0,0,10,6,10,4,4],
[4,6,6,4,4,10,0,10,6,10,4,4],
[4,0,0,0,4,0,0,0,0,4,4,4],
[4,4,10,4,4,4,4,10,0,4,4,4],
[0,0,6,0,0,0,0,6,6,0,0,4],
[4,6,6,0,4,6,6,6,6,10,0,4],
[6,6,6,6,0,6,6,6,6,6,6,0]])


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
result = np.append(np.array([12, 9, 1, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 1, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 1, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 1, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,6,6,10,6,0,6,6,10,6,10],
[6,0,6,6,6,6,6,6,6,6,6,6],
[4,4,0,4,4,6,4,6,4,10,4,10],
[4,4,6,0,10,6,4,6,6,10,6,10],
[0,4,6,0,0,6,0,6,0,10,6,6],
[4,4,4,4,4,0,4,6,4,10,4,10],
[10,4,6,6,10,6,0,6,6,10,6,10],
[4,4,4,4,4,4,4,0,4,10,4,10],
[4,4,6,4,10,6,4,6,0,10,6,10],
[0,4,0,0,0,0,0,0,0,0,0,0],
[4,4,6,4,4,6,4,6,4,10,0,10],
[0,4,0,0,4,0,0,0,0,10,0,0]])


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
result = np.append(np.array([12, 9, 2, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 2, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 2, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 2, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,0,0,0,0,6,0,0,0,0,0,0],
[10,0,0,0,0,6,6,0,0,0,0,0],
[10,10,0,6,6,10,6,10,6,10,4,6],
[10,10,4,0,4,10,6,4,10,4,4,10],
[10,10,4,6,0,10,6,10,10,10,4,10],
[4,4,0,0,0,0,0,0,0,0,4,0],
[10,4,4,4,4,10,0,4,4,4,4,4],
[10,10,0,6,0,10,6,0,6,6,4,6],
[10,10,4,0,0,10,6,4,0,4,4,4],
[10,10,0,6,0,10,6,4,6,0,4,6],
[10,10,6,6,6,6,6,6,6,6,0,6],
[10,10,4,0,0,10,6,4,6,4,4,0]])


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
result = np.append(np.array([12, 9, 3, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 3, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 3, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 3, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,6,6,4,8,10,6,4,6,6,4],
[6,0,10,6,4,8,10,6,6,6,6,6],
[4,0,0,0,0,8,6,2,0,2,4,0],
[4,4,10,0,4,8,10,6,4,6,6,4],
[6,6,10,6,0,8,10,6,6,6,6,10],
[2,2,2,2,2,0,6,2,2,2,2,2],
[0,0,4,0,0,4,0,0,0,0,0,0],
[4,4,8,4,4,8,10,0,4,6,4,4],
[6,4,10,6,4,8,10,6,0,6,6,6],
[4,4,8,4,4,8,10,4,4,0,4,4],
[4,4,6,4,4,8,10,6,4,6,0,4],
[6,4,10,6,0,8,10,6,4,6,6,0]])


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
result = np.append(np.array([12, 9, 4, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 4, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 4, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 4, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,4,10,4,4,10,0,10,4,4,4,6],
[6,0,10,0,6,6,0,6,6,6,4,6],
[0,0,0,0,0,6,0,0,0,0,4,0],
[6,10,10,0,6,6,0,6,6,6,4,6],
[6,4,10,4,0,6,0,6,6,6,4,6],
[0,4,4,4,4,0,0,4,0,4,4,0],
[10,10,10,10,10,10,0,10,10,10,4,6],
[0,4,10,4,4,6,0,0,0,0,4,0],
[6,4,10,4,4,10,0,10,0,4,4,6],
[6,4,10,4,4,6,0,10,6,0,4,6],
[6,6,6,6,6,6,6,6,6,6,0,6],
[4,4,10,4,4,10,4,10,4,4,4,0]])


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
result = np.append(np.array([12, 9, 5, 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 5, 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 5, 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))


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
result = np.append(np.array([12, 9, 5, 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

 
pd.DataFrame(results12).to_csv("results12cr_azzini.csv")