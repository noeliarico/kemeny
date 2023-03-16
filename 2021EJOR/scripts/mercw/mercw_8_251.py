
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,122,115,111,109,122,122,124],
[129,0,141,124,117,126,129,119],
[136,110,0,119,100,124,135,121],
[140,127,132,0,124,137,133,135],
[142,134,151,127,0,129,135,123],
[129,125,127,114,122,0,143,130],
[129,122,116,118,116,108,0,129],
[127,132,130,116,128,121,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,124,114,125,117,119,128],
[135,0,119,143,126,125,117,134],
[127,132,0,131,125,138,124,124],
[137,108,120,0,111,116,120,119],
[126,125,126,140,0,128,127,149],
[134,126,113,135,123,0,119,120],
[132,134,127,131,124,132,0,133],
[123,117,127,132,102,131,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,114,108,121,128,129,133],
[131,0,120,124,128,128,130,120],
[137,131,0,136,129,123,139,133],
[143,127,115,0,123,124,131,136],
[130,123,122,128,0,127,131,133],
[123,123,128,127,124,0,134,145],
[122,121,112,120,120,117,0,119],
[118,131,118,115,118,106,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,120,141,117,126,137,129],
[137,0,123,121,153,141,112,151],
[131,128,0,143,135,148,120,139],
[110,130,108,0,113,123,117,130],
[134,98,116,138,0,115,112,115],
[125,110,103,128,136,0,124,130],
[114,139,131,134,139,127,0,154],
[122,100,112,121,136,121,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,122,135,118,133,123,155],
[124,0,129,125,126,132,118,143],
[129,122,0,128,117,117,115,140],
[116,126,123,0,120,133,119,128],
[133,125,134,131,0,133,132,128],
[118,119,134,118,118,0,127,137],
[128,133,136,132,119,124,0,141],
[96,108,111,123,123,114,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,142,125,142,128,133,107],
[138,0,150,157,158,147,135,121],
[109,101,0,105,120,123,95,99],
[126,94,146,0,121,124,116,111],
[109,93,131,130,0,105,90,108],
[123,104,128,127,146,0,114,104],
[118,116,156,135,161,137,0,134],
[144,130,152,140,143,147,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,118,129,138,112,120,134],
[123,0,151,112,105,122,117,123],
[133,100,0,127,121,118,108,134],
[122,139,124,0,124,122,136,121],
[113,146,130,127,0,134,123,142],
[139,129,133,129,117,0,138,136],
[131,134,143,115,128,113,0,142],
[117,128,117,130,109,115,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,120,120,105,131,121,125],
[144,0,133,133,125,141,134,134],
[131,118,0,119,120,128,121,129],
[131,118,132,0,122,136,121,126],
[146,126,131,129,0,143,118,139],
[120,110,123,115,108,0,122,128],
[130,117,130,130,133,129,0,134],
[126,117,122,125,112,123,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,133,114,127,133,127,134],
[129,0,138,113,118,126,119,154],
[118,113,0,110,106,120,110,124],
[137,138,141,0,122,132,133,143],
[124,133,145,129,0,135,120,147],
[118,125,131,119,116,0,122,129],
[124,132,141,118,131,129,0,143],
[117,97,127,108,104,122,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,121,123,140,117,114,125],
[134,0,113,125,133,124,126,138],
[130,138,0,134,137,138,109,135],
[128,126,117,0,128,123,107,124],
[111,118,114,123,0,111,95,117],
[134,127,113,128,140,0,114,140],
[137,125,142,144,156,137,0,139],
[126,113,116,127,134,111,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,131,142,140,121,126,124],
[110,0,90,99,122,114,116,120],
[120,161,0,149,139,136,115,135],
[109,152,102,0,126,103,116,126],
[111,129,112,125,0,102,104,105],
[130,137,115,148,149,0,137,155],
[125,135,136,135,147,114,0,134],
[127,131,116,125,146,96,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,117,129,143,118,133,106],
[110,0,69,97,43,120,92,91],
[134,182,0,143,122,148,120,142],
[122,154,108,0,79,126,67,99],
[108,208,129,172,0,156,94,107],
[133,131,103,125,95,0,115,100],
[118,159,131,184,157,136,0,135],
[145,160,109,152,144,151,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,120,107,112,125,122,123],
[132,0,122,116,135,120,137,126],
[131,129,0,120,138,127,139,136],
[144,135,131,0,131,127,146,124],
[139,116,113,120,0,120,136,140],
[126,131,124,124,131,0,144,131],
[129,114,112,105,115,107,0,113],
[128,125,115,127,111,120,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,160,129,117,145,117,129],
[100,0,132,110,92,108,98,113],
[91,119,0,125,142,108,128,130],
[122,141,126,0,100,132,130,106],
[134,159,109,151,0,153,144,159],
[106,143,143,119,98,0,128,112],
[134,153,123,121,107,123,0,136],
[122,138,121,145,92,139,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,101,125,136,126,118,137],
[119,0,126,128,117,120,110,118],
[150,125,0,132,139,138,132,154],
[126,123,119,0,144,113,121,140],
[115,134,112,107,0,123,114,137],
[125,131,113,138,128,0,106,121],
[133,141,119,130,137,145,0,154],
[114,133,97,111,114,130,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,117,131,124,117,121,116],
[139,0,135,122,149,122,130,133],
[134,116,0,127,133,128,130,128],
[120,129,124,0,120,109,110,127],
[127,102,118,131,0,111,123,120],
[134,129,123,142,140,0,121,134],
[130,121,121,141,128,130,0,125],
[135,118,123,124,131,117,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,130,124,138,136,124,137],
[121,0,111,118,133,135,117,137],
[121,140,0,118,135,118,122,129],
[127,133,133,0,148,123,132,129],
[113,118,116,103,0,132,113,108],
[115,116,133,128,119,0,110,121],
[127,134,129,119,138,141,0,140],
[114,114,122,122,143,130,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,122,123,126,120,128,131],
[124,0,123,137,116,115,131,136],
[129,128,0,140,117,125,123,124],
[128,114,111,0,125,110,124,108],
[125,135,134,126,0,127,137,136],
[131,136,126,141,124,0,140,127],
[123,120,128,127,114,111,0,122],
[120,115,127,143,115,124,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,137,116,137,124,124,153],
[133,0,144,140,135,133,110,146],
[114,107,0,107,120,117,120,129],
[135,111,144,0,140,116,123,134],
[114,116,131,111,0,123,119,123],
[127,118,134,135,128,0,126,169],
[127,141,131,128,132,125,0,140],
[98,105,122,117,128,82,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,128,120,132,104,113,139],
[143,0,119,131,152,141,127,162],
[123,132,0,155,142,141,142,156],
[131,120,96,0,143,136,121,132],
[119,99,109,108,0,90,114,134],
[147,110,110,115,161,0,113,145],
[138,124,109,130,137,138,0,163],
[112,89,95,119,117,106,88,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,125,133,124,126,153,124],
[104,0,125,146,126,123,135,123],
[126,126,0,116,118,124,134,120],
[118,105,135,0,122,113,113,116],
[127,125,133,129,0,115,138,123],
[125,128,127,138,136,0,136,140],
[98,116,117,138,113,115,0,116],
[127,128,131,135,128,111,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,147,124,109,134,124,130],
[133,0,132,129,106,110,114,128],
[104,119,0,120,93,113,110,122],
[127,122,131,0,101,127,122,134],
[142,145,158,150,0,125,156,143],
[117,141,138,124,126,0,149,148],
[127,137,141,129,95,102,0,132],
[121,123,129,117,108,103,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,139,123,126,120,143,135],
[119,0,134,128,131,127,127,124],
[112,117,0,120,110,113,127,124],
[128,123,131,0,133,122,137,134],
[125,120,141,118,0,115,137,128],
[131,124,138,129,136,0,135,134],
[108,124,124,114,114,116,0,126],
[116,127,127,117,123,117,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,117,110,121,122,124,123],
[124,0,133,125,121,125,127,136],
[134,118,0,132,128,128,130,150],
[141,126,119,0,134,136,130,125],
[130,130,123,117,0,134,126,137],
[129,126,123,115,117,0,121,129],
[127,124,121,121,125,130,0,134],
[128,115,101,126,114,122,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,158,130,115,119,114,110,132],
[93,0,101,89,101,83,92,109],
[121,150,0,136,126,122,115,134],
[136,162,115,0,149,129,138,152],
[132,150,125,102,0,109,120,130],
[137,168,129,122,142,0,130,133],
[141,159,136,113,131,121,0,129],
[119,142,117,99,121,118,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,132,136,129,126,141,115],
[127,0,165,131,118,176,100,145],
[119,86,0,127,89,100,133,76],
[115,120,124,0,87,120,110,97],
[122,133,162,164,0,173,117,135],
[125,75,151,131,78,0,120,117],
[110,151,118,141,134,131,0,114],
[136,106,175,154,116,134,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,157,127,118,158,143,121,179],
[94,0,62,100,135,120,137,157],
[124,189,0,137,120,173,151,211],
[133,151,114,0,162,135,135,176],
[93,116,131,89,0,116,122,139],
[108,131,78,116,135,0,163,193],
[130,114,100,116,129,88,0,141],
[72,94,40,75,112,58,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,116,124,113,121,127,117],
[126,0,126,119,109,111,121,118],
[135,125,0,120,116,110,122,121],
[127,132,131,0,123,122,146,137],
[138,142,135,128,0,120,131,129],
[130,140,141,129,131,0,131,123],
[124,130,129,105,120,120,0,122],
[134,133,130,114,122,128,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,121,135,128,148,132,126],
[118,0,151,150,114,136,129,124],
[130,100,0,129,112,123,116,124],
[116,101,122,0,106,119,106,95],
[123,137,139,145,0,140,128,127],
[103,115,128,132,111,0,94,116],
[119,122,135,145,123,157,0,128],
[125,127,127,156,124,135,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,126,122,131,136,121,123],
[150,0,130,124,140,139,146,138],
[125,121,0,117,123,127,116,129],
[129,127,134,0,143,131,120,119],
[120,111,128,108,0,136,115,126],
[115,112,124,120,115,0,119,128],
[130,105,135,131,136,132,0,124],
[128,113,122,132,125,123,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,45,95,158,113,140,18],
[140,0,45,95,158,95,140,158],
[206,206,0,95,158,113,140,113],
[156,156,156,0,158,113,251,63],
[93,93,93,93,0,188,188,93],
[138,156,138,138,63,0,138,156],
[111,111,111,0,63,113,0,18],
[233,93,138,188,158,95,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,118,117,138,125,127,124],
[123,0,131,124,139,137,134,135],
[133,120,0,117,131,126,128,119],
[134,127,134,0,131,141,130,123],
[113,112,120,120,0,128,116,113],
[126,114,125,110,123,0,126,119],
[124,117,123,121,135,125,0,120],
[127,116,132,128,138,132,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,126,133,133,133,133,128],
[130,0,125,131,120,121,141,119],
[125,126,0,125,129,127,134,126],
[118,120,126,0,133,133,141,124],
[118,131,122,118,0,125,130,120],
[118,130,124,118,126,0,145,125],
[118,110,117,110,121,106,0,120],
[123,132,125,127,131,126,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,144,127,130,138,122,120],
[121,0,130,139,135,155,121,136],
[107,121,0,131,126,131,136,123],
[124,112,120,0,149,138,106,122],
[121,116,125,102,0,127,94,100],
[113,96,120,113,124,0,85,96],
[129,130,115,145,157,166,0,140],
[131,115,128,129,151,155,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,97,93,127,166,103,129],
[181,0,87,88,122,149,93,124],
[154,164,0,199,97,167,164,177],
[158,163,52,0,144,119,151,99],
[124,129,154,107,0,80,124,85],
[85,102,84,132,171,0,60,134],
[148,158,87,100,127,191,0,80],
[122,127,74,152,166,117,171,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,77,152,132,150,89,96,156],
[174,0,187,181,166,125,172,201],
[99,64,0,125,122,123,131,115],
[119,70,126,0,143,95,123,128],
[101,85,129,108,0,118,88,164],
[162,126,128,156,133,0,119,219],
[155,79,120,128,163,132,0,179],
[95,50,136,123,87,32,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,123,145,143,135,144,145],
[111,0,119,141,127,114,136,129],
[128,132,0,135,112,133,133,136],
[106,110,116,0,118,118,113,130],
[108,124,139,133,0,122,141,123],
[116,137,118,133,129,0,133,127],
[107,115,118,138,110,118,0,122],
[106,122,115,121,128,124,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,135,120,152,134,143,160],
[123,0,152,135,146,147,151,162],
[116,99,0,119,147,114,119,137],
[131,116,132,0,148,128,146,143],
[99,105,104,103,0,123,111,120],
[117,104,137,123,128,0,111,148],
[108,100,132,105,140,140,0,134],
[91,89,114,108,131,103,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,129,129,118,119,124,130],
[121,0,121,109,110,113,120,131],
[122,130,0,121,129,111,134,130],
[122,142,130,0,128,123,128,127],
[133,141,122,123,0,131,134,134],
[132,138,140,128,120,0,130,146],
[127,131,117,123,117,121,0,134],
[121,120,121,124,117,105,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,124,133,127,135,114,129],
[128,0,120,112,126,138,117,124],
[127,131,0,111,128,136,125,128],
[118,139,140,0,132,133,130,138],
[124,125,123,119,0,134,118,129],
[116,113,115,118,117,0,120,130],
[137,134,126,121,133,131,0,126],
[122,127,123,113,122,121,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,144,148,131,113,138,148],
[115,0,128,130,124,104,136,86],
[107,123,0,118,107,119,111,114],
[103,121,133,0,99,120,102,99],
[120,127,144,152,0,120,141,118],
[138,147,132,131,131,0,114,126],
[113,115,140,149,110,137,0,130],
[103,165,137,152,133,125,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,113,121,129,141,113,99],
[109,0,119,116,121,127,120,105],
[138,132,0,143,139,127,142,121],
[130,135,108,0,125,137,132,117],
[122,130,112,126,0,111,121,128],
[110,124,124,114,140,0,126,102],
[138,131,109,119,130,125,0,95],
[152,146,130,134,123,149,156,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,121,138,138,112,129,137],
[100,0,114,115,128,118,113,125],
[130,137,0,108,123,127,104,141],
[113,136,143,0,127,118,130,136],
[113,123,128,124,0,118,126,142],
[139,133,124,133,133,0,140,143],
[122,138,147,121,125,111,0,137],
[114,126,110,115,109,108,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,133,117,140,182,148,141],
[122,0,150,118,123,160,138,164],
[118,101,0,109,138,127,136,108],
[134,133,142,0,111,148,134,91],
[111,128,113,140,0,148,162,137],
[69,91,124,103,103,0,116,75],
[103,113,115,117,89,135,0,145],
[110,87,143,160,114,176,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,109,101,122,100,102,121],
[136,0,116,102,120,124,116,105],
[142,135,0,123,123,137,138,136],
[150,149,128,0,129,139,143,124],
[129,131,128,122,0,137,130,129],
[151,127,114,112,114,0,123,131],
[149,135,113,108,121,128,0,126],
[130,146,115,127,122,120,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,121,117,114,125,126,133],
[116,0,109,127,122,121,111,129],
[130,142,0,131,123,132,116,135],
[134,124,120,0,112,117,103,133],
[137,129,128,139,0,125,122,142],
[126,130,119,134,126,0,122,136],
[125,140,135,148,129,129,0,141],
[118,122,116,118,109,115,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,116,117,133,121,118,135],
[131,0,125,137,133,126,126,123],
[135,126,0,125,134,126,127,123],
[134,114,126,0,124,131,118,131],
[118,118,117,127,0,127,120,127],
[130,125,125,120,124,0,123,139],
[133,125,124,133,131,128,0,121],
[116,128,128,120,124,112,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,122,137,110,127,114,126],
[131,0,116,126,112,137,132,126],
[129,135,0,144,113,148,138,154],
[114,125,107,0,105,132,102,114],
[141,139,138,146,0,153,119,134],
[124,114,103,119,98,0,108,107],
[137,119,113,149,132,143,0,134],
[125,125,97,137,117,144,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,167,138,136,123,189,155,126],
[84,0,83,107,114,149,110,35],
[113,168,0,191,140,184,177,111],
[115,144,60,0,104,192,138,104],
[128,137,111,147,0,150,158,104],
[62,102,67,59,101,0,75,42],
[96,141,74,113,93,176,0,48],
[125,216,140,147,147,209,203,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,132,116,109,129,147,119],
[116,0,118,116,121,127,119,118],
[119,133,0,125,133,130,139,135],
[135,135,126,0,133,129,134,120],
[142,130,118,118,0,127,136,126],
[122,124,121,122,124,0,136,122],
[104,132,112,117,115,115,0,115],
[132,133,116,131,125,129,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,123,123,115,105,117,124],
[129,0,133,120,128,116,113,142],
[128,118,0,126,110,107,111,123],
[128,131,125,0,119,109,116,122],
[136,123,141,132,0,134,127,147],
[146,135,144,142,117,0,128,137],
[134,138,140,135,124,123,0,133],
[127,109,128,129,104,114,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,151,147,168,78,79,105],
[137,0,213,229,205,135,133,100],
[100,38,0,111,111,59,133,100],
[104,22,140,0,172,50,79,100],
[83,46,140,79,0,51,103,79],
[173,116,192,201,200,0,164,194],
[172,118,118,172,148,87,0,115],
[146,151,151,151,172,57,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,121,178,165,132,155,158],
[102,0,128,182,146,129,129,146],
[130,123,0,158,147,121,106,156],
[73,69,93,0,106,106,88,76],
[86,105,104,145,0,123,105,111],
[119,122,130,145,128,0,119,164],
[96,122,145,163,146,132,0,139],
[93,105,95,175,140,87,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,123,133,133,136,135,144],
[108,0,118,139,114,111,115,122],
[128,133,0,130,132,140,101,124],
[118,112,121,0,106,100,112,124],
[118,137,119,145,0,131,135,111],
[115,140,111,151,120,0,108,114],
[116,136,150,139,116,143,0,126],
[107,129,127,127,140,137,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,128,140,119,135,130,120],
[111,0,112,120,88,120,105,96],
[123,139,0,114,128,126,153,133],
[111,131,137,0,129,140,126,130],
[132,163,123,122,0,137,159,116],
[116,131,125,111,114,0,134,111],
[121,146,98,125,92,117,0,134],
[131,155,118,121,135,140,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,107,122,113,112,116,115],
[130,0,116,125,117,107,122,123],
[144,135,0,127,146,125,139,134],
[129,126,124,0,132,118,135,128],
[138,134,105,119,0,123,131,123],
[139,144,126,133,128,0,142,124],
[135,129,112,116,120,109,0,108],
[136,128,117,123,128,127,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,95,170,146,132,119,126],
[136,0,103,167,141,145,104,127],
[156,148,0,185,143,153,125,155],
[81,84,66,0,101,118,78,111],
[105,110,108,150,0,140,127,101],
[119,106,98,133,111,0,94,110],
[132,147,126,173,124,157,0,154],
[125,124,96,140,150,141,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,129,134,132,127,137,125],
[118,0,121,133,134,116,128,129],
[122,130,0,138,124,130,139,126],
[117,118,113,0,123,126,115,125],
[119,117,127,128,0,113,118,120],
[124,135,121,125,138,0,143,134],
[114,123,112,136,133,108,0,131],
[126,122,125,126,131,117,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,116,89,106,127,96,80],
[142,0,142,93,121,129,109,137],
[135,109,0,98,135,136,114,107],
[162,158,153,0,140,145,121,127],
[145,130,116,111,0,111,93,121],
[124,122,115,106,140,0,127,131],
[155,142,137,130,158,124,0,151],
[171,114,144,124,130,120,100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,123,132,145,116,156,141],
[107,0,94,122,143,99,137,111],
[128,157,0,124,146,137,152,142],
[119,129,127,0,118,91,112,119],
[106,108,105,133,0,72,120,106],
[135,152,114,160,179,0,161,133],
[95,114,99,139,131,90,0,128],
[110,140,109,132,145,118,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,134,152,114,130,145,121],
[128,0,123,152,137,147,136,133],
[117,128,0,132,136,139,137,140],
[99,99,119,0,93,99,117,120],
[137,114,115,158,0,141,131,130],
[121,104,112,152,110,0,114,129],
[106,115,114,134,120,137,0,122],
[130,118,111,131,121,122,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,110,96,117,113,92,119],
[149,0,116,129,137,124,138,149],
[141,135,0,124,142,129,130,144],
[155,122,127,0,155,143,136,147],
[134,114,109,96,0,114,110,132],
[138,127,122,108,137,0,129,128],
[159,113,121,115,141,122,0,133],
[132,102,107,104,119,123,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,130,127,131,121,141,118],
[116,0,128,124,134,119,135,125],
[121,123,0,122,131,124,130,119],
[124,127,129,0,133,122,130,126],
[120,117,120,118,0,121,122,114],
[130,132,127,129,130,0,136,124],
[110,116,121,121,129,115,0,117],
[133,126,132,125,137,127,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,120,122,109,117,118,108],
[126,0,133,113,126,101,128,97],
[131,118,0,106,128,106,130,119],
[129,138,145,0,126,116,151,105],
[142,125,123,125,0,128,127,118],
[134,150,145,135,123,0,136,150],
[133,123,121,100,124,115,0,91],
[143,154,132,146,133,101,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,115,124,113,128,132,124],
[128,0,124,124,128,138,137,124],
[136,127,0,121,130,136,124,126],
[127,127,130,0,126,118,118,117],
[138,123,121,125,0,122,116,121],
[123,113,115,133,129,0,124,133],
[119,114,127,133,135,127,0,132],
[127,127,125,134,130,118,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,145,130,143,146,142,125],
[110,0,139,118,133,143,130,127],
[106,112,0,95,134,123,109,126],
[121,133,156,0,131,141,118,149],
[108,118,117,120,0,138,129,105],
[105,108,128,110,113,0,110,123],
[109,121,142,133,122,141,0,113],
[126,124,125,102,146,128,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,149,128,121,120,130,148],
[123,0,124,143,131,113,111,124],
[102,127,0,144,118,117,117,131],
[123,108,107,0,96,119,115,134],
[130,120,133,155,0,125,137,120],
[131,138,134,132,126,0,114,148],
[121,140,134,136,114,137,0,161],
[103,127,120,117,131,103,90,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,136,117,135,157,130,124],
[107,0,116,102,97,133,114,109],
[115,135,0,126,123,145,140,126],
[134,149,125,0,123,147,139,134],
[116,154,128,128,0,151,129,127],
[94,118,106,104,100,0,122,126],
[121,137,111,112,122,129,0,125],
[127,142,125,117,124,125,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,127,117,120,124,109,117],
[140,0,131,123,126,122,119,120],
[124,120,0,126,120,123,120,113],
[134,128,125,0,131,134,127,131],
[131,125,131,120,0,126,119,125],
[127,129,128,117,125,0,121,120],
[142,132,131,124,132,130,0,117],
[134,131,138,120,126,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,138,143,138,118,132,126],
[124,0,130,133,133,114,139,119],
[113,121,0,129,126,113,120,119],
[108,118,122,0,122,111,127,114],
[113,118,125,129,0,118,137,125],
[133,137,138,140,133,0,146,122],
[119,112,131,124,114,105,0,109],
[125,132,132,137,126,129,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,139,95,134,115,115,136],
[129,0,134,132,124,125,107,133],
[112,117,0,124,112,116,112,128],
[156,119,127,0,114,113,117,135],
[117,127,139,137,0,128,131,142],
[136,126,135,138,123,0,117,137],
[136,144,139,134,120,134,0,133],
[115,118,123,116,109,114,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,116,136,113,121,116,124],
[130,0,119,132,121,130,126,125],
[135,132,0,131,115,124,122,126],
[115,119,120,0,119,118,117,125],
[138,130,136,132,0,124,131,140],
[130,121,127,133,127,0,130,130],
[135,125,129,134,120,121,0,137],
[127,126,125,126,111,121,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,115,112,146,125,110,114],
[103,0,134,99,137,100,94,87],
[136,117,0,96,151,147,116,106],
[139,152,155,0,162,140,119,172],
[105,114,100,89,0,111,84,98],
[126,151,104,111,140,0,138,117],
[141,157,135,132,167,113,0,148],
[137,164,145,79,153,134,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,137,112,124,112,116,105],
[127,0,129,133,159,121,139,97],
[114,122,0,123,135,149,114,116],
[139,118,128,0,130,117,121,106],
[127,92,116,121,0,106,113,99],
[139,130,102,134,145,0,121,136],
[135,112,137,130,138,130,0,108],
[146,154,135,145,152,115,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,89,178,137,131,107,154],
[138,0,107,185,145,83,125,172],
[162,144,0,209,192,119,154,174],
[73,66,42,0,115,72,90,60],
[114,106,59,136,0,89,131,154],
[120,168,132,179,162,0,125,162],
[144,126,97,161,120,126,0,144],
[97,79,77,191,97,89,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,138,131,123,121,123,127],
[145,0,150,127,128,126,119,135],
[113,101,0,119,119,128,110,102],
[120,124,132,0,118,121,121,108],
[128,123,132,133,0,135,107,115],
[130,125,123,130,116,0,107,113],
[128,132,141,130,144,144,0,119],
[124,116,149,143,136,138,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,100,118,98,106,105,131],
[153,0,116,150,128,139,129,159],
[151,135,0,124,121,146,115,134],
[133,101,127,0,117,136,95,119],
[153,123,130,134,0,133,119,150],
[145,112,105,115,118,0,109,157],
[146,122,136,156,132,142,0,161],
[120,92,117,132,101,94,90,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,109,77,111,114,103,94],
[146,0,144,142,116,131,136,110],
[142,107,0,129,127,113,127,100],
[174,109,122,0,130,114,132,146],
[140,135,124,121,0,123,140,122],
[137,120,138,137,128,0,118,116],
[148,115,124,119,111,133,0,112],
[157,141,151,105,129,135,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,122,132,113,133,116,139],
[130,0,119,139,135,136,131,124],
[129,132,0,143,138,154,116,134],
[119,112,108,0,120,133,113,126],
[138,116,113,131,0,130,121,117],
[118,115,97,118,121,0,110,105],
[135,120,135,138,130,141,0,134],
[112,127,117,125,134,146,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,155,131,139,58,107,97],
[187,0,197,143,177,146,139,101],
[96,54,0,98,88,77,88,31],
[120,108,153,0,118,80,113,71],
[112,74,163,133,0,97,117,96],
[193,105,174,171,154,0,160,137],
[144,112,163,138,134,91,0,99],
[154,150,220,180,155,114,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,119,129,132,121,129,123],
[119,0,120,122,131,124,127,124],
[132,131,0,128,132,117,145,127],
[122,129,123,0,130,129,132,113],
[119,120,119,121,0,128,147,124],
[130,127,134,122,123,0,139,120],
[122,124,106,119,104,112,0,104],
[128,127,124,138,127,131,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,152,126,126,159,122,113],
[115,0,124,120,116,156,114,119],
[99,127,0,115,110,139,106,108],
[125,131,136,0,118,157,135,128],
[125,135,141,133,0,165,121,139],
[92,95,112,94,86,0,95,97],
[129,137,145,116,130,156,0,145],
[138,132,143,123,112,154,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,125,102,119,115,106,136],
[131,0,119,114,130,128,125,150],
[126,132,0,125,134,129,130,128],
[149,137,126,0,138,122,138,143],
[132,121,117,113,0,133,123,126],
[136,123,122,129,118,0,136,132],
[145,126,121,113,128,115,0,136],
[115,101,123,108,125,119,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,104,119,95,98,117,117],
[144,0,119,138,127,128,122,127],
[147,132,0,125,120,145,140,133],
[132,113,126,0,111,123,109,131],
[156,124,131,140,0,132,139,138],
[153,123,106,128,119,0,125,118],
[134,129,111,142,112,126,0,124],
[134,124,118,120,113,133,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,131,127,115,130,117,122],
[128,0,123,134,130,127,127,124],
[120,128,0,127,120,120,127,127],
[124,117,124,0,121,132,118,118],
[136,121,131,130,0,135,123,131],
[121,124,131,119,116,0,120,116],
[134,124,124,133,128,131,0,121],
[129,127,124,133,120,135,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,156,125,156,139,141,133],
[107,0,155,145,153,130,149,122],
[95,96,0,125,122,123,138,123],
[126,106,126,0,121,139,153,122],
[95,98,129,130,0,116,132,120],
[112,121,128,112,135,0,163,143],
[110,102,113,98,119,88,0,91],
[118,129,128,129,131,108,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,145,133,137,133,131,124],
[136,0,129,131,131,121,124,128],
[106,122,0,115,120,128,121,125],
[118,120,136,0,122,129,129,130],
[114,120,131,129,0,131,118,126],
[118,130,123,122,120,0,127,112],
[120,127,130,122,133,124,0,132],
[127,123,126,121,125,139,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,141,124,119,130,126,123],
[128,0,137,119,138,112,116,121],
[110,114,0,107,114,116,108,105],
[127,132,144,0,125,137,123,133],
[132,113,137,126,0,128,109,109],
[121,139,135,114,123,0,123,131],
[125,135,143,128,142,128,0,122],
[128,130,146,118,142,120,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,121,136,132,135,119,118],
[111,0,112,141,117,114,121,108],
[130,139,0,135,124,137,126,124],
[115,110,116,0,116,102,108,117],
[119,134,127,135,0,137,132,133],
[116,137,114,149,114,0,125,119],
[132,130,125,143,119,126,0,118],
[133,143,127,134,118,132,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,120,133,158,121,118,134],
[146,0,112,142,154,135,118,145],
[131,139,0,141,146,133,116,145],
[118,109,110,0,155,125,115,129],
[93,97,105,96,0,112,100,133],
[130,116,118,126,139,0,142,131],
[133,133,135,136,151,109,0,137],
[117,106,106,122,118,120,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,122,115,135,124,121,117],
[125,0,124,125,138,139,108,107],
[129,127,0,123,125,131,122,123],
[136,126,128,0,147,133,137,118],
[116,113,126,104,0,125,110,109],
[127,112,120,118,126,0,120,118],
[130,143,129,114,141,131,0,129],
[134,144,128,133,142,133,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,99,129,116,121,119,142],
[110,0,113,134,111,120,122,120],
[152,138,0,153,114,133,142,143],
[122,117,98,0,99,108,120,115],
[135,140,137,152,0,120,150,148],
[130,131,118,143,131,0,138,142],
[132,129,109,131,101,113,0,127],
[109,131,108,136,103,109,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,117,138,123,131,128,121],
[119,0,127,125,126,125,137,128],
[134,124,0,137,132,132,139,134],
[113,126,114,0,120,131,125,118],
[128,125,119,131,0,132,134,127],
[120,126,119,120,119,0,133,130],
[123,114,112,126,117,118,0,123],
[130,123,117,133,124,121,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,134,122,124,127,125,119],
[121,0,121,121,121,133,127,123],
[117,130,0,119,123,125,137,135],
[129,130,132,0,119,135,136,122],
[127,130,128,132,0,129,140,124],
[124,118,126,116,122,0,131,107],
[126,124,114,115,111,120,0,119],
[132,128,116,129,127,144,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,101,138,116,135,131,119],
[112,0,104,131,108,132,119,122],
[150,147,0,125,149,167,149,134],
[113,120,126,0,133,132,125,106],
[135,143,102,118,0,129,164,116],
[116,119,84,119,122,0,133,92],
[120,132,102,126,87,118,0,104],
[132,129,117,145,135,159,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,116,127,130,120,114,126],
[141,0,129,141,140,121,139,127],
[135,122,0,136,127,135,117,112],
[124,110,115,0,125,113,126,106],
[121,111,124,126,0,139,121,115],
[131,130,116,138,112,0,121,123],
[137,112,134,125,130,130,0,125],
[125,124,139,145,136,128,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,144,134,128,122,106,130],
[151,0,184,147,131,140,153,106],
[107,67,0,148,120,102,141,76],
[117,104,103,0,121,87,99,103],
[123,120,131,130,0,122,137,108],
[129,111,149,164,129,0,116,120],
[145,98,110,152,114,135,0,129],
[121,145,175,148,143,131,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,122,124,118,128,117,115],
[139,0,138,123,132,133,133,131],
[129,113,0,116,116,136,134,124],
[127,128,135,0,118,137,129,128],
[133,119,135,133,0,144,131,124],
[123,118,115,114,107,0,123,123],
[134,118,117,122,120,128,0,118],
[136,120,127,123,127,128,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,124,118,133,121,134,131],
[115,0,114,126,134,128,126,128],
[127,137,0,129,124,133,142,137],
[133,125,122,0,141,131,132,128],
[118,117,127,110,0,123,134,131],
[130,123,118,120,128,0,124,130],
[117,125,109,119,117,127,0,127],
[120,123,114,123,120,121,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,112,116,136,109,115,127],
[127,0,129,115,133,131,129,121],
[139,122,0,131,136,122,123,131],
[135,136,120,0,131,124,117,124],
[115,118,115,120,0,114,119,120],
[142,120,129,127,137,0,124,137],
[136,122,128,134,132,127,0,133],
[124,130,120,127,131,114,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,126,106,107,133,110,108],
[132,0,136,124,132,132,107,117],
[125,115,0,112,91,118,100,108],
[145,127,139,0,127,121,127,113],
[144,119,160,124,0,145,115,114],
[118,119,133,130,106,0,123,118],
[141,144,151,124,136,128,0,132],
[143,134,143,138,137,133,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,124,141,134,143,135,142],
[123,0,126,127,144,136,130,115],
[127,125,0,120,135,124,130,113],
[110,124,131,0,123,143,129,105],
[117,107,116,128,0,124,132,122],
[108,115,127,108,127,0,130,122],
[116,121,121,122,119,121,0,110],
[109,136,138,146,129,129,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,157,114,151,125,171,151],
[127,0,138,124,109,128,151,133],
[94,113,0,104,106,109,139,112],
[137,127,147,0,134,122,149,152],
[100,142,145,117,0,131,158,124],
[126,123,142,129,120,0,155,150],
[80,100,112,102,93,96,0,108],
[100,118,139,99,127,101,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,113,124,127,123,142,141],
[105,0,108,94,113,107,103,116],
[138,143,0,124,124,130,134,131],
[127,157,127,0,140,120,139,145],
[124,138,127,111,0,115,128,143],
[128,144,121,131,136,0,127,138],
[109,148,117,112,123,124,0,135],
[110,135,120,106,108,113,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,126,135,135,129,123,130],
[121,0,128,129,134,119,123,124],
[125,123,0,127,136,125,118,132],
[116,122,124,0,142,119,122,127],
[116,117,115,109,0,121,115,118],
[122,132,126,132,130,0,128,123],
[128,128,133,129,136,123,0,133],
[121,127,119,124,133,128,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,121,110,121,118,116,121],
[145,0,137,141,124,127,119,118],
[130,114,0,114,129,114,111,114],
[141,110,137,0,128,122,136,126],
[130,127,122,123,0,123,109,102],
[133,124,137,129,128,0,128,114],
[135,132,140,115,142,123,0,121],
[130,133,137,125,149,137,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,132,137,122,131,151,145],
[125,0,130,131,135,129,143,145],
[119,121,0,129,133,124,136,134],
[114,120,122,0,130,132,139,127],
[129,116,118,121,0,133,135,122],
[120,122,127,119,118,0,133,129],
[100,108,115,112,116,118,0,133],
[106,106,117,124,129,122,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,116,98,89,101,98,158],
[152,0,141,115,120,126,114,147],
[135,110,0,134,111,119,122,138],
[153,136,117,0,112,111,133,166],
[162,131,140,139,0,122,122,141],
[150,125,132,140,129,0,121,140],
[153,137,129,118,129,130,0,156],
[93,104,113,85,110,111,95,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,133,123,134,129,144,117],
[121,0,139,111,114,128,133,125],
[118,112,0,114,114,115,117,109],
[128,140,137,0,122,134,131,131],
[117,137,137,129,0,134,130,129],
[122,123,136,117,117,0,130,110],
[107,118,134,120,121,121,0,111],
[134,126,142,120,122,141,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,115,121,125,115,121,123],
[125,0,111,118,121,116,127,130],
[136,140,0,124,141,134,137,142],
[130,133,127,0,128,120,128,134],
[126,130,110,123,0,128,108,124],
[136,135,117,131,123,0,128,133],
[130,124,114,123,143,123,0,125],
[128,121,109,117,127,118,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,159,106,127,116,159,151],
[125,0,178,133,135,161,170,155],
[92,73,0,98,73,73,93,100],
[145,118,153,0,97,101,130,117],
[124,116,178,154,0,134,170,157],
[135,90,178,150,117,0,147,143],
[92,81,158,121,81,104,0,155],
[100,96,151,134,94,108,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,124,135,128,127,125],
[124,0,126,128,128,137,124,123],
[128,125,0,128,140,130,132,133],
[127,123,123,0,122,121,120,126],
[116,123,111,129,0,115,119,115],
[123,114,121,130,136,0,130,127],
[124,127,119,131,132,121,0,125],
[126,128,118,125,136,124,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,107,111,110,151,132,180],
[135,0,135,145,63,122,134,144],
[144,116,0,123,86,129,93,136],
[140,106,128,0,100,91,97,174],
[141,188,165,151,0,149,107,121],
[100,129,122,160,102,0,109,166],
[119,117,158,154,144,142,0,160],
[71,107,115,77,130,85,91,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,136,129,128,122,127,121],
[134,0,145,150,134,125,120,137],
[115,106,0,122,114,130,116,126],
[122,101,129,0,123,130,115,125],
[123,117,137,128,0,129,108,129],
[129,126,121,121,122,0,121,120],
[124,131,135,136,143,130,0,139],
[130,114,125,126,122,131,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,117,141,125,135,121,128],
[122,0,118,132,130,137,122,126],
[134,133,0,139,135,143,127,124],
[110,119,112,0,130,126,121,124],
[126,121,116,121,0,137,117,128],
[116,114,108,125,114,0,116,116],
[130,129,124,130,134,135,0,139],
[123,125,127,127,123,135,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,161,135,85,151,187,187,144],
[90,0,155,115,158,176,85,64],
[116,96,0,32,103,113,134,84],
[166,136,219,0,205,171,112,88],
[100,93,148,46,0,60,65,53],
[64,75,138,80,191,0,75,87],
[64,166,117,139,186,176,0,142],
[107,187,167,163,198,164,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,111,125,132,118,118,125],
[133,0,133,115,133,120,118,121],
[140,118,0,119,126,125,127,130],
[126,136,132,0,130,132,114,121],
[119,118,125,121,0,126,115,107],
[133,131,126,119,125,0,123,124],
[133,133,124,137,136,128,0,125],
[126,130,121,130,144,127,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,112,122,137,122,142,108],
[123,0,124,117,135,127,128,125],
[139,127,0,123,135,139,128,123],
[129,134,128,0,102,120,125,107],
[114,116,116,149,0,115,138,113],
[129,124,112,131,136,0,148,127],
[109,123,123,126,113,103,0,113],
[143,126,128,144,138,124,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,194,165,172,140,125,144],
[107,0,144,125,168,134,126,131],
[57,107,0,118,122,115,90,107],
[86,126,133,0,132,111,93,119],
[79,83,129,119,0,111,114,127],
[111,117,136,140,140,0,94,116],
[126,125,161,158,137,157,0,123],
[107,120,144,132,124,135,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,124,123,126,125,133,141],
[132,0,143,124,137,128,137,143],
[127,108,0,126,125,117,127,133],
[128,127,125,0,132,116,127,141],
[125,114,126,119,0,116,117,123],
[126,123,134,135,135,0,139,138],
[118,114,124,124,134,112,0,133],
[110,108,118,110,128,113,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,87,100,104,130,146,107],
[133,0,108,114,122,166,151,137],
[164,143,0,97,100,151,137,134],
[151,137,154,0,130,170,179,113],
[147,129,151,121,0,183,140,114],
[121,85,100,81,68,0,127,95],
[105,100,114,72,111,124,0,138],
[144,114,117,138,137,156,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,126,122,90,153,129,93],
[132,0,115,203,166,167,153,138],
[125,136,0,168,122,183,143,96],
[129,48,83,0,104,75,105,45],
[161,85,129,147,0,153,123,121],
[98,84,68,176,98,0,144,109],
[122,98,108,146,128,107,0,73],
[158,113,155,206,130,142,178,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,149,151,126,125,136,131],
[112,0,130,127,129,129,138,125],
[102,121,0,119,127,114,121,123],
[100,124,132,0,122,114,128,117],
[125,122,124,129,0,110,135,119],
[126,122,137,137,141,0,139,134],
[115,113,130,123,116,112,0,119],
[120,126,128,134,132,117,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,141,134,132,164,125,124],
[117,0,142,113,114,119,119,104],
[110,109,0,124,99,127,108,126],
[117,138,127,0,105,120,120,102],
[119,137,152,146,0,148,123,130],
[87,132,124,131,103,0,118,127],
[126,132,143,131,128,133,0,114],
[127,147,125,149,121,124,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,84,112,109,91,98,129],
[149,0,125,140,132,112,115,142],
[167,126,0,140,136,115,148,145],
[139,111,111,0,130,132,147,142],
[142,119,115,121,0,126,121,125],
[160,139,136,119,125,0,133,148],
[153,136,103,104,130,118,0,113],
[122,109,106,109,126,103,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,122,132,119,125,129,120],
[111,0,108,114,120,98,119,115],
[129,143,0,128,129,119,133,130],
[119,137,123,0,128,118,126,124],
[132,131,122,123,0,114,120,110],
[126,153,132,133,137,0,136,119],
[122,132,118,125,131,115,0,121],
[131,136,121,127,141,132,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,192,184,121,156,118,177],
[101,0,197,102,149,174,137,150],
[59,54,0,41,130,84,116,113],
[67,149,210,0,125,124,124,186],
[130,102,121,126,0,115,125,145],
[95,77,167,127,136,0,121,129],
[133,114,135,127,126,130,0,170],
[74,101,138,65,106,122,81,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,138,115,122,121,121,148],
[123,0,132,133,125,141,135,140],
[113,119,0,140,123,124,107,141],
[136,118,111,0,109,119,118,117],
[129,126,128,142,0,147,114,142],
[130,110,127,132,104,0,102,120],
[130,116,144,133,137,149,0,155],
[103,111,110,134,109,131,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,132,118,125,140,131,154],
[127,0,134,115,126,131,126,143],
[119,117,0,119,132,129,129,131],
[133,136,132,0,125,145,129,148],
[126,125,119,126,0,131,118,146],
[111,120,122,106,120,0,125,128],
[120,125,122,122,133,126,0,131],
[97,108,120,103,105,123,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,108,118,97,111,101,109],
[137,0,135,113,115,136,122,122],
[143,116,0,130,130,135,116,123],
[133,138,121,0,115,121,130,125],
[154,136,121,136,0,139,131,128],
[140,115,116,130,112,0,111,114],
[150,129,135,121,120,140,0,145],
[142,129,128,126,123,137,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,183,187,96,95,150,89],
[120,0,210,171,154,154,195,186],
[68,41,0,42,38,88,37,33],
[64,80,209,0,100,114,108,97],
[155,97,213,151,0,150,150,122],
[156,97,163,137,101,0,90,125],
[101,56,214,143,101,161,0,116],
[162,65,218,154,129,126,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,138,137,143,148,114,128],
[121,0,127,118,134,155,142,137],
[113,124,0,126,126,118,125,128],
[114,133,125,0,110,152,123,141],
[108,117,125,141,0,128,127,107],
[103,96,133,99,123,0,109,129],
[137,109,126,128,124,142,0,125],
[123,114,123,110,144,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,123,150,155,128,153,126],
[113,0,117,128,139,132,129,121],
[128,134,0,147,144,118,146,123],
[101,123,104,0,137,117,125,110],
[96,112,107,114,0,117,119,107],
[123,119,133,134,134,0,140,133],
[98,122,105,126,132,111,0,125],
[125,130,128,141,144,118,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,115,111,123,120,116,117],
[131,0,115,123,123,122,137,133],
[136,136,0,123,127,132,123,128],
[140,128,128,0,127,123,123,135],
[128,128,124,124,0,126,115,129],
[131,129,119,128,125,0,128,125],
[135,114,128,128,136,123,0,124],
[134,118,123,116,122,126,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,40,103,40,0,65,188],
[251,0,105,143,145,103,128,188],
[211,146,0,103,143,106,128,251],
[148,108,148,0,148,83,65,148],
[211,106,108,103,0,106,128,211],
[251,148,145,168,145,0,65,188],
[186,123,123,186,123,186,0,123],
[63,63,0,103,40,63,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,160,136,135,129,151,151,115],
[91,0,113,86,92,114,89,88],
[115,138,0,98,70,138,130,120],
[116,165,153,0,126,148,132,123],
[122,159,181,125,0,162,132,153],
[100,137,113,103,89,0,101,93],
[100,162,121,119,119,150,0,118],
[136,163,131,128,98,158,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,155,163,111,131,118,145],
[108,0,119,141,84,113,100,143],
[96,132,0,128,133,103,157,118],
[88,110,123,0,79,110,121,99],
[140,167,118,172,0,120,170,160],
[120,138,148,141,131,0,156,97],
[133,151,94,130,81,95,0,109],
[106,108,133,152,91,154,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,84,123,123,110,124,135,133],
[167,0,115,132,139,170,140,145],
[128,136,0,116,125,140,133,121],
[128,119,135,0,114,161,125,103],
[141,112,126,137,0,147,149,155],
[127,81,111,90,104,0,135,118],
[116,111,118,126,102,116,0,121],
[118,106,130,148,96,133,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,124,124,124,125,132,130],
[116,0,119,103,111,112,122,113],
[127,132,0,109,132,122,140,133],
[127,148,142,0,134,130,139,116],
[127,140,119,117,0,130,139,131],
[126,139,129,121,121,0,139,120],
[119,129,111,112,112,112,0,111],
[121,138,118,135,120,131,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,86,97,89,101,88,142],
[141,0,106,121,117,100,143,153],
[165,145,0,128,126,137,116,138],
[154,130,123,0,127,133,128,147],
[162,134,125,124,0,132,135,145],
[150,151,114,118,119,0,137,124],
[163,108,135,123,116,114,0,136],
[109,98,113,104,106,127,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,124,136,128,139,136,138],
[122,0,134,127,119,127,133,126],
[127,117,0,129,114,135,125,120],
[115,124,122,0,120,135,118,128],
[123,132,137,131,0,133,130,140],
[112,124,116,116,118,0,116,130],
[115,118,126,133,121,135,0,127],
[113,125,131,123,111,121,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,139,132,163,123,147,92],
[131,0,136,119,170,115,144,108],
[112,115,0,113,162,107,93,117],
[119,132,138,0,173,128,144,127],
[88,81,89,78,0,92,109,103],
[128,136,144,123,159,0,94,113],
[104,107,158,107,142,157,0,111],
[159,143,134,124,148,138,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,55,76,143,129,46,93],
[206,0,75,145,192,206,131,115],
[196,176,0,123,210,196,184,93],
[175,106,128,0,143,195,143,166],
[108,59,41,108,0,218,128,98],
[122,45,55,56,33,0,26,66],
[205,120,67,108,123,225,0,85],
[158,136,158,85,153,185,166,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,154,132,138,137,147,126],
[129,0,135,125,138,127,141,125],
[97,116,0,124,133,126,130,113],
[119,126,127,0,124,101,129,123],
[113,113,118,127,0,145,126,121],
[114,124,125,150,106,0,141,126],
[104,110,121,122,125,110,0,118],
[125,126,138,128,130,125,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,109,122,150,136,131,127],
[116,0,115,97,111,124,125,107],
[142,136,0,123,150,170,166,128],
[129,154,128,0,135,147,139,118],
[101,140,101,116,0,122,136,125],
[115,127,81,104,129,0,117,110],
[120,126,85,112,115,134,0,110],
[124,144,123,133,126,141,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,132,100,114,119,125,117],
[135,0,124,108,140,137,113,150],
[119,127,0,139,137,135,132,161],
[151,143,112,0,140,150,129,161],
[137,111,114,111,0,140,129,123],
[132,114,116,101,111,0,120,140],
[126,138,119,122,122,131,0,139],
[134,101,90,90,128,111,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,122,130,135,127,138,128],
[127,0,120,127,117,119,134,118],
[129,131,0,123,125,140,143,119],
[121,124,128,0,122,126,126,117],
[116,134,126,129,0,135,144,121],
[124,132,111,125,116,0,137,115],
[113,117,108,125,107,114,0,118],
[123,133,132,134,130,136,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,111,121,126,127,121,136],
[131,0,121,108,104,125,115,134],
[140,130,0,124,121,154,117,142],
[130,143,127,0,158,129,124,166],
[125,147,130,93,0,122,133,142],
[124,126,97,122,129,0,136,139],
[130,136,134,127,118,115,0,134],
[115,117,109,85,109,112,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,150,136,125,133,121,120],
[121,0,131,139,125,116,124,113],
[101,120,0,136,111,98,109,102],
[115,112,115,0,118,96,111,116],
[126,126,140,133,0,133,121,133],
[118,135,153,155,118,0,124,128],
[130,127,142,140,130,127,0,120],
[131,138,149,135,118,123,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,131,155,141,113,137,125],
[120,0,123,143,141,111,128,137],
[120,128,0,153,148,134,129,120],
[96,108,98,0,128,96,118,103],
[110,110,103,123,0,109,127,105],
[138,140,117,155,142,0,136,124],
[114,123,122,133,124,115,0,121],
[126,114,131,148,146,127,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,95,94,114,95,127,116],
[117,0,105,101,119,122,128,107],
[156,146,0,127,117,135,163,155],
[157,150,124,0,138,146,141,130],
[137,132,134,113,0,133,160,136],
[156,129,116,105,118,0,138,153],
[124,123,88,110,91,113,0,100],
[135,144,96,121,115,98,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,92,95,104,101,145,95,90],
[159,0,140,160,124,149,159,127],
[156,111,0,133,146,132,130,150],
[147,91,118,0,126,128,137,132],
[150,127,105,125,0,148,114,137],
[106,102,119,123,103,0,110,116],
[156,92,121,114,137,141,0,133],
[161,124,101,119,114,135,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,114,129,141,148,140,128],
[111,0,133,112,121,119,133,132],
[137,118,0,123,116,141,115,133],
[122,139,128,0,138,149,156,129],
[110,130,135,113,0,140,130,144],
[103,132,110,102,111,0,133,126],
[111,118,136,95,121,118,0,141],
[123,119,118,122,107,125,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,144,123,132,167,137,131],
[129,0,100,137,139,123,96,79],
[107,151,0,150,120,137,146,134],
[128,114,101,0,107,130,120,116],
[119,112,131,144,0,157,144,93],
[84,128,114,121,94,0,136,116],
[114,155,105,131,107,115,0,135],
[120,172,117,135,158,135,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,142,125,123,149,130,135],
[119,0,117,131,145,137,122,142],
[109,134,0,108,109,134,105,128],
[126,120,143,0,132,151,128,137],
[128,106,142,119,0,113,115,127],
[102,114,117,100,138,0,118,126],
[121,129,146,123,136,133,0,140],
[116,109,123,114,124,125,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,128,140,121,128,125,121],
[119,0,118,132,117,121,115,130],
[123,133,0,134,128,126,134,132],
[111,119,117,0,114,121,119,122],
[130,134,123,137,0,121,124,129],
[123,130,125,130,130,0,119,130],
[126,136,117,132,127,132,0,120],
[130,121,119,129,122,121,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,122,134,120,126,127,130],
[123,0,144,145,136,139,133,139],
[129,107,0,114,124,109,115,130],
[117,106,137,0,145,116,131,137],
[131,115,127,106,0,119,126,132],
[125,112,142,135,132,0,133,151],
[124,118,136,120,125,118,0,121],
[121,112,121,114,119,100,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,145,130,130,112,119,128],
[123,0,136,148,126,136,157,134],
[106,115,0,121,117,106,129,123],
[121,103,130,0,120,103,151,132],
[121,125,134,131,0,116,135,115],
[139,115,145,148,135,0,153,148],
[132,94,122,100,116,98,0,116],
[123,117,128,119,136,103,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,148,127,138,136,121,141],
[124,0,116,134,136,120,126,139],
[103,135,0,137,138,120,124,131],
[124,117,114,0,136,115,129,126],
[113,115,113,115,0,125,115,140],
[115,131,131,136,126,0,111,133],
[130,125,127,122,136,140,0,137],
[110,112,120,125,111,118,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,142,130,135,122,109,148],
[105,0,110,102,104,110,96,120],
[109,141,0,119,139,124,119,141],
[121,149,132,0,127,144,120,113],
[116,147,112,124,0,129,135,139],
[129,141,127,107,122,0,118,120],
[142,155,132,131,116,133,0,132],
[103,131,110,138,112,131,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,110,136,129,143,133,129],
[137,0,129,122,148,136,150,138],
[141,122,0,135,134,148,147,126],
[115,129,116,0,134,140,132,151],
[122,103,117,117,0,132,133,129],
[108,115,103,111,119,0,123,121],
[118,101,104,119,118,128,0,116],
[122,113,125,100,122,130,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,148,138,134,137,121,141],
[112,0,120,126,129,139,120,115],
[103,131,0,121,119,118,112,106],
[113,125,130,0,120,129,115,121],
[117,122,132,131,0,126,120,120],
[114,112,133,122,125,0,128,124],
[130,131,139,136,131,123,0,131],
[110,136,145,130,131,127,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,121,118,136,108,131,124],
[135,0,147,124,148,127,141,120],
[130,104,0,116,136,108,129,113],
[133,127,135,0,134,106,142,117],
[115,103,115,117,0,94,121,101],
[143,124,143,145,157,0,147,126],
[120,110,122,109,130,104,0,110],
[127,131,138,134,150,125,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,120,128,120,127,117,138],
[131,0,132,111,133,121,111,132],
[131,119,0,124,110,135,110,132],
[123,140,127,0,133,129,110,132],
[131,118,141,118,0,119,130,125],
[124,130,116,122,132,0,119,144],
[134,140,141,141,121,132,0,139],
[113,119,119,119,126,107,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,142,137,120,133,152,137],
[114,0,128,133,111,122,142,126],
[109,123,0,125,107,123,137,121],
[114,118,126,0,111,115,135,126],
[131,140,144,140,0,116,148,131],
[118,129,128,136,135,0,145,129],
[99,109,114,116,103,106,0,122],
[114,125,130,125,120,122,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,114,113,136,126,129,124],
[122,0,122,104,120,135,124,118],
[137,129,0,119,124,136,129,108],
[138,147,132,0,119,136,136,120],
[115,131,127,132,0,135,125,128],
[125,116,115,115,116,0,133,121],
[122,127,122,115,126,118,0,113],
[127,133,143,131,123,130,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,118,135,127,131,129,128],
[111,0,124,115,108,128,121,107],
[133,127,0,125,130,129,133,122],
[116,136,126,0,118,130,127,135],
[124,143,121,133,0,137,134,119],
[120,123,122,121,114,0,133,121],
[122,130,118,124,117,118,0,105],
[123,144,129,116,132,130,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,106,137,165,134,180,131],
[132,0,122,157,197,146,111,161],
[145,129,0,151,188,117,149,89],
[114,94,100,0,175,121,98,111],
[86,54,63,76,0,105,79,97],
[117,105,134,130,146,0,129,108],
[71,140,102,153,172,122,0,121],
[120,90,162,140,154,143,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,126,105,126,112,102,118],
[121,0,128,103,129,125,106,122],
[125,123,0,108,120,139,103,116],
[146,148,143,0,140,138,137,124],
[125,122,131,111,0,119,108,120],
[139,126,112,113,132,0,113,128],
[149,145,148,114,143,138,0,127],
[133,129,135,127,131,123,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,124,120,132,136,126,108],
[138,0,134,129,129,128,121,132],
[127,117,0,124,126,131,126,130],
[131,122,127,0,121,122,127,127],
[119,122,125,130,0,132,114,142],
[115,123,120,129,119,0,110,135],
[125,130,125,124,137,141,0,128],
[143,119,121,124,109,116,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,136,119,123,124,130,129],
[123,0,124,122,108,118,125,123],
[115,127,0,117,125,119,128,123],
[132,129,134,0,120,127,149,121],
[128,143,126,131,0,123,133,125],
[127,133,132,124,128,0,148,123],
[121,126,123,102,118,103,0,124],
[122,128,128,130,126,128,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,136,124,112,148,151,131],
[101,0,124,106,107,136,152,130],
[115,127,0,114,93,118,143,111],
[127,145,137,0,127,142,122,108],
[139,144,158,124,0,148,142,138],
[103,115,133,109,103,0,128,98],
[100,99,108,129,109,123,0,124],
[120,121,140,143,113,153,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,106,86,115,104,115,132],
[151,0,141,110,126,114,140,133],
[145,110,0,125,143,103,109,124],
[165,141,126,0,149,112,143,129],
[136,125,108,102,0,132,126,124],
[147,137,148,139,119,0,115,119],
[136,111,142,108,125,136,0,117],
[119,118,127,122,127,132,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,124,150,142,157,142,161],
[111,0,134,123,127,131,135,155],
[127,117,0,124,127,131,141,136],
[101,128,127,0,111,129,121,127],
[109,124,124,140,0,127,130,123],
[94,120,120,122,124,0,127,151],
[109,116,110,130,121,124,0,121],
[90,96,115,124,128,100,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,128,127,138,124,132,129],
[121,0,123,122,124,125,125,118],
[123,128,0,126,128,128,126,121],
[124,129,125,0,128,131,124,131],
[113,127,123,123,0,121,108,112],
[127,126,123,120,130,0,139,127],
[119,126,125,127,143,112,0,123],
[122,133,130,120,139,124,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,117,131,120,135,107,119],
[123,0,112,129,116,129,120,126],
[134,139,0,125,133,136,132,118],
[120,122,126,0,117,152,123,130],
[131,135,118,134,0,144,124,126],
[116,122,115,99,107,0,109,122],
[144,131,119,128,127,142,0,143],
[132,125,133,121,125,129,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,90,113,111,123,123,122,132],
[161,0,143,143,134,110,161,135],
[138,108,0,123,125,121,111,153],
[140,108,128,0,144,136,128,138],
[128,117,126,107,0,126,132,106],
[128,141,130,115,125,0,150,132],
[129,90,140,123,119,101,0,127],
[119,116,98,113,145,119,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,158,140,151,129,125,139,124],
[93,0,116,126,107,104,118,102],
[111,135,0,134,120,102,129,110],
[100,125,117,0,107,111,117,106],
[122,144,131,144,0,126,136,123],
[126,147,149,140,125,0,130,134],
[112,133,122,134,115,121,0,124],
[127,149,141,145,128,117,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,130,126,127,130,132,108],
[121,0,137,139,133,131,127,128],
[121,114,0,126,109,120,118,108],
[125,112,125,0,114,116,119,106],
[124,118,142,137,0,130,128,121],
[121,120,131,135,121,0,135,123],
[119,124,133,132,123,116,0,112],
[143,123,143,145,130,128,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,97,127,140,151,102,159,137],
[154,0,124,161,142,104,138,146],
[124,127,0,118,138,124,149,172],
[111,90,133,0,121,85,104,163],
[100,109,113,130,0,126,125,127],
[149,147,127,166,125,0,140,151],
[92,113,102,147,126,111,0,144],
[114,105,79,88,124,100,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,118,125,91,142,123,130],
[127,0,93,104,101,130,69,141],
[133,158,0,153,108,202,88,153],
[126,147,98,0,82,140,74,156],
[160,150,143,169,0,205,132,125],
[109,121,49,111,46,0,55,99],
[128,182,163,177,119,196,0,175],
[121,110,98,95,126,152,76,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,131,125,109,129,119,106],
[122,0,126,121,105,126,129,112],
[120,125,0,114,112,129,113,108],
[126,130,137,0,129,121,144,124],
[142,146,139,122,0,133,127,131],
[122,125,122,130,118,0,120,108],
[132,122,138,107,124,131,0,115],
[145,139,143,127,120,143,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,112,114,119,129,123,130],
[113,0,102,92,113,110,101,124],
[139,149,0,122,122,121,120,126],
[137,159,129,0,119,126,130,137],
[132,138,129,132,0,116,143,138],
[122,141,130,125,135,0,130,148],
[128,150,131,121,108,121,0,139],
[121,127,125,114,113,103,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,119,180,140,136,138,140],
[88,0,94,149,92,114,90,116],
[132,157,0,132,117,170,136,101],
[71,102,119,0,87,118,96,90],
[111,159,134,164,0,166,147,132],
[115,137,81,133,85,0,113,78],
[113,161,115,155,104,138,0,117],
[111,135,150,161,119,173,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,117,120,122,123,114,117],
[129,0,134,126,131,130,124,128],
[134,117,0,125,132,127,125,123],
[131,125,126,0,119,133,123,129],
[129,120,119,132,0,124,132,122],
[128,121,124,118,127,0,115,121],
[137,127,126,128,119,136,0,123],
[134,123,128,122,129,130,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,125,167,133,135,143,162],
[101,0,121,128,122,144,145,144],
[126,130,0,124,131,143,139,148],
[84,123,127,0,122,123,126,121],
[118,129,120,129,0,116,128,149],
[116,107,108,128,135,0,120,145],
[108,106,112,125,123,131,0,138],
[89,107,103,130,102,106,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,125,117,126,132,122,117],
[133,0,127,126,142,142,125,131],
[126,124,0,130,140,134,122,124],
[134,125,121,0,143,137,133,137],
[125,109,111,108,0,120,106,123],
[119,109,117,114,131,0,114,112],
[129,126,129,118,145,137,0,128],
[134,120,127,114,128,139,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,119,128,117,131,126,123],
[128,0,116,118,107,126,111,120],
[132,135,0,118,127,136,125,121],
[123,133,133,0,117,134,114,133],
[134,144,124,134,0,136,127,145],
[120,125,115,117,115,0,113,121],
[125,140,126,137,124,138,0,130],
[128,131,130,118,106,130,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,155,123,124,141,144,130],
[125,0,147,147,133,144,139,132],
[96,104,0,87,86,109,98,116],
[128,104,164,0,126,128,130,136],
[127,118,165,125,0,123,143,147],
[110,107,142,123,128,0,141,136],
[107,112,153,121,108,110,0,137],
[121,119,135,115,104,115,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,142,107,116,137,130,125],
[134,0,130,113,115,122,115,137],
[109,121,0,113,111,115,117,118],
[144,138,138,0,132,148,122,144],
[135,136,140,119,0,140,134,144],
[114,129,136,103,111,0,130,128],
[121,136,134,129,117,121,0,135],
[126,114,133,107,107,123,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,132,135,143,122,109,111],
[156,0,126,158,151,140,128,125],
[119,125,0,126,140,124,112,113],
[116,93,125,0,118,133,113,110],
[108,100,111,133,0,107,109,108],
[129,111,127,118,144,0,115,120],
[142,123,139,138,142,136,0,129],
[140,126,138,141,143,131,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,171,228,87,87,168,111],
[117,0,171,228,60,87,168,111],
[80,80,0,80,80,140,57,80],
[23,23,171,0,83,87,168,134],
[164,191,171,168,0,144,168,111],
[164,164,111,164,107,0,168,107],
[83,83,194,83,83,83,0,83],
[140,140,171,117,140,144,168,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,145,136,129,126,126,125],
[121,0,120,123,130,131,131,134],
[106,131,0,121,128,132,123,122],
[115,128,130,0,122,125,126,126],
[122,121,123,129,0,134,129,122],
[125,120,119,126,117,0,120,129],
[125,120,128,125,122,131,0,122],
[126,117,129,125,129,122,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,120,122,132,130,131,123],
[113,0,109,132,126,137,122,140],
[131,142,0,129,130,139,115,139],
[129,119,122,0,136,135,102,122],
[119,125,121,115,0,127,116,120],
[121,114,112,116,124,0,107,103],
[120,129,136,149,135,144,0,141],
[128,111,112,129,131,148,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,142,129,116,114,97,116],
[106,0,130,112,109,121,100,106],
[109,121,0,106,110,131,102,107],
[122,139,145,0,120,151,113,129],
[135,142,141,131,0,141,129,118],
[137,130,120,100,110,0,100,105],
[154,151,149,138,122,151,0,125],
[135,145,144,122,133,146,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,125,127,130,138,114,135],
[114,0,122,112,117,137,115,113],
[126,129,0,125,132,129,126,130],
[124,139,126,0,133,141,127,138],
[121,134,119,118,0,132,114,135],
[113,114,122,110,119,0,117,125],
[137,136,125,124,137,134,0,134],
[116,138,121,113,116,126,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,164,160,165,140,204,143],
[134,0,124,138,171,127,148,140],
[87,127,0,111,154,91,143,116],
[91,113,140,0,151,53,163,138],
[86,80,97,100,0,81,147,132],
[111,124,160,198,170,0,161,159],
[47,103,108,88,104,90,0,152],
[108,111,135,113,119,92,99,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,103,144,125,118,137,119],
[134,0,122,146,109,132,134,114],
[148,129,0,143,129,137,145,115],
[107,105,108,0,104,126,106,113],
[126,142,122,147,0,164,142,122],
[133,119,114,125,87,0,114,113],
[114,117,106,145,109,137,0,129],
[132,137,136,138,129,138,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,126,125,116,124,127,133],
[140,0,126,127,130,121,128,132],
[125,125,0,122,127,125,128,128],
[126,124,129,0,125,125,127,122],
[135,121,124,126,0,122,123,120],
[127,130,126,126,129,0,120,125],
[124,123,123,124,128,131,0,128],
[118,119,123,129,131,126,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,109,140,119,128,140,114],
[125,0,131,106,143,102,149,108],
[142,120,0,109,113,126,151,103],
[111,145,142,0,116,122,135,135],
[132,108,138,135,0,103,119,108],
[123,149,125,129,148,0,139,141],
[111,102,100,116,132,112,0,110],
[137,143,148,116,143,110,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 251, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_8_251.csv", index=False, header=False)