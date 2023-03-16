
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,126,118,114,123,113,126,137,131,116],
[125,0,124,106,120,109,113,131,135,128],
[133,127,0,108,122,116,111,119,118,130],
[137,145,143,0,125,129,128,142,131,121],
[128,131,129,126,0,111,117,133,132,122],
[138,142,135,122,140,0,129,144,133,139],
[125,138,140,123,134,122,0,138,133,146],
[114,120,132,109,118,107,113,0,111,121],
[120,116,133,120,119,118,118,140,0,120],
[135,123,121,130,129,112,105,130,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,96,120,119,134,107,111,136,133],
[113,0,89,119,106,138,108,94,115,120],
[155,162,0,116,132,143,106,144,143,142],
[131,132,135,0,104,153,108,98,140,118],
[132,145,119,147,0,148,122,120,146,141],
[117,113,108,98,103,0,109,100,123,112],
[144,143,145,143,129,142,0,110,145,141],
[140,157,107,153,131,151,141,0,154,131],
[115,136,108,111,105,128,106,97,0,128],
[118,131,109,133,110,139,110,120,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,144,136,138,124,127,127,131,128],
[118,0,133,125,125,135,127,128,121,127],
[107,118,0,123,133,126,115,112,125,127],
[115,126,128,0,134,129,130,126,135,131],
[113,126,118,117,0,118,128,117,119,126],
[127,116,125,122,133,0,121,120,116,120],
[124,124,136,121,123,130,0,115,116,125],
[124,123,139,125,134,131,136,0,120,137],
[120,130,126,116,132,135,135,131,0,129],
[123,124,124,120,125,131,126,114,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,153,138,128,119,135,139,111,140,126],
[98,0,110,129,67,101,117,118,90,101],
[113,141,0,148,138,116,140,113,144,142],
[123,122,103,0,110,116,125,105,100,76],
[132,184,113,141,0,116,154,127,131,95],
[116,150,135,135,135,0,179,141,144,142],
[112,134,111,126,97,72,0,99,139,107],
[140,133,138,146,124,110,152,0,130,111],
[111,161,107,151,120,107,112,121,0,105],
[125,150,109,175,156,109,144,140,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,111,120,122,125,132,122,122,126],
[123,0,120,119,112,119,126,120,126,128],
[140,131,0,129,126,116,128,131,133,128],
[131,132,122,0,129,139,146,133,123,138],
[129,139,125,122,0,130,133,126,128,137],
[126,132,135,112,121,0,139,112,122,124],
[119,125,123,105,118,112,0,111,120,121],
[129,131,120,118,125,139,140,0,123,131],
[129,125,118,128,123,129,131,128,0,132],
[125,123,123,113,114,127,130,120,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,116,111,124,125,127,111,119,125],
[135,0,120,115,128,129,130,116,128,129],
[135,131,0,126,137,126,119,114,117,122],
[140,136,125,0,150,136,140,129,129,138],
[127,123,114,101,0,128,126,108,116,129],
[126,122,125,115,123,0,128,118,121,134],
[124,121,132,111,125,123,0,113,123,130],
[140,135,137,122,143,133,138,0,129,130],
[132,123,134,122,135,130,128,122,0,137],
[126,122,129,113,122,117,121,121,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,127,117,139,132,134,104,119,115],
[99,0,118,114,118,130,115,122,141,102],
[124,133,0,143,136,150,156,127,137,114],
[134,137,108,0,139,137,148,123,124,115],
[112,133,115,112,0,129,134,115,115,130],
[119,121,101,114,122,0,153,94,145,114],
[117,136,95,103,117,98,0,95,115,107],
[147,129,124,128,136,157,156,0,138,112],
[132,110,114,127,136,106,136,113,0,123],
[136,149,137,136,121,137,144,139,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,134,109,117,143,112,132,108,133],
[140,0,135,129,115,131,122,134,116,125],
[117,116,0,110,113,122,112,131,114,120],
[142,122,141,0,117,137,135,142,133,137],
[134,136,138,134,0,144,124,154,112,134],
[108,120,129,114,107,0,109,111,101,124],
[139,129,139,116,127,142,0,144,126,134],
[119,117,120,109,97,140,107,0,109,126],
[143,135,137,118,139,150,125,142,0,142],
[118,126,131,114,117,127,117,125,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,137,134,131,148,124,132,142,153],
[118,0,127,121,108,130,122,134,135,130],
[114,124,0,123,106,142,134,116,108,138],
[117,130,128,0,115,149,130,132,127,121],
[120,143,145,136,0,156,143,137,149,148],
[103,121,109,102,95,0,126,121,109,110],
[127,129,117,121,108,125,0,127,107,111],
[119,117,135,119,114,130,124,0,141,123],
[109,116,143,124,102,142,144,110,0,129],
[98,121,113,130,103,141,140,128,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,136,118,134,116,131,125,124,117],
[128,0,128,122,119,121,133,115,130,123],
[115,123,0,110,132,103,123,109,120,122],
[133,129,141,0,135,118,130,125,129,119],
[117,132,119,116,0,108,119,113,118,107],
[135,130,148,133,143,0,137,117,127,131],
[120,118,128,121,132,114,0,112,126,114],
[126,136,142,126,138,134,139,0,129,124],
[127,121,131,122,133,124,125,122,0,121],
[134,128,129,132,144,120,137,127,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,104,125,131,126,115,124,142,112],
[128,0,102,129,132,127,126,122,134,118],
[147,149,0,149,153,156,125,143,157,137],
[126,122,102,0,122,114,120,115,130,118],
[120,119,98,129,0,120,126,120,125,115],
[125,124,95,137,131,0,117,114,144,121],
[136,125,126,131,125,134,0,136,141,123],
[127,129,108,136,131,137,115,0,139,120],
[109,117,94,121,126,107,110,112,0,119],
[139,133,114,133,136,130,128,131,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,167,168,110,140,125,92,128,101],
[143,0,132,152,129,163,151,118,110,126],
[84,119,0,101,87,110,100,76,100,109],
[83,99,150,0,75,91,135,108,114,90],
[141,122,164,176,0,133,158,128,147,139],
[111,88,141,160,118,0,145,96,130,102],
[126,100,151,116,93,106,0,79,111,104],
[159,133,175,143,123,155,172,0,152,116],
[123,141,151,137,104,121,140,99,0,106],
[150,125,142,161,112,149,147,135,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,135,119,129,130,128,125,125,133],
[127,0,123,120,134,126,139,139,134,128],
[116,128,0,111,122,128,126,120,125,125],
[132,131,140,0,123,137,128,134,130,136],
[122,117,129,128,0,113,134,122,127,131],
[121,125,123,114,138,0,130,124,135,132],
[123,112,125,123,117,121,0,121,120,122],
[126,112,131,117,129,127,130,0,127,131],
[126,117,126,121,124,116,131,124,0,130],
[118,123,126,115,120,119,129,120,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,114,117,113,129,132,130,127,138],
[147,0,124,139,131,117,139,152,127,144],
[137,127,0,128,138,122,125,125,119,137],
[134,112,123,0,108,120,120,125,117,122],
[138,120,113,143,0,127,113,138,119,137],
[122,134,129,131,124,0,126,128,120,146],
[119,112,126,131,138,125,0,129,129,126],
[121,99,126,126,113,123,122,0,120,129],
[124,124,132,134,132,131,122,131,0,155],
[113,107,114,129,114,105,125,122,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,127,123,118,129,125,120,119,125],
[124,0,123,119,124,132,125,112,115,125],
[124,128,0,119,117,130,121,117,117,135],
[128,132,132,0,124,137,130,122,127,124],
[133,127,134,127,0,127,127,123,120,117],
[122,119,121,114,124,0,126,119,114,117],
[126,126,130,121,124,125,0,126,120,130],
[131,139,134,129,128,132,125,0,130,126],
[132,136,134,124,131,137,131,121,0,121],
[126,126,116,127,134,134,121,125,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,138,155,114,122,134,117,121,127],
[109,0,122,131,116,125,113,121,104,117],
[113,129,0,143,105,121,125,121,111,130],
[96,120,108,0,104,131,120,128,105,142],
[137,135,146,147,0,133,134,144,123,132],
[129,126,130,120,118,0,129,125,126,132],
[117,138,126,131,117,122,0,121,118,133],
[134,130,130,123,107,126,130,0,104,121],
[130,147,140,146,128,125,133,147,0,135],
[124,134,121,109,119,119,118,130,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,133,138,138,123,143,114,126,110],
[117,0,117,127,123,125,137,109,114,111],
[118,134,0,127,129,137,137,139,130,112],
[113,124,124,0,125,124,115,105,118,103],
[113,128,122,126,0,118,113,120,123,92],
[128,126,114,127,133,0,118,119,122,101],
[108,114,114,136,138,133,0,123,119,98],
[137,142,112,146,131,132,128,0,139,130],
[125,137,121,133,128,129,132,112,0,106],
[141,140,139,148,159,150,153,121,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,113,119,119,115,123,138,123,121],
[121,0,134,116,120,127,124,119,131,124],
[138,117,0,135,137,127,127,129,136,124],
[132,135,116,0,140,137,138,134,135,128],
[132,131,114,111,0,114,118,122,130,113],
[136,124,124,114,137,0,118,132,129,119],
[128,127,124,113,133,133,0,126,127,116],
[113,132,122,117,129,119,125,0,124,117],
[128,120,115,116,121,122,124,127,0,123],
[130,127,127,123,138,132,135,134,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,115,134,119,123,119,126,126,128],
[122,0,128,135,118,127,121,134,134,125],
[136,123,0,124,125,135,124,127,138,136],
[117,116,127,0,127,115,121,131,128,134],
[132,133,126,124,0,139,127,140,133,141],
[128,124,116,136,112,0,116,131,128,130],
[132,130,127,130,124,135,0,140,135,128],
[125,117,124,120,111,120,111,0,128,129],
[125,117,113,123,118,123,116,123,0,125],
[123,126,115,117,110,121,123,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,117,123,122,120,124,116,132,121],
[133,0,131,119,125,122,129,119,131,128],
[134,120,0,117,117,126,117,126,126,127],
[128,132,134,0,130,129,124,122,139,134],
[129,126,134,121,0,126,131,133,136,139],
[131,129,125,122,125,0,124,125,134,130],
[127,122,134,127,120,127,0,118,131,123],
[135,132,125,129,118,126,133,0,133,132],
[119,120,125,112,115,117,120,118,0,118],
[130,123,124,117,112,121,128,119,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,105,122,136,111,122,116,126,123],
[140,0,127,110,150,98,113,118,108,150],
[146,124,0,146,173,149,150,175,138,158],
[129,141,105,0,116,96,108,102,95,116],
[115,101,78,135,0,82,122,119,102,89],
[140,153,102,155,169,0,139,132,132,126],
[129,138,101,143,129,112,0,147,113,145],
[135,133,76,149,132,119,104,0,109,122],
[125,143,113,156,149,119,138,142,0,143],
[128,101,93,135,162,125,106,129,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,126,123,125,123,124,125,128,128],
[130,0,129,125,120,121,129,116,121,117],
[125,122,0,116,128,121,115,115,115,128],
[128,126,135,0,117,115,129,129,126,123],
[126,131,123,134,0,122,130,124,125,129],
[128,130,130,136,129,0,121,124,132,131],
[127,122,136,122,121,130,0,128,128,129],
[126,135,136,122,127,127,123,0,123,125],
[123,130,136,125,126,119,123,128,0,117],
[123,134,123,128,122,120,122,126,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,118,128,129,147,107,126,114,113],
[133,0,119,129,124,130,133,138,125,117],
[133,132,0,127,116,127,120,129,130,109],
[123,122,124,0,129,133,123,141,131,128],
[122,127,135,122,0,147,120,119,134,133],
[104,121,124,118,104,0,109,115,117,117],
[144,118,131,128,131,142,0,136,116,119],
[125,113,122,110,132,136,115,0,132,116],
[137,126,121,120,117,134,135,119,0,125],
[138,134,142,123,118,134,132,135,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,119,129,128,123,126,120,111,117],
[132,0,116,136,132,127,142,139,117,125],
[132,135,0,131,126,115,132,126,123,141],
[122,115,120,0,113,126,124,116,107,107],
[123,119,125,138,0,115,114,141,122,115],
[128,124,136,125,136,0,128,131,132,135],
[125,109,119,127,137,123,0,131,115,118],
[131,112,125,135,110,120,120,0,121,127],
[140,134,128,144,129,119,136,130,0,124],
[134,126,110,144,136,116,133,124,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,141,156,149,160,138,149,136,131],
[132,0,129,142,121,145,111,135,108,140],
[110,122,0,118,144,147,122,129,109,131],
[95,109,133,0,141,150,108,137,114,136],
[102,130,107,110,0,135,83,107,80,99],
[91,106,104,101,116,0,95,89,67,131],
[113,140,129,143,168,156,0,138,110,146],
[102,116,122,114,144,162,113,0,98,126],
[115,143,142,137,171,184,141,153,0,160],
[120,111,120,115,152,120,105,125,91,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,157,164,124,155,173,82,174,68,136],
[94,0,49,92,80,35,80,80,80,49],
[87,202,0,101,134,88,129,106,47,129],
[127,159,150,0,188,126,49,136,124,185],
[96,171,117,63,0,142,84,119,136,138],
[78,216,163,125,109,0,64,181,54,113],
[169,171,122,202,167,187,0,202,113,180],
[77,171,145,115,132,70,49,0,68,103],
[183,171,204,127,115,197,138,183,0,192],
[115,202,122,66,113,138,71,148,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,123,122,116,145,117,111,105],
[115,0,117,123,113,122,136,109,105,105],
[125,134,0,126,124,137,142,116,120,115],
[128,128,125,0,131,134,142,120,124,124],
[129,138,127,120,0,134,149,120,121,113],
[135,129,114,117,117,0,128,107,121,103],
[106,115,109,109,102,123,0,102,108,95],
[134,142,135,131,131,144,149,0,133,120],
[140,146,131,127,130,130,143,118,0,130],
[146,146,136,127,138,148,156,131,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,138,130,120,118,116,125,125,125],
[112,0,140,122,137,106,118,132,127,139],
[113,111,0,108,119,105,94,94,105,114],
[121,129,143,0,135,109,128,120,122,118],
[131,114,132,116,0,109,105,125,120,123],
[133,145,146,142,142,0,127,113,129,136],
[135,133,157,123,146,124,0,117,125,119],
[126,119,157,131,126,138,134,0,126,141],
[126,124,146,129,131,122,126,125,0,133],
[126,112,137,133,128,115,132,110,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,127,133,132,125,135,124,131,132],
[117,0,123,132,124,113,124,121,138,116],
[124,128,0,133,135,117,117,115,132,122],
[118,119,118,0,114,117,119,116,126,110],
[119,127,116,137,0,126,133,117,128,111],
[126,138,134,134,125,0,130,132,128,122],
[116,127,134,132,118,121,0,126,122,127],
[127,130,136,135,134,119,125,0,147,137],
[120,113,119,125,123,123,129,104,0,124],
[119,135,129,141,140,129,124,114,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,133,124,124,120,127,138,129,141],
[125,0,115,121,129,105,123,136,128,133],
[118,136,0,127,137,118,130,144,141,135],
[127,130,124,0,124,120,137,136,138,125],
[127,122,114,127,0,124,127,121,117,124],
[131,146,133,131,127,0,118,144,131,129],
[124,128,121,114,124,133,0,146,125,136],
[113,115,107,115,130,107,105,0,109,123],
[122,123,110,113,134,120,126,142,0,121],
[110,118,116,126,127,122,115,128,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,125,139,130,135,130,129,123,129],
[126,0,125,132,132,129,132,131,129,135],
[126,126,0,142,123,119,119,134,129,138],
[112,119,109,0,112,111,120,111,119,121],
[121,119,128,139,0,130,133,122,130,133],
[116,122,132,140,121,0,124,121,121,124],
[121,119,132,131,118,127,0,117,118,125],
[122,120,117,140,129,130,134,0,135,121],
[128,122,122,132,121,130,133,116,0,135],
[122,116,113,130,118,127,126,130,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,136,109,121,133,126,134,122,127],
[137,0,127,121,127,130,113,129,127,115],
[115,124,0,123,121,128,122,121,114,98],
[142,130,128,0,137,107,133,125,126,107],
[130,124,130,114,0,141,130,126,140,130],
[118,121,123,144,110,0,129,119,124,122],
[125,138,129,118,121,122,0,128,114,111],
[117,122,130,126,125,132,123,0,114,109],
[129,124,137,125,111,127,137,137,0,134],
[124,136,153,144,121,129,140,142,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,129,124,127,129,126,123,113,128],
[136,0,134,135,133,124,134,123,120,137],
[122,117,0,129,127,110,131,124,122,116],
[127,116,122,0,132,116,131,114,121,145],
[124,118,124,119,0,112,132,120,121,126],
[122,127,141,135,139,0,136,122,127,130],
[125,117,120,120,119,115,0,130,115,131],
[128,128,127,137,131,129,121,0,130,127],
[138,131,129,130,130,124,136,121,0,129],
[123,114,135,106,125,121,120,124,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,148,133,126,122,175,97,105,86],
[108,0,143,155,129,115,159,118,154,127],
[103,108,0,98,93,105,125,65,118,87],
[118,96,153,0,114,131,180,105,110,81],
[125,122,158,137,0,112,145,73,128,115],
[129,136,146,120,139,0,162,149,146,96],
[76,92,126,71,106,89,0,69,78,76],
[154,133,186,146,178,102,182,0,179,130],
[146,97,133,141,123,105,173,72,0,86],
[165,124,164,170,136,155,175,121,165,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,132,112,160,127,153,163,134,176],
[122,0,135,130,150,119,121,156,134,121],
[119,116,0,93,103,137,147,171,202,157],
[139,121,158,0,147,137,139,147,222,157],
[91,101,148,104,0,75,80,143,155,124],
[124,132,114,114,176,0,147,187,150,160],
[98,130,104,112,171,104,0,226,152,121],
[88,95,80,104,108,64,25,0,108,92],
[117,117,49,29,96,101,99,143,0,186],
[75,130,94,94,127,91,130,159,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,96,143,115,129,121,140,130,127],
[122,0,108,144,130,117,140,132,131,126],
[155,143,0,154,121,139,137,134,139,135],
[108,107,97,0,111,108,127,121,121,128],
[136,121,130,140,0,130,119,127,118,136],
[122,134,112,143,121,0,113,138,125,117],
[130,111,114,124,132,138,0,127,119,126],
[111,119,117,130,124,113,124,0,122,117],
[121,120,112,130,133,126,132,129,0,119],
[124,125,116,123,115,134,125,134,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,116,128,111,111,136,102,119,127],
[134,0,120,158,131,136,147,124,140,140],
[135,131,0,122,147,132,154,134,123,151],
[123,93,129,0,126,126,140,115,111,125],
[140,120,104,125,0,103,135,122,121,140],
[140,115,119,125,148,0,171,136,140,134],
[115,104,97,111,116,80,0,94,113,108],
[149,127,117,136,129,115,157,0,134,136],
[132,111,128,140,130,111,138,117,0,155],
[124,111,100,126,111,117,143,115,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,156,114,148,157,172,151,100,153,153],
[95,0,107,158,108,121,157,93,132,138],
[137,144,0,129,131,121,179,94,140,122],
[103,93,122,0,108,104,144,112,113,102],
[94,143,120,143,0,78,152,71,112,112],
[79,130,130,147,173,0,160,118,107,100],
[100,94,72,107,99,91,0,65,93,98],
[151,158,157,139,180,133,186,0,143,121],
[98,119,111,138,139,144,158,108,0,133],
[98,113,129,149,139,151,153,130,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,132,124,138,127,130,126,129,134],
[117,0,133,121,139,127,128,141,124,137],
[119,118,0,111,138,121,119,125,119,117],
[127,130,140,0,133,119,128,125,126,122],
[113,112,113,118,0,119,109,111,132,121],
[124,124,130,132,132,0,121,123,131,121],
[121,123,132,123,142,130,0,125,121,125],
[125,110,126,126,140,128,126,0,118,120],
[122,127,132,125,119,120,130,133,0,126],
[117,114,134,129,130,130,126,131,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,125,131,119,137,119,125,119,122],
[112,0,128,126,121,130,113,123,121,116],
[126,123,0,134,133,142,122,122,116,127],
[120,125,117,0,121,134,122,120,107,117],
[132,130,118,130,0,132,122,129,128,119],
[114,121,109,117,119,0,117,117,105,114],
[132,138,129,129,129,134,0,129,123,133],
[126,128,129,131,122,134,122,0,124,123],
[132,130,135,144,123,146,128,127,0,135],
[129,135,124,134,132,137,118,128,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,142,137,127,114,126,128,130],
[115,0,119,127,123,111,115,120,116,113],
[125,132,0,126,125,132,124,113,124,123],
[109,124,125,0,105,111,94,106,112,93],
[114,128,126,146,0,118,122,124,131,114],
[124,140,119,140,133,0,128,132,135,129],
[137,136,127,157,129,123,0,123,151,130],
[125,131,138,145,127,119,128,0,126,120],
[123,135,127,139,120,116,100,125,0,113],
[121,138,128,158,137,122,121,131,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,139,113,114,137,141,128,132,117],
[132,0,133,123,116,126,144,132,128,116],
[112,118,0,114,125,117,128,124,120,128],
[138,128,137,0,139,118,127,126,134,117],
[137,135,126,112,0,121,129,127,140,128],
[114,125,134,133,130,0,121,133,141,120],
[110,107,123,124,122,130,0,119,125,133],
[123,119,127,125,124,118,132,0,133,132],
[119,123,131,117,111,110,126,118,0,123],
[134,135,123,134,123,131,118,119,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,155,139,142,137,125,137,138,132,130],
[96,0,112,123,116,93,124,106,111,114],
[112,139,0,139,130,114,127,114,129,118],
[109,128,112,0,121,107,121,103,114,115],
[114,135,121,130,0,132,108,124,121,131],
[126,158,137,144,119,0,127,128,139,128],
[114,127,124,130,143,124,0,119,137,117],
[113,145,137,148,127,123,132,0,135,117],
[119,140,122,137,130,112,114,116,0,121],
[121,137,133,136,120,123,134,134,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,129,133,128,127,129,122,133,133],
[122,0,125,120,123,118,127,119,125,116],
[122,126,0,120,125,116,129,121,126,120],
[118,131,131,0,129,120,126,123,120,120],
[123,128,126,122,0,120,124,123,120,124],
[124,133,135,131,131,0,132,138,129,134],
[122,124,122,125,127,119,0,114,117,123],
[129,132,130,128,128,113,137,0,130,124],
[118,126,125,131,131,122,134,121,0,122],
[118,135,131,131,127,117,128,127,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,82,124,55,111,165,154,80,92,117],
[169,0,147,57,98,186,171,79,49,104],
[127,104,0,97,111,122,223,127,92,112],
[196,194,154,0,161,194,223,117,157,230],
[140,153,140,90,0,206,216,97,82,97],
[86,65,129,57,45,0,110,86,57,64],
[97,80,28,28,35,141,0,50,21,67],
[171,172,124,134,154,165,201,0,147,208],
[159,202,159,94,169,194,230,104,0,187],
[134,147,139,21,154,187,184,43,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,114,123,124,116,118,109,125,132],
[137,0,121,131,110,128,130,119,140,126],
[137,130,0,151,129,121,128,128,133,135],
[128,120,100,0,106,109,110,110,125,108],
[127,141,122,145,0,125,129,121,134,126],
[135,123,130,142,126,0,138,130,130,120],
[133,121,123,141,122,113,0,114,116,120],
[142,132,123,141,130,121,137,0,142,129],
[126,111,118,126,117,121,135,109,0,123],
[119,125,116,143,125,131,131,122,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,57,148,125,174,144,125,142,159],
[107,0,122,110,73,136,59,111,33,107],
[194,129,0,150,183,161,169,143,120,123],
[103,141,101,0,71,169,110,84,130,105],
[126,178,68,180,0,136,110,51,108,74],
[77,115,90,82,115,0,84,115,52,75],
[107,192,82,141,141,167,0,131,118,67],
[126,140,108,167,200,136,120,0,104,131],
[109,218,131,121,143,199,133,147,0,112],
[92,144,128,146,177,176,184,120,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,139,136,128,144,125,126,127,138],
[124,0,129,120,126,141,116,118,125,126],
[112,122,0,118,132,137,115,105,113,116],
[115,131,133,0,131,139,128,128,133,137],
[123,125,119,120,0,137,117,119,119,115],
[107,110,114,112,114,0,107,108,112,117],
[126,135,136,123,134,144,0,113,131,136],
[125,133,146,123,132,143,138,0,125,137],
[124,126,138,118,132,139,120,126,0,131],
[113,125,135,114,136,134,115,114,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,134,131,143,118,139,138,133,126],
[121,0,122,143,143,123,118,122,120,122],
[117,129,0,114,130,130,119,126,120,121],
[120,108,137,0,135,128,119,112,138,128],
[108,108,121,116,0,101,120,110,106,112],
[133,128,121,123,150,0,121,118,110,128],
[112,133,132,132,131,130,0,128,127,120],
[113,129,125,139,141,133,123,0,131,130],
[118,131,131,113,145,141,124,120,0,127],
[125,129,130,123,139,123,131,121,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,132,135,136,128,130,128,108,141],
[114,0,125,120,110,116,116,118,100,123],
[119,126,0,131,132,128,142,133,120,150],
[116,131,120,0,131,134,119,139,126,135],
[115,141,119,120,0,126,135,116,114,119],
[123,135,123,117,125,0,114,121,98,124],
[121,135,109,132,116,137,0,127,117,137],
[123,133,118,112,135,130,124,0,125,127],
[143,151,131,125,137,153,134,126,0,151],
[110,128,101,116,132,127,114,124,100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,123,136,130,103,136,132,147,142],
[102,0,88,109,98,52,109,73,99,83],
[128,163,0,131,139,129,138,109,120,113],
[115,142,120,0,115,84,99,90,105,107],
[121,153,112,136,0,90,137,113,121,110],
[148,199,122,167,161,0,160,143,154,142],
[115,142,113,152,114,91,0,107,139,120],
[119,178,142,161,138,108,144,0,132,145],
[104,152,131,146,130,97,112,119,0,111],
[109,168,138,144,141,109,131,106,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,128,120,142,130,140,115,134,135],
[123,0,118,125,136,122,137,126,159,133],
[123,133,0,149,142,132,156,126,146,146],
[131,126,102,0,134,115,135,116,136,125],
[109,115,109,117,0,110,117,105,132,125],
[121,129,119,136,141,0,134,116,133,134],
[111,114,95,116,134,117,0,112,132,111],
[136,125,125,135,146,135,139,0,148,142],
[117,92,105,115,119,118,119,103,0,112],
[116,118,105,126,126,117,140,109,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,168,168,135,129,116,152,131,161,144],
[83,0,115,126,119,114,123,94,95,85],
[83,136,0,126,133,127,145,108,117,115],
[116,125,125,0,123,140,136,110,131,108],
[122,132,118,128,0,114,152,105,89,85],
[135,137,124,111,137,0,134,97,146,124],
[99,128,106,115,99,117,0,108,103,92],
[120,157,143,141,146,154,143,0,114,92],
[90,156,134,120,162,105,148,137,0,96],
[107,166,136,143,166,127,159,159,155,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,118,133,118,128,122,129,112,124],
[118,0,110,132,119,132,123,123,118,118],
[133,141,0,129,128,138,112,146,120,129],
[118,119,122,0,110,120,121,116,111,107],
[133,132,123,141,0,134,127,143,126,122],
[123,119,113,131,117,0,118,130,103,116],
[129,128,139,130,124,133,0,135,123,122],
[122,128,105,135,108,121,116,0,112,121],
[139,133,131,140,125,148,128,139,0,128],
[127,133,122,144,129,135,129,130,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,123,133,125,150,140,131,153,120],
[132,0,138,144,137,142,119,130,120,106],
[128,113,0,142,140,146,132,128,120,129],
[118,107,109,0,113,136,128,134,123,114],
[126,114,111,138,0,142,118,129,116,117],
[101,109,105,115,109,0,115,103,129,103],
[111,132,119,123,133,136,0,144,112,111],
[120,121,123,117,122,148,107,0,109,120],
[98,131,131,128,135,122,139,142,0,113],
[131,145,122,137,134,148,140,131,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,120,120,113,124,120,118,105,133],
[119,0,111,123,109,123,126,117,107,114],
[131,140,0,128,132,138,125,136,129,130],
[131,128,123,0,113,137,129,131,120,123],
[138,142,119,138,0,148,125,126,125,131],
[127,128,113,114,103,0,123,122,110,124],
[131,125,126,122,126,128,0,118,119,122],
[133,134,115,120,125,129,133,0,115,132],
[146,144,122,131,126,141,132,136,0,137],
[118,137,121,128,120,127,129,119,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,134,137,133,130,123,133,122,134],
[119,0,133,121,128,124,127,120,127,135],
[117,118,0,129,127,118,127,108,118,123],
[114,130,122,0,127,107,121,126,116,132],
[118,123,124,124,0,116,120,114,111,126],
[121,127,133,144,135,0,133,126,126,126],
[128,124,124,130,131,118,0,130,120,125],
[118,131,143,125,137,125,121,0,128,131],
[129,124,133,135,140,125,131,123,0,139],
[117,116,128,119,125,125,126,120,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,139,126,132,128,123,139,142,141],
[121,0,121,121,111,104,111,116,137,123],
[112,130,0,122,120,121,128,139,149,129],
[125,130,129,0,115,121,119,144,141,132],
[119,140,131,136,0,132,134,141,138,144],
[123,147,130,130,119,0,142,146,143,150],
[128,140,123,132,117,109,0,155,126,142],
[112,135,112,107,110,105,96,0,115,115],
[109,114,102,110,113,108,125,136,0,128],
[110,128,122,119,107,101,109,136,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,128,138,127,118,130,141,122,126],
[138,0,139,143,136,126,127,144,123,117],
[123,112,0,122,119,111,105,133,122,110],
[113,108,129,0,120,110,109,132,106,119],
[124,115,132,131,0,117,117,142,115,121],
[133,125,140,141,134,0,128,157,135,140],
[121,124,146,142,134,123,0,135,137,125],
[110,107,118,119,109,94,116,0,124,116],
[129,128,129,145,136,116,114,127,0,121],
[125,134,141,132,130,111,126,135,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,126,124,129,127,120,143,118,127],
[124,0,120,124,124,116,119,137,110,121],
[125,131,0,127,130,126,120,137,126,125],
[127,127,124,0,132,118,132,145,115,126],
[122,127,121,119,0,124,125,139,118,130],
[124,135,125,133,127,0,137,148,135,136],
[131,132,131,119,126,114,0,138,115,122],
[108,114,114,106,112,103,113,0,110,106],
[133,141,125,136,133,116,136,141,0,135],
[124,130,126,125,121,115,129,145,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,140,125,132,121,115,139,113,138],
[130,0,132,120,131,115,122,139,123,152],
[111,119,0,127,118,99,124,130,121,136],
[126,131,124,0,125,116,119,132,121,125],
[119,120,133,126,0,119,125,141,121,147],
[130,136,152,135,132,0,129,145,125,149],
[136,129,127,132,126,122,0,134,138,135],
[112,112,121,119,110,106,117,0,110,124],
[138,128,130,130,130,126,113,141,0,142],
[113,99,115,126,104,102,116,127,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,170,137,97,165,190,153,185,176],
[109,0,126,124,101,102,164,123,155,135],
[81,125,0,96,118,129,169,122,130,119],
[114,127,155,0,121,142,153,130,164,156],
[154,150,133,130,0,125,199,175,209,174],
[86,149,122,109,126,0,189,136,153,149],
[61,87,82,98,52,62,0,97,150,107],
[98,128,129,121,76,115,154,0,136,153],
[66,96,121,87,42,98,101,115,0,149],
[75,116,132,95,77,102,144,98,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,126,119,119,142,117,131,116,116],
[130,0,129,123,123,141,118,124,123,117],
[125,122,0,131,123,126,106,123,105,100],
[132,128,120,0,113,135,106,125,121,108],
[132,128,128,138,0,138,116,134,118,102],
[109,110,125,116,113,0,101,116,98,105],
[134,133,145,145,135,150,0,137,137,119],
[120,127,128,126,117,135,114,0,110,115],
[135,128,146,130,133,153,114,141,0,128],
[135,134,151,143,149,146,132,136,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,202,170,125,156,155,161,142,160],
[25,0,177,153,110,99,155,147,119,161],
[49,74,0,81,76,99,113,98,71,131],
[81,98,170,0,101,84,156,104,111,114],
[126,141,175,150,0,144,134,106,129,117],
[95,152,152,167,107,0,135,150,131,144],
[96,96,138,95,117,116,0,154,111,123],
[90,104,153,147,145,101,97,0,142,105],
[109,132,180,140,122,120,140,109,0,155],
[91,90,120,137,134,107,128,146,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,139,121,160,175,132,159,118,143],
[112,0,105,127,112,103,127,122,116,124],
[112,146,0,133,136,143,152,154,128,136],
[130,124,118,0,121,94,138,123,144,134],
[91,139,115,130,0,135,139,139,110,139],
[76,148,108,157,116,0,110,112,99,105],
[119,124,99,113,112,141,0,135,90,105],
[92,129,97,128,112,139,116,0,123,131],
[133,135,123,107,141,152,161,128,0,157],
[108,127,115,117,112,146,146,120,94,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,140,134,133,136,133,144,130,137],
[126,0,138,129,134,123,137,127,124,134],
[111,113,0,121,118,136,119,111,121,122],
[117,122,130,0,130,129,133,134,126,145],
[118,117,133,121,0,130,128,125,128,143],
[115,128,115,122,121,0,118,125,134,131],
[118,114,132,118,123,133,0,125,123,134],
[107,124,140,117,126,126,126,0,117,135],
[121,127,130,125,123,117,128,134,0,137],
[114,117,129,106,108,120,117,116,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,110,104,106,97,96,108,104,105],
[137,0,131,132,125,129,118,129,107,125],
[141,120,0,127,122,110,98,115,108,125],
[147,119,124,0,118,133,110,122,119,128],
[145,126,129,133,0,116,128,124,141,126],
[154,122,141,118,135,0,109,120,112,124],
[155,133,153,141,123,142,0,144,140,149],
[143,122,136,129,127,131,107,0,125,137],
[147,144,143,132,110,139,111,126,0,138],
[146,126,126,123,125,127,102,114,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,153,145,138,136,132,123,144,152],
[126,0,141,127,117,122,136,133,130,132],
[98,110,0,98,121,108,111,102,103,110],
[106,124,153,0,117,129,125,114,117,126],
[113,134,130,134,0,139,124,113,130,127],
[115,129,143,122,112,0,110,121,114,130],
[119,115,140,126,127,141,0,118,129,127],
[128,118,149,137,138,130,133,0,126,138],
[107,121,148,134,121,137,122,125,0,134],
[99,119,141,125,124,121,124,113,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,111,117,121,130,151,132,140,139],
[103,0,108,114,94,101,124,111,123,129],
[140,143,0,94,103,80,118,97,114,134],
[134,137,157,0,125,119,115,131,140,146],
[130,157,148,126,0,121,167,138,120,149],
[121,150,171,132,130,0,152,150,144,165],
[100,127,133,136,84,99,0,127,113,136],
[119,140,154,120,113,101,124,0,118,128],
[111,128,137,111,131,107,138,133,0,134],
[112,122,117,105,102,86,115,123,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,110,111,114,116,117,116,121,126],
[134,0,108,101,144,129,113,104,125,111],
[141,143,0,119,136,142,140,139,132,123],
[140,150,132,0,140,146,130,117,128,130],
[137,107,115,111,0,126,116,107,124,112],
[135,122,109,105,125,0,126,121,124,127],
[134,138,111,121,135,125,0,110,136,125],
[135,147,112,134,144,130,141,0,136,138],
[130,126,119,123,127,127,115,115,0,123],
[125,140,128,121,139,124,126,113,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,124,144,123,113,119,152,111,97],
[133,0,124,129,126,129,144,141,135,118],
[127,127,0,119,122,93,132,120,114,85],
[107,122,132,0,122,113,129,123,93,106],
[128,125,129,129,0,128,117,132,107,120],
[138,122,158,138,123,0,137,171,113,100],
[132,107,119,122,134,114,0,139,109,109],
[99,110,131,128,119,80,112,0,112,93],
[140,116,137,158,144,138,142,139,0,127],
[154,133,166,145,131,151,142,158,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,126,139,139,137,124,136,139,140],
[108,0,116,143,135,131,121,125,122,118],
[125,135,0,145,134,133,116,124,129,132],
[112,108,106,0,122,121,107,118,114,119],
[112,116,117,129,0,121,119,115,115,115],
[114,120,118,130,130,0,115,123,113,123],
[127,130,135,144,132,136,0,125,129,140],
[115,126,127,133,136,128,126,0,124,121],
[112,129,122,137,136,138,122,127,0,130],
[111,133,119,132,136,128,111,130,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,120,135,132,121,121,122,129,127],
[121,0,125,125,137,111,113,121,135,122],
[131,126,0,131,127,127,126,118,130,126],
[116,126,120,0,127,113,121,127,126,122],
[119,114,124,124,0,119,123,112,131,119],
[130,140,124,138,132,0,129,116,142,128],
[130,138,125,130,128,122,0,120,143,132],
[129,130,133,124,139,135,131,0,140,120],
[122,116,121,125,120,109,108,111,0,117],
[124,129,125,129,132,123,119,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,124,122,105,139,116,114,128,115],
[133,0,123,126,118,128,113,119,113,121],
[127,128,0,130,106,124,118,118,121,117],
[129,125,121,0,110,121,116,126,122,129],
[146,133,145,141,0,139,136,134,135,119],
[112,123,127,130,112,0,115,107,127,104],
[135,138,133,135,115,136,0,130,124,121],
[137,132,133,125,117,144,121,0,119,113],
[123,138,130,129,116,124,127,132,0,108],
[136,130,134,122,132,147,130,138,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,102,92,106,96,125,126,108,113],
[133,0,136,125,133,122,130,124,96,134],
[149,115,0,109,129,117,138,136,119,132],
[159,126,142,0,146,116,149,146,114,124],
[145,118,122,105,0,113,149,124,102,122],
[155,129,134,135,138,0,147,135,119,119],
[126,121,113,102,102,104,0,129,91,119],
[125,127,115,105,127,116,122,0,105,111],
[143,155,132,137,149,132,160,146,0,124],
[138,117,119,127,129,132,132,140,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,126,130,137,118,116,132,134,111],
[128,0,137,126,118,145,143,143,137,117],
[125,114,0,123,125,132,126,138,123,100],
[121,125,128,0,127,136,128,142,137,128],
[114,133,126,124,0,144,129,131,128,127],
[133,106,119,115,107,0,118,134,123,103],
[135,108,125,123,122,133,0,137,126,116],
[119,108,113,109,120,117,114,0,120,107],
[117,114,128,114,123,128,125,131,0,116],
[140,134,151,123,124,148,135,144,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,143,142,125,126,132,127,127,119],
[118,0,133,149,117,121,135,149,138,126],
[108,118,0,132,123,132,134,135,124,96],
[109,102,119,0,130,134,109,118,127,108],
[126,134,128,121,0,128,137,122,130,122],
[125,130,119,117,123,0,139,130,111,102],
[119,116,117,142,114,112,0,120,130,106],
[124,102,116,133,129,121,131,0,123,98],
[124,113,127,124,121,140,121,128,0,124],
[132,125,155,143,129,149,145,153,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,117,112,138,107,81,121,120,128],
[123,0,118,139,147,126,118,137,131,134],
[134,133,0,109,126,134,120,125,130,135],
[139,112,142,0,171,127,132,167,133,146],
[113,104,125,80,0,126,119,125,143,139],
[144,125,117,124,125,0,117,127,124,124],
[170,133,131,119,132,134,0,142,156,157],
[130,114,126,84,126,124,109,0,122,151],
[131,120,121,118,108,127,95,129,0,131],
[123,117,116,105,112,127,94,100,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,128,121,124,122,135,114,121,141],
[126,0,113,98,135,114,139,115,100,124],
[123,138,0,123,137,121,132,132,125,136],
[130,153,128,0,125,126,130,130,117,147],
[127,116,114,126,0,124,134,123,121,137],
[129,137,130,125,127,0,140,122,135,148],
[116,112,119,121,117,111,0,118,110,142],
[137,136,119,121,128,129,133,0,119,118],
[130,151,126,134,130,116,141,132,0,145],
[110,127,115,104,114,103,109,133,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,124,121,124,102,123,102,125,125],
[112,0,131,106,118,99,138,122,120,123],
[127,120,0,144,127,124,136,139,110,151],
[130,145,107,0,104,108,131,118,140,121],
[127,133,124,147,0,124,117,120,119,142],
[149,152,127,143,127,0,131,134,123,135],
[128,113,115,120,134,120,0,113,126,140],
[149,129,112,133,131,117,138,0,128,141],
[126,131,141,111,132,128,125,123,0,125],
[126,128,100,130,109,116,111,110,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,129,119,129,120,103,122,143,135],
[124,0,139,147,125,132,135,117,136,119],
[122,112,0,132,135,96,112,139,144,121],
[132,104,119,0,139,117,94,126,140,102],
[122,126,116,112,0,114,95,111,131,115],
[131,119,155,134,137,0,132,150,157,135],
[148,116,139,157,156,119,0,115,150,127],
[129,134,112,125,140,101,136,0,116,110],
[108,115,107,111,120,94,101,135,0,108],
[116,132,130,149,136,116,124,141,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,116,116,129,112,108,125,123,125],
[129,0,133,120,125,129,129,129,129,136],
[135,118,0,123,128,110,100,122,122,123],
[135,131,128,0,129,125,110,128,128,138],
[122,126,123,122,0,119,112,133,129,118],
[139,122,141,126,132,0,118,140,128,141],
[143,122,151,141,139,133,0,141,135,141],
[126,122,129,123,118,111,110,0,114,123],
[128,122,129,123,122,123,116,137,0,144],
[126,115,128,113,133,110,110,128,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,60,33,102,88,118,52,139,60],
[199,0,185,56,121,232,118,163,224,152],
[191,66,0,0,121,143,118,163,191,8],
[218,195,251,0,148,195,195,163,251,115],
[149,130,130,103,0,111,85,160,141,111],
[163,19,108,56,140,0,137,113,163,27],
[133,133,133,56,166,114,0,125,133,133],
[199,88,88,88,91,138,126,0,232,8],
[112,27,60,0,110,88,118,19,0,27],
[191,99,243,136,140,224,118,243,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,136,121,111,138,118,139,104,128],
[156,0,153,142,146,129,125,137,130,143],
[115,98,0,105,106,106,89,130,110,108],
[130,109,146,0,125,119,107,131,126,122],
[140,105,145,126,0,135,125,144,128,126],
[113,122,145,132,116,0,122,126,133,123],
[133,126,162,144,126,129,0,142,136,122],
[112,114,121,120,107,125,109,0,123,103],
[147,121,141,125,123,118,115,128,0,120],
[123,108,143,129,125,128,129,148,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,116,100,157,111,125,100,185,150],
[124,0,193,179,140,169,159,129,166,112],
[135,58,0,89,130,143,71,101,106,131],
[151,72,162,0,132,191,135,78,113,124],
[94,111,121,119,0,151,115,121,122,119],
[140,82,108,60,100,0,119,65,157,113],
[126,92,180,116,136,132,0,91,166,65],
[151,122,150,173,130,186,160,0,138,138],
[66,85,145,138,129,94,85,113,0,86],
[101,139,120,127,132,138,186,113,165,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,132,130,137,115,119,108,130,118],
[143,0,156,159,150,136,127,131,122,123],
[119,95,0,128,104,120,119,118,106,131],
[121,92,123,0,135,120,119,108,108,126],
[114,101,147,116,0,100,122,95,111,135],
[136,115,131,131,151,0,150,130,116,114],
[132,124,132,132,129,101,0,132,116,143],
[143,120,133,143,156,121,119,0,117,141],
[121,129,145,143,140,135,135,134,0,148],
[133,128,120,125,116,137,108,110,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,130,141,115,134,134,129,129,137],
[117,0,114,147,119,112,126,131,113,144],
[121,137,0,124,102,124,119,112,120,117],
[110,104,127,0,111,125,112,127,113,126],
[136,132,149,140,0,129,125,141,136,139],
[117,139,127,126,122,0,122,129,117,145],
[117,125,132,139,126,129,0,111,122,140],
[122,120,139,124,110,122,140,0,128,133],
[122,138,131,138,115,134,129,123,0,133],
[114,107,134,125,112,106,111,118,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,163,131,158,123,164,184,141,176],
[118,0,120,81,98,151,76,161,82,161],
[88,131,0,140,116,131,85,159,76,123],
[120,170,111,0,144,171,113,143,130,137],
[93,153,135,107,0,115,86,178,98,206],
[128,100,120,80,136,0,115,163,146,129],
[87,175,166,138,165,136,0,219,147,184],
[67,90,92,108,73,88,32,0,78,121],
[110,169,175,121,153,105,104,173,0,146],
[75,90,128,114,45,122,67,130,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,122,121,115,114,120,120,123,128],
[135,0,130,137,126,130,136,124,131,128],
[129,121,0,123,122,115,136,123,132,128],
[130,114,128,0,126,120,129,134,127,131],
[136,125,129,125,0,120,125,135,139,131],
[137,121,136,131,131,0,145,139,137,139],
[131,115,115,122,126,106,0,127,126,137],
[131,127,128,117,116,112,124,0,132,123],
[128,120,119,124,112,114,125,119,0,125],
[123,123,123,120,120,112,114,128,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,127,130,116,112,122,122,111,124],
[126,0,128,108,108,107,112,119,118,121],
[124,123,0,129,120,116,118,128,130,119],
[121,143,122,0,123,117,121,130,133,131],
[135,143,131,128,0,113,119,137,135,128],
[139,144,135,134,138,0,133,123,140,135],
[129,139,133,130,132,118,0,138,128,122],
[129,132,123,121,114,128,113,0,126,122],
[140,133,121,118,116,111,123,125,0,122],
[127,130,132,120,123,116,129,129,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,123,151,104,128,123,136,130,138],
[114,0,98,110,100,67,109,113,94,116],
[128,153,0,108,85,95,111,146,120,176],
[100,141,143,0,80,121,136,145,149,167],
[147,151,166,171,0,117,126,139,100,168],
[123,184,156,130,134,0,114,117,148,158],
[128,142,140,115,125,137,0,138,163,148],
[115,138,105,106,112,134,113,0,111,120],
[121,157,131,102,151,103,88,140,0,161],
[113,135,75,84,83,93,103,131,90,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,122,126,123,128,118,119,117,123],
[115,0,119,117,129,123,125,121,110,110],
[129,132,0,118,124,121,118,120,111,116],
[125,134,133,0,138,127,136,131,127,126],
[128,122,127,113,0,127,112,120,114,117],
[123,128,130,124,124,0,133,125,106,119],
[133,126,133,115,139,118,0,126,123,122],
[132,130,131,120,131,126,125,0,121,115],
[134,141,140,124,137,145,128,130,0,134],
[128,141,135,125,134,132,129,136,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,119,90,151,88,59,98,113,120],
[172,0,95,114,145,106,61,154,114,124],
[132,156,0,69,138,114,77,149,77,95],
[161,137,182,0,162,98,130,148,89,121],
[100,106,113,89,0,87,85,136,51,107],
[163,145,137,153,164,0,103,176,143,131],
[192,190,174,121,166,148,0,197,164,127],
[153,97,102,103,115,75,54,0,70,85],
[138,137,174,162,200,108,87,181,0,174],
[131,127,156,130,144,120,124,166,77,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,125,117,117,120,122,110,119,111],
[142,0,136,135,124,124,133,130,121,145],
[126,115,0,110,117,121,117,118,127,131],
[134,116,141,0,117,122,128,115,128,136],
[134,127,134,134,0,129,124,128,117,138],
[131,127,130,129,122,0,125,129,132,136],
[129,118,134,123,127,126,0,116,116,137],
[141,121,133,136,123,122,135,0,126,134],
[132,130,124,123,134,119,135,125,0,134],
[140,106,120,115,113,115,114,117,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,114,131,123,116,99,154,128,137],
[116,0,106,122,110,127,116,142,134,105],
[137,145,0,129,126,117,108,150,126,119],
[120,129,122,0,124,129,123,159,120,112],
[128,141,125,127,0,118,128,154,132,134],
[135,124,134,122,133,0,140,156,120,140],
[152,135,143,128,123,111,0,174,139,128],
[97,109,101,92,97,95,77,0,111,104],
[123,117,125,131,119,131,112,140,0,129],
[114,146,132,139,117,111,123,147,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,116,117,143,124,130,117,130,129],
[119,0,115,129,120,125,111,127,128,115],
[135,136,0,142,142,124,129,135,135,139],
[134,122,109,0,132,123,119,132,120,116],
[108,131,109,119,0,120,109,132,122,105],
[127,126,127,128,131,0,118,130,130,125],
[121,140,122,132,142,133,0,127,119,131],
[134,124,116,119,119,121,124,0,121,127],
[121,123,116,131,129,121,132,130,0,121],
[122,136,112,135,146,126,120,124,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,126,136,125,135,126,133,136],
[129,0,137,105,125,125,116,105,118,138],
[124,114,0,108,126,114,116,116,119,133],
[125,146,143,0,148,128,149,145,145,143],
[115,126,125,103,0,112,120,122,118,123],
[126,126,137,123,139,0,141,128,125,131],
[116,135,135,102,131,110,0,108,126,128],
[125,146,135,106,129,123,143,0,126,132],
[118,133,132,106,133,126,125,125,0,123],
[115,113,118,108,128,120,123,119,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,81,68,87,79,81,116,115,100],
[149,0,110,155,167,145,121,150,196,179],
[170,141,0,135,159,122,183,164,223,140],
[183,96,116,0,141,114,159,134,169,129],
[164,84,92,110,0,143,111,88,165,73],
[172,106,129,137,108,0,165,125,143,144],
[170,130,68,92,140,86,0,152,179,154],
[135,101,87,117,163,126,99,0,162,129],
[136,55,28,82,86,108,72,89,0,97],
[151,72,111,122,178,107,97,122,154,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,125,145,188,163,182,166,173,175],
[130,0,127,93,180,116,139,126,123,100],
[126,124,0,109,216,141,132,151,104,111],
[106,158,142,0,155,135,153,148,142,137],
[63,71,35,96,0,85,95,89,70,68],
[88,135,110,116,166,0,152,158,138,139],
[69,112,119,98,156,99,0,125,74,78],
[85,125,100,103,162,93,126,0,111,133],
[78,128,147,109,181,113,177,140,0,132],
[76,151,140,114,183,112,173,118,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,105,118,121,106,115,106,114,122],
[150,0,94,127,126,112,129,116,130,131],
[146,157,0,163,125,135,136,147,146,139],
[133,124,88,0,115,122,114,102,128,117],
[130,125,126,136,0,117,134,129,118,123],
[145,139,116,129,134,0,123,111,150,125],
[136,122,115,137,117,128,0,127,125,126],
[145,135,104,149,122,140,124,0,128,129],
[137,121,105,123,133,101,126,123,0,136],
[129,120,112,134,128,126,125,122,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,111,133,135,131,111,126,102,148],
[120,0,119,110,131,133,139,111,106,140],
[140,132,0,128,133,113,146,122,140,152],
[118,141,123,0,121,123,112,113,98,135],
[116,120,118,130,0,112,119,109,98,134],
[120,118,138,128,139,0,107,114,127,136],
[140,112,105,139,132,144,0,125,127,124],
[125,140,129,138,142,137,126,0,123,150],
[149,145,111,153,153,124,124,128,0,131],
[103,111,99,116,117,115,127,101,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,121,132,109,152,125,156,176,174],
[119,0,89,166,117,97,62,108,117,170],
[130,162,0,145,130,106,91,179,139,162],
[119,85,106,0,101,90,77,109,96,126],
[142,134,121,150,0,146,146,183,166,158],
[99,154,145,161,105,0,99,143,140,185],
[126,189,160,174,105,152,0,185,169,166],
[95,143,72,142,68,108,66,0,118,154],
[75,134,112,155,85,111,82,133,0,145],
[77,81,89,125,93,66,85,97,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,130,133,128,115,137,108,137,107],
[146,0,151,142,148,153,141,124,160,134],
[121,100,0,115,119,103,117,71,131,116],
[118,109,136,0,120,124,126,121,134,108],
[123,103,132,131,0,106,109,113,130,105],
[136,98,148,127,145,0,147,112,142,128],
[114,110,134,125,142,104,0,93,119,113],
[143,127,180,130,138,139,158,0,155,119],
[114,91,120,117,121,109,132,96,0,112],
[144,117,135,143,146,123,138,132,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,136,132,143,118,128,114,144,147],
[144,0,125,125,143,149,147,131,149,136],
[115,126,0,120,125,134,135,125,139,127],
[119,126,131,0,123,139,131,112,137,128],
[108,108,126,128,0,118,128,121,132,116],
[133,102,117,112,133,0,153,116,144,138],
[123,104,116,120,123,98,0,105,117,136],
[137,120,126,139,130,135,146,0,153,137],
[107,102,112,114,119,107,134,98,0,134],
[104,115,124,123,135,113,115,114,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,69,146,134,136,137,135,153,186,138],
[182,0,142,138,194,145,113,158,168,144],
[105,109,0,115,114,140,126,102,167,124],
[117,113,136,0,121,136,139,134,133,161],
[115,57,137,130,0,147,111,134,156,135],
[114,106,111,115,104,0,98,104,95,132],
[116,138,125,112,140,153,0,116,134,154],
[98,93,149,117,117,147,135,0,155,111],
[65,83,84,118,95,156,117,96,0,127],
[113,107,127,90,116,119,97,140,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,127,129,118,112,134,117,122,122],
[110,0,123,115,116,108,116,106,125,117],
[124,128,0,119,129,129,136,113,132,129],
[122,136,132,0,117,111,125,113,121,127],
[133,135,122,134,0,122,123,132,132,134],
[139,143,122,140,129,0,129,124,131,147],
[117,135,115,126,128,122,0,115,124,137],
[134,145,138,138,119,127,136,0,135,149],
[129,126,119,130,119,120,127,116,0,124],
[129,134,122,124,117,104,114,102,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,143,117,119,130,125,131,153,121],
[131,0,138,102,116,136,121,123,143,119],
[108,113,0,119,126,149,112,110,134,102],
[134,149,132,0,143,139,111,130,146,136],
[132,135,125,108,0,148,139,121,145,122],
[121,115,102,112,103,0,98,110,110,107],
[126,130,139,140,112,153,0,131,147,143],
[120,128,141,121,130,141,120,0,137,119],
[98,108,117,105,106,141,104,114,0,118],
[130,132,149,115,129,144,108,132,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,118,153,111,168,139,121,154,131],
[110,0,105,145,100,147,126,115,139,106],
[133,146,0,151,133,153,146,124,143,142],
[98,106,100,0,68,126,126,110,117,112],
[140,151,118,183,0,158,155,140,146,154],
[83,104,98,125,93,0,123,89,104,101],
[112,125,105,125,96,128,0,115,110,111],
[130,136,127,141,111,162,136,0,145,120],
[97,112,108,134,105,147,141,106,0,124],
[120,145,109,139,97,150,140,131,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,122,118,121,132,124,126,132,128],
[135,0,120,121,125,129,129,117,125,132],
[129,131,0,134,123,135,128,133,129,142],
[133,130,117,0,129,127,115,120,128,125],
[130,126,128,122,0,132,131,129,127,126],
[119,122,116,124,119,0,119,120,126,123],
[127,122,123,136,120,132,0,120,122,134],
[125,134,118,131,122,131,131,0,128,129],
[119,126,122,123,124,125,129,123,0,120],
[123,119,109,126,125,128,117,122,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,116,113,104,116,114,122,100,114],
[144,0,128,118,121,122,132,134,127,114],
[135,123,0,114,128,112,139,126,112,115],
[138,133,137,0,130,134,131,143,123,131],
[147,130,123,121,0,128,137,136,116,119],
[135,129,139,117,123,0,132,127,131,115],
[137,119,112,120,114,119,0,121,106,111],
[129,117,125,108,115,124,130,0,114,105],
[151,124,139,128,135,120,145,137,0,125],
[137,137,136,120,132,136,140,146,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,129,134,133,126,128,137,138],
[129,0,124,112,120,139,117,124,122,146],
[124,127,0,121,124,138,117,124,128,133],
[122,139,130,0,133,136,122,132,136,133],
[117,131,127,118,0,125,125,133,123,146],
[118,112,113,115,126,0,115,116,115,138],
[125,134,134,129,126,136,0,118,132,147],
[123,127,127,119,118,135,133,0,140,136],
[114,129,123,115,128,136,119,111,0,132],
[113,105,118,118,105,113,104,115,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,112,147,99,120,139,142,113,124],
[113,0,121,124,103,104,134,118,145,127],
[139,130,0,139,130,114,139,155,133,137],
[104,127,112,0,111,104,116,120,130,115],
[152,148,121,140,0,132,153,136,156,150],
[131,147,137,147,119,0,122,148,147,148],
[112,117,112,135,98,129,0,121,125,122],
[109,133,96,131,115,103,130,0,145,139],
[138,106,118,121,95,104,126,106,0,122],
[127,124,114,136,101,103,129,112,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,106,110,107,119,130,125,124,108],
[142,0,145,133,119,131,141,140,123,125],
[145,106,0,135,121,128,134,124,117,130],
[141,118,116,0,115,136,142,135,126,120],
[144,132,130,136,0,122,140,137,137,123],
[132,120,123,115,129,0,140,133,126,132],
[121,110,117,109,111,111,0,118,114,111],
[126,111,127,116,114,118,133,0,120,116],
[127,128,134,125,114,125,137,131,0,114],
[143,126,121,131,128,119,140,135,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,103,123,120,122,121,114,127,120],
[129,0,124,119,128,124,138,127,127,144],
[148,127,0,118,141,134,153,116,145,134],
[128,132,133,0,130,124,134,115,131,133],
[131,123,110,121,0,117,140,120,132,138],
[129,127,117,127,134,0,140,129,130,139],
[130,113,98,117,111,111,0,113,122,113],
[137,124,135,136,131,122,138,0,139,137],
[124,124,106,120,119,121,129,112,0,137],
[131,107,117,118,113,112,138,114,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,120,112,142,133,128,125,123,146],
[142,0,128,128,144,130,134,127,121,144],
[131,123,0,116,142,134,130,129,143,138],
[139,123,135,0,153,136,127,135,130,149],
[109,107,109,98,0,107,121,116,112,133],
[118,121,117,115,144,0,120,132,120,135],
[123,117,121,124,130,131,0,124,125,150],
[126,124,122,116,135,119,127,0,130,133],
[128,130,108,121,139,131,126,121,0,141],
[105,107,113,102,118,116,101,118,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,128,151,130,123,129,109,99,149],
[127,0,117,109,109,109,116,93,127,138],
[123,134,0,132,122,116,95,98,115,133],
[100,142,119,0,115,112,111,86,83,144],
[121,142,129,136,0,151,128,130,139,153],
[128,142,135,139,100,0,120,90,116,145],
[122,135,156,140,123,131,0,104,110,139],
[142,158,153,165,121,161,147,0,139,171],
[152,124,136,168,112,135,141,112,0,153],
[102,113,118,107,98,106,112,80,98,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,139,132,135,133,130,131,130,124],
[121,0,133,121,116,131,122,125,119,122],
[112,118,0,121,116,113,116,115,112,116],
[119,130,130,0,119,121,138,117,118,127],
[116,135,135,132,0,132,128,131,123,123],
[118,120,138,130,119,0,129,120,124,130],
[121,129,135,113,123,122,0,121,133,119],
[120,126,136,134,120,131,130,0,128,129],
[121,132,139,133,128,127,118,123,0,123],
[127,129,135,124,128,121,132,122,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,129,133,130,142,120,136,117,138],
[125,0,123,115,126,132,118,122,114,114],
[122,128,0,119,126,138,116,132,116,124],
[118,136,132,0,144,146,126,130,121,125],
[121,125,125,107,0,145,127,145,120,110],
[109,119,113,105,106,0,112,135,111,95],
[131,133,135,125,124,139,0,129,116,122],
[115,129,119,121,106,116,122,0,112,111],
[134,137,135,130,131,140,135,139,0,116],
[113,137,127,126,141,156,129,140,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,115,135,107,125,127,131,114,113],
[121,0,106,119,115,121,121,110,104,106],
[136,145,0,132,122,134,124,139,121,125],
[116,132,119,0,122,136,121,135,118,117],
[144,136,129,129,0,146,129,142,123,131],
[126,130,117,115,105,0,120,133,111,120],
[124,130,127,130,122,131,0,140,129,110],
[120,141,112,116,109,118,111,0,110,103],
[137,147,130,133,128,140,122,141,0,128],
[138,145,126,134,120,131,141,148,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,117,113,134,128,114,124,123,120],
[128,0,125,124,129,133,116,131,125,119],
[134,126,0,125,135,136,119,135,137,139],
[138,127,126,0,143,132,110,141,142,123],
[117,122,116,108,0,121,112,129,123,118],
[123,118,115,119,130,0,114,124,133,125],
[137,135,132,141,139,137,0,138,139,125],
[127,120,116,110,122,127,113,0,126,111],
[128,126,114,109,128,118,112,125,0,113],
[131,132,112,128,133,126,126,140,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,99,108,46,139,36,50,131,103],
[170,0,139,165,147,156,116,160,153,133],
[152,112,0,103,172,156,55,123,121,117],
[143,86,148,0,112,211,108,125,126,114],
[205,104,79,139,0,192,104,62,157,129],
[112,95,95,40,59,0,72,72,143,131],
[215,135,196,143,147,179,0,146,121,177],
[201,91,128,126,189,179,105,0,153,158],
[120,98,130,125,94,108,130,98,0,146],
[148,118,134,137,122,120,74,93,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,128,121,121,121,132,135,118,126],
[116,0,120,109,129,126,139,124,122,134],
[123,131,0,126,131,138,146,123,138,138],
[130,142,125,0,151,135,141,141,126,137],
[130,122,120,100,0,113,133,122,109,132],
[130,125,113,116,138,0,137,128,130,131],
[119,112,105,110,118,114,0,119,114,114],
[116,127,128,110,129,123,132,0,117,134],
[133,129,113,125,142,121,137,134,0,128],
[125,117,113,114,119,120,137,117,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,108,108,63,69,81,118,20,107],
[180,0,135,129,165,112,126,182,123,141],
[143,116,0,76,75,136,126,182,41,83],
[143,122,175,0,119,152,142,142,106,155],
[188,86,176,132,0,123,99,218,164,128],
[182,139,115,99,128,0,159,152,46,116],
[170,125,125,109,152,92,0,182,133,146],
[133,69,69,109,33,99,69,0,33,38],
[231,128,210,145,87,205,118,218,0,186],
[144,110,168,96,123,135,105,213,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,130,134,127,129,133,125,131,118],
[119,0,121,121,112,122,126,121,122,112],
[121,130,0,128,124,123,127,109,127,121],
[117,130,123,0,124,123,125,123,127,120],
[124,139,127,127,0,133,129,127,120,117],
[122,129,128,128,118,0,124,123,130,123],
[118,125,124,126,122,127,0,123,132,125],
[126,130,142,128,124,128,128,0,141,126],
[120,129,124,124,131,121,119,110,0,116],
[133,139,130,131,134,128,126,125,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,145,124,127,138,157,137,162,133],
[124,0,121,118,100,124,125,126,155,143],
[106,130,0,138,142,125,127,134,179,148],
[127,133,113,0,136,140,140,148,168,135],
[124,151,109,115,0,147,131,135,155,143],
[113,127,126,111,104,0,137,132,171,142],
[94,126,124,111,120,114,0,111,157,121],
[114,125,117,103,116,119,140,0,171,135],
[89,96,72,83,96,80,94,80,0,127],
[118,108,103,116,108,109,130,116,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,129,122,136,111,121,122,140,112],
[142,0,126,128,137,131,129,139,137,117],
[122,125,0,103,124,115,128,122,161,114],
[129,123,148,0,149,154,128,135,141,128],
[115,114,127,102,0,111,112,112,123,108],
[140,120,136,97,140,0,117,135,136,132],
[130,122,123,123,139,134,0,117,140,112],
[129,112,129,116,139,116,134,0,124,99],
[111,114,90,110,128,115,111,127,0,132],
[139,134,137,123,143,119,139,152,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,118,113,115,115,129,112,125,111],
[122,0,117,112,118,117,133,116,115,111],
[133,134,0,120,133,124,141,125,128,123],
[138,139,131,0,126,133,138,129,130,122],
[136,133,118,125,0,117,134,126,122,126],
[136,134,127,118,134,0,136,129,124,124],
[122,118,110,113,117,115,0,121,123,114],
[139,135,126,122,125,122,130,0,125,118],
[126,136,123,121,129,127,128,126,0,113],
[140,140,128,129,125,127,137,133,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,187,146,147,102,147,113,156,142],
[137,0,177,132,150,144,140,97,114,179],
[64,74,0,110,117,69,112,82,102,142],
[105,119,141,0,139,101,130,97,112,141],
[104,101,134,112,0,94,108,101,110,126],
[149,107,182,150,157,0,121,120,123,145],
[104,111,139,121,143,130,0,120,127,171],
[138,154,169,154,150,131,131,0,122,157],
[95,137,149,139,141,128,124,129,0,170],
[109,72,109,110,125,106,80,94,81,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,132,134,136,116,142,119,140,129],
[111,0,123,140,131,118,122,132,138,130],
[119,128,0,125,128,125,115,125,141,123],
[117,111,126,0,130,105,108,119,129,125],
[115,120,123,121,0,109,123,125,134,116],
[135,133,126,146,142,0,125,135,149,139],
[109,129,136,143,128,126,0,128,141,128],
[132,119,126,132,126,116,123,0,135,115],
[111,113,110,122,117,102,110,116,0,108],
[122,121,128,126,135,112,123,136,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,130,139,132,111,129,120,116,128],
[135,0,128,136,129,129,113,104,128,127],
[121,123,0,131,112,116,116,98,124,122],
[112,115,120,0,135,119,109,115,110,123],
[119,122,139,116,0,121,113,105,116,129],
[140,122,135,132,130,0,128,117,119,145],
[122,138,135,142,138,123,0,130,129,133],
[131,147,153,136,146,134,121,0,128,144],
[135,123,127,141,135,132,122,123,0,133],
[123,124,129,128,122,106,118,107,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,146,126,144,121,158,164,131,147],
[124,0,164,139,126,139,140,145,137,138],
[105,87,0,92,101,100,118,120,135,116],
[125,112,159,0,141,140,163,140,136,128],
[107,125,150,110,0,133,134,147,127,133],
[130,112,151,111,118,0,141,143,124,114],
[93,111,133,88,117,110,0,121,127,103],
[87,106,131,111,104,108,130,0,128,92],
[120,114,116,115,124,127,124,123,0,100],
[104,113,135,123,118,137,148,159,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,90,115,150,122,129,144,121,119,128],
[161,0,154,192,122,123,173,166,155,109],
[136,97,0,154,87,103,139,135,132,94],
[101,59,97,0,103,74,97,122,119,94],
[129,129,164,148,0,116,183,144,142,105],
[122,128,148,177,135,0,160,154,145,87],
[107,78,112,154,68,91,0,121,121,84],
[130,85,116,129,107,97,130,0,127,111],
[132,96,119,132,109,106,130,124,0,88],
[123,142,157,157,146,164,167,140,163,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,131,114,121,115,123,139,116,120],
[130,0,135,130,122,122,122,128,133,127],
[120,116,0,125,126,130,133,133,125,122],
[137,121,126,0,129,134,129,130,123,122],
[130,129,125,122,0,122,129,129,118,123],
[136,129,121,117,129,0,121,127,125,121],
[128,129,118,122,122,130,0,133,129,124],
[112,123,118,121,122,124,118,0,113,131],
[135,118,126,128,133,126,122,138,0,130],
[131,124,129,129,128,130,127,120,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,142,126,127,128,145,133,129,130],
[130,0,121,110,129,121,133,132,120,131],
[109,130,0,113,116,115,131,123,125,124],
[125,141,138,0,145,130,143,139,132,129],
[124,122,135,106,0,116,140,129,127,131],
[123,130,136,121,135,0,132,127,131,124],
[106,118,120,108,111,119,0,132,110,126],
[118,119,128,112,122,124,119,0,122,123],
[122,131,126,119,124,120,141,129,0,135],
[121,120,127,122,120,127,125,128,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,118,137,112,160,149,148,132,147],
[144,0,94,178,132,164,170,126,104,150],
[133,157,0,158,109,160,146,132,143,164],
[114,73,93,0,111,138,142,110,117,135],
[139,119,142,140,0,175,154,178,111,166],
[91,87,91,113,76,0,100,116,125,100],
[102,81,105,109,97,151,0,96,100,110],
[103,125,119,141,73,135,155,0,125,137],
[119,147,108,134,140,126,151,126,0,146],
[104,101,87,116,85,151,141,114,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,117,111,107,109,118,117,98,112],
[145,0,128,116,123,145,111,133,126,132],
[134,123,0,129,128,146,130,136,118,136],
[140,135,122,0,136,140,135,156,128,143],
[144,128,123,115,0,122,130,144,111,112],
[142,106,105,111,129,0,110,110,130,131],
[133,140,121,116,121,141,0,137,120,143],
[134,118,115,95,107,141,114,0,115,130],
[153,125,133,123,140,121,131,136,0,144],
[139,119,115,108,139,120,108,121,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,141,132,122,144,132,132,129,148],
[115,0,148,112,111,139,115,122,140,114],
[110,103,0,104,122,117,116,123,128,119],
[119,139,147,0,123,138,134,120,148,137],
[129,140,129,128,0,126,125,114,148,126],
[107,112,134,113,125,0,122,108,125,114],
[119,136,135,117,126,129,0,120,130,121],
[119,129,128,131,137,143,131,0,130,119],
[122,111,123,103,103,126,121,121,0,128],
[103,137,132,114,125,137,130,132,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,124,116,139,130,120,133,138,127],
[117,0,137,118,139,135,120,129,118,123],
[127,114,0,110,134,133,117,109,120,119],
[135,133,141,0,139,131,122,128,128,127],
[112,112,117,112,0,120,107,113,120,111],
[121,116,118,120,131,0,123,111,121,124],
[131,131,134,129,144,128,0,120,129,118],
[118,122,142,123,138,140,131,0,126,128],
[113,133,131,123,131,130,122,125,0,128],
[124,128,132,124,140,127,133,123,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,132,128,153,143,121,136,124,143],
[132,0,162,137,143,134,118,144,138,166],
[119,89,0,127,134,141,106,102,80,123],
[123,114,124,0,129,167,131,145,109,138],
[98,108,117,122,0,135,113,133,107,128],
[108,117,110,84,116,0,121,119,110,122],
[130,133,145,120,138,130,0,142,135,157],
[115,107,149,106,118,132,109,0,126,148],
[127,113,171,142,144,141,116,125,0,133],
[108,85,128,113,123,129,94,103,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,112,114,104,124,131,125,103,129],
[120,0,114,121,103,102,125,119,81,96],
[139,137,0,140,142,133,142,126,126,125],
[137,130,111,0,106,93,108,119,119,100],
[147,148,109,145,0,110,128,131,115,127],
[127,149,118,158,141,0,138,153,124,132],
[120,126,109,143,123,113,0,112,119,132],
[126,132,125,132,120,98,139,0,94,116],
[148,170,125,132,136,127,132,157,0,130],
[122,155,126,151,124,119,119,135,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,143,127,121,122,125,124,120,123],
[112,0,127,125,129,123,114,126,135,126],
[108,124,0,105,115,115,106,118,107,105],
[124,126,146,0,131,130,131,128,130,130],
[130,122,136,120,0,121,124,128,135,115],
[129,128,136,121,130,0,115,134,126,118],
[126,137,145,120,127,136,0,140,129,133],
[127,125,133,123,123,117,111,0,127,118],
[131,116,144,121,116,125,122,124,0,125],
[128,125,146,121,136,133,118,133,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,139,176,100,93,118,85,167,139],
[147,0,113,146,151,176,124,125,156,158],
[112,138,0,160,127,132,147,154,151,184],
[75,105,91,0,99,94,99,83,111,124],
[151,100,124,152,0,102,137,122,154,143],
[158,75,119,157,149,0,162,133,194,165],
[133,127,104,152,114,89,0,75,181,189],
[166,126,97,168,129,118,176,0,183,171],
[84,95,100,140,97,57,70,68,0,98],
[112,93,67,127,108,86,62,80,153,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,135,124,136,126,133,137,136,145],
[100,0,105,118,116,97,113,119,113,137],
[116,146,0,114,121,110,117,118,116,132],
[127,133,137,0,140,118,147,126,125,155],
[115,135,130,111,0,103,115,109,122,119],
[125,154,141,133,148,0,152,154,130,155],
[118,138,134,104,136,99,0,117,118,144],
[114,132,133,125,142,97,134,0,129,143],
[115,138,135,126,129,121,133,122,0,140],
[106,114,119,96,132,96,107,108,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,125,111,121,123,141,113,115,112],
[119,0,117,120,120,114,138,116,108,123],
[126,134,0,121,133,122,123,134,116,118],
[140,131,130,0,124,140,141,140,133,139],
[130,131,118,127,0,122,136,116,116,121],
[128,137,129,111,129,0,144,129,125,126],
[110,113,128,110,115,107,0,107,108,116],
[138,135,117,111,135,122,144,0,120,131],
[136,143,135,118,135,126,143,131,0,139],
[139,128,133,112,130,125,135,120,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,126,124,171,183,126,126,126,126],
[127,0,44,92,69,69,12,82,102,24],
[125,207,0,92,67,57,140,140,195,70],
[127,159,159,0,69,69,127,139,159,139],
[80,182,184,182,0,12,140,172,182,172],
[68,182,194,182,239,0,184,184,182,184],
[125,239,111,124,111,67,0,239,239,123],
[125,169,111,112,79,67,12,0,111,91],
[125,149,56,92,69,69,12,140,0,24],
[125,227,181,112,79,67,128,160,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,128,127,134,127,136,131,128,118],
[124,0,124,122,122,119,123,125,125,124],
[123,127,0,125,111,125,129,138,123,119],
[124,129,126,0,127,127,128,126,135,127],
[117,129,140,124,0,131,130,129,117,122],
[124,132,126,124,120,0,132,134,133,122],
[115,128,122,123,121,119,0,124,126,134],
[120,126,113,125,122,117,127,0,124,123],
[123,126,128,116,134,118,125,127,0,121],
[133,127,132,124,129,129,117,128,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,126,132,114,126,124,136,123,121],
[129,0,129,128,127,125,133,132,136,120],
[125,122,0,121,121,137,133,124,123,119],
[119,123,130,0,109,119,125,130,122,132],
[137,124,130,142,0,124,131,134,135,132],
[125,126,114,132,127,0,128,129,118,130],
[127,118,118,126,120,123,0,121,113,129],
[115,119,127,121,117,122,130,0,125,117],
[128,115,128,129,116,133,138,126,0,121],
[130,131,132,119,119,121,122,134,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,130,132,127,137,134,116,127,144],
[126,0,130,131,127,124,129,121,121,125],
[121,121,0,122,115,123,127,116,123,127],
[119,120,129,0,118,113,123,113,123,125],
[124,124,136,133,0,122,139,130,123,136],
[114,127,128,138,129,0,132,123,125,124],
[117,122,124,128,112,119,0,109,122,120],
[135,130,135,138,121,128,142,0,125,140],
[124,130,128,128,128,126,129,126,0,123],
[107,126,124,126,115,127,131,111,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,138,113,132,114,104,126,127,128],
[149,0,125,122,141,127,109,115,133,114],
[113,126,0,122,129,138,114,127,134,115],
[138,129,129,0,132,115,122,139,125,130],
[119,110,122,119,0,120,102,101,120,111],
[137,124,113,136,131,0,129,151,129,124],
[147,142,137,129,149,122,0,144,137,130],
[125,136,124,112,150,100,107,0,141,136],
[124,118,117,126,131,122,114,110,0,113],
[123,137,136,121,140,127,121,115,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,141,118,120,142,146,123,126,126],
[111,0,113,98,104,101,115,87,99,109],
[110,138,0,137,121,131,139,132,145,134],
[133,153,114,0,116,117,135,113,101,106],
[131,147,130,135,0,125,140,123,109,136],
[109,150,120,134,126,0,140,137,130,133],
[105,136,112,116,111,111,0,99,108,112],
[128,164,119,138,128,114,152,0,120,120],
[125,152,106,150,142,121,143,131,0,146],
[125,142,117,145,115,118,139,131,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,113,112,127,122,125,118,98,118],
[116,0,109,114,140,116,95,113,91,116],
[138,142,0,149,110,128,95,119,129,117],
[139,137,102,0,98,122,99,110,106,105],
[124,111,141,153,0,106,122,117,125,83],
[129,135,123,129,145,0,111,120,106,102],
[126,156,156,152,129,140,0,118,129,113],
[133,138,132,141,134,131,133,0,125,117],
[153,160,122,145,126,145,122,126,0,135],
[133,135,134,146,168,149,138,134,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,113,115,137,127,112,129,108,107],
[118,0,114,106,132,117,126,115,102,120],
[138,137,0,119,136,128,110,123,117,125],
[136,145,132,0,132,135,119,127,125,120],
[114,119,115,119,0,110,111,100,105,101],
[124,134,123,116,141,0,119,113,133,123],
[139,125,141,132,140,132,0,113,105,119],
[122,136,128,124,151,138,138,0,120,126],
[143,149,134,126,146,118,146,131,0,127],
[144,131,126,131,150,128,132,125,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,121,138,130,128,150,137,153,129],
[110,0,125,107,94,128,117,112,111,120],
[130,126,0,129,121,138,142,123,145,139],
[113,144,122,0,100,115,115,108,137,112],
[121,157,130,151,0,134,141,111,129,152],
[123,123,113,136,117,0,138,114,144,132],
[101,134,109,136,110,113,0,125,134,120],
[114,139,128,143,140,137,126,0,154,137],
[98,140,106,114,122,107,117,97,0,122],
[122,131,112,139,99,119,131,114,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,136,126,142,132,123,109,136,143],
[119,0,119,130,133,137,135,129,131,127],
[115,132,0,114,127,125,131,111,119,141],
[125,121,137,0,124,113,127,112,124,123],
[109,118,124,127,0,113,117,112,131,126],
[119,114,126,138,138,0,115,111,129,132],
[128,116,120,124,134,136,0,109,123,138],
[142,122,140,139,139,140,142,0,137,132],
[115,120,132,127,120,122,128,114,0,132],
[108,124,110,128,125,119,113,119,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,132,129,127,119,135,121,133,135],
[122,0,135,121,120,124,129,123,132,129],
[119,116,0,125,122,107,123,120,125,129],
[122,130,126,0,127,123,133,128,128,133],
[124,131,129,124,0,123,135,124,125,133],
[132,127,144,128,128,0,129,119,123,133],
[116,122,128,118,116,122,0,128,121,135],
[130,128,131,123,127,132,123,0,127,122],
[118,119,126,123,126,128,130,124,0,128],
[116,122,122,118,118,118,116,129,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,138,127,125,131,134,135,139,137],
[132,0,143,133,119,124,131,134,121,122],
[113,108,0,113,118,126,123,134,128,118],
[124,118,138,0,127,120,137,133,131,132],
[126,132,133,124,0,126,129,127,134,139],
[120,127,125,131,125,0,139,137,139,131],
[117,120,128,114,122,112,0,131,130,121],
[116,117,117,118,124,114,120,0,124,131],
[112,130,123,120,117,112,121,127,0,126],
[114,129,133,119,112,120,130,120,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,127,110,116,117,131,132,99,123],
[122,0,117,113,130,107,131,126,100,112],
[124,134,0,127,123,117,142,125,115,114],
[141,138,124,0,124,121,139,132,113,130],
[135,121,128,127,0,120,141,128,118,124],
[134,144,134,130,131,0,143,137,122,115],
[120,120,109,112,110,108,0,129,109,117],
[119,125,126,119,123,114,122,0,111,126],
[152,151,136,138,133,129,142,140,0,120],
[128,139,137,121,127,136,134,125,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,47,168,135,126,94,129,155,83],
[151,0,151,177,136,156,164,124,215,141],
[204,100,0,199,166,117,125,125,215,143],
[83,74,52,0,67,126,66,93,155,42],
[116,115,85,184,0,102,106,126,177,42],
[125,95,134,125,149,0,108,134,195,153],
[157,87,126,185,145,143,0,126,182,93],
[122,127,126,158,125,117,125,0,145,101],
[96,36,36,96,74,56,69,106,0,74],
[168,110,108,209,209,98,158,150,177,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,124,111,125,116,151,135,101,128],
[123,0,106,114,145,116,141,121,132,136],
[127,145,0,135,139,118,148,153,142,158],
[140,137,116,0,130,131,144,149,125,138],
[126,106,112,121,0,107,137,137,131,135],
[135,135,133,120,144,0,146,144,134,125],
[100,110,103,107,114,105,0,127,104,121],
[116,130,98,102,114,107,124,0,95,110],
[150,119,109,126,120,117,147,156,0,142],
[123,115,93,113,116,126,130,141,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,89,122,81,110,122,123,163,134,81],
[162,0,162,122,122,122,115,169,162,162],
[129,89,0,89,36,36,82,89,129,82],
[170,129,162,0,150,117,170,129,129,244],
[141,129,215,101,0,101,141,107,100,141],
[129,129,215,134,150,0,129,129,100,203],
[128,136,169,81,110,122,0,128,128,128],
[88,82,162,122,144,122,123,0,47,115],
[117,89,122,122,151,151,123,204,0,151],
[170,89,169,7,110,48,123,136,100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,130,119,111,108,125,119,114,120],
[135,0,144,129,128,111,124,126,122,131],
[121,107,0,111,116,110,113,119,122,121],
[132,122,140,0,120,114,121,118,114,124],
[140,123,135,131,0,129,133,133,125,125],
[143,140,141,137,122,0,118,128,115,127],
[126,127,138,130,118,133,0,126,130,124],
[132,125,132,133,118,123,125,0,116,114],
[137,129,129,137,126,136,121,135,0,129],
[131,120,130,127,126,124,127,137,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,166,121,159,136,128,149,123,126,131],
[85,0,135,96,79,107,98,127,144,89],
[130,116,0,114,102,126,148,150,142,130],
[92,155,137,0,132,91,117,124,145,92],
[115,172,149,119,0,124,108,119,170,93],
[123,144,125,160,127,0,124,140,149,112],
[102,153,103,134,143,127,0,117,118,121],
[128,124,101,127,132,111,134,0,125,90],
[125,107,109,106,81,102,133,126,0,130],
[120,162,121,159,158,139,130,161,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,129,138,111,123,111,126,143,132],
[115,0,111,127,130,110,105,90,135,135],
[122,140,0,104,113,128,119,111,133,150],
[113,124,147,0,133,122,142,131,131,140],
[140,121,138,118,0,138,123,114,126,153],
[128,141,123,129,113,0,113,107,133,128],
[140,146,132,109,128,138,0,138,171,138],
[125,161,140,120,137,144,113,0,138,151],
[108,116,118,120,125,118,80,113,0,131],
[119,116,101,111,98,123,113,100,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,125,141,107,132,109,116,120,129],
[130,0,134,110,115,128,107,127,122,120],
[126,117,0,129,119,131,119,120,113,114],
[110,141,122,0,122,122,131,129,115,123],
[144,136,132,129,0,128,137,139,125,129],
[119,123,120,129,123,0,125,125,116,119],
[142,144,132,120,114,126,0,132,129,128],
[135,124,131,122,112,126,119,0,111,109],
[131,129,138,136,126,135,122,140,0,131],
[122,131,137,128,122,132,123,142,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,114,120,118,99,113,116,129,122],
[133,0,120,127,115,118,124,126,130,124],
[137,131,0,132,128,133,126,123,131,132],
[131,124,119,0,120,113,120,120,136,119],
[133,136,123,131,0,121,118,139,136,129],
[152,133,118,138,130,0,131,144,142,133],
[138,127,125,131,133,120,0,133,136,136],
[135,125,128,131,112,107,118,0,135,131],
[122,121,120,115,115,109,115,116,0,122],
[129,127,119,132,122,118,115,120,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,128,126,137,133,118,128,132,139],
[121,0,111,123,130,136,118,129,121,128],
[123,140,0,129,140,136,134,136,135,137],
[125,128,122,0,130,136,126,132,128,126],
[114,121,111,121,0,124,112,126,122,124],
[118,115,115,115,127,0,121,113,119,122],
[133,133,117,125,139,130,0,134,130,139],
[123,122,115,119,125,138,117,0,122,124],
[119,130,116,123,129,132,121,129,0,130],
[112,123,114,125,127,129,112,127,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,121,126,132,128,145,128,115,125],
[107,0,101,105,110,114,113,123,107,108],
[130,150,0,116,128,126,136,126,129,137],
[125,146,135,0,130,127,136,130,124,123],
[119,141,123,121,0,126,120,122,120,130],
[123,137,125,124,125,0,126,126,106,118],
[106,138,115,115,131,125,0,114,121,111],
[123,128,125,121,129,125,137,0,121,118],
[136,144,122,127,131,145,130,130,0,135],
[126,143,114,128,121,133,140,133,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,134,111,120,120,116,121,100,131],
[122,0,122,116,112,115,122,112,124,111],
[117,129,0,120,116,126,118,116,100,117],
[140,135,131,0,137,123,128,120,121,130],
[131,139,135,114,0,114,120,135,127,132],
[131,136,125,128,137,0,133,136,137,117],
[135,129,133,123,131,118,0,127,123,121],
[130,139,135,131,116,115,124,0,128,125],
[151,127,151,130,124,114,128,123,0,134],
[120,140,134,121,119,134,130,126,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,172,80,172,113,246,238,251,184,122],
[79,0,129,179,158,184,129,193,159,133],
[171,122,0,146,117,217,183,201,121,117],
[79,72,105,0,5,108,74,151,121,129],
[138,93,134,246,0,238,209,222,147,167],
[5,67,34,143,13,0,126,72,64,67],
[13,122,68,177,42,125,0,127,127,96],
[0,58,50,100,29,179,124,0,171,37],
[67,92,130,130,104,187,124,80,0,99],
[129,118,134,122,84,184,155,214,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,127,124,127,108,118,105,128,138],
[111,0,98,113,100,110,105,100,102,128],
[124,153,0,121,119,104,108,131,122,143],
[127,138,130,0,129,120,124,107,136,155],
[124,151,132,122,0,138,113,123,137,149],
[143,141,147,131,113,0,123,119,119,147],
[133,146,143,127,138,128,0,99,126,160],
[146,151,120,144,128,132,152,0,139,149],
[123,149,129,115,114,132,125,112,0,144],
[113,123,108,96,102,104,91,102,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,121,122,107,114,114,112,120,123],
[142,0,139,134,118,128,122,134,130,123],
[130,112,0,125,109,117,116,119,129,128],
[129,117,126,0,121,119,127,120,125,126],
[144,133,142,130,0,128,130,127,130,124],
[137,123,134,132,123,0,134,134,128,126],
[137,129,135,124,121,117,0,127,135,129],
[139,117,132,131,124,117,124,0,130,124],
[131,121,122,126,121,123,116,121,0,123],
[128,128,123,125,127,125,122,127,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,118,131,137,131,115,148,116,119],
[125,0,110,115,102,118,108,112,105,102],
[133,141,0,139,124,136,118,133,123,122],
[120,136,112,0,102,114,105,105,116,119],
[114,149,127,149,0,131,126,133,124,128],
[120,133,115,137,120,0,119,134,123,119],
[136,143,133,146,125,132,0,117,136,131],
[103,139,118,146,118,117,134,0,130,127],
[135,146,128,135,127,128,115,121,0,132],
[132,149,129,132,123,132,120,124,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,107,91,99,104,102,92,101,139],
[179,0,119,134,150,132,122,138,122,161],
[144,132,0,119,137,121,120,126,122,146],
[160,117,132,0,141,135,145,135,130,148],
[152,101,114,110,0,108,130,110,125,141],
[147,119,130,116,143,0,123,119,139,151],
[149,129,131,106,121,128,0,115,133,146],
[159,113,125,116,141,132,136,0,131,154],
[150,129,129,121,126,112,118,120,0,159],
[112,90,105,103,110,100,105,97,92,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,135,128,115,131,117,125,122,115],
[115,0,113,127,109,112,119,107,114,122],
[116,138,0,142,126,136,126,135,122,139],
[123,124,109,0,103,116,112,110,105,129],
[136,142,125,148,0,122,114,110,119,128],
[120,139,115,135,129,0,116,126,123,123],
[134,132,125,139,137,135,0,128,125,128],
[126,144,116,141,141,125,123,0,131,129],
[129,137,129,146,132,128,126,120,0,129],
[136,129,112,122,123,128,123,122,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,172,140,166,142,110,170,125,150,116],
[79,0,122,115,129,97,107,105,126,114],
[111,129,0,160,136,89,132,90,141,114],
[85,136,91,0,123,111,121,146,83,108],
[109,122,115,128,0,119,128,101,80,121],
[141,154,162,140,132,0,162,104,133,140],
[81,144,119,130,123,89,0,104,115,85],
[126,146,161,105,150,147,147,0,140,150],
[101,125,110,168,171,118,136,111,0,122],
[135,137,137,143,130,111,166,101,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,132,122,125,138,127,142,130,127],
[118,0,131,109,128,121,120,131,119,123],
[119,120,0,107,122,126,120,131,130,113],
[129,142,144,0,132,131,130,140,125,121],
[126,123,129,119,0,121,129,117,129,117],
[113,130,125,120,130,0,114,135,129,120],
[124,131,131,121,122,137,0,134,119,122],
[109,120,120,111,134,116,117,0,130,115],
[121,132,121,126,122,122,132,121,0,122],
[124,128,138,130,134,131,129,136,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,116,108,112,115,117,102,128,133],
[124,0,116,109,119,106,126,113,123,133],
[135,135,0,126,137,121,122,119,140,140],
[143,142,125,0,133,117,121,132,145,156],
[139,132,114,118,0,128,121,126,148,128],
[136,145,130,134,123,0,122,122,141,132],
[134,125,129,130,130,129,0,133,157,136],
[149,138,132,119,125,129,118,0,157,142],
[123,128,111,106,103,110,94,94,0,120],
[118,118,111,95,123,119,115,109,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,130,130,123,138,128,128,126,139],
[126,0,124,140,115,127,126,125,124,145],
[121,127,0,118,128,130,114,124,124,131],
[121,111,133,0,118,127,124,123,130,137],
[128,136,123,133,0,146,132,130,128,146],
[113,124,121,124,105,0,122,115,114,132],
[123,125,137,127,119,129,0,137,123,149],
[123,126,127,128,121,136,114,0,128,127],
[125,127,127,121,123,137,128,123,0,141],
[112,106,120,114,105,119,102,124,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,129,141,135,128,134,130,125,139],
[122,0,125,138,128,125,130,129,128,126],
[122,126,0,117,129,121,134,115,126,136],
[110,113,134,0,132,119,129,121,130,121],
[116,123,122,119,0,129,138,118,127,128],
[123,126,130,132,122,0,132,113,138,133],
[117,121,117,122,113,119,0,124,108,136],
[121,122,136,130,133,138,127,0,133,139],
[126,123,125,121,124,113,143,118,0,133],
[112,125,115,130,123,118,115,112,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,119,126,117,116,122,121,122,116],
[140,0,129,130,132,127,124,139,120,133],
[132,122,0,128,113,119,112,127,131,118],
[125,121,123,0,114,111,122,127,125,122],
[134,119,138,137,0,132,125,130,132,120],
[135,124,132,140,119,0,128,138,121,128],
[129,127,139,129,126,123,0,138,117,131],
[130,112,124,124,121,113,113,0,109,124],
[129,131,120,126,119,130,134,142,0,118],
[135,118,133,129,131,123,120,127,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,117,132,122,119,123,126,119,112],
[132,0,132,134,131,132,133,131,124,122],
[134,119,0,112,106,143,127,134,119,110],
[119,117,139,0,119,149,129,145,119,130],
[129,120,145,132,0,157,130,131,134,116],
[132,119,108,102,94,0,111,110,105,107],
[128,118,124,122,121,140,0,127,125,111],
[125,120,117,106,120,141,124,0,116,88],
[132,127,132,132,117,146,126,135,0,119],
[139,129,141,121,135,144,140,163,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,119,144,129,128,141,139,140,143],
[113,0,134,138,118,116,127,138,137,137],
[132,117,0,115,130,131,118,140,137,123],
[107,113,136,0,115,105,121,126,114,118],
[122,133,121,136,0,127,130,135,145,140],
[123,135,120,146,124,0,128,139,138,126],
[110,124,133,130,121,123,0,133,148,151],
[112,113,111,125,116,112,118,0,122,114],
[111,114,114,137,106,113,103,129,0,124],
[108,114,128,133,111,125,100,137,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,128,128,148,141,139,142,136,138],
[136,0,142,113,142,149,139,137,140,141],
[123,109,0,103,117,130,117,121,126,131],
[123,138,148,0,136,155,151,130,138,142],
[103,109,134,115,0,129,126,114,114,134],
[110,102,121,96,122,0,124,99,126,126],
[112,112,134,100,125,127,0,109,120,116],
[109,114,130,121,137,152,142,0,128,136],
[115,111,125,113,137,125,131,123,0,136],
[113,110,120,109,117,125,135,115,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,129,123,116,122,124,135,123,115],
[105,0,124,123,110,113,114,117,123,113],
[122,127,0,125,121,126,115,125,118,118],
[128,128,126,0,124,123,126,125,117,117],
[135,141,130,127,0,130,129,129,133,119],
[129,138,125,128,121,0,119,133,123,119],
[127,137,136,125,122,132,0,134,131,128],
[116,134,126,126,122,118,117,0,121,120],
[128,128,133,134,118,128,120,130,0,119],
[136,138,133,134,132,132,123,131,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,127,130,130,127,127,125,127],
[129,0,127,127,133,135,125,134,126,122],
[124,124,0,125,139,135,118,120,128,124],
[124,124,126,0,141,132,118,131,138,131],
[121,118,112,110,0,112,118,124,126,125],
[121,116,116,119,139,0,118,132,139,134],
[124,126,133,133,133,133,0,131,137,136],
[124,117,131,120,127,119,120,0,136,117],
[126,125,123,113,125,112,114,115,0,119],
[124,129,127,120,126,117,115,134,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,121,115,120,100,112,95,124,104],
[148,0,115,127,129,101,126,120,136,141],
[130,136,0,119,110,96,108,97,128,122],
[136,124,132,0,123,104,145,120,125,119],
[131,122,141,128,0,118,148,136,152,119],
[151,150,155,147,133,0,121,132,153,139],
[139,125,143,106,103,130,0,143,150,139],
[156,131,154,131,115,119,108,0,157,133],
[127,115,123,126,99,98,101,94,0,102],
[147,110,129,132,132,112,112,118,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,151,142,73,98,134,68,104,66],
[170,0,161,91,146,108,168,124,83,73],
[100,90,0,27,100,161,100,70,27,120],
[109,160,224,0,136,177,207,124,167,129],
[178,105,151,115,0,91,122,105,105,80],
[153,143,90,74,160,0,97,117,97,153],
[117,83,151,44,129,154,0,83,20,149],
[183,127,181,127,146,134,168,0,134,86],
[147,168,224,84,146,154,231,117,0,129],
[185,178,131,122,171,98,102,165,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,126,141,113,128,116,132,108,121],
[122,0,125,124,116,124,117,130,115,114],
[125,126,0,130,115,111,109,124,116,121],
[110,127,121,0,116,115,114,128,112,115],
[138,135,136,135,0,122,127,127,124,136],
[123,127,140,136,129,0,116,132,112,116],
[135,134,142,137,124,135,0,135,125,136],
[119,121,127,123,124,119,116,0,120,114],
[143,136,135,139,127,139,126,131,0,120],
[130,137,130,136,115,135,115,137,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,110,136,118,131,117,116,123,131],
[126,0,112,124,125,130,120,126,131,122],
[141,139,0,130,140,125,136,132,135,141],
[115,127,121,0,119,131,129,123,124,123],
[133,126,111,132,0,126,119,130,116,112],
[120,121,126,120,125,0,117,119,123,123],
[134,131,115,122,132,134,0,135,127,126],
[135,125,119,128,121,132,116,0,127,126],
[128,120,116,127,135,128,124,124,0,129],
[120,129,110,128,139,128,125,125,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,114,121,128,133,118,115,136,126],
[123,0,137,125,114,126,116,123,130,127],
[137,114,0,122,133,121,128,124,121,126],
[130,126,129,0,132,131,118,132,131,121],
[123,137,118,119,0,125,106,124,123,125],
[118,125,130,120,126,0,114,126,132,121],
[133,135,123,133,145,137,0,127,137,131],
[136,128,127,119,127,125,124,0,131,104],
[115,121,130,120,128,119,114,120,0,114],
[125,124,125,130,126,130,120,147,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,122,115,118,123,116,125,124,116],
[119,0,116,118,121,131,122,125,127,129],
[129,135,0,123,127,127,120,125,128,124],
[136,133,128,0,122,137,132,131,125,132],
[133,130,124,129,0,138,124,123,122,138],
[128,120,124,114,113,0,117,128,116,116],
[135,129,131,119,127,134,0,133,126,136],
[126,126,126,120,128,123,118,0,120,118],
[127,124,123,126,129,135,125,131,0,132],
[135,122,127,119,113,135,115,133,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,117,131,131,127,124,123,130,134],
[127,0,130,120,131,119,124,118,123,133],
[134,121,0,132,129,121,127,137,139,133],
[120,131,119,0,136,126,121,118,140,136],
[120,120,122,115,0,104,109,114,126,118],
[124,132,130,125,147,0,125,123,128,137],
[127,127,124,130,142,126,0,117,134,128],
[128,133,114,133,137,128,134,0,131,140],
[121,128,112,111,125,123,117,120,0,133],
[117,118,118,115,133,114,123,111,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,96,77,139,98,100,97,96,96,77],
[155,0,82,119,96,107,86,109,101,106],
[174,169,0,161,128,145,125,124,130,109],
[112,132,90,0,111,122,92,85,115,80],
[153,155,123,140,0,118,115,122,144,105],
[151,144,106,129,133,0,110,141,147,124],
[154,165,126,159,136,141,0,128,141,121],
[155,142,127,166,129,110,123,0,140,132],
[155,150,121,136,107,104,110,111,0,105],
[174,145,142,171,146,127,130,119,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,116,141,123,115,124,120,108,120],
[128,0,130,126,129,134,120,120,113,121],
[135,121,0,131,135,137,120,120,127,130],
[110,125,120,0,134,126,107,113,117,125],
[128,122,116,117,0,130,128,115,110,123],
[136,117,114,125,121,0,112,106,103,129],
[127,131,131,144,123,139,0,132,121,135],
[131,131,131,138,136,145,119,0,115,146],
[143,138,124,134,141,148,130,136,0,148],
[131,130,121,126,128,122,116,105,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,86,92,113,100,114,114,130,87],
[150,0,123,118,125,117,129,130,138,123],
[165,128,0,144,141,121,154,132,147,142],
[159,133,107,0,126,120,153,143,147,116],
[138,126,110,125,0,119,130,142,145,116],
[151,134,130,131,132,0,146,115,147,132],
[137,122,97,98,121,105,0,112,137,108],
[137,121,119,108,109,136,139,0,133,97],
[121,113,104,104,106,104,114,118,0,101],
[164,128,109,135,135,119,143,154,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,127,138,141,123,121,134,123,127],
[137,0,136,131,127,123,131,130,134,132],
[124,115,0,133,128,127,132,128,137,132],
[113,120,118,0,125,123,119,128,132,111],
[110,124,123,126,0,113,110,130,127,113],
[128,128,124,128,138,0,127,123,131,125],
[130,120,119,132,141,124,0,129,126,126],
[117,121,123,123,121,128,122,0,131,130],
[128,117,114,119,124,120,125,120,0,115],
[124,119,119,140,138,126,125,121,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,113,123,131,140,127,122,121,130],
[123,0,116,115,133,113,122,128,115,127],
[138,135,0,129,131,135,131,121,131,131],
[128,136,122,0,128,130,130,121,119,136],
[120,118,120,123,0,122,125,121,115,129],
[111,138,116,121,129,0,130,115,120,127],
[124,129,120,121,126,121,0,114,101,118],
[129,123,130,130,130,136,137,0,119,138],
[130,136,120,132,136,131,150,132,0,135],
[121,124,120,115,122,124,133,113,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,131,138,123,137,127,114,135,114],
[127,0,132,135,133,131,132,132,137,108],
[120,119,0,113,114,127,120,120,118,115],
[113,116,138,0,118,135,131,115,128,112],
[128,118,137,133,0,139,128,125,120,122],
[114,120,124,116,112,0,120,114,119,115],
[124,119,131,120,123,131,0,122,135,118],
[137,119,131,136,126,137,129,0,143,128],
[116,114,133,123,131,132,116,108,0,111],
[137,143,136,139,129,136,133,123,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,115,131,126,120,126,115,126,124],
[135,0,131,130,133,123,132,132,142,127],
[136,120,0,138,126,130,129,127,129,127],
[120,121,113,0,123,118,123,122,127,118],
[125,118,125,128,0,116,124,120,130,127],
[131,128,121,133,135,0,125,112,129,126],
[125,119,122,128,127,126,0,123,136,132],
[136,119,124,129,131,139,128,0,130,128],
[125,109,122,124,121,122,115,121,0,119],
[127,124,124,133,124,125,119,123,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,120,133,122,120,118,118,119,123],
[140,0,121,140,128,134,124,128,123,144],
[131,130,0,136,135,136,135,126,123,139],
[118,111,115,0,114,115,129,126,104,124],
[129,123,116,137,0,134,136,128,127,120],
[131,117,115,136,117,0,125,120,122,120],
[133,127,116,122,115,126,0,120,112,116],
[133,123,125,125,123,131,131,0,126,131],
[132,128,128,147,124,129,139,125,0,131],
[128,107,112,127,131,131,135,120,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 251, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_10_251.csv", index=False, header=False)