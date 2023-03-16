
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,118,114,118,122,115,102,116,114,123,116,114],
[132,0,122,121,119,128,108,126,127,123,131,123],
[136,128,0,133,128,137,98,119,130,123,117,128],
[132,129,117,0,120,116,112,106,112,122,117,121],
[128,131,122,130,0,117,105,124,121,114,102,121],
[135,122,113,134,133,0,100,122,104,122,118,120],
[148,142,152,138,145,150,0,130,139,145,125,130],
[134,124,131,144,126,128,120,0,131,133,124,145],
[136,123,120,138,129,146,111,119,0,126,115,137],
[127,127,127,128,136,128,105,117,124,0,115,127],
[134,119,133,133,148,132,125,126,135,135,0,131],
[136,127,122,129,129,130,120,105,113,123,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 1, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,148,131,108,123,100,120,123,115,173,127],
[122,0,118,109,83,113,110,126,116,135,161,154],
[102,132,0,96,81,88,110,89,95,134,171,105],
[119,141,154,0,76,120,134,140,96,106,155,135],
[142,167,169,174,0,125,160,138,147,142,159,186],
[127,137,162,130,125,0,142,149,114,127,168,149],
[150,140,140,116,90,108,0,153,111,140,163,138],
[130,124,161,110,112,101,97,0,88,134,163,127],
[127,134,155,154,103,136,139,162,0,148,153,150],
[135,115,116,144,108,123,110,116,102,0,156,149],
[77,89,79,95,91,82,87,87,97,94,0,130],
[123,96,145,115,64,101,112,123,100,101,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 2, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,131,116,137,141,162,151,134,132,130,147],
[117,0,115,123,110,129,150,151,131,123,113,121],
[119,135,0,106,118,127,137,137,121,137,117,139],
[134,127,144,0,120,134,148,117,148,153,127,153],
[113,140,132,130,0,121,151,131,136,135,115,152],
[109,121,123,116,129,0,132,149,130,132,114,146],
[88,100,113,102,99,118,0,122,107,121,97,120],
[99,99,113,133,119,101,128,0,114,119,101,122],
[116,119,129,102,114,120,143,136,0,131,105,135],
[118,127,113,97,115,118,129,131,119,0,107,118],
[120,137,133,123,135,136,153,149,145,143,0,147],
[103,129,111,97,98,104,130,128,115,132,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 3, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,123,136,125,111,122,114,129,133,119,121],
[137,0,126,118,118,117,129,120,131,124,127,136],
[127,124,0,110,123,117,125,109,128,127,105,121],
[114,132,140,0,122,121,119,112,138,119,125,130],
[125,132,127,128,0,124,127,111,138,142,123,133],
[139,133,133,129,126,0,137,131,137,152,119,139],
[128,121,125,131,123,113,0,119,140,124,124,132],
[136,130,141,138,139,119,131,0,128,147,128,135],
[121,119,122,112,112,113,110,122,0,131,120,116],
[117,126,123,131,108,98,126,103,119,0,110,113],
[131,123,145,125,127,131,126,122,130,140,0,142],
[129,114,129,120,117,111,118,115,134,137,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 4, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,124,92,102,135,142,130,108,119,116,94],
[127,0,125,105,129,126,149,107,138,112,106,121],
[126,125,0,103,100,144,123,129,130,121,116,120],
[158,145,147,0,137,156,163,105,141,131,137,123],
[148,121,150,113,0,149,147,147,127,136,132,139],
[115,124,106,94,101,0,137,117,114,97,108,94],
[108,101,127,87,103,113,0,103,127,104,110,94],
[120,143,121,145,103,133,147,0,112,132,130,130],
[142,112,120,109,123,136,123,138,0,126,136,111],
[131,138,129,119,114,153,146,118,124,0,134,122],
[134,144,134,113,118,142,140,120,114,116,0,113],
[156,129,130,127,111,156,156,120,139,128,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 5, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,167,116,148,124,93,149,110,140,160,130],
[125,0,153,103,152,128,97,136,115,115,129,125],
[83,97,0,76,149,127,95,137,127,140,112,123],
[134,147,174,0,128,147,133,143,121,167,168,152],
[102,98,101,122,0,104,128,140,75,118,87,101],
[126,122,123,103,146,0,114,119,129,148,157,131],
[157,153,155,117,122,136,0,168,121,161,121,133],
[101,114,113,107,110,131,82,0,144,142,91,148],
[140,135,123,129,175,121,129,106,0,138,142,140],
[110,135,110,83,132,102,89,108,112,0,137,141],
[90,121,138,82,163,93,129,159,108,113,0,136],
[120,125,127,98,149,119,117,102,110,109,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 6, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,137,123,105,96,118,111,115,114,112,104],
[148,0,144,134,112,113,117,117,127,114,118,111],
[113,106,0,107,101,109,109,108,116,107,112,109],
[127,116,143,0,100,112,125,117,127,125,121,116],
[145,138,149,150,0,114,121,131,139,133,115,121],
[154,137,141,138,136,0,124,125,142,122,133,131],
[132,133,141,125,129,126,0,124,140,128,122,131],
[139,133,142,133,119,125,126,0,134,139,121,125],
[135,123,134,123,111,108,110,116,0,113,112,118],
[136,136,143,125,117,128,122,111,137,0,143,132],
[138,132,138,129,135,117,128,129,138,107,0,128],
[146,139,141,134,129,119,119,125,132,118,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 7, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,105,173,90,60,112,101,92,115,106,68],
[149,0,90,165,125,101,98,123,113,90,124,111],
[145,160,0,192,127,107,96,117,78,102,106,116],
[77,85,58,0,99,74,88,131,94,91,105,78],
[160,125,123,151,0,132,117,124,123,121,137,129],
[190,149,143,176,118,0,139,148,115,120,143,107],
[138,152,154,162,133,111,0,142,101,117,146,103],
[149,127,133,119,126,102,108,0,129,107,120,129],
[158,137,172,156,127,135,149,121,0,132,125,131],
[135,160,148,159,129,130,133,143,118,0,150,117],
[144,126,144,145,113,107,104,130,125,100,0,118],
[182,139,134,172,121,143,147,121,119,133,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 8, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,91,141,19,149,67,78,150,146,140,166,132],
[159,0,175,33,126,33,57,146,127,93,101,106],
[109,75,0,53,64,57,72,162,52,67,97,92],
[231,217,197,0,147,160,121,160,209,165,172,137],
[101,124,186,103,0,71,113,163,138,104,201,139],
[183,217,193,90,179,0,152,131,193,169,183,153],
[172,193,178,129,137,98,0,192,148,108,136,138],
[100,104,88,90,87,119,58,0,88,54,115,96],
[104,123,198,41,112,57,102,162,0,132,108,130],
[110,157,183,85,146,81,142,196,118,0,141,137],
[84,149,153,78,49,67,114,135,142,109,0,113],
[118,144,158,113,111,97,112,154,120,113,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 9, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,119,138,119,114,120,113,117,139,116,116],
[119,0,113,125,125,128,117,127,113,123,125,103],
[131,137,0,136,136,130,123,124,107,133,122,122],
[112,125,114,0,121,120,108,113,107,98,124,102],
[131,125,114,129,0,127,111,116,107,117,121,126],
[136,122,120,130,123,0,125,115,112,108,110,112],
[130,133,127,142,139,125,0,128,130,131,123,122],
[137,123,126,137,134,135,122,0,114,121,122,135],
[133,137,143,143,143,138,120,136,0,131,149,136],
[111,127,117,152,133,142,119,129,119,0,121,106],
[134,125,128,126,129,140,127,128,101,129,0,127],
[134,147,128,148,124,138,128,115,114,144,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 10, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,125,131,106,156,107,144,119,117,138,138],
[127,0,114,143,133,156,118,155,116,124,141,137],
[125,136,0,149,133,142,144,149,135,148,152,139],
[119,107,101,0,106,135,118,131,111,116,118,116],
[144,117,117,144,0,141,126,137,128,119,147,141],
[94,94,108,115,109,0,109,122,115,108,121,117],
[143,132,106,132,124,141,0,132,116,123,130,129],
[106,95,101,119,113,128,118,0,108,116,113,109],
[131,134,115,139,122,135,134,142,0,133,134,131],
[133,126,102,134,131,142,127,134,117,0,133,121],
[112,109,98,132,103,129,120,137,116,117,0,122],
[112,113,111,134,109,133,121,141,119,129,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 11, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,158,105,141,139,150,116,143,124,147,131,118],
[92,0,128,132,129,146,98,114,108,139,98,132],
[145,122,0,127,162,167,90,135,135,154,129,157],
[109,118,123,0,123,149,100,121,108,108,126,121],
[111,121,88,127,0,151,88,82,127,102,117,84],
[100,104,83,101,99,0,104,92,93,130,92,109],
[134,152,160,150,162,146,0,152,144,157,118,131],
[107,136,115,129,168,158,98,0,121,124,131,118],
[126,142,115,142,123,157,106,129,0,122,121,125],
[103,111,96,142,148,120,93,126,128,0,129,105],
[119,152,121,124,133,158,132,119,129,121,0,120],
[132,118,93,129,166,141,119,132,125,145,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 12, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,90,105,142,119,115,123,106,118,104,104,100],
[160,0,140,126,138,133,147,114,157,121,146,135],
[145,110,0,164,148,128,127,119,104,127,127,118],
[108,124,86,0,110,97,102,101,105,128,119,85],
[131,112,102,140,0,119,129,129,127,127,139,121],
[135,117,122,153,131,0,129,126,119,126,163,126],
[127,103,123,148,121,121,0,118,117,129,157,136],
[144,136,131,149,121,124,132,0,110,151,119,120],
[132,93,146,145,123,131,133,140,0,127,147,142],
[146,129,123,122,123,124,121,99,123,0,149,103],
[146,104,123,131,111,87,93,131,103,101,0,100],
[150,115,132,165,129,124,114,130,108,147,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 13, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,125,128,121,132,129,110,154,123,118,126],
[109,0,117,99,99,112,110,94,117,105,102,100],
[125,133,0,113,107,130,125,111,141,114,135,131],
[122,151,137,0,138,149,136,123,154,139,142,145],
[129,151,143,112,0,149,128,135,144,154,124,125],
[118,138,120,101,101,0,113,106,140,126,116,134],
[121,140,125,114,122,137,0,109,138,134,128,119],
[140,156,139,127,115,144,141,0,156,144,126,130],
[96,133,109,96,106,110,112,94,0,119,117,106],
[127,145,136,111,96,124,116,106,131,0,113,128],
[132,148,115,108,126,134,122,124,133,137,0,132],
[124,150,119,105,125,116,131,120,144,122,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 14, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,133,124,118,131,131,104,133,129,132,123],
[117,0,132,117,125,132,133,126,138,135,132,123],
[117,118,0,124,115,132,135,117,135,125,121,117],
[126,133,126,0,123,135,131,129,132,128,131,131],
[132,125,135,127,0,124,126,131,135,123,125,127],
[119,118,118,115,126,0,125,127,137,115,129,118],
[119,117,115,119,124,125,0,117,123,127,120,113],
[146,124,133,121,119,123,133,0,135,118,123,127],
[117,112,115,118,115,113,127,115,0,119,129,116],
[121,115,125,122,127,135,123,132,131,0,135,132],
[118,118,129,119,125,121,130,127,121,115,0,123],
[127,127,133,119,123,132,137,123,134,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 15, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,121,136,135,136,133,142,140,119,130,145],
[103,0,104,123,118,122,129,119,132,117,119,137],
[129,146,0,130,142,148,135,133,127,126,118,150],
[114,127,120,0,129,127,117,143,118,111,130,127],
[115,132,108,121,0,127,139,129,125,120,124,132],
[114,128,102,123,123,0,123,114,118,121,121,126],
[117,121,115,133,111,127,0,134,136,115,124,140],
[108,131,117,107,121,136,116,0,123,106,113,138],
[110,118,123,132,125,132,114,127,0,108,131,136],
[131,133,124,139,130,129,135,144,142,0,132,141],
[120,131,132,120,126,129,126,137,119,118,0,128],
[105,113,100,123,118,124,110,112,114,109,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 16, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,129,130,146,135,133,120,125,116,128,146],
[128,0,127,121,129,125,135,121,127,124,132,129],
[121,123,0,126,134,116,135,113,119,125,115,138],
[120,129,124,0,122,115,124,114,107,119,122,133],
[104,121,116,128,0,118,126,112,111,119,125,137],
[115,125,134,135,132,0,131,132,123,122,133,136],
[117,115,115,126,124,119,0,101,110,117,123,129],
[130,129,137,136,138,118,149,0,117,120,137,140],
[125,123,131,143,139,127,140,133,0,122,122,125],
[134,126,125,131,131,128,133,130,128,0,133,137],
[122,118,135,128,125,117,127,113,128,117,0,144],
[104,121,112,117,113,114,121,110,125,113,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 17, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,138,106,122,127,150,110,155,138,143,124],
[111,0,145,102,119,110,119,94,141,118,108,129],
[112,105,0,113,120,100,148,106,133,125,125,118],
[144,148,137,0,114,116,145,127,151,131,111,125],
[128,131,130,136,0,127,144,122,135,129,119,119],
[123,140,150,134,123,0,155,131,147,139,134,141],
[100,131,102,105,106,95,0,97,119,114,103,126],
[140,156,144,123,128,119,153,0,144,138,134,130],
[95,109,117,99,115,103,131,106,0,112,110,113],
[112,132,125,119,121,111,136,112,138,0,116,128],
[107,142,125,139,131,116,147,116,140,134,0,131],
[126,121,132,125,131,109,124,120,137,122,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 18, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,96,142,175,103,132,105,169,114,130,149,125],
[154,0,109,175,113,168,107,142,112,154,100,95],
[108,141,0,174,149,146,134,159,116,90,139,163],
[75,75,76,0,31,87,93,31,79,41,100,57],
[147,137,101,219,0,130,179,104,88,117,84,129],
[118,82,104,163,120,0,137,104,131,106,149,102],
[145,143,116,157,71,113,0,115,119,96,113,131],
[81,108,91,219,146,146,135,0,157,114,104,87],
[136,138,134,171,162,119,131,93,0,93,91,87],
[120,96,160,209,133,144,154,136,157,0,149,156],
[101,150,111,150,166,101,137,146,159,101,0,114],
[125,155,87,193,121,148,119,163,163,94,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 19, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,165,189,170,120,136,128,161,148,188,89],
[134,0,186,162,169,110,181,151,190,163,151,141],
[85,64,0,139,132,62,162,111,186,80,123,104],
[61,88,111,0,162,80,171,96,185,88,139,131],
[80,81,118,88,0,52,114,84,145,92,82,57],
[130,140,188,170,198,0,170,122,203,164,172,126],
[114,69,88,79,136,80,0,131,155,89,109,104],
[122,99,139,154,166,128,119,0,156,151,158,112],
[89,60,64,65,105,47,95,94,0,63,98,42],
[102,87,170,162,158,86,161,99,187,0,133,113],
[62,99,127,111,168,78,141,92,152,117,0,62],
[161,109,146,119,193,124,146,138,208,137,188,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 20, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,131,136,140,116,119,122,125,108,132,147],
[123,0,127,139,132,112,125,124,112,120,133,136],
[119,123,0,133,125,118,124,112,132,109,133,125],
[114,111,117,0,113,102,132,119,107,103,116,129],
[110,118,125,137,0,117,112,112,108,103,121,125],
[134,138,132,148,133,0,140,133,130,126,125,150],
[131,125,126,118,138,110,0,127,109,105,126,141],
[128,126,138,131,138,117,123,0,109,113,137,135],
[125,138,118,143,142,120,141,141,0,124,142,157],
[142,130,141,147,147,124,145,137,126,0,144,152],
[118,117,117,134,129,125,124,113,108,106,0,124],
[103,114,125,121,125,100,109,115,93,98,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 21, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,115,115,121,126,139,137,126,118,140,120],
[147,0,127,127,118,137,136,152,135,147,140,129],
[135,123,0,112,130,129,125,137,134,124,147,125],
[135,123,138,0,122,137,157,149,137,141,144,127],
[129,132,120,128,0,144,132,149,157,146,137,145],
[124,113,121,113,106,0,126,129,131,136,123,108],
[111,114,125,93,118,124,0,125,107,128,130,123],
[113,98,113,101,101,121,125,0,121,132,130,113],
[124,115,116,113,93,119,143,129,0,123,129,133],
[132,103,126,109,104,114,122,118,127,0,131,118],
[110,110,103,106,113,127,120,120,121,119,0,110],
[130,121,125,123,105,142,127,137,117,132,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 22, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,114,110,115,118,124,137,137,117,144,132],
[120,0,118,116,119,131,118,139,139,119,143,138],
[136,132,0,119,133,138,136,148,145,134,138,145],
[140,134,131,0,128,143,122,142,138,133,144,143],
[135,131,117,122,0,137,128,137,139,134,140,136],
[132,119,112,107,113,0,120,127,128,111,137,129],
[126,132,114,128,122,130,0,141,134,136,148,138],
[113,111,102,108,113,123,109,0,124,113,117,118],
[113,111,105,112,111,122,116,126,0,119,126,124],
[133,131,116,117,116,139,114,137,131,0,127,137],
[106,107,112,106,110,113,102,133,124,123,0,119],
[118,112,105,107,114,121,112,132,126,113,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 23, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,111,146,118,117,130,145,133,129,126,114],
[127,0,127,124,129,134,123,148,161,121,116,121],
[139,123,0,127,132,115,116,138,143,110,116,107],
[104,126,123,0,129,112,110,146,137,127,88,115],
[132,121,118,121,0,90,118,146,113,132,106,129],
[133,116,135,138,160,0,137,168,166,137,123,133],
[120,127,134,140,132,113,0,143,155,156,102,131],
[105,102,112,104,104,82,107,0,140,125,116,133],
[117,89,107,113,137,84,95,110,0,89,105,93],
[121,129,140,123,118,113,94,125,161,0,109,122],
[124,134,134,162,144,127,148,134,145,141,0,133],
[136,129,143,135,121,117,119,117,157,128,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 24, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,134,129,141,139,148,123,119,121,129,118],
[115,0,126,123,117,110,125,110,116,116,119,129],
[116,124,0,130,137,117,138,129,120,131,121,122],
[121,127,120,0,133,130,138,123,127,119,130,114],
[109,133,113,117,0,130,121,125,120,111,123,126],
[111,140,133,120,120,0,133,123,137,123,124,127],
[102,125,112,112,129,117,0,117,122,111,123,106],
[127,140,121,127,125,127,133,0,127,115,121,124],
[131,134,130,123,130,113,128,123,0,122,128,126],
[129,134,119,131,139,127,139,135,128,0,132,130],
[121,131,129,120,127,126,127,129,122,118,0,115],
[132,121,128,136,124,123,144,126,124,120,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 25, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,113,141,134,130,125,127,142,123,128,113],
[106,0,121,121,120,104,115,107,119,130,121,112],
[137,129,0,143,159,140,121,136,134,147,139,134],
[109,129,107,0,141,113,129,117,124,134,120,113],
[116,130,91,109,0,125,115,110,118,123,103,110],
[120,146,110,137,125,0,128,130,125,149,125,119],
[125,135,129,121,135,122,0,128,124,153,126,121],
[123,143,114,133,140,120,122,0,115,131,111,116],
[108,131,116,126,132,125,126,135,0,138,120,134],
[127,120,103,116,127,101,97,119,112,0,102,102],
[122,129,111,130,147,125,124,139,130,148,0,119],
[137,138,116,137,140,131,129,134,116,148,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 26, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,151,79,72,72,118,68,62,29,39,101],
[143,0,172,110,122,182,211,89,62,33,182,143],
[99,78,0,50,39,72,167,78,29,39,138,132],
[171,140,200,0,111,111,200,140,62,140,171,200],
[178,128,211,139,0,172,178,128,122,128,128,161],
[178,68,178,139,78,0,217,107,29,68,167,128],
[132,39,83,50,72,33,0,78,62,33,39,33],
[182,161,172,110,122,143,172,0,62,33,93,93],
[188,188,221,188,128,221,188,188,0,78,188,221],
[221,217,211,110,122,182,217,217,172,0,149,250],
[211,68,112,79,122,83,211,157,62,101,0,211],
[149,107,118,50,89,122,217,157,29,0,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 27, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,123,139,126,136,121,130,121,154,128,138],
[119,0,137,148,144,119,120,141,123,157,127,145],
[127,113,0,134,138,126,112,120,135,137,125,138],
[111,102,116,0,129,109,106,104,117,122,109,131],
[124,106,112,121,0,110,109,120,113,125,115,127],
[114,131,124,141,140,0,121,130,121,144,130,136],
[129,130,138,144,141,129,0,137,120,138,133,133],
[120,109,130,146,130,120,113,0,105,129,120,121],
[129,127,115,133,137,129,130,145,0,148,123,156],
[96,93,113,128,125,106,112,121,102,0,110,127],
[122,123,125,141,135,120,117,130,127,140,0,135],
[112,105,112,119,123,114,117,129,94,123,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 28, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,113,128,117,121,119,124,113,122,117,113],
[129,0,122,126,125,114,125,126,132,122,124,120],
[137,128,0,138,122,117,127,131,127,134,124,129],
[122,124,112,0,127,124,129,127,133,128,123,118],
[133,125,128,123,0,131,130,134,146,130,125,130],
[129,136,133,126,119,0,120,130,114,127,120,122],
[131,125,123,121,120,130,0,127,132,120,119,118],
[126,124,119,123,116,120,123,0,126,112,102,117],
[137,118,123,117,104,136,118,124,0,118,108,117],
[128,128,116,122,120,123,130,138,132,0,122,126],
[133,126,126,127,125,130,131,148,142,128,0,126],
[137,130,121,132,120,128,132,133,133,124,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 29, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,129,160,148,125,128,116,132,127,134,146],
[109,0,103,116,115,95,121,89,99,100,119,110],
[121,147,0,147,142,119,129,131,118,125,126,137],
[90,134,103,0,136,103,116,110,120,126,130,128],
[102,135,108,114,0,101,117,112,115,117,120,114],
[125,155,131,147,149,0,134,114,127,139,135,133],
[122,129,121,134,133,116,0,125,126,136,141,140],
[134,161,119,140,138,136,125,0,130,140,154,132],
[118,151,132,130,135,123,124,120,0,134,133,131],
[123,150,125,124,133,111,114,110,116,0,123,123],
[116,131,124,120,130,115,109,96,117,127,0,124],
[104,140,113,122,136,117,110,118,119,127,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 30, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,114,105,105,115,120,121,114,119,101,123],
[138,0,125,112,113,126,137,123,117,123,116,132],
[136,125,0,126,124,131,141,141,124,140,116,139],
[145,138,124,0,133,147,143,138,124,137,130,142],
[145,137,126,117,0,137,134,134,135,139,123,133],
[135,124,119,103,113,0,130,123,116,110,107,117],
[130,113,109,107,116,120,0,134,129,134,130,124],
[129,127,109,112,116,127,116,0,123,126,104,129],
[136,133,126,126,115,134,121,127,0,123,119,126],
[131,127,110,113,111,140,116,124,127,0,119,124],
[149,134,134,120,127,143,120,146,131,131,0,137],
[127,118,111,108,117,133,126,121,124,126,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 31, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,103,121,99,124,103,122,109,105,124,109],
[137,0,123,113,97,145,112,138,122,97,149,90],
[147,127,0,121,131,129,122,133,134,115,146,109],
[129,137,129,0,107,148,115,115,123,96,118,111],
[151,153,119,143,0,153,129,138,140,131,144,136],
[126,105,121,102,97,0,82,117,83,99,130,119],
[147,138,128,135,121,168,0,173,133,113,147,116],
[128,112,117,135,112,133,77,0,122,114,109,108],
[141,128,116,127,110,167,117,128,0,104,122,118],
[145,153,135,154,119,151,137,136,146,0,167,126],
[126,101,104,132,106,120,103,141,128,83,0,93],
[141,160,141,139,114,131,134,142,132,124,157,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 32, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,137,130,135,122,135,118,127,123,114,134],
[130,0,130,125,128,122,119,135,113,129,117,133],
[113,120,0,127,136,125,131,127,123,123,110,125],
[120,125,123,0,131,121,133,136,120,117,118,138],
[115,122,114,119,0,124,126,125,116,117,112,128],
[128,128,125,129,126,0,121,128,128,113,126,123],
[115,131,119,117,124,129,0,108,129,125,121,129],
[132,115,123,114,125,122,142,0,128,121,111,127],
[123,137,127,130,134,122,121,122,0,135,113,136],
[127,121,127,133,133,137,125,129,115,0,132,133],
[136,133,140,132,138,124,129,139,137,118,0,145],
[116,117,125,112,122,127,121,123,114,117,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 33, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,107,153,139,134,136,131,134,142,101,120],
[142,0,117,165,121,172,125,165,140,164,121,138],
[143,133,0,158,159,162,114,168,138,149,128,152],
[97,85,92,0,105,140,119,135,121,130,110,114],
[111,129,91,145,0,126,112,133,139,120,109,139],
[116,78,88,110,124,0,103,137,112,141,97,108],
[114,125,136,131,138,147,0,147,138,121,126,137],
[119,85,82,115,117,113,103,0,120,112,108,100],
[116,110,112,129,111,138,112,130,0,127,103,121],
[108,86,101,120,130,109,129,138,123,0,115,120],
[149,129,122,140,141,153,124,142,147,135,0,137],
[130,112,98,136,111,142,113,150,129,130,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 34, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,171,144,116,171,128,174,73,217,174,43],
[33,0,98,98,116,43,0,46,0,128,0,43],
[79,152,0,101,73,46,119,46,0,174,46,0],
[106,152,149,0,149,149,73,152,106,207,152,149],
[134,134,177,101,0,144,101,134,88,101,134,122],
[79,207,204,101,106,0,119,79,33,207,152,33],
[122,250,131,177,149,131,0,177,76,250,134,76],
[76,204,204,98,116,171,73,0,116,171,128,43],
[177,250,250,144,162,217,174,134,0,217,174,122],
[33,122,76,43,149,43,0,79,33,0,33,76],
[76,250,204,98,116,98,116,122,76,217,0,76],
[207,207,250,101,128,217,174,207,128,174,174,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 35, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,110,113,118,109,123,108,106,123,115,107],
[141,0,125,125,130,111,141,121,128,137,124,135],
[140,125,0,117,129,95,123,116,125,124,125,129],
[137,125,133,0,137,126,126,109,118,130,122,119],
[132,120,121,113,0,102,107,109,101,115,100,115],
[141,139,155,124,148,0,150,118,133,143,136,152],
[127,109,127,124,143,100,0,130,116,130,113,139],
[142,129,134,141,141,132,120,0,106,123,118,131],
[144,122,125,132,149,117,134,144,0,145,130,128],
[127,113,126,120,135,107,120,127,105,0,119,108],
[135,126,125,128,150,114,137,132,120,131,0,136],
[143,115,121,131,135,98,111,119,122,142,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 36, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,130,128,117,113,123,122,127,117,124,115],
[125,0,127,116,113,126,116,115,137,116,133,121],
[120,123,0,122,110,122,106,124,131,105,131,115],
[122,134,128,0,112,118,121,118,130,115,127,123],
[133,137,140,138,0,138,127,109,129,123,135,130],
[137,124,128,132,112,0,111,124,118,109,140,125],
[127,134,144,129,123,139,0,120,133,125,136,128],
[128,135,126,132,141,126,130,0,135,126,136,125],
[123,113,119,120,121,132,117,115,0,120,129,111],
[133,134,145,135,127,141,125,124,130,0,135,115],
[126,117,119,123,115,110,114,114,121,115,0,109],
[135,129,135,127,120,125,122,125,139,135,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 37, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,139,146,131,160,161,140,141,151,114,134],
[103,0,112,107,101,128,123,82,117,96,73,102],
[111,138,0,111,107,100,97,103,124,98,122,97],
[104,143,139,0,143,147,131,110,138,130,138,88],
[119,149,143,107,0,133,129,84,133,86,110,106],
[90,122,150,103,117,0,109,113,137,103,121,92],
[89,127,153,119,121,141,0,128,152,104,109,101],
[110,168,147,140,166,137,122,0,136,111,93,114],
[109,133,126,112,117,113,98,114,0,97,89,94],
[99,154,152,120,164,147,146,139,153,0,134,99],
[136,177,128,112,140,129,141,157,161,116,0,126],
[116,148,153,162,144,158,149,136,156,151,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 38, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,123,116,136,112,118,116,127,123,123,136],
[139,0,121,138,142,127,137,135,131,138,135,142],
[127,129,0,135,126,131,141,123,113,129,130,132],
[134,112,115,0,133,113,121,123,118,122,119,127],
[114,108,124,117,0,112,123,120,121,121,106,118],
[138,123,119,137,138,0,128,130,130,133,130,131],
[132,113,109,129,127,122,0,121,125,118,124,126],
[134,115,127,127,130,120,129,0,120,125,121,130],
[123,119,137,132,129,120,125,130,0,115,126,132],
[127,112,121,128,129,117,132,125,135,0,123,135],
[127,115,120,131,144,120,126,129,124,127,0,123],
[114,108,118,123,132,119,124,120,118,115,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 39, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,139,120,129,130,139,131,124,137,123,129],
[123,0,124,114,129,114,115,110,141,132,109,125],
[111,126,0,111,125,120,112,117,117,128,118,116],
[130,136,139,0,133,133,140,126,125,137,131,131],
[121,121,125,117,0,116,137,124,122,127,120,133],
[120,136,130,117,134,0,145,118,123,128,124,122],
[111,135,138,110,113,105,0,114,116,124,120,131],
[119,140,133,124,126,132,136,0,114,140,132,128],
[126,109,133,125,128,127,134,136,0,144,118,119],
[113,118,122,113,123,122,126,110,106,0,106,112],
[127,141,132,119,130,126,130,118,132,144,0,127],
[121,125,134,119,117,128,119,122,131,138,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 40, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,143,120,120,131,121,131,118,96,96,133],
[122,0,145,111,115,120,118,119,104,110,119,136],
[107,105,0,107,120,98,97,107,89,100,86,110],
[130,139,143,0,132,133,133,143,121,123,118,145],
[130,135,130,118,0,126,113,131,117,141,105,130],
[119,130,152,117,124,0,123,129,120,130,120,123],
[129,132,153,117,137,127,0,129,114,135,126,137],
[119,131,143,107,119,121,121,0,114,112,100,116],
[132,146,161,129,133,130,136,136,0,132,122,134],
[154,140,150,127,109,120,115,138,118,0,114,119],
[154,131,164,132,145,130,124,150,128,136,0,146],
[117,114,140,105,120,127,113,134,116,131,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 41, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,97,142,117,122,113,122,116,123,120,111],
[130,0,113,140,133,121,121,132,125,118,120,124],
[153,137,0,137,124,135,122,122,127,123,125,94],
[108,110,113,0,111,126,109,108,110,113,109,94],
[133,117,126,139,0,124,133,135,123,122,125,125],
[128,129,115,124,126,0,135,113,121,128,121,108],
[137,129,128,141,117,115,0,118,118,122,117,119],
[128,118,128,142,115,137,132,0,125,124,134,111],
[134,125,123,140,127,129,132,125,0,126,117,122],
[127,132,127,137,128,122,128,126,124,0,129,106],
[130,130,125,141,125,129,133,116,133,121,0,116],
[139,126,156,156,125,142,131,139,128,144,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 42, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,117,122,121,124,113,136,136,123,125,118],
[122,0,122,135,129,122,119,116,131,119,128,134],
[133,128,0,143,141,121,121,129,138,114,136,126],
[128,115,107,0,117,103,105,120,129,116,127,130],
[129,121,109,133,0,129,133,122,121,124,131,117],
[126,128,129,147,121,0,116,126,142,125,130,130],
[137,131,129,145,117,134,0,137,133,126,133,135],
[114,134,121,130,128,124,113,0,121,115,124,123],
[114,119,112,121,129,108,117,129,0,115,126,118],
[127,131,136,134,126,125,124,135,135,0,135,139],
[125,122,114,123,119,120,117,126,124,115,0,119],
[132,116,124,120,133,120,115,127,132,111,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 43, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,153,113,135,121,154,118,142,143,128,126,123],
[97,0,91,131,94,128,98,137,121,105,116,89],
[137,159,0,112,138,151,122,143,144,131,142,106],
[115,119,138,0,114,132,85,90,147,127,126,102],
[129,156,112,136,0,145,114,156,156,147,163,143],
[96,122,99,118,105,0,88,120,104,115,106,102],
[132,152,128,165,136,162,0,175,157,135,162,110],
[108,113,107,160,94,130,75,0,133,114,141,88],
[107,129,106,103,94,146,93,117,0,121,105,81],
[122,145,119,123,103,135,115,136,129,0,142,101],
[124,134,108,124,87,144,88,109,145,108,0,96],
[127,161,144,148,107,148,140,162,169,149,154,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 44, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,111,128,117,111,144,115,121,121,129,122],
[128,0,128,139,131,122,136,137,141,130,135,132],
[139,122,0,127,116,129,149,136,136,135,142,132],
[122,111,123,0,110,115,139,126,129,134,134,126],
[133,119,134,140,0,126,140,122,126,118,124,132],
[139,128,121,135,124,0,142,142,141,116,137,159],
[106,114,101,111,110,108,0,109,116,116,112,112],
[135,113,114,124,128,108,141,0,132,119,130,126],
[129,109,114,121,124,109,134,118,0,108,123,127],
[129,120,115,116,132,134,134,131,142,0,122,121],
[121,115,108,116,126,113,138,120,127,128,0,121],
[128,118,118,124,118,91,138,124,123,129,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 45, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,125,121,124,128,132,120,134,124,126,111],
[137,0,128,137,149,139,135,121,134,135,132,127],
[125,122,0,114,129,126,135,114,123,119,118,112],
[129,113,136,0,137,130,135,121,123,127,134,127],
[126,101,121,113,0,118,125,111,113,119,118,100],
[122,111,124,120,132,0,128,108,129,133,124,120],
[118,115,115,115,125,122,0,124,127,111,116,105],
[130,129,136,129,139,142,126,0,131,116,128,130],
[116,116,127,127,137,121,123,119,0,117,117,121],
[126,115,131,123,131,117,139,134,133,0,122,127],
[124,118,132,116,132,126,134,122,133,128,0,124],
[139,123,138,123,150,130,145,120,129,123,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 46, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,135,154,146,138,140,134,151,124,153,138],
[102,0,138,129,142,127,124,148,140,124,125,131],
[115,112,0,122,124,92,117,136,127,110,114,115],
[96,121,128,0,126,120,112,131,117,108,120,111],
[104,108,126,124,0,117,116,130,126,115,139,118],
[112,123,158,130,133,0,134,146,143,125,127,131],
[110,126,133,138,134,116,0,119,118,117,135,123],
[116,102,114,119,120,104,131,0,136,110,130,136],
[99,110,123,133,124,107,132,114,0,117,129,112],
[126,126,140,142,135,125,133,140,133,0,124,117],
[97,125,136,130,111,123,115,120,121,126,0,129],
[112,119,135,139,132,119,127,114,138,133,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 47, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,128,126,126,138,134,120,126,121,133,132],
[116,0,125,123,109,123,126,124,118,129,127,120],
[122,125,0,128,116,129,124,122,115,114,135,122],
[124,127,122,0,120,133,125,117,121,122,126,115],
[124,141,134,130,0,119,124,120,108,114,129,117],
[112,127,121,117,131,0,115,110,112,122,117,127],
[116,124,126,125,126,135,0,125,119,119,125,126],
[130,126,128,133,130,140,125,0,131,127,133,131],
[124,132,135,129,142,138,131,119,0,125,125,126],
[129,121,136,128,136,128,131,123,125,0,135,127],
[117,123,115,124,121,133,125,117,125,115,0,120],
[118,130,128,135,133,123,124,119,124,123,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 48, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,119,106,132,121,119,113,128,122,129,116],
[127,0,122,128,140,132,134,127,125,139,136,121],
[131,128,0,121,133,129,123,129,129,133,130,125],
[144,122,129,0,138,126,128,133,128,133,131,118],
[118,110,117,112,0,117,123,118,116,116,122,103],
[129,118,121,124,133,0,124,113,124,122,128,115],
[131,116,127,122,127,126,0,123,125,123,129,114],
[137,123,121,117,132,137,127,0,123,134,131,123],
[122,125,121,122,134,126,125,127,0,128,131,127],
[128,111,117,117,134,128,127,116,122,0,130,111],
[121,114,120,119,128,122,121,119,119,120,0,121],
[134,129,125,132,147,135,136,127,123,139,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 49, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,114,133,138,125,116,114,160,127,125,136],
[105,0,124,149,137,140,122,135,177,144,108,143],
[136,126,0,137,114,136,134,107,156,155,130,148],
[117,101,113,0,107,112,95,126,125,128,94,119],
[112,113,136,143,0,124,129,130,162,151,135,142],
[125,110,114,138,126,0,109,136,158,141,126,155],
[134,128,116,155,121,141,0,110,180,160,99,130],
[136,115,143,124,120,114,140,0,145,135,118,121],
[90,73,94,125,88,92,70,105,0,109,109,150],
[123,106,95,122,99,109,90,115,141,0,103,126],
[125,142,120,156,115,124,151,132,141,147,0,136],
[114,107,102,131,108,95,120,129,100,124,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 50, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,151,125,109,108,129,135,125,147,127,134],
[120,0,144,102,103,109,116,116,120,138,141,113],
[99,106,0,103,97,92,126,101,92,121,106,109],
[125,148,147,0,122,120,142,121,117,142,125,134],
[141,147,153,128,0,126,132,139,113,151,140,137],
[142,141,158,130,124,0,153,148,128,150,114,137],
[121,134,124,108,118,97,0,113,99,119,111,114],
[115,134,149,129,111,102,137,0,122,139,146,127],
[125,130,158,133,137,122,151,128,0,162,134,125],
[103,112,129,108,99,100,131,111,88,0,130,109],
[123,109,144,125,110,136,139,104,116,120,0,105],
[116,137,141,116,113,113,136,123,125,141,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 51, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,115,134,127,128,129,138,123,134,133,125],
[131,0,123,134,119,123,124,128,120,127,120,108],
[135,127,0,146,138,138,124,137,126,123,137,124],
[116,116,104,0,128,114,119,125,113,110,114,124],
[123,131,112,122,0,118,115,134,122,110,137,121],
[122,127,112,136,132,0,115,122,123,132,119,119],
[121,126,126,131,135,135,0,132,124,132,149,130],
[112,122,113,125,116,128,118,0,110,111,123,114],
[127,130,124,137,128,127,126,140,0,128,138,117],
[116,123,127,140,140,118,118,139,122,0,125,120],
[117,130,113,136,113,131,101,127,112,125,0,111],
[125,142,126,126,129,131,120,136,133,130,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 52, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,137,139,138,146,142,115,127,130,142,141],
[116,0,116,128,127,146,128,119,117,121,136,138],
[113,134,0,132,118,125,128,119,110,130,136,140],
[111,122,118,0,121,126,125,116,112,122,126,134],
[112,123,132,129,0,133,124,122,114,129,124,136],
[104,104,125,124,117,0,123,118,124,123,122,131],
[108,122,122,125,126,127,0,111,130,118,123,120],
[135,131,131,134,128,132,139,0,120,127,131,141],
[123,133,140,138,136,126,120,130,0,127,135,147],
[120,129,120,128,121,127,132,123,123,0,122,142],
[108,114,114,124,126,128,127,119,115,128,0,138],
[109,112,110,116,114,119,130,109,103,108,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 53, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,115,121,119,108,122,138,122,139,118,137],
[143,0,127,132,145,135,138,128,119,165,132,131],
[135,123,0,125,140,133,131,132,142,168,123,124],
[129,118,125,0,130,106,135,144,121,138,129,130],
[131,105,110,120,0,126,122,121,132,141,121,129],
[142,115,117,144,124,0,135,136,121,132,126,138],
[128,112,119,115,128,115,0,136,125,127,111,131],
[112,122,118,106,129,114,114,0,118,134,120,110],
[128,131,108,129,118,129,125,132,0,149,122,117],
[111,85,82,112,109,118,123,116,101,0,105,95],
[132,118,127,121,129,124,139,130,128,145,0,140],
[113,119,126,120,121,112,119,140,133,155,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 54, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,130,120,117,128,128,136,119,114,116],
[123,0,120,128,115,132,116,113,117,121,128,133],
[127,130,0,146,120,131,121,113,126,126,134,130],
[120,122,104,0,122,136,122,126,114,114,118,113],
[130,135,130,128,0,135,121,134,130,130,139,134],
[133,118,119,114,115,0,120,122,128,117,118,115],
[122,134,129,128,129,130,0,131,130,123,134,137],
[122,137,137,124,116,128,119,0,129,122,119,124],
[114,133,124,136,120,122,120,121,0,118,126,126],
[131,129,124,136,120,133,127,128,132,0,130,132],
[136,122,116,132,111,132,116,131,124,120,0,132],
[134,117,120,137,116,135,113,126,124,118,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 55, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,128,122,129,143,128,125,122,132,134,132],
[120,0,121,116,129,123,121,119,121,121,129,129],
[122,129,0,125,127,126,123,128,120,130,131,139],
[128,134,125,0,130,136,123,114,126,123,133,134],
[121,121,123,120,0,135,123,121,118,129,129,140],
[107,127,124,114,115,0,116,118,108,128,134,127],
[122,129,127,127,127,134,0,130,126,142,139,130],
[125,131,122,136,129,132,120,0,130,133,135,136],
[128,129,130,124,132,142,124,120,0,125,134,128],
[118,129,120,127,121,122,108,117,125,0,114,138],
[116,121,119,117,121,116,111,115,116,136,0,128],
[118,121,111,116,110,123,120,114,122,112,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 56, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,121,121,105,104,110,114,110,124,114,105],
[130,0,134,138,125,112,103,138,110,135,123,114],
[129,116,0,139,139,109,114,132,119,118,145,125],
[129,112,111,0,119,103,110,117,112,121,116,108],
[145,125,111,131,0,127,119,140,135,116,124,126],
[146,138,141,147,123,0,132,138,121,128,137,135],
[140,147,136,140,131,118,0,146,127,151,143,121],
[136,112,118,133,110,112,104,0,98,118,115,125],
[140,140,131,138,115,129,123,152,0,141,130,124],
[126,115,132,129,134,122,99,132,109,0,122,113],
[136,127,105,134,126,113,107,135,120,128,0,128],
[145,136,125,142,124,115,129,125,126,137,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 57, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,122,138,132,128,142,142,136,116,128,110],
[133,0,118,120,107,127,125,118,142,137,130,121],
[128,132,0,149,119,119,145,142,155,150,122,120],
[112,130,101,0,101,125,115,101,130,120,80,90],
[118,143,131,149,0,112,158,146,144,147,121,118],
[122,123,131,125,138,0,131,153,110,136,123,126],
[108,125,105,135,92,119,0,116,128,118,102,110],
[108,132,108,149,104,97,134,0,112,126,114,103],
[114,108,95,120,106,140,122,138,0,139,108,104],
[134,113,100,130,103,114,132,124,111,0,114,132],
[122,120,128,170,129,127,148,136,142,136,0,101],
[140,129,130,160,132,124,140,147,146,118,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 58, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,138,132,137,117,134,141,114,130,142],
[114,0,123,135,129,124,122,136,139,129,114,147],
[124,127,0,120,127,125,120,136,146,129,137,142],
[112,115,130,0,130,128,126,125,124,122,119,138],
[118,121,123,120,0,124,121,133,137,126,120,137],
[113,126,125,122,126,0,131,137,129,124,133,139],
[133,128,130,124,129,119,0,130,136,125,122,148],
[116,114,114,125,117,113,120,0,130,126,126,135],
[109,111,104,126,113,121,114,120,0,123,111,128],
[136,121,121,128,124,126,125,124,127,0,124,144],
[120,136,113,131,130,117,128,124,139,126,0,149],
[108,103,108,112,113,111,102,115,122,106,101,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 59, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,118,145,138,150,117,136,152,96,111,130],
[118,0,122,137,126,140,115,121,133,129,111,108],
[132,128,0,95,127,126,106,129,108,118,112,124],
[105,113,155,0,108,121,127,116,107,139,128,119],
[112,124,123,142,0,113,110,117,123,117,109,135],
[100,110,124,129,137,0,108,111,111,93,113,130],
[133,135,144,123,140,142,0,143,149,112,125,149],
[114,129,121,134,133,139,107,0,110,103,129,118],
[98,117,142,143,127,139,101,140,0,104,125,132],
[154,121,132,111,133,157,138,147,146,0,110,147],
[139,139,138,122,141,137,125,121,125,140,0,123],
[120,142,126,131,115,120,101,132,118,103,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 60, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,122,133,129,133,123,134,125,131,118,126],
[140,0,130,141,136,127,127,129,121,133,132,131],
[128,120,0,129,129,125,132,130,117,128,116,117],
[117,109,121,0,135,125,115,125,113,116,110,111],
[121,114,121,115,0,131,123,125,112,110,124,109],
[117,123,125,125,119,0,111,136,111,119,115,122],
[127,123,118,135,127,139,0,130,125,132,135,119],
[116,121,120,125,125,114,120,0,126,128,117,126],
[125,129,133,137,138,139,125,124,0,140,130,129],
[119,117,122,134,140,131,118,122,110,0,122,116],
[132,118,134,140,126,135,115,133,120,128,0,131],
[124,119,133,139,141,128,131,124,121,134,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 61, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,120,130,117,119,132,131,136,125,121,133],
[131,0,116,118,114,120,139,130,122,122,108,133],
[130,134,0,134,132,115,136,108,126,121,115,131],
[120,132,116,0,125,123,142,115,130,127,123,135],
[133,136,118,125,0,121,132,116,130,129,132,132],
[131,130,135,127,129,0,135,125,132,136,123,132],
[118,111,114,108,118,115,0,107,120,115,107,117],
[119,120,142,135,134,125,143,0,142,142,119,127],
[114,128,124,120,120,118,130,108,0,110,117,113],
[125,128,129,123,121,114,135,108,140,0,124,130],
[129,142,135,127,118,127,143,131,133,126,0,137],
[117,117,119,115,118,118,133,123,137,120,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 62, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,125,110,97,120,122,83,104,126,111,114],
[132,0,137,121,128,126,126,124,118,156,141,131],
[125,113,0,126,116,112,113,83,102,128,114,102],
[140,129,124,0,126,118,118,104,95,141,130,147],
[153,122,134,124,0,138,138,140,133,153,146,152],
[130,124,138,132,112,0,120,109,126,125,122,111],
[128,124,137,132,112,130,0,109,92,127,111,131],
[167,126,167,146,110,141,141,0,124,137,167,146],
[146,132,148,155,117,124,158,126,0,131,135,156],
[124,94,122,109,97,125,123,113,119,0,109,121],
[139,109,136,120,104,128,139,83,115,141,0,112],
[136,119,148,103,98,139,119,104,94,129,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 63, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,131,116,127,115,138,139,137,127,123,127],
[121,0,130,101,109,79,128,123,104,92,119,110],
[119,120,0,100,127,95,121,123,112,123,101,111],
[134,149,150,0,149,132,142,118,103,125,125,147],
[123,141,123,101,0,114,119,137,115,115,129,101],
[135,171,155,118,136,0,155,138,133,133,154,123],
[112,122,129,108,131,95,0,119,114,121,109,112],
[111,127,127,132,113,112,131,0,107,111,129,107],
[113,146,138,147,135,117,136,143,0,126,127,121],
[123,158,127,125,135,117,129,139,124,0,147,120],
[127,131,149,125,121,96,141,121,123,103,0,97],
[123,140,139,103,149,127,138,143,129,130,153,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 64, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,136,115,116,107,126,111,126,122,138,139],
[134,0,110,99,107,107,138,127,109,124,132,137],
[114,140,0,110,96,116,128,125,122,130,136,130],
[135,151,140,0,128,126,136,144,117,146,144,152],
[134,143,154,122,0,134,140,129,118,130,122,138],
[143,143,134,124,116,0,132,144,132,114,132,139],
[124,112,122,114,110,118,0,124,117,135,114,136],
[139,123,125,106,121,106,126,0,110,132,127,135],
[124,141,128,133,132,118,133,140,0,130,141,127],
[128,126,120,104,120,136,115,118,120,0,113,140],
[112,118,114,106,128,118,136,123,109,137,0,135],
[111,113,120,98,112,111,114,115,123,110,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 65, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,104,125,125,145,114,140,160,158,146,118],
[98,0,95,120,138,144,135,123,143,125,147,126],
[146,155,0,110,120,152,118,151,152,171,137,121],
[125,130,140,0,120,156,115,151,172,168,144,133],
[125,112,130,130,0,132,110,134,112,134,140,80],
[105,106,98,94,118,0,86,154,136,110,128,97],
[136,115,132,135,140,164,0,146,163,152,132,126],
[110,127,99,99,116,96,104,0,122,132,139,114],
[90,107,98,78,138,114,87,128,0,95,131,102],
[92,125,79,82,116,140,98,118,155,0,121,131],
[104,103,113,106,110,122,118,111,119,129,0,96],
[132,124,129,117,170,153,124,136,148,119,154,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 66, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,94,126,119,113,106,116,140,106,132,105],
[151,0,113,138,123,172,117,153,131,111,147,101],
[156,137,0,160,144,158,136,135,163,119,168,100],
[124,112,90,0,98,125,102,120,105,102,136,78],
[131,127,106,152,0,148,116,149,136,128,154,104],
[137,78,92,125,102,0,87,105,120,96,112,73],
[144,133,114,148,134,163,0,153,147,127,140,130],
[134,97,115,130,101,145,97,0,142,86,123,110],
[110,119,87,145,114,130,103,108,0,121,131,109],
[144,139,131,148,122,154,123,164,129,0,146,115],
[118,103,82,114,96,138,110,127,119,104,0,101],
[145,149,150,172,146,177,120,140,141,135,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 67, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,126,124,118,138,135,143,127,131,140,123],
[103,0,125,124,130,135,139,132,130,118,121,110],
[124,125,0,132,124,135,143,141,126,122,138,110],
[126,126,118,0,121,146,160,133,134,134,129,118],
[132,120,126,129,0,138,138,135,124,131,122,128],
[112,115,115,104,112,0,125,126,112,122,125,102],
[115,111,107,90,112,125,0,121,117,126,114,101],
[107,118,109,117,115,124,129,0,111,118,135,109],
[123,120,124,116,126,138,133,139,0,124,128,113],
[119,132,128,116,119,128,124,132,126,0,122,104],
[110,129,112,121,128,125,136,115,122,128,0,101],
[127,140,140,132,122,148,149,141,137,146,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 68, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,105,135,117,135,115,110,74,112,126,92],
[98,0,90,120,80,71,87,125,78,115,98,97],
[145,160,0,144,144,137,137,155,124,139,127,129],
[115,130,106,0,116,113,131,96,91,108,131,113],
[133,170,106,134,0,121,135,147,106,167,94,115],
[115,179,113,137,129,0,111,109,89,133,117,127],
[135,163,113,119,115,139,0,152,126,167,111,131],
[140,125,95,154,103,141,98,0,80,98,113,105],
[176,172,126,159,144,161,124,170,0,161,144,129],
[138,135,111,142,83,117,83,152,89,0,104,108],
[124,152,123,119,156,133,139,137,106,146,0,126],
[158,153,121,137,135,123,119,145,121,142,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 69, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,114,125,132,116,121,128,120,118,154,112],
[121,0,122,131,131,126,134,134,126,126,148,123],
[136,128,0,130,132,132,134,128,120,131,136,114],
[125,119,120,0,142,118,125,137,130,126,144,124],
[118,119,118,108,0,127,143,132,129,137,132,126],
[134,124,118,132,123,0,133,136,114,114,147,124],
[129,116,116,125,107,117,0,115,113,123,136,106],
[122,116,122,113,118,114,135,0,125,131,130,110],
[130,124,130,120,121,136,137,125,0,136,140,139],
[132,124,119,124,113,136,127,119,114,0,138,131],
[96,102,114,106,118,103,114,120,110,112,0,103],
[138,127,136,126,124,126,144,140,111,119,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 70, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,126,113,151,119,133,100,116,115,130,136],
[123,0,143,109,165,122,110,96,140,123,127,147],
[124,107,0,120,167,127,131,115,141,127,125,135],
[137,141,130,0,162,125,156,127,136,150,155,156],
[99,85,83,88,0,94,118,104,93,86,93,103],
[131,128,123,125,156,0,142,127,142,118,133,126],
[117,140,119,94,132,108,0,89,143,125,121,116],
[150,154,135,123,146,123,161,0,164,127,145,155],
[134,110,109,114,157,108,107,86,0,126,153,139],
[135,127,123,100,164,132,125,123,124,0,134,147],
[120,123,125,95,157,117,129,105,97,116,0,120],
[114,103,115,94,147,124,134,95,111,103,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 71, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,122,146,147,132,135,140,134,139,147,152],
[108,0,126,144,125,126,125,149,93,142,144,115],
[128,124,0,148,129,135,128,148,124,143,133,133],
[104,106,102,0,125,125,112,132,126,124,126,111],
[103,125,121,125,0,120,127,130,115,137,118,112],
[118,124,115,125,130,0,112,152,121,131,133,124],
[115,125,122,138,123,138,0,141,98,140,124,129],
[110,101,102,118,120,98,109,0,96,119,136,115],
[116,157,126,124,135,129,152,154,0,146,161,135],
[111,108,107,126,113,119,110,131,104,0,118,127],
[103,106,117,124,132,117,126,114,89,132,0,101],
[98,135,117,139,138,126,121,135,115,123,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 72, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,124,125,138,130,139,122,122,131,122,122],
[106,0,106,111,135,119,111,119,119,118,127,126],
[126,144,0,122,142,133,132,163,102,151,126,94],
[125,139,128,0,150,139,138,126,140,125,128,110],
[112,115,108,100,0,136,119,107,108,122,122,90],
[120,131,117,111,114,0,135,128,105,126,111,117],
[111,139,118,112,131,115,0,114,109,130,112,108],
[128,131,87,124,143,122,136,0,125,132,128,98],
[128,131,148,110,142,145,141,125,0,127,133,114],
[119,132,99,125,128,124,120,118,123,0,119,125],
[128,123,124,122,128,139,138,122,117,131,0,119],
[128,124,156,140,160,133,142,152,136,125,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 73, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,128,110,129,121,131,146,114,130,126,132],
[123,0,127,125,115,137,117,133,118,136,102,127],
[122,123,0,113,131,133,114,135,126,135,118,120],
[140,125,137,0,117,140,124,141,127,134,123,130],
[121,135,119,133,0,141,115,137,131,140,130,133],
[129,113,117,110,109,0,116,125,124,128,123,117],
[119,133,136,126,135,134,0,145,128,138,112,133],
[104,117,115,109,113,125,105,0,116,127,102,113],
[136,132,124,123,119,126,122,134,0,136,117,123],
[120,114,115,116,110,122,112,123,114,0,109,122],
[124,148,132,127,120,127,138,148,133,141,0,148],
[118,123,130,120,117,133,117,137,127,128,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 74, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,126,134,124,129,140,144,129,134,139,123],
[118,0,127,130,118,118,120,133,112,129,121,113],
[124,123,0,132,113,118,125,133,119,122,127,121],
[116,120,118,0,113,131,123,129,119,120,115,115],
[126,132,137,137,0,122,128,135,120,126,128,126],
[121,132,132,119,128,0,115,131,118,133,127,118],
[110,130,125,127,122,135,0,136,117,125,123,121],
[106,117,117,121,115,119,114,0,112,126,112,115],
[121,138,131,131,130,132,133,138,0,129,131,123],
[116,121,128,130,124,117,125,124,121,0,119,121],
[111,129,123,135,122,123,127,138,119,131,0,116],
[127,137,129,135,124,132,129,135,127,129,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 75, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,103,88,126,117,153,109,124,132,93,135],
[136,0,149,109,154,131,162,134,129,148,128,156],
[147,101,0,115,133,145,149,113,116,135,136,157],
[162,141,135,0,175,158,192,128,137,137,111,164],
[124,96,117,75,0,115,140,111,95,97,85,110],
[133,119,105,92,135,0,132,124,137,131,111,159],
[97,88,101,58,110,118,0,91,93,104,91,148],
[141,116,137,122,139,126,159,0,123,131,109,126],
[126,121,134,113,155,113,157,127,0,155,126,132],
[118,102,115,113,153,119,146,119,95,0,108,146],
[157,122,114,139,165,139,159,141,124,142,0,148],
[115,94,93,86,140,91,102,124,118,104,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 76, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,125,89,86,106,102,99,89,91,123,68],
[142,0,107,130,112,137,82,89,121,126,100,114],
[125,143,0,144,124,132,137,86,142,125,118,100],
[161,120,106,0,90,102,133,136,140,119,119,145],
[164,138,126,160,0,150,141,122,131,162,140,119],
[144,113,118,148,100,0,118,125,137,109,111,116],
[148,168,113,117,109,132,0,105,125,118,136,133],
[151,161,164,114,128,125,145,0,110,127,151,136],
[161,129,108,110,119,113,125,140,0,140,78,133],
[159,124,125,131,88,141,132,123,110,0,127,128],
[127,150,132,131,110,139,114,99,172,123,0,127],
[182,136,150,105,131,134,117,114,117,122,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 77, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,125,141,145,118,129,141,140,136,147,138],
[120,0,129,132,117,135,137,138,135,131,147,122],
[125,121,0,125,118,105,124,131,114,123,125,111],
[109,118,125,0,113,116,124,133,135,116,143,118],
[105,133,132,137,0,126,126,139,133,133,146,116],
[132,115,145,134,124,0,127,138,147,140,137,114],
[121,113,126,126,124,123,0,147,133,123,133,113],
[109,112,119,117,111,112,103,0,117,125,121,118],
[110,115,136,115,117,103,117,133,0,131,129,115],
[114,119,127,134,117,110,127,125,119,0,135,104],
[103,103,125,107,104,113,117,129,121,115,0,117],
[112,128,139,132,134,136,137,132,135,146,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 78, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,196,84,86,120,196,211,148,165,148,158,107],
[54,0,0,91,82,138,137,85,109,153,178,71],
[166,250,0,116,138,158,212,207,201,247,201,138],
[164,159,134,0,85,110,139,162,110,131,110,110],
[130,168,112,165,0,161,173,168,126,165,176,117],
[54,112,92,140,89,0,148,123,63,138,153,89],
[39,113,38,111,77,102,0,126,122,99,138,74],
[102,165,43,88,82,127,124,0,127,142,127,153],
[85,141,49,140,124,187,128,123,0,159,149,74],
[102,97,3,119,85,112,151,108,91,0,165,74],
[92,72,49,140,74,97,112,123,101,85,0,46],
[143,179,112,140,133,161,176,97,176,176,204,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 79, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,156,130,107,132,105,106,106,113,123,109],
[142,0,153,141,126,152,122,118,113,138,146,142],
[94,97,0,126,114,118,99,87,85,98,108,93],
[120,109,124,0,105,122,109,117,88,104,118,116],
[143,124,136,145,0,152,142,124,128,147,140,129],
[118,98,132,128,98,0,91,98,78,94,105,96],
[145,128,151,141,108,159,0,131,114,122,145,136],
[144,132,163,133,126,152,119,0,125,141,150,127],
[144,137,165,162,122,172,136,125,0,141,128,144],
[137,112,152,146,103,156,128,109,109,0,111,121],
[127,104,142,132,110,145,105,100,122,139,0,119],
[141,108,157,134,121,154,114,123,106,129,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 80, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,129,165,126,145,143,119,114,148,142,124],
[115,0,119,140,108,124,131,119,109,130,129,116],
[121,131,0,135,111,123,123,121,105,137,132,126],
[85,110,115,0,109,114,115,110,98,117,118,105],
[124,142,139,141,0,143,141,138,123,163,140,138],
[105,126,127,136,107,0,119,113,128,117,123,125],
[107,119,127,135,109,131,0,131,116,136,132,130],
[131,131,129,140,112,137,119,0,119,141,133,118],
[136,141,145,152,127,122,134,131,0,136,147,141],
[102,120,113,133,87,133,114,109,114,0,128,98],
[108,121,118,132,110,127,118,117,103,122,0,112],
[126,134,124,145,112,125,120,132,109,152,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 81, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,155,135,131,122,131,141,139,140,118,118,154],
[95,0,127,132,130,129,131,130,119,100,126,132],
[115,123,0,124,119,139,145,137,125,108,105,150],
[119,118,126,0,126,145,144,137,135,126,108,134],
[128,120,131,124,0,133,133,130,124,120,137,134],
[119,121,111,105,117,0,118,136,114,116,107,123],
[109,119,105,106,117,132,0,128,126,113,106,129],
[111,120,113,113,120,114,122,0,113,118,118,135],
[110,131,125,115,126,136,124,137,0,96,127,142],
[132,150,142,124,130,134,137,132,154,0,133,161],
[132,124,145,142,113,143,144,132,123,117,0,141],
[96,118,100,116,116,127,121,115,108,89,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 82, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,167,129,129,154,123,250,95,198,102,133,160],
[83,0,154,206,206,58,212,95,185,58,133,95],
[121,96,0,250,179,148,250,133,185,154,133,127],
[121,44,0,0,69,96,185,133,185,44,133,37],
[96,44,71,181,0,58,219,95,185,44,133,37],
[127,192,102,154,192,0,192,95,185,75,133,154],
[0,38,0,65,31,58,0,89,133,0,127,37],
[155,155,117,117,155,155,161,0,250,90,69,154],
[52,65,65,65,65,65,117,0,0,0,31,102],
[148,192,96,206,206,175,250,160,250,0,198,154],
[117,117,117,117,117,117,123,181,219,52,0,154],
[90,155,123,213,213,96,213,96,148,96,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 83, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,120,111,129,120,132,123,125,125,119,118],
[141,0,134,127,136,123,129,135,122,135,119,127],
[130,116,0,114,125,119,133,123,125,128,130,133],
[139,123,136,0,133,145,124,141,139,138,127,129],
[121,114,125,117,0,130,132,126,118,122,107,116],
[130,127,131,105,120,0,130,130,124,134,124,123],
[118,121,117,126,118,120,0,138,128,127,127,124],
[127,115,127,109,124,120,112,0,119,125,121,95],
[125,128,125,111,132,126,122,131,0,138,116,120],
[125,115,122,112,128,116,123,125,112,0,120,111],
[131,131,120,123,143,126,123,129,134,130,0,131],
[132,123,117,121,134,127,126,155,130,139,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 84, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,105,132,129,114,121,111,128,122,114,116],
[127,0,99,119,129,124,128,122,133,145,108,110],
[145,151,0,127,134,122,146,117,126,130,108,131],
[118,131,123,0,139,127,143,126,138,128,131,114],
[121,121,116,111,0,104,121,113,119,118,116,102],
[136,126,128,123,146,0,142,145,164,137,121,125],
[129,122,104,107,129,108,0,110,131,119,118,104],
[139,128,133,124,137,105,140,0,149,127,112,125],
[122,117,124,112,131,86,119,101,0,122,103,97],
[128,105,120,122,132,113,131,123,128,0,113,127],
[136,142,142,119,134,129,132,138,147,137,0,118],
[134,140,119,136,148,125,146,125,153,123,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 85, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,122,130,122,133,123,130,116,113,120,118],
[147,0,128,148,144,140,133,135,134,132,121,116],
[128,122,0,128,132,142,131,130,134,116,124,117],
[120,102,122,0,111,122,109,117,123,110,114,108],
[128,106,118,139,0,137,118,138,136,133,105,124],
[117,110,108,128,113,0,122,122,123,121,113,125],
[127,117,119,141,132,128,0,130,126,115,118,132],
[120,115,120,133,112,128,120,0,123,121,110,116],
[134,116,116,127,114,127,124,127,0,126,126,117],
[137,118,134,140,117,129,135,129,124,0,108,108],
[130,129,126,136,145,137,132,140,124,142,0,136],
[132,134,133,142,126,125,118,134,133,142,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 86, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,130,134,120,119,120,115,122,126,107,115],
[122,0,126,104,120,117,95,110,120,111,111,112],
[120,124,0,116,121,126,125,127,115,118,119,100],
[116,146,134,0,134,150,140,135,129,142,144,126],
[130,130,129,116,0,130,115,139,123,102,123,110],
[131,133,124,100,120,0,118,123,113,109,103,114],
[130,155,125,110,135,132,0,146,123,128,116,126],
[135,140,123,115,111,127,104,0,133,110,111,116],
[128,130,135,121,127,137,127,117,0,134,134,131],
[124,139,132,108,148,141,122,140,116,0,132,122],
[143,139,131,106,127,147,134,139,116,118,0,126],
[135,138,150,124,140,136,124,134,119,128,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 87, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,134,152,135,141,132,128,165,145,135,139],
[131,0,124,138,133,129,137,124,152,134,139,136],
[116,126,0,133,131,123,127,126,149,125,129,133],
[98,112,117,0,122,130,111,124,154,119,111,117],
[115,117,119,128,0,129,124,115,140,121,131,131],
[109,121,127,120,121,0,132,118,158,119,122,126],
[118,113,123,139,126,118,0,119,151,115,121,127],
[122,126,124,126,135,132,131,0,145,133,125,128],
[85,98,101,96,110,92,99,105,0,115,90,102],
[105,116,125,131,129,131,135,117,135,0,125,131],
[115,111,121,139,119,128,129,125,160,125,0,124],
[111,114,117,133,119,124,123,122,148,119,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 88, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,117,111,113,145,108,123,112,100,122,136],
[134,0,129,121,112,120,120,113,127,108,135,114],
[133,121,0,104,116,128,122,133,121,119,122,125],
[139,129,146,0,135,136,114,134,127,127,136,127],
[137,138,134,115,0,122,125,164,133,119,143,138],
[105,130,122,114,128,0,118,116,124,120,131,119],
[142,130,128,136,125,132,0,148,142,122,140,133],
[127,137,117,116,86,134,102,0,110,92,129,106],
[138,123,129,123,117,126,108,140,0,117,149,127],
[150,142,131,123,131,130,128,158,133,0,147,132],
[128,115,128,114,107,119,110,121,101,103,0,113],
[114,136,125,123,112,131,117,144,123,118,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 89, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,107,124,111,138,133,134,137,131,128,125],
[108,0,113,138,134,123,117,126,132,128,133,111],
[143,137,0,131,146,143,142,132,141,165,149,121],
[126,112,119,0,139,120,128,120,132,132,134,95],
[139,116,104,111,0,129,134,136,136,110,136,118],
[112,127,107,130,121,0,126,121,114,133,157,135],
[117,133,108,122,116,124,0,130,122,123,141,119],
[116,124,118,130,114,129,120,0,126,128,153,118],
[113,118,109,118,114,136,128,124,0,124,131,127],
[119,122,85,118,140,117,127,122,126,0,134,143],
[122,117,101,116,114,93,109,97,119,116,0,118],
[125,139,129,155,132,115,131,132,123,107,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 90, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,117,121,127,135,117,126,136,127,115,138],
[112,0,109,116,107,121,124,120,118,113,107,121],
[133,141,0,137,121,131,117,133,130,127,124,143],
[129,134,113,0,116,122,121,130,116,120,125,139],
[123,143,129,134,0,137,127,132,135,124,136,144],
[115,129,119,128,113,0,111,127,119,110,113,125],
[133,126,133,129,123,139,0,124,136,120,130,144],
[124,130,117,120,118,123,126,0,122,122,121,141],
[114,132,120,134,115,131,114,128,0,126,118,131],
[123,137,123,130,126,140,130,128,124,0,130,142],
[135,143,126,125,114,137,120,129,132,120,0,143],
[112,129,107,111,106,125,106,109,119,108,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 91, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,143,142,116,126,148,126,130,137,132,135],
[127,0,140,136,134,134,145,130,125,123,148,137],
[107,110,0,113,133,119,125,127,109,117,137,123],
[108,114,137,0,130,132,140,133,112,132,116,136],
[134,116,117,120,0,124,143,130,109,125,134,123],
[124,116,131,118,126,0,137,120,119,129,124,131],
[102,105,125,110,107,113,0,114,100,127,120,120],
[124,120,123,117,120,130,136,0,130,127,139,140],
[120,125,141,138,141,131,150,120,0,128,146,123],
[113,127,133,118,125,121,123,123,122,0,126,133],
[118,102,113,134,116,126,130,111,104,124,0,131],
[115,113,127,114,127,119,130,110,127,117,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 92, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,158,172,103,150,153,125,139,163,145,170,151],
[92,0,81,68,87,105,128,100,127,91,116,111],
[78,169,0,133,111,134,123,89,137,117,122,154],
[147,182,117,0,169,137,167,151,148,125,147,140],
[100,163,139,81,0,141,121,102,107,92,108,145],
[97,145,116,113,109,0,146,83,82,67,122,96],
[125,122,127,83,129,104,0,122,119,82,116,122],
[111,150,161,99,148,167,128,0,133,139,156,130],
[87,123,113,102,143,168,131,117,0,82,130,143],
[105,159,133,125,158,183,168,111,168,0,161,157],
[80,134,128,103,142,128,134,94,120,89,0,122],
[99,139,96,110,105,154,128,120,107,93,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 93, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,146,120,87,126,139,121,131,103,119,122],
[106,0,125,118,92,113,140,114,125,131,129,108],
[104,125,0,116,87,105,118,108,120,103,143,115],
[130,132,134,0,95,102,119,103,125,108,127,111],
[163,158,163,155,0,120,125,135,146,152,153,145],
[124,137,145,148,130,0,138,135,136,150,157,135],
[111,110,132,131,125,112,0,117,123,107,99,104],
[129,136,142,147,115,115,133,0,121,123,125,121],
[119,125,130,125,104,114,127,129,0,136,122,122],
[147,119,147,142,98,100,143,127,114,0,113,120],
[131,121,107,123,97,93,151,125,128,137,0,127],
[128,142,135,139,105,115,146,129,128,130,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 94, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,136,126,123,131,132,136,107,127,129,126],
[127,0,123,127,117,115,130,126,115,127,124,116],
[114,127,0,123,121,124,118,142,111,127,123,111],
[124,123,127,0,131,122,126,125,121,129,118,118],
[127,133,129,119,0,121,132,136,124,130,135,127],
[119,135,126,128,129,0,124,136,116,126,125,109],
[118,120,132,124,118,126,0,129,109,128,117,121],
[114,124,108,125,114,114,121,0,113,103,113,116],
[143,135,139,129,126,134,141,137,0,135,142,116],
[123,123,123,121,120,124,122,147,115,0,138,125],
[121,126,127,132,115,125,133,137,108,112,0,118],
[124,134,139,132,123,141,129,134,134,125,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 95, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,133,152,121,134,144,130,138,136,120,150],
[108,0,96,125,102,102,123,89,118,106,124,125],
[117,154,0,174,114,131,138,126,131,151,137,163],
[98,125,76,0,111,122,110,105,127,125,127,127],
[129,148,136,139,0,142,130,125,124,146,116,133],
[116,148,119,128,108,0,159,118,120,128,122,154],
[106,127,112,140,120,91,0,105,113,130,127,126],
[120,161,124,145,125,132,145,0,131,136,129,149],
[112,132,119,123,126,130,137,119,0,138,143,144],
[114,144,99,125,104,122,120,114,112,0,121,118],
[130,126,113,123,134,128,123,121,107,129,0,150],
[100,125,87,123,117,96,124,101,106,132,100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 96, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,121,121,127,115,109,117,121,122,115,127],
[124,0,106,96,124,113,104,118,120,120,114,119],
[129,144,0,121,134,123,108,118,135,132,125,127],
[129,154,129,0,124,122,129,136,136,131,121,133],
[123,126,116,126,0,105,113,119,137,126,110,131],
[135,137,127,128,145,0,128,124,129,145,126,136],
[141,146,142,121,137,122,0,115,140,147,124,132],
[133,132,132,114,131,126,135,0,143,140,144,128],
[129,130,115,114,113,121,110,107,0,122,121,124],
[128,130,118,119,124,105,103,110,128,0,127,121],
[135,136,125,129,140,124,126,106,129,123,0,132],
[123,131,123,117,119,114,118,122,126,129,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 97, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,126,134,147,124,125,120,142,145,139,135],
[98,0,103,123,140,103,101,109,111,123,128,114],
[124,147,0,131,175,122,138,119,134,151,153,136],
[116,127,119,0,118,102,139,96,100,112,110,87],
[103,110,75,132,0,98,100,98,121,123,113,103],
[126,147,128,148,152,0,134,141,125,154,132,137],
[125,149,112,111,150,116,0,96,118,139,148,121],
[130,141,131,154,152,109,154,0,131,163,143,107],
[108,139,116,150,129,125,132,119,0,119,130,116],
[105,127,99,138,127,96,111,87,131,0,101,99],
[111,122,97,140,137,118,102,107,120,149,0,128],
[115,136,114,163,147,113,129,143,134,151,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 98, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,125,131,131,130,141,118,128,131,125,138],
[121,0,117,125,121,124,128,126,129,140,121,133],
[125,133,0,128,125,130,124,123,131,138,118,134],
[119,125,122,0,124,126,128,123,123,137,107,126],
[119,129,125,126,0,121,118,115,119,130,116,125],
[120,126,120,124,129,0,124,119,124,130,117,130],
[109,122,126,122,132,126,0,122,129,143,117,129],
[132,124,127,127,135,131,128,0,128,147,123,135],
[122,121,119,127,131,126,121,122,0,134,119,121],
[119,110,112,113,120,120,107,103,116,0,107,120],
[125,129,132,143,134,133,133,127,131,143,0,137],
[112,117,116,124,125,120,121,115,129,130,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 99, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,119,128,126,110,121,132,113,122,115,128],
[118,0,111,124,125,121,122,115,112,126,112,137],
[131,139,0,122,134,126,128,135,119,131,122,134],
[122,126,128,0,129,122,131,123,123,133,110,132],
[124,125,116,121,0,116,128,120,112,119,112,125],
[140,129,124,128,134,0,138,123,112,132,119,141],
[129,128,122,119,122,112,0,123,114,133,126,142],
[118,135,115,127,130,127,127,0,125,140,118,139],
[137,138,131,127,138,138,136,125,0,139,125,136],
[128,124,119,117,131,118,117,110,111,0,106,132],
[135,138,128,140,138,131,124,132,125,144,0,138],
[122,113,116,118,125,109,108,111,114,118,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 100, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,130,123,141,133,125,133,136,135,136,126],
[129,0,134,138,148,134,123,135,129,133,130,121],
[120,116,0,126,146,132,127,139,137,139,141,130],
[127,112,124,0,134,127,115,144,138,132,130,130],
[109,102,104,116,0,113,100,113,118,123,127,111],
[117,116,118,123,137,0,127,119,129,127,130,116],
[125,127,123,135,150,123,0,130,131,130,141,123],
[117,115,111,106,137,131,120,0,134,117,133,115],
[114,121,113,112,132,121,119,116,0,129,136,118],
[115,117,111,118,127,123,120,133,121,0,134,119],
[114,120,109,120,123,120,109,117,114,116,0,125],
[124,129,120,120,139,134,127,135,132,131,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 101, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,124,99,138,136,122,120,132,101,122,133],
[138,0,139,107,138,145,140,127,145,133,126,152],
[126,111,0,115,120,126,144,109,119,115,121,124],
[151,143,135,0,132,136,136,131,135,119,134,146],
[112,112,130,118,0,123,123,86,111,113,109,116],
[114,105,124,114,127,0,133,114,112,106,122,122],
[128,110,106,114,127,117,0,106,125,114,122,120],
[130,123,141,119,164,136,144,0,123,128,154,148],
[118,105,131,115,139,138,125,127,0,111,134,146],
[149,117,135,131,137,144,136,122,139,0,138,146],
[128,124,129,116,141,128,128,96,116,112,0,136],
[117,98,126,104,134,128,130,102,104,104,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 102, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,123,112,121,133,121,129,136,119,129,124],
[129,0,112,126,118,127,129,123,125,118,118,127],
[127,138,0,131,129,131,129,130,127,117,135,138],
[138,124,119,0,129,141,128,133,137,128,128,136],
[129,132,121,121,0,136,133,132,125,125,127,133],
[117,123,119,109,114,0,118,125,130,111,125,123],
[129,121,121,122,117,132,0,120,122,114,128,120],
[121,127,120,117,118,125,130,0,129,119,124,131],
[114,125,123,113,125,120,128,121,0,125,123,130],
[131,132,133,122,125,139,136,131,125,0,133,122],
[121,132,115,122,123,125,122,126,127,117,0,123],
[126,123,112,114,117,127,130,119,120,128,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 103, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,121,124,115,115,120,80,122,105,109,122],
[130,0,138,128,122,118,142,94,133,105,132,134],
[129,112,0,127,111,116,136,102,104,112,114,101],
[126,122,123,0,130,86,122,99,107,101,94,107],
[135,128,139,120,0,119,127,125,124,108,118,131],
[135,132,134,164,131,0,141,112,155,133,126,151],
[130,108,114,128,123,109,0,96,131,97,109,115],
[170,156,148,151,125,138,154,0,159,137,134,154],
[128,117,146,143,126,95,119,91,0,125,130,137],
[145,145,138,149,142,117,153,113,125,0,123,131],
[141,118,136,156,132,124,141,116,120,127,0,122],
[128,116,149,143,119,99,135,96,113,119,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 104, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,125,128,121,120,143,127,138,128,131,123],
[113,0,117,114,114,121,108,127,125,118,126,113],
[125,133,0,126,113,125,135,131,124,127,124,126],
[122,136,124,0,120,120,132,128,124,123,127,123],
[129,136,137,130,0,138,135,137,137,140,141,124],
[130,129,125,130,112,0,126,134,123,132,126,115],
[107,142,115,118,115,124,0,133,121,118,124,118],
[123,123,119,122,113,116,117,0,118,111,116,113],
[112,125,126,126,113,127,129,132,0,126,123,115],
[122,132,123,127,110,118,132,139,124,0,122,129],
[119,124,126,123,109,124,126,134,127,128,0,116],
[127,137,124,127,126,135,132,137,135,121,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 105, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,107,131,124,130,128,130,139,134,118,114],
[132,0,114,118,107,129,129,130,134,134,125,119],
[143,136,0,144,124,152,132,147,152,137,147,115],
[119,132,106,0,111,133,121,132,140,104,109,111],
[126,143,126,139,0,138,129,143,149,143,115,119],
[120,121,98,117,112,0,110,128,120,119,109,118],
[122,121,118,129,121,140,0,144,148,131,139,130],
[120,120,103,118,107,122,106,0,146,105,109,106],
[111,116,98,110,101,130,102,104,0,98,114,98],
[116,116,113,146,107,131,119,145,152,0,111,120],
[132,125,103,141,135,141,111,141,136,139,0,128],
[136,131,135,139,131,132,120,144,152,130,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 106, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,125,109,114,136,136,122,122,121,134,124],
[131,0,127,118,123,139,137,120,124,125,134,129],
[125,123,0,126,117,136,138,129,131,118,136,151],
[141,132,124,0,125,147,153,131,129,132,149,139],
[136,127,133,125,0,136,143,133,133,125,139,138],
[114,111,114,103,114,0,121,106,123,116,120,115],
[114,113,112,97,107,129,0,117,133,116,117,118],
[128,130,121,119,117,144,133,0,122,125,134,127],
[128,126,119,121,117,127,117,128,0,109,135,132],
[129,125,132,118,125,134,134,125,141,0,148,144],
[116,116,114,101,111,130,133,116,115,102,0,122],
[126,121,99,111,112,135,132,123,118,106,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 107, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,129,136,141,126,126,123,121,143,121,136],
[118,0,135,120,118,132,111,118,126,129,113,122],
[121,115,0,110,118,119,114,114,111,124,104,119],
[114,130,140,0,146,141,119,116,126,132,117,122],
[109,132,132,104,0,117,114,110,112,126,111,119],
[124,118,131,109,133,0,130,123,120,130,112,126],
[124,139,136,131,136,120,0,123,134,131,133,123],
[127,132,136,134,140,127,127,0,129,151,121,120],
[129,124,139,124,138,130,116,121,0,135,121,136],
[107,121,126,118,124,120,119,99,115,0,117,119],
[129,137,146,133,139,138,117,129,129,133,0,125],
[114,128,131,128,131,124,127,130,114,131,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 108, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,140,161,128,135,147,149,149,138,99,116],
[120,0,156,147,139,134,147,158,156,160,141,132],
[110,94,0,134,136,99,112,152,119,116,126,128],
[89,103,116,0,135,107,112,116,127,120,129,118],
[122,111,114,115,0,113,109,134,145,110,89,117],
[115,116,151,143,137,0,145,142,124,120,143,147],
[103,103,138,138,141,105,0,148,130,89,129,111],
[101,92,98,134,116,108,102,0,122,118,93,113],
[101,94,131,123,105,126,120,128,0,125,131,114],
[112,90,134,130,140,130,161,132,125,0,124,119],
[151,109,124,121,161,107,121,157,119,126,0,123],
[134,118,122,132,133,103,139,137,136,131,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 109, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,130,141,134,132,132,129,130,142,132,136],
[125,0,124,120,121,111,131,120,119,130,124,118],
[120,126,0,122,127,121,118,120,126,125,117,127],
[109,130,128,0,129,117,125,120,123,129,118,134],
[116,129,123,121,0,107,118,118,117,120,106,118],
[118,139,129,133,143,0,139,118,122,137,119,129],
[118,119,132,125,132,111,0,116,113,131,121,134],
[121,130,130,130,132,132,134,0,127,132,125,123],
[120,131,124,127,133,128,137,123,0,127,119,126],
[108,120,125,121,130,113,119,118,123,0,108,123],
[118,126,133,132,144,131,129,125,131,142,0,128],
[114,132,123,116,132,121,116,127,124,127,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 110, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,111,118,116,130,125,124,128,120,138,140],
[131,0,124,123,121,135,127,122,126,132,127,132],
[139,126,0,109,105,124,126,122,126,127,129,131],
[132,127,141,0,130,132,134,119,132,141,133,132],
[134,129,145,120,0,138,131,135,130,143,137,146],
[120,115,126,118,112,0,123,112,124,130,135,129],
[125,123,124,116,119,127,0,125,121,131,127,126],
[126,128,128,131,115,138,125,0,138,132,120,144],
[122,124,124,118,120,126,129,112,0,127,127,131],
[130,118,123,109,107,120,119,118,123,0,126,126],
[112,123,121,117,113,115,123,130,123,124,0,136],
[110,118,119,118,104,121,124,106,119,124,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 111, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,120,126,121,118,135,128,121,116,120,112],
[114,0,113,124,124,111,134,114,117,110,110,119],
[130,137,0,135,129,121,130,130,128,122,122,138],
[124,126,115,0,125,125,124,116,119,115,120,120],
[129,126,121,125,0,128,134,123,119,123,125,128],
[132,139,129,125,122,0,146,131,139,133,138,134],
[115,116,120,126,116,104,0,113,108,112,118,109],
[122,136,120,134,127,119,137,0,117,126,125,134],
[129,133,122,131,131,111,142,133,0,121,121,121],
[134,140,128,135,127,117,138,124,129,0,134,128],
[130,140,128,130,125,112,132,125,129,116,0,124],
[138,131,112,130,122,116,141,116,129,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 112, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,123,105,108,110,93,115,79,100,105,105],
[141,0,128,133,130,116,140,120,98,122,144,119],
[127,122,0,117,136,105,107,116,120,99,130,113],
[145,117,133,0,131,128,123,123,101,130,137,115],
[142,120,114,119,0,117,106,129,110,123,131,138],
[140,134,145,122,133,0,126,150,126,126,130,131],
[157,110,143,127,144,124,0,131,128,123,144,111],
[135,130,134,127,121,100,119,0,106,78,100,131],
[171,152,130,149,140,124,122,144,0,155,160,137],
[150,128,151,120,127,124,127,172,95,0,142,142],
[145,106,120,113,119,120,106,150,90,108,0,111],
[145,131,137,135,112,119,139,119,113,108,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 113, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,111,114,119,135,119,123,112,110,119,126],
[127,0,123,124,122,135,118,122,117,126,127,125],
[139,127,0,134,128,133,125,144,131,129,132,125],
[136,126,116,0,125,134,133,141,127,133,125,121],
[131,128,122,125,0,139,133,144,115,129,130,128],
[115,115,117,116,111,0,114,128,104,112,102,116],
[131,132,125,117,117,136,0,122,124,127,121,119],
[127,128,106,109,106,122,128,0,108,115,104,109],
[138,133,119,123,135,146,126,142,0,136,127,122],
[140,124,121,117,121,138,123,135,114,0,119,120],
[131,123,118,125,120,148,129,146,123,131,0,129],
[124,125,125,129,122,134,131,141,128,130,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 114, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,127,140,126,125,135,119,136,133,141,141],
[131,0,126,129,129,113,136,136,134,123,137,134],
[123,124,0,136,135,116,139,118,128,123,138,136],
[110,121,114,0,110,119,128,118,121,121,129,122],
[124,121,115,140,0,121,143,123,128,125,133,140],
[125,137,134,131,129,0,140,129,144,129,136,143],
[115,114,111,122,107,110,0,102,119,121,127,135],
[131,114,132,132,127,121,148,0,134,128,136,141],
[114,116,122,129,122,106,131,116,0,128,125,131],
[117,127,127,129,125,121,129,122,122,0,134,131],
[109,113,112,121,117,114,123,114,125,116,0,131],
[109,116,114,128,110,107,115,109,119,119,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 115, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,123,123,118,134,124,126,112,122,127,136],
[126,0,138,123,123,143,121,112,124,117,125,126],
[127,112,0,106,132,149,125,108,124,113,124,125],
[127,127,144,0,121,141,143,141,128,128,141,141],
[132,127,118,129,0,142,114,135,134,106,143,141],
[116,107,101,109,108,0,106,103,119,112,99,124],
[126,129,125,107,136,144,0,120,119,108,140,132],
[124,138,142,109,115,147,130,0,117,121,124,134],
[138,126,126,122,116,131,131,133,0,125,136,134],
[128,133,137,122,144,138,142,129,125,0,137,129],
[123,125,126,109,107,151,110,126,114,113,0,129],
[114,124,125,109,109,126,118,116,116,121,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 116, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,126,124,120,121,134,139,120,127,119,115],
[119,0,131,121,124,125,118,127,128,122,122,119],
[124,119,0,116,124,125,132,118,109,127,118,119],
[126,129,134,0,128,119,130,132,123,128,127,123],
[130,126,126,122,0,124,118,122,120,117,123,128],
[129,125,125,131,126,0,131,144,119,120,124,119],
[116,132,118,120,132,119,0,131,114,115,120,114],
[111,123,132,118,128,106,119,0,116,112,110,128],
[130,122,141,127,130,131,136,134,0,124,129,121],
[123,128,123,122,133,130,135,138,126,0,126,118],
[131,128,132,123,127,126,130,140,121,124,0,118],
[135,131,131,127,122,131,136,122,129,132,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 117, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,123,133,129,141,136,128,129,132,130,148],
[104,0,119,105,116,115,121,118,111,111,112,120],
[127,131,0,135,133,130,149,128,133,124,129,146],
[117,145,115,0,123,125,140,110,125,122,106,122],
[121,134,117,127,0,129,141,121,126,122,125,132],
[109,135,120,125,121,0,135,123,125,127,122,127],
[114,129,101,110,109,115,0,105,116,107,117,127],
[122,132,122,140,129,127,145,0,129,134,129,134],
[121,139,117,125,124,125,134,121,0,133,120,126],
[118,139,126,128,128,123,143,116,117,0,120,149],
[120,138,121,144,125,128,133,121,130,130,0,147],
[102,130,104,128,118,123,123,116,124,101,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 118, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,125,122,123,125,118,110,129,125,129,129],
[124,0,117,116,117,126,125,121,115,133,130,116],
[125,133,0,112,133,127,120,117,135,132,128,125],
[128,134,138,0,139,133,121,131,140,134,129,133],
[127,133,117,111,0,124,115,119,118,127,124,121],
[125,124,123,117,126,0,121,119,122,126,129,115],
[132,125,130,129,135,129,0,121,125,136,126,135],
[140,129,133,119,131,131,129,0,132,140,134,136],
[121,135,115,110,132,128,125,118,0,121,126,123],
[125,117,118,116,123,124,114,110,129,0,120,113],
[121,120,122,121,126,121,124,116,124,130,0,119],
[121,134,125,117,129,135,115,114,127,137,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 119, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,106,108,142,128,151,140,132,150,134,139],
[116,0,106,110,128,122,125,119,143,118,142,124],
[144,144,0,124,137,149,150,118,141,136,129,105],
[142,140,126,0,118,137,147,120,137,147,141,136],
[108,122,113,132,0,114,146,118,132,131,136,122],
[122,128,101,113,136,0,155,102,121,141,135,137],
[99,125,100,103,104,95,0,85,113,114,119,103],
[110,131,132,130,132,148,165,0,146,142,132,113],
[118,107,109,113,118,129,137,104,0,131,118,120],
[100,132,114,103,119,109,136,108,119,0,123,99],
[116,108,121,109,114,115,131,118,132,127,0,125],
[111,126,145,114,128,113,147,137,130,151,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 120, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,132,148,98,101,107,136,126,107,121,96],
[133,0,123,151,86,137,90,119,139,115,115,154],
[118,127,0,127,94,116,117,112,118,141,114,109],
[102,99,123,0,83,92,96,100,120,95,86,89],
[152,164,156,167,0,130,125,174,178,156,120,181],
[149,113,134,158,120,0,82,98,115,115,106,101],
[143,160,133,154,125,168,0,117,134,159,140,143],
[114,131,138,150,76,152,133,0,141,139,149,143],
[124,111,132,130,72,135,116,109,0,87,134,97],
[143,135,109,155,94,135,91,111,163,0,108,120],
[129,135,136,164,130,144,110,101,116,142,0,107],
[154,96,141,161,69,149,107,107,153,130,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 121, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,122,132,135,123,121,124,127,134,144,117],
[118,0,116,125,135,124,117,125,117,126,125,135],
[128,134,0,132,132,122,130,132,121,125,123,125],
[118,125,118,0,132,117,121,115,99,127,119,117],
[115,115,118,118,0,124,123,123,116,105,131,117],
[127,126,128,133,126,0,124,135,114,127,133,120],
[129,133,120,129,127,126,0,113,123,120,125,113],
[126,125,118,135,127,115,137,0,111,121,122,118],
[123,133,129,151,134,136,127,139,0,144,139,131],
[116,124,125,123,145,123,130,129,106,0,125,132],
[106,125,127,131,119,117,125,128,111,125,0,114],
[133,115,125,133,133,130,137,132,119,118,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 122, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,141,129,130,58,88,90,189,76,131,88],
[144,0,147,140,120,110,118,137,159,140,129,99],
[109,103,0,137,128,79,128,104,151,98,136,88],
[121,110,113,0,114,100,104,65,140,85,108,103],
[120,130,122,136,0,143,142,110,128,129,124,105],
[192,140,171,150,107,0,165,156,196,118,147,124],
[162,132,122,146,108,85,0,121,204,123,135,116],
[160,113,146,185,140,94,129,0,186,104,159,131],
[61,91,99,110,122,54,46,64,0,57,77,78],
[174,110,152,165,121,132,127,146,193,0,121,115],
[119,121,114,142,126,103,115,91,173,129,0,89],
[162,151,162,147,145,126,134,119,172,135,161,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 123, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,133,79,92,124,53,84,117,95,144,111],
[100,0,110,73,124,90,103,127,70,118,116,94],
[117,140,0,122,159,159,141,193,116,154,139,134],
[171,177,128,0,164,97,138,158,111,117,160,156],
[158,126,91,86,0,111,61,156,46,123,164,114],
[126,160,91,153,139,0,92,163,128,103,119,71],
[197,147,109,112,189,158,0,202,116,127,167,144],
[166,123,57,92,94,87,48,0,93,70,109,66],
[133,180,134,139,204,122,134,157,0,120,141,141],
[155,132,96,133,127,147,123,180,130,0,132,90],
[106,134,111,90,86,131,83,141,109,118,0,88],
[139,156,116,94,136,179,106,184,109,160,162,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 124, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,137,133,140,131,122,121,134,122,134,123],
[122,0,132,125,132,130,125,123,141,126,125,122],
[113,118,0,117,135,122,127,113,126,116,131,127],
[117,125,133,0,120,130,124,107,124,119,118,116],
[110,118,115,130,0,116,117,106,121,114,122,111],
[119,120,128,120,134,0,122,106,125,118,124,120],
[128,125,123,126,133,128,0,125,136,125,132,128],
[129,127,137,143,144,144,125,0,140,123,134,129],
[116,109,124,126,129,125,114,110,0,121,118,114],
[128,124,134,131,136,132,125,127,129,0,133,119],
[116,125,119,132,128,126,118,116,132,117,0,119],
[127,128,123,134,139,130,122,121,136,131,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 125, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,145,133,110,124,113,118,115,126,120,120],
[117,0,128,129,115,125,109,114,115,115,114,114],
[105,122,0,121,115,114,99,101,99,109,103,121],
[117,121,129,0,110,116,112,115,114,109,118,118],
[140,135,135,140,0,126,122,108,125,126,107,118],
[126,125,136,134,124,0,114,119,118,120,119,118],
[137,141,151,138,128,136,0,130,127,135,125,128],
[132,136,149,135,142,131,120,0,127,127,124,135],
[135,135,151,136,125,132,123,123,0,123,119,131],
[124,135,141,141,124,130,115,123,127,0,126,134],
[130,136,147,132,143,131,125,126,131,124,0,134],
[130,136,129,132,132,132,122,115,119,116,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 126, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,136,132,152,122,108,94,130,119,151,110],
[101,0,148,115,108,141,99,105,132,89,146,104],
[114,102,0,103,131,128,89,74,156,83,86,111],
[118,135,147,0,143,153,121,106,173,105,141,131],
[98,142,119,107,0,118,101,95,108,69,131,91],
[128,109,122,97,132,0,90,65,143,61,108,100],
[142,151,161,129,149,160,0,105,179,116,140,135],
[156,145,176,144,155,185,145,0,145,125,168,175],
[120,118,94,77,142,107,71,105,0,104,127,91],
[131,161,167,145,181,189,134,125,146,0,154,155],
[99,104,164,109,119,142,110,82,123,96,0,93],
[140,146,139,119,159,150,115,75,159,95,157,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 127, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,92,113,98,77,130,123,139,111,174,83,93],
[158,0,109,89,95,135,132,74,78,216,92,98],
[137,141,0,138,92,138,133,161,110,191,147,175],
[152,161,112,0,95,165,135,119,123,159,108,116],
[173,155,158,155,0,143,186,143,93,192,143,138],
[120,115,112,85,107,0,180,130,83,155,133,120],
[127,118,117,115,64,70,0,151,115,162,168,106],
[111,176,89,131,107,120,99,0,142,180,95,126],
[139,172,140,127,157,167,135,108,0,187,113,116],
[76,34,59,91,58,95,88,70,63,0,73,89],
[167,158,103,142,107,117,82,155,137,177,0,89],
[157,152,75,134,112,130,144,124,134,161,161,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 128, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,133,129,131,151,125,135,132,149,131,141],
[111,0,123,132,130,143,112,123,108,132,123,122],
[117,127,0,121,122,130,120,121,118,135,135,126],
[121,118,129,0,128,139,108,125,115,130,123,129],
[119,120,128,122,0,136,122,121,124,137,132,125],
[99,107,120,111,114,0,96,111,109,124,111,133],
[125,138,130,142,128,154,0,127,127,133,139,137],
[115,127,129,125,129,139,123,0,138,128,136,135],
[118,142,132,135,126,141,123,112,0,129,124,138],
[101,118,115,120,113,126,117,122,121,0,133,127],
[119,127,115,127,118,139,111,114,126,117,0,130],
[109,128,124,121,125,117,113,115,112,123,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 129, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,132,132,126,121,130,123,134,118,131,128],
[126,0,115,126,135,138,137,136,122,124,123,124],
[118,135,0,138,127,119,132,130,121,121,123,120],
[118,124,112,0,114,116,123,119,109,110,118,118],
[124,115,123,136,0,120,131,121,131,106,125,113],
[129,112,131,134,130,0,116,126,123,124,121,116],
[120,113,118,127,119,134,0,122,123,108,120,117],
[127,114,120,131,129,124,128,0,117,107,119,124],
[116,128,129,141,119,127,127,133,0,130,114,121],
[132,126,129,140,144,126,142,143,120,0,139,129],
[119,127,127,132,125,129,130,131,136,111,0,135],
[122,126,130,132,137,134,133,126,129,121,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 130, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,142,117,144,136,139,139,127,137,130,114],
[119,0,125,118,120,135,118,117,131,116,113,111],
[108,125,0,128,133,139,134,129,109,124,132,126],
[133,132,122,0,127,140,143,141,132,134,134,139],
[106,130,117,123,0,132,116,118,122,131,131,112],
[114,115,111,110,118,0,119,121,116,140,127,101],
[111,132,116,107,134,131,0,137,131,145,137,113],
[111,133,121,109,132,129,113,0,116,119,112,102],
[123,119,141,118,128,134,119,134,0,130,120,121],
[113,134,126,116,119,110,105,131,120,0,130,125],
[120,137,118,116,119,123,113,138,130,120,0,120],
[136,139,124,111,138,149,137,148,129,125,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 131, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,130,132,133,133,128,113,123,116,130,128],
[127,0,116,117,129,119,113,129,117,123,123,122],
[120,134,0,130,132,132,132,129,109,125,136,121],
[118,133,120,0,131,139,135,125,123,133,141,122],
[117,121,118,119,0,121,123,121,118,122,122,113],
[117,131,118,111,129,0,121,123,111,116,125,126],
[122,137,118,115,127,129,0,114,113,126,124,117],
[137,121,121,125,129,127,136,0,135,131,120,123],
[127,133,141,127,132,139,137,115,0,137,136,125],
[134,127,125,117,128,134,124,119,113,0,126,123],
[120,127,114,109,128,125,126,130,114,124,0,129],
[122,128,129,128,137,124,133,127,125,127,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 132, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,117,115,134,116,141,112,126,123,110,128],
[134,0,119,119,128,117,128,115,112,119,111,127],
[133,131,0,126,135,131,137,129,120,121,134,128],
[135,131,124,0,123,130,135,124,138,129,127,134],
[116,122,115,127,0,117,135,120,133,122,109,121],
[134,133,119,120,133,0,127,111,119,114,112,119],
[109,122,113,115,115,123,0,99,124,107,105,121],
[138,135,121,126,130,139,151,0,123,125,122,123],
[124,138,130,112,117,131,126,127,0,114,116,122],
[127,131,129,121,128,136,143,125,136,0,118,130],
[140,139,116,123,141,138,145,128,134,132,0,143],
[122,123,122,116,129,131,129,127,128,120,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 133, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,108,126,129,122,128,102,130,110,141,104],
[120,0,118,125,126,108,117,114,120,112,120,113],
[142,132,0,124,144,116,123,119,135,122,123,113],
[124,125,126,0,137,119,116,121,134,118,140,111],
[121,124,106,113,0,111,112,110,126,96,115,108],
[128,142,134,131,139,0,123,119,135,129,127,116],
[122,133,127,134,138,127,0,121,143,128,119,112],
[148,136,131,129,140,131,129,0,140,116,138,125],
[120,130,115,116,124,115,107,110,0,110,124,101],
[140,138,128,132,154,121,122,134,140,0,133,118],
[109,130,127,110,135,123,131,112,126,117,0,107],
[146,137,137,139,142,134,138,125,149,132,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 134, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,90,70,139,151,143,157,131,96,84,161,66],
[160,0,128,154,145,144,103,119,101,114,139,128],
[180,122,0,205,184,167,188,198,111,141,194,132],
[111,96,45,0,179,134,155,155,124,119,141,85],
[99,105,66,71,0,116,89,112,103,98,126,98],
[107,106,83,116,134,0,115,133,80,126,94,75],
[93,147,62,95,161,135,0,128,107,67,145,75],
[119,131,52,95,138,117,122,0,86,23,90,110],
[154,149,139,126,147,170,143,164,0,106,133,135],
[166,136,109,131,152,124,183,227,144,0,152,118],
[89,111,56,109,124,156,105,160,117,98,0,65],
[184,122,118,165,152,175,175,140,115,132,185,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 135, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,82,143,89,118,121,56,80,126,98,141],
[196,0,135,172,125,153,146,120,112,168,135,170],
[168,115,0,147,94,132,119,121,98,111,180,157],
[107,78,103,0,15,126,118,63,86,82,106,137],
[161,125,156,235,0,187,169,131,152,170,173,198],
[132,97,118,124,63,0,127,94,102,114,83,143],
[129,104,131,132,81,123,0,117,86,107,109,139],
[194,130,129,187,119,156,133,0,158,127,172,143],
[170,138,152,164,98,148,164,92,0,181,185,178],
[124,82,139,168,80,136,143,123,69,0,130,158],
[152,115,70,144,77,167,141,78,65,120,0,147],
[109,80,93,113,52,107,111,107,72,92,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 136, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,88,76,146,142,115,81,100,130,107,136,145],
[162,0,137,94,154,129,109,117,117,156,87,152],
[174,113,0,132,113,123,127,153,130,134,93,138],
[104,156,118,0,123,141,135,119,125,161,76,134],
[108,96,137,127,0,105,114,116,162,145,136,124],
[135,121,127,109,145,0,119,127,119,100,103,121],
[169,141,123,115,136,131,0,125,154,153,133,131],
[150,133,97,131,134,123,125,0,137,128,113,140],
[120,133,120,125,88,131,96,113,0,150,70,109],
[143,94,116,89,105,150,97,122,100,0,80,96],
[114,163,157,174,114,147,117,137,180,170,0,147],
[105,98,112,116,126,129,119,110,141,154,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 137, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,144,121,106,125,127,132,128,148,110,124],
[127,0,147,151,132,119,151,126,144,151,119,114],
[106,103,0,118,78,107,119,106,112,106,98,101],
[129,99,132,0,117,88,119,107,142,147,124,90],
[144,118,172,133,0,119,150,116,136,146,110,137],
[125,131,143,162,131,0,145,130,149,154,105,112],
[123,99,131,131,100,105,0,122,116,141,126,110],
[118,124,144,143,134,120,128,0,171,162,134,121],
[122,106,138,108,114,101,134,79,0,128,105,119],
[102,99,144,103,104,96,109,88,122,0,117,116],
[140,131,152,126,140,145,124,116,145,133,0,117],
[126,136,149,160,113,138,140,129,131,134,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 138, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,123,122,124,109,133,124,126,143,116,128],
[121,0,112,111,110,100,106,107,97,123,98,92],
[127,138,0,118,126,127,130,113,113,138,100,105],
[128,139,132,0,125,101,138,130,123,140,112,117],
[126,140,124,125,0,111,141,135,137,163,126,134],
[141,150,123,149,139,0,144,123,146,153,133,117],
[117,144,120,112,109,106,0,123,116,142,116,106],
[126,143,137,120,115,127,127,0,120,137,112,102],
[124,153,137,127,113,104,134,130,0,146,122,111],
[107,127,112,110,87,97,108,113,104,0,119,106],
[134,152,150,138,124,117,134,138,128,131,0,113],
[122,158,145,133,116,133,144,148,139,144,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 139, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,195,136,195,110,109,195,168,110,168,195,117],
[55,0,27,85,59,58,86,117,86,59,144,86],
[114,223,0,172,87,109,114,196,86,196,172,114],
[55,165,78,0,138,51,165,196,137,138,117,114],
[140,191,163,112,0,136,144,223,144,196,144,199],
[141,192,141,199,114,0,141,172,141,114,172,141],
[55,164,136,85,106,109,0,137,0,164,85,55],
[82,133,54,54,27,78,113,0,113,55,144,82],
[140,164,164,113,106,109,250,137,0,164,172,113],
[82,191,54,112,54,136,86,195,86,0,144,82],
[55,106,78,133,106,78,165,106,78,106,0,55],
[133,164,136,136,51,109,195,168,137,168,195,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 140, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,140,149,120,141,148,138,149,126,128,136],
[116,0,141,123,124,130,128,123,143,129,120,129],
[110,109,0,120,112,115,125,112,119,105,115,116],
[101,127,130,0,113,118,112,118,130,118,110,123],
[130,126,138,137,0,125,130,125,132,118,123,132],
[109,120,135,132,125,0,124,113,132,123,119,118],
[102,122,125,138,120,126,0,116,134,113,115,123],
[112,127,138,132,125,137,134,0,130,113,121,128],
[101,107,131,120,118,118,116,120,0,114,103,117],
[124,121,145,132,132,127,137,137,136,0,123,124],
[122,130,135,140,127,131,135,129,147,127,0,123],
[114,121,134,127,118,132,127,122,133,126,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 141, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,128,130,132,120,140,127,127,148,127,138],
[119,0,118,106,130,125,118,122,129,127,122,130],
[122,132,0,117,137,124,124,117,127,144,132,133],
[120,144,133,0,140,127,133,131,130,141,128,137],
[118,120,113,110,0,119,123,118,116,135,122,123],
[130,125,126,123,131,0,131,118,132,136,127,122],
[110,132,126,117,127,119,0,114,123,137,125,121],
[123,128,133,119,132,132,136,0,139,142,130,129],
[123,121,123,120,134,118,127,111,0,146,122,109],
[102,123,106,109,115,114,113,108,104,0,114,112],
[123,128,118,122,128,123,125,120,128,136,0,118],
[112,120,117,113,127,128,129,121,141,138,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 142, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,120,116,131,131,116,121,122,120,122,114],
[140,0,123,129,146,133,130,149,135,122,134,111],
[130,127,0,123,142,134,118,121,125,116,140,120],
[134,121,127,0,130,143,126,133,127,125,142,114],
[119,104,108,120,0,122,108,124,129,103,119,110],
[119,117,116,107,128,0,114,125,113,108,127,110],
[134,120,132,124,142,136,0,127,128,116,136,118],
[129,101,129,117,126,125,123,0,117,126,122,107],
[128,115,125,123,121,137,122,133,0,120,123,123],
[130,128,134,125,147,142,134,124,130,0,140,130],
[128,116,110,108,131,123,114,128,127,110,0,112],
[136,139,130,136,140,140,132,143,127,120,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 143, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,123,128,119,121,114,127,123,114,112,131],
[131,0,127,129,126,127,122,136,126,123,126,131],
[127,123,0,129,118,117,113,124,129,117,123,126],
[122,121,121,0,109,121,110,118,128,116,117,130],
[131,124,132,141,0,131,121,139,129,126,123,130],
[129,123,133,129,119,0,112,129,126,111,114,132],
[136,128,137,140,129,138,0,140,138,119,124,137],
[123,114,126,132,111,121,110,0,125,117,112,117],
[127,124,121,122,121,124,112,125,0,122,121,127],
[136,127,133,134,124,139,131,133,128,0,122,136],
[138,124,127,133,127,136,126,138,129,128,0,136],
[119,119,124,120,120,118,113,133,123,114,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 144, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,127,112,110,94,96,107,99,104,137,121],
[136,0,135,130,145,122,122,128,123,142,135,118],
[123,115,0,127,153,116,108,137,115,129,139,115],
[138,120,123,0,140,115,118,148,114,121,152,134],
[140,105,97,110,0,103,110,114,117,111,126,122],
[156,128,134,135,147,0,136,136,125,142,157,135],
[154,128,142,132,140,114,0,135,109,131,146,127],
[143,122,113,102,136,114,115,0,119,102,136,124],
[151,127,135,136,133,125,141,131,0,135,140,141],
[146,108,121,129,139,108,119,148,115,0,139,125],
[113,115,111,98,124,93,104,114,110,111,0,111],
[129,132,135,116,128,115,123,126,109,125,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 145, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,131,128,115,137,126,124,131,127,115,119],
[109,0,133,125,121,127,114,117,116,110,118,128],
[119,117,0,110,119,125,107,114,119,123,129,121],
[122,125,140,0,127,133,121,121,132,115,118,127],
[135,129,131,123,0,142,120,125,134,112,135,127],
[113,123,125,117,108,0,113,109,124,113,119,121],
[124,136,143,129,130,137,0,117,132,120,134,134],
[126,133,136,129,125,141,133,0,138,118,135,123],
[119,134,131,118,116,126,118,112,0,122,117,129],
[123,140,127,135,138,137,130,132,128,0,130,132],
[135,132,121,132,115,131,116,115,133,120,0,123],
[131,122,129,123,123,129,116,127,121,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 146, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,135,125,138,139,132,133,123,132,137,141],
[107,0,120,112,116,126,123,125,113,122,131,134],
[115,130,0,109,123,126,112,133,124,125,133,125],
[125,138,141,0,134,130,127,130,137,122,135,137],
[112,134,127,116,0,131,133,127,125,130,138,138],
[111,124,124,120,119,0,125,133,123,110,123,123],
[118,127,138,123,117,125,0,142,122,129,140,138],
[117,125,117,120,123,117,108,0,117,123,141,118],
[127,137,126,113,125,127,128,133,0,131,139,141],
[118,128,125,128,120,140,121,127,119,0,126,134],
[113,119,117,115,112,127,110,109,111,124,0,118],
[109,116,125,113,112,127,112,132,109,116,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 147, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,134,143,136,141,133,137,118,125,131,132],
[104,0,127,128,116,120,122,124,109,124,127,115],
[116,123,0,121,126,114,122,142,113,133,116,119],
[107,122,129,0,119,114,113,132,106,115,112,117],
[114,134,124,131,0,134,128,137,110,130,132,122],
[109,130,136,136,116,0,122,137,124,127,115,125],
[117,128,128,137,122,128,0,146,125,123,127,130],
[113,126,108,118,113,113,104,0,106,117,113,119],
[132,141,137,144,140,126,125,144,0,139,139,135],
[125,126,117,135,120,123,127,133,111,0,109,121],
[119,123,134,138,118,135,123,137,111,141,0,133],
[118,135,131,133,128,125,120,131,115,129,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 148, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,121,124,121,135,129,135,144,121,140,132],
[139,0,126,120,126,119,120,140,128,121,128,132],
[129,124,0,123,126,116,130,142,163,117,129,128],
[126,130,127,0,151,117,124,131,135,115,136,135],
[129,124,124,99,0,103,129,133,141,114,140,126],
[115,131,134,133,147,0,137,143,147,133,145,142],
[121,130,120,126,121,113,0,137,139,113,121,137],
[115,110,108,119,117,107,113,0,144,113,114,114],
[106,122,87,115,109,103,111,106,0,100,111,116],
[129,129,133,135,136,117,137,137,150,0,127,144],
[110,122,121,114,110,105,129,136,139,123,0,134],
[118,118,122,115,124,108,113,136,134,106,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 149, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,192,113,147,131,144,131,132,152,158,141],
[137,0,171,93,142,103,135,117,138,126,145,120],
[58,79,0,55,53,37,70,66,26,125,104,50],
[137,157,195,0,164,154,181,144,175,169,129,108],
[103,108,197,86,0,113,151,108,132,128,90,128],
[119,147,213,96,137,0,148,160,149,162,145,132],
[106,115,180,69,99,102,0,112,122,154,87,100],
[119,133,184,106,142,90,138,0,99,96,101,108],
[118,112,224,75,118,101,128,151,0,129,98,131],
[98,124,125,81,122,88,96,154,121,0,90,46],
[92,105,146,121,160,105,163,149,152,160,0,103],
[109,130,200,142,122,118,150,142,119,204,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 150, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,139,110,119,119,112,109,117,110,118,129],
[128,0,153,131,122,132,125,137,130,125,120,136],
[111,97,0,89,102,105,91,98,123,104,95,107],
[140,119,161,0,119,121,131,144,126,117,109,120],
[131,128,148,131,0,136,134,125,138,120,115,146],
[131,118,145,129,114,0,118,132,132,117,116,140],
[138,125,159,119,116,132,0,137,140,127,132,129],
[141,113,152,106,125,118,113,0,148,119,111,128],
[133,120,127,124,112,118,110,102,0,101,114,115],
[140,125,146,133,130,133,123,131,149,0,119,124],
[132,130,155,141,135,134,118,139,136,131,0,145],
[121,114,143,130,104,110,121,122,135,126,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 151, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,137,131,147,145,112,138,136,156,148,139],
[114,0,119,133,115,125,101,128,121,126,116,102],
[113,131,0,132,131,132,118,136,139,144,131,113],
[119,117,118,0,123,132,124,133,136,129,126,111],
[103,135,119,127,0,134,127,139,125,144,133,93],
[105,125,118,118,116,0,94,113,122,128,132,98],
[138,149,132,126,123,156,0,156,143,150,140,104],
[112,122,114,117,111,137,94,0,119,133,122,94],
[114,129,111,114,125,128,107,131,0,122,115,105],
[94,124,106,121,106,122,100,117,128,0,121,108],
[102,134,119,124,117,118,110,128,135,129,0,108],
[111,148,137,139,157,152,146,156,145,142,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 152, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,115,129,123,126,121,134,127,125,118,130],
[115,0,112,121,110,123,120,127,128,120,117,115],
[135,138,0,133,125,141,133,132,140,124,129,140],
[121,129,117,0,117,128,116,118,131,126,116,136],
[127,140,125,133,0,131,133,127,138,123,125,135],
[124,127,109,122,119,0,113,119,136,125,110,116],
[129,130,117,134,117,137,0,123,137,132,118,130],
[116,123,118,132,123,131,127,0,130,131,130,126],
[123,122,110,119,112,114,113,120,0,125,117,121],
[125,130,126,124,127,125,118,119,125,0,114,129],
[132,133,121,134,125,140,132,120,133,136,0,129],
[120,135,110,114,115,134,120,124,129,121,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 153, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,130,133,132,137,113,140,123,134,114],
[125,0,121,115,116,130,118,126,126,107,130,113],
[129,129,0,130,124,140,120,132,134,117,124,132],
[120,135,120,0,137,128,124,122,136,114,123,124],
[117,134,126,113,0,123,125,124,143,113,124,119],
[118,120,110,122,127,0,120,120,130,114,115,123],
[113,132,130,126,125,130,0,133,137,121,126,124],
[137,124,118,128,126,130,117,0,138,121,112,119],
[110,124,116,114,107,120,113,112,0,113,118,121],
[127,143,133,136,137,136,129,129,137,0,124,124],
[116,120,126,127,126,135,124,138,132,126,0,120],
[136,137,118,126,131,127,126,131,129,126,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 154, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,144,140,134,137,149,146,132,128,143,124],
[108,0,129,119,114,118,114,122,110,116,118,110],
[106,121,0,126,119,117,123,130,118,124,143,119],
[110,131,124,0,121,124,129,128,114,128,125,124],
[116,136,131,129,0,120,131,133,119,126,126,124],
[113,132,133,126,130,0,140,143,117,122,124,122],
[101,136,127,121,119,110,0,137,113,129,125,130],
[104,128,120,122,117,107,113,0,121,126,127,116],
[118,140,132,136,131,133,137,129,0,136,131,123],
[122,134,126,122,124,128,121,124,114,0,123,115],
[107,132,107,125,124,126,125,123,119,127,0,122],
[126,140,131,126,126,128,120,134,127,135,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 155, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,128,129,129,135,138,123,139,138,137,125],
[131,0,134,138,139,119,142,135,143,134,128,142],
[122,116,0,128,132,129,141,118,129,134,133,131],
[121,112,122,0,130,125,126,136,142,138,121,128],
[121,111,118,120,0,110,124,110,128,130,123,118],
[115,131,121,125,140,0,133,121,130,141,123,132],
[112,108,109,124,126,117,0,120,128,108,106,114],
[127,115,132,114,140,129,130,0,131,128,133,133],
[111,107,121,108,122,120,122,119,0,128,114,117],
[112,116,116,112,120,109,142,122,122,0,116,126],
[113,122,117,129,127,127,144,117,136,134,0,129],
[125,108,119,122,132,118,136,117,133,124,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 156, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,137,136,144,124,142,132,134,132,128,133],
[121,0,126,126,124,132,134,135,131,123,128,127],
[113,124,0,121,129,122,132,128,124,128,118,125],
[114,124,129,0,124,119,130,135,128,128,125,124],
[106,126,121,126,0,117,120,128,126,131,129,118],
[126,118,128,131,133,0,135,135,130,128,123,132],
[108,116,118,120,130,115,0,133,129,125,114,119],
[118,115,122,115,122,115,117,0,112,116,116,122],
[116,119,126,122,124,120,121,138,0,125,129,119],
[118,127,122,122,119,122,125,134,125,0,122,125],
[122,122,132,125,121,127,136,134,121,128,0,122],
[117,123,125,126,132,118,131,128,131,125,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 157, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,115,127,126,116,119,115,109,120,125,110],
[137,0,123,144,128,130,132,135,127,129,129,117],
[135,127,0,140,135,127,134,129,126,126,133,120],
[123,106,110,0,130,112,117,116,99,122,109,102],
[124,122,115,120,0,126,122,123,116,119,119,109],
[134,120,123,138,124,0,127,126,124,122,117,118],
[131,118,116,133,128,123,0,124,124,129,121,117],
[135,115,121,134,127,124,126,0,120,130,132,125],
[141,123,124,151,134,126,126,130,0,130,141,119],
[130,121,124,128,131,128,121,120,120,0,124,125],
[125,121,117,141,131,133,129,118,109,126,0,112],
[140,133,130,148,141,132,133,125,131,125,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 158, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,108,128,120,119,142,127,143,120,141,136],
[117,0,118,129,118,115,134,126,114,132,121,135],
[142,132,0,152,130,125,148,156,131,129,144,139],
[122,121,98,0,112,103,123,107,95,105,122,117],
[130,132,120,138,0,106,143,137,117,141,124,122],
[131,135,125,147,144,0,150,135,139,134,148,119],
[108,116,102,127,107,100,0,120,133,111,137,122],
[123,124,94,143,113,115,130,0,109,124,131,120],
[107,136,119,155,133,111,117,141,0,146,129,122],
[130,118,121,145,109,116,139,126,104,0,123,112],
[109,129,106,128,126,102,113,119,121,127,0,104],
[114,115,111,133,128,131,128,130,128,138,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 159, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,127,139,134,123,135,152,129,129,131,128],
[121,0,122,136,128,117,124,144,135,115,117,116],
[123,128,0,116,129,131,130,129,124,131,116,130],
[111,114,134,0,128,130,135,156,117,133,111,118],
[116,122,121,122,0,121,127,126,110,128,109,119],
[127,133,119,120,129,0,125,144,136,115,121,115],
[115,126,120,115,123,125,0,149,109,116,117,111],
[98,106,121,94,124,106,101,0,93,108,98,98],
[121,115,126,133,140,114,141,157,0,126,139,115],
[121,135,119,117,122,135,134,142,124,0,119,136],
[119,133,134,139,141,129,133,152,111,131,0,126],
[122,134,120,132,131,135,139,152,135,114,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 160, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,120,123,125,142,133,127,110,124,117,142],
[127,0,127,134,132,147,149,131,124,152,131,144],
[130,123,0,122,112,116,129,109,104,138,119,130],
[127,116,128,0,128,140,136,130,134,134,130,145],
[125,118,138,122,0,127,134,123,117,135,128,136],
[108,103,134,110,123,0,134,121,100,123,114,132],
[117,101,121,114,116,116,0,114,102,126,108,117],
[123,119,141,120,127,129,136,0,124,143,129,146],
[140,126,146,116,133,150,148,126,0,144,128,136],
[126,98,112,116,115,127,124,107,106,0,122,135],
[133,119,131,120,122,136,142,121,122,128,0,142],
[108,106,120,105,114,118,133,104,114,115,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 161, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,123,119,127,132,123,117,125,123,127,123],
[126,0,123,120,113,128,111,113,134,107,126,122],
[127,127,0,118,135,128,131,125,127,119,130,124],
[131,130,132,0,134,142,128,124,118,119,134,125],
[123,137,115,116,0,130,127,116,121,113,121,116],
[118,122,122,108,120,0,115,118,111,116,117,115],
[127,139,119,122,123,135,0,111,128,113,124,116],
[133,137,125,126,134,132,139,0,132,134,137,138],
[125,116,123,132,129,139,122,118,0,105,124,115],
[127,143,131,131,137,134,137,116,145,0,143,124],
[123,124,120,116,129,133,126,113,126,107,0,119],
[127,128,126,125,134,135,134,112,135,126,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 162, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,103,134,135,138,133,126,127,127,122,135],
[110,0,114,120,133,114,120,129,129,119,113,111],
[147,136,0,136,134,148,138,127,132,123,110,139],
[116,130,114,0,118,125,131,120,119,124,111,129],
[115,117,116,132,0,133,120,136,121,110,117,132],
[112,136,102,125,117,0,110,111,115,114,110,112],
[117,130,112,119,130,140,0,115,129,129,132,138],
[124,121,123,130,114,139,135,0,139,125,123,135],
[123,121,118,131,129,135,121,111,0,134,136,139],
[123,131,127,126,140,136,121,125,116,0,102,133],
[128,137,140,139,133,140,118,127,114,148,0,122],
[115,139,111,121,118,138,112,115,111,117,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 163, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,137,124,131,130,128,132,122,122,118,139],
[107,0,120,110,110,115,122,122,120,105,104,108],
[113,130,0,123,120,120,122,131,111,118,97,112],
[126,140,127,0,126,133,138,123,112,108,117,118],
[119,140,130,124,0,128,132,125,128,122,110,124],
[120,135,130,117,122,0,122,122,115,122,107,114],
[122,128,128,112,118,128,0,110,112,123,109,113],
[118,128,119,127,125,128,140,0,119,134,114,123],
[128,130,139,138,122,135,138,131,0,121,117,119],
[128,145,132,142,128,128,127,116,129,0,119,121],
[132,146,153,133,140,143,141,136,133,131,0,125],
[111,142,138,132,126,136,137,127,131,129,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 164, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,135,134,129,131,127,141,125,135,133,133],
[121,0,127,136,141,126,122,124,130,139,125,123],
[115,123,0,129,133,121,115,127,132,127,124,116],
[116,114,121,0,122,124,112,131,127,142,129,118],
[121,109,117,128,0,113,120,125,115,130,117,111],
[119,124,129,126,137,0,123,147,133,140,132,123],
[123,128,135,138,130,127,0,136,123,137,126,127],
[109,126,123,119,125,103,114,0,124,130,122,116],
[125,120,118,123,135,117,127,126,0,132,135,121],
[115,111,123,108,120,110,113,120,118,0,123,118],
[117,125,126,121,133,118,124,128,115,127,0,118],
[117,127,134,132,139,127,123,134,129,132,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 165, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,114,133,115,126,117,142,125,134,116,123],
[120,0,110,140,104,127,125,134,116,121,118,133],
[136,140,0,157,132,128,119,141,125,125,112,130],
[117,110,93,0,102,105,115,125,109,121,116,99],
[135,146,118,148,0,152,139,140,135,149,133,136],
[124,123,122,145,98,0,120,135,117,134,128,116],
[133,125,131,135,111,130,0,124,124,137,130,129],
[108,116,109,125,110,115,126,0,130,128,101,110],
[125,134,125,141,115,133,126,120,0,128,103,110],
[116,129,125,129,101,116,113,122,122,0,116,122],
[134,132,138,134,117,122,120,149,147,134,0,124],
[127,117,120,151,114,134,121,140,140,128,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 166, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,135,141,139,169,124,136,141,131,135,113],
[118,0,106,131,125,153,149,114,108,121,117,118],
[115,144,0,137,127,159,139,112,133,122,145,116],
[109,119,113,0,138,152,141,122,117,121,133,119],
[111,125,123,112,0,169,119,133,134,127,148,115],
[81,97,91,98,81,0,110,91,102,99,109,91],
[126,101,111,109,131,140,0,122,117,122,122,116],
[114,136,138,128,117,159,128,0,138,125,138,130],
[109,142,117,133,116,148,133,112,0,128,115,113],
[119,129,128,129,123,151,128,125,122,0,126,105],
[115,133,105,117,102,141,128,112,135,124,0,103],
[137,132,134,131,135,159,134,120,137,145,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 167, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,116,136,95,145,101,97,136,113,124,107],
[132,0,145,147,135,141,140,150,139,167,127,115],
[134,105,0,133,127,147,115,114,123,133,120,96],
[114,103,117,0,126,141,107,112,131,122,126,112],
[155,115,123,124,0,138,116,103,121,138,128,131],
[105,109,103,109,112,0,95,98,106,135,110,110],
[149,110,135,143,134,155,0,138,150,142,159,126],
[153,100,136,138,147,152,112,0,125,129,138,116],
[114,111,127,119,129,144,100,125,0,117,118,94],
[137,83,117,128,112,115,108,121,133,0,117,107],
[126,123,130,124,122,140,91,112,132,133,0,125],
[143,135,154,138,119,140,124,134,156,143,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 168, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,124,147,121,142,118,134,139,140,137,131],
[128,0,114,122,119,133,132,137,144,141,143,132],
[126,136,0,140,129,139,124,134,147,147,152,137],
[103,128,110,0,116,139,116,125,124,135,133,127],
[129,131,121,134,0,144,127,130,130,145,135,142],
[108,117,111,111,106,0,110,127,125,133,122,118],
[132,118,126,134,123,140,0,136,147,142,136,143],
[116,113,116,125,120,123,114,0,130,129,136,129],
[111,106,103,126,120,125,103,120,0,131,137,123],
[110,109,103,115,105,117,108,121,119,0,122,113],
[113,107,98,117,115,128,114,114,113,128,0,124],
[119,118,113,123,108,132,107,121,127,137,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 169, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,123,109,114,130,94,115,122,123,75,102],
[141,0,128,142,145,134,128,147,128,121,124,127],
[127,122,0,134,136,145,124,138,129,116,117,133],
[141,108,116,0,151,126,114,119,125,127,110,123],
[136,105,114,99,0,123,112,128,118,116,116,110],
[120,116,105,124,127,0,110,128,123,115,103,123],
[156,122,126,136,138,140,0,139,146,148,104,118],
[135,103,112,131,122,122,111,0,110,111,103,104],
[128,122,121,125,132,127,104,140,0,131,109,124],
[127,129,134,123,134,135,102,139,119,0,119,134],
[175,126,133,140,134,147,146,147,141,131,0,123],
[148,123,117,127,140,127,132,146,126,116,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 170, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,170,128,219,127,79,171,127,125,124,174,31],
[80,0,78,125,47,110,152,127,125,124,174,31],
[122,172,0,139,91,152,202,172,91,122,206,152],
[31,125,111,0,0,62,155,111,61,61,111,61],
[123,203,159,250,0,110,249,160,109,155,159,109],
[171,140,98,188,140,0,170,140,46,138,144,126],
[79,98,48,95,1,80,0,99,49,94,98,79],
[123,123,78,139,90,110,151,0,48,125,124,61],
[125,125,159,189,141,204,201,202,0,249,205,156],
[126,126,128,189,95,112,156,125,1,0,128,112],
[76,76,44,139,91,106,152,126,45,122,0,106],
[219,219,98,189,141,124,171,189,94,138,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 171, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,101,130,111,107,115,130,143,119,111,142],
[129,0,107,120,114,115,133,130,150,142,144,142],
[149,143,0,123,153,127,155,155,132,143,128,140],
[120,130,127,0,126,111,125,134,137,137,128,149],
[139,136,97,124,0,140,135,124,122,111,119,136],
[143,135,123,139,110,0,134,145,142,145,126,135],
[135,117,95,125,115,116,0,95,106,91,107,131],
[120,120,95,116,126,105,155,0,115,124,101,141],
[107,100,118,113,128,108,144,135,0,118,120,125],
[131,108,107,113,139,105,159,126,132,0,106,138],
[139,106,122,122,131,124,143,149,130,144,0,132],
[108,108,110,101,114,115,119,109,125,112,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 172, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,122,114,110,104,109,124,116,114,134,123],
[138,0,125,132,121,112,119,129,123,111,122,135],
[128,125,0,133,111,118,120,124,122,129,134,118],
[136,118,117,0,109,116,118,115,119,120,130,111],
[140,129,139,141,0,119,136,119,133,149,142,134],
[146,138,132,134,131,0,123,135,116,121,126,131],
[141,131,130,132,114,127,0,131,120,131,136,138],
[126,121,126,135,131,115,119,0,127,129,125,129],
[134,127,128,131,117,134,130,123,0,127,128,138],
[136,139,121,130,101,129,119,121,123,0,148,135],
[116,128,116,120,108,124,114,125,122,102,0,121],
[127,115,132,139,116,119,112,121,112,115,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 173, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,134,124,122,120,132,123,139,136,137,129],
[109,0,125,128,120,117,128,111,116,118,133,121],
[116,125,0,124,139,121,120,119,128,124,141,116],
[126,122,126,0,133,129,125,136,127,133,143,125],
[128,130,111,117,0,109,119,116,126,116,125,116],
[130,133,129,121,141,0,134,126,129,135,142,141],
[118,122,130,125,131,116,0,115,124,121,139,117],
[127,139,131,114,134,124,135,0,134,122,143,131],
[111,134,122,123,124,121,126,116,0,126,137,123],
[114,132,126,117,134,115,129,128,124,0,136,129],
[113,117,109,107,125,108,111,107,113,114,0,115],
[121,129,134,125,134,109,133,119,127,121,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 174, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,113,120,131,102,117,122,95,90,101,105],
[140,0,125,138,136,135,126,136,137,132,109,124],
[137,125,0,123,119,107,117,136,118,120,112,106],
[130,112,127,0,129,124,130,125,123,119,108,128],
[119,114,131,121,0,136,130,139,130,127,101,125],
[148,115,143,126,114,0,106,125,127,133,109,115],
[133,124,133,120,120,144,0,105,138,127,102,110],
[128,114,114,125,111,125,145,0,118,125,98,124],
[155,113,132,127,120,123,112,132,0,119,133,117],
[160,118,130,131,123,117,123,125,131,0,116,121],
[149,141,138,142,149,141,148,152,117,134,0,144],
[145,126,144,122,125,135,140,126,133,129,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 175, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,135,104,146,128,107,114,110,106,126,130],
[136,0,145,124,148,141,128,140,151,129,122,121],
[115,105,0,117,84,92,125,109,125,95,92,106],
[146,126,133,0,102,100,123,125,135,89,111,139],
[104,102,166,148,0,134,127,144,145,114,112,120],
[122,109,158,150,116,0,157,124,122,126,125,158],
[143,122,125,127,123,93,0,127,121,83,97,138],
[136,110,141,125,106,126,123,0,137,120,105,119],
[140,99,125,115,105,128,129,113,0,74,118,108],
[144,121,155,161,136,124,167,130,176,0,141,163],
[124,128,158,139,138,125,153,145,132,109,0,144],
[120,129,144,111,130,92,112,131,142,87,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 176, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,119,133,144,125,143,117,127,125,123,111],
[114,0,116,125,126,116,123,112,117,125,131,109],
[131,134,0,142,141,110,146,128,132,142,136,127],
[117,125,108,0,125,118,133,126,109,121,132,100],
[106,124,109,125,0,107,132,107,118,118,133,114],
[125,134,140,132,143,0,149,120,130,136,156,112],
[107,127,104,117,118,101,0,104,119,120,130,101],
[133,138,122,124,143,130,146,0,128,127,140,128],
[123,133,118,141,132,120,131,122,0,126,129,115],
[125,125,108,129,132,114,130,123,124,0,131,104],
[127,119,114,118,117,94,120,110,121,119,0,100],
[139,141,123,150,136,138,149,122,135,146,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 177, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,151,118,134,147,122,141,133,128,112,131],
[147,0,147,137,131,130,144,139,141,136,124,139],
[99,103,0,101,105,126,117,125,113,131,103,142],
[132,113,149,0,131,137,127,125,137,140,126,147],
[116,119,145,119,0,128,124,114,129,134,134,164],
[103,120,124,113,122,0,129,104,128,125,111,120],
[128,106,133,123,126,121,0,101,130,128,107,144],
[109,111,125,125,136,146,149,0,139,147,122,143],
[117,109,137,113,121,122,120,111,0,142,108,124],
[122,114,119,110,116,125,122,103,108,0,107,124],
[138,126,147,124,116,139,143,128,142,143,0,128],
[119,111,108,103,86,130,106,107,126,126,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 178, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,107,109,129,114,113,127,111,115,109,127],
[129,0,112,110,130,113,127,136,112,102,101,127],
[143,138,0,115,146,126,112,129,131,111,111,132],
[141,140,135,0,142,122,133,131,114,114,118,132],
[121,120,104,108,0,119,119,119,120,108,97,111],
[136,137,124,128,131,0,135,131,125,116,128,125],
[137,123,138,117,131,115,0,130,102,116,121,141],
[123,114,121,119,131,119,120,0,109,112,109,118],
[139,138,119,136,130,125,148,141,0,122,126,131],
[135,148,139,136,142,134,134,138,128,0,115,137],
[141,149,139,132,153,122,129,141,124,135,0,140],
[123,123,118,118,139,125,109,132,119,113,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 179, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,143,131,131,136,135,124,139,132,131,127],
[101,0,117,112,99,107,102,108,116,104,108,113],
[107,133,0,126,120,120,115,115,120,117,124,127],
[119,138,124,0,127,123,126,121,111,122,125,126],
[119,151,130,123,0,130,128,111,113,114,124,129],
[114,143,130,127,120,0,125,114,130,116,129,123],
[115,148,135,124,122,125,0,123,125,124,131,126],
[126,142,135,129,139,136,127,0,129,131,138,119],
[111,134,130,139,137,120,125,121,0,127,138,132],
[118,146,133,128,136,134,126,119,123,0,138,141],
[119,142,126,125,126,121,119,112,112,112,0,133],
[123,137,123,124,121,127,124,131,118,109,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 180, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,138,142,122,127,127,133,120,129,128,136],
[113,0,104,121,104,91,118,104,111,111,111,120],
[112,146,0,127,123,120,139,120,113,131,119,139],
[108,129,123,0,114,108,121,106,105,118,117,138],
[128,146,127,136,0,115,132,115,122,128,137,137],
[123,159,130,142,135,0,143,123,122,125,139,138],
[123,132,111,129,118,107,0,114,112,112,115,134],
[117,146,130,144,135,127,136,0,111,130,125,146],
[130,139,137,145,128,128,138,139,0,123,128,146],
[121,139,119,132,122,125,138,120,127,0,126,137],
[122,139,131,133,113,111,135,125,122,124,0,126],
[114,130,111,112,113,112,116,104,104,113,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 181, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,138,138,133,135,129,124,131,144,122,143],
[137,0,123,120,128,136,132,127,136,140,138,143],
[112,127,0,112,110,129,126,126,119,126,127,136],
[112,130,138,0,127,131,115,125,126,125,121,144],
[117,122,140,123,0,129,122,128,130,128,136,127],
[115,114,121,119,121,0,124,107,111,124,120,135],
[121,118,124,135,128,126,0,129,134,128,127,134],
[126,123,124,125,122,143,121,0,120,138,120,149],
[119,114,131,124,120,139,116,130,0,127,113,146],
[106,110,124,125,122,126,122,112,123,0,119,121],
[128,112,123,129,114,130,123,130,137,131,0,136],
[107,107,114,106,123,115,116,101,104,129,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 182, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,132,142,98,115,121,118,116,110,104,124],
[127,0,133,117,90,120,111,128,131,101,121,116],
[118,117,0,140,115,130,113,123,123,118,105,121],
[108,133,110,0,98,127,116,129,110,110,103,99],
[152,160,135,152,0,148,146,149,143,120,135,143],
[135,130,120,123,102,0,118,138,134,106,103,112],
[129,139,137,134,104,132,0,142,134,123,127,118],
[132,122,127,121,101,112,108,0,123,103,123,112],
[134,119,127,140,107,116,116,127,0,123,107,114],
[140,149,132,140,130,144,127,147,127,0,127,117],
[146,129,145,147,115,147,123,127,143,123,0,123],
[126,134,129,151,107,138,132,138,136,133,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 183, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,149,138,129,112,151,118,143,137,123,157],
[124,0,165,151,112,113,113,128,94,186,105,193],
[101,85,0,136,134,85,128,151,134,109,100,130],
[112,99,114,0,97,57,57,80,102,103,74,105],
[121,138,116,153,0,78,78,119,84,131,64,87],
[138,137,165,193,172,0,150,104,131,180,128,193],
[99,137,122,193,172,100,0,117,79,180,127,175],
[132,122,99,170,131,146,133,0,127,126,124,127],
[107,156,116,148,166,119,171,123,0,160,145,181],
[113,64,141,147,119,70,70,124,90,0,76,108],
[127,145,150,176,186,122,123,126,105,174,0,169],
[93,57,120,145,163,57,75,123,69,142,81,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 184, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,108,128,136,115,123,114,126,119,110,118],
[136,0,114,136,124,117,124,132,124,122,104,121],
[142,136,0,139,135,116,131,128,124,134,132,138],
[122,114,111,0,123,98,111,118,100,111,98,113],
[114,126,115,127,0,116,115,116,113,119,109,114],
[135,133,134,152,134,0,119,116,121,134,126,134],
[127,126,119,139,135,131,0,128,122,130,131,133],
[136,118,122,132,134,134,122,0,135,131,126,123],
[124,126,126,150,137,129,128,115,0,122,132,127],
[131,128,116,139,131,116,120,119,128,0,123,124],
[140,146,118,152,141,124,119,124,118,127,0,132],
[132,129,112,137,136,116,117,127,123,126,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 185, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,135,141,161,154,84,166,131,171,139,141],
[117,0,158,122,129,131,156,137,105,168,127,128],
[115,92,0,110,124,116,101,133,118,126,115,129],
[109,128,140,0,131,169,113,136,134,146,140,122],
[89,121,126,119,0,91,95,127,147,156,146,93],
[96,119,134,81,159,0,89,113,121,163,124,131],
[166,94,149,137,155,161,0,145,144,170,118,133],
[84,113,117,114,123,137,105,0,127,131,142,121],
[119,145,132,116,103,129,106,123,0,145,103,94],
[79,82,124,104,94,87,80,119,105,0,119,106],
[111,123,135,110,104,126,132,108,147,131,0,124],
[109,122,121,128,157,119,117,129,156,144,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 186, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,138,103,109,107,111,114,112,121,125,120],
[126,0,124,126,105,129,121,117,125,113,119,122],
[112,126,0,98,95,118,100,105,110,119,120,108],
[147,124,152,0,134,142,136,123,135,130,145,128],
[141,145,155,116,0,130,131,136,144,124,137,121],
[143,121,132,108,120,0,120,125,134,136,130,124],
[139,129,150,114,119,130,0,118,132,115,128,121],
[136,133,145,127,114,125,132,0,138,135,136,136],
[138,125,140,115,106,116,118,112,0,116,122,129],
[129,137,131,120,126,114,135,115,134,0,123,127],
[125,131,130,105,113,120,122,114,128,127,0,121],
[130,128,142,122,129,126,129,114,121,123,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 187, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,175,105,149,140,117,175,205,155,151,86],
[114,0,133,96,126,120,92,175,177,183,148,99],
[75,117,0,70,130,63,50,152,85,119,107,66],
[145,154,180,0,104,107,135,196,139,151,151,91],
[101,124,120,146,0,91,74,136,171,150,172,90],
[110,130,187,143,159,0,115,151,191,140,181,147],
[133,158,200,115,176,135,0,218,197,198,168,101],
[75,75,98,54,114,99,32,0,130,106,128,63],
[45,73,165,111,79,59,53,120,0,159,134,34],
[95,67,131,99,100,110,52,144,91,0,135,73],
[99,102,143,99,78,69,82,122,116,115,0,35],
[164,151,184,159,160,103,149,187,216,177,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 188, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,113,119,125,145,135,116,129,109,118,127],
[138,0,122,133,123,142,151,133,130,134,131,139],
[137,128,0,131,110,145,128,123,140,112,123,126],
[131,117,119,0,121,136,129,120,113,118,130,129],
[125,127,140,129,0,143,138,118,140,127,120,144],
[105,108,105,114,107,0,110,102,102,117,103,112],
[115,99,122,121,112,140,0,120,118,117,103,117],
[134,117,127,130,132,148,130,0,135,122,130,133],
[121,120,110,137,110,148,132,115,0,115,123,130],
[141,116,138,132,123,133,133,128,135,0,128,115],
[132,119,127,120,130,147,147,120,127,122,0,126],
[123,111,124,121,106,138,133,117,120,135,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 189, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,110,115,122,123,123,111,109,116,116,132],
[152,0,129,132,136,136,133,149,120,138,141,138],
[140,121,0,125,125,129,113,136,120,131,128,130],
[135,118,125,0,123,118,124,113,117,127,119,120],
[128,114,125,127,0,127,130,131,119,116,125,122],
[127,114,121,132,123,0,116,120,114,127,125,121],
[127,117,137,126,120,134,0,128,124,127,128,133],
[139,101,114,137,119,130,122,0,134,136,129,126],
[141,130,130,133,131,136,126,116,0,134,130,139],
[134,112,119,123,134,123,123,114,116,0,126,129],
[134,109,122,131,125,125,122,121,120,124,0,129],
[118,112,120,130,128,129,117,124,111,121,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 190, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,137,138,133,129,133,123,127,130,130,132],
[118,0,133,123,126,120,127,101,120,115,137,127],
[113,117,0,116,110,123,121,112,113,105,120,99],
[112,127,134,0,121,144,129,112,123,118,124,112],
[117,124,140,129,0,143,125,125,120,131,126,126],
[121,130,127,106,107,0,116,116,112,118,117,122],
[117,123,129,121,125,134,0,113,121,121,126,109],
[127,149,138,138,125,134,137,0,121,133,135,138],
[123,130,137,127,130,138,129,129,0,134,122,118],
[120,135,145,132,119,132,129,117,116,0,123,111],
[120,113,130,126,124,133,124,115,128,127,0,121],
[118,123,151,138,124,128,141,112,132,139,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 191, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,153,146,153,132,151,120,144,174,118,141],
[116,0,109,135,138,101,130,123,116,141,111,143],
[97,141,0,139,111,112,136,136,123,145,133,125],
[104,115,111,0,126,111,163,110,124,123,107,129],
[97,112,139,124,0,117,118,126,122,112,115,138],
[118,149,138,139,133,0,156,119,128,154,137,149],
[99,120,114,87,132,94,0,126,111,136,107,109],
[130,127,114,140,124,131,124,0,133,133,102,108],
[106,134,127,126,128,122,139,117,0,138,128,126],
[76,109,105,127,138,96,114,117,112,0,120,125],
[132,139,117,143,135,113,143,148,122,130,0,138],
[109,107,125,121,112,101,141,142,124,125,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 192, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,145,111,124,107,143,101,97,98,146,160],
[105,0,145,134,93,77,172,149,148,122,136,137],
[105,105,0,133,140,98,137,83,93,99,160,147],
[139,116,117,0,108,101,168,114,120,63,132,156],
[126,157,110,142,0,106,186,119,136,121,134,164],
[143,173,152,149,144,0,196,110,136,116,161,209],
[107,78,113,82,64,54,0,114,88,58,70,87],
[149,101,167,136,131,140,136,0,108,132,141,147],
[153,102,157,130,114,114,162,142,0,118,178,148],
[152,128,151,187,129,134,192,118,132,0,153,162],
[104,114,90,118,116,89,180,109,72,97,0,134],
[90,113,103,94,86,41,163,103,102,88,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 193, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,120,144,98,131,139,135,136,105,127,127],
[114,0,126,131,110,124,157,107,122,115,119,139],
[130,124,0,139,125,144,154,152,140,124,123,137],
[106,119,111,0,101,131,147,116,119,118,107,129],
[152,140,125,149,0,134,147,148,128,136,139,146],
[119,126,106,119,116,0,149,131,137,106,123,134],
[111,93,96,103,103,101,0,111,135,72,105,103],
[115,143,98,134,102,119,139,0,120,118,121,136],
[114,128,110,131,122,113,115,130,0,109,122,127],
[145,135,126,132,114,144,178,132,141,0,117,147],
[123,131,127,143,111,127,145,129,128,133,0,134],
[123,111,113,121,104,116,147,114,123,103,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 194, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,130,129,114,120,133,130,130,118,125,139],
[124,0,119,121,113,115,128,126,137,130,120,140],
[120,131,0,129,118,129,140,142,129,133,128,132],
[121,129,121,0,126,128,129,137,137,129,126,135],
[136,137,132,124,0,115,143,141,128,123,129,140],
[130,135,121,122,135,0,143,136,135,129,122,137],
[117,122,110,121,107,107,0,137,114,119,117,125],
[120,124,108,113,109,114,113,0,120,125,122,127],
[120,113,121,113,122,115,136,130,0,121,126,120],
[132,120,117,121,127,121,131,125,129,0,114,128],
[125,130,122,124,121,128,133,128,124,136,0,135],
[111,110,118,115,110,113,125,123,130,122,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 195, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,100,116,99,122,72,128,127,112,115,89],
[200,0,103,174,150,170,134,139,145,139,170,179],
[150,147,0,156,110,190,102,159,170,141,148,171],
[134,76,94,0,86,139,75,128,89,128,94,94],
[151,100,140,164,0,142,115,124,124,114,122,104],
[128,80,60,111,108,0,65,102,92,125,91,87],
[178,116,148,175,135,185,0,142,174,188,160,141],
[122,111,91,122,126,148,108,0,134,117,112,120],
[123,105,80,161,126,158,76,116,0,129,138,140],
[138,111,109,122,136,125,62,133,121,0,132,92],
[135,80,102,156,128,159,90,138,112,118,0,114],
[161,71,79,156,146,163,109,130,110,158,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 196, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,132,130,124,129,131,139,153,120,132,131],
[125,0,119,126,113,124,133,123,144,118,138,120],
[118,131,0,131,121,125,130,123,144,122,130,131],
[120,124,119,0,121,123,131,126,147,123,129,123],
[126,137,129,129,0,133,127,136,139,125,136,127],
[121,126,125,127,117,0,125,132,149,122,135,127],
[119,117,120,119,123,125,0,122,138,117,135,127],
[111,127,127,124,114,118,128,0,132,108,129,121],
[97,106,106,103,111,101,112,118,0,105,122,114],
[130,132,128,127,125,128,133,142,145,0,136,122],
[118,112,120,121,114,115,115,121,128,114,0,123],
[119,130,119,127,123,123,123,129,136,128,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 197, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,103,120,108,130,131,131,128,123,132,116],
[119,0,119,124,104,130,122,123,133,120,124,135],
[147,131,0,136,114,146,141,148,148,136,143,132],
[130,126,114,0,116,141,106,114,138,126,132,122],
[142,146,136,134,0,121,119,137,131,130,154,144],
[120,120,104,109,129,0,134,128,127,120,132,118],
[119,128,109,144,131,116,0,135,128,132,151,120],
[119,127,102,136,113,122,115,0,127,123,125,122],
[122,117,102,112,119,123,122,123,0,123,117,126],
[127,130,114,124,120,130,118,127,127,0,140,107],
[118,126,107,118,96,118,99,125,133,110,0,108],
[134,115,118,128,106,132,130,128,124,143,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 198, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,131,138,111,112,123,140,131,179,115,146],
[119,0,103,126,112,115,140,147,152,164,124,150],
[119,147,0,134,122,97,133,143,114,153,127,153],
[112,124,116,0,142,118,131,122,132,164,119,162],
[139,138,128,108,0,110,130,131,138,139,122,163],
[138,135,153,132,140,0,153,150,152,171,118,178],
[127,110,117,119,120,97,0,131,130,157,123,161],
[110,103,107,128,119,100,119,0,105,133,103,141],
[119,98,136,118,112,98,120,145,0,134,122,138],
[71,86,97,86,111,79,93,117,116,0,110,137],
[135,126,123,131,128,132,127,147,128,140,0,168],
[104,100,97,88,87,72,89,109,112,113,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 199, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,125,125,145,129,134,130,116,134,126,110],
[141,0,131,135,142,125,135,118,108,138,116,122],
[125,119,0,127,132,112,135,118,113,129,107,117],
[125,115,123,0,147,117,125,121,129,134,127,130],
[105,108,118,103,0,100,123,115,105,128,114,104],
[121,125,138,133,150,0,150,117,123,147,143,120],
[116,115,115,125,127,100,0,110,116,136,110,110],
[120,132,132,129,135,133,140,0,123,149,119,123],
[134,142,137,121,145,127,134,127,0,141,137,120],
[116,112,121,116,122,103,114,101,109,0,108,102],
[124,134,143,123,136,107,140,131,113,142,0,121],
[140,128,133,120,146,130,140,127,130,148,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 250, 200, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/ejor/results/meprcw/meprcw_12_250.csv", index=False, header=False)