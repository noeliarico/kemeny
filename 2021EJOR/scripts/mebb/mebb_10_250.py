
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,126,118,114,122,112,126,136,131,116],
[124,0,123,105,119,108,112,130,134,127],
[132,127,0,108,121,115,111,118,118,129],
[136,145,142,0,124,128,127,141,130,120],
[128,131,129,126,0,111,117,132,132,122],
[138,142,135,122,139,0,129,143,133,139],
[124,138,139,123,133,121,0,137,132,145],
[114,120,132,109,118,107,113,0,111,121],
[119,116,132,120,118,117,118,139,0,119],
[134,123,121,130,128,111,105,129,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,95,119,118,132,106,110,135,133],
[111,0,88,117,105,136,108,94,115,119],
[155,162,0,116,131,143,107,144,144,142],
[131,133,134,0,104,153,110,96,141,119],
[132,145,119,146,0,147,123,121,147,143],
[118,114,107,97,103,0,110,99,125,112],
[144,142,143,140,127,140,0,108,145,140],
[140,156,106,154,129,151,142,0,154,133],
[115,135,106,109,103,125,105,96,0,127],
[117,131,108,131,107,138,110,117,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,153,136,114,122,128,118,121,124],
[147,0,174,167,115,131,144,128,105,147],
[97,76,0,103,82,117,105,81,78,116],
[114,83,147,0,109,97,141,105,119,119],
[136,135,168,141,0,150,152,127,119,124],
[128,119,133,153,100,0,132,107,115,123],
[122,106,145,109,98,118,0,121,127,119],
[132,122,169,145,123,143,129,0,113,142],
[129,145,172,131,131,135,123,137,0,140],
[126,103,134,131,126,127,131,108,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,110,143,123,94,124,119,113,125],
[128,0,101,126,111,95,108,85,100,99],
[140,149,0,152,156,110,130,124,140,132],
[107,124,98,0,109,110,135,101,133,121],
[127,139,94,141,0,131,133,99,129,114],
[156,155,140,140,119,0,111,139,153,125],
[126,142,120,115,117,139,0,91,131,128],
[131,165,126,149,151,111,159,0,131,153],
[137,150,110,117,121,97,119,119,0,129],
[125,151,118,129,136,125,122,97,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,115,127,126,130,135,119,126,127],
[117,0,115,117,111,114,118,124,120,125],
[135,135,0,136,131,113,127,131,132,125],
[123,133,114,0,126,126,138,132,121,132],
[124,139,119,124,0,121,129,131,127,131],
[120,136,137,124,129,0,137,117,128,129],
[115,132,123,112,121,113,0,115,123,127],
[131,126,119,118,119,133,135,0,122,128],
[124,130,118,129,123,122,127,128,0,128],
[123,125,125,118,119,121,123,122,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,123,124,130,128,127,120,122,124],
[124,0,129,129,131,129,128,131,138,124],
[127,121,0,131,131,120,115,120,119,118],
[126,121,119,0,135,130,124,126,122,119],
[120,119,119,115,0,127,122,123,122,126],
[122,121,130,120,123,0,126,124,127,118],
[123,122,135,126,128,124,0,126,126,126],
[130,119,130,124,127,126,124,0,124,117],
[128,112,131,128,128,123,124,126,0,123],
[126,126,132,131,124,132,124,133,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,126,107,143,102,115,109,128,130],
[135,0,140,139,162,124,133,124,142,150],
[124,110,0,116,136,121,102,123,134,134],
[143,111,134,0,164,126,113,124,137,145],
[107,88,114,86,0,112,87,114,104,112],
[148,126,129,124,138,0,108,135,138,129],
[135,117,148,137,163,142,0,139,171,147],
[141,126,127,126,136,115,111,0,153,131],
[122,108,116,113,146,112,79,97,0,114],
[120,100,116,105,138,121,103,119,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,125,125,124,108,114,131,126,126],
[134,0,128,136,127,101,118,142,128,116],
[125,122,0,144,131,110,127,151,133,119],
[125,114,106,0,120,110,116,142,126,123],
[126,123,119,130,0,107,111,143,116,115],
[142,149,140,140,143,0,123,148,144,142],
[136,132,123,134,139,127,0,134,136,129],
[119,108,99,108,107,102,116,0,117,110],
[124,122,117,124,134,106,114,133,0,115],
[124,134,131,127,135,108,121,140,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,176,104,95,88,125,98,117,124],
[136,0,141,106,109,87,102,140,134,100],
[74,109,0,109,101,53,105,107,138,115],
[146,144,141,0,110,89,120,126,153,105],
[155,141,149,140,0,134,114,111,139,139],
[162,163,197,161,116,0,145,119,142,155],
[125,148,145,130,136,105,0,130,145,118],
[152,110,143,124,139,131,120,0,117,143],
[133,116,112,97,111,108,105,133,0,112],
[126,150,135,145,111,95,132,107,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,128,122,117,122,102,119,112,116],
[138,0,130,133,128,137,132,124,130,131],
[122,120,0,127,115,122,110,119,111,118],
[128,117,123,0,121,129,102,119,120,117],
[133,122,135,129,0,126,122,119,126,114],
[128,113,128,121,124,0,112,124,114,118],
[148,118,140,148,128,138,0,132,135,134],
[131,126,131,131,131,126,118,0,125,120],
[138,120,139,130,124,136,115,125,0,127],
[134,119,132,133,136,132,116,130,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,120,115,124,133,120,139,120,127],
[133,0,123,138,124,119,128,138,130,126],
[130,127,0,128,123,121,120,135,125,129],
[135,112,122,0,125,119,135,146,130,131],
[126,126,127,125,0,122,127,139,126,126],
[117,131,129,131,128,0,118,130,126,130],
[130,122,130,115,123,132,0,137,125,131],
[111,112,115,104,111,120,113,0,113,119],
[130,120,125,120,124,124,125,137,0,119],
[123,124,121,119,124,120,119,131,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,121,138,122,131,116,133,130,129],
[116,0,117,125,112,125,109,137,123,119],
[129,133,0,131,120,129,118,127,129,120],
[112,125,119,0,125,121,117,135,119,114],
[128,138,130,125,0,135,123,140,140,131],
[119,125,121,129,115,0,115,130,122,118],
[134,141,132,133,127,135,0,145,131,123],
[117,113,123,115,110,120,105,0,124,112],
[120,127,121,131,110,128,119,126,0,119],
[121,131,130,136,119,132,127,138,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,143,142,144,110,133,142,123,130],
[134,0,130,136,139,136,118,124,119,83],
[107,120,0,122,148,135,101,131,125,121],
[108,114,128,0,160,143,126,115,140,124],
[106,111,102,90,0,119,86,104,110,110],
[140,114,115,107,131,0,122,116,119,102],
[117,132,149,124,164,128,0,132,145,132],
[108,126,119,135,146,134,118,0,142,114],
[127,131,125,110,140,131,105,108,0,113],
[120,167,129,126,140,148,118,136,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,132,126,132,115,134,130,128,121],
[129,0,126,131,123,117,135,118,128,121],
[118,124,0,119,142,113,131,116,137,124],
[124,119,131,0,134,112,124,107,121,105],
[118,127,108,116,0,106,113,118,111,100],
[135,133,137,138,144,0,141,112,130,136],
[116,115,119,126,137,109,0,111,122,110],
[120,132,134,143,132,138,139,0,133,127],
[122,122,113,129,139,120,128,117,0,112],
[129,129,126,145,150,114,140,123,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,108,133,125,87,83,109,97,109],
[139,0,111,158,109,79,110,112,118,141],
[142,139,0,149,124,86,128,121,111,125],
[117,92,101,0,97,72,81,82,106,98],
[125,141,126,153,0,91,122,100,145,130],
[163,171,164,178,159,0,147,110,147,155],
[167,140,122,169,128,103,0,112,112,145],
[141,138,129,168,150,140,138,0,119,157],
[153,132,139,144,105,103,138,131,0,111],
[141,109,125,152,120,95,105,93,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,113,122,124,111,116,101,122,134],
[138,0,127,132,113,114,138,115,140,135],
[137,123,0,126,122,117,130,121,124,125],
[128,118,124,0,114,122,131,106,127,122],
[126,137,128,136,0,127,135,122,132,142],
[139,136,133,128,123,0,135,121,131,147],
[134,112,120,119,115,115,0,119,126,124],
[149,135,129,144,128,129,131,0,121,134],
[128,110,126,123,118,119,124,129,0,126],
[116,115,125,128,108,103,126,116,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,136,131,134,136,123,130,142,139],
[120,0,119,118,133,131,137,138,131,138],
[114,131,0,122,135,128,126,132,131,130],
[119,132,128,0,105,140,124,141,126,143],
[116,117,115,145,0,126,136,130,127,140],
[114,119,122,110,124,0,119,120,131,131],
[127,113,124,126,114,131,0,125,119,130],
[120,112,118,109,120,130,125,0,109,133],
[108,119,119,124,123,119,131,141,0,125],
[111,112,120,107,110,119,120,117,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,122,139,110,134,145,125,115,134],
[116,0,120,119,116,139,130,137,130,120],
[128,130,0,130,125,139,135,128,109,138],
[111,131,120,0,128,139,145,137,123,142],
[140,134,125,122,0,127,135,136,116,137],
[116,111,111,111,123,0,125,116,113,127],
[105,120,115,105,115,125,0,117,124,122],
[125,113,122,113,114,134,133,0,98,110],
[135,120,141,127,134,137,126,152,0,135],
[116,130,112,108,113,123,128,140,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,120,110,115,149,121,129,118,129],
[142,0,121,124,124,139,134,144,135,127],
[130,129,0,108,128,138,115,110,122,116],
[140,126,142,0,126,166,129,121,131,127],
[135,126,122,124,0,150,113,134,137,124],
[101,111,112,84,100,0,111,95,101,97],
[129,116,135,121,137,139,0,135,137,136],
[121,106,140,129,116,155,115,0,127,124],
[132,115,128,119,113,149,113,123,0,129],
[121,123,134,123,126,153,114,126,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,88,97,118,135,102,118,140,113,115],
[162,0,123,136,116,146,134,148,124,133],
[153,127,0,139,120,162,126,150,139,135],
[132,114,111,0,125,147,115,144,148,127],
[115,134,130,125,0,126,131,149,109,119],
[148,104,88,103,124,0,100,154,117,123],
[132,116,124,135,119,150,0,141,114,118],
[110,102,100,106,101,96,109,0,100,91],
[137,126,111,102,141,133,136,150,0,122],
[135,117,115,123,131,127,132,159,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,107,121,107,114,130,126,118,125],
[126,0,137,123,128,128,156,144,125,150],
[143,113,0,114,111,109,135,127,114,122],
[129,127,136,0,125,131,149,141,123,135],
[143,122,139,125,0,119,143,125,121,135],
[136,122,141,119,131,0,136,141,117,115],
[120,94,115,101,107,114,0,132,100,125],
[124,106,123,109,125,109,118,0,114,114],
[132,125,136,127,129,133,150,136,0,135],
[125,100,128,115,115,135,125,136,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,125,126,120,126,123,120,119,130],
[112,0,118,112,125,130,117,105,116,135],
[125,132,0,124,122,131,120,129,133,151],
[124,138,126,0,125,132,127,120,120,133],
[130,125,128,125,0,139,120,126,120,127],
[124,120,119,118,111,0,116,118,117,129],
[127,133,130,123,130,134,0,124,124,137],
[130,145,121,130,124,132,126,0,132,146],
[131,134,117,130,130,133,126,118,0,126],
[120,115,99,117,123,121,113,104,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,129,124,117,122,116,114,118,142],
[121,0,140,140,118,130,120,119,134,145],
[121,110,0,119,116,119,124,108,113,134],
[126,110,131,0,117,117,114,120,118,143],
[133,132,134,133,0,122,120,120,119,144],
[128,120,131,133,128,0,126,113,133,140],
[134,130,126,136,130,124,0,140,124,149],
[136,131,142,130,130,137,110,0,118,147],
[132,116,137,132,131,117,126,132,0,141],
[108,105,116,107,106,110,101,103,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,121,139,118,120,139,117,116,131],
[132,0,125,127,128,121,130,123,119,123],
[129,125,0,131,124,117,135,117,114,133],
[111,123,119,0,110,122,132,115,113,126],
[132,122,126,140,0,121,130,132,121,130],
[130,129,133,128,129,0,140,114,133,132],
[111,120,115,118,120,110,0,121,121,126],
[133,127,133,135,118,136,129,0,117,135],
[134,131,136,137,129,117,129,133,0,129],
[119,127,117,124,120,118,124,115,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,128,136,145,128,110,116,107,133],
[135,0,138,128,147,121,109,139,119,131],
[122,112,0,120,146,120,118,124,108,111],
[114,122,130,0,138,123,121,123,107,130],
[105,103,104,112,0,114,92,107,98,98],
[122,129,130,127,136,0,126,119,128,128],
[140,141,132,129,158,124,0,123,122,128],
[134,111,126,127,143,131,127,0,119,123],
[143,131,142,143,152,122,128,131,0,136],
[117,119,139,120,152,122,122,127,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,171,161,175,147,164,125,148,134],
[114,0,128,121,127,109,128,105,91,124],
[79,122,0,82,124,110,113,111,100,113],
[89,129,168,0,147,118,99,109,108,118],
[75,123,126,103,0,102,109,92,115,85],
[103,141,140,132,148,0,103,122,116,106],
[86,122,137,151,141,147,0,114,125,105],
[125,145,139,141,158,128,136,0,143,169],
[102,159,150,142,135,134,125,107,0,128],
[116,126,137,132,165,144,145,81,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,109,111,151,133,129,143,119,124],
[114,0,123,96,117,129,117,126,107,112],
[141,127,0,132,157,135,147,119,131,133],
[139,154,118,0,156,166,140,144,124,133],
[99,133,93,94,0,107,116,108,114,92],
[117,121,115,84,143,0,102,140,118,100],
[121,133,103,110,134,148,0,131,123,109],
[107,124,131,106,142,110,119,0,113,111],
[131,143,119,126,136,132,127,137,0,137],
[126,138,117,117,158,150,141,139,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,102,85,169,141,78,123,108,153],
[172,0,163,172,164,126,113,196,200,117],
[148,87,0,126,118,110,48,157,148,101],
[165,78,124,0,163,147,124,152,170,153],
[81,86,132,87,0,117,116,133,157,163],
[109,124,140,103,133,0,140,133,187,163],
[172,137,202,126,134,110,0,165,143,141],
[127,54,93,98,117,117,85,0,185,85],
[142,50,102,80,93,63,107,65,0,87],
[97,133,149,97,87,87,109,165,163,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,109,154,104,130,135,125,123,125],
[149,0,111,145,120,138,148,160,171,158],
[141,139,0,150,134,145,127,101,158,144],
[96,105,100,0,128,124,121,116,147,122],
[146,130,116,122,0,138,145,128,158,154],
[120,112,105,126,112,0,118,128,127,154],
[115,102,123,129,105,132,0,129,123,131],
[125,90,149,134,122,122,121,0,161,148],
[127,79,92,103,92,123,127,89,0,125],
[125,92,106,128,96,96,119,102,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,105,125,114,112,120,126,117,128],
[128,0,118,133,113,125,120,127,120,133],
[145,132,0,125,124,143,131,139,132,152],
[125,117,125,0,116,102,119,132,115,139],
[136,137,126,134,0,140,126,135,122,144],
[138,125,107,148,110,0,113,139,126,133],
[130,130,119,131,124,137,0,129,125,125],
[124,123,111,118,115,111,121,0,115,117],
[133,130,118,135,128,124,125,135,0,147],
[122,117,98,111,106,117,125,133,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,114,124,117,111,119,118,115,123],
[135,0,127,119,125,121,129,133,122,129],
[136,123,0,126,111,120,113,139,124,129],
[126,131,124,0,122,123,121,135,126,137],
[133,125,139,128,0,132,131,145,127,141],
[139,129,130,127,118,0,125,143,127,135],
[131,121,137,129,119,125,0,127,124,127],
[132,117,111,115,105,107,123,0,117,121],
[135,128,126,124,123,123,126,133,0,133],
[127,121,121,113,109,115,123,129,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,124,125,122,133,145,106,110,114],
[124,0,154,123,141,159,159,129,162,153],
[126,96,0,106,103,128,115,142,133,122],
[125,127,144,0,130,147,164,137,141,101],
[128,109,147,120,0,123,127,134,119,146],
[117,91,122,103,127,0,148,119,152,144],
[105,91,135,86,123,102,0,116,111,135],
[144,121,108,113,116,131,134,0,124,116],
[140,88,117,109,131,98,139,126,0,131],
[136,97,128,149,104,106,115,134,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,111,127,143,136,133,127,135,138],
[124,0,139,128,128,124,124,121,143,128],
[139,111,0,124,151,134,126,136,146,147],
[123,122,126,0,122,114,113,131,141,127],
[107,122,99,128,0,113,128,115,133,122],
[114,126,116,136,137,0,106,124,142,134],
[117,126,124,137,122,144,0,138,125,147],
[123,129,114,119,135,126,112,0,134,131],
[115,107,104,109,117,108,125,116,0,117],
[112,122,103,123,128,116,103,119,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,121,123,108,120,126,141,135,116],
[140,0,115,141,127,131,117,131,115,120],
[129,135,0,125,128,114,142,129,125,141],
[127,109,125,0,98,121,123,133,138,102],
[142,123,122,152,0,106,130,126,143,128],
[130,119,136,129,144,0,117,113,121,143],
[124,133,108,127,120,133,0,140,135,131],
[109,119,121,117,124,137,110,0,111,115],
[115,135,125,112,107,129,115,139,0,105],
[134,130,109,148,122,107,119,135,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,137,134,120,131,146,121,101,139],
[139,0,119,117,138,124,148,122,124,133],
[113,131,0,122,109,118,146,141,117,132],
[116,133,128,0,119,121,157,121,119,146],
[130,112,141,131,0,117,149,125,110,138],
[119,126,132,129,133,0,155,119,114,132],
[104,102,104,93,101,95,0,105,92,125],
[129,128,109,129,125,131,145,0,127,154],
[149,126,133,131,140,136,158,123,0,156],
[111,117,118,104,112,118,125,96,94,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,121,138,126,112,124,137,116,121],
[110,0,121,149,118,130,135,131,103,114],
[129,129,0,138,126,107,126,134,124,138],
[112,101,112,0,98,107,99,104,89,94],
[124,132,124,152,0,105,108,137,112,122],
[138,120,143,143,145,0,127,144,131,142],
[126,115,124,151,142,123,0,138,127,120],
[113,119,116,146,113,106,112,0,126,111],
[134,147,126,161,138,119,123,124,0,108],
[129,136,112,156,128,108,130,139,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,132,127,136,129,126,113,130,121],
[129,0,117,122,122,128,121,128,130,138],
[118,133,0,121,138,139,126,128,129,131],
[123,128,129,0,138,131,123,128,134,131],
[114,128,112,112,0,122,102,107,112,111],
[121,122,111,119,128,0,116,105,100,133],
[124,129,124,127,148,134,0,123,131,133],
[137,122,122,122,143,145,127,0,116,123],
[120,120,121,116,138,150,119,134,0,146],
[129,112,119,119,139,117,117,127,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,123,126,120,123,136,122,119,106],
[124,0,123,132,124,129,129,115,121,118],
[127,127,0,126,119,132,137,120,128,113],
[124,118,124,0,126,127,139,122,128,126],
[130,126,131,124,0,133,144,122,126,115],
[127,121,118,123,117,0,124,116,121,111],
[114,121,113,111,106,126,0,117,114,103],
[128,135,130,128,128,134,133,0,124,118],
[131,129,122,122,124,129,136,126,0,120],
[144,132,137,124,135,139,147,132,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,118,134,131,151,135,140,125,134],
[104,0,112,123,120,117,113,126,124,111],
[132,138,0,119,125,121,123,126,123,119],
[116,127,131,0,111,135,123,121,117,111],
[119,130,125,139,0,148,145,135,122,118],
[99,133,129,115,102,0,108,134,111,110],
[115,137,127,127,105,142,0,137,125,126],
[110,124,124,129,115,116,113,0,126,121],
[125,126,127,133,128,139,125,124,0,126],
[116,139,131,139,132,140,124,129,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,136,116,117,98,111,126,118,139],
[151,0,120,143,125,103,128,125,112,134],
[114,130,0,133,120,105,130,132,129,127],
[134,107,117,0,110,109,136,123,120,120],
[133,125,130,140,0,113,150,128,118,118],
[152,147,145,141,137,0,123,149,132,136],
[139,122,120,114,100,127,0,132,128,123],
[124,125,118,127,122,101,118,0,120,116],
[132,138,121,130,132,118,122,130,0,113],
[111,116,123,130,132,114,127,134,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,126,114,132,123,120,138,134,142],
[127,0,133,136,147,119,128,159,153,150],
[124,117,0,137,131,113,113,144,131,142],
[136,114,113,0,119,123,123,130,142,144],
[118,103,119,131,0,119,112,114,119,126],
[127,131,137,127,131,0,120,145,139,145],
[130,122,137,127,138,130,0,139,127,148],
[112,91,106,120,136,105,111,0,114,131],
[116,97,119,108,131,111,123,136,0,130],
[108,100,108,106,124,105,102,119,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,131,119,129,119,111,119,122,135],
[126,0,123,138,135,117,122,121,117,127],
[119,127,0,130,130,136,123,116,131,138],
[131,112,120,0,127,119,101,112,119,126],
[121,115,120,123,0,113,103,112,122,129],
[131,133,114,131,137,0,119,119,122,135],
[139,128,127,149,147,131,0,126,124,140],
[131,129,134,138,138,131,124,0,122,143],
[128,133,119,131,128,128,126,128,0,144],
[115,123,112,124,121,115,110,107,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,83,112,81,95,109,72,101,119,87],
[167,0,152,153,127,124,131,100,122,132],
[138,98,0,91,83,108,86,97,100,103],
[169,97,159,0,124,147,111,152,163,107],
[155,123,167,126,0,150,131,106,135,103],
[141,126,142,103,100,0,138,116,135,117],
[178,119,164,139,119,112,0,152,121,151],
[149,150,153,98,144,134,98,0,162,117],
[131,128,150,87,115,115,129,88,0,126],
[163,118,147,143,147,133,99,133,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,132,140,173,100,145,153,69,142],
[109,0,115,130,145,54,110,115,115,116],
[118,135,0,136,140,110,149,120,105,87],
[110,120,114,0,107,74,114,166,79,126],
[77,105,110,143,0,69,154,121,70,145],
[150,196,140,176,181,0,133,154,125,146],
[105,140,101,136,96,117,0,186,105,100],
[97,135,130,84,129,96,64,0,94,84],
[181,135,145,171,180,125,145,156,0,186],
[108,134,163,124,105,104,150,166,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,133,126,134,133,130,125,124,140],
[128,0,131,136,139,122,133,123,122,136],
[117,119,0,129,129,121,137,119,137,133],
[124,114,121,0,135,119,132,114,120,124],
[116,111,121,115,0,118,114,115,114,107],
[117,128,129,131,132,0,131,122,126,124],
[120,117,113,118,136,119,0,110,112,114],
[125,127,131,136,135,128,140,0,135,129],
[126,128,113,130,136,124,138,115,0,123],
[110,114,117,126,143,126,136,121,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,126,132,122,132,123,124,120,120],
[130,0,118,133,118,130,135,120,117,123],
[124,132,0,128,130,139,124,135,125,127],
[118,117,122,0,116,125,118,121,116,131],
[128,132,120,134,0,129,125,125,123,126],
[118,120,111,125,121,0,114,113,109,118],
[127,115,126,132,125,136,0,121,118,128],
[126,130,115,129,125,137,129,0,111,125],
[130,133,125,134,127,141,132,139,0,126],
[130,127,123,119,124,132,122,125,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,138,139,120,116,129,140,138,121],
[114,0,128,131,113,134,131,143,114,127],
[112,122,0,130,117,123,121,137,117,111],
[111,119,120,0,118,128,124,136,121,109],
[130,137,133,132,0,124,128,146,130,116],
[134,116,127,122,126,0,129,138,115,120],
[121,119,129,126,122,121,0,130,127,120],
[110,107,113,114,104,112,120,0,116,106],
[112,136,133,129,120,135,123,134,0,121],
[129,123,139,141,134,130,130,144,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,134,111,135,134,123,135,126,134],
[117,0,120,111,127,138,119,138,122,140],
[116,130,0,119,132,129,120,135,124,132],
[139,139,131,0,138,143,130,155,125,140],
[115,123,118,112,0,128,119,132,107,123],
[116,112,121,107,122,0,111,146,110,138],
[127,131,130,120,131,139,0,151,126,143],
[115,112,115,95,118,104,99,0,102,122],
[124,128,126,125,143,140,124,148,0,131],
[116,110,118,110,127,112,107,128,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,139,123,129,124,119,130,135,125],
[127,0,145,125,134,128,124,134,139,119],
[111,105,0,114,115,123,112,120,124,117],
[127,125,136,0,136,130,126,136,141,133],
[121,116,135,114,0,117,119,136,135,126],
[126,122,127,120,133,0,124,134,132,131],
[131,126,138,124,131,126,0,130,139,126],
[120,116,130,114,114,116,120,0,127,110],
[115,111,126,109,115,118,111,123,0,117],
[125,131,133,117,124,119,124,140,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,133,139,110,130,149,123,104,112],
[132,0,124,142,119,109,128,120,100,125],
[117,126,0,138,113,117,123,117,110,115],
[111,108,112,0,119,109,133,105,107,119],
[140,131,137,131,0,128,148,120,130,121],
[120,141,133,141,122,0,156,119,88,118],
[101,122,127,117,102,94,0,108,82,114],
[127,130,133,145,130,131,142,0,109,104],
[146,150,140,143,120,162,168,141,0,128],
[138,125,135,131,129,132,136,146,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,109,96,102,100,122,96,86,132],
[146,0,126,110,117,126,140,117,113,130],
[141,124,0,98,122,112,110,111,95,88],
[154,140,152,0,144,121,126,127,116,165],
[148,133,128,106,0,115,126,103,110,132],
[150,124,138,129,135,0,118,116,125,125],
[128,110,140,124,124,132,0,130,95,137],
[154,133,139,123,147,134,120,0,124,128],
[164,137,155,134,140,125,155,126,0,135],
[118,120,162,85,118,125,113,122,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,118,136,127,120,130,123,135,117],
[118,0,123,132,132,123,122,128,131,125],
[132,127,0,139,135,129,132,127,135,117],
[114,118,111,0,121,114,120,118,125,116],
[123,118,115,129,0,119,127,124,135,123],
[130,127,121,136,131,0,122,119,135,123],
[120,128,118,130,123,128,0,121,119,119],
[127,122,123,132,126,131,129,0,133,131],
[115,119,115,125,115,115,131,117,0,126],
[133,125,133,134,127,127,131,119,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,135,140,124,134,119,142,137,116],
[123,0,121,152,129,126,92,133,129,126],
[115,129,0,149,137,158,133,142,129,125],
[110,98,101,0,133,120,96,125,102,110],
[126,121,113,117,0,123,108,123,119,117],
[116,124,92,130,127,0,107,139,121,121],
[131,158,117,154,142,143,0,129,130,123],
[108,117,108,125,127,111,121,0,135,124],
[113,121,121,148,131,129,120,115,0,121],
[134,124,125,140,133,129,127,126,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,124,120,135,113,126,122,125,124],
[118,0,119,117,136,124,123,137,121,125],
[126,131,0,113,135,122,122,132,119,118],
[130,133,137,0,137,122,127,133,129,123],
[115,114,115,113,0,119,106,111,125,122],
[137,126,128,128,131,0,122,115,134,123],
[124,127,128,123,144,128,0,129,117,123],
[128,113,118,117,139,135,121,0,118,117],
[125,129,131,121,125,116,133,132,0,129],
[126,125,132,127,128,127,127,133,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,106,122,125,143,112,123,112,119],
[120,0,140,111,125,140,109,113,116,128],
[144,110,0,115,129,159,127,122,118,120],
[128,139,135,0,133,148,128,137,105,130],
[125,125,121,117,0,153,141,129,141,120],
[107,110,91,102,97,0,108,118,98,122],
[138,141,123,122,109,142,0,123,124,141],
[127,137,128,113,121,132,127,0,109,120],
[138,134,132,145,109,152,126,141,0,147],
[131,122,130,120,130,128,109,130,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,89,107,113,105,109,93,103,98,100],
[161,0,143,139,128,153,134,140,128,118],
[143,107,0,125,101,125,107,123,116,114],
[137,111,125,0,121,119,126,125,106,114],
[145,122,149,129,0,143,130,147,132,133],
[141,97,125,131,107,0,111,119,119,111],
[157,116,143,124,120,139,0,133,123,122],
[147,110,127,125,103,131,117,0,122,103],
[152,122,134,144,118,131,127,128,0,125],
[150,132,136,136,117,139,128,147,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,139,117,122,131,130,136,135,119],
[121,0,119,116,113,117,128,133,119,117],
[111,131,0,111,126,127,134,131,127,118],
[133,134,139,0,138,132,129,128,138,125],
[128,137,124,112,0,135,120,138,135,127],
[119,133,123,118,115,0,117,131,132,120],
[120,122,116,121,130,133,0,127,125,119],
[114,117,119,122,112,119,123,0,133,124],
[115,131,123,112,115,118,125,117,0,122],
[131,133,132,125,123,130,131,126,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,126,138,125,125,120,133,130],
[123,0,124,116,131,117,126,124,128,114],
[127,126,0,117,128,114,130,121,128,117],
[124,134,133,0,134,121,128,128,123,127],
[112,119,122,116,0,112,117,118,113,121],
[125,133,136,129,138,0,132,136,132,137],
[125,124,120,122,133,118,0,116,125,126],
[130,126,129,122,132,114,134,0,132,119],
[117,122,122,127,137,118,125,118,0,121],
[120,136,133,123,129,113,124,131,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,103,90,110,120,122,103,97,118],
[142,0,104,112,127,122,112,103,96,115],
[147,146,0,117,129,129,122,136,115,136],
[160,138,133,0,136,140,127,125,117,130],
[140,123,121,114,0,128,122,124,108,119],
[130,128,121,110,122,0,109,113,116,109],
[128,138,128,123,128,141,0,103,112,128],
[147,147,114,125,126,137,147,0,142,125],
[153,154,135,133,142,134,138,108,0,109],
[132,135,114,120,131,141,122,125,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,140,141,131,132,130,141,135,156],
[130,0,119,95,92,123,137,99,146,137],
[110,131,0,126,101,129,109,143,120,134],
[109,155,124,0,102,136,96,115,133,124],
[119,158,149,148,0,120,130,139,136,158],
[118,127,121,114,130,0,96,137,124,135],
[120,113,141,154,120,154,0,128,132,116],
[109,151,107,135,111,113,122,0,116,129],
[115,104,130,117,114,126,118,134,0,127],
[94,113,116,126,92,115,134,121,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,122,121,145,128,185,151,121,142],
[99,0,66,63,119,99,117,91,78,111],
[128,184,0,134,163,173,197,183,152,125],
[129,187,116,0,146,147,170,102,141,126],
[105,131,87,104,0,134,149,98,119,122],
[122,151,77,103,116,0,187,153,120,132],
[65,133,53,80,101,63,0,99,83,100],
[99,159,67,148,152,97,151,0,120,109],
[129,172,98,109,131,130,167,130,0,123],
[108,139,125,124,128,118,150,141,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,117,126,128,150,115,127,116,135],
[130,0,126,119,140,142,120,127,104,137],
[133,124,0,123,138,149,121,127,107,144],
[124,131,127,0,137,131,133,134,130,145],
[122,110,112,113,0,126,107,116,108,130],
[100,108,101,119,124,0,116,111,105,129],
[135,130,129,117,143,134,0,127,120,149],
[123,123,123,116,134,139,123,0,109,140],
[134,146,143,120,142,145,130,141,0,154],
[115,113,106,105,120,121,101,110,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,120,119,127,108,130,122,117,119],
[136,0,115,119,119,115,129,112,121,120],
[130,135,0,127,125,128,137,125,116,121],
[131,131,123,0,124,123,138,116,122,125],
[123,131,125,126,0,112,130,122,116,121],
[142,135,122,127,138,0,134,133,120,124],
[120,121,113,112,120,116,0,116,115,111],
[128,138,125,134,128,117,134,0,119,132],
[133,129,134,128,134,130,135,131,0,122],
[131,130,129,125,129,126,139,118,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,142,114,147,125,138,118,138,141],
[123,0,144,138,164,150,148,144,140,139],
[108,106,0,102,127,108,118,126,117,115],
[136,112,148,0,132,120,126,122,135,133],
[103,86,123,118,0,128,132,117,113,129],
[125,100,142,130,122,0,115,113,123,126],
[112,102,132,124,118,135,0,129,109,118],
[132,106,124,128,133,137,121,0,132,124],
[112,110,133,115,137,127,141,118,0,119],
[109,111,135,117,121,124,132,126,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,124,130,122,122,125,106,112,117],
[123,0,126,131,126,124,117,127,121,133],
[126,124,0,126,115,120,131,118,121,127],
[120,119,124,0,117,122,117,115,111,119],
[128,124,135,133,0,132,133,115,126,143],
[128,126,130,128,118,0,128,110,127,119],
[125,133,119,133,117,122,0,112,118,137],
[144,123,132,135,135,140,138,0,127,147],
[138,129,129,139,124,123,132,123,0,138],
[133,117,123,131,107,131,113,103,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,122,134,124,133,133,126,112,139],
[128,0,135,144,118,132,143,129,128,131],
[128,115,0,129,124,129,133,125,126,142],
[116,106,121,0,107,132,118,128,122,116],
[126,132,126,143,0,142,133,131,124,129],
[117,118,121,118,108,0,127,121,110,117],
[117,107,117,132,117,123,0,130,119,126],
[124,121,125,122,119,129,120,0,114,138],
[138,122,124,128,126,140,131,136,0,129],
[111,119,108,134,121,133,124,112,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,124,113,117,130,128,108,126,127],
[123,0,114,113,119,129,140,115,127,117],
[126,136,0,119,112,136,124,120,134,121],
[137,137,131,0,121,148,158,129,146,118],
[133,131,138,129,0,154,140,117,140,141],
[120,121,114,102,96,0,121,123,123,122],
[122,110,126,92,110,129,0,110,115,113],
[142,135,130,121,133,127,140,0,146,127],
[124,123,116,104,110,127,135,104,0,107],
[123,133,129,132,109,128,137,123,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,117,109,116,113,97,114,113,108],
[137,0,139,115,141,128,122,124,133,126],
[133,111,0,123,119,120,130,102,116,116],
[141,135,127,0,161,120,133,134,129,143],
[134,109,131,89,0,103,115,98,112,116],
[137,122,130,130,147,0,128,121,126,117],
[153,128,120,117,135,122,0,132,117,126],
[136,126,148,116,152,129,118,0,127,135],
[137,117,134,121,138,124,133,123,0,128],
[142,124,134,107,134,133,124,115,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,97,122,130,127,109,128,94,127],
[138,0,115,112,125,127,131,118,128,136],
[153,135,0,153,137,145,161,144,123,147],
[128,138,97,0,129,123,127,124,88,133],
[120,125,113,121,0,125,146,132,125,127],
[123,123,105,127,125,0,129,121,119,138],
[141,119,89,123,104,121,0,114,106,125],
[122,132,106,126,118,129,136,0,109,141],
[156,122,127,162,125,131,144,141,0,139],
[123,114,103,117,123,112,125,109,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,127,121,131,132,123,120,128,123],
[123,0,113,126,118,127,121,110,118,109],
[123,137,0,130,136,121,123,143,127,130],
[129,124,120,0,132,111,127,121,122,123],
[119,132,114,118,0,124,120,130,138,117],
[118,123,129,139,126,0,130,114,115,127],
[127,129,127,123,130,120,0,130,127,132],
[130,140,107,129,120,136,120,0,125,113],
[122,132,123,128,112,135,123,125,0,131],
[127,141,120,127,133,123,118,137,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,133,121,127,127,138,141,138,131],
[122,0,129,125,117,113,129,124,128,122],
[117,121,0,110,119,122,131,129,134,124],
[129,125,140,0,121,132,131,138,129,132],
[123,133,131,129,0,135,145,140,134,140],
[123,137,128,118,115,0,140,141,137,139],
[112,121,119,119,105,110,0,133,126,125],
[109,126,121,112,110,109,117,0,121,122],
[112,122,116,121,116,113,124,129,0,122],
[119,128,126,118,110,111,125,128,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,140,144,138,136,132,138,128,140],
[128,0,150,149,134,124,142,124,119,122],
[110,100,0,129,125,108,113,120,108,118],
[106,101,121,0,113,102,103,114,89,111],
[112,116,125,137,0,115,116,128,103,129],
[114,126,142,148,135,0,127,132,123,136],
[118,108,137,147,134,123,0,122,119,129],
[112,126,130,136,122,118,128,0,126,127],
[122,131,142,161,147,127,131,124,0,138],
[110,128,132,139,121,114,121,123,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,110,123,129,119,121,135,114,117],
[121,0,114,116,125,115,121,138,116,113],
[140,136,0,128,140,133,129,154,124,120],
[127,134,122,0,145,124,137,151,124,125],
[121,125,110,105,0,107,128,146,113,115],
[131,135,117,126,143,0,144,158,131,129],
[129,129,121,113,122,106,0,135,110,110],
[115,112,96,99,104,92,115,0,101,96],
[136,134,126,126,137,119,140,149,0,128],
[133,137,130,125,135,121,140,154,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,130,107,134,135,113,131,110,119],
[132,0,144,107,128,130,119,135,117,138],
[120,106,0,111,118,118,113,117,105,138],
[143,143,139,0,146,139,124,152,129,151],
[116,122,132,104,0,136,125,129,113,126],
[115,120,132,111,114,0,114,129,119,132],
[137,131,137,126,125,136,0,140,126,131],
[119,115,133,98,121,121,110,0,96,135],
[140,133,145,121,137,131,124,154,0,155],
[131,112,112,99,124,118,119,115,95,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,156,183,158,150,121,180,132,154,144],
[94,0,160,141,145,142,151,165,175,113],
[67,90,0,125,117,73,127,68,92,97],
[92,109,125,0,86,107,111,102,117,97],
[100,105,133,164,0,88,145,122,114,125],
[129,108,177,143,162,0,163,146,180,149],
[70,99,123,139,105,87,0,126,126,172],
[118,85,182,148,128,104,124,0,127,92],
[96,75,158,133,136,70,124,123,0,132],
[106,137,153,153,125,101,78,158,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,140,115,122,132,129,133,123,130],
[128,0,125,118,125,127,132,125,133,138],
[110,125,0,112,114,112,124,111,130,127],
[135,132,138,0,124,130,131,125,132,122],
[128,125,136,126,0,129,130,130,133,145],
[118,123,138,120,121,0,122,119,125,137],
[121,118,126,119,120,128,0,115,136,134],
[117,125,139,125,120,131,135,0,128,130],
[127,117,120,118,117,125,114,122,0,138],
[120,112,123,128,105,113,116,120,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,110,117,113,139,124,129,110,119],
[130,0,129,134,109,157,137,133,130,140],
[140,121,0,132,128,140,129,134,119,147],
[133,116,118,0,114,141,116,134,111,127],
[137,141,122,136,0,153,135,135,125,128],
[111,93,110,109,97,0,114,110,95,126],
[126,113,121,134,115,136,0,133,123,119],
[121,117,116,116,115,140,117,0,123,128],
[140,120,131,139,125,155,127,127,0,143],
[131,110,103,123,122,124,131,122,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,111,121,113,135,118,118,126,122],
[136,0,112,126,114,129,123,128,117,112],
[139,138,0,127,121,124,125,133,138,113],
[129,124,123,0,117,118,105,130,131,129],
[137,136,129,133,0,129,133,128,137,110],
[115,121,126,132,121,0,99,122,115,113],
[132,127,125,145,117,151,0,125,142,135],
[132,122,117,120,122,128,125,0,135,128],
[124,133,112,119,113,135,108,115,0,131],
[128,138,137,121,140,137,115,122,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,128,137,119,112,127,114,122,119],
[136,0,140,144,114,143,153,135,133,129],
[122,110,0,114,121,117,130,116,123,131],
[113,106,136,0,126,128,150,105,135,118],
[131,136,129,124,0,132,145,116,119,127],
[138,107,133,122,118,0,127,116,119,112],
[123,97,120,100,105,123,0,106,127,120],
[136,115,134,145,134,134,144,0,148,119],
[128,117,127,115,131,131,123,102,0,112],
[131,121,119,132,123,138,130,131,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,137,140,153,135,129,123,117,143],
[121,0,109,131,136,125,114,125,125,140],
[113,141,0,124,131,134,124,111,113,133],
[110,119,126,0,129,108,125,115,114,147],
[97,114,119,121,0,116,114,97,108,127],
[115,125,116,142,134,0,120,121,117,141],
[121,136,126,125,136,130,0,120,108,128],
[127,125,139,135,153,129,130,0,133,149],
[133,125,137,136,142,133,142,117,0,147],
[107,110,117,103,123,109,122,101,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,128,122,123,134,129,126,117,121],
[129,0,121,124,118,123,122,124,120,137],
[122,129,0,135,124,131,131,139,127,131],
[128,126,115,0,118,114,130,126,118,134],
[127,132,126,132,0,120,133,130,127,132],
[116,127,119,136,130,0,120,125,123,130],
[121,128,119,120,117,130,0,125,118,126],
[124,126,111,124,120,125,125,0,117,140],
[133,130,123,132,123,127,132,133,0,146],
[129,113,119,116,118,120,124,110,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,128,128,130,118,136,136,115],
[125,0,117,123,133,135,126,141,133,118],
[129,133,0,136,141,141,122,136,138,129],
[122,127,114,0,137,125,120,134,128,128],
[122,117,109,113,0,120,125,133,128,110],
[120,115,109,125,130,0,123,132,129,114],
[132,124,128,130,125,127,0,140,139,125],
[114,109,114,116,117,118,110,0,116,112],
[114,117,112,122,122,121,111,134,0,116],
[135,132,121,122,140,136,125,138,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,94,99,98,95,94,139,84,96],
[196,0,210,99,161,189,215,190,151,149],
[156,40,0,85,100,104,128,129,75,75],
[151,151,165,0,116,191,185,235,166,119],
[152,89,150,134,0,104,175,176,154,120],
[155,61,146,59,146,0,126,161,126,105],
[156,35,122,65,75,124,0,160,100,100],
[111,60,121,15,74,89,90,0,50,79],
[166,99,175,84,96,124,150,200,0,129],
[154,101,175,131,130,145,150,171,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,113,103,147,75,139,92,139,126],
[128,0,112,105,97,97,92,98,104,136],
[137,138,0,109,122,124,137,127,119,132],
[147,145,141,0,119,119,111,121,111,152],
[103,153,128,131,0,88,79,107,116,134],
[175,153,126,131,162,0,155,133,121,164],
[111,158,113,139,171,95,0,108,128,121],
[158,152,123,129,143,117,142,0,130,168],
[111,146,131,139,134,129,122,120,0,135],
[124,114,118,98,116,86,129,82,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,140,139,127,141,132,153,149,164],
[128,0,125,122,124,130,128,147,129,160],
[110,125,0,118,124,119,125,125,127,143],
[111,128,132,0,123,140,127,126,110,144],
[123,126,126,127,0,146,127,135,128,151],
[109,120,131,110,104,0,113,129,109,135],
[118,122,125,123,123,137,0,134,133,139],
[97,103,125,124,115,121,116,0,115,146],
[101,121,123,140,122,141,117,135,0,144],
[86,90,107,106,99,115,111,104,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,138,147,145,154,121,135,133,121],
[102,0,106,123,101,141,110,114,129,110],
[112,144,0,132,131,154,123,118,137,139],
[103,127,118,0,120,120,104,114,137,115],
[105,149,119,130,0,151,135,116,154,124],
[96,109,96,130,99,0,108,91,121,102],
[129,140,127,146,115,142,0,122,133,110],
[115,136,132,136,134,159,128,0,155,134],
[117,121,113,113,96,129,117,95,0,91],
[129,140,111,135,126,148,140,116,159,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,112,116,123,124,140,118,131,124],
[117,0,100,98,113,114,118,97,126,116],
[138,150,0,117,118,122,139,125,132,132],
[134,152,133,0,124,126,132,123,127,134],
[127,137,132,126,0,127,139,107,140,113],
[126,136,128,124,123,0,141,121,137,123],
[110,132,111,118,111,109,0,111,122,122],
[132,153,125,127,143,129,139,0,135,142],
[119,124,118,123,110,113,128,115,0,117],
[126,134,118,116,137,127,128,108,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,96,127,110,102,107,129,111,117],
[151,0,131,130,140,150,137,137,149,120],
[154,119,0,135,142,144,125,134,144,120],
[123,120,115,0,120,133,119,125,122,106],
[140,110,108,130,0,136,122,144,113,124],
[148,100,106,117,114,0,126,150,112,112],
[143,113,125,131,128,124,0,140,120,114],
[121,113,116,125,106,100,110,0,116,108],
[139,101,106,128,137,138,130,134,0,126],
[133,130,130,144,126,138,136,142,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,128,139,123,130,125,136,120,126],
[119,0,122,136,130,116,113,120,123,121],
[122,128,0,140,123,126,126,114,128,134],
[111,114,110,0,119,117,121,120,114,112],
[127,120,127,131,0,130,124,123,123,104],
[120,134,124,133,120,0,129,120,120,125],
[125,137,124,129,126,121,0,119,118,126],
[114,130,136,130,127,130,131,0,127,116],
[130,127,122,136,127,130,132,123,0,122],
[124,129,116,138,146,125,124,134,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,134,137,135,109,129,119,120,132],
[128,0,128,126,142,121,121,129,138,122],
[116,122,0,113,127,111,117,117,117,115],
[113,124,137,0,133,112,115,127,125,125],
[115,108,123,117,0,111,107,108,128,116],
[141,129,139,138,139,0,120,130,156,135],
[121,129,133,135,143,130,0,132,143,130],
[131,121,133,123,142,120,118,0,134,122],
[130,112,133,125,122,94,107,116,0,125],
[118,128,135,125,134,115,120,128,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,130,106,130,115,97,113,116,114],
[121,0,120,114,133,131,107,128,109,97],
[120,130,0,129,145,126,124,125,134,137],
[144,136,121,0,142,134,128,144,122,133],
[120,117,105,108,0,103,96,107,99,95],
[135,119,124,116,147,0,108,139,118,128],
[153,143,126,122,154,142,0,146,131,124],
[137,122,125,106,143,111,104,0,109,115],
[134,141,116,128,151,132,119,141,0,116],
[136,153,113,117,155,122,126,135,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,110,115,154,135,113,115,119,132],
[105,0,132,133,134,157,109,119,131,139],
[140,118,0,110,128,120,114,97,101,116],
[135,117,140,0,96,154,112,123,106,126],
[96,116,122,154,0,125,113,79,97,109],
[115,93,130,96,125,0,82,100,111,102],
[137,141,136,138,137,168,0,105,117,129],
[135,131,153,127,171,150,145,0,139,121],
[131,119,149,144,153,139,133,111,0,114],
[118,111,134,124,141,148,121,129,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,127,145,123,114,116,140,132,118],
[117,0,116,136,110,106,107,134,128,111],
[123,134,0,135,119,131,120,151,134,114],
[105,114,115,0,114,106,119,135,120,121],
[127,140,131,136,0,123,132,162,144,124],
[136,144,119,144,127,0,133,159,142,126],
[134,143,130,131,118,117,0,146,140,123],
[110,116,99,115,88,91,104,0,118,103],
[118,122,116,130,106,108,110,132,0,106],
[132,139,136,129,126,124,127,147,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,123,132,110,128,132,135,125],
[125,0,127,129,126,136,141,146,140,134],
[129,123,0,126,130,132,123,141,134,124],
[127,121,124,0,123,126,130,145,134,136],
[118,124,120,127,0,132,132,125,127,125],
[140,114,118,124,118,0,124,142,129,126],
[122,109,127,120,118,126,0,133,124,125],
[118,104,109,105,125,108,117,0,124,117],
[115,110,116,116,123,121,126,126,0,122],
[125,116,126,114,125,124,125,133,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,123,108,131,116,105,140,134,118],
[141,0,122,135,134,141,140,141,132,124],
[127,128,0,115,131,125,119,119,134,120],
[142,115,135,0,140,124,134,149,129,126],
[119,116,119,110,0,126,134,132,132,129],
[134,109,125,126,124,0,128,128,131,114],
[145,110,131,116,116,122,0,130,138,127],
[110,109,131,101,118,122,120,0,136,123],
[116,118,116,121,118,119,112,114,0,111],
[132,126,130,124,121,136,123,127,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,118,127,120,109,124,109,118,127],
[106,0,116,99,111,101,120,108,98,112],
[132,134,0,128,128,121,122,136,115,138],
[123,151,122,0,119,113,124,122,128,137],
[130,139,122,131,0,123,116,126,124,134],
[141,149,129,137,127,0,132,124,127,136],
[126,130,128,126,134,118,0,124,123,139],
[141,142,114,128,124,126,126,0,112,128],
[132,152,135,122,126,123,127,138,0,134],
[123,138,112,113,116,114,111,122,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,137,102,138,140,112,141,134,131],
[112,0,142,94,136,92,107,99,99,142],
[113,108,0,96,132,116,120,109,130,140],
[148,156,154,0,135,147,120,146,174,162],
[112,114,118,115,0,143,138,66,122,143],
[110,158,134,103,107,0,93,111,124,144],
[138,143,130,130,112,157,0,121,139,152],
[109,151,141,104,184,139,129,0,156,157],
[116,151,120,76,128,126,111,94,0,124],
[119,108,110,88,107,106,98,93,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,142,136,137,133,118,118,128,131],
[114,0,131,134,124,123,123,122,127,113],
[108,119,0,126,129,114,113,115,121,110],
[114,116,124,0,124,112,112,113,108,104],
[113,126,121,126,0,121,111,123,120,115],
[117,127,136,138,129,0,130,137,125,131],
[132,127,137,138,139,120,0,123,124,125],
[132,128,135,137,127,113,127,0,122,129],
[122,123,129,142,130,125,126,128,0,124],
[119,137,140,146,135,119,125,121,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,117,142,94,118,125,120,151,116],
[138,0,148,174,147,177,121,142,161,136],
[133,102,0,134,116,155,109,136,122,119],
[108,76,116,0,92,118,79,100,97,92],
[156,103,134,158,0,155,128,141,143,132],
[132,73,95,132,95,0,88,120,109,101],
[125,129,141,171,122,162,0,154,177,131],
[130,108,114,150,109,130,96,0,144,98],
[99,89,128,153,107,141,73,106,0,96],
[134,114,131,158,118,149,119,152,154,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,113,78,131,105,84,86,115,97],
[134,0,102,96,125,125,126,125,131,120],
[137,148,0,102,134,111,115,111,124,113],
[172,154,148,0,154,132,127,108,155,128],
[119,125,116,96,0,101,110,104,126,93],
[145,125,139,118,149,0,116,123,127,127],
[166,124,135,123,140,134,0,125,145,126],
[164,125,139,142,146,127,125,0,127,122],
[135,119,126,95,124,123,105,123,0,112],
[153,130,137,122,157,123,124,128,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,120,137,121,130,126,126,140,119],
[130,0,122,140,123,127,121,124,136,123],
[130,128,0,137,121,133,118,130,138,120],
[113,110,113,0,118,122,117,110,117,112],
[129,127,129,132,0,134,131,124,137,115],
[120,123,117,128,116,0,112,123,119,119],
[124,129,132,133,119,138,0,121,132,125],
[124,126,120,140,126,127,129,0,142,116],
[110,114,112,133,113,131,118,108,0,116],
[131,127,130,138,135,131,125,134,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,124,125,118,114,123,128,136,116],
[128,0,136,141,125,123,131,126,128,117],
[126,114,0,124,121,115,125,127,117,103],
[125,109,126,0,123,101,119,120,125,106],
[132,125,129,127,0,114,114,117,124,114],
[136,127,135,149,136,0,131,138,143,125],
[127,119,125,131,136,119,0,136,116,112],
[122,124,123,130,133,112,114,0,124,105],
[114,122,133,125,126,107,134,126,0,121],
[134,133,147,144,136,125,138,145,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,122,118,135,119,124,124,137,121],
[124,0,121,125,141,110,123,106,139,116],
[128,129,0,132,143,114,130,102,131,123],
[132,125,118,0,145,106,117,127,131,121],
[115,109,107,105,0,97,105,104,121,107],
[131,140,136,144,153,0,144,121,148,134],
[126,127,120,133,145,106,0,114,140,110],
[126,144,148,123,146,129,136,0,148,129],
[113,111,119,119,129,102,110,102,0,111],
[129,134,127,129,143,116,140,121,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,108,114,93,111,128,151,92,122],
[135,0,139,133,155,104,135,138,135,136],
[142,111,0,103,147,112,137,141,122,129],
[136,117,147,0,133,112,120,130,128,157],
[157,95,103,117,0,99,119,134,114,119],
[139,146,138,138,151,0,138,124,139,135],
[122,115,113,130,131,112,0,133,119,127],
[99,112,109,120,116,126,117,0,115,95],
[158,115,128,122,136,111,131,135,0,121],
[128,114,121,93,131,115,123,155,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,133,124,125,131,129,113,123,124],
[132,0,126,135,136,126,125,122,126,127],
[117,124,0,124,126,134,118,119,121,121],
[126,115,126,0,135,128,125,117,116,123],
[125,114,124,115,0,122,121,131,128,121],
[119,124,116,122,128,0,119,111,128,116],
[121,125,132,125,129,131,0,121,126,130],
[137,128,131,133,119,139,129,0,133,128],
[127,124,129,134,122,122,124,117,0,126],
[126,123,129,127,129,134,120,122,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,170,164,109,116,206,98,110,163],
[127,0,152,55,82,87,96,30,91,182],
[80,98,0,115,125,136,170,73,99,188],
[86,195,135,0,173,178,131,126,135,135],
[141,168,125,77,0,131,114,142,105,204],
[134,163,114,72,119,0,163,182,163,163],
[44,154,80,119,136,87,0,93,47,154],
[152,220,177,124,108,68,157,0,152,215],
[140,159,151,115,145,87,203,98,0,188],
[87,68,62,115,46,87,96,35,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,133,124,122,117,129,132,136,137],
[114,0,108,128,102,118,122,125,128,116],
[117,142,0,125,118,110,129,119,129,120],
[126,122,125,0,118,120,131,127,128,128],
[128,148,132,132,0,126,123,141,141,131],
[133,132,140,130,124,0,144,137,141,137],
[121,128,121,119,127,106,0,137,129,128],
[118,125,131,123,109,113,113,0,127,119],
[114,122,121,122,109,109,121,123,0,120],
[113,134,130,122,119,113,122,131,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,129,137,136,136,136,129,148,113],
[114,0,116,125,114,113,126,108,127,120],
[121,134,0,127,140,136,131,135,131,125],
[113,125,123,0,120,121,132,113,127,114],
[114,136,110,130,0,131,140,120,134,129],
[114,137,114,129,119,0,133,113,137,126],
[114,124,119,118,110,117,0,114,133,119],
[121,142,115,137,130,137,136,0,150,115],
[102,123,119,123,116,113,117,100,0,111],
[137,130,125,136,121,124,131,135,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,138,119,133,126,125,123,131,133],
[133,0,147,122,144,130,132,128,137,145],
[112,103,0,100,113,100,109,110,98,111],
[131,128,150,0,123,129,129,136,133,145],
[117,106,137,127,0,121,132,113,128,146],
[124,120,150,121,129,0,132,135,128,144],
[125,118,141,121,118,118,0,119,130,138],
[127,122,140,114,137,115,131,0,130,147],
[119,113,152,117,122,122,120,120,0,135],
[117,105,139,105,104,106,112,103,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,122,116,122,121,113,119,126,128],
[115,0,132,119,121,121,120,130,127,128],
[128,118,0,116,123,118,121,133,127,130],
[134,131,134,0,119,120,118,132,127,127],
[128,129,127,131,0,119,119,128,122,128],
[129,129,132,130,131,0,126,124,126,124],
[137,130,129,132,131,124,0,128,127,126],
[131,120,117,118,122,126,122,0,125,126],
[124,123,123,123,128,124,123,125,0,119],
[122,122,120,123,122,126,124,124,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,113,123,134,111,144,120,138,123],
[126,0,121,132,136,117,127,139,138,125],
[137,129,0,107,130,110,139,134,151,136],
[127,118,143,0,128,136,156,127,149,111],
[116,114,120,122,0,128,117,137,124,140],
[139,133,140,114,122,0,147,140,144,118],
[106,123,111,94,133,103,0,124,140,118],
[130,111,116,123,113,110,126,0,113,113],
[112,112,99,101,126,106,110,137,0,112],
[127,125,114,139,110,132,132,137,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,108,82,118,85,122,141,115,126],
[156,0,115,63,135,140,135,164,111,148],
[142,135,0,77,105,126,104,119,114,65],
[168,187,173,0,102,139,149,133,167,147],
[132,115,145,148,0,132,124,183,126,123],
[165,110,124,111,118,0,142,143,141,122],
[128,115,146,101,126,108,0,104,145,147],
[109,86,131,117,67,107,146,0,100,109],
[135,139,136,83,124,109,105,150,0,101],
[124,102,185,103,127,128,103,141,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,128,117,115,116,126,131,115,127],
[106,0,123,113,101,109,122,121,106,113],
[122,127,0,136,115,116,133,144,135,132],
[133,137,114,0,131,126,127,149,123,131],
[135,149,135,119,0,143,151,146,123,140],
[134,141,134,124,107,0,127,131,115,141],
[124,128,117,123,99,123,0,123,109,134],
[119,129,106,101,104,119,127,0,115,124],
[135,144,115,127,127,135,141,135,0,145],
[123,137,118,119,110,109,116,126,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,91,135,162,92,118,129,94,79,107],
[159,0,159,163,150,159,124,130,90,117],
[115,91,0,111,86,84,104,77,51,105],
[88,87,139,0,108,104,91,97,67,92],
[158,100,164,142,0,140,127,110,89,119],
[132,91,166,146,110,0,135,121,90,125],
[121,126,146,159,123,115,0,120,93,124],
[156,120,173,153,140,129,130,0,129,129],
[171,160,199,183,161,160,157,121,0,143],
[143,133,145,158,131,125,126,121,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,121,121,129,133,117,119,118,130],
[110,0,117,108,124,120,127,115,107,110],
[129,133,0,110,136,123,124,124,116,119],
[129,142,140,0,143,131,141,134,125,138],
[121,126,114,107,0,126,113,121,110,126],
[117,130,127,119,124,0,133,123,107,123],
[133,123,126,109,137,117,0,125,118,125],
[131,135,126,116,129,127,125,0,115,128],
[132,143,134,125,140,143,132,135,0,139],
[120,140,131,112,124,127,125,122,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,104,111,110,120,118,107,120,102],
[155,0,128,133,119,118,141,150,136,140],
[146,122,0,116,122,122,115,139,121,114],
[139,117,134,0,117,115,137,132,130,125],
[140,131,128,133,0,127,122,148,126,125],
[130,132,128,135,123,0,120,152,146,121],
[132,109,135,113,128,130,0,121,138,131],
[143,100,111,118,102,98,129,0,130,108],
[130,114,129,120,124,104,112,120,0,116],
[148,110,136,125,125,129,119,142,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,117,82,101,131,101,135,161,174],
[132,0,91,76,82,113,124,170,155,143],
[133,159,0,101,133,90,62,151,167,121],
[168,174,149,0,130,172,117,134,171,152],
[149,168,117,120,0,157,109,167,182,146],
[119,137,160,78,93,0,143,192,216,155],
[149,126,188,133,141,107,0,152,162,165],
[115,80,99,116,83,58,98,0,115,120],
[89,95,83,79,68,34,88,135,0,101],
[76,107,129,98,104,95,85,130,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,121,109,116,119,126,115,120,102],
[145,0,137,142,124,138,143,134,129,140],
[129,113,0,109,122,127,133,121,130,142],
[141,108,141,0,122,127,130,118,138,148],
[134,126,128,128,0,129,122,118,127,135],
[131,112,123,123,121,0,123,120,126,134],
[124,107,117,120,128,127,0,117,117,142],
[135,116,129,132,132,130,133,0,129,140],
[130,121,120,112,123,124,133,121,0,144],
[148,110,108,102,115,116,108,110,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,120,120,119,118,116,119,123,135],
[136,0,111,129,121,127,128,125,120,129],
[130,139,0,143,117,121,134,128,137,128],
[130,121,107,0,114,118,122,102,129,113],
[131,129,133,136,0,119,124,122,127,127],
[132,123,129,132,131,0,117,129,136,126],
[134,122,116,128,126,133,0,126,135,126],
[131,125,122,148,128,121,124,0,141,130],
[127,130,113,121,123,114,115,109,0,119],
[115,121,122,137,123,124,124,120,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,122,119,134,109,113,128,148,129],
[148,0,131,133,142,137,133,142,136,124],
[128,119,0,137,149,129,131,129,117,145],
[131,117,113,0,116,124,128,113,126,124],
[116,108,101,134,0,127,113,136,127,135],
[141,113,121,126,123,0,129,138,133,137],
[137,117,119,122,137,121,0,132,137,127],
[122,108,121,137,114,112,118,0,129,136],
[102,114,133,124,123,117,113,121,0,130],
[121,126,105,126,115,113,123,114,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,136,148,134,124,149,151,124,172],
[129,0,141,180,111,137,151,159,159,98],
[114,109,0,106,78,161,118,125,147,117],
[102,70,144,0,76,102,103,130,135,112],
[116,139,172,174,0,157,125,157,160,134],
[126,113,89,148,93,0,102,155,144,117],
[101,99,132,147,125,148,0,154,109,145],
[99,91,125,120,93,95,96,0,117,117],
[126,91,103,115,90,106,141,133,0,94],
[78,152,133,138,116,133,105,133,156,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,122,113,115,129,124,131,123,117],
[112,0,107,114,113,129,117,128,112,123],
[128,143,0,122,129,134,125,130,120,129],
[137,136,128,0,128,133,134,138,126,124],
[135,137,121,122,0,139,125,132,131,121],
[121,121,116,117,111,0,114,128,112,119],
[126,133,125,116,125,136,0,127,125,119],
[119,122,120,112,118,122,123,0,124,125],
[127,138,130,124,119,138,125,126,0,122],
[133,127,121,126,129,131,131,125,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,122,128,139,127,129,118,132,133],
[127,0,113,113,132,145,124,122,134,133],
[128,137,0,133,138,137,129,126,132,125],
[122,137,117,0,135,132,132,127,130,121],
[111,118,112,115,0,132,124,120,127,117],
[123,105,113,118,118,0,128,114,133,122],
[121,126,121,118,126,122,0,120,122,130],
[132,128,124,123,130,136,130,0,134,130],
[118,116,118,120,123,117,128,116,0,132],
[117,117,125,129,133,128,120,120,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,131,130,128,122,122,131,129,124],
[106,0,110,111,103,104,93,106,118,116],
[119,140,0,116,121,120,120,117,122,123],
[120,139,134,0,123,118,129,123,129,128],
[122,147,129,127,0,128,122,126,139,130],
[128,146,130,132,122,0,118,128,134,143],
[128,157,130,121,128,132,0,125,138,130],
[119,144,133,127,124,122,125,0,128,129],
[121,132,128,121,111,116,112,122,0,113],
[126,134,127,122,120,107,120,121,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,127,119,128,129,122,129,120],
[128,0,131,116,131,134,122,125,123,112],
[123,119,0,127,124,148,129,116,126,117],
[123,134,123,0,129,133,111,133,117,121],
[131,119,126,121,0,145,124,124,131,120],
[122,116,102,117,105,0,110,105,124,105],
[121,128,121,139,126,140,0,126,129,125],
[128,125,134,117,126,145,124,0,137,112],
[121,127,124,133,119,126,121,113,0,104],
[130,138,133,129,130,145,125,138,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,117,124,118,129,127,124,133,128],
[128,0,121,132,128,123,118,116,125,128],
[133,129,0,137,142,123,136,132,142,135],
[126,118,113,0,110,121,120,118,126,122],
[132,122,108,140,0,120,127,124,136,131],
[121,127,127,129,130,0,128,123,128,131],
[123,132,114,130,123,122,0,118,128,121],
[126,134,118,132,126,127,132,0,126,130],
[117,125,108,124,114,122,122,124,0,118],
[122,122,115,128,119,119,129,120,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,121,118,120,142,123,125,141,135],
[140,0,127,127,132,147,143,123,131,142],
[129,123,0,133,127,150,131,124,130,149],
[132,123,117,0,138,138,118,121,137,128],
[130,118,123,112,0,143,130,123,132,121],
[108,103,100,112,107,0,109,107,121,119],
[127,107,119,132,120,141,0,118,134,133],
[125,127,126,129,127,143,132,0,135,140],
[109,119,120,113,118,129,116,115,0,123],
[115,108,101,122,129,131,117,110,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,105,110,128,110,108,120,127,114],
[125,0,99,89,120,111,114,118,136,103],
[145,151,0,126,146,127,148,116,136,126],
[140,161,124,0,138,137,135,134,143,142],
[122,130,104,112,0,108,126,111,112,110],
[140,139,123,113,142,0,147,126,140,125],
[142,136,102,115,124,103,0,119,113,114],
[130,132,134,116,139,124,131,0,126,113],
[123,114,114,107,138,110,137,124,0,113],
[136,147,124,108,140,125,136,137,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,131,159,143,139,151,147,125,158],
[105,0,131,147,120,133,126,135,111,143],
[119,119,0,137,122,143,117,147,122,142],
[91,103,113,0,107,104,109,118,98,108],
[107,130,128,143,0,135,126,138,140,143],
[111,117,107,146,115,0,111,135,124,140],
[99,124,133,141,124,139,0,145,114,146],
[103,115,103,132,112,115,105,0,119,128],
[125,139,128,152,110,126,136,131,0,162],
[92,107,108,142,107,110,104,122,88,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,118,157,131,133,127,140,124,135],
[105,0,85,108,104,122,96,105,118,119],
[132,165,0,159,139,136,114,132,135,134],
[93,142,91,0,115,115,102,138,112,116],
[119,146,111,135,0,113,129,136,132,136],
[117,128,114,135,137,0,110,126,108,137],
[123,154,136,148,121,140,0,139,140,147],
[110,145,118,112,114,124,111,0,133,133],
[126,132,115,138,118,142,110,117,0,145],
[115,131,116,134,114,113,103,117,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,97,103,110,99,114,115,105,123,93],
[153,0,142,137,127,115,159,147,142,130],
[147,108,0,116,136,120,157,108,128,118],
[140,113,134,0,139,149,143,124,113,106],
[151,123,114,111,0,131,152,127,141,139],
[136,135,130,101,119,0,154,105,124,142],
[135,91,93,107,98,96,0,120,130,106],
[145,103,142,126,123,145,130,0,121,130],
[127,108,122,137,109,126,120,129,0,144],
[157,120,132,144,111,108,144,120,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,109,120,110,106,115,117,119,96],
[140,0,132,129,133,129,135,146,120,123],
[141,118,0,135,121,122,144,110,135,119],
[130,121,115,0,104,135,110,126,110,100],
[140,117,129,146,0,125,137,120,124,130],
[144,121,128,115,125,0,151,119,130,109],
[135,115,106,140,113,99,0,117,115,116],
[133,104,140,124,130,131,133,0,139,133],
[131,130,115,140,126,120,135,111,0,108],
[154,127,131,150,120,141,134,117,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,131,139,148,124,136,134,142,143],
[128,0,141,130,134,134,120,131,136,144],
[119,109,0,132,144,118,116,123,128,137],
[111,120,118,0,133,112,121,115,116,133],
[102,116,106,117,0,117,112,123,130,133],
[126,116,132,138,133,0,120,117,128,131],
[114,130,134,129,138,130,0,116,132,137],
[116,119,127,135,127,133,134,0,131,149],
[108,114,122,134,120,122,118,119,0,133],
[107,106,113,117,117,119,113,101,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,155,155,134,151,153,125,142,133,147],
[95,0,129,104,96,109,108,96,110,95],
[95,121,0,102,112,107,102,80,102,91],
[116,146,148,0,124,125,128,123,133,111],
[99,154,138,126,0,138,131,125,137,121],
[97,141,143,125,112,0,106,120,155,105],
[125,142,148,122,119,144,0,138,136,140],
[108,154,170,127,125,130,112,0,138,127],
[117,140,148,117,113,95,114,112,0,129],
[103,155,159,139,129,145,110,123,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,124,125,118,127,120,106,124,113],
[124,0,121,114,124,113,110,111,117,124],
[126,129,0,111,124,126,114,107,122,123],
[125,136,139,0,134,128,140,130,141,127],
[132,126,126,116,0,130,120,123,127,119],
[123,137,124,122,120,0,115,110,118,115],
[130,140,136,110,130,135,0,118,127,130],
[144,139,143,120,127,140,132,0,130,128],
[126,133,128,109,123,132,123,120,0,126],
[137,126,127,123,131,135,120,122,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,125,118,127,129,104,120,104,113],
[122,0,137,131,118,119,130,116,134,126],
[125,113,0,144,119,114,117,133,113,116],
[132,119,106,0,119,121,126,124,109,105],
[123,132,131,131,0,129,116,130,111,110],
[121,131,136,129,121,0,125,126,110,109],
[146,120,133,124,134,125,0,122,104,106],
[130,134,117,126,120,124,128,0,109,115],
[146,116,137,141,139,140,146,141,0,137],
[137,124,134,145,140,141,144,135,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,134,133,119,124,121,126,132,120],
[125,0,131,130,132,128,136,134,132,132],
[116,119,0,122,119,120,123,123,120,112],
[117,120,128,0,110,124,123,116,131,124],
[131,118,131,140,0,141,125,133,130,132],
[126,122,130,126,109,0,128,126,129,126],
[129,114,127,127,125,122,0,130,126,123],
[124,116,127,134,117,124,120,0,129,127],
[118,118,130,119,120,121,124,121,0,114],
[130,118,138,126,118,124,127,123,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,132,126,125,132,130,146,116,129],
[127,0,127,104,122,131,123,127,115,109],
[118,123,0,118,126,133,118,126,119,112],
[124,146,132,0,135,136,139,132,123,131],
[125,128,124,115,0,139,125,144,130,108],
[118,119,117,114,111,0,120,133,118,107],
[120,127,132,111,125,130,0,128,120,116],
[104,123,124,118,106,117,122,0,122,108],
[134,135,131,127,120,132,130,128,0,108],
[121,141,138,119,142,143,134,142,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,123,159,140,143,134,146,141,146],
[127,0,125,142,140,137,131,143,125,140],
[127,125,0,127,142,117,117,130,131,143],
[91,108,123,0,119,98,97,107,106,121],
[110,110,108,131,0,117,97,129,134,135],
[107,113,133,152,133,0,121,129,139,139],
[116,119,133,153,153,129,0,147,118,133],
[104,107,120,143,121,121,103,0,133,126],
[109,125,119,144,116,111,132,117,0,138],
[104,110,107,129,115,111,117,124,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,132,125,110,110,126,98,99,115],
[124,0,141,123,119,129,142,111,136,123],
[118,109,0,119,134,148,142,112,119,126],
[125,127,131,0,128,147,148,128,129,125],
[140,131,116,122,0,149,158,103,136,124],
[140,121,102,103,101,0,145,97,112,116],
[124,108,108,102,92,105,0,92,121,103],
[152,139,138,122,147,153,158,0,138,134],
[151,114,131,121,114,138,129,112,0,129],
[135,127,124,125,126,134,147,116,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,122,128,128,130,119,123,124,143],
[131,0,137,128,142,135,128,129,118,146],
[128,113,0,130,120,132,122,122,110,144],
[122,122,120,0,125,120,129,119,127,133],
[122,108,130,125,0,130,122,115,120,133],
[120,115,118,130,120,0,117,112,118,142],
[131,122,128,121,128,133,0,119,114,130],
[127,121,128,131,135,138,131,0,126,148],
[126,132,140,123,130,132,136,124,0,136],
[107,104,106,117,117,108,120,102,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,114,131,126,106,116,116,115,134],
[136,0,111,112,127,126,119,148,107,133],
[136,139,0,120,139,133,138,138,126,159],
[119,138,130,0,136,132,136,125,115,137],
[124,123,111,114,0,123,128,112,101,130],
[144,124,117,118,127,0,124,128,117,135],
[134,131,112,114,122,126,0,139,129,129],
[134,102,112,125,138,122,111,0,108,136],
[135,143,124,135,149,133,121,142,0,134],
[116,117,91,113,120,115,121,114,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,129,124,109,112,144,133,127],
[123,0,108,120,125,117,125,141,131,125],
[127,142,0,131,135,133,122,151,141,135],
[121,130,119,0,142,120,129,159,144,130],
[126,125,115,108,0,113,102,139,129,127],
[141,133,117,130,137,0,122,150,151,134],
[138,125,128,121,148,128,0,152,140,129],
[106,109,99,91,111,100,98,0,108,121],
[117,119,109,106,121,99,110,142,0,115],
[123,125,115,120,123,116,121,129,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,142,118,134,134,126,127,116,117],
[133,0,115,116,127,127,128,118,114,113],
[108,135,0,107,123,123,107,113,100,123],
[132,134,143,0,149,144,130,132,124,132],
[116,123,127,101,0,121,119,123,102,115],
[116,123,127,106,129,0,120,133,102,122],
[124,122,143,120,131,130,0,130,125,123],
[123,132,137,118,127,117,120,0,123,121],
[134,136,150,126,148,148,125,127,0,118],
[133,137,127,118,135,128,127,129,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,130,131,110,131,115,125,128,123],
[107,0,105,113,117,105,105,112,113,115],
[120,145,0,128,132,140,127,134,131,130],
[119,137,122,0,118,132,137,140,123,132],
[140,133,118,132,0,136,122,132,134,124],
[119,145,110,118,114,0,128,133,132,123],
[135,145,123,113,128,122,0,131,131,133],
[125,138,116,110,118,117,119,0,122,132],
[122,137,119,127,116,118,119,128,0,123],
[127,135,120,118,126,127,117,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,122,117,138,131,115,116,131,118],
[103,0,104,104,127,125,110,106,125,108],
[128,146,0,127,146,127,130,126,123,117],
[133,146,123,0,149,130,123,124,135,127],
[112,123,104,101,0,106,104,106,120,101],
[119,125,123,120,144,0,123,119,128,110],
[135,140,120,127,146,127,0,115,120,125],
[134,144,124,126,144,131,135,0,121,127],
[119,125,127,115,130,122,130,129,0,110],
[132,142,133,123,149,140,125,123,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,133,116,132,122,117,122,137,116],
[114,0,122,108,134,117,100,131,122,109],
[117,128,0,113,123,128,119,120,127,121],
[134,142,137,0,131,137,124,134,140,132],
[118,116,127,119,0,119,110,133,123,118],
[128,133,122,113,131,0,113,117,117,113],
[133,150,131,126,140,137,0,138,127,118],
[128,119,130,116,117,133,112,0,133,108],
[113,128,123,110,127,133,123,117,0,111],
[134,141,129,118,132,137,132,142,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,96,65,121,89,112,89,81,142,82],
[154,0,91,93,100,128,108,112,120,129],
[185,159,0,111,116,105,133,129,122,153],
[129,157,139,0,89,110,124,100,159,129],
[161,150,134,161,0,143,133,110,144,157],
[138,122,145,140,107,0,123,100,126,137],
[161,142,117,126,117,127,0,116,161,144],
[169,138,121,150,140,150,134,0,161,183],
[108,130,128,91,106,124,89,89,0,100],
[168,121,97,121,93,113,106,67,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,123,120,124,127,128,140,127,120],
[133,0,126,134,134,139,134,146,122,125],
[127,124,0,132,120,131,146,144,127,118],
[130,116,118,0,124,117,125,135,124,104],
[126,116,130,126,0,121,141,133,123,123],
[123,111,119,133,129,0,129,143,130,124],
[122,116,104,125,109,121,0,124,105,124],
[110,104,106,115,117,107,126,0,107,106],
[123,128,123,126,127,120,145,143,0,116],
[130,125,132,146,127,126,126,144,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,100,90,85,127,102,95,121,126],
[145,0,135,99,128,144,114,125,138,144],
[150,115,0,124,133,142,138,93,123,109],
[160,151,126,0,122,169,136,144,146,157],
[165,122,117,128,0,136,112,137,144,130],
[123,106,108,81,114,0,107,94,116,116],
[148,136,112,114,138,143,0,115,128,127],
[155,125,157,106,113,156,135,0,119,160],
[129,112,127,104,106,134,122,131,0,139],
[124,106,141,93,120,134,123,90,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,77,139,118,106,134,143,94,121],
[128,0,115,105,106,143,125,128,94,140],
[173,135,0,157,97,143,217,93,87,138],
[111,145,93,0,62,91,89,76,53,62],
[132,144,153,188,0,120,184,158,136,122],
[144,107,107,159,130,0,151,128,109,138],
[116,125,33,161,66,99,0,83,21,100],
[107,122,157,174,92,122,167,0,133,100],
[156,156,163,197,114,141,229,117,0,141],
[129,110,112,188,128,112,150,150,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,132,142,134,132,132,110,136,132],
[119,0,130,144,135,132,120,130,126,123],
[118,120,0,122,122,124,114,102,128,118],
[108,106,128,0,114,128,111,113,104,112],
[116,115,128,136,0,124,119,116,136,116],
[118,118,126,122,126,0,114,115,131,127],
[118,130,136,139,131,136,0,117,126,127],
[140,120,148,137,134,135,133,0,127,127],
[114,124,122,146,114,119,124,123,0,125],
[118,127,132,138,134,123,123,123,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,161,148,157,149,114,130,133,139],
[105,0,141,120,149,142,107,140,96,105],
[89,109,0,86,102,66,59,67,98,106],
[102,130,164,0,179,138,97,149,144,137],
[93,101,148,71,0,91,54,94,84,112],
[101,108,184,112,159,0,132,168,89,150],
[136,143,191,153,196,118,0,150,112,138],
[120,110,183,101,156,82,100,0,97,121],
[117,154,152,106,166,161,138,153,0,204],
[111,145,144,113,138,100,112,129,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,133,125,136,118,129,115,128,115],
[128,0,126,115,143,130,140,121,116,117],
[117,124,0,115,136,118,131,114,109,121],
[125,135,135,0,141,134,130,125,124,126],
[114,107,114,109,0,110,115,116,103,121],
[132,120,132,116,140,0,135,121,128,131],
[121,110,119,120,135,115,0,114,119,117],
[135,129,136,125,134,129,136,0,124,124],
[122,134,141,126,147,122,131,126,0,135],
[135,133,129,124,129,119,133,126,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,118,113,103,115,120,114,123,118],
[122,0,115,114,109,107,121,110,117,114],
[132,135,0,111,128,119,132,122,139,114],
[137,136,139,0,118,122,138,129,132,135],
[147,141,122,132,0,128,136,121,128,123],
[135,143,131,128,122,0,125,131,130,117],
[130,129,118,112,114,125,0,121,128,107],
[136,140,128,121,129,119,129,0,128,120],
[127,133,111,118,122,120,122,122,0,112],
[132,136,136,115,127,133,143,130,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,109,108,136,119,111,148,138,123],
[140,0,131,128,120,124,121,134,129,140],
[141,119,0,114,116,138,118,155,121,108],
[142,122,136,0,146,128,136,139,110,132],
[114,130,134,104,0,111,106,138,139,124],
[131,126,112,122,139,0,96,159,136,119],
[139,129,132,114,144,154,0,146,135,136],
[102,116,95,111,112,91,104,0,113,128],
[112,121,129,140,111,114,115,137,0,130],
[127,110,142,118,126,131,114,122,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,141,132,127,110,144,120,134,128],
[131,0,141,147,132,129,118,140,136,133],
[109,109,0,108,124,109,105,108,134,111],
[118,103,142,0,132,105,105,126,148,131],
[123,118,126,118,0,102,123,116,129,116],
[140,121,141,145,148,0,128,128,152,133],
[106,132,145,145,127,122,0,134,142,125],
[130,110,142,124,134,122,116,0,132,112],
[116,114,116,102,121,98,108,118,0,111],
[122,117,139,119,134,117,125,138,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,116,126,128,124,129,122,116,123],
[124,0,118,125,123,127,122,115,123,127],
[134,132,0,134,128,130,134,122,129,137],
[124,125,116,0,135,116,121,123,112,122],
[122,127,122,115,0,114,113,120,116,119],
[126,123,120,134,136,0,131,129,118,134],
[121,128,116,129,137,119,0,124,124,121],
[128,135,128,127,130,121,126,0,118,129],
[134,127,121,138,134,132,126,132,0,124],
[127,123,113,128,131,116,129,121,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,131,118,127,121,121,123,109,119],
[135,0,129,123,129,125,117,137,118,130],
[119,121,0,103,128,107,106,125,116,122],
[132,127,147,0,132,125,123,141,128,129],
[123,121,122,118,0,120,116,137,116,122],
[129,125,143,125,130,0,122,132,121,116],
[129,133,144,127,134,128,0,124,136,129],
[127,113,125,109,113,118,126,0,122,107],
[141,132,134,122,134,129,114,128,0,131],
[131,120,128,121,128,134,121,143,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,127,127,129,120,128,113,119,112],
[120,0,130,133,117,126,128,124,126,128],
[123,120,0,124,125,124,129,123,115,116],
[123,117,126,0,109,119,119,109,124,119],
[121,133,125,141,0,127,133,115,127,121],
[130,124,126,131,123,0,124,125,132,117],
[122,122,121,131,117,126,0,129,123,117],
[137,126,127,141,135,125,121,0,127,119],
[131,124,135,126,123,118,127,123,0,122],
[138,122,134,131,129,133,133,131,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,162,121,151,124,128,128,127,131],
[115,0,144,128,143,131,138,133,129,124],
[88,106,0,108,120,95,114,105,75,92],
[129,122,142,0,127,116,136,126,101,126],
[99,107,130,123,0,113,132,121,109,88],
[126,119,155,134,137,0,128,141,115,123],
[122,112,136,114,118,122,0,111,106,111],
[122,117,145,124,129,109,139,0,111,104],
[123,121,175,149,141,135,144,139,0,113],
[119,126,158,124,162,127,139,146,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,167,128,146,135,114,195,143,143,153],
[83,0,117,102,94,92,132,78,141,115],
[122,133,0,159,130,116,158,81,156,144],
[104,148,91,0,111,72,158,68,125,72],
[115,156,120,139,0,113,217,137,135,133],
[136,158,134,178,137,0,196,161,142,117],
[55,118,92,92,33,54,0,43,123,44],
[107,172,169,182,113,89,207,0,144,138],
[107,109,94,125,115,108,127,106,0,83],
[97,135,106,178,117,133,206,112,167,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,134,120,121,118,122,126,130,135],
[142,0,139,130,118,146,126,127,121,125],
[116,111,0,131,112,119,117,118,114,116],
[130,120,119,0,119,120,110,137,114,105],
[129,132,138,131,0,128,120,134,125,116],
[132,104,131,130,122,0,129,130,118,128],
[128,124,133,140,130,121,0,128,127,139],
[124,123,132,113,116,120,122,0,121,111],
[120,129,136,136,125,132,123,129,0,111],
[115,125,134,145,134,122,111,139,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,133,114,120,119,128,128,117,126],
[114,0,128,115,116,114,123,111,115,115],
[117,122,0,114,122,124,126,119,113,122],
[136,135,136,0,137,133,131,137,122,130],
[130,134,128,113,0,122,126,123,118,130],
[131,136,126,117,128,0,121,133,125,123],
[122,127,124,119,124,129,0,123,123,126],
[122,139,131,113,127,117,127,0,116,131],
[133,135,137,128,132,125,127,134,0,139],
[124,135,128,120,120,127,124,119,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,114,144,125,123,110,145,110,120],
[120,0,127,127,135,131,117,151,112,138],
[136,123,0,142,125,127,126,140,141,143],
[106,123,108,0,119,113,112,125,103,125],
[125,115,125,131,0,136,117,128,115,133],
[127,119,123,137,114,0,123,126,125,130],
[140,133,124,138,133,127,0,138,134,129],
[105,99,110,125,122,124,112,0,98,128],
[140,138,109,147,135,125,116,152,0,156],
[130,112,107,125,117,120,121,122,94,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,165,133,153,148,159,158,161,133],
[146,0,140,129,146,111,167,150,153,129],
[85,110,0,129,114,84,123,130,117,113],
[117,121,121,0,152,139,160,164,103,144],
[97,104,136,98,0,108,136,115,132,116],
[102,139,166,111,142,0,140,154,141,116],
[91,83,127,90,114,110,0,112,104,107],
[92,100,120,86,135,96,138,0,132,121],
[89,97,133,147,118,109,146,118,0,106],
[117,121,137,106,134,134,143,129,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,126,123,138,134,117,131,139,127],
[113,0,138,130,134,129,126,128,127,129],
[124,112,0,114,138,123,115,112,126,117],
[127,120,136,0,139,120,116,120,127,119],
[112,116,112,111,0,117,101,106,116,106],
[116,121,127,130,133,0,127,117,127,119],
[133,124,135,134,149,123,0,126,135,120],
[119,122,138,130,144,133,124,0,129,128],
[111,123,124,123,134,123,115,121,0,122],
[123,121,133,131,144,131,130,122,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,135,122,125,136,128,129,109,127],
[118,0,131,125,124,131,121,132,121,121],
[115,119,0,116,116,124,118,117,110,113],
[128,125,134,0,126,132,121,133,127,126],
[125,126,134,124,0,125,122,131,121,120],
[114,119,126,118,125,0,121,125,118,108],
[122,129,132,129,128,129,0,131,124,135],
[121,118,133,117,119,125,119,0,117,116],
[141,129,140,123,129,132,126,133,0,121],
[123,129,137,124,130,142,115,134,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,133,122,124,127,134,107,129,119],
[121,0,119,114,121,116,133,109,115,122],
[117,131,0,120,126,124,128,122,130,116],
[128,136,130,0,125,133,136,126,137,126],
[126,129,124,125,0,125,130,113,127,114],
[123,134,126,117,125,0,136,118,124,120],
[116,117,122,114,120,114,0,108,117,110],
[143,141,128,124,137,132,142,0,135,135],
[121,135,120,113,123,126,133,115,0,120],
[131,128,134,124,136,130,140,115,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,134,131,132,120,133,135,143,133],
[106,0,125,121,111,114,128,122,129,118],
[116,125,0,127,115,123,133,123,132,135],
[119,129,123,0,119,117,134,131,115,125],
[118,139,135,131,0,128,136,134,127,125],
[130,136,127,133,122,0,132,120,143,133],
[117,122,117,116,114,118,0,132,134,126],
[115,128,127,119,116,130,118,0,124,129],
[107,121,118,135,123,107,116,126,0,118],
[117,132,115,125,125,117,124,121,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,161,135,134,122,138,137,112,167],
[119,0,133,121,126,129,154,90,123,119],
[89,117,0,119,118,100,148,89,114,137],
[115,129,131,0,139,105,93,111,90,135],
[116,124,132,111,0,85,144,112,147,135],
[128,121,150,145,165,0,158,131,134,150],
[112,96,102,157,106,92,0,77,64,133],
[113,160,161,139,138,119,173,0,149,165],
[138,127,136,160,103,116,186,101,0,123],
[83,131,113,115,115,100,117,85,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,102,99,111,94,97,97,91,93],
[140,0,128,115,141,123,107,119,124,117],
[148,122,0,107,132,109,98,99,114,101],
[151,135,143,0,128,109,102,114,120,127],
[139,109,118,122,0,91,86,126,102,107],
[156,127,141,141,159,0,122,137,136,122],
[153,143,152,148,164,128,0,149,145,116],
[153,131,151,136,124,113,101,0,123,106],
[159,126,136,130,148,114,105,127,0,109],
[157,133,149,123,143,128,134,144,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,117,128,130,74,136,128,148,76],
[148,0,126,127,83,131,148,161,106,98],
[133,124,0,98,72,85,125,116,110,69],
[122,123,152,0,150,124,122,140,136,128],
[120,167,178,100,0,142,174,112,156,140],
[176,119,165,126,108,0,156,183,128,137],
[114,102,125,128,76,94,0,105,97,120],
[122,89,134,110,138,67,145,0,118,69],
[102,144,140,114,94,122,153,132,0,117],
[174,152,181,122,110,113,130,181,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,131,138,125,133,127,137,122,122],
[129,0,130,132,122,114,134,130,143,137],
[119,120,0,123,129,135,152,141,125,136],
[112,118,127,0,108,119,126,129,111,121],
[125,128,121,142,0,120,131,131,129,132],
[117,136,115,131,130,0,133,123,121,128],
[123,116,98,124,119,117,0,110,117,121],
[113,120,109,121,119,127,140,0,119,114],
[128,107,125,139,121,129,133,131,0,136],
[128,113,114,129,118,122,129,136,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,121,124,116,127,121,127,122,125],
[116,0,116,112,120,136,112,127,126,110],
[129,134,0,128,133,134,134,138,130,125],
[126,138,122,0,117,137,129,133,134,117],
[134,130,117,133,0,123,123,132,129,119],
[123,114,116,113,127,0,116,122,126,117],
[129,138,116,121,127,134,0,142,130,122],
[123,123,112,117,118,128,108,0,129,110],
[128,124,120,116,121,124,120,121,0,109],
[125,140,125,133,131,133,128,140,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,127,119,126,113,130,127,131,126],
[121,0,138,121,129,124,132,119,131,123],
[123,112,0,124,115,124,129,116,128,125],
[131,129,126,0,124,124,129,124,143,125],
[124,121,135,126,0,128,133,117,132,121],
[137,126,126,126,122,0,126,117,126,129],
[120,118,121,121,117,124,0,121,120,117],
[123,131,134,126,133,133,129,0,135,139],
[119,119,122,107,118,124,130,115,0,118],
[124,127,125,125,129,121,133,111,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,116,122,143,150,118,131,145,146],
[137,0,125,145,144,161,125,130,134,150],
[134,125,0,127,120,139,139,138,145,127],
[128,105,123,0,125,123,132,115,126,127],
[107,106,130,125,0,127,129,122,135,123],
[100,89,111,127,123,0,116,115,124,120],
[132,125,111,118,121,134,0,107,140,118],
[119,120,112,135,128,135,143,0,131,137],
[105,116,105,124,115,126,110,119,0,105],
[104,100,123,123,127,130,132,113,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,53,153,140,83,96,81,78,59],
[175,0,125,181,155,127,156,124,130,128],
[197,125,0,176,190,150,196,130,128,128],
[97,69,74,0,116,80,60,95,108,80],
[110,95,60,134,0,77,98,113,69,96],
[167,123,100,170,173,0,159,139,130,86],
[154,94,54,190,152,91,0,110,99,104],
[169,126,120,155,137,111,140,0,126,103],
[172,120,122,142,181,120,151,124,0,116],
[191,122,122,170,154,164,146,147,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,125,125,125,131,131,116,122,132],
[132,0,128,129,133,130,131,126,119,129],
[125,122,0,129,119,124,126,120,127,135],
[125,121,121,0,125,126,125,121,119,123],
[125,117,131,125,0,128,137,127,121,133],
[119,120,126,124,122,0,128,117,122,125],
[119,119,124,125,113,122,0,121,117,122],
[134,124,130,129,123,133,129,0,119,134],
[128,131,123,131,129,128,133,131,0,126],
[118,121,115,127,117,125,128,116,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,125,118,131,107,108,122,116,116],
[144,0,118,126,145,118,119,120,118,123],
[125,132,0,120,126,127,124,125,129,119],
[132,124,130,0,131,109,124,129,115,134],
[119,105,124,119,0,117,103,99,106,113],
[143,132,123,141,133,0,138,144,140,134],
[142,131,126,126,147,112,0,129,122,136],
[128,130,125,121,151,106,121,0,131,135],
[134,132,121,135,144,110,128,119,0,130],
[134,127,131,116,137,116,114,115,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,148,143,141,153,134,138,122,124],
[118,0,122,128,120,131,128,133,125,138],
[102,128,0,133,126,130,124,115,108,133],
[107,122,117,0,124,118,116,116,103,116],
[109,130,124,126,0,144,115,125,124,125],
[97,119,120,132,106,0,104,122,115,113],
[116,122,126,134,135,146,0,155,132,119],
[112,117,135,134,125,128,95,0,117,112],
[128,125,142,147,126,135,118,133,0,133],
[126,112,117,134,125,137,131,138,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,125,134,149,148,113,122,117,116],
[112,0,124,119,133,146,117,119,114,116],
[125,126,0,130,159,150,126,138,126,138],
[116,131,120,0,151,138,119,141,108,118],
[101,117,91,99,0,119,99,99,105,94],
[102,104,100,112,131,0,126,125,103,136],
[137,133,124,131,151,124,0,144,120,137],
[128,131,112,109,151,125,106,0,108,111],
[133,136,124,142,145,147,130,142,0,147],
[134,134,112,132,156,114,113,139,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,118,118,117,137,112,132,125,142],
[111,0,121,115,118,123,118,126,110,132],
[132,129,0,127,130,120,121,133,126,141],
[132,135,123,0,128,130,126,139,126,150],
[133,132,120,122,0,146,126,127,133,132],
[113,127,130,120,104,0,124,116,121,137],
[138,132,129,124,124,126,0,136,126,148],
[118,124,117,111,123,134,114,0,122,143],
[125,140,124,124,117,129,124,128,0,138],
[108,118,109,100,118,113,102,107,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,115,122,106,121,111,118,118,103],
[133,0,119,131,123,118,118,123,111,115],
[135,131,0,136,108,112,116,119,114,102],
[128,119,114,0,112,118,113,113,117,115],
[144,127,142,138,0,137,133,127,129,112],
[129,132,138,132,113,0,116,131,116,115],
[139,132,134,137,117,134,0,119,127,124],
[132,127,131,137,123,119,131,0,130,112],
[132,139,136,133,121,134,123,120,0,127],
[147,135,148,135,138,135,126,138,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,118,137,126,133,134,119,126,119],
[128,0,131,141,125,129,142,137,134,120],
[132,119,0,139,135,143,142,117,129,113],
[113,109,111,0,112,126,134,115,123,119],
[124,125,115,138,0,130,135,123,126,125],
[117,121,107,124,120,0,138,118,136,113],
[116,108,108,116,115,112,0,112,120,108],
[131,113,133,135,127,132,138,0,137,117],
[124,116,121,127,124,114,130,113,0,99],
[131,130,137,131,125,137,142,133,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,102,138,119,112,127,128,133,134],
[146,0,122,158,130,130,130,131,123,141],
[148,128,0,139,108,124,134,114,137,129],
[112,92,111,0,103,108,97,98,136,109],
[131,120,142,147,0,116,143,126,139,124],
[138,120,126,142,134,0,115,138,145,131],
[123,120,116,153,107,135,0,118,133,134],
[122,119,136,152,124,112,132,0,138,107],
[117,127,113,114,111,105,117,112,0,101],
[116,109,121,141,126,119,116,143,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,113,80,84,158,141,92,111,126],
[146,0,109,116,147,183,158,107,123,123],
[137,141,0,111,153,163,111,120,87,126],
[170,134,139,0,120,153,124,82,121,120],
[166,103,97,130,0,172,157,115,126,106],
[92,67,87,97,78,0,94,43,66,71],
[109,92,139,126,93,156,0,73,145,106],
[158,143,130,168,135,207,177,0,112,115],
[139,127,163,129,124,184,105,138,0,140],
[124,127,124,130,144,179,144,135,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,123,138,121,115,142,126,124,121],
[118,0,133,133,125,124,134,128,130,125],
[127,117,0,135,135,124,146,126,142,123],
[112,117,115,0,118,118,129,118,117,122],
[129,125,115,132,0,125,132,130,129,126],
[135,126,126,132,125,0,140,125,124,123],
[108,116,104,121,118,110,0,121,117,115],
[124,122,124,132,120,125,129,0,144,128],
[126,120,108,133,121,126,133,106,0,129],
[129,125,127,128,124,127,135,122,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,105,149,144,118,116,150,144,126],
[110,0,100,126,115,95,99,123,109,112],
[145,150,0,157,138,120,148,159,151,126],
[101,124,93,0,139,121,102,148,136,130],
[106,135,112,111,0,102,121,122,134,137],
[132,155,130,129,148,0,111,131,140,140],
[134,151,102,148,129,139,0,142,150,145],
[100,127,91,102,128,119,108,0,135,118],
[106,141,99,114,116,110,100,115,0,109],
[124,138,124,120,113,110,105,132,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,139,143,117,131,147,130,144,156],
[117,0,126,120,123,126,141,123,128,139],
[111,124,0,154,111,124,145,121,149,126],
[107,130,96,0,131,117,125,113,131,115],
[133,127,139,119,0,96,130,141,149,140],
[119,124,126,133,154,0,151,141,160,142],
[103,109,105,125,120,99,0,119,155,126],
[120,127,129,137,109,109,131,0,155,127],
[106,122,101,119,101,90,95,95,0,105],
[94,111,124,135,110,108,124,123,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,127,122,120,137,131,136,131,149],
[120,0,126,119,124,126,119,130,116,128],
[123,124,0,110,112,128,131,146,136,135],
[128,131,140,0,125,136,142,136,140,132],
[130,126,138,125,0,138,136,144,136,155],
[113,124,122,114,112,0,145,128,133,130],
[119,131,119,108,114,105,0,131,134,119],
[114,120,104,114,106,122,119,0,115,131],
[119,134,114,110,114,117,116,135,0,134],
[101,122,115,118,95,120,131,119,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,115,124,108,113,132,129,113,128],
[132,0,110,122,118,109,132,124,106,113],
[135,140,0,145,133,133,145,136,130,124],
[126,128,105,0,125,114,137,126,110,122],
[142,132,117,125,0,114,140,124,117,126],
[137,141,117,136,136,0,145,148,122,127],
[118,118,105,113,110,105,0,131,104,117],
[121,126,114,124,126,102,119,0,115,126],
[137,144,120,140,133,128,146,135,0,127],
[122,137,126,128,124,123,133,124,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,132,113,125,118,133,122,109,133],
[118,0,114,108,128,104,122,114,122,124],
[118,136,0,113,130,116,124,133,133,133],
[137,142,137,0,138,131,138,139,125,139],
[125,122,120,112,0,109,130,134,122,128],
[132,146,134,119,141,0,131,133,133,121],
[117,128,126,112,120,119,0,136,128,125],
[128,136,117,111,116,117,114,0,122,127],
[141,128,117,125,128,117,122,128,0,142],
[117,126,117,111,122,129,125,123,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,114,90,147,168,172,173,139,209],
[104,0,124,136,139,149,124,173,112,173],
[136,126,0,128,103,149,176,133,131,139],
[160,114,122,0,127,119,127,181,118,151],
[103,111,147,123,0,168,140,123,123,192],
[82,101,101,131,82,0,111,111,106,49],
[78,126,74,123,110,139,0,140,102,146],
[77,77,117,69,127,139,110,0,143,110],
[111,138,119,132,127,144,148,107,0,168],
[41,77,111,99,58,201,104,140,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,160,170,159,193,166,134,136,128,109],
[90,0,148,170,149,144,137,94,82,121],
[80,102,0,185,127,161,81,104,112,75],
[91,80,65,0,105,158,117,105,116,86],
[57,101,123,145,0,161,87,71,99,50],
[84,106,89,92,89,0,76,110,101,87],
[116,113,169,133,163,174,0,102,139,86],
[114,156,146,145,179,140,148,0,97,173],
[122,168,138,134,151,149,111,153,0,149],
[141,129,175,164,200,163,164,77,101,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,121,134,132,141,126,121,132,135],
[111,0,119,133,121,136,120,118,119,126],
[129,131,0,130,132,138,131,125,125,131],
[116,117,120,0,127,126,130,125,113,123],
[118,129,118,123,0,131,113,120,109,127],
[109,114,112,124,119,0,105,109,116,122],
[124,130,119,120,137,145,0,131,133,131],
[129,132,125,125,130,141,119,0,137,125],
[118,131,125,137,141,134,117,113,0,134],
[115,124,119,127,123,128,119,125,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,116,140,114,131,130,129,132,114],
[131,0,129,146,116,138,130,98,146,97],
[134,121,0,136,138,127,138,118,141,110],
[110,104,114,0,101,109,107,93,113,106],
[136,134,112,149,0,127,136,120,146,124],
[119,112,123,141,123,0,134,102,136,85],
[120,120,112,143,114,116,0,121,129,96],
[121,152,132,157,130,148,129,0,138,141],
[118,104,109,137,104,114,121,112,0,112],
[136,153,140,144,126,165,154,109,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,140,147,125,135,117,145,121,127],
[123,0,135,127,117,142,113,134,115,120],
[110,115,0,129,114,132,111,129,110,109],
[103,123,121,0,122,125,120,133,103,107],
[125,133,136,128,0,118,117,131,108,118],
[115,108,118,125,132,0,113,126,111,115],
[133,137,139,130,133,137,0,139,117,128],
[105,116,121,117,119,124,111,0,95,104],
[129,135,140,147,142,139,133,155,0,120],
[123,130,141,143,132,135,122,146,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,114,94,130,99,95,104,124,121],
[146,0,133,122,144,131,127,136,123,130],
[136,117,0,102,125,112,113,119,107,116],
[156,128,148,0,129,128,112,139,128,150],
[120,106,125,121,0,120,111,141,104,132],
[151,119,138,122,130,0,120,146,124,134],
[155,123,137,138,139,130,0,145,130,148],
[146,114,131,111,109,104,105,0,108,123],
[126,127,143,122,146,126,120,142,0,141],
[129,120,134,100,118,116,102,127,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,113,135,111,112,120,122,127,137],
[122,0,112,128,101,112,118,126,129,129],
[137,138,0,139,125,138,129,131,132,138],
[115,122,111,0,108,109,122,115,131,116],
[139,149,125,142,0,130,131,152,144,131],
[138,138,112,141,120,0,127,135,134,137],
[130,132,121,128,119,123,0,127,139,130],
[128,124,119,135,98,115,123,0,138,135],
[123,121,118,119,106,116,111,112,0,117],
[113,121,112,134,119,113,120,115,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 250, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_250.csv", index=False, header=False)