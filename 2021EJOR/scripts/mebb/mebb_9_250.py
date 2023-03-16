
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,123,113,117,138,111,96,121,124],
[127,0,105,110,121,114,116,113,105],
[137,145,0,130,125,118,136,156,127],
[133,140,120,0,124,127,121,127,112],
[112,129,125,126,0,121,121,128,139],
[139,136,132,123,129,0,124,146,135],
[154,134,114,129,129,126,0,141,130],
[129,137,94,123,122,104,109,0,107],
[126,145,123,138,111,115,120,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,130,130,127,126,141,124,125],
[120,0,124,127,120,113,117,118,118],
[120,126,0,125,126,105,128,126,118],
[120,123,125,0,124,121,116,125,120],
[123,130,124,126,0,121,120,122,125],
[124,137,145,129,129,0,126,135,134],
[109,133,122,134,130,124,0,122,126],
[126,132,124,125,128,115,128,0,117],
[125,132,132,130,125,116,124,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,162,114,130,158,146,130,122],
[100,0,122,112,119,104,122,115,112],
[88,128,0,133,110,116,141,114,113],
[136,138,117,0,117,128,161,132,131],
[120,131,140,133,0,140,133,124,105],
[92,146,134,122,110,0,114,95,102],
[104,128,109,89,117,136,0,111,122],
[120,135,136,118,126,155,139,0,132],
[128,138,137,119,145,148,128,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,133,136,119,129,122,130,143],
[133,0,138,138,118,130,116,125,141],
[117,112,0,131,115,113,113,113,127],
[114,112,119,0,116,121,122,118,126],
[131,132,135,134,0,156,129,125,145],
[121,120,137,129,94,0,118,117,119],
[128,134,137,128,121,132,0,129,138],
[120,125,137,132,125,133,121,0,125],
[107,109,123,124,105,131,112,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,176,197,141,153,173,172,137,119],
[74,0,112,104,114,113,146,108,119],
[53,138,0,107,91,83,138,99,68],
[109,146,143,0,126,137,147,146,124],
[97,136,159,124,0,80,126,108,93],
[77,137,167,113,170,0,147,116,119],
[78,104,112,103,124,103,0,95,62],
[113,142,151,104,142,134,155,0,130],
[131,131,182,126,157,131,188,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,118,161,110,94,118,133,131],
[115,0,109,123,138,129,101,136,138],
[132,141,0,149,108,92,72,142,148],
[89,127,101,0,124,86,84,104,115],
[140,112,142,126,0,102,134,172,130],
[156,121,158,164,148,0,132,177,170],
[132,149,178,166,116,118,0,134,158],
[117,114,108,146,78,73,116,0,143],
[119,112,102,135,120,80,92,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,126,122,130,127,138,149,149],
[132,0,115,134,128,148,134,168,130],
[124,135,0,142,138,142,125,149,142],
[128,116,108,0,132,125,119,143,117],
[120,122,112,118,0,118,112,140,113],
[123,102,108,125,132,0,127,140,127],
[112,116,125,131,138,123,0,137,129],
[101,82,101,107,110,110,113,0,117],
[101,120,108,133,137,123,121,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,122,141,134,124,137,143,134],
[117,0,130,122,124,113,126,112,115],
[128,120,0,129,129,129,137,143,132],
[109,128,121,0,125,111,144,137,128],
[116,126,121,125,0,109,137,138,137],
[126,137,121,139,141,0,143,138,137],
[113,124,113,106,113,107,0,114,126],
[107,138,107,113,112,112,136,0,121],
[116,135,118,122,113,113,124,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,116,114,125,116,119,111,113],
[125,0,123,124,123,122,123,118,114],
[134,127,0,125,123,125,119,129,123],
[136,126,125,0,130,121,104,112,110],
[125,127,127,120,0,110,125,112,114],
[134,128,125,129,140,0,125,127,123],
[131,127,131,146,125,125,0,118,129],
[139,132,121,138,138,123,132,0,129],
[137,136,127,140,136,127,121,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,94,78,113,88,78,83,106],
[130,0,138,116,130,97,72,136,141],
[156,112,0,110,142,123,112,136,113],
[172,134,140,0,162,140,130,108,121],
[137,120,108,88,0,126,76,134,125],
[162,153,127,110,124,0,69,142,118],
[172,178,138,120,174,181,0,147,150],
[167,114,114,142,116,108,103,0,129],
[144,109,137,129,125,132,100,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,133,130,140,135,136,135,115],
[123,0,130,123,134,117,127,123,116],
[117,120,0,118,134,123,128,131,115],
[120,127,132,0,130,120,128,123,108],
[110,116,116,120,0,117,120,117,112],
[115,133,127,130,133,0,131,122,115],
[114,123,122,122,130,119,0,121,116],
[115,127,119,127,133,128,129,0,125],
[135,134,135,142,138,135,134,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,130,132,124,132,132,143,110],
[129,0,150,119,131,141,128,151,144],
[120,100,0,132,126,119,135,146,120],
[118,131,118,0,107,134,134,156,119],
[126,119,124,143,0,120,130,134,112],
[118,109,131,116,130,0,124,134,128],
[118,122,115,116,120,126,0,143,131],
[107,99,104,94,116,116,107,0,117],
[140,106,130,131,138,122,119,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,173,65,76,108,76,39,108],
[133,0,148,105,148,130,146,68,157],
[77,102,0,77,126,131,88,39,156],
[185,145,173,0,183,93,92,41,93],
[174,102,124,67,0,81,70,68,93],
[142,120,119,157,169,0,119,82,172],
[174,104,162,158,180,131,0,131,131],
[211,182,211,209,182,168,119,0,168],
[142,93,94,157,157,78,119,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,110,122,140,115,130,123,132],
[122,0,129,129,120,124,151,121,116],
[140,121,0,121,146,141,150,133,136],
[128,121,129,0,120,134,141,122,123],
[110,130,104,130,0,131,136,107,113],
[135,126,109,116,119,0,129,114,112],
[120,99,100,109,114,121,0,110,109],
[127,129,117,128,143,136,140,0,116],
[118,134,114,127,137,138,141,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,107,114,108,110,142,124,105],
[146,0,124,102,116,131,131,120,129],
[143,126,0,127,119,141,126,129,130],
[136,148,123,0,125,140,141,135,129],
[142,134,131,125,0,138,127,133,116],
[140,119,109,110,112,0,124,116,119],
[108,119,124,109,123,126,0,136,121],
[126,130,121,115,117,134,114,0,122],
[145,121,120,121,134,131,129,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,135,125,125,130,136,114,136],
[124,0,113,115,116,117,126,113,118],
[115,137,0,98,118,118,137,121,122],
[125,135,152,0,133,136,140,133,127],
[125,134,132,117,0,108,128,115,128],
[120,133,132,114,142,0,124,110,122],
[114,124,113,110,122,126,0,106,114],
[136,137,129,117,135,140,144,0,127],
[114,132,128,123,122,128,136,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,115,119,116,116,120,113,110],
[138,0,126,125,120,118,133,134,134],
[135,124,0,140,116,127,120,124,123],
[131,125,110,0,112,109,131,114,117],
[134,130,134,138,0,110,141,123,113],
[134,132,123,141,140,0,129,124,116],
[130,117,130,119,109,121,0,106,115],
[137,116,126,136,127,126,144,0,130],
[140,116,127,133,137,134,135,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,130,129,124,139,127,136,134],
[111,0,124,117,116,119,107,134,134],
[120,126,0,134,122,140,112,138,144],
[121,133,116,0,125,136,125,138,138],
[126,134,128,125,0,129,113,140,131],
[111,131,110,114,121,0,109,135,119],
[123,143,138,125,137,141,0,148,140],
[114,116,112,112,110,115,102,0,125],
[116,116,106,112,119,131,110,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,126,138,138,134,137,142,143],
[133,0,124,138,119,142,142,145,119],
[124,126,0,139,114,133,135,136,129],
[112,112,111,0,118,112,133,128,111],
[112,131,136,132,0,132,132,128,144],
[116,108,117,138,118,0,132,134,115],
[113,108,115,117,118,118,0,117,119],
[108,105,114,122,122,116,133,0,122],
[107,131,121,139,106,135,131,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,101,114,96,107,118,114,116],
[141,0,98,131,108,127,123,126,114],
[149,152,0,132,114,142,116,133,117],
[136,119,118,0,107,126,108,127,105],
[154,142,136,143,0,136,115,136,140],
[143,123,108,124,114,0,126,138,135],
[132,127,134,142,135,124,0,114,105],
[136,124,117,123,114,112,136,0,116],
[134,136,133,145,110,115,145,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,123,120,128,119,105,106,119],
[135,0,137,119,121,119,126,121,115],
[127,113,0,133,121,119,116,109,122],
[130,131,117,0,115,128,101,106,118],
[122,129,129,135,0,118,123,114,112],
[131,131,131,122,132,0,122,111,130],
[145,124,134,149,127,128,0,131,134],
[144,129,141,144,136,139,119,0,120],
[131,135,128,132,138,120,116,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,123,114,126,132,131,123,115],
[122,0,127,118,111,121,121,115,128],
[127,123,0,123,132,129,119,135,120],
[136,132,127,0,128,134,137,121,126],
[124,139,118,122,0,128,121,120,114],
[118,129,121,116,122,0,127,120,121],
[119,129,131,113,129,123,0,125,116],
[127,135,115,129,130,130,125,0,131],
[135,122,130,124,136,129,134,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,71,99,74,104,89,118,83],
[126,0,95,147,92,147,114,148,86],
[179,155,0,127,145,150,120,122,113],
[151,103,123,0,113,129,84,92,94],
[176,158,105,137,0,203,103,170,130],
[146,103,100,121,47,0,95,103,93],
[161,136,130,166,147,155,0,144,125],
[132,102,128,158,80,147,106,0,74],
[167,164,137,156,120,157,125,176,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,152,166,163,129,135,107,123],
[87,0,131,141,136,104,100,84,126],
[98,119,0,124,140,123,130,134,126],
[84,109,126,0,156,121,142,128,125],
[87,114,110,94,0,118,106,81,85],
[121,146,127,129,132,0,131,78,140],
[115,150,120,108,144,119,0,133,132],
[143,166,116,122,169,172,117,0,131],
[127,124,124,125,165,110,118,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,162,128,132,144,152,122,151],
[108,0,123,104,122,138,133,103,128],
[88,127,0,106,108,126,117,128,116],
[122,146,144,0,147,157,145,133,146],
[118,128,142,103,0,151,141,119,136],
[106,112,124,93,99,0,132,105,116],
[98,117,133,105,109,118,0,113,113],
[128,147,122,117,131,145,137,0,133],
[99,122,134,104,114,134,137,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,109,112,116,118,124,111,115],
[131,0,111,111,121,119,119,128,125],
[141,139,0,125,128,129,128,138,129],
[138,139,125,0,130,135,142,137,129],
[134,129,122,120,0,126,120,124,128],
[132,131,121,115,124,0,140,129,134],
[126,131,122,108,130,110,0,126,126],
[139,122,112,113,126,121,124,0,122],
[135,125,121,121,122,116,124,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,130,147,125,151,135,128,128],
[108,0,126,127,123,128,118,121,116],
[120,124,0,135,122,140,128,115,126],
[103,123,115,0,108,122,114,111,108],
[125,127,128,142,0,132,120,126,122],
[99,122,110,128,118,0,115,117,106],
[115,132,122,136,130,135,0,132,132],
[122,129,135,139,124,133,118,0,122],
[122,134,124,142,128,144,118,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,154,128,125,166,142,137,140],
[128,0,169,118,118,161,143,127,116],
[96,81,0,80,113,114,124,112,101],
[122,132,170,0,133,166,151,162,124],
[125,132,137,117,0,127,130,120,116],
[84,89,136,84,123,0,102,125,88],
[108,107,126,99,120,148,0,116,93],
[113,123,138,88,130,125,134,0,110],
[110,134,149,126,134,162,157,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,155,118,126,130,125,130,146],
[107,0,106,112,121,110,103,112,110],
[95,144,0,109,120,109,100,124,132],
[132,138,141,0,138,136,109,145,126],
[124,129,130,112,0,106,109,119,126],
[120,140,141,114,144,0,129,131,132],
[125,147,150,141,141,121,0,134,154],
[120,138,126,105,131,119,116,0,121],
[104,140,118,124,124,118,96,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,135,121,117,125,135,141,135],
[127,0,138,130,122,131,136,144,130],
[115,112,0,132,128,121,124,136,124],
[129,120,118,0,120,133,130,130,111],
[133,128,122,130,0,134,136,149,123],
[125,119,129,117,116,0,139,138,119],
[115,114,126,120,114,111,0,133,110],
[109,106,114,120,101,112,117,0,109],
[115,120,126,139,127,131,140,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,43,186,53,78,96,150,110],
[169,0,129,199,134,115,185,166,172],
[207,121,0,239,119,134,147,196,176],
[64,51,11,0,83,59,80,56,54],
[197,116,131,167,0,148,122,204,167],
[172,135,116,191,102,0,137,159,151],
[154,65,103,170,128,113,0,194,134],
[100,84,54,194,46,91,56,0,99],
[140,78,74,196,83,99,116,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,142,118,124,123,134,126,133],
[122,0,122,107,130,120,116,105,114],
[108,128,0,106,125,108,127,104,129],
[132,143,144,0,140,125,140,139,154],
[126,120,125,110,0,117,118,118,128],
[127,130,142,125,133,0,147,126,144],
[116,134,123,110,132,103,0,115,124],
[124,145,146,111,132,124,135,0,129],
[117,136,121,96,122,106,126,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,168,148,117,154,135,147,134,139],
[82,0,95,109,126,118,112,113,111],
[102,155,0,129,154,131,155,128,159],
[133,141,121,0,134,137,131,126,129],
[96,124,96,116,0,109,132,104,109],
[115,132,119,113,141,0,115,88,134],
[103,138,95,119,118,135,0,108,107],
[116,137,122,124,146,162,142,0,127],
[111,139,91,121,141,116,143,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,135,108,121,126,133,119,109],
[130,0,123,123,132,131,144,126,116],
[115,127,0,122,127,131,130,120,127],
[142,127,128,0,130,131,135,135,119],
[129,118,123,120,0,125,122,119,131],
[124,119,119,119,125,0,126,112,115],
[117,106,120,115,128,124,0,107,116],
[131,124,130,115,131,138,143,0,130],
[141,134,123,131,119,135,134,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,127,121,134,134,138,124,126],
[114,0,124,123,128,130,139,123,122],
[123,126,0,122,114,125,135,125,122],
[129,127,128,0,114,130,134,128,122],
[116,122,136,136,0,129,132,136,116],
[116,120,125,120,121,0,124,125,113],
[112,111,115,116,118,126,0,103,106],
[126,127,125,122,114,125,147,0,115],
[124,128,128,128,134,137,144,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,97,162,122,138,81,96,141],
[146,0,131,154,145,164,153,116,165],
[153,119,0,118,131,144,93,79,145],
[88,96,132,0,90,134,88,69,110],
[128,105,119,160,0,137,98,129,145],
[112,86,106,116,113,0,64,90,109],
[169,97,157,162,152,186,0,92,149],
[154,134,171,181,121,160,158,0,161],
[109,85,105,140,105,141,101,89,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,109,116,123,97,108,135,128],
[127,0,102,109,124,107,114,120,148],
[141,148,0,146,124,128,137,152,149],
[134,141,104,0,95,100,116,131,133],
[127,126,126,155,0,114,112,140,126],
[153,143,122,150,136,0,125,161,126],
[142,136,113,134,138,125,0,156,132],
[115,130,98,119,110,89,94,0,118],
[122,102,101,117,124,124,118,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,121,147,127,130,122,147,124],
[126,0,119,131,122,131,120,137,128],
[129,131,0,140,131,130,119,131,126],
[103,119,110,0,115,117,122,129,119],
[123,128,119,135,0,130,115,126,129],
[120,119,120,133,120,0,117,122,127],
[128,130,131,128,135,133,0,133,123],
[103,113,119,121,124,128,117,0,117],
[126,122,124,131,121,123,127,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,160,135,136,112,121,136,130],
[138,0,150,117,144,128,151,136,113],
[90,100,0,136,126,92,117,98,111],
[115,133,114,0,129,116,121,115,98],
[114,106,124,121,0,107,110,110,95],
[138,122,158,134,143,0,138,136,128],
[129,99,133,129,140,112,0,121,112],
[114,114,152,135,140,114,129,0,115],
[120,137,139,152,155,122,138,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,125,118,127,136,123,137,112],
[135,0,127,119,148,131,146,143,139],
[125,123,0,121,139,136,133,129,121],
[132,131,129,0,129,136,132,123,137],
[123,102,111,121,0,129,107,130,112],
[114,119,114,114,121,0,127,114,120],
[127,104,117,118,143,123,0,125,135],
[113,107,121,127,120,136,125,0,117],
[138,111,129,113,138,130,115,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,132,122,129,134,121,129,136],
[123,0,145,131,127,137,139,117,125],
[118,105,0,118,109,116,111,107,114],
[128,119,132,0,124,121,118,118,122],
[121,123,141,126,0,136,117,130,127],
[116,113,134,129,114,0,113,108,119],
[129,111,139,132,133,137,0,125,138],
[121,133,143,132,120,142,125,0,129],
[114,125,136,128,123,131,112,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,123,158,132,143,144,128,141],
[116,0,116,140,110,128,139,138,128],
[127,134,0,137,143,113,141,137,160],
[92,110,113,0,108,106,113,131,135],
[118,140,107,142,0,124,122,136,141],
[107,122,137,144,126,0,141,140,143],
[106,111,109,137,128,109,0,129,139],
[122,112,113,119,114,110,121,0,127],
[109,122,90,115,109,107,111,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,111,109,67,142,111,48,123],
[139,0,70,124,100,128,70,120,90],
[139,180,0,163,122,161,136,153,188],
[141,126,87,0,130,130,130,153,161],
[183,150,128,120,0,220,217,162,163],
[108,122,89,120,30,0,42,122,138],
[139,180,114,120,33,208,0,104,172],
[202,130,97,97,88,128,146,0,146],
[127,160,62,89,87,112,78,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,123,132,141,126,138,122,106],
[115,0,126,125,115,129,117,118,112],
[127,124,0,111,142,115,133,125,123],
[118,125,139,0,113,125,124,112,122],
[109,135,108,137,0,109,124,97,114],
[124,121,135,125,141,0,142,103,125],
[112,133,117,126,126,108,0,116,108],
[128,132,125,138,153,147,134,0,123],
[144,138,127,128,136,125,142,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,115,121,96,95,113,86,99],
[156,0,146,142,139,142,151,122,129],
[135,104,0,125,132,131,138,106,123],
[129,108,125,0,77,114,123,116,107],
[154,111,118,173,0,104,130,127,128],
[155,108,119,136,146,0,139,127,135],
[137,99,112,127,120,111,0,131,123],
[164,128,144,134,123,123,119,0,123],
[151,121,127,143,122,115,127,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,109,172,160,152,169,141,128],
[98,0,104,178,186,126,160,127,147],
[141,146,0,138,172,138,171,113,131],
[78,72,112,0,141,137,139,134,121],
[90,64,78,109,0,130,154,114,131],
[98,124,112,113,120,0,141,128,146],
[81,90,79,111,96,109,0,122,97],
[109,123,137,116,136,122,128,0,118],
[122,103,119,129,119,104,153,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,114,118,130,125,120,128,121],
[126,0,115,129,129,111,116,125,114],
[136,135,0,132,137,122,118,125,120],
[132,121,118,0,142,114,126,117,112],
[120,121,113,108,0,117,105,113,107],
[125,139,128,136,133,0,119,117,125],
[130,134,132,124,145,131,0,125,116],
[122,125,125,133,137,133,125,0,121],
[129,136,130,138,143,125,134,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,123,124,130,116,139,113,121],
[132,0,123,117,122,132,136,126,120],
[127,127,0,124,102,121,124,125,125],
[126,133,126,0,125,117,136,126,114],
[120,128,148,125,0,131,148,126,122],
[134,118,129,133,119,0,139,129,127],
[111,114,126,114,102,111,0,116,112],
[137,124,125,124,124,121,134,0,130],
[129,130,125,136,128,123,138,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,114,126,119,130,121,134,117],
[117,0,109,113,115,145,105,130,135],
[136,141,0,125,133,123,126,142,125],
[124,137,125,0,130,138,118,141,126],
[131,135,117,120,0,130,124,149,126],
[120,105,127,112,120,0,107,145,113],
[129,145,124,132,126,143,0,143,122],
[116,120,108,109,101,105,107,0,114],
[133,115,125,124,124,137,128,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,138,133,135,147,128,118,140],
[119,0,120,152,114,159,122,129,134],
[112,130,0,118,109,156,127,120,127],
[117,98,132,0,126,150,125,130,118],
[115,136,141,124,0,164,126,126,136],
[103,91,94,100,86,0,95,108,103],
[122,128,123,125,124,155,0,126,122],
[132,121,130,120,124,142,124,0,128],
[110,116,123,132,114,147,128,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,116,131,162,141,133,99,109],
[106,0,120,122,133,119,144,115,120],
[134,130,0,127,141,120,140,108,110],
[119,128,123,0,143,116,137,101,108],
[88,117,109,107,0,96,132,92,111],
[109,131,130,134,154,0,139,128,138],
[117,106,110,113,118,111,0,90,105],
[151,135,142,149,158,122,160,0,131],
[141,130,140,142,139,112,145,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,142,139,113,94,122,135,155],
[135,0,112,108,106,116,110,114,140],
[108,138,0,120,106,104,126,137,146],
[111,142,130,0,140,136,111,144,169],
[137,144,144,110,0,156,122,133,172],
[156,134,146,114,94,0,142,137,151],
[128,140,124,139,128,108,0,143,178],
[115,136,113,106,117,113,107,0,142],
[95,110,104,81,78,99,72,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,92,114,91,77,87,124,89],
[107,0,123,129,52,86,94,92,87],
[158,127,0,170,88,94,115,125,123],
[136,121,80,0,143,112,97,92,73],
[159,198,162,107,0,110,136,156,141],
[173,164,156,138,140,0,109,159,124],
[163,156,135,153,114,141,0,123,160],
[126,158,125,158,94,91,127,0,120],
[161,163,127,177,109,126,90,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,80,97,75,94,115,114,133],
[152,0,110,92,97,131,117,137,126],
[170,140,0,125,99,117,160,154,158],
[153,158,125,0,165,111,135,161,145],
[175,153,151,85,0,142,146,140,144],
[156,119,133,139,108,0,126,164,138],
[135,133,90,115,104,124,0,141,142],
[136,113,96,89,110,86,109,0,99],
[117,124,92,105,106,112,108,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,113,132,135,138,117,129,129],
[112,0,109,117,108,108,109,122,109],
[137,141,0,141,121,131,107,137,119],
[118,133,109,0,113,129,101,134,94],
[115,142,129,137,0,131,108,130,126],
[112,142,119,121,119,0,105,133,102],
[133,141,143,149,142,145,0,143,110],
[121,128,113,116,120,117,107,0,90],
[121,141,131,156,124,148,140,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,99,119,150,118,156,116,135],
[114,0,111,105,125,94,145,100,113],
[151,139,0,155,147,144,160,118,162],
[131,145,95,0,156,153,179,99,163],
[100,125,103,94,0,91,132,101,141],
[132,156,106,97,159,0,175,134,167],
[94,105,90,71,118,75,0,74,108],
[134,150,132,151,149,116,176,0,180],
[115,137,88,87,109,83,142,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,135,148,159,144,139,137,125],
[107,0,134,127,133,134,120,99,108],
[115,116,0,137,144,117,96,117,102],
[102,123,113,0,122,130,109,113,107],
[91,117,106,128,0,121,97,95,101],
[106,116,133,120,129,0,110,112,105],
[111,130,154,141,153,140,0,123,104],
[113,151,133,137,155,138,127,0,135],
[125,142,148,143,149,145,146,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,123,123,107,146,94,109,128],
[129,0,120,134,102,123,87,121,109],
[127,130,0,119,116,143,92,143,126],
[127,116,131,0,133,167,101,137,137],
[143,148,134,117,0,170,100,126,142],
[104,127,107,83,80,0,89,116,113],
[156,163,158,149,150,161,0,130,125],
[141,129,107,113,124,134,120,0,121],
[122,141,124,113,108,137,125,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,137,137,137,125,134,133,123],
[132,0,133,154,140,130,119,126,139],
[113,117,0,138,131,115,114,96,116],
[113,96,112,0,135,111,107,100,89],
[113,110,119,115,0,129,109,109,97],
[125,120,135,139,121,0,108,100,110],
[116,131,136,143,141,142,0,134,140],
[117,124,154,150,141,150,116,0,137],
[127,111,134,161,153,140,110,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,119,113,124,124,136,126,128],
[131,0,128,133,127,136,137,124,132],
[131,122,0,119,129,122,126,118,114],
[137,117,131,0,141,121,138,143,119],
[126,123,121,109,0,116,118,119,111],
[126,114,128,129,134,0,143,118,122],
[114,113,124,112,132,107,0,116,107],
[124,126,132,107,131,132,134,0,123],
[122,118,136,131,139,128,143,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,129,94,120,134,124,135,114],
[130,0,124,129,127,114,122,128,120],
[121,126,0,112,111,110,103,118,113],
[156,121,138,0,126,134,126,137,123],
[130,123,139,124,0,117,119,119,130],
[116,136,140,116,133,0,113,136,115],
[126,128,147,124,131,137,0,123,134],
[115,122,132,113,131,114,127,0,146],
[136,130,137,127,120,135,116,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,115,117,112,93,118,126,102],
[145,0,142,129,135,131,128,117,118],
[135,108,0,114,124,122,118,119,135],
[133,121,136,0,129,118,131,121,136],
[138,115,126,121,0,96,108,101,127],
[157,119,128,132,154,0,146,102,135],
[132,122,132,119,142,104,0,102,127],
[124,133,131,129,149,148,148,0,129],
[148,132,115,114,123,115,123,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,81,111,116,110,84,124,178,105],
[169,0,135,131,108,145,121,174,128],
[139,115,0,130,135,117,97,165,154],
[134,119,120,0,122,100,126,164,88],
[140,142,115,128,0,130,105,161,150],
[166,105,133,150,120,0,143,174,160],
[126,129,153,124,145,107,0,171,153],
[72,76,85,86,89,76,79,0,101],
[145,122,96,162,100,90,97,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,122,119,124,117,127,123,125],
[112,0,120,128,120,125,118,125,126],
[128,130,0,138,133,123,130,132,132],
[131,122,112,0,123,110,125,121,128],
[126,130,117,127,0,122,130,124,135],
[133,125,127,140,128,0,123,120,136],
[123,132,120,125,120,127,0,140,127],
[127,125,118,129,126,130,110,0,136],
[125,124,118,122,115,114,123,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,98,112,130,108,117,116,124],
[146,0,126,135,124,140,135,126,137],
[152,124,0,137,151,132,144,130,149],
[138,115,113,0,120,132,132,144,125],
[120,126,99,130,0,128,136,114,140],
[142,110,118,118,122,0,127,143,142],
[133,115,106,118,114,123,0,147,152],
[134,124,120,106,136,107,103,0,127],
[126,113,101,125,110,108,98,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,118,140,147,125,132,153,135],
[128,0,128,119,133,131,124,135,121],
[132,122,0,146,146,138,130,143,128],
[110,131,104,0,128,143,140,134,124],
[103,117,104,122,0,140,111,132,122],
[125,119,112,107,110,0,92,130,129],
[118,126,120,110,139,158,0,124,136],
[97,115,107,116,118,120,126,0,123],
[115,129,122,126,128,121,114,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,122,138,119,116,118,120,126],
[138,0,137,132,132,125,131,124,140],
[128,113,0,128,112,126,112,125,130],
[112,118,122,0,114,129,118,119,136],
[131,118,138,136,0,127,120,120,126],
[134,125,124,121,123,0,127,116,120],
[132,119,138,132,130,123,0,119,135],
[130,126,125,131,130,134,131,0,136],
[124,110,120,114,124,130,115,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,109,126,134,124,115,135,123],
[129,0,132,139,132,127,118,145,118],
[141,118,0,152,132,142,125,131,127],
[124,111,98,0,120,114,101,127,104],
[116,118,118,130,0,128,117,142,117],
[126,123,108,136,122,0,125,136,114],
[135,132,125,149,133,125,0,134,131],
[115,105,119,123,108,114,116,0,129],
[127,132,123,146,133,136,119,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,130,125,120,122,106,119,111],
[123,0,129,125,110,118,113,118,111],
[120,121,0,111,119,104,92,108,113],
[125,125,139,0,125,133,127,121,123],
[130,140,131,125,0,125,115,125,138],
[128,132,146,117,125,0,108,103,120],
[144,137,158,123,135,142,0,134,124],
[131,132,142,129,125,147,116,0,119],
[139,139,137,127,112,130,126,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,127,113,126,122,128,128,125],
[121,0,132,116,111,133,126,120,108],
[123,118,0,123,108,129,138,111,118],
[137,134,127,0,127,151,146,124,129],
[124,139,142,123,0,140,145,124,132],
[128,117,121,99,110,0,128,117,107],
[122,124,112,104,105,122,0,110,99],
[122,130,139,126,126,133,140,0,130],
[125,142,132,121,118,143,151,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,145,131,122,126,128,143,127],
[120,0,143,131,106,125,119,125,125],
[105,107,0,104,98,98,102,118,119],
[119,119,146,0,114,112,122,143,128],
[128,144,152,136,0,130,124,156,136],
[124,125,152,138,120,0,127,148,124],
[122,131,148,128,126,123,0,155,148],
[107,125,132,107,94,102,95,0,114],
[123,125,131,122,114,126,102,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,110,110,107,114,120,120,114],
[134,0,119,123,123,128,135,136,119],
[140,131,0,125,127,144,130,143,129],
[140,127,125,0,129,128,137,137,124],
[143,127,123,121,0,130,133,130,124],
[136,122,106,122,120,0,130,119,125],
[130,115,120,113,117,120,0,125,116],
[130,114,107,113,120,131,125,0,118],
[136,131,121,126,126,125,134,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,152,138,155,147,126,111,150],
[98,0,129,121,121,128,123,109,130],
[98,121,0,125,125,123,109,99,104],
[112,129,125,0,129,137,114,118,119],
[95,129,125,121,0,133,117,123,130],
[103,122,127,113,117,0,124,118,126],
[124,127,141,136,133,126,0,100,135],
[139,141,151,132,127,132,150,0,118],
[100,120,146,131,120,124,115,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,113,109,127,117,123,121,99],
[149,0,123,127,139,138,140,147,132],
[137,127,0,124,152,158,133,148,133],
[141,123,126,0,147,142,140,147,128],
[123,111,98,103,0,112,107,95,103],
[133,112,92,108,138,0,123,130,120],
[127,110,117,110,143,127,0,129,116],
[129,103,102,103,155,120,121,0,94],
[151,118,117,122,147,130,134,156,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,141,146,134,147,114,150,143],
[98,0,112,111,114,135,118,113,124],
[109,138,0,140,116,139,101,122,118],
[104,139,110,0,113,121,115,119,128],
[116,136,134,137,0,134,132,139,143],
[103,115,111,129,116,0,131,109,135],
[136,132,149,135,118,119,0,132,135],
[100,137,128,131,111,141,118,0,119],
[107,126,132,122,107,115,115,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,117,127,120,113,117,114,118],
[132,0,126,109,124,128,124,118,122],
[133,124,0,125,126,124,125,120,126],
[123,141,125,0,131,132,122,128,135],
[130,126,124,119,0,118,113,128,123],
[137,122,126,118,132,0,123,129,125],
[133,126,125,128,137,127,0,120,126],
[136,132,130,122,122,121,130,0,114],
[132,128,124,115,127,125,124,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,99,82,140,96,88,93,102],
[129,0,122,137,111,125,120,113,97],
[151,128,0,166,152,139,134,103,141],
[168,113,84,0,141,112,113,116,125],
[110,139,98,109,0,124,112,100,128],
[154,125,111,138,126,0,128,98,128],
[162,130,116,137,138,122,0,129,127],
[157,137,147,134,150,152,121,0,113],
[148,153,109,125,122,122,123,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,131,118,119,123,126,116,133],
[142,0,132,126,136,135,117,125,121],
[119,118,0,124,124,132,111,116,129],
[132,124,126,0,133,134,128,124,129],
[131,114,126,117,0,138,105,115,138],
[127,115,118,116,112,0,133,129,120],
[124,133,139,122,145,117,0,131,126],
[134,125,134,126,135,121,119,0,131],
[117,129,121,121,112,130,124,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,122,122,129,135,132,123,126],
[135,0,126,124,126,142,140,125,132],
[128,124,0,130,137,145,137,129,124],
[128,126,120,0,114,139,146,119,123],
[121,124,113,136,0,133,132,129,126],
[115,108,105,111,117,0,136,121,119],
[118,110,113,104,118,114,0,122,129],
[127,125,121,131,121,129,128,0,121],
[124,118,126,127,124,131,121,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,115,115,123,124,134,117,119],
[133,0,126,117,130,130,143,143,129],
[135,124,0,129,119,128,136,123,134],
[135,133,121,0,134,132,136,133,117],
[127,120,131,116,0,137,121,123,124],
[126,120,122,118,113,0,122,126,124],
[116,107,114,114,129,128,0,116,122],
[133,107,127,117,127,124,134,0,115],
[131,121,116,133,126,126,128,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,130,137,151,107,106,108,145],
[147,0,88,140,139,110,117,124,155],
[120,162,0,147,130,115,124,141,127],
[113,110,103,0,120,136,103,105,125],
[99,111,120,130,0,117,94,112,145],
[143,140,135,114,133,0,120,118,131],
[144,133,126,147,156,130,0,106,157],
[142,126,109,145,138,132,144,0,116],
[105,95,123,125,105,119,93,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,134,128,133,124,132,132,123],
[135,0,132,127,128,122,136,136,123],
[116,118,0,126,117,107,117,115,112],
[122,123,124,0,122,127,116,117,117],
[117,122,133,128,0,121,117,129,121],
[126,128,143,123,129,0,131,127,127],
[118,114,133,134,133,119,0,126,129],
[118,114,135,133,121,123,124,0,126],
[127,127,138,133,129,123,121,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,128,117,131,120,117,125,125],
[130,0,128,125,142,129,127,126,133],
[122,122,0,123,125,121,116,114,126],
[133,125,127,0,128,121,114,122,124],
[119,108,125,122,0,118,114,116,122],
[130,121,129,129,132,0,107,113,127],
[133,123,134,136,136,143,0,130,137],
[125,124,136,128,134,137,120,0,135],
[125,117,124,126,128,123,113,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,107,141,88,132,110,113,78],
[113,0,133,116,138,142,77,116,111],
[143,117,0,177,147,131,136,171,155],
[109,134,73,0,114,120,102,107,91],
[162,112,103,136,0,113,101,126,126],
[118,108,119,130,137,0,109,142,106],
[140,173,114,148,149,141,0,133,124],
[137,134,79,143,124,108,117,0,85],
[172,139,95,159,124,144,126,165,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,120,124,126,126,114,129,126],
[110,0,118,111,124,122,114,125,126],
[130,132,0,129,124,123,131,125,133],
[126,139,121,0,115,116,123,118,128],
[124,126,126,135,0,126,123,131,131],
[124,128,127,134,124,0,126,122,137],
[136,136,119,127,127,124,0,124,138],
[121,125,125,132,119,128,126,0,127],
[124,124,117,122,119,113,112,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,94,157,102,23,4,76,73],
[174,0,91,204,117,19,73,117,72],
[156,159,0,133,146,51,74,149,48],
[93,46,117,0,118,46,46,118,118],
[148,133,104,132,0,23,51,123,47],
[227,231,199,204,227,0,74,146,145],
[246,177,176,204,199,176,0,94,72],
[174,133,101,132,127,104,156,0,129],
[177,178,202,132,203,105,178,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,136,128,137,125,123,125,133],
[126,0,137,137,138,125,131,123,131],
[114,113,0,119,126,106,112,100,123],
[122,113,131,0,118,119,116,111,120],
[113,112,124,132,0,119,120,103,122],
[125,125,144,131,131,0,132,124,133],
[127,119,138,134,130,118,0,118,137],
[125,127,150,139,147,126,132,0,134],
[117,119,127,130,128,117,113,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,121,125,132,133,131,136,132],
[122,0,129,133,136,127,135,139,126],
[129,121,0,124,122,127,134,129,143],
[125,117,126,0,122,123,124,135,134],
[118,114,128,128,0,119,121,124,132],
[117,123,123,127,131,0,122,122,133],
[119,115,116,126,129,128,0,123,127],
[114,111,121,115,126,128,127,0,124],
[118,124,107,116,118,117,123,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,133,133,133,121,116,128,126],
[129,0,133,135,132,136,127,119,121],
[117,117,0,126,126,120,125,111,127],
[117,115,124,0,112,119,108,102,126],
[117,118,124,138,0,126,121,115,121],
[129,114,130,131,124,0,115,118,138],
[134,123,125,142,129,135,0,121,131],
[122,131,139,148,135,132,129,0,130],
[124,129,123,124,129,112,119,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,139,131,111,131,113,102,128],
[119,0,127,125,120,118,110,152,104],
[111,123,0,111,109,128,109,91,102],
[119,125,139,0,112,141,113,99,114],
[139,130,141,138,0,142,140,118,140],
[119,132,122,109,108,0,103,77,122],
[137,140,141,137,110,147,0,127,133],
[148,98,159,151,132,173,123,0,130],
[122,146,148,136,110,128,117,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,121,126,114,125,123,136,116],
[136,0,128,144,138,120,135,156,136],
[129,122,0,125,126,103,122,136,121],
[124,106,125,0,116,111,120,124,114],
[136,112,124,134,0,121,131,138,128],
[125,130,147,139,129,0,122,135,134],
[127,115,128,130,119,128,0,141,128],
[114,94,114,126,112,115,109,0,106],
[134,114,129,136,122,116,122,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,139,120,116,129,106,114,118],
[132,0,149,112,127,130,128,129,134],
[111,101,0,118,113,117,121,112,114],
[130,138,132,0,129,137,125,129,127],
[134,123,137,121,0,144,119,131,125],
[121,120,133,113,106,0,115,115,115],
[144,122,129,125,131,135,0,128,133],
[136,121,138,121,119,135,122,0,121],
[132,116,136,123,125,135,117,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,100,107,121,115,108,114,107],
[131,0,135,151,127,125,125,130,103],
[150,115,0,140,133,121,111,129,103],
[143,99,110,0,130,118,113,121,114],
[129,123,117,120,0,116,98,104,93],
[135,125,129,132,134,0,104,111,117],
[142,125,139,137,152,146,0,140,131],
[136,120,121,129,146,139,110,0,128],
[143,147,147,136,157,133,119,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,86,75,117,124,106,116,106],
[137,0,99,70,82,101,92,102,104],
[164,151,0,118,145,141,141,136,130],
[175,180,132,0,127,126,108,138,129],
[133,168,105,123,0,110,108,134,148],
[126,149,109,124,140,0,138,129,140],
[144,158,109,142,142,112,0,126,119],
[134,148,114,112,116,121,124,0,101],
[144,146,120,121,102,110,131,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,129,138,131,131,120,124,128],
[125,0,132,147,134,139,126,127,131],
[121,118,0,129,130,129,122,120,128],
[112,103,121,0,132,116,112,123,122],
[119,116,120,118,0,123,100,117,128],
[119,111,121,134,127,0,104,119,128],
[130,124,128,138,150,146,0,129,138],
[126,123,130,127,133,131,121,0,123],
[122,119,122,128,122,122,112,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,119,132,128,115,121,113,112],
[140,0,141,138,136,121,129,128,133],
[131,109,0,119,120,101,128,113,107],
[118,112,131,0,117,99,122,110,120],
[122,114,130,133,0,114,127,108,116],
[135,129,149,151,136,0,138,121,123],
[129,121,122,128,123,112,0,117,102],
[137,122,137,140,142,129,133,0,129],
[138,117,143,130,134,127,148,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,134,134,119,114,123,133,120],
[120,0,116,130,130,97,133,106,121],
[116,134,0,121,127,120,154,121,111],
[116,120,129,0,116,135,144,120,118],
[131,120,123,134,0,121,125,126,129],
[136,153,130,115,129,0,143,133,135],
[127,117,96,106,125,107,0,101,99],
[117,144,129,130,124,117,149,0,145],
[130,129,139,132,121,115,151,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,129,139,117,117,119,133,125],
[109,0,126,139,126,116,112,111,121],
[121,124,0,129,124,123,120,114,119],
[111,111,121,0,124,101,113,118,118],
[133,124,126,126,0,127,127,120,144],
[133,134,127,149,123,0,151,130,130],
[131,138,130,137,123,99,0,113,127],
[117,139,136,132,130,120,137,0,110],
[125,129,131,132,106,120,123,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,105,110,112,106,121,129,100],
[138,0,120,122,114,128,124,124,128],
[145,130,0,120,117,119,137,124,123],
[140,128,130,0,114,120,111,134,107],
[138,136,133,136,0,109,125,127,123],
[144,122,131,130,141,0,130,109,124],
[129,126,113,139,125,120,0,128,127],
[121,126,126,116,123,141,122,0,127],
[150,122,127,143,127,126,123,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,135,121,117,130,130,131,140],
[120,0,124,116,109,122,115,119,123],
[115,126,0,114,117,125,114,130,127],
[129,134,136,0,123,133,129,136,139],
[133,141,133,127,0,125,132,142,139],
[120,128,125,117,125,0,124,130,132],
[120,135,136,121,118,126,0,130,128],
[119,131,120,114,108,120,120,0,123],
[110,127,123,111,111,118,122,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,123,120,112,128,141,141,124],
[104,0,117,100,122,114,117,115,113],
[127,133,0,127,113,111,141,124,113],
[130,150,123,0,113,116,143,138,125],
[138,128,137,137,0,109,143,131,125],
[122,136,139,134,141,0,147,133,139],
[109,133,109,107,107,103,0,132,113],
[109,135,126,112,119,117,118,0,101],
[126,137,137,125,125,111,137,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,126,128,121,122,131,117,116],
[115,0,121,121,139,121,130,118,123],
[124,129,0,119,134,116,129,124,123],
[122,129,131,0,131,124,133,126,134],
[129,111,116,119,0,116,127,124,119],
[128,129,134,126,134,0,124,124,126],
[119,120,121,117,123,126,0,112,115],
[133,132,126,124,126,126,138,0,125],
[134,127,127,116,131,124,135,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,127,126,124,125,132,123,120],
[122,0,124,107,131,121,133,122,119],
[123,126,0,125,139,134,129,125,130],
[124,143,125,0,133,127,133,113,125],
[126,119,111,117,0,114,118,112,115],
[125,129,116,123,136,0,139,125,126],
[118,117,121,117,132,111,0,127,122],
[127,128,125,137,138,125,123,0,122],
[130,131,120,125,135,124,128,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,104,118,108,127,133,98,126],
[137,0,121,138,136,119,114,125,108],
[146,129,0,129,132,117,149,120,120],
[132,112,121,0,115,109,133,101,119],
[142,114,118,135,0,120,130,105,114],
[123,131,133,141,130,0,147,129,130],
[117,136,101,117,120,103,0,107,115],
[152,125,130,149,145,121,143,0,142],
[124,142,130,131,136,120,135,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,134,141,131,133,115,141,134],
[116,0,124,138,137,131,112,141,127],
[116,126,0,121,111,103,111,120,113],
[109,112,129,0,125,108,119,121,119],
[119,113,139,125,0,107,126,125,121],
[117,119,147,142,143,0,123,146,133],
[135,138,139,131,124,127,0,119,139],
[109,109,130,129,125,104,131,0,120],
[116,123,137,131,129,117,111,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,104,131,137,126,127,101,123],
[122,0,133,107,125,112,136,117,126],
[146,117,0,135,135,139,164,113,134],
[119,143,115,0,98,126,151,132,123],
[113,125,115,152,0,125,151,90,130],
[124,138,111,124,125,0,123,110,130],
[123,114,86,99,99,127,0,83,105],
[149,133,137,118,160,140,167,0,133],
[127,124,116,127,120,120,145,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,114,133,123,118,123,111,126],
[137,0,152,134,132,138,137,127,116],
[136,98,0,113,110,106,118,113,104],
[117,116,137,0,117,113,128,106,115],
[127,118,140,133,0,122,143,116,109],
[132,112,144,137,128,0,126,131,126],
[127,113,132,122,107,124,0,125,137],
[139,123,137,144,134,119,125,0,132],
[124,134,146,135,141,124,113,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,119,133,123,133,140,122,120],
[132,0,128,131,133,129,132,140,125],
[131,122,0,118,131,132,131,117,123],
[117,119,132,0,132,129,132,119,123],
[127,117,119,118,0,133,131,119,120],
[117,121,118,121,117,0,128,123,126],
[110,118,119,118,119,122,0,111,117],
[128,110,133,131,131,127,139,0,111],
[130,125,127,127,130,124,133,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,108,114,116,113,132,110,129],
[138,0,134,126,129,125,152,148,145],
[142,116,0,126,134,115,126,151,136],
[136,124,124,0,122,128,145,138,156],
[134,121,116,128,0,102,131,136,142],
[137,125,135,122,148,0,149,138,141],
[118,98,124,105,119,101,0,130,126],
[140,102,99,112,114,112,120,0,134],
[121,105,114,94,108,109,124,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,111,133,119,134,104,122,133],
[123,0,106,110,115,138,106,102,128],
[139,144,0,161,124,143,132,121,136],
[117,140,89,0,107,106,99,103,127],
[131,135,126,143,0,146,100,120,112],
[116,112,107,144,104,0,104,129,123],
[146,144,118,151,150,146,0,126,166],
[128,148,129,147,130,121,124,0,144],
[117,122,114,123,138,127,84,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,121,137,118,133,125,119,122],
[112,0,105,129,118,121,113,116,117],
[129,145,0,135,117,134,122,134,131],
[113,121,115,0,112,115,117,124,117],
[132,132,133,138,0,124,125,131,124],
[117,129,116,135,126,0,123,132,126],
[125,137,128,133,125,127,0,125,129],
[131,134,116,126,119,118,125,0,121],
[128,133,119,133,126,124,121,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,131,141,127,135,115,116],
[114,0,116,107,117,106,123,109,119],
[124,134,0,114,140,128,138,134,130],
[119,143,136,0,133,122,127,124,137],
[109,133,110,117,0,114,132,119,102],
[123,144,122,128,136,0,145,117,115],
[115,127,112,123,118,105,0,101,99],
[135,141,116,126,131,133,149,0,126],
[134,131,120,113,148,135,151,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,121,122,115,128,122,129,125],
[120,0,126,120,127,118,127,112,130],
[129,124,0,134,122,127,139,128,132],
[128,130,116,0,124,122,134,125,121],
[135,123,128,126,0,133,126,133,131],
[122,132,123,128,117,0,119,128,136],
[128,123,111,116,124,131,0,125,131],
[121,138,122,125,117,122,125,0,136],
[125,120,118,129,119,114,119,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,131,123,128,134,122,141,122],
[110,0,125,116,122,127,112,121,113],
[119,125,0,120,117,128,111,143,124],
[127,134,130,0,120,124,113,141,118],
[122,128,133,130,0,127,100,130,119],
[116,123,122,126,123,0,138,134,113],
[128,138,139,137,150,112,0,143,133],
[109,129,107,109,120,116,107,0,113],
[128,137,126,132,131,137,117,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,97,121,115,129,132,119,143],
[130,0,100,112,109,128,113,141,131],
[153,150,0,165,141,137,114,123,151],
[129,138,85,0,115,133,106,138,145],
[135,141,109,135,0,118,121,120,144],
[121,122,113,117,132,0,129,131,136],
[118,137,136,144,129,121,0,137,122],
[131,109,127,112,130,119,113,0,128],
[107,119,99,105,106,114,128,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,116,120,124,126,132,119,120],
[136,0,122,117,120,126,127,118,118],
[134,128,0,124,128,128,139,135,130],
[130,133,126,0,131,143,135,124,127],
[126,130,122,119,0,126,126,136,127],
[124,124,122,107,124,0,130,119,115],
[118,123,111,115,124,120,0,122,123],
[131,132,115,126,114,131,128,0,124],
[130,132,120,123,123,135,127,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,126,136,117,127,139,126,138],
[118,0,131,110,106,118,132,122,128],
[124,119,0,124,114,116,136,128,117],
[114,140,126,0,127,129,144,130,140],
[133,144,136,123,0,142,154,136,147],
[123,132,134,121,108,0,141,119,131],
[111,118,114,106,96,109,0,117,122],
[124,128,122,120,114,131,133,0,124],
[112,122,133,110,103,119,128,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,133,131,147,128,154,140,124],
[105,0,111,96,103,107,93,104,106],
[117,139,0,109,98,94,104,89,107],
[119,154,141,0,101,105,118,135,92],
[103,147,152,149,0,146,129,135,137],
[122,143,156,145,104,0,89,149,129],
[96,157,146,132,121,161,0,174,122],
[110,146,161,115,115,101,76,0,115],
[126,144,143,158,113,121,128,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,145,147,132,131,107,145,133],
[130,0,143,134,148,134,107,169,142],
[105,107,0,96,130,134,101,126,112],
[103,116,154,0,137,112,98,121,126],
[118,102,120,113,0,116,112,146,126],
[119,116,116,138,134,0,131,163,135],
[143,143,149,152,138,119,0,138,141],
[105,81,124,129,104,87,112,0,116],
[117,108,138,124,124,115,109,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,148,136,139,135,123,132,132],
[119,0,127,150,114,129,123,134,118],
[102,123,0,124,121,115,125,119,119],
[114,100,126,0,100,117,105,111,104],
[111,136,129,150,0,131,131,127,141],
[115,121,135,133,119,0,127,130,115],
[127,127,125,145,119,123,0,116,126],
[118,116,131,139,123,120,134,0,125],
[118,132,131,146,109,135,124,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,114,111,124,121,110,114,133],
[132,0,121,119,122,134,124,125,123],
[136,129,0,121,127,134,134,120,123],
[139,131,129,0,128,134,129,111,127],
[126,128,123,122,0,140,128,124,121],
[129,116,116,116,110,0,117,108,116],
[140,126,116,121,122,133,0,119,121],
[136,125,130,139,126,142,131,0,130],
[117,127,127,123,129,134,129,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,124,113,130,128,126,118,121],
[137,0,136,124,130,123,136,133,126],
[126,114,0,123,127,123,124,124,125],
[137,126,127,0,136,133,136,115,133],
[120,120,123,114,0,119,127,111,125],
[122,127,127,117,131,0,130,134,124],
[124,114,126,114,123,120,0,119,120],
[132,117,126,135,139,116,131,0,127],
[129,124,125,117,125,126,130,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,116,102,111,114,115,114,120],
[127,0,113,105,118,103,118,103,134],
[134,137,0,122,123,112,131,116,125],
[148,145,128,0,132,119,127,128,132],
[139,132,127,118,0,127,129,130,128],
[136,147,138,131,123,0,140,125,137],
[135,132,119,123,121,110,0,120,118],
[136,147,134,122,120,125,130,0,117],
[130,116,125,118,122,113,132,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,112,123,120,130,122,108,114],
[129,0,127,142,123,140,132,119,127],
[138,123,0,132,125,146,124,126,112],
[127,108,118,0,113,138,124,105,108],
[130,127,125,137,0,151,143,129,141],
[120,110,104,112,99,0,119,105,101],
[128,118,126,126,107,131,0,115,121],
[142,131,124,145,121,145,135,0,122],
[136,123,138,142,109,149,129,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,154,148,145,123,119,149,148],
[124,0,136,123,137,131,131,140,135],
[96,114,0,111,113,131,111,127,126],
[102,127,139,0,129,113,122,119,128],
[105,113,137,121,0,102,112,124,107],
[127,119,119,137,148,0,134,132,145],
[131,119,139,128,138,116,0,130,120],
[101,110,123,131,126,118,120,0,113],
[102,115,124,122,143,105,130,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,125,128,84,139,47,128,139],
[155,0,99,190,116,169,88,132,128],
[125,151,0,192,151,132,172,125,125],
[122,60,58,0,127,111,148,0,100],
[166,134,99,123,0,139,122,74,139],
[111,81,118,139,111,0,111,90,209],
[203,162,78,102,128,139,0,102,139],
[122,118,125,250,176,160,148,0,183],
[111,122,125,150,111,41,111,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,89,101,119,120,105,117,128],
[110,0,106,107,124,116,115,88,109],
[161,144,0,134,147,144,131,124,153],
[149,143,116,0,160,148,118,133,145],
[131,126,103,90,0,105,86,104,107],
[130,134,106,102,145,0,118,123,107],
[145,135,119,132,164,132,0,127,136],
[133,162,126,117,146,127,123,0,126],
[122,141,97,105,143,143,114,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,154,138,132,149,144,117,122,102],
[96,0,123,105,133,120,108,102,104],
[112,127,0,107,123,118,114,98,105],
[118,145,143,0,147,152,133,113,110],
[101,117,127,103,0,112,128,125,111],
[106,130,132,98,138,0,122,105,122],
[133,142,136,117,122,128,0,121,126],
[128,148,152,137,125,145,129,0,126],
[148,146,145,140,139,128,124,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,132,143,134,125,122,140,130],
[128,0,136,131,138,121,140,142,121],
[118,114,0,128,136,119,120,124,119],
[107,119,122,0,114,113,115,126,132],
[116,112,114,136,0,121,113,123,114],
[125,129,131,137,129,0,114,133,126],
[128,110,130,135,137,136,0,142,123],
[110,108,126,124,127,117,108,0,108],
[120,129,131,118,136,124,127,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,121,130,136,119,127,124,127],
[144,0,121,131,128,119,135,136,122],
[129,129,0,128,140,135,131,141,124],
[120,119,122,0,140,117,124,125,124],
[114,122,110,110,0,123,114,122,135],
[131,131,115,133,127,0,133,128,137],
[123,115,119,126,136,117,0,120,118],
[126,114,109,125,128,122,130,0,126],
[123,128,126,126,115,113,132,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,128,139,128,137,134,144,119],
[114,0,116,125,120,119,112,134,119],
[122,134,0,135,117,135,122,133,120],
[111,125,115,0,116,111,121,134,120],
[122,130,133,134,0,130,121,133,125],
[113,131,115,139,120,0,115,130,118],
[116,138,128,129,129,135,0,130,120],
[106,116,117,116,117,120,120,0,124],
[131,131,130,130,125,132,130,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,164,136,129,116,103,129,152],
[117,0,160,154,112,118,120,116,146],
[86,90,0,80,92,103,93,97,106],
[114,96,170,0,117,126,147,126,174],
[121,138,158,133,0,134,131,126,147],
[134,132,147,124,116,0,112,115,141],
[147,130,157,103,119,138,0,130,169],
[121,134,153,124,124,135,120,0,126],
[98,104,144,76,103,109,81,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,126,155,143,110,140,124,112],
[117,0,131,133,127,109,130,100,123],
[124,119,0,131,134,128,132,114,120],
[95,117,119,0,103,98,115,114,126],
[107,123,116,147,0,118,145,116,114],
[140,141,122,152,132,0,138,136,131],
[110,120,118,135,105,112,0,125,118],
[126,150,136,136,134,114,125,0,131],
[138,127,130,124,136,119,132,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,113,130,132,117,120,129,135],
[118,0,125,129,128,118,125,126,139],
[137,125,0,144,146,123,130,141,146],
[120,121,106,0,122,113,108,120,127],
[118,122,104,128,0,113,98,116,127],
[133,132,127,137,137,0,121,128,131],
[130,125,120,142,152,129,0,128,132],
[121,124,109,130,134,122,122,0,127],
[115,111,104,123,123,119,118,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,126,134,136,126,121,127,117],
[131,0,126,140,131,116,127,127,133],
[124,124,0,136,124,133,127,132,118],
[116,110,114,0,116,105,120,127,114],
[114,119,126,134,0,128,118,129,123],
[124,134,117,145,122,0,133,124,122],
[129,123,123,130,132,117,0,128,116],
[123,123,118,123,121,126,122,0,115],
[133,117,132,136,127,128,134,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,119,128,124,135,132,130,131],
[129,0,116,124,118,141,123,123,122],
[131,134,0,128,127,138,123,122,138],
[122,126,122,0,124,144,121,129,126],
[126,132,123,126,0,137,125,119,131],
[115,109,112,106,113,0,116,102,110],
[118,127,127,129,125,134,0,133,136],
[120,127,128,121,131,148,117,0,125],
[119,128,112,124,119,140,114,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,143,140,138,137,129,135,112],
[122,0,115,131,141,141,126,140,126],
[107,135,0,143,151,148,121,130,128],
[110,119,107,0,133,146,127,137,109],
[112,109,99,117,0,118,110,122,96],
[113,109,102,104,132,0,120,118,93],
[121,124,129,123,140,130,0,135,125],
[115,110,120,113,128,132,115,0,110],
[138,124,122,141,154,157,125,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,115,131,123,125,131,124,126],
[136,0,128,144,135,121,124,142,138],
[135,122,0,136,133,132,129,140,138],
[119,106,114,0,130,106,120,127,121],
[127,115,117,120,0,120,113,136,135],
[125,129,118,144,130,0,129,131,131],
[119,126,121,130,137,121,0,133,133],
[126,108,110,123,114,119,117,0,122],
[124,112,112,129,115,119,117,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,82,110,99,116,93,115,126],
[152,0,93,94,122,151,97,129,106],
[168,157,0,86,159,154,113,132,150],
[140,156,164,0,133,162,119,111,134],
[151,128,91,117,0,165,100,124,88],
[134,99,96,88,85,0,91,132,111],
[157,153,137,131,150,159,0,108,165],
[135,121,118,139,126,118,142,0,163],
[124,144,100,116,162,139,85,87,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,147,113,107,143,113,129,110],
[106,0,146,107,109,128,121,146,106],
[103,104,0,104,90,141,86,108,97],
[137,143,146,0,132,148,121,121,120],
[143,141,160,118,0,165,140,144,123],
[107,122,109,102,85,0,99,121,98],
[137,129,164,129,110,151,0,127,139],
[121,104,142,129,106,129,123,0,92],
[140,144,153,130,127,152,111,158,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,130,124,132,120,126,115,120],
[126,0,125,125,125,122,138,125,133],
[120,125,0,118,127,113,125,121,119],
[126,125,132,0,126,123,136,124,115],
[118,125,123,124,0,123,129,113,121],
[130,128,137,127,127,0,133,123,125],
[124,112,125,114,121,117,0,115,118],
[135,125,129,126,137,127,135,0,126],
[130,117,131,135,129,125,132,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,134,120,118,129,131,134,132],
[113,0,126,110,111,123,116,137,124],
[116,124,0,104,111,118,119,123,117],
[130,140,146,0,120,129,127,129,133],
[132,139,139,130,0,125,124,138,142],
[121,127,132,121,125,0,126,122,128],
[119,134,131,123,126,124,0,133,118],
[116,113,127,121,112,128,117,0,126],
[118,126,133,117,108,122,132,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,108,133,128,139,124,140,117],
[140,0,130,129,118,128,126,119,123],
[142,120,0,140,122,128,144,139,124],
[117,121,110,0,103,124,109,127,161],
[122,132,128,147,0,136,143,133,151],
[111,122,122,126,114,0,131,128,142],
[126,124,106,141,107,119,0,125,121],
[110,131,111,123,117,122,125,0,131],
[133,127,126,89,99,108,129,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,121,160,154,135,135,141,132],
[107,0,124,143,142,136,126,138,107],
[129,126,0,140,126,120,140,135,118],
[90,107,110,0,110,124,133,125,93],
[96,108,124,140,0,129,101,128,124],
[115,114,130,126,121,0,112,139,108],
[115,124,110,117,149,138,0,142,106],
[109,112,115,125,122,111,108,0,110],
[118,143,132,157,126,142,144,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,124,147,133,141,115,129,132],
[119,0,127,127,141,135,131,124,130],
[126,123,0,134,114,128,105,115,125],
[103,123,116,0,128,131,99,121,121],
[117,109,136,122,0,137,122,122,132],
[109,115,122,119,113,0,106,123,118],
[135,119,145,151,128,144,0,134,135],
[121,126,135,129,128,127,116,0,127],
[118,120,125,129,118,132,115,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,116,125,115,113,132,122,134],
[139,0,139,135,125,136,141,136,149],
[134,111,0,128,116,118,129,127,137],
[125,115,122,0,114,124,121,127,141],
[135,125,134,136,0,131,137,141,137],
[137,114,132,126,119,0,132,129,143],
[118,109,121,129,113,118,0,129,138],
[128,114,123,123,109,121,121,0,128],
[116,101,113,109,113,107,112,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,114,136,120,129,118,137,133],
[113,0,112,120,120,117,117,128,128],
[136,138,0,136,128,131,124,130,135],
[114,130,114,0,116,129,116,132,131],
[130,130,122,134,0,136,134,138,139],
[121,133,119,121,114,0,115,131,135],
[132,133,126,134,116,135,0,126,130],
[113,122,120,118,112,119,124,0,123],
[117,122,115,119,111,115,120,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,138,124,119,124,118,133,138],
[124,0,131,129,122,129,148,126,126],
[112,119,0,116,112,111,113,128,130],
[126,121,134,0,123,124,133,137,133],
[131,128,138,127,0,122,133,138,145],
[126,121,139,126,128,0,121,130,152],
[132,102,137,117,117,129,0,118,125],
[117,124,122,113,112,120,132,0,126],
[112,124,120,117,105,98,125,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,120,125,128,130,139,134,128],
[127,0,121,128,116,119,130,119,119],
[130,129,0,132,126,133,143,131,122],
[125,122,118,0,111,128,120,125,115],
[122,134,124,139,0,131,132,124,125],
[120,131,117,122,119,0,132,134,119],
[111,120,107,130,118,118,0,119,126],
[116,131,119,125,126,116,131,0,126],
[122,131,128,135,125,131,124,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,127,139,124,145,133,134,143],
[120,0,133,132,142,158,142,140,138],
[123,117,0,137,120,144,136,137,139],
[111,118,113,0,109,136,129,111,112],
[126,108,130,141,0,130,133,117,130],
[105,92,106,114,120,0,125,108,113],
[117,108,114,121,117,125,0,114,125],
[116,110,113,139,133,142,136,0,133],
[107,112,111,138,120,137,125,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,135,130,139,142,136,137,137],
[126,0,112,118,132,114,121,124,136],
[115,138,0,128,134,120,121,137,139],
[120,132,122,0,132,114,109,116,120],
[111,118,116,118,0,116,124,128,119],
[108,136,130,136,134,0,123,128,134],
[114,129,129,141,126,127,0,131,122],
[113,126,113,134,122,122,119,0,138],
[113,114,111,130,131,116,128,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,120,106,120,109,133,123,101],
[126,0,122,138,160,122,152,116,125],
[130,128,0,134,125,124,134,136,125],
[144,112,116,0,153,135,157,130,141],
[130,90,125,97,0,137,133,123,126],
[141,128,126,115,113,0,153,137,138],
[117,98,116,93,117,97,0,124,114],
[127,134,114,120,127,113,126,0,115],
[149,125,125,109,124,112,136,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,110,116,148,122,129,132,138],
[126,0,118,127,151,145,130,139,132],
[140,132,0,123,149,143,127,145,130],
[134,123,127,0,151,139,126,141,135],
[102,99,101,99,0,121,105,103,117],
[128,105,107,111,129,0,118,114,125],
[121,120,123,124,145,132,0,127,130],
[118,111,105,109,147,136,123,0,125],
[112,118,120,115,133,125,120,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,180,166,134,92,94,132,131,126],
[70,0,132,123,114,90,104,111,109],
[84,118,0,98,61,76,102,75,100],
[116,127,152,0,111,105,123,115,125],
[158,136,189,139,0,112,159,152,134],
[156,160,174,145,138,0,152,116,135],
[118,146,148,127,91,98,0,103,126],
[119,139,175,135,98,134,147,0,133],
[124,141,150,125,116,115,124,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,123,130,130,121,121,127,133],
[127,0,124,122,133,118,136,138,126],
[127,126,0,124,133,132,132,131,134],
[120,128,126,0,124,123,138,133,126],
[120,117,117,126,0,121,134,131,125],
[129,132,118,127,129,0,134,126,124],
[129,114,118,112,116,116,0,124,127],
[123,112,119,117,119,124,126,0,122],
[117,124,116,124,125,126,123,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,133,132,127,119,121,124,116],
[123,0,118,118,122,123,119,137,120],
[117,132,0,114,116,114,105,117,118],
[118,132,136,0,118,122,117,121,123],
[123,128,134,132,0,133,115,123,127],
[131,127,136,128,117,0,127,130,134],
[129,131,145,133,135,123,0,135,131],
[126,113,133,129,127,120,115,0,114],
[134,130,132,127,123,116,119,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,136,91,104,107,118,94,122],
[129,0,124,102,118,127,97,124,138],
[114,126,0,97,103,115,99,96,116],
[159,148,153,0,127,148,130,113,151],
[146,132,147,123,0,147,114,126,147],
[143,123,135,102,103,0,106,108,122],
[132,153,151,120,136,144,0,136,175],
[156,126,154,137,124,142,114,0,148],
[128,112,134,99,103,128,75,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,121,119,121,122,166,111,118],
[156,0,131,143,120,115,139,143,144],
[129,119,0,131,116,151,158,130,139],
[131,107,119,0,133,142,173,137,112],
[129,130,134,117,0,137,138,117,115],
[128,135,99,108,113,0,144,117,99],
[84,111,92,77,112,106,0,107,117],
[139,107,120,113,133,133,143,0,109],
[132,106,111,138,135,151,133,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,137,145,130,150,133,130,152],
[132,0,122,113,104,132,123,100,130],
[113,128,0,110,114,125,123,106,129],
[105,137,140,0,104,125,130,123,125],
[120,146,136,146,0,129,143,134,139],
[100,118,125,125,121,0,124,130,139],
[117,127,127,120,107,126,0,116,131],
[120,150,144,127,116,120,134,0,131],
[98,120,121,125,111,111,119,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,119,131,109,114,132,107,117],
[130,0,128,119,110,118,121,119,128],
[131,122,0,122,126,130,124,120,115],
[119,131,128,0,127,129,136,109,115],
[141,140,124,123,0,125,124,116,122],
[136,132,120,121,125,0,121,114,111],
[118,129,126,114,126,129,0,117,121],
[143,131,130,141,134,136,133,0,124],
[133,122,135,135,128,139,129,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,115,109,124,115,101,104,121],
[124,0,117,116,95,126,93,106,115],
[135,133,0,136,127,143,123,136,155],
[141,134,114,0,121,130,104,137,133],
[126,155,123,129,0,137,120,120,147],
[135,124,107,120,113,0,121,115,124],
[149,157,127,146,130,129,0,114,144],
[146,144,114,113,130,135,136,0,125],
[129,135,95,117,103,126,106,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,130,144,137,137,152,127,127],
[127,0,139,132,123,139,117,116,129],
[120,111,0,125,120,141,130,139,125],
[106,118,125,0,112,122,129,124,111],
[113,127,130,138,0,136,147,163,137],
[113,111,109,128,114,0,130,127,124],
[98,133,120,121,103,120,0,145,119],
[123,134,111,126,87,123,105,0,116],
[123,121,125,139,113,126,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,121,126,127,136,126,121,124],
[123,0,124,135,127,140,123,122,122],
[129,126,0,128,129,129,131,126,121],
[124,115,122,0,112,120,128,114,133],
[123,123,121,138,0,127,130,115,128],
[114,110,121,130,123,0,119,114,121],
[124,127,119,122,120,131,0,113,122],
[129,128,124,136,135,136,137,0,131],
[126,128,129,117,122,129,128,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,148,137,143,164,144,149,159],
[128,0,126,129,137,135,124,129,134],
[102,124,0,117,115,139,125,129,136],
[113,121,133,0,134,143,129,118,128],
[107,113,135,116,0,125,111,101,149],
[86,115,111,107,125,0,107,104,126],
[106,126,125,121,139,143,0,119,125],
[101,121,121,132,149,146,131,0,139],
[91,116,114,122,101,124,125,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,122,128,125,126,116,124,127],
[122,0,126,124,133,129,126,121,123],
[128,124,0,127,129,128,127,125,122],
[122,126,123,0,132,121,129,120,121],
[125,117,121,118,0,119,120,110,125],
[124,121,122,129,131,0,122,123,121],
[134,124,123,121,130,128,0,123,134],
[126,129,125,130,140,127,127,0,127],
[123,127,128,129,125,129,116,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,129,142,140,138,119,136,130],
[110,0,116,132,118,113,127,126,130],
[121,134,0,133,131,133,126,132,123],
[108,118,117,0,129,112,113,128,112],
[110,132,119,121,0,117,125,124,128],
[112,137,117,138,133,0,125,134,120],
[131,123,124,137,125,125,0,132,119],
[114,124,118,122,126,116,118,0,116],
[120,120,127,138,122,130,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,134,129,137,129,134,133,125],
[121,0,132,124,131,126,120,122,111],
[116,118,0,110,133,119,113,122,117],
[121,126,140,0,132,124,124,124,126],
[113,119,117,118,0,113,112,120,117],
[121,124,131,126,137,0,120,120,125],
[116,130,137,126,138,130,0,126,126],
[117,128,128,126,130,130,124,0,123],
[125,139,133,124,133,125,124,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,116,137,109,148,141,138,158],
[109,0,114,134,94,114,123,114,138],
[134,136,0,150,127,121,129,143,163],
[113,116,100,0,130,126,105,112,137],
[141,156,123,120,0,148,135,136,157],
[102,136,129,124,102,0,116,112,143],
[109,127,121,145,115,134,0,130,144],
[112,136,107,138,114,138,120,0,140],
[92,112,87,113,93,107,106,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,123,120,122,121,127,127,136],
[130,0,124,135,130,125,129,133,139],
[127,126,0,129,124,130,132,124,114],
[130,115,121,0,122,113,114,115,130],
[128,120,126,128,0,127,115,126,126],
[129,125,120,137,123,0,114,116,128],
[123,121,118,136,135,136,0,117,120],
[123,117,126,135,124,134,133,0,128],
[114,111,136,120,124,122,130,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,140,124,131,118,133,95,177],
[124,0,150,140,112,173,91,126,147],
[110,100,0,104,110,135,108,89,135],
[126,110,146,0,148,147,118,94,132],
[119,138,140,102,0,117,108,90,146],
[132,77,115,103,133,0,118,82,110],
[117,159,142,132,142,132,0,103,161],
[155,124,161,156,160,168,147,0,161],
[73,103,115,118,104,140,89,89,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,171,131,135,110,151,127,124],
[118,0,123,107,134,96,140,125,105],
[79,127,0,60,107,111,131,111,101],
[119,143,190,0,141,126,139,147,116],
[115,116,143,109,0,122,141,120,133],
[140,154,139,124,128,0,143,146,132],
[99,110,119,111,109,107,0,95,115],
[123,125,139,103,130,104,155,0,115],
[126,145,149,134,117,118,135,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,136,137,115,130,120,129,107],
[116,0,143,133,98,133,113,116,107],
[114,107,0,117,90,118,91,107,105],
[113,117,133,0,111,132,105,123,98],
[135,152,160,139,0,141,123,130,126],
[120,117,132,118,109,0,102,109,108],
[130,137,159,145,127,148,0,150,125],
[121,134,143,127,120,141,100,0,113],
[143,143,145,152,124,142,125,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,110,106,120,99,120,141,107],
[122,0,129,109,116,101,129,141,108],
[140,121,0,111,112,93,107,129,98],
[144,141,139,0,149,123,123,153,135],
[130,134,138,101,0,122,140,132,99],
[151,149,157,127,128,0,149,164,110],
[130,121,143,127,110,101,0,135,108],
[109,109,121,97,118,86,115,0,90],
[143,142,152,115,151,140,142,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,135,120,113,133,130,122],
[123,0,107,117,142,135,129,133,124],
[127,143,0,104,128,116,130,139,113],
[115,133,146,0,133,133,130,149,128],
[130,108,122,117,0,105,140,137,116],
[137,115,134,117,145,0,130,139,138],
[117,121,120,120,110,120,0,127,119],
[120,117,111,101,113,111,123,0,110],
[128,126,137,122,134,112,131,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,125,114,113,117,124,120],
[125,0,131,131,123,130,130,133,131],
[129,119,0,135,128,128,127,127,129],
[125,119,115,0,131,110,127,132,129],
[136,127,122,119,0,113,131,135,133],
[137,120,122,140,137,0,130,135,136],
[133,120,123,123,119,120,0,126,131],
[126,117,123,118,115,115,124,0,107],
[130,119,121,121,117,114,119,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,135,125,115,143,127,114,123],
[116,0,114,123,125,132,116,122,123],
[115,136,0,118,118,144,118,119,117],
[125,127,132,0,126,137,128,125,133],
[135,125,132,124,0,141,128,130,136],
[107,118,106,113,109,0,113,112,108],
[123,134,132,122,122,137,0,127,133],
[136,128,131,125,120,138,123,0,129],
[127,127,133,117,114,142,117,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,90,128,116,112,107,117,114],
[138,0,112,143,119,124,112,119,103],
[160,138,0,149,129,151,120,154,137],
[122,107,101,0,111,133,104,123,97],
[134,131,121,139,0,137,111,143,122],
[138,126,99,117,113,0,108,123,113],
[143,138,130,146,139,142,0,131,109],
[133,131,96,127,107,127,119,0,118],
[136,147,113,153,128,137,141,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,134,117,130,107,124,129,126],
[124,0,138,121,122,120,134,129,131],
[116,112,0,120,124,128,130,125,136],
[133,129,130,0,131,118,132,142,146],
[120,128,126,119,0,125,133,128,126],
[143,130,122,132,125,0,140,136,143],
[126,116,120,118,117,110,0,127,118],
[121,121,125,108,122,114,123,0,137],
[124,119,114,104,124,107,132,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,132,134,123,110,131,135,137],
[123,0,128,136,119,125,133,132,128],
[118,122,0,122,122,127,135,122,138],
[116,114,128,0,113,113,131,134,135],
[127,131,128,137,0,113,144,141,138],
[140,125,123,137,137,0,140,135,134],
[119,117,115,119,106,110,0,120,137],
[115,118,128,116,109,115,130,0,120],
[113,122,112,115,112,116,113,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,134,136,133,137,140,127,125],
[119,0,126,123,128,122,140,116,120],
[116,124,0,109,114,115,124,109,109],
[114,127,141,0,125,132,126,130,135],
[117,122,136,125,0,117,130,120,122],
[113,128,135,118,133,0,149,129,113],
[110,110,126,124,120,101,0,97,114],
[123,134,141,120,130,121,153,0,105],
[125,130,141,115,128,137,136,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,132,94,101,125,115,108,98],
[126,0,132,131,117,131,111,123,123],
[118,118,0,110,123,114,111,114,124],
[156,119,140,0,131,123,125,146,116],
[149,133,127,119,0,143,123,143,151],
[125,119,136,127,107,0,100,128,133],
[135,139,139,125,127,150,0,134,121],
[142,127,136,104,107,122,116,0,114],
[152,127,126,134,99,117,129,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,113,124,120,125,124,122,113],
[115,0,115,119,106,117,114,111,110],
[137,135,0,124,119,122,122,118,115],
[126,131,126,0,124,128,131,123,113],
[130,144,131,126,0,127,135,122,127],
[125,133,128,122,123,0,128,111,121],
[126,136,128,119,115,122,0,121,122],
[128,139,132,127,128,139,129,0,122],
[137,140,135,137,123,129,128,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,123,136,149,126,128,133,116],
[131,0,129,139,130,152,140,123,136],
[127,121,0,130,135,140,142,122,100],
[114,111,120,0,134,136,125,137,135],
[101,120,115,116,0,135,118,137,127],
[124,98,110,114,115,0,117,132,111],
[122,110,108,125,132,133,0,128,110],
[117,127,128,113,113,118,122,0,111],
[134,114,150,115,123,139,140,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,120,145,119,127,131,156,132],
[113,0,109,136,81,116,141,136,121],
[130,141,0,142,125,140,143,154,142],
[105,114,108,0,95,127,136,145,122],
[131,169,125,155,0,127,138,152,132],
[123,134,110,123,123,0,119,148,111],
[119,109,107,114,112,131,0,137,117],
[94,114,96,105,98,102,113,0,110],
[118,129,108,128,118,139,133,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,128,123,123,119,107,129,115],
[140,0,124,113,119,110,122,115,144],
[122,126,0,112,126,128,109,115,132],
[127,137,138,0,127,141,140,117,135],
[127,131,124,123,0,146,127,114,148],
[131,140,122,109,104,0,114,113,128],
[143,128,141,110,123,136,0,124,144],
[121,135,135,133,136,137,126,0,145],
[135,106,118,115,102,122,106,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,133,128,113,110,139,144,115],
[109,0,115,133,117,108,105,137,111],
[117,135,0,133,108,103,102,133,117],
[122,117,117,0,124,119,132,146,125],
[137,133,142,126,0,124,137,156,140],
[140,142,147,131,126,0,116,154,122],
[111,145,148,118,113,134,0,145,138],
[106,113,117,104,94,96,105,0,118],
[135,139,133,125,110,128,112,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,127,105,120,111,98,106,120],
[114,0,119,112,113,102,83,108,108],
[123,131,0,119,115,111,109,122,119],
[145,138,131,0,126,134,108,121,112],
[130,137,135,124,0,126,105,123,111],
[139,148,139,116,124,0,90,107,120],
[152,167,141,142,145,160,0,122,129],
[144,142,128,129,127,143,128,0,125],
[130,142,131,138,139,130,121,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,70,101,78,76,109,122,132],
[142,0,107,122,104,115,130,129,122],
[180,143,0,170,125,146,166,122,173],
[149,128,80,0,101,122,128,141,112],
[172,146,125,149,0,151,168,159,151],
[174,135,104,128,99,0,170,140,168],
[141,120,84,122,82,80,0,96,134],
[128,121,128,109,91,110,154,0,130],
[118,128,77,138,99,82,116,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,149,136,124,131,131,145,123],
[122,0,135,124,137,137,143,137,131],
[101,115,0,113,113,118,127,135,128],
[114,126,137,0,112,136,127,150,141],
[126,113,137,138,0,146,155,161,136],
[119,113,132,114,104,0,128,141,121],
[119,107,123,123,95,122,0,125,130],
[105,113,115,100,89,109,125,0,111],
[127,119,122,109,114,129,120,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,147,127,133,135,129,138,125],
[117,0,110,113,111,104,118,128,104],
[103,140,0,106,106,115,113,133,111],
[123,137,144,0,125,118,129,134,127],
[117,139,144,125,0,131,128,147,132],
[115,146,135,132,119,0,133,138,122],
[121,132,137,121,122,117,0,126,120],
[112,122,117,116,103,112,124,0,112],
[125,146,139,123,118,128,130,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,123,117,108,123,130,118,147],
[142,0,138,130,130,148,134,124,168],
[127,112,0,113,106,133,110,111,131],
[133,120,137,0,129,119,124,129,145],
[142,120,144,121,0,140,134,120,138],
[127,102,117,131,110,0,95,127,121],
[120,116,140,126,116,155,0,124,137],
[132,126,139,121,130,123,126,0,145],
[103,82,119,105,112,129,113,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,116,115,118,111,117,119,109],
[117,0,113,109,117,113,116,127,108],
[134,137,0,131,129,131,122,132,122],
[135,141,119,0,118,120,123,140,130],
[132,133,121,132,0,117,121,137,122],
[139,137,119,130,133,0,116,144,125],
[133,134,128,127,129,134,0,132,123],
[131,123,118,110,113,106,118,0,106],
[141,142,128,120,128,125,127,144,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,120,119,128,124,123,125,133],
[126,0,136,127,124,114,118,126,128],
[130,114,0,132,134,120,120,132,137],
[131,123,118,0,135,126,126,120,134],
[122,126,116,115,0,108,120,114,120],
[126,136,130,124,142,0,125,132,142],
[127,132,130,124,130,125,0,126,147],
[125,124,118,130,136,118,124,0,125],
[117,122,113,116,130,108,103,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,109,92,119,92,124,117,97],
[156,0,136,133,116,121,144,138,140],
[141,114,0,132,123,116,144,161,137],
[158,117,118,0,92,110,135,157,123],
[131,134,127,158,0,116,150,121,106],
[158,129,134,140,134,0,147,117,144],
[126,106,106,115,100,103,0,124,134],
[133,112,89,93,129,133,126,0,126],
[153,110,113,127,144,106,116,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,133,124,134,123,126,139,123],
[110,0,124,120,126,112,128,138,111],
[117,126,0,134,126,117,129,134,116],
[126,130,116,0,122,121,134,145,127],
[116,124,124,128,0,113,132,131,115],
[127,138,133,129,137,0,130,133,125],
[124,122,121,116,118,120,0,124,117],
[111,112,116,105,119,117,126,0,111],
[127,139,134,123,135,125,133,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,123,152,142,151,142,150,146],
[108,0,136,131,154,128,120,133,141],
[127,114,0,147,161,134,140,140,121],
[98,119,103,0,145,133,130,112,127],
[108,96,89,105,0,100,94,112,97],
[99,122,116,117,150,0,123,131,131],
[108,130,110,120,156,127,0,119,148],
[100,117,110,138,138,119,131,0,127],
[104,109,129,123,153,119,102,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,125,130,124,131,128,125,124],
[118,0,129,121,118,136,122,125,118],
[125,121,0,122,120,121,130,127,118],
[120,129,128,0,137,128,139,124,127],
[126,132,130,113,0,133,134,122,118],
[119,114,129,122,117,0,125,119,120],
[122,128,120,111,116,125,0,115,120],
[125,125,123,126,128,131,135,0,125],
[126,132,132,123,132,130,130,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,142,118,126,129,128,133,128],
[122,0,140,122,125,130,131,132,127],
[108,110,0,113,118,119,118,121,113],
[132,128,137,0,127,135,123,132,129],
[124,125,132,123,0,131,135,130,124],
[121,120,131,115,119,0,116,123,124],
[122,119,132,127,115,134,0,130,117],
[117,118,129,118,120,127,120,0,124],
[122,123,137,121,126,126,133,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,120,119,116,113,114,126,108],
[141,0,133,153,128,136,130,119,116],
[130,117,0,137,116,121,127,135,130],
[131,97,113,0,121,124,114,109,107],
[134,122,134,129,0,116,135,133,134],
[137,114,129,126,134,0,122,113,99],
[136,120,123,136,115,128,0,122,108],
[124,131,115,141,117,137,128,0,110],
[142,134,120,143,116,151,142,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,126,128,131,125,137,130,120],
[112,0,114,128,133,117,139,123,126],
[124,136,0,134,134,128,134,122,114],
[122,122,116,0,130,116,124,114,119],
[119,117,116,120,0,113,129,125,122],
[125,133,122,134,137,0,137,124,126],
[113,111,116,126,121,113,0,111,128],
[120,127,128,136,125,126,139,0,124],
[130,124,136,131,128,124,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 250, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_9_250.csv", index=False, header=False)