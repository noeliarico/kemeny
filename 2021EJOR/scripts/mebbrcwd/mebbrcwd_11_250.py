
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,131,121,130,129,105,117,122,111,121,122],
[119,0,115,135,125,123,125,134,112,124,125],
[129,135,0,138,120,120,122,112,110,131,110],
[120,115,112,0,126,121,105,135,105,116,119],
[121,125,130,124,0,106,115,130,105,123,119],
[145,127,130,129,144,0,121,140,130,138,128],
[133,125,128,145,135,129,0,136,122,131,138],
[128,116,138,115,120,110,114,0,105,131,126],
[139,138,140,145,145,120,128,145,0,150,126],
[129,126,119,134,127,112,119,119,100,0,132],
[128,125,140,131,131,122,112,124,124,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,135,130,132,119,118,128,130,126,127],
[118,0,130,115,117,115,123,122,129,113,114],
[115,120,0,109,112,110,109,109,125,112,115],
[120,135,141,0,130,128,128,129,141,136,134],
[118,133,138,120,0,113,124,130,125,131,119],
[131,135,140,122,137,0,132,132,137,135,129],
[132,127,141,122,126,118,0,125,130,127,122],
[122,128,141,121,120,118,125,0,135,119,123],
[120,121,125,109,125,113,120,115,0,118,117],
[124,137,138,114,119,115,123,131,132,0,124],
[123,136,135,116,131,121,128,127,133,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,124,134,129,136,124,126,130,134,125],
[114,0,116,108,120,122,119,111,120,126,98],
[126,134,0,127,119,127,138,117,114,135,118],
[116,142,123,0,139,134,126,125,134,133,114],
[121,130,131,111,0,138,136,117,116,133,108],
[114,128,123,116,112,0,119,129,129,129,125],
[126,131,112,124,114,131,0,126,118,125,117],
[124,139,133,125,133,121,124,0,131,125,114],
[120,130,136,116,134,121,132,119,0,132,121],
[116,124,115,117,117,121,125,125,118,0,108],
[125,152,132,136,142,125,133,136,129,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,120,118,119,116,112,119,118,123,104],
[135,0,133,130,136,131,128,132,124,124,120],
[130,117,0,123,126,125,128,140,126,117,129],
[132,120,127,0,128,126,121,124,114,117,118],
[131,114,124,122,0,125,117,110,116,116,116],
[134,119,125,124,125,0,126,128,127,115,120],
[138,122,122,129,133,124,0,130,127,126,120],
[131,118,110,126,140,122,120,0,122,128,119],
[132,126,124,136,134,123,123,128,0,121,122],
[127,126,133,133,134,135,124,122,129,0,125],
[146,130,121,132,134,130,130,131,128,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,111,115,132,117,126,130,116,109,120],
[115,0,110,128,120,126,113,128,122,113,120],
[139,140,0,133,137,126,120,137,119,114,128],
[135,122,117,0,124,118,121,135,122,119,116],
[118,130,113,126,0,119,110,126,123,117,125],
[133,124,124,132,131,0,114,141,117,107,126],
[124,137,130,129,140,136,0,134,144,128,123],
[120,122,113,115,124,109,116,0,124,113,125],
[134,128,131,128,127,133,106,126,0,116,120],
[141,137,136,131,133,143,122,137,134,0,135],
[130,130,122,134,125,124,127,125,130,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,128,181,128,139,136,118,130,131,107],
[106,0,155,157,153,152,133,125,130,143,132],
[122,95,0,149,117,126,127,109,136,105,108],
[69,93,101,0,101,99,120,96,113,92,77],
[122,97,133,149,0,135,121,132,139,148,100],
[111,98,124,151,115,0,106,109,114,99,124],
[114,117,123,130,129,144,0,115,124,99,112],
[132,125,141,154,118,141,135,0,129,135,120],
[120,120,114,137,111,136,126,121,0,108,113],
[119,107,145,158,102,151,151,115,142,0,116],
[143,118,142,173,150,126,138,130,137,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,148,130,123,151,134,150,121,104,121],
[126,0,159,127,115,135,146,122,100,105,125],
[102,91,0,98,95,124,124,108,110,85,97],
[120,123,152,0,109,137,130,147,92,94,133],
[127,135,155,141,0,117,139,154,95,142,114],
[99,115,126,113,133,0,139,131,100,116,118],
[116,104,126,120,111,111,0,127,99,93,110],
[100,128,142,103,96,119,123,0,63,116,115],
[129,150,140,158,155,150,151,187,0,118,142],
[146,145,165,156,108,134,157,134,132,0,116],
[129,125,153,117,136,132,140,135,108,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,131,121,116,121,125,132,122,111,120],
[113,0,120,110,106,126,105,106,117,106,113],
[119,130,0,127,115,139,111,125,122,124,132],
[129,140,123,0,127,127,122,109,124,119,132],
[134,144,135,123,0,146,115,136,136,131,144],
[129,124,111,123,104,0,112,123,117,114,118],
[125,145,139,128,135,138,0,123,134,124,133],
[118,144,125,141,114,127,127,0,128,132,140],
[128,133,128,126,114,133,116,122,0,124,132],
[139,144,126,131,119,136,126,118,126,0,144],
[130,137,118,118,106,132,117,110,118,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,134,124,117,130,141,133,128,127,129],
[129,0,127,134,123,113,129,113,103,115,136],
[116,123,0,128,122,126,120,123,115,113,131],
[126,116,122,0,106,129,131,126,109,105,126],
[133,127,128,144,0,139,144,130,133,123,117],
[120,137,124,121,111,0,133,134,133,133,127],
[109,121,130,119,106,117,0,123,123,101,119],
[117,137,127,124,120,116,127,0,108,116,105],
[122,147,135,141,117,117,127,142,0,138,142],
[123,135,137,145,127,117,149,134,112,0,122],
[121,114,119,124,133,123,131,145,108,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,166,135,126,145,129,172,143,120,115,105],
[84,0,108,150,147,95,139,155,123,112,100],
[115,142,0,163,148,134,193,118,131,116,124],
[124,100,87,0,133,73,120,134,104,89,73],
[105,103,102,117,0,123,148,102,107,96,92],
[121,155,116,177,127,0,121,129,109,108,107],
[78,111,57,130,102,129,0,117,84,97,88],
[107,95,132,116,148,121,133,0,123,115,102],
[130,127,119,146,143,141,166,127,0,132,103],
[135,138,134,161,154,142,153,135,118,0,126],
[145,150,126,177,158,143,162,148,147,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,111,151,128,109,126,110,148,120,130],
[132,0,95,139,123,125,123,107,130,127,105],
[139,155,0,160,158,119,152,122,164,144,126],
[99,111,90,0,124,103,110,93,128,109,98],
[122,127,92,126,0,108,102,100,119,122,114],
[141,125,131,147,142,0,122,113,144,142,137],
[124,127,98,140,148,128,0,106,140,113,123],
[140,143,128,157,150,137,144,0,149,140,125],
[102,120,86,122,131,106,110,101,0,113,107],
[130,123,106,141,128,108,137,110,137,0,106],
[120,145,124,152,136,113,127,125,143,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,91,151,137,109,112,153,101,105,93],
[113,0,90,103,114,97,125,99,99,93,100],
[159,160,0,130,142,134,148,151,104,107,123],
[99,147,120,0,124,107,145,143,88,120,116],
[113,136,108,126,0,114,131,92,87,109,142],
[141,153,116,143,136,0,159,116,146,138,117],
[138,125,102,105,119,91,0,144,77,90,154],
[97,151,99,107,158,134,106,0,110,92,140],
[149,151,146,162,163,104,173,140,0,148,181],
[145,157,143,130,141,112,160,158,102,0,147],
[157,150,127,134,108,133,96,110,69,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,113,123,107,98,128,117,116,131,110],
[125,0,127,135,106,131,133,122,138,131,140],
[137,123,0,130,112,120,133,105,138,137,124],
[127,115,120,0,99,108,125,106,119,107,108],
[143,144,138,151,0,115,132,143,136,139,148],
[152,119,130,142,135,0,132,124,136,135,126],
[122,117,117,125,118,118,0,95,124,118,119],
[133,128,145,144,107,126,155,0,128,135,134],
[134,112,112,131,114,114,126,122,0,122,121],
[119,119,113,143,111,115,132,115,128,0,121],
[140,110,126,142,102,124,131,116,129,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,168,105,146,166,132,197,124,125,154],
[21,0,74,54,94,166,86,196,94,54,77],
[82,176,0,72,125,183,135,229,124,72,115],
[145,196,178,0,147,166,159,174,143,119,83],
[104,156,125,103,0,166,145,207,127,105,83],
[84,84,67,84,84,0,136,182,83,84,71],
[118,164,115,91,105,114,0,177,104,108,134],
[53,54,21,76,43,68,73,0,41,54,53],
[126,156,126,107,123,167,146,209,0,127,105],
[125,196,178,131,145,166,142,196,123,0,105],
[96,173,135,167,167,179,116,197,145,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,123,131,123,115,122,132,118,123,112],
[126,0,121,131,128,119,126,134,126,121,124],
[127,129,0,128,124,125,105,131,126,112,118],
[119,119,122,0,105,113,108,132,118,110,117],
[127,122,126,145,0,115,111,123,128,113,124],
[135,131,125,137,135,0,120,149,131,118,134],
[128,124,145,142,139,130,0,134,125,128,129],
[118,116,119,118,127,101,116,0,113,114,118],
[132,124,124,132,122,119,125,137,0,114,124],
[127,129,138,140,137,132,122,136,136,0,125],
[138,126,132,133,126,116,121,132,126,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,122,112,116,122,142,115,112,119,129],
[132,0,131,126,120,121,135,129,119,128,117],
[128,119,0,108,118,109,133,129,115,114,119],
[138,124,142,0,128,130,144,139,128,122,130],
[134,130,132,122,0,128,133,119,126,129,120],
[128,129,141,120,122,0,133,120,119,114,120],
[108,115,117,106,117,117,0,109,107,112,103],
[135,121,121,111,131,130,141,0,124,117,128],
[138,131,135,122,124,131,143,126,0,126,120],
[131,122,136,128,121,136,138,133,124,0,131],
[121,133,131,120,130,130,147,122,130,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,104,115,95,95,100,104,119,108,103],
[140,0,128,120,114,115,111,120,112,126,126],
[146,122,0,118,124,122,106,123,112,126,113],
[135,130,132,0,104,125,114,124,129,131,130],
[155,136,126,146,0,124,122,128,122,133,143],
[155,135,128,125,126,0,127,124,126,121,122],
[150,139,144,136,128,123,0,138,129,126,121],
[146,130,127,126,122,126,112,0,123,120,124],
[131,138,138,121,128,124,121,127,0,131,123],
[142,124,124,119,117,129,124,130,119,0,118],
[147,124,137,120,107,128,129,126,127,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,114,131,121,112,112,111,104,106,116],
[141,0,131,145,118,128,127,120,115,136,132],
[136,119,0,138,125,137,123,122,119,141,132],
[119,105,112,0,118,108,104,105,107,117,120],
[129,132,125,132,0,105,116,106,122,120,129],
[138,122,113,142,145,0,122,118,136,126,121],
[138,123,127,146,134,128,0,127,122,130,135],
[139,130,128,145,144,132,123,0,128,131,146],
[146,135,131,143,128,114,128,122,0,133,132],
[144,114,109,133,130,124,120,119,117,0,123],
[134,118,118,130,121,129,115,104,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,126,118,118,118,118,112,130,134,136],
[113,0,124,104,114,118,115,114,118,123,119],
[124,126,0,114,117,124,114,132,128,132,121],
[132,146,136,0,126,130,135,121,126,141,143],
[132,136,133,124,0,119,120,132,127,133,138],
[132,132,126,120,131,0,112,120,123,125,132],
[132,135,136,115,130,138,0,130,136,143,128],
[138,136,118,129,118,130,120,0,126,130,129],
[120,132,122,124,123,127,114,124,0,122,136],
[116,127,118,109,117,125,107,120,128,0,131],
[114,131,129,107,112,118,122,121,114,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,127,137,125,115,114,123,119,114,114],
[144,0,138,139,141,122,128,132,134,132,136],
[123,112,0,134,127,105,124,121,120,121,116],
[113,111,116,0,120,104,105,116,108,120,108],
[125,109,123,130,0,113,109,120,123,118,116],
[135,128,145,146,137,0,121,132,129,129,128],
[136,122,126,145,141,129,0,132,133,129,132],
[127,118,129,134,130,118,118,0,123,122,132],
[131,116,130,142,127,121,117,127,0,125,124],
[136,118,129,130,132,121,121,128,125,0,121],
[136,114,134,142,134,122,118,118,126,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,159,92,122,153,120,111,135,150,119,115],
[91,0,75,85,133,101,100,86,105,97,80],
[158,175,0,160,137,133,101,130,176,154,148],
[128,165,90,0,171,115,116,120,139,127,116],
[97,117,113,79,0,101,107,110,104,114,85],
[130,149,117,135,149,0,126,120,136,140,117],
[139,150,149,134,143,124,0,140,165,143,122],
[115,164,120,130,140,130,110,0,152,141,145],
[100,145,74,111,146,114,85,98,0,100,104],
[131,153,96,123,136,110,107,109,150,0,118],
[135,170,102,134,165,133,128,105,146,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,121,135,100,105,117,105,104,88,89],
[128,0,110,123,99,100,80,96,108,106,113],
[129,140,0,119,114,114,132,116,98,96,106],
[115,127,131,0,100,120,103,91,86,88,102],
[150,151,136,150,0,161,124,126,121,111,109],
[145,150,136,130,89,0,108,119,117,112,123],
[133,170,118,147,126,142,0,124,123,135,130],
[145,154,134,159,124,131,126,0,117,116,114],
[146,142,152,164,129,133,127,133,0,118,113],
[162,144,154,162,139,138,115,134,132,0,138],
[161,137,144,148,141,127,120,136,137,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,145,133,136,147,134,117,134,134,137],
[116,0,128,114,118,124,128,116,114,121,124],
[105,122,0,109,131,135,121,129,125,121,125],
[117,136,141,0,137,140,135,121,127,106,140],
[114,132,119,113,0,143,112,115,111,122,123],
[103,126,115,110,107,0,115,110,115,112,111],
[116,122,129,115,138,135,0,130,121,111,125],
[133,134,121,129,135,140,120,0,117,122,122],
[116,136,125,123,139,135,129,133,0,120,133],
[116,129,129,144,128,138,139,128,130,0,131],
[113,126,125,110,127,139,125,128,117,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,140,134,135,151,114,157,139,144,118],
[141,0,117,116,137,131,126,140,138,128,124],
[110,133,0,121,125,139,102,123,120,116,134],
[116,134,129,0,131,148,112,158,139,122,134],
[115,113,125,119,0,130,127,154,129,146,131],
[99,119,111,102,120,0,104,143,128,108,116],
[136,124,148,138,123,146,0,145,158,138,129],
[93,110,127,92,96,107,105,0,112,95,111],
[111,112,130,111,121,122,92,138,0,116,107],
[106,122,134,128,104,142,112,155,134,0,120],
[132,126,116,116,119,134,121,139,143,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,127,125,137,108,137,134,118,117,115],
[137,0,109,128,131,100,119,127,128,118,114],
[123,141,0,137,124,125,132,106,123,92,108],
[125,122,113,0,130,117,134,122,133,92,118],
[113,119,126,120,0,109,148,114,129,98,112],
[142,150,125,133,141,0,137,133,121,112,126],
[113,131,118,116,102,113,0,109,111,112,123],
[116,123,144,128,136,117,141,0,130,126,126],
[132,122,127,117,121,129,139,120,0,114,116],
[133,132,158,158,152,138,138,124,136,0,129],
[135,136,142,132,138,124,127,124,134,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,130,116,120,130,120,136,136,111,127],
[138,0,130,123,126,137,136,134,143,124,132],
[120,120,0,127,119,129,127,119,136,116,136],
[134,127,123,0,118,131,119,119,139,122,118],
[130,124,131,132,0,142,125,135,142,128,133],
[120,113,121,119,108,0,119,127,129,112,125],
[130,114,123,131,125,131,0,124,143,114,122],
[114,116,131,131,115,123,126,0,140,117,126],
[114,107,114,111,108,121,107,110,0,109,111],
[139,126,134,128,122,138,136,133,141,0,144],
[123,118,114,132,117,125,128,124,139,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,131,144,112,114,125,130,121,132,108],
[121,0,134,136,143,131,119,133,105,151,102],
[119,116,0,126,133,121,108,130,117,132,99],
[106,114,124,0,108,103,117,124,104,119,87],
[138,107,117,142,0,126,126,132,107,137,103],
[136,119,129,147,124,0,117,137,113,140,121],
[125,131,142,133,124,133,0,138,113,132,125],
[120,117,120,126,118,113,112,0,109,131,110],
[129,145,133,146,143,137,137,141,0,147,124],
[118,99,118,131,113,110,118,119,103,0,95],
[142,148,151,163,147,129,125,140,126,155,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,126,124,109,121,115,116,123,121,130],
[145,0,139,132,140,124,142,133,146,151,146],
[124,111,0,118,118,118,113,121,129,137,128],
[126,118,132,0,125,133,134,116,140,125,137],
[141,110,132,125,0,124,127,134,119,136,148],
[129,126,132,117,126,0,128,124,129,137,133],
[135,108,137,116,123,122,0,128,122,130,141],
[134,117,129,134,116,126,122,0,132,133,128],
[127,104,121,110,131,121,128,118,0,123,127],
[129,99,113,125,114,113,120,117,127,0,138],
[120,104,122,113,102,117,109,122,123,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,120,106,118,110,126,126,92,123,119],
[124,0,123,112,131,114,131,122,111,126,133],
[130,127,0,128,150,133,141,145,125,158,138],
[144,138,122,0,142,110,137,134,126,140,145],
[132,119,100,108,0,114,143,127,122,119,130],
[140,136,117,140,136,0,146,126,125,138,153],
[124,119,109,113,107,104,0,122,119,125,133],
[124,128,105,116,123,124,128,0,110,133,137],
[158,139,125,124,128,125,131,140,0,144,133],
[127,124,92,110,131,112,125,117,106,0,124],
[131,117,112,105,120,97,117,113,117,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,145,200,153,123,112,128,157,121,107],
[114,0,153,195,128,123,122,154,152,145,121],
[105,97,0,131,92,111,123,131,155,113,118],
[50,55,119,0,77,94,83,129,95,79,92],
[97,122,158,173,0,112,140,155,147,121,129],
[127,127,139,156,138,0,132,156,164,141,112],
[138,128,127,167,110,118,0,160,148,119,135],
[122,96,119,121,95,94,90,0,121,133,127],
[93,98,95,155,103,86,102,129,0,102,98],
[129,105,137,171,129,109,131,117,148,0,100],
[143,129,132,158,121,138,115,123,152,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,184,190,77,140,127,170,116,123,124,136],
[66,0,133,97,96,105,74,116,122,106,100],
[60,117,0,75,141,124,63,101,115,65,86],
[173,153,175,0,119,100,149,134,135,102,173],
[110,154,109,131,0,91,120,147,145,131,148],
[123,145,126,150,159,0,147,122,179,96,158],
[80,176,187,101,130,103,0,103,121,70,147],
[134,134,149,116,103,128,147,0,178,97,156],
[127,128,135,115,105,71,129,72,0,98,152],
[126,144,185,148,119,154,180,153,152,0,187],
[114,150,164,77,102,92,103,94,98,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,119,119,127,127,121,141,115,129,111],
[137,0,119,134,130,130,119,142,114,145,130],
[131,131,0,124,122,123,123,138,115,139,114],
[131,116,126,0,133,126,118,131,114,143,115],
[123,120,128,117,0,117,117,138,116,122,101],
[123,120,127,124,133,0,109,142,119,138,131],
[129,131,127,132,133,141,0,155,131,134,125],
[109,108,112,119,112,108,95,0,117,124,103],
[135,136,135,136,134,131,119,133,0,136,112],
[121,105,111,107,128,112,116,126,114,0,108],
[139,120,136,135,149,119,125,147,138,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,122,127,122,99,134,119,118,131,129],
[137,0,142,139,141,133,139,130,134,148,121],
[128,108,0,110,97,101,111,126,118,112,120],
[123,111,140,0,130,116,119,138,120,154,140],
[128,109,153,120,0,133,126,139,120,142,140],
[151,117,149,134,117,0,141,140,136,153,133],
[116,111,139,131,124,109,0,131,128,125,133],
[131,120,124,112,111,110,119,0,117,112,98],
[132,116,132,130,130,114,122,133,0,137,127],
[119,102,138,96,108,97,125,138,113,0,101],
[121,129,130,110,110,117,117,152,123,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,149,126,116,111,153,141,147,130,134],
[126,0,143,114,151,136,125,137,126,140,110],
[101,107,0,116,99,100,116,116,100,133,105],
[124,136,134,0,122,109,108,129,121,113,125],
[134,99,151,128,0,126,124,126,144,139,125],
[139,114,150,141,124,0,123,137,151,134,123],
[97,125,134,142,126,127,0,146,135,155,125],
[109,113,134,121,124,113,104,0,121,104,121],
[103,124,150,129,106,99,115,129,0,125,127],
[120,110,117,137,111,116,95,146,125,0,123],
[116,140,145,125,125,127,125,129,123,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,104,143,116,105,98,121,120,131,133],
[123,0,108,135,133,107,121,115,122,116,109],
[146,142,0,138,133,115,132,133,126,143,132],
[107,115,112,0,136,106,115,122,111,129,124],
[134,117,117,114,0,101,87,114,124,121,113],
[145,143,135,144,149,0,139,131,125,132,137],
[152,129,118,135,163,111,0,132,143,138,139],
[129,135,117,128,136,119,118,0,123,154,118],
[130,128,124,139,126,125,107,127,0,132,119],
[119,134,107,121,129,118,112,96,118,0,104],
[117,141,118,126,137,113,111,132,131,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,132,157,139,118,123,128,131,142,135],
[116,0,122,144,95,106,135,93,107,100,122],
[118,128,0,175,110,113,108,125,133,126,145],
[93,106,75,0,72,124,106,88,76,89,114],
[111,155,140,178,0,134,144,136,127,134,127],
[132,144,137,126,116,0,152,137,117,138,155],
[127,115,142,144,106,98,0,127,134,138,123],
[122,157,125,162,114,113,123,0,121,149,160],
[119,143,117,174,123,133,116,129,0,112,152],
[108,150,124,161,116,112,112,101,138,0,124],
[115,128,105,136,123,95,127,90,98,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,111,106,116,97,87,101,105,85,109],
[144,0,108,115,117,100,93,87,126,100,147],
[139,142,0,121,135,135,135,131,138,132,129],
[144,135,129,0,135,116,122,134,116,121,154],
[134,133,115,115,0,125,113,123,109,118,136],
[153,150,115,134,125,0,134,124,113,103,136],
[163,157,115,128,137,116,0,152,138,116,147],
[149,163,119,116,127,126,98,0,117,115,137],
[145,124,112,134,141,137,112,133,0,124,132],
[165,150,118,129,132,147,134,135,126,0,149],
[141,103,121,96,114,114,103,113,118,101,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,118,136,144,119,113,107,163,134,111],
[134,0,107,133,147,115,117,126,148,133,118],
[132,143,0,135,139,111,90,118,141,134,124],
[114,117,115,0,141,104,91,97,142,127,135],
[106,103,111,109,0,95,82,78,119,124,98],
[131,135,139,146,155,0,103,127,157,132,136],
[137,133,160,159,168,147,0,124,148,146,148],
[143,124,132,153,172,123,126,0,161,133,126],
[87,102,109,108,131,93,102,89,0,128,99],
[116,117,116,123,126,118,104,117,122,0,109],
[139,132,126,115,152,114,102,124,151,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,82,152,111,86,120,146,125,143,151,85],
[168,0,148,141,146,69,170,141,106,168,60],
[98,102,0,116,130,162,64,75,119,106,100],
[139,109,134,0,137,97,91,88,155,163,88],
[164,104,120,113,0,93,142,140,140,140,56],
[130,181,88,153,157,0,110,106,124,157,63],
[104,80,186,159,108,140,0,144,162,107,128],
[125,109,175,162,110,144,106,0,151,139,135],
[107,144,131,95,110,126,88,99,0,150,94],
[99,82,144,87,110,93,143,111,100,0,84],
[165,190,150,162,194,187,122,115,156,166,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,144,116,137,128,78,117,103,146,134],
[123,0,158,138,105,140,132,111,98,138,106],
[106,92,0,107,106,96,82,87,60,125,119],
[134,112,143,0,156,108,98,116,131,152,128],
[113,145,144,94,0,141,103,89,118,156,131],
[122,110,154,142,109,0,110,105,72,144,121],
[172,118,168,152,147,140,0,124,82,163,146],
[133,139,163,134,161,145,126,0,121,172,134],
[147,152,190,119,132,178,168,129,0,186,141],
[104,112,125,98,94,106,87,78,64,0,107],
[116,144,131,122,119,129,104,116,109,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,124,150,114,124,142,134,152,121,129],
[125,0,127,134,127,132,140,110,131,128,130],
[126,123,0,142,98,109,119,102,103,89,99],
[100,116,108,0,96,107,104,98,120,89,129],
[136,123,152,154,0,121,126,132,142,120,146],
[126,118,141,143,129,0,144,108,133,110,145],
[108,110,131,146,124,106,0,94,114,112,146],
[116,140,148,152,118,142,156,0,150,117,148],
[98,119,147,130,108,117,136,100,0,118,139],
[129,122,161,161,130,140,138,133,132,0,138],
[121,120,151,121,104,105,104,102,111,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,136,132,111,131,140,125,153,138,138],
[116,0,126,112,106,130,113,102,116,116,113],
[114,124,0,107,101,103,129,110,130,110,123],
[118,138,143,0,113,120,138,131,134,111,147],
[139,144,149,137,0,129,150,123,130,126,133],
[119,120,147,130,121,0,130,136,130,109,124],
[110,137,121,112,100,120,0,114,132,110,124],
[125,148,140,119,127,114,136,0,135,116,111],
[97,134,120,116,120,120,118,115,0,103,108],
[112,134,140,139,124,141,140,134,147,0,128],
[112,137,127,103,117,126,126,139,142,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,131,122,125,120,129,123,122,130,115],
[122,0,113,112,115,111,127,124,130,119,115],
[119,137,0,121,127,124,129,122,124,134,128],
[128,138,129,0,128,124,139,133,131,128,126],
[125,135,123,122,0,111,141,126,126,129,126],
[130,139,126,126,139,0,144,131,125,132,124],
[121,123,121,111,109,106,0,111,114,117,118],
[127,126,128,117,124,119,139,0,122,133,124],
[128,120,126,119,124,125,136,128,0,135,124],
[120,131,116,122,121,118,133,117,115,0,114],
[135,135,122,124,124,126,132,126,126,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,116,123,121,121,136,129,118,141,128],
[130,0,125,136,134,145,141,139,131,144,130],
[134,125,0,124,141,139,133,135,129,146,126],
[127,114,126,0,125,136,143,129,133,140,124],
[129,116,109,125,0,130,137,127,126,139,132],
[129,105,111,114,120,0,125,123,111,129,119],
[114,109,117,107,113,125,0,111,119,132,120],
[121,111,115,121,123,127,139,0,126,129,125],
[132,119,121,117,124,139,131,124,0,140,112],
[109,106,104,110,111,121,118,121,110,0,110],
[122,120,124,126,118,131,130,125,138,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,124,122,125,132,134,123,108,139,131],
[123,0,126,122,118,120,128,117,123,125,142],
[126,124,0,127,123,127,137,126,124,119,141],
[128,128,123,0,121,129,134,123,119,125,134],
[125,132,127,129,0,130,133,132,136,128,146],
[118,130,123,121,120,0,129,125,120,120,132],
[116,122,113,116,117,121,0,120,113,127,127],
[127,133,124,127,118,125,130,0,119,128,134],
[142,127,126,131,114,130,137,131,0,130,141],
[111,125,131,125,122,130,123,122,120,0,122],
[119,108,109,116,104,118,123,116,109,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,129,125,118,114,129,124,120,123,126],
[135,0,120,131,135,129,129,128,115,132,127],
[121,130,0,130,129,131,128,119,117,128,116],
[125,119,120,0,118,117,126,123,113,122,120],
[132,115,121,132,0,123,132,121,120,134,121],
[136,121,119,133,127,0,129,120,116,123,124],
[121,121,122,124,118,121,0,121,115,132,124],
[126,122,131,127,129,130,129,0,122,131,131],
[130,135,133,137,130,134,135,128,0,132,119],
[127,118,122,128,116,127,118,119,118,0,116],
[124,123,134,130,129,126,126,119,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,125,139,113,97,122,115,133,111,121],
[136,0,122,105,107,105,107,116,134,116,117],
[125,128,0,131,127,114,102,117,143,135,126],
[111,145,119,0,129,111,105,129,140,128,118],
[137,143,123,121,0,122,130,138,149,131,123],
[153,145,136,139,128,0,115,155,149,142,137],
[128,143,148,145,120,135,0,158,157,139,145],
[135,134,133,121,112,95,92,0,134,106,117],
[117,116,107,110,101,101,93,116,0,103,109],
[139,134,115,122,119,108,111,144,147,0,132],
[129,133,124,132,127,113,105,133,141,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,124,120,119,105,104,121,113,121,146],
[142,0,146,120,129,117,129,142,110,125,140],
[126,104,0,95,90,81,107,109,99,130,122],
[130,130,155,0,115,123,121,126,111,139,157],
[131,121,160,135,0,136,137,104,140,135,150],
[145,133,169,127,114,0,136,131,120,150,148],
[146,121,143,129,113,114,0,117,132,148,138],
[129,108,141,124,146,119,133,0,112,142,148],
[137,140,151,139,110,130,118,138,0,146,152],
[129,125,120,111,115,100,102,108,104,0,152],
[104,110,128,93,100,102,112,102,98,98,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,114,128,128,115,105,124,117,119,109],
[147,0,126,127,131,132,124,132,142,129,125],
[136,124,0,117,123,116,96,127,122,125,112],
[122,123,133,0,121,121,111,123,131,121,123],
[122,119,127,129,0,121,108,130,127,129,113],
[135,118,134,129,129,0,118,133,130,131,116],
[145,126,154,139,142,132,0,142,141,144,122],
[126,118,123,127,120,117,108,0,115,116,124],
[133,108,128,119,123,120,109,135,0,133,112],
[131,121,125,129,121,119,106,134,117,0,125],
[141,125,138,127,137,134,128,126,138,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,106,102,106,107,112,118,113,107,106],
[152,0,136,129,132,138,142,137,131,137,123],
[144,114,0,133,120,116,122,117,119,126,127],
[148,121,117,0,114,122,124,131,128,124,122],
[144,118,130,136,0,126,135,121,122,130,125],
[143,112,134,128,124,0,138,129,134,138,128],
[138,108,128,126,115,112,0,119,110,112,119],
[132,113,133,119,129,121,131,0,119,125,110],
[137,119,131,122,128,116,140,131,0,127,122],
[143,113,124,126,120,112,138,125,123,0,128],
[144,127,123,128,125,122,131,140,128,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,125,131,124,140,127,135,130,130,110],
[123,0,126,117,122,130,123,129,125,141,130],
[125,124,0,125,122,133,130,131,134,123,127],
[119,133,125,0,122,130,130,128,134,138,130],
[126,128,128,128,0,128,132,126,129,128,113],
[110,120,117,120,122,0,115,125,124,123,123],
[123,127,120,120,118,135,0,129,131,125,111],
[115,121,119,122,124,125,121,0,128,127,108],
[120,125,116,116,121,126,119,122,0,119,126],
[120,109,127,112,122,127,125,123,131,0,121],
[140,120,123,120,137,127,139,142,124,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,134,122,140,157,140,119,124,119],
[125,0,127,140,117,129,143,135,144,155,121],
[129,123,0,125,123,126,149,116,109,124,139],
[116,110,125,0,112,122,127,122,103,115,141],
[128,133,127,138,0,115,153,120,126,128,136],
[110,121,124,128,135,0,136,130,127,137,120],
[93,107,101,123,97,114,0,101,91,116,103],
[110,115,134,128,130,120,149,0,121,137,120],
[131,106,141,147,124,123,159,129,0,113,128],
[126,95,126,135,122,113,134,113,137,0,139],
[131,129,111,109,114,130,147,130,122,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,155,194,144,151,119,132,138,154,148,135],
[95,0,133,138,98,116,116,74,119,94,104],
[56,117,0,125,113,125,107,84,98,108,88],
[106,112,125,0,85,137,85,86,142,71,90],
[99,152,137,165,0,124,111,61,113,107,150],
[131,134,125,113,126,0,81,87,138,107,118],
[118,134,143,165,139,169,0,115,116,132,132],
[112,176,166,164,189,163,135,0,164,151,162],
[96,131,152,108,137,112,134,86,0,119,119],
[102,156,142,179,143,143,118,99,131,0,119],
[115,146,162,160,100,132,118,88,131,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,141,134,140,108,129,121,116,97,113],
[121,0,122,112,111,85,111,106,138,106,106],
[109,128,0,120,124,101,100,117,111,96,99],
[116,138,130,0,119,122,129,124,116,126,112],
[110,139,126,131,0,118,132,114,116,116,118],
[142,165,149,128,132,0,123,148,140,134,139],
[121,139,150,121,118,127,0,141,136,122,136],
[129,144,133,126,136,102,109,0,114,100,114],
[134,112,139,134,134,110,114,136,0,128,117],
[153,144,154,124,134,116,128,150,122,0,119],
[137,144,151,138,132,111,114,136,133,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,72,113,122,90,101,76,111,76,90],
[150,0,119,104,139,112,109,116,143,110,120],
[178,131,0,132,117,113,115,115,121,96,103],
[137,146,118,0,136,99,110,91,140,98,116],
[128,111,133,114,0,115,115,82,117,103,114],
[160,138,137,151,135,0,112,86,147,114,115],
[149,141,135,140,135,138,0,101,144,112,143],
[174,134,135,159,168,164,149,0,161,125,127],
[139,107,129,110,133,103,106,89,0,79,90],
[174,140,154,152,147,136,138,125,171,0,132],
[160,130,147,134,136,135,107,123,160,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,134,147,139,119,102,118,118,138,125],
[121,0,117,129,113,131,117,110,109,145,116],
[116,133,0,132,125,103,105,124,98,142,118],
[103,121,118,0,124,117,95,107,104,122,104],
[111,137,125,126,0,106,90,116,104,143,110],
[131,119,147,133,144,0,120,119,107,133,120],
[148,133,145,155,160,130,0,142,143,169,120],
[132,140,126,143,134,131,108,0,109,140,131],
[132,141,152,146,146,143,107,141,0,146,123],
[112,105,108,128,107,117,81,110,104,0,98],
[125,134,132,146,140,130,130,119,127,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,124,132,122,129,134,124,127,123,128],
[130,0,119,131,127,129,128,136,133,137,134],
[126,131,0,134,122,123,123,134,137,130,125],
[118,119,116,0,116,123,116,120,123,122,130],
[128,123,128,134,0,128,124,120,132,129,128],
[121,121,127,127,122,0,125,138,128,128,128],
[116,122,127,134,126,125,0,125,132,125,123],
[126,114,116,130,130,112,125,0,124,128,122],
[123,117,113,127,118,122,118,126,0,127,122],
[127,113,120,128,121,122,125,122,123,0,123],
[122,116,125,120,122,122,127,128,128,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,144,125,144,149,138,134,130,134,135],
[137,0,105,129,117,131,132,121,110,126,111],
[106,145,0,146,144,156,146,139,128,130,117],
[125,121,104,0,136,139,153,96,94,117,143],
[106,133,106,114,0,145,143,116,73,79,119],
[101,119,94,111,105,0,119,116,70,85,120],
[112,118,104,97,107,131,0,127,91,91,98],
[116,129,111,154,134,134,123,0,125,113,121],
[120,140,122,156,177,180,159,125,0,126,132],
[116,124,120,133,171,165,159,137,124,0,161],
[115,139,133,107,131,130,152,129,118,89,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,123,121,118,122,115,123,113,137,131],
[126,0,122,118,127,128,132,126,121,129,132],
[127,128,0,123,123,129,125,116,117,117,131],
[129,132,127,0,134,126,127,130,125,125,127],
[132,123,127,116,0,121,126,122,115,123,117],
[128,122,121,124,129,0,128,121,126,117,126],
[135,118,125,123,124,122,0,121,111,122,129],
[127,124,134,120,128,129,129,0,119,124,138],
[137,129,133,125,135,124,139,131,0,132,138],
[113,121,133,125,127,133,128,126,118,0,141],
[119,118,119,123,133,124,121,112,112,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,149,130,143,119,161,128,110,121,136],
[143,0,150,134,120,114,142,134,121,160,151],
[101,100,0,115,117,103,136,122,121,121,115],
[120,116,135,0,92,90,118,123,104,115,107],
[107,130,133,158,0,126,155,153,151,150,134],
[131,136,147,160,124,0,165,159,149,182,145],
[89,108,114,132,95,85,0,118,123,109,120],
[122,116,128,127,97,91,132,0,118,111,130],
[140,129,129,146,99,101,127,132,0,134,143],
[129,90,129,135,100,68,141,139,116,0,124],
[114,99,135,143,116,105,130,120,107,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,130,126,128,136,114,127,125,124,127],
[122,0,123,123,118,138,130,119,113,124,115],
[120,127,0,112,119,144,128,118,128,125,120],
[124,127,138,0,128,138,125,122,134,134,115],
[122,132,131,122,0,127,130,116,121,125,125],
[114,112,106,112,123,0,131,118,109,113,121],
[136,120,122,125,120,119,0,120,118,132,116],
[123,131,132,128,134,132,130,0,122,126,118],
[125,137,122,116,129,141,132,128,0,137,127],
[126,126,125,116,125,137,118,124,113,0,112],
[123,135,130,135,125,129,134,132,123,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,119,141,127,129,130,118,133,143,126],
[130,0,116,122,133,125,124,112,127,136,127],
[131,134,0,142,138,143,128,116,139,151,145],
[109,128,108,0,106,116,117,119,114,129,109],
[123,117,112,144,0,127,109,129,127,140,123],
[121,125,107,134,123,0,126,113,122,152,133],
[120,126,122,133,141,124,0,126,138,161,136],
[132,138,134,131,121,137,124,0,149,153,115],
[117,123,111,136,123,128,112,101,0,155,126],
[107,114,99,121,110,98,89,97,95,0,116],
[124,123,105,141,127,117,114,135,124,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,124,135,127,122,137,121,127,118,130],
[125,0,127,125,133,121,136,114,127,113,132],
[126,123,0,120,132,120,143,116,119,119,116],
[115,125,130,0,130,116,134,117,123,122,117],
[123,117,118,120,0,112,130,109,127,121,114],
[128,129,130,134,138,0,135,118,134,122,112],
[113,114,107,116,120,115,0,100,103,108,112],
[129,136,134,133,141,132,150,0,149,128,121],
[123,123,131,127,123,116,147,101,0,123,115],
[132,137,131,128,129,128,142,122,127,0,131],
[120,118,134,133,136,138,138,129,135,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,132,134,136,133,131,130,125,118,140],
[129,0,128,135,143,145,143,130,128,123,135],
[118,122,0,126,127,133,107,119,130,112,128],
[116,115,124,0,129,122,131,124,112,118,131],
[114,107,123,121,0,117,122,131,115,117,128],
[117,105,117,128,133,0,124,121,109,118,133],
[119,107,143,119,128,126,0,129,124,125,124],
[120,120,131,126,119,129,121,0,117,105,134],
[125,122,120,138,135,141,126,133,0,121,134],
[132,127,138,132,133,132,125,145,129,0,143],
[110,115,122,119,122,117,126,116,116,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,112,126,126,132,105,146,136,114,107],
[115,0,112,122,120,139,111,118,115,116,107],
[138,138,0,124,123,128,121,151,128,132,119],
[124,128,126,0,118,144,130,119,119,122,117],
[124,130,127,132,0,149,120,150,135,128,136],
[118,111,122,106,101,0,113,130,117,109,100],
[145,139,129,120,130,137,0,159,135,140,121],
[104,132,99,131,100,120,91,0,120,101,97],
[114,135,122,131,115,133,115,130,0,135,127],
[136,134,118,128,122,141,110,149,115,0,128],
[143,143,131,133,114,150,129,153,123,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,131,129,126,131,124,140,118,113,126],
[119,0,123,133,120,130,121,134,118,124,133],
[119,127,0,129,112,129,123,125,127,115,122],
[121,117,121,0,120,126,109,127,103,118,122],
[124,130,138,130,0,133,130,138,124,119,141],
[119,120,121,124,117,0,111,125,114,104,126],
[126,129,127,141,120,139,0,142,123,119,125],
[110,116,125,123,112,125,108,0,110,106,115],
[132,132,123,147,126,136,127,140,0,128,130],
[137,126,135,132,131,146,131,144,122,0,133],
[124,117,128,128,109,124,125,135,120,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,120,124,137,126,117,119,136,115,130],
[123,0,129,121,120,134,124,114,143,111,124],
[130,121,0,136,125,123,116,125,127,113,118],
[126,129,114,0,123,137,132,123,136,113,131],
[113,130,125,127,0,120,131,111,138,109,124],
[124,116,127,113,130,0,129,126,139,113,124],
[133,126,134,118,119,121,0,122,150,125,136],
[131,136,125,127,139,124,128,0,139,122,128],
[114,107,123,114,112,111,100,111,0,103,122],
[135,139,137,137,141,137,125,128,147,0,136],
[120,126,132,119,126,126,114,122,128,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,129,130,131,113,133,131,106,94,144],
[141,0,129,134,168,127,131,141,111,136,151],
[121,121,0,140,139,96,133,143,127,99,143],
[120,116,110,0,127,126,137,118,88,81,121],
[119,82,111,123,0,125,114,129,100,90,128],
[137,123,154,124,125,0,102,101,104,110,111],
[117,119,117,113,136,148,0,123,124,111,120],
[119,109,107,132,121,149,127,0,103,99,138],
[144,139,123,162,150,146,126,147,0,134,134],
[156,114,151,169,160,140,139,151,116,0,143],
[106,99,107,129,122,139,130,112,116,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,136,123,119,117,133,134,119,124,127],
[122,0,125,120,115,117,133,120,121,112,113],
[114,125,0,113,113,111,121,124,109,113,100],
[127,130,137,0,124,123,128,141,126,133,122],
[131,135,137,126,0,126,125,138,119,134,127],
[133,133,139,127,124,0,143,135,125,131,123],
[117,117,129,122,125,107,0,127,112,121,115],
[116,130,126,109,112,115,123,0,124,111,105],
[131,129,141,124,131,125,138,126,0,124,121],
[126,138,137,117,116,119,129,139,126,0,119],
[123,137,150,128,123,127,135,145,129,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,145,144,123,139,145,134,122,133,136],
[123,0,130,158,140,117,134,106,147,132,151],
[105,120,0,124,99,105,110,114,119,106,124],
[106,92,126,0,115,129,111,101,129,107,116],
[127,110,151,135,0,154,133,122,130,125,133],
[111,133,145,121,96,0,121,120,136,129,134],
[105,116,140,139,117,129,0,131,128,127,131],
[116,144,136,149,128,130,119,0,137,130,141],
[128,103,131,121,120,114,122,113,0,103,130],
[117,118,144,143,125,121,123,120,147,0,127],
[114,99,126,134,117,116,119,109,120,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,130,128,116,124,136,141,145,142,141],
[128,0,148,146,123,141,134,149,141,141,145],
[120,102,0,132,109,125,110,110,121,120,117],
[122,104,118,0,98,132,126,121,132,133,118],
[134,127,141,152,0,121,129,132,129,132,148],
[126,109,125,118,129,0,118,127,138,134,123],
[114,116,140,124,121,132,0,122,142,130,123],
[109,101,140,129,118,123,128,0,137,130,154],
[105,109,129,118,121,112,108,113,0,128,125],
[108,109,130,117,118,116,120,120,122,0,130],
[109,105,133,132,102,127,127,96,125,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,152,142,142,147,145,148,123,147,138],
[135,0,119,129,117,149,143,123,134,127,135],
[98,131,0,132,121,147,124,110,114,126,120],
[108,121,118,0,117,129,124,113,113,123,121],
[108,133,129,133,0,146,133,136,116,133,144],
[103,101,103,121,104,0,125,127,117,113,120],
[105,107,126,126,117,125,0,126,114,126,142],
[102,127,140,137,114,123,124,0,108,118,130],
[127,116,136,137,134,133,136,142,0,131,130],
[103,123,124,127,117,137,124,132,119,0,119],
[112,115,130,129,106,130,108,120,120,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,147,129,126,113,140,130,149,140,153],
[112,0,121,132,124,114,127,129,123,123,126],
[103,129,0,104,117,119,118,141,110,122,143],
[121,118,146,0,105,127,146,157,141,139,142],
[124,126,133,145,0,115,134,137,125,126,127],
[137,136,131,123,135,0,145,157,140,140,149],
[110,123,132,104,116,105,0,130,128,129,127],
[120,121,109,93,113,93,120,0,119,126,124],
[101,127,140,109,125,110,122,131,0,131,135],
[110,127,128,111,124,110,121,124,119,0,134],
[97,124,107,108,123,101,123,126,115,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,114,119,133,143,135,147,128,131,140],
[105,0,132,109,119,120,120,130,124,127,147],
[136,118,0,114,127,119,107,131,122,124,137],
[131,141,136,0,134,119,133,142,131,140,143],
[117,131,123,116,0,104,118,130,122,125,126],
[107,130,131,131,146,0,131,123,136,137,152],
[115,130,143,117,132,119,0,124,119,137,149],
[103,120,119,108,120,127,126,0,120,115,130],
[122,126,128,119,128,114,131,130,0,135,135],
[119,123,126,110,125,113,113,135,115,0,138],
[110,103,113,107,124,98,101,120,115,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,134,126,118,121,123,131,117,124,131],
[119,0,129,116,117,126,118,112,116,120,119],
[116,121,0,120,111,105,117,108,119,113,117],
[124,134,130,0,131,122,128,123,125,131,136],
[132,133,139,119,0,118,127,131,118,122,139],
[129,124,145,128,132,0,136,133,129,121,127],
[127,132,133,122,123,114,0,115,129,116,131],
[119,138,142,127,119,117,135,0,117,120,138],
[133,134,131,125,132,121,121,133,0,139,137],
[126,130,137,119,128,129,134,130,111,0,134],
[119,131,133,114,111,123,119,112,113,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,111,120,97,109,107,121,148,89,125],
[151,0,155,135,114,131,130,149,167,141,147],
[139,95,0,133,91,111,122,126,169,117,145],
[130,115,117,0,101,143,126,155,161,113,134],
[153,136,159,149,0,158,123,145,183,155,152],
[141,119,139,107,92,0,144,139,162,122,125],
[143,120,128,124,127,106,0,148,150,135,128],
[129,101,124,95,105,111,102,0,130,110,106],
[102,83,81,89,67,88,100,120,0,88,98],
[161,109,133,137,95,128,115,140,162,0,153],
[125,103,105,116,98,125,122,144,152,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,120,118,118,111,115,108,120,108,108],
[136,0,138,121,120,131,132,127,124,123,132],
[130,112,0,109,101,122,113,127,122,115,123],
[132,129,141,0,122,137,128,124,125,121,116],
[132,130,149,128,0,141,141,133,134,129,117],
[139,119,128,113,109,0,117,126,120,126,117],
[135,118,137,122,109,133,0,124,131,125,115],
[142,123,123,126,117,124,126,0,127,129,119],
[130,126,128,125,116,130,119,123,0,120,126],
[142,127,135,129,121,124,125,121,130,0,132],
[142,118,127,134,133,133,135,131,124,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,131,119,134,134,114,142,117,130,133],
[105,0,115,121,110,125,108,122,139,107,116],
[119,135,0,132,139,127,122,146,121,136,130],
[131,129,118,0,124,128,130,130,125,135,125],
[116,140,111,126,0,126,122,116,116,111,128],
[116,125,123,122,124,0,125,126,111,106,120],
[136,142,128,120,128,125,0,133,118,124,128],
[108,128,104,120,134,124,117,0,112,108,133],
[133,111,129,125,134,139,132,138,0,118,130],
[120,143,114,115,139,144,126,142,132,0,129],
[117,134,120,125,122,130,122,117,120,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,141,135,107,139,126,153,131,141,116],
[101,0,141,118,96,112,105,113,107,135,113],
[109,109,0,125,91,118,89,119,117,125,131],
[115,132,125,0,115,102,101,129,99,135,119],
[143,154,159,135,0,147,130,140,133,125,130],
[111,138,132,148,103,0,104,111,134,126,121],
[124,145,161,149,120,146,0,147,130,159,146],
[97,137,131,121,110,139,103,0,119,129,116],
[119,143,133,151,117,116,120,131,0,124,103],
[109,115,125,115,125,124,91,121,126,0,107],
[134,137,119,131,120,129,104,134,147,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,118,133,131,127,124,121,129,128,120],
[127,0,127,128,129,145,128,121,128,120,125],
[132,123,0,128,123,126,121,125,125,125,119],
[117,122,122,0,116,127,111,109,131,128,116],
[119,121,127,134,0,128,118,119,137,127,115],
[123,105,124,123,122,0,112,119,116,126,114],
[126,122,129,139,132,138,0,118,129,131,137],
[129,129,125,141,131,131,132,0,137,141,127],
[121,122,125,119,113,134,121,113,0,127,121],
[122,130,125,122,123,124,119,109,123,0,121],
[130,125,131,134,135,136,113,123,129,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,133,141,144,130,149,144,123,124,127],
[142,0,137,155,135,133,152,160,147,109,124],
[117,113,0,127,133,116,135,135,116,95,112],
[109,95,123,0,124,110,132,127,112,105,97],
[106,115,117,126,0,112,142,116,116,120,95],
[120,117,134,140,138,0,133,131,125,109,102],
[101,98,115,118,108,117,0,112,105,106,80],
[106,90,115,123,134,119,138,0,132,109,106],
[127,103,134,138,134,125,145,118,0,118,115],
[126,141,155,145,130,141,144,141,132,0,118],
[123,126,138,153,155,148,170,144,135,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,140,142,141,134,121,133,127,147,120],
[117,0,120,126,115,128,119,115,126,133,112],
[110,130,0,138,130,137,116,136,128,133,127],
[108,124,112,0,117,119,112,124,113,131,115],
[109,135,120,133,0,123,103,131,120,139,117],
[116,122,113,131,127,0,114,127,119,131,110],
[129,131,134,138,147,136,0,135,134,145,123],
[117,135,114,126,119,123,115,0,112,133,119],
[123,124,122,137,130,131,116,138,0,143,125],
[103,117,117,119,111,119,105,117,107,0,110],
[130,138,123,135,133,140,127,131,125,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,128,121,144,110,140,132,137,114,124],
[118,0,133,126,141,125,146,127,130,126,126],
[122,117,0,120,150,145,130,133,136,122,131],
[129,124,130,0,145,129,145,119,140,136,127],
[106,109,100,105,0,115,118,129,121,126,105],
[140,125,105,121,135,0,129,124,136,138,130],
[110,104,120,105,132,121,0,124,120,102,127],
[118,123,117,131,121,126,126,0,127,119,116],
[113,120,114,110,129,114,130,123,0,121,130],
[136,124,128,114,124,112,148,131,129,0,107],
[126,124,119,123,145,120,123,134,120,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,125,120,106,104,124,125,97,122,128],
[132,0,110,121,112,133,137,136,113,138,105],
[125,140,0,123,121,132,133,130,96,121,103],
[130,129,127,0,114,117,128,116,97,133,104],
[144,138,129,136,0,134,145,146,125,136,133],
[146,117,118,133,116,0,135,135,108,136,103],
[126,113,117,122,105,115,0,134,97,107,100],
[125,114,120,134,104,115,116,0,90,126,103],
[153,137,154,153,125,142,153,160,0,138,120],
[128,112,129,117,114,114,143,124,112,0,97],
[122,145,147,146,117,147,150,147,130,153,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,107,83,128,60,98,84,52,73,96],
[119,0,38,79,134,61,108,91,33,84,58],
[143,212,0,126,173,132,138,136,80,78,109],
[167,171,124,0,198,147,152,130,94,125,115],
[122,116,77,52,0,84,110,110,64,80,81],
[190,189,118,103,166,0,147,101,75,111,107],
[152,142,112,98,140,103,0,95,88,105,68],
[166,159,114,120,140,149,155,0,117,129,136],
[198,217,170,156,186,175,162,133,0,133,118],
[177,166,172,125,170,139,145,121,117,0,103],
[154,192,141,135,169,143,182,114,132,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,153,141,131,134,132,133,139,113,139],
[108,0,90,104,104,100,99,133,119,101,87],
[97,160,0,100,104,126,103,125,138,119,86],
[109,146,150,0,103,104,130,121,168,106,136],
[119,146,146,147,0,142,129,115,140,133,92],
[116,150,124,146,108,0,116,123,117,129,129],
[118,151,147,120,121,134,0,113,148,154,104],
[117,117,125,129,135,127,137,0,156,119,121],
[111,131,112,82,110,133,102,94,0,121,98],
[137,149,131,144,117,121,96,131,129,0,101],
[111,163,164,114,158,121,146,129,152,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,127,111,113,124,122,126,117,120,133],
[114,0,116,110,121,113,113,120,113,100,120],
[123,134,0,117,121,131,113,118,128,127,132],
[139,140,133,0,132,134,129,148,130,116,137],
[137,129,129,118,0,126,128,137,124,107,129],
[126,137,119,116,124,0,118,146,112,102,139],
[128,137,137,121,122,132,0,137,113,105,111],
[124,130,132,102,113,104,113,0,110,95,121],
[133,137,122,120,126,138,137,140,0,116,136],
[130,150,123,134,143,148,145,155,134,0,135],
[117,130,118,113,121,111,139,129,114,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,130,125,124,104,116,115,120,127,128],
[124,0,144,119,98,115,129,114,109,140,124],
[120,106,0,136,103,115,122,126,106,128,122],
[125,131,114,0,115,103,115,109,111,120,127],
[126,152,147,135,0,120,119,131,136,136,135],
[146,135,135,147,130,0,136,128,124,136,137],
[134,121,128,135,131,114,0,118,114,137,125],
[135,136,124,141,119,122,132,0,116,142,133],
[130,141,144,139,114,126,136,134,0,136,132],
[123,110,122,130,114,114,113,108,114,0,117],
[122,126,128,123,115,113,125,117,118,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,141,130,125,142,89,88,103,118,59],
[117,0,160,120,97,141,77,93,107,59,59],
[109,90,0,100,147,137,117,96,109,63,75],
[120,130,150,0,131,158,129,119,129,102,113],
[125,153,103,119,0,84,99,100,90,99,44],
[108,109,113,92,166,0,73,66,128,82,54],
[161,173,133,121,151,177,0,120,148,82,123],
[162,157,154,131,150,184,130,0,99,97,57],
[147,143,141,121,160,122,102,151,0,130,99],
[132,191,187,148,151,168,168,153,120,0,134],
[191,191,175,137,206,196,127,193,151,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,174,105,101,101,69,117,147,215,139],
[122,0,125,105,94,67,79,157,144,140,138],
[76,125,0,66,75,87,139,138,200,135,157],
[145,145,184,0,91,141,106,156,167,173,144],
[149,156,175,159,0,196,79,186,173,239,172],
[149,183,163,109,54,0,118,149,178,151,114],
[181,171,111,144,171,132,0,187,222,183,157],
[133,93,112,94,64,101,63,0,109,133,138],
[103,106,50,83,77,72,28,141,0,144,85],
[35,110,115,77,11,99,67,117,106,0,51],
[111,112,93,106,78,136,93,112,165,199,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,119,113,117,96,90,113,109,114,107],
[147,0,136,114,128,134,125,133,123,141,126],
[131,114,0,109,125,98,98,109,104,123,99],
[137,136,141,0,148,115,122,133,140,136,138],
[133,122,125,102,0,115,119,121,113,113,109],
[154,116,152,135,135,0,118,145,132,134,135],
[160,125,152,128,131,132,0,136,132,133,123],
[137,117,141,117,129,105,114,0,131,123,127],
[141,127,146,110,137,118,118,119,0,123,122],
[136,109,127,114,137,116,117,127,127,0,125],
[143,124,151,112,141,115,127,123,128,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,128,179,124,192,154,152,139,120,159],
[104,0,100,185,134,158,128,127,145,102,138],
[122,150,0,152,133,177,130,102,133,122,140],
[71,65,98,0,85,97,74,91,90,67,82],
[126,116,117,165,0,195,116,148,134,140,136],
[58,92,73,153,55,0,99,78,87,52,108],
[96,122,120,176,134,151,0,133,127,97,146],
[98,123,148,159,102,172,117,0,135,106,140],
[111,105,117,160,116,163,123,115,0,79,140],
[130,148,128,183,110,198,153,144,171,0,148],
[91,112,110,168,114,142,104,110,110,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,134,135,131,138,125,130,139,132,127],
[128,0,118,115,129,115,125,124,137,138,120],
[116,132,0,118,125,124,106,113,127,129,113],
[115,135,132,0,124,132,107,115,124,130,103],
[119,121,125,126,0,127,115,124,129,129,116],
[112,135,126,118,123,0,124,128,136,128,122],
[125,125,144,143,135,126,0,131,137,149,131],
[120,126,137,135,126,122,119,0,140,138,116],
[111,113,123,126,121,114,113,110,0,129,115],
[118,112,121,120,121,122,101,112,121,0,106],
[123,130,137,147,134,128,119,134,135,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,128,137,132,125,119,134,137,126,123],
[124,0,116,142,143,125,143,138,144,132,118],
[122,134,0,133,126,121,114,128,118,109,130],
[113,108,117,0,136,134,113,132,123,115,123],
[118,107,124,114,0,116,109,130,119,115,122],
[125,125,129,116,134,0,132,135,134,127,124],
[131,107,136,137,141,118,0,124,121,114,132],
[116,112,122,118,120,115,126,0,128,111,129],
[113,106,132,127,131,116,129,122,0,107,117],
[124,118,141,135,135,123,136,139,143,0,139],
[127,132,120,127,128,126,118,121,133,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,133,127,138,135,125,139,125,136,127],
[126,0,144,134,132,146,148,133,122,138,140],
[117,106,0,118,140,140,125,126,112,120,120],
[123,116,132,0,139,133,123,122,115,124,123],
[112,118,110,111,0,129,114,132,117,125,123],
[115,104,110,117,121,0,114,115,113,117,125],
[125,102,125,127,136,136,0,129,121,133,136],
[111,117,124,128,118,135,121,0,117,113,116],
[125,128,138,135,133,137,129,133,0,149,124],
[114,112,130,126,125,133,117,137,101,0,115],
[123,110,130,127,127,125,114,134,126,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,118,121,120,118,110,126,123,124,119],
[140,0,123,123,122,121,124,121,127,133,130],
[132,127,0,128,119,127,126,126,138,142,130],
[129,127,122,0,132,124,125,119,127,124,130],
[130,128,131,118,0,135,119,124,127,134,131],
[132,129,123,126,115,0,119,125,128,124,127],
[140,126,124,125,131,131,0,125,131,129,141],
[124,129,124,131,126,125,125,0,126,136,130],
[127,123,112,123,123,122,119,124,0,132,129],
[126,117,108,126,116,126,121,114,118,0,121],
[131,120,120,120,119,123,109,120,121,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,149,116,141,135,149,146,122,144,133],
[130,0,134,108,132,118,154,136,113,122,140],
[101,116,0,102,123,120,139,121,97,117,112],
[134,142,148,0,143,166,164,152,125,134,137],
[109,118,127,107,0,125,142,142,103,116,118],
[115,132,130,84,125,0,137,132,103,120,125],
[101,96,111,86,108,113,0,118,99,104,123],
[104,114,129,98,108,118,132,0,86,101,117],
[128,137,153,125,147,147,151,164,0,141,154],
[106,128,133,116,134,130,146,149,109,0,118],
[117,110,138,113,132,125,127,133,96,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,110,123,113,122,109,116,123,127,109],
[118,0,108,104,107,111,102,104,110,101,109],
[140,142,0,129,116,141,116,113,124,121,114],
[127,146,121,0,113,129,113,132,131,129,112],
[137,143,134,137,0,135,134,132,128,130,124],
[128,139,109,121,115,0,119,124,125,116,115],
[141,148,134,137,116,131,0,138,124,142,127],
[134,146,137,118,118,126,112,0,131,126,132],
[127,140,126,119,122,125,126,119,0,124,129],
[123,149,129,121,120,134,108,124,126,0,117],
[141,141,136,138,126,135,123,118,121,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,126,107,94,103,71,74,98,87,84],
[147,0,160,141,134,156,164,124,158,123,98],
[124,90,0,115,95,143,129,116,106,92,96],
[143,109,135,0,95,135,93,90,129,114,81],
[156,116,155,155,0,142,143,125,128,159,93],
[147,94,107,115,108,0,75,77,115,97,69],
[179,86,121,157,107,175,0,122,132,134,123],
[176,126,134,160,125,173,128,0,128,105,120],
[152,92,144,121,122,135,118,122,0,109,97],
[163,127,158,136,91,153,116,145,141,0,125],
[166,152,154,169,157,181,127,130,153,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,138,110,128,115,116,119,115,122,117],
[129,0,124,104,134,103,110,124,112,112,106],
[112,126,0,77,109,112,100,112,101,98,98],
[140,146,173,0,135,141,132,147,124,151,127],
[122,116,141,115,0,101,111,130,115,124,102],
[135,147,138,109,149,0,119,135,130,128,113],
[134,140,150,118,139,131,0,125,125,135,127],
[131,126,138,103,120,115,125,0,120,122,108],
[135,138,149,126,135,120,125,130,0,130,122],
[128,138,152,99,126,122,115,128,120,0,110],
[133,144,152,123,148,137,123,142,128,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,125,136,145,124,134,133,132,128,150],
[121,0,127,131,131,131,129,140,121,118,137],
[125,123,0,129,132,134,127,138,137,121,138],
[114,119,121,0,126,119,125,121,121,113,135],
[105,119,118,124,0,117,122,123,112,116,129],
[126,119,116,131,133,0,132,131,116,123,144],
[116,121,123,125,128,118,0,131,121,115,147],
[117,110,112,129,127,119,119,0,119,119,121],
[118,129,113,129,138,134,129,131,0,124,129],
[122,132,129,137,134,127,135,131,126,0,133],
[100,113,112,115,121,106,103,129,121,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,141,105,136,129,125,124,118,142],
[128,0,160,121,144,147,128,128,133,122,134],
[123,90,0,116,97,118,108,122,111,110,119],
[109,129,134,0,114,144,126,124,108,129,123],
[145,106,153,136,0,153,118,134,138,124,126],
[114,103,132,106,97,0,114,130,110,111,118],
[121,122,142,124,132,136,0,111,137,110,132],
[125,122,128,126,116,120,139,0,127,138,144],
[126,117,139,142,112,140,113,123,0,131,127],
[132,128,140,121,126,139,140,112,119,0,146],
[108,116,131,127,124,132,118,106,123,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,119,125,110,137,137,107,141,127,145],
[106,0,121,102,113,62,129,118,120,104,127],
[131,129,0,109,111,110,118,128,139,141,151],
[125,148,141,0,112,117,142,130,134,127,168],
[140,137,139,138,0,104,145,131,136,168,168],
[113,188,140,133,146,0,174,145,179,126,183],
[113,121,132,108,105,76,0,114,123,139,158],
[143,132,122,120,119,105,136,0,129,122,140],
[109,130,111,116,114,71,127,121,0,111,156],
[123,146,109,123,82,124,111,128,139,0,151],
[105,123,99,82,82,67,92,110,94,99,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,125,130,140,126,135,132,124,127,130],
[119,0,114,135,138,131,133,124,124,122,117],
[125,136,0,138,138,133,138,135,137,129,135],
[120,115,112,0,134,129,121,121,119,108,130],
[110,112,112,116,0,120,125,120,115,109,109],
[124,119,117,121,130,0,118,115,115,127,120],
[115,117,112,129,125,132,0,111,120,116,120],
[118,126,115,129,130,135,139,0,127,136,132],
[126,126,113,131,135,135,130,123,0,125,122],
[123,128,121,142,141,123,134,114,125,0,129],
[120,133,115,120,141,130,130,118,128,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,134,118,127,120,119,122,123,129,125],
[126,0,128,129,113,123,127,118,128,131,125],
[116,122,0,124,121,115,132,115,129,118,128],
[132,121,126,0,123,126,117,122,125,127,126],
[123,137,129,127,0,134,124,123,134,126,123],
[130,127,135,124,116,0,131,119,129,130,129],
[131,123,118,133,126,119,0,116,122,126,122],
[128,132,135,128,127,131,134,0,132,132,125],
[127,122,121,125,116,121,128,118,0,124,125],
[121,119,132,123,124,120,124,118,126,0,137],
[125,125,122,124,127,121,128,125,125,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,134,127,133,131,117,126,147,136,131],
[131,0,128,117,125,124,124,132,133,135,135],
[116,122,0,123,125,123,114,130,140,132,134],
[123,133,127,0,135,137,123,132,135,146,129],
[117,125,125,115,0,126,126,131,133,138,140],
[119,126,127,113,124,0,124,127,130,134,125],
[133,126,136,127,124,126,0,137,130,141,132],
[124,118,120,118,119,123,113,0,139,142,131],
[103,117,110,115,117,120,120,111,0,137,122],
[114,115,118,104,112,116,109,108,113,0,111],
[119,115,116,121,110,125,118,119,128,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,127,129,140,127,112,144,120,124,99],
[133,0,114,144,127,136,143,156,121,132,129],
[123,136,0,142,107,126,123,126,113,116,101],
[121,106,108,0,103,119,113,144,114,117,98],
[110,123,143,147,0,134,133,149,153,134,134],
[123,114,124,131,116,0,119,148,123,128,125],
[138,107,127,137,117,131,0,170,146,153,129],
[106,94,124,106,101,102,80,0,100,85,93],
[130,129,137,136,97,127,104,150,0,100,141],
[126,118,134,133,116,122,97,165,150,0,108],
[151,121,149,152,116,125,121,157,109,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,141,125,126,125,133,132,121,139,137],
[118,0,126,116,130,125,118,128,125,133,129],
[109,124,0,113,123,118,112,121,114,126,127],
[125,134,137,0,142,130,123,118,123,138,136],
[124,120,127,108,0,121,122,124,125,117,126],
[125,125,132,120,129,0,134,134,133,130,122],
[117,132,138,127,128,116,0,124,122,135,133],
[118,122,129,132,126,116,126,0,117,127,125],
[129,125,136,127,125,117,128,133,0,141,146],
[111,117,124,112,133,120,115,123,109,0,118],
[113,121,123,114,124,128,117,125,104,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,126,127,130,131,145,136,133,126,126],
[134,0,125,129,138,115,138,127,124,136,137],
[124,125,0,127,116,124,141,141,127,127,129],
[123,121,123,0,131,124,135,130,122,132,132],
[120,112,134,119,0,115,124,135,109,132,122],
[119,135,126,126,135,0,137,125,122,137,127],
[105,112,109,115,126,113,0,114,104,118,114],
[114,123,109,120,115,125,136,0,121,118,121],
[117,126,123,128,141,128,146,129,0,128,128],
[124,114,123,118,118,113,132,132,122,0,123],
[124,113,121,118,128,123,136,129,122,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,109,138,146,129,121,143,143,151,133],
[106,0,115,129,121,120,127,137,129,121,102],
[141,135,0,133,133,135,138,139,151,138,125],
[112,121,117,0,131,113,105,144,112,125,106],
[104,129,117,119,0,99,111,128,117,126,123],
[121,130,115,137,151,0,104,136,117,132,113],
[129,123,112,145,139,146,0,154,155,141,136],
[107,113,111,106,122,114,96,0,124,122,115],
[107,121,99,138,133,133,95,126,0,121,105],
[99,129,112,125,124,118,109,128,129,0,107],
[117,148,125,144,127,137,114,135,145,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,128,128,128,128,115,107,134,132,118],
[128,0,121,120,126,119,120,120,117,129,134],
[122,129,0,127,134,144,149,141,117,130,137],
[122,130,123,0,127,122,120,146,120,128,126],
[122,124,116,123,0,113,127,116,121,128,127],
[122,131,106,128,137,0,127,130,125,124,138],
[135,130,101,130,123,123,0,126,113,131,131],
[143,130,109,104,134,120,124,0,131,130,134],
[116,133,133,130,129,125,137,119,0,128,131],
[118,121,120,122,122,126,119,120,122,0,128],
[132,116,113,124,123,112,119,116,119,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,127,105,175,106,109,92,126,154,124],
[130,0,117,145,192,109,128,143,126,183,151],
[123,133,0,132,171,115,138,110,142,149,150],
[145,105,118,0,162,108,97,120,123,129,131],
[75,58,79,88,0,91,66,72,83,111,98],
[144,141,135,142,159,0,107,108,147,152,165],
[141,122,112,153,184,143,0,119,133,156,159],
[158,107,140,130,178,142,131,0,158,184,150],
[124,124,108,127,167,103,117,92,0,143,140],
[96,67,101,121,139,98,94,66,107,0,126],
[126,99,100,119,152,85,91,100,110,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,107,145,142,127,105,69,126,137,92],
[113,0,71,123,109,96,96,104,149,94,83],
[143,179,0,168,175,173,136,108,195,142,158],
[105,127,82,0,91,100,75,54,128,139,55],
[108,141,75,159,0,152,84,73,140,132,108],
[123,154,77,150,98,0,116,67,136,106,106],
[145,154,114,175,166,134,0,139,157,152,140],
[181,146,142,196,177,183,111,0,184,163,159],
[124,101,55,122,110,114,93,66,0,124,98],
[113,156,108,111,118,144,98,87,126,0,83],
[158,167,92,195,142,144,110,91,152,167,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,133,133,64,151,82,47,186,186,18],
[186,0,151,151,47,186,81,47,151,150,46],
[117,99,0,185,110,221,81,110,185,81,117],
[117,99,65,0,146,221,117,146,214,81,117],
[186,203,140,104,0,186,221,187,157,185,186],
[99,64,29,29,64,0,53,47,82,92,46],
[168,169,169,133,29,197,0,83,133,161,168],
[203,203,140,104,63,203,167,0,139,167,168],
[64,99,65,36,93,168,117,111,0,63,64],
[64,100,169,169,65,158,89,83,187,0,82],
[232,204,133,133,64,204,82,82,186,168,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,119,144,152,110,99,127,127,91,106],
[137,0,127,132,140,139,116,124,140,132,133],
[131,123,0,120,150,149,106,117,143,123,115],
[106,118,130,0,121,109,101,106,145,111,145],
[98,110,100,129,0,137,82,123,132,97,121],
[140,111,101,141,113,0,116,105,132,112,122],
[151,134,144,149,168,134,0,134,163,97,148],
[123,126,133,144,127,145,116,0,141,99,121],
[123,110,107,105,118,118,87,109,0,99,143],
[159,118,127,139,153,138,153,151,151,0,135],
[144,117,135,105,129,128,102,129,107,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,139,140,135,122,138,138,123,146,139],
[121,0,144,129,143,126,143,135,133,144,149],
[111,106,0,124,117,111,122,124,106,139,123],
[110,121,126,0,125,112,120,120,113,125,131],
[115,107,133,125,0,129,133,129,121,132,138],
[128,124,139,138,121,0,128,126,134,142,126],
[112,107,128,130,117,122,0,129,127,128,126],
[112,115,126,130,121,124,121,0,126,138,124],
[127,117,144,137,129,116,123,124,0,149,142],
[104,106,111,125,118,108,122,112,101,0,119],
[111,101,127,119,112,124,124,126,108,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,123,157,148,129,138,127,159,123,118],
[132,0,136,151,157,153,122,141,140,127,132],
[127,114,0,154,137,145,105,138,146,135,106],
[93,99,96,0,125,126,100,110,128,104,74],
[102,93,113,125,0,119,96,90,107,103,90],
[121,97,105,124,131,0,117,118,128,98,101],
[112,128,145,150,154,133,0,122,155,136,114],
[123,109,112,140,160,132,128,0,142,115,120],
[91,110,104,122,143,122,95,108,0,94,99],
[127,123,115,146,147,152,114,135,156,0,120],
[132,118,144,176,160,149,136,130,151,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,125,133,138,131,129,137,141,119,139],
[119,0,119,122,112,133,125,115,132,123,122],
[125,131,0,129,135,130,134,132,133,128,122],
[117,128,121,0,116,127,117,121,132,115,125],
[112,138,115,134,0,116,129,128,130,118,133],
[119,117,120,123,134,0,133,126,141,124,121],
[121,125,116,133,121,117,0,116,124,120,117],
[113,135,118,129,122,124,134,0,139,134,123],
[109,118,117,118,120,109,126,111,0,111,111],
[131,127,122,135,132,126,130,116,139,0,131],
[111,128,128,125,117,129,133,127,139,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,128,127,129,126,124,132,136,125,132],
[119,0,117,122,107,118,110,121,119,127,131],
[122,133,0,137,126,124,125,132,122,124,124],
[123,128,113,0,116,132,121,120,129,130,131],
[121,143,124,134,0,137,126,134,132,126,132],
[124,132,126,118,113,0,119,111,126,123,141],
[126,140,125,129,124,131,0,133,133,126,139],
[118,129,118,130,116,139,117,0,123,131,132],
[114,131,128,121,118,124,117,127,0,116,126],
[125,123,126,120,124,127,124,119,134,0,127],
[118,119,126,119,118,109,111,118,124,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,134,120,120,130,120,127,119,142,122],
[114,0,118,119,119,124,109,117,121,131,124],
[116,132,0,117,127,117,129,126,133,141,135],
[130,131,133,0,116,121,122,132,131,142,129],
[130,131,123,134,0,133,126,124,129,147,135],
[120,126,133,129,117,0,122,121,131,141,134],
[130,141,121,128,124,128,0,124,125,136,136],
[123,133,124,118,126,129,126,0,120,144,133],
[131,129,117,119,121,119,125,130,0,136,122],
[108,119,109,108,103,109,114,106,114,0,126],
[128,126,115,121,115,116,114,117,128,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,108,122,98,137,113,141,122,135,103],
[112,0,110,134,113,127,104,115,102,111,102],
[142,140,0,154,148,138,119,139,110,156,147],
[128,116,96,0,103,118,102,123,101,124,115],
[152,137,102,147,0,132,122,134,139,135,121],
[113,123,112,132,118,0,135,125,117,117,135],
[137,146,131,148,128,115,0,146,118,125,119],
[109,135,111,127,116,125,104,0,123,110,108],
[128,148,140,149,111,133,132,127,0,151,134],
[115,139,94,126,115,133,125,140,99,0,119],
[147,148,103,135,129,115,131,142,116,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,118,129,129,106,122,119,130,120,132],
[118,0,121,119,104,113,121,116,111,110,119],
[132,129,0,114,122,104,120,127,120,115,127],
[121,131,136,0,129,125,132,123,119,117,134],
[121,146,128,121,0,124,128,123,126,123,139],
[144,137,146,125,126,0,130,127,124,129,136],
[128,129,130,118,122,120,0,122,120,118,138],
[131,134,123,127,127,123,128,0,128,112,133],
[120,139,130,131,124,126,130,122,0,126,133],
[130,140,135,133,127,121,132,138,124,0,134],
[118,131,123,116,111,114,112,117,117,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,144,128,138,132,129,138,122,120,131],
[122,0,123,103,142,137,146,133,134,125,107],
[106,127,0,125,134,141,144,136,126,136,126],
[122,147,125,0,142,146,152,144,125,138,134],
[112,108,116,108,0,116,124,116,128,117,102],
[118,113,109,104,134,0,135,130,121,117,115],
[121,104,106,98,126,115,0,122,125,96,108],
[112,117,114,106,134,120,128,0,124,113,119],
[128,116,124,125,122,129,125,126,0,125,119],
[130,125,114,112,133,133,154,137,125,0,119],
[119,143,124,116,148,135,142,131,131,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,191,145,68,174,168,155,126,139,156,126],
[59,0,112,41,105,116,57,56,85,117,50],
[105,138,0,81,152,150,118,118,146,172,99],
[182,209,169,0,165,199,152,145,180,161,124],
[76,145,98,85,0,131,68,77,95,135,78],
[82,134,100,51,119,0,98,81,86,139,66],
[95,193,132,98,182,152,0,105,123,175,117],
[124,194,132,105,173,169,145,0,157,210,116],
[111,165,104,70,155,164,127,93,0,159,104],
[94,133,78,89,115,111,75,40,91,0,102],
[124,200,151,126,172,184,133,134,146,148,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,112,126,110,118,120,123,137,121,129],
[124,0,130,136,124,125,141,135,144,135,134],
[138,120,0,140,128,142,141,137,131,114,133],
[124,114,110,0,117,130,139,137,141,126,125],
[140,126,122,133,0,131,141,133,146,135,130],
[132,125,108,120,119,0,138,132,130,125,134],
[130,109,109,111,109,112,0,126,132,120,117],
[127,115,113,113,117,118,124,0,132,124,123],
[113,106,119,109,104,120,118,118,0,113,123],
[129,115,136,124,115,125,130,126,137,0,131],
[121,116,117,125,120,116,133,127,127,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,137,111,132,132,160,124,119,123,127],
[124,0,111,124,122,143,135,114,122,108,132],
[113,139,0,135,118,135,164,173,104,140,117],
[139,126,115,0,118,148,143,99,113,117,112],
[118,128,132,132,0,175,137,144,135,135,117],
[118,107,115,102,75,0,136,112,129,126,106],
[90,115,86,107,113,114,0,102,100,90,110],
[126,136,77,151,106,138,148,0,111,142,110],
[131,128,146,137,115,121,150,139,0,143,152],
[127,142,110,133,115,124,160,108,107,0,126],
[123,118,133,138,133,144,140,140,98,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,100,108,148,127,142,166,139,110,147],
[117,0,95,68,65,91,130,122,145,107,107],
[150,155,0,122,92,138,126,136,176,118,160],
[142,182,128,0,106,122,132,135,188,138,186],
[102,185,158,144,0,142,155,152,157,112,155],
[123,159,112,128,108,0,123,170,137,121,146],
[108,120,124,118,95,127,0,146,140,101,157],
[84,128,114,115,98,80,104,0,124,109,137],
[111,105,74,62,93,113,110,126,0,112,136],
[140,143,132,112,138,129,149,141,138,0,174],
[103,143,90,64,95,104,93,113,114,76,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,141,137,126,140,132,123,143,144,147],
[112,0,122,135,120,125,119,124,134,126,133],
[109,128,0,129,111,132,113,130,138,130,125],
[113,115,121,0,104,134,105,99,116,128,112],
[124,130,139,146,0,135,112,124,140,147,134],
[110,125,118,116,115,0,124,112,132,130,123],
[118,131,137,145,138,126,0,126,134,138,134],
[127,126,120,151,126,138,124,0,148,137,140],
[107,116,112,134,110,118,116,102,0,125,116],
[106,124,120,122,103,120,112,113,125,0,131],
[103,117,125,138,116,127,116,110,134,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,137,121,129,134,130,137,135,146,128],
[115,0,132,119,111,126,114,118,115,127,115],
[113,118,0,120,115,135,123,126,107,138,113],
[129,131,130,0,114,120,124,131,123,135,110],
[121,139,135,136,0,130,124,133,127,136,121],
[116,124,115,130,120,0,114,126,106,122,110],
[120,136,127,126,126,136,0,130,113,139,117],
[113,132,124,119,117,124,120,0,112,125,111],
[115,135,143,127,123,144,137,138,0,135,128],
[104,123,112,115,114,128,111,125,115,0,116],
[122,135,137,140,129,140,133,139,122,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,124,131,130,128,137,115,144,162,130],
[120,0,107,111,114,118,130,110,125,144,128],
[126,143,0,129,125,134,142,136,150,149,153],
[119,139,121,0,122,111,132,124,124,146,122],
[120,136,125,128,0,115,134,122,132,145,132],
[122,132,116,139,135,0,142,125,137,145,136],
[113,120,108,118,116,108,0,116,121,142,120],
[135,140,114,126,128,125,134,0,127,152,125],
[106,125,100,126,118,113,129,123,0,144,119],
[88,106,101,104,105,105,108,98,106,0,110],
[120,122,97,128,118,114,130,125,131,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,126,142,115,142,133,151,134,127,129],
[128,0,126,129,121,136,129,148,131,133,126],
[124,124,0,133,123,125,126,135,133,121,115],
[108,121,117,0,119,132,120,138,136,119,122],
[135,129,127,131,0,122,128,139,126,126,124],
[108,114,125,118,128,0,120,140,130,114,117],
[117,121,124,130,122,130,0,145,140,123,130],
[99,102,115,112,111,110,105,0,123,103,106],
[116,119,117,114,124,120,110,127,0,108,123],
[123,117,129,131,124,136,127,147,142,0,129],
[121,124,135,128,126,133,120,144,127,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,125,132,138,136,140,132,129,132,130],
[129,0,124,127,129,126,141,117,135,133,131],
[125,126,0,141,162,159,144,132,145,135,152],
[118,123,109,0,127,142,136,125,139,121,136],
[112,121,88,123,0,132,125,121,118,122,119],
[114,124,91,108,118,0,115,137,121,129,96],
[110,109,106,114,125,135,0,114,119,128,112],
[118,133,118,125,129,113,136,0,132,143,125],
[121,115,105,111,132,129,131,118,0,130,129],
[118,117,115,129,128,121,122,107,120,0,114],
[120,119,98,114,131,154,138,125,121,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,114,116,119,122,119,121,109,119,116],
[130,0,130,130,110,128,131,122,109,123,118],
[136,120,0,118,111,126,125,120,110,122,110],
[134,120,132,0,130,127,123,120,124,123,129],
[131,140,139,120,0,132,132,129,122,143,123],
[128,122,124,123,118,0,125,115,113,123,116],
[131,119,125,127,118,125,0,124,117,124,118],
[129,128,130,130,121,135,126,0,115,124,114],
[141,141,140,126,128,137,133,135,0,125,129],
[131,127,128,127,107,127,126,126,125,0,122],
[134,132,140,121,127,134,132,136,121,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,119,132,124,133,126,135,136,125,115],
[123,0,128,129,128,130,124,134,138,123,119],
[131,122,0,137,136,131,131,142,137,141,121],
[118,121,113,0,136,122,121,120,144,123,123],
[126,122,114,114,0,119,112,126,136,132,120],
[117,120,119,128,131,0,117,118,123,135,126],
[124,126,119,129,138,133,0,125,137,131,130],
[115,116,108,130,124,132,125,0,142,121,127],
[114,112,113,106,114,127,113,108,0,123,109],
[125,127,109,127,118,115,119,129,127,0,111],
[135,131,129,127,130,124,120,123,141,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,112,129,121,141,124,122,144,137,141],
[106,0,113,121,124,132,109,119,115,130,117],
[138,137,0,125,135,148,125,131,123,143,128],
[121,129,125,0,118,125,117,118,124,155,139],
[129,126,115,132,0,144,121,132,133,145,139],
[109,118,102,125,106,0,123,113,125,137,141],
[126,141,125,133,129,127,0,126,129,144,131],
[128,131,119,132,118,137,124,0,137,149,130],
[106,135,127,126,117,125,121,113,0,149,140],
[113,120,107,95,105,113,106,101,101,0,117],
[109,133,122,111,111,109,119,120,110,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,122,128,124,116,111,137,120,112,111],
[121,0,121,140,126,133,115,137,137,135,122],
[128,129,0,138,133,126,120,145,145,120,133],
[122,110,112,0,111,125,111,118,135,128,119],
[126,124,117,139,0,144,116,129,130,132,126],
[134,117,124,125,106,0,126,132,146,126,132],
[139,135,130,139,134,124,0,132,141,143,141],
[113,113,105,132,121,118,118,0,128,120,132],
[130,113,105,115,120,104,109,122,0,87,115],
[138,115,130,122,118,124,107,130,163,0,119],
[139,128,117,131,124,118,109,118,135,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,136,119,143,147,117,167,121,139,132],
[128,0,123,122,126,126,105,145,112,139,141],
[114,127,0,117,124,135,105,147,110,129,127],
[131,128,133,0,124,145,126,154,109,127,137],
[107,124,126,126,0,128,106,141,128,139,141],
[103,124,115,105,122,0,89,142,104,115,119],
[133,145,145,124,144,161,0,163,134,146,153],
[83,105,103,96,109,108,87,0,89,110,125],
[129,138,140,141,122,146,116,161,0,129,156],
[111,111,121,123,111,135,104,140,121,0,136],
[118,109,123,113,109,131,97,125,94,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,123,118,124,141,121,128,124,126,114],
[128,0,121,126,121,128,116,121,126,116,113],
[127,129,0,118,118,118,117,125,120,122,125],
[132,124,132,0,123,130,124,131,131,115,133],
[126,129,132,127,0,128,128,113,119,128,114],
[109,122,132,120,122,0,119,114,122,121,111],
[129,134,133,126,122,131,0,126,133,130,116],
[122,129,125,119,137,136,124,0,120,123,129],
[126,124,130,119,131,128,117,130,0,130,115],
[124,134,128,135,122,129,120,127,120,0,128],
[136,137,125,117,136,139,134,121,135,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,127,119,125,123,121,127,116,121,127],
[116,0,125,121,129,130,128,128,126,115,117],
[123,125,0,121,119,129,124,128,127,119,117],
[131,129,129,0,123,129,130,121,129,125,125],
[125,121,131,127,0,124,116,121,125,130,119],
[127,120,121,121,126,0,123,130,125,106,119],
[129,122,126,120,134,127,0,129,125,112,123],
[123,122,122,129,129,120,121,0,114,112,129],
[134,124,123,121,125,125,125,136,0,117,124],
[129,135,131,125,120,144,138,138,133,0,121],
[123,133,133,125,131,131,127,121,126,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,136,137,124,130,129,130,135,120,131],
[125,0,146,143,124,127,138,124,134,131,135],
[114,104,0,130,120,110,122,125,121,115,112],
[113,107,120,0,117,109,121,125,119,116,107],
[126,126,130,133,0,121,125,128,133,116,126],
[120,123,140,141,129,0,126,128,121,124,114],
[121,112,128,129,125,124,0,130,129,115,118],
[120,126,125,125,122,122,120,0,123,108,124],
[115,116,129,131,117,129,121,127,0,112,123],
[130,119,135,134,134,126,135,142,138,0,127],
[119,115,138,143,124,136,132,126,127,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,113,121,120,121,116,117,127,122,119],
[137,0,118,118,134,119,119,127,130,118,132],
[137,132,0,123,128,142,132,134,134,134,143],
[129,132,127,0,132,121,120,120,133,113,129],
[130,116,122,118,0,121,122,116,136,118,122],
[129,131,108,129,129,0,118,119,125,126,121],
[134,131,118,130,128,132,0,122,138,131,135],
[133,123,116,130,134,131,128,0,139,129,129],
[123,120,116,117,114,125,112,111,0,112,134],
[128,132,116,137,132,124,119,121,138,0,129],
[131,118,107,121,128,129,115,121,116,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,139,113,112,107,152,116,140,110,143],
[155,0,164,145,152,125,122,128,157,143,134],
[111,86,0,129,102,105,142,91,120,106,100],
[137,105,121,0,145,105,128,93,134,111,129],
[138,98,148,105,0,94,132,115,135,75,127],
[143,125,145,145,156,0,144,141,173,114,134],
[98,128,108,122,118,106,0,110,125,132,115],
[134,122,159,157,135,109,140,0,148,128,132],
[110,93,130,116,115,77,125,102,0,112,123],
[140,107,144,139,175,136,118,122,138,0,145],
[107,116,150,121,123,116,135,118,127,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,139,135,142,133,121,129,146,145,131],
[130,0,124,112,129,124,132,129,134,139,132],
[111,126,0,120,129,120,129,137,130,128,116],
[115,138,130,0,146,123,125,128,147,135,129],
[108,121,121,104,0,113,121,109,132,124,122],
[117,126,130,127,137,0,120,115,139,130,127],
[129,118,121,125,129,130,0,118,133,131,113],
[121,121,113,122,141,135,132,0,136,128,122],
[104,116,120,103,118,111,117,114,0,123,113],
[105,111,122,115,126,120,119,122,127,0,113],
[119,118,134,121,128,123,137,128,137,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,127,125,125,112,126,119,114,114,136],
[125,0,126,109,123,124,123,119,121,130,129],
[123,124,0,115,139,120,131,127,133,133,136],
[125,141,135,0,128,128,134,131,128,121,129],
[125,127,111,122,0,134,126,121,125,122,124],
[138,126,130,122,116,0,115,134,127,125,116],
[124,127,119,116,124,135,0,122,130,126,125],
[131,131,123,119,129,116,128,0,125,122,120],
[136,129,117,122,125,123,120,125,0,132,132],
[136,120,117,129,128,125,124,128,118,0,118],
[114,121,114,121,126,134,125,130,118,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,177,157,140,154,177,154,106,177,177],
[108,0,170,169,93,160,202,122,78,130,150],
[73,80,0,137,101,140,171,143,113,151,151],
[93,81,113,0,132,146,169,128,98,182,113],
[110,157,149,118,0,145,142,95,151,178,178],
[96,90,110,104,105,0,142,85,103,99,145],
[73,48,79,81,108,108,0,141,111,108,108],
[96,128,107,122,155,165,109,0,83,143,150],
[144,172,137,152,99,147,139,167,0,145,171],
[73,120,99,68,72,151,142,107,105,0,154],
[73,100,99,137,72,105,142,100,79,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,138,134,129,133,117,122,133,119,116],
[121,0,132,122,136,132,117,123,140,122,120],
[112,118,0,109,130,129,116,109,134,115,117],
[116,128,141,0,131,134,124,131,141,120,120],
[121,114,120,119,0,122,122,116,135,131,117],
[117,118,121,116,128,0,113,113,140,116,105],
[133,133,134,126,128,137,0,123,150,127,126],
[128,127,141,119,134,137,127,0,139,118,114],
[117,110,116,109,115,110,100,111,0,113,106],
[131,128,135,130,119,134,123,132,137,0,122],
[134,130,133,130,133,145,124,136,144,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,128,124,119,114,128,121,121,125,119],
[106,0,121,111,118,129,117,119,118,118,105],
[122,129,0,110,124,124,123,122,121,126,114],
[126,139,140,0,139,129,148,141,111,129,130],
[131,132,126,111,0,123,119,125,111,126,123],
[136,121,126,121,127,0,124,144,123,111,123],
[122,133,127,102,131,126,0,115,124,115,121],
[129,131,128,109,125,106,135,0,118,128,119],
[129,132,129,139,139,127,126,132,0,122,117],
[125,132,124,121,124,139,135,122,128,0,124],
[131,145,136,120,127,127,129,131,133,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,140,125,121,138,127,141,140,129,133],
[131,0,121,116,122,130,109,145,107,123,122],
[110,129,0,132,126,128,120,147,117,131,146],
[125,134,118,0,113,134,113,142,108,126,129],
[129,128,124,137,0,143,120,148,132,133,145],
[112,120,122,116,107,0,117,135,113,114,119],
[123,141,130,137,130,133,0,142,118,128,127],
[109,105,103,108,102,115,108,0,106,127,107],
[110,143,133,142,118,137,132,144,0,123,134],
[121,127,119,124,117,136,122,123,127,0,125],
[117,128,104,121,105,131,123,143,116,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,127,125,128,121,122,122,127,110],
[114,0,116,127,122,118,119,114,119,133,118],
[124,134,0,127,124,117,121,112,117,131,114],
[123,123,123,0,123,121,126,125,121,141,116],
[125,128,126,127,0,121,122,122,119,130,119],
[122,132,133,129,129,0,114,128,131,138,119],
[129,131,129,124,128,136,0,128,129,137,115],
[128,136,138,125,128,122,122,0,121,139,126],
[128,131,133,129,131,119,121,129,0,141,118],
[123,117,119,109,120,112,113,111,109,0,111],
[140,132,136,134,131,131,135,124,132,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,136,135,122,116,121,138,121,116,127],
[130,0,142,128,123,117,134,135,121,125,125],
[114,108,0,122,104,112,125,114,118,119,117],
[115,122,128,0,121,122,116,127,120,114,116],
[128,127,146,129,0,133,130,134,133,117,128],
[134,133,138,128,117,0,135,139,132,115,122],
[129,116,125,134,120,115,0,123,121,111,128],
[112,115,136,123,116,111,127,0,107,105,110],
[129,129,132,130,117,118,129,143,0,121,133],
[134,125,131,136,133,135,139,145,129,0,129],
[123,125,133,134,122,128,122,140,117,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,129,122,114,121,111,121,120,115,123],
[127,0,128,136,127,126,115,127,126,120,133],
[121,122,0,128,106,122,111,125,125,111,125],
[128,114,122,0,97,117,115,120,121,107,123],
[136,123,144,153,0,137,130,137,138,136,140],
[129,124,128,133,113,0,117,121,118,122,125],
[139,135,139,135,120,133,0,137,127,132,136],
[129,123,125,130,113,129,113,0,116,121,134],
[130,124,125,129,112,132,123,134,0,132,135],
[135,130,139,143,114,128,118,129,118,0,127],
[127,117,125,127,110,125,114,116,115,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,116,122,169,121,115,149,132,129,124],
[119,0,121,120,165,113,120,142,127,128,128],
[134,129,0,119,141,121,124,126,142,129,129],
[128,130,131,0,170,119,109,147,126,137,117],
[81,85,109,80,0,81,106,123,109,110,91],
[129,137,129,131,169,0,115,157,125,134,123],
[135,130,126,141,144,135,0,140,127,124,102],
[101,108,124,103,127,93,110,0,104,111,106],
[118,123,108,124,141,125,123,146,0,135,92],
[121,122,121,113,140,116,126,139,115,0,114],
[126,122,121,133,159,127,148,144,158,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,124,125,127,133,117,117,110,117,121],
[141,0,127,139,135,143,140,139,120,112,141],
[126,123,0,128,128,140,134,124,115,128,131],
[125,111,122,0,125,136,116,118,109,100,126],
[123,115,122,125,0,131,116,114,110,122,117],
[117,107,110,114,119,0,107,123,107,102,122],
[133,110,116,134,134,143,0,123,124,115,131],
[133,111,126,132,136,127,127,0,118,114,125],
[140,130,135,141,140,143,126,132,0,125,134],
[133,138,122,150,128,148,135,136,125,0,133],
[129,109,119,124,133,128,119,125,116,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,129,131,131,134,132,123,109,127,128],
[130,0,121,131,125,139,141,126,135,125,135],
[121,129,0,96,140,136,131,120,131,106,111],
[119,119,154,0,122,140,132,139,126,129,126],
[119,125,110,128,0,130,126,131,112,111,113],
[116,111,114,110,120,0,127,109,121,114,113],
[118,109,119,118,124,123,0,131,114,118,123],
[127,124,130,111,119,141,119,0,113,114,115],
[141,115,119,124,138,129,136,137,0,128,115],
[123,125,144,121,139,136,132,136,122,0,126],
[122,115,139,124,137,137,127,135,135,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,111,115,146,136,125,128,121,118,124],
[126,0,122,120,130,147,112,122,110,124,127],
[139,128,0,129,146,144,138,142,122,128,130],
[135,130,121,0,141,135,129,130,115,125,139],
[104,120,104,109,0,129,111,119,101,112,120],
[114,103,106,115,121,0,110,124,98,116,106],
[125,138,112,121,139,140,0,135,119,128,130],
[122,128,108,120,131,126,115,0,111,113,123],
[129,140,128,135,149,152,131,139,0,125,122],
[132,126,122,125,138,134,122,137,125,0,133],
[126,123,120,111,130,144,120,127,128,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,131,118,131,131,129,120,137,134,124],
[126,0,127,114,105,131,141,138,135,115,118],
[119,123,0,112,99,112,122,121,129,127,113],
[132,136,138,0,119,138,150,131,148,125,130],
[119,145,151,131,0,144,143,137,144,152,140],
[119,119,138,112,106,0,128,126,131,128,127],
[121,109,128,100,107,122,0,121,104,124,115],
[130,112,129,119,113,124,129,0,132,125,113],
[113,115,121,102,106,119,146,118,0,103,124],
[116,135,123,125,98,122,126,125,147,0,123],
[126,132,137,120,110,123,135,137,126,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,126,125,143,120,142,135,123,136,146],
[105,0,125,110,133,109,132,116,121,134,125],
[124,125,0,119,145,106,135,119,126,132,130],
[125,140,131,0,138,103,134,120,122,127,122],
[107,117,105,112,0,115,109,114,96,117,103],
[130,141,144,147,135,0,142,132,125,135,137],
[108,118,115,116,141,108,0,111,117,125,114],
[115,134,131,130,136,118,139,0,121,131,117],
[127,129,124,128,154,125,133,129,0,144,127],
[114,116,118,123,133,115,125,119,106,0,124],
[104,125,120,128,147,113,136,133,123,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,129,121,120,129,132,127,127,127,134],
[131,0,124,127,128,124,122,132,127,130,126],
[121,126,0,120,132,134,140,124,118,126,142],
[129,123,130,0,129,132,146,129,127,128,137],
[130,122,118,121,0,128,122,119,135,137,130],
[121,126,116,118,122,0,132,125,121,122,131],
[118,128,110,104,128,118,0,116,111,117,117],
[123,118,126,121,131,125,134,0,116,119,132],
[123,123,132,123,115,129,139,134,0,123,134],
[123,120,124,122,113,128,133,131,127,0,116],
[116,124,108,113,120,119,133,118,116,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,133,133,124,129,133,114,118,119,111],
[122,0,125,134,123,134,137,120,127,123,118],
[117,125,0,122,122,126,123,119,105,121,106],
[117,116,128,0,118,118,117,118,104,116,108],
[126,127,128,132,0,125,137,127,118,128,124],
[121,116,124,132,125,0,132,117,119,117,108],
[117,113,127,133,113,118,0,114,112,119,108],
[136,130,131,132,123,133,136,0,122,126,112],
[132,123,145,146,132,131,138,128,0,129,123],
[131,127,129,134,122,133,131,124,121,0,125],
[139,132,144,142,126,142,142,138,127,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,117,123,105,101,111,107,111,107,111],
[147,0,131,132,132,126,125,126,131,119,128],
[133,119,0,123,124,107,133,117,127,119,117],
[127,118,127,0,126,99,115,126,127,109,114],
[145,118,126,124,0,119,120,126,125,123,122],
[149,124,143,151,131,0,132,129,132,124,121],
[139,125,117,135,130,118,0,114,132,122,123],
[143,124,133,124,124,121,136,0,137,133,125],
[139,119,123,123,125,118,118,113,0,118,116],
[143,131,131,141,127,126,128,117,132,0,130],
[139,122,133,136,128,129,127,125,134,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,114,152,114,91,101,121,121,120,128],
[132,0,123,142,131,131,128,136,137,134,131],
[136,127,0,139,122,127,135,148,148,126,121],
[98,108,111,0,112,104,111,111,122,106,113],
[136,119,128,138,0,118,136,137,126,140,126],
[159,119,123,146,132,0,134,141,123,142,129],
[149,122,115,139,114,116,0,133,118,125,129],
[129,114,102,139,113,109,117,0,126,126,122],
[129,113,102,128,124,127,132,124,0,134,122],
[130,116,124,144,110,108,125,124,116,0,127],
[122,119,129,137,124,121,121,128,128,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,117,126,122,98,107,125,108,116,118],
[124,0,116,120,124,106,106,127,109,118,114],
[133,134,0,122,127,105,115,134,118,119,126],
[124,130,128,0,121,112,117,133,119,127,105],
[128,126,123,129,0,112,123,124,109,119,114],
[152,144,145,138,138,0,127,148,124,138,138],
[143,144,135,133,127,123,0,140,130,130,127],
[125,123,116,117,126,102,110,0,115,118,124],
[142,141,132,131,141,126,120,135,0,129,121],
[134,132,131,123,131,112,120,132,121,0,128],
[132,136,124,145,136,112,123,126,129,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,83,126,122,115,112,123,120,105,112],
[120,0,81,112,142,109,118,110,112,111,113],
[167,169,0,128,146,138,169,152,143,124,144],
[124,138,122,0,115,116,123,121,131,111,128],
[128,108,104,135,0,117,123,128,145,134,146],
[135,141,112,134,133,0,116,130,136,123,123],
[138,132,81,127,127,134,0,121,125,118,139],
[127,140,98,129,122,120,129,0,121,103,131],
[130,138,107,119,105,114,125,129,0,121,119],
[145,139,126,139,116,127,132,147,129,0,139],
[138,137,106,122,104,127,111,119,131,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,123,137,150,163,142,143,146,130,127],
[119,0,121,115,141,146,115,116,142,127,108],
[127,129,0,130,133,145,115,146,141,116,117],
[113,135,120,0,131,143,114,144,136,116,106],
[100,109,117,119,0,127,106,122,117,95,98],
[87,104,105,107,123,0,98,114,120,97,103],
[108,135,135,136,144,152,0,133,136,112,118],
[107,134,104,106,128,136,117,0,127,104,125],
[104,108,109,114,133,130,114,123,0,123,108],
[120,123,134,134,155,153,138,146,127,0,118],
[123,142,133,144,152,147,132,125,142,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,112,132,129,115,129,128,111,136,112],
[132,0,127,138,127,113,127,141,110,128,108],
[138,123,0,141,128,128,130,142,123,143,125],
[118,112,109,0,120,116,116,130,116,124,115],
[121,123,122,130,0,115,127,132,112,124,120],
[135,137,122,134,135,0,126,141,130,129,117],
[121,123,120,134,123,124,0,126,118,122,115],
[122,109,108,120,118,109,124,0,113,120,108],
[139,140,127,134,138,120,132,137,0,136,126],
[114,122,107,126,126,121,128,130,114,0,118],
[138,142,125,135,130,133,135,142,124,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,139,124,134,122,148,131,136,136,151],
[121,0,127,131,135,129,144,128,126,129,150],
[111,123,0,140,130,128,138,145,126,134,145],
[126,119,110,0,131,135,132,143,128,128,144],
[116,115,120,119,0,127,112,122,113,117,142],
[128,121,122,115,123,0,145,146,122,130,157],
[102,106,112,118,138,105,0,141,112,116,140],
[119,122,105,107,128,104,109,0,97,109,134],
[114,124,124,122,137,128,138,153,0,143,138],
[114,121,116,122,133,120,134,141,107,0,132],
[99,100,105,106,108,93,110,116,112,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,110,106,118,120,112,123,128,125,111],
[115,0,111,101,119,118,118,121,104,127,107],
[140,139,0,133,140,135,123,117,145,138,143],
[144,149,117,0,139,131,138,134,151,155,127],
[132,131,110,111,0,115,121,111,126,125,105],
[130,132,115,119,135,0,119,117,134,133,125],
[138,132,127,112,129,131,0,119,127,134,114],
[127,129,133,116,139,133,131,0,134,138,115],
[122,146,105,99,124,116,123,116,0,129,112],
[125,123,112,95,125,117,116,112,121,0,99],
[139,143,107,123,145,125,136,135,138,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,145,123,132,146,150,142,157,127,139],
[105,0,131,104,116,113,122,139,109,108,122],
[105,119,0,93,109,121,105,139,112,102,116],
[127,146,157,0,139,127,142,140,137,125,149],
[118,134,141,111,0,126,125,140,136,121,131],
[104,137,129,123,124,0,133,143,147,113,139],
[100,128,145,108,125,117,0,129,113,124,134],
[108,111,111,110,110,107,121,0,107,120,116],
[93,141,138,113,114,103,137,143,0,114,123],
[123,142,148,125,129,137,126,130,136,0,126],
[111,128,134,101,119,111,116,134,127,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,167,134,177,144,126,139,123,116,124,134],
[83,0,61,117,109,89,108,79,91,54,120],
[116,189,0,137,126,121,157,88,131,101,119],
[73,133,113,0,131,104,110,110,141,100,99],
[106,141,124,119,0,136,132,103,95,106,122],
[124,161,129,146,114,0,152,117,112,122,134],
[111,142,93,140,118,98,0,93,124,88,134],
[127,171,162,140,147,133,157,0,107,152,145],
[134,159,119,109,155,138,126,143,0,114,145],
[126,196,149,150,144,128,162,98,136,0,144],
[116,130,131,151,128,116,116,105,105,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,137,118,109,134,123,164,174,137,90],
[126,0,105,124,93,82,132,131,157,122,97],
[113,145,0,124,102,91,138,147,179,136,145],
[132,126,126,0,109,123,162,141,202,154,138],
[141,157,148,141,0,115,144,161,181,149,120],
[116,168,159,127,135,0,128,161,194,128,126],
[127,118,112,88,106,122,0,168,142,100,118],
[86,119,103,109,89,89,82,0,151,111,86],
[76,93,71,48,69,56,108,99,0,82,88],
[113,128,114,96,101,122,150,139,168,0,98],
[160,153,105,112,130,124,132,164,162,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,89,87,106,94,110,136,88,96,69,109],
[161,0,119,150,113,151,130,120,122,124,153],
[163,131,0,118,105,120,107,96,96,81,122],
[144,100,132,0,105,102,122,150,157,116,149],
[156,137,145,145,0,108,117,133,143,125,135],
[140,99,130,148,142,0,135,152,127,110,152],
[114,120,143,128,133,115,0,157,149,124,125],
[162,130,154,100,117,98,93,0,120,89,127],
[154,128,154,93,107,123,101,130,0,87,118],
[181,126,169,134,125,140,126,161,163,0,179],
[141,97,128,101,115,98,125,123,132,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,218,192,97,121,108,111,132,110,109],
[125,0,138,140,96,120,114,93,70,100,132],
[32,112,0,85,57,70,77,62,58,109,54],
[58,110,165,0,54,100,50,93,38,65,43],
[153,154,193,196,0,131,122,97,124,154,96],
[129,130,180,150,119,0,104,80,89,121,61],
[142,136,173,200,128,146,0,127,107,87,135],
[139,157,188,157,153,170,123,0,122,134,95],
[118,180,192,212,126,161,143,128,0,131,99],
[140,150,141,185,96,129,163,116,119,0,114],
[141,118,196,207,154,189,115,155,151,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,136,149,121,130,142,130,135,148,136],
[98,0,111,133,103,121,109,104,116,118,124],
[114,139,0,152,125,127,141,132,123,141,132],
[101,117,98,0,92,112,121,115,113,112,128],
[129,147,125,158,0,132,134,119,136,130,137],
[120,129,123,138,118,0,127,129,122,132,136],
[108,141,109,129,116,123,0,127,128,139,136],
[120,146,118,135,131,121,123,0,124,128,129],
[115,134,127,137,114,128,122,126,0,121,135],
[102,132,109,138,120,118,111,122,129,0,134],
[114,126,118,122,113,114,114,121,115,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,169,202,174,169,169,192,155,188,122],
[116,0,114,141,105,115,110,130,152,165,69],
[81,136,0,185,142,143,130,157,174,147,139],
[48,109,65,0,83,91,95,91,93,114,62],
[76,145,108,167,0,141,108,161,159,176,94],
[81,135,107,159,109,0,100,153,125,137,84],
[81,140,120,155,142,150,0,155,144,131,91],
[58,120,93,159,89,97,95,0,114,129,77],
[95,98,76,157,91,125,106,136,0,141,111],
[62,85,103,136,74,113,119,121,109,0,78],
[128,181,111,188,156,166,159,173,139,172,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,127,130,131,153,125,125,128,127,126],
[116,0,130,121,131,142,118,123,124,120,134],
[123,120,0,120,133,138,117,120,123,130,133],
[120,129,130,0,134,144,128,114,132,129,143],
[119,119,117,116,0,134,119,112,128,113,112],
[97,108,112,106,116,0,116,108,111,101,103],
[125,132,133,122,131,134,0,133,121,143,139],
[125,127,130,136,138,142,117,0,132,133,125],
[122,126,127,118,122,139,129,118,0,117,119],
[123,130,120,121,137,149,107,117,133,0,118],
[124,116,117,107,138,147,111,125,131,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,107,121,115,125,117,111,114,135,110],
[116,0,106,126,127,115,124,93,116,101,117],
[143,144,0,98,143,112,169,120,109,122,113],
[129,124,152,0,146,112,149,103,134,124,104],
[135,123,107,104,0,105,132,109,114,117,112],
[125,135,138,138,145,0,146,114,133,107,122],
[133,126,81,101,118,104,0,86,115,103,89],
[139,157,130,147,141,136,164,0,150,122,124],
[136,134,141,116,136,117,135,100,0,125,112],
[115,149,128,126,133,143,147,128,125,0,125],
[140,133,137,146,138,128,161,126,138,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,96,138,116,119,90,120,101,120,125,113],
[154,0,141,147,126,118,140,126,121,146,129],
[112,109,0,114,100,119,123,105,120,126,122],
[134,103,136,0,104,122,114,106,105,138,134],
[131,124,150,146,0,127,135,107,109,129,133],
[160,132,131,128,123,0,141,124,131,151,146],
[130,110,127,136,115,109,0,117,105,142,143],
[149,124,145,144,143,126,133,0,123,128,120],
[130,129,130,145,141,119,145,127,0,133,135],
[125,104,124,112,121,99,108,122,117,0,116],
[137,121,128,116,117,104,107,130,115,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,146,148,123,115,128,116,138,166,119],
[115,0,137,144,145,98,136,106,121,134,130],
[104,113,0,121,121,101,115,120,106,122,114],
[102,106,129,0,115,83,106,102,117,121,112],
[127,105,129,135,0,121,100,121,111,137,118],
[135,152,149,167,129,0,138,143,143,151,104],
[122,114,135,144,150,112,0,131,114,149,128],
[134,144,130,148,129,107,119,0,137,156,110],
[112,129,144,133,139,107,136,113,0,151,141],
[84,116,128,129,113,99,101,94,99,0,128],
[131,120,136,138,132,146,122,140,109,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,123,132,106,134,118,130,128,123,122],
[127,0,127,133,116,131,121,119,121,123,122],
[127,123,0,136,124,129,124,132,118,123,123],
[118,117,114,0,119,134,122,121,119,117,115],
[144,134,126,131,0,144,137,122,126,134,132],
[116,119,121,116,106,0,110,115,124,109,123],
[132,129,126,128,113,140,0,123,121,138,130],
[120,131,118,129,128,135,127,0,123,141,139],
[122,129,132,131,124,126,129,127,0,131,124],
[127,127,127,133,116,141,112,109,119,0,120],
[128,128,127,135,118,127,120,111,126,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,129,105,114,150,135,115,127,137,147],
[134,0,168,125,108,161,136,136,127,154,109],
[121,82,0,95,94,129,130,110,118,135,99],
[145,125,155,0,127,159,141,125,145,162,133],
[136,142,156,123,0,178,149,145,167,155,152],
[100,89,121,91,72,0,111,85,98,98,113],
[115,114,120,109,101,139,0,134,124,128,118],
[135,114,140,125,105,165,116,0,130,140,102],
[123,123,132,105,83,152,126,120,0,151,107],
[113,96,115,88,95,152,122,110,99,0,107],
[103,141,151,117,98,137,132,148,143,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,102,106,79,95,114,124,116,109,106],
[169,0,149,173,144,125,186,143,159,148,151],
[148,101,0,128,120,95,138,145,134,104,125],
[144,77,122,0,104,100,145,116,114,118,118],
[171,106,130,146,0,94,163,122,109,137,141],
[155,125,155,150,156,0,179,161,145,153,130],
[136,64,112,105,87,71,0,125,104,87,73],
[126,107,105,134,128,89,125,0,114,95,123],
[134,91,116,136,141,105,146,136,0,149,134],
[141,102,146,132,113,97,163,155,101,0,127],
[144,99,125,132,109,120,177,127,116,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,135,137,126,119,130,136,132,122,125],
[133,0,132,139,130,118,133,128,132,132,120],
[115,118,0,128,120,122,130,126,121,126,106],
[113,111,122,0,118,123,123,116,116,118,111],
[124,120,130,132,0,118,135,130,133,120,117],
[131,132,128,127,132,0,135,140,135,124,122],
[120,117,120,127,115,115,0,125,124,119,110],
[114,122,124,134,120,110,125,0,121,119,121],
[118,118,129,134,117,115,126,129,0,122,116],
[128,118,124,132,130,126,131,131,128,0,124],
[125,130,144,139,133,128,140,129,134,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,128,124,143,122,133,131,127,120,123],
[127,0,132,116,132,106,135,123,122,122,122],
[122,118,0,124,136,113,108,133,116,126,115],
[126,134,126,0,144,117,124,126,126,120,117],
[107,118,114,106,0,113,127,108,117,123,101],
[128,144,137,133,137,0,139,150,140,130,125],
[117,115,142,126,123,111,0,130,127,113,117],
[119,127,117,124,142,100,120,0,131,119,130],
[123,128,134,124,133,110,123,119,0,130,116],
[130,128,124,130,127,120,137,131,120,0,122],
[127,128,135,133,149,125,133,120,134,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,111,134,104,121,105,127,91,118,121],
[128,0,125,128,135,148,144,146,124,146,139],
[139,125,0,136,135,120,121,126,125,146,150],
[116,122,114,0,128,121,134,130,116,136,132],
[146,115,115,122,0,126,120,131,122,136,133],
[129,102,130,129,124,0,124,130,123,128,126],
[145,106,129,116,130,126,0,135,125,135,136],
[123,104,124,120,119,120,115,0,112,116,130],
[159,126,125,134,128,127,125,138,0,155,145],
[132,104,104,114,114,122,115,134,95,0,130],
[129,111,100,118,117,124,114,120,105,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,149,153,151,125,154,146,152,133,144],
[118,0,137,137,130,112,123,114,121,112,147],
[101,113,0,135,112,120,117,129,109,102,144],
[97,113,115,0,113,122,125,115,115,118,146],
[99,120,138,137,0,113,132,126,139,117,139],
[125,138,130,128,137,0,131,123,138,135,137],
[96,127,133,125,118,119,0,110,146,133,140],
[104,136,121,135,124,127,140,0,130,114,139],
[98,129,141,135,111,112,104,120,0,128,137],
[117,138,148,132,133,115,117,136,122,0,145],
[106,103,106,104,111,113,110,111,113,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,100,160,120,88,117,139,101,83,137],
[171,0,109,142,121,165,149,180,77,105,141],
[150,141,0,152,166,96,146,145,133,129,128],
[90,108,98,0,126,165,95,126,133,144,138],
[130,129,84,124,0,88,151,137,101,83,127],
[162,85,154,85,162,0,108,162,139,117,101],
[133,101,104,155,99,142,0,185,133,115,181],
[111,70,105,124,113,88,65,0,124,79,123],
[149,173,117,117,149,111,117,126,0,136,150],
[167,145,121,106,167,133,135,171,114,0,145],
[113,109,122,112,123,149,69,127,100,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,130,136,130,140,142,128,138,135,119],
[119,0,129,124,133,129,133,134,149,131,133],
[120,121,0,132,143,137,127,142,134,137,129],
[114,126,118,0,126,128,129,130,119,132,120],
[120,117,107,124,0,127,134,133,130,128,124],
[110,121,113,122,123,0,126,116,121,130,123],
[108,117,123,121,116,124,0,120,126,138,126],
[122,116,108,120,117,134,130,0,124,132,112],
[112,101,116,131,120,129,124,126,0,132,108],
[115,119,113,118,122,120,112,118,118,0,118],
[131,117,121,130,126,127,124,138,142,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,124,134,115,123,116,126,127,124,111],
[141,0,131,130,129,127,124,122,126,130,133],
[126,119,0,119,124,125,107,123,126,131,127],
[116,120,131,0,126,118,114,124,123,135,127],
[135,121,126,124,0,126,112,129,129,130,129],
[127,123,125,132,124,0,114,125,117,140,138],
[134,126,143,136,138,136,0,131,123,140,137],
[124,128,127,126,121,125,119,0,123,124,131],
[123,124,124,127,121,133,127,127,0,125,138],
[126,120,119,115,120,110,110,126,125,0,128],
[139,117,123,123,121,112,113,119,112,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,130,134,119,132,121,132,127,155,141],
[113,0,106,115,122,110,116,104,124,122,127],
[120,144,0,127,144,133,122,127,128,160,136],
[116,135,123,0,129,124,123,110,141,140,140],
[131,128,106,121,0,131,128,116,109,130,145],
[118,140,117,126,119,0,117,122,131,142,132],
[129,134,128,127,122,133,0,121,143,142,145],
[118,146,123,140,134,128,129,0,141,140,147],
[123,126,122,109,141,119,107,109,0,152,139],
[95,128,90,110,120,108,108,110,98,0,122],
[109,123,114,110,105,118,105,103,111,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,160,103,97,132,85,113,135,88,70,115],
[90,0,115,118,113,90,112,124,125,84,111],
[147,135,0,91,153,79,95,115,111,98,103],
[153,132,159,0,145,124,155,153,116,125,132],
[118,137,97,105,0,94,142,84,110,118,109],
[165,160,171,126,156,0,175,151,125,106,138],
[137,138,155,95,108,75,0,123,90,126,116],
[115,126,135,97,166,99,127,0,132,127,100],
[162,125,139,134,140,125,160,118,0,120,140],
[180,166,152,125,132,144,124,123,130,0,141],
[135,139,147,118,141,112,134,150,110,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,139,130,115,135,145,118,139,121],
[123,0,118,129,129,117,126,131,120,135,115],
[127,132,0,127,123,108,132,134,114,140,115],
[111,121,123,0,139,122,126,135,120,143,113],
[120,121,127,111,0,120,134,123,111,138,126],
[135,133,142,128,130,0,123,137,127,152,129],
[115,124,118,124,116,127,0,137,109,135,120],
[105,119,116,115,127,113,113,0,114,140,112],
[132,130,136,130,139,123,141,136,0,145,143],
[111,115,110,107,112,98,115,110,105,0,99],
[129,135,135,137,124,121,130,138,107,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,103,126,100,113,110,119,111,115,119],
[138,0,125,132,129,121,108,134,118,125,124],
[147,125,0,138,124,126,129,118,122,135,133],
[124,118,112,0,113,121,114,127,122,126,132],
[150,121,126,137,0,134,123,141,137,132,147],
[137,129,124,129,116,0,119,135,127,134,142],
[140,142,121,136,127,131,0,141,129,138,131],
[131,116,132,123,109,115,109,0,110,126,123],
[139,132,128,128,113,123,121,140,0,146,129],
[135,125,115,124,118,116,112,124,104,0,120],
[131,126,117,118,103,108,119,127,121,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,121,110,123,129,119,119,109,113,140],
[123,0,135,123,110,131,101,127,127,103,148],
[129,115,0,122,111,127,112,111,139,138,138],
[140,127,128,0,126,146,127,125,104,119,153],
[127,140,139,124,0,144,126,136,127,131,171],
[121,119,123,104,106,0,96,127,115,129,132],
[131,149,138,123,124,154,0,138,129,140,151],
[131,123,139,125,114,123,112,0,137,124,129],
[141,123,111,146,123,135,121,113,0,126,141],
[137,147,112,131,119,121,110,126,124,0,153],
[110,102,112,97,79,118,99,121,109,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,112,130,106,132,133,123,125,112,134],
[129,0,132,132,121,130,132,133,141,122,128],
[138,118,0,136,118,121,126,118,139,112,138],
[120,118,114,0,113,128,114,116,126,117,126],
[144,129,132,137,0,132,114,130,140,124,136],
[118,120,129,122,118,0,125,119,138,96,135],
[117,118,124,136,136,125,0,118,132,125,122],
[127,117,132,134,120,131,132,0,132,118,125],
[125,109,111,124,110,112,118,118,0,109,126],
[138,128,138,133,126,154,125,132,141,0,148],
[116,122,112,124,114,115,128,125,124,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,104,131,123,114,116,118,113,122,123],
[135,0,127,132,128,135,122,130,129,127,132],
[146,123,0,139,136,123,139,130,133,130,138],
[119,118,111,0,117,118,125,119,118,122,114],
[127,122,114,133,0,121,114,126,118,129,127],
[136,115,127,132,129,0,123,130,130,136,135],
[134,128,111,125,136,127,0,124,119,132,128],
[132,120,120,131,124,120,126,0,118,135,135],
[137,121,117,132,132,120,131,132,0,132,130],
[128,123,120,128,121,114,118,115,118,0,130],
[127,118,112,136,123,115,122,115,120,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,123,122,117,88,98,147,147,127,96],
[146,0,141,143,138,127,141,158,148,160,122],
[127,109,0,127,123,93,111,139,155,121,121],
[128,107,123,0,137,120,127,150,150,136,113],
[133,112,127,113,0,101,117,118,151,123,104],
[162,123,157,130,149,0,136,181,172,138,145],
[152,109,139,123,133,114,0,160,140,133,112],
[103,92,111,100,132,69,90,0,137,114,91],
[103,102,95,100,99,78,110,113,0,97,114],
[123,90,129,114,127,112,117,136,153,0,113],
[154,128,129,137,146,105,138,159,136,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,128,135,124,135,132,127,144,143,118],
[113,0,120,119,117,119,119,115,124,123,113],
[122,130,0,124,122,127,133,122,135,130,124],
[115,131,126,0,125,128,135,123,129,127,117],
[126,133,128,125,0,127,124,126,126,144,122],
[115,131,123,122,123,0,115,120,125,136,104],
[118,131,117,115,126,135,0,123,119,134,120],
[123,135,128,127,124,130,127,0,133,135,126],
[106,126,115,121,124,125,131,117,0,132,116],
[107,127,120,123,106,114,116,115,118,0,113],
[132,137,126,133,128,146,130,124,134,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,142,126,118,144,129,133,113,134,125],
[117,0,126,118,103,133,112,109,112,113,116],
[108,124,0,121,113,137,122,122,117,121,119],
[124,132,129,0,112,138,130,132,125,129,117],
[132,147,137,138,0,148,131,136,137,119,123],
[106,117,113,112,102,0,104,105,106,106,95],
[121,138,128,120,119,146,0,125,136,124,116],
[117,141,128,118,114,145,125,0,112,128,139],
[137,138,133,125,113,144,114,138,0,127,120],
[116,137,129,121,131,144,126,122,123,0,129],
[125,134,131,133,127,155,134,111,130,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,161,145,133,121,163,146,150,130,134],
[119,0,115,125,106,95,118,123,95,93,103],
[89,135,0,116,119,102,112,110,101,102,104],
[105,125,134,0,136,110,136,101,110,125,121],
[117,144,131,114,0,114,118,115,113,117,136],
[129,155,148,140,136,0,138,128,130,117,130],
[87,132,138,114,132,112,0,123,106,91,126],
[104,127,140,149,135,122,127,0,129,118,103],
[100,155,149,140,137,120,144,121,0,153,129],
[120,157,148,125,133,133,159,132,97,0,150],
[116,147,146,129,114,120,124,147,121,100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,125,145,126,134,96,124,115,133,115],
[117,0,116,129,109,121,126,126,111,104,113],
[125,134,0,139,122,134,110,146,114,121,114],
[105,121,111,0,127,119,95,121,105,112,118],
[124,141,128,123,0,105,102,121,125,126,112],
[116,129,116,131,145,0,106,121,126,131,118],
[154,124,140,155,148,144,0,154,115,143,137],
[126,124,104,129,129,129,96,0,89,115,118],
[135,139,136,145,125,124,135,161,0,135,139],
[117,146,129,138,124,119,107,135,115,0,130],
[135,137,136,132,138,132,113,132,111,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 250, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_11_250.csv", index=False, header=False)