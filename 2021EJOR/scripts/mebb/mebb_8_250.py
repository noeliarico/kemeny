
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,122,115,111,109,122,122,124],
[128,0,140,123,116,126,129,119],
[135,110,0,118,100,124,135,121],
[139,127,132,0,124,137,133,135],
[141,134,150,126,0,129,135,123],
[128,124,126,113,121,0,142,129],
[128,121,115,117,115,108,0,129],
[126,131,129,115,127,121,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,125,113,125,118,120,129],
[134,0,119,142,126,125,117,134],
[125,131,0,130,125,138,123,125],
[137,108,120,0,110,116,120,119],
[125,124,125,140,0,129,126,148],
[132,125,112,134,121,0,117,119],
[130,133,127,130,124,133,0,133],
[121,116,125,131,102,131,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,121,112,122,134,118,129],
[124,0,116,121,121,122,117,107],
[129,134,0,130,124,126,128,129],
[138,129,120,0,123,123,131,133],
[128,129,126,127,0,124,126,129],
[116,128,124,127,126,0,122,130],
[132,133,122,119,124,128,0,122],
[121,143,121,117,121,120,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,128,117,131,131,119,145],
[132,0,122,140,122,156,141,150],
[122,128,0,123,140,132,136,136],
[133,110,127,0,140,82,114,141],
[119,128,110,110,0,125,135,151],
[119,94,118,168,125,0,146,148],
[131,109,114,136,115,104,0,135],
[105,100,114,109,99,102,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,130,128,125,132,134,134],
[115,0,119,122,118,123,118,132],
[120,131,0,124,122,120,122,132],
[122,128,126,0,118,134,125,137],
[125,132,128,132,0,134,126,141],
[118,127,130,116,116,0,124,138],
[116,132,128,125,124,126,0,131],
[116,118,118,113,109,112,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,124,115,116,118,120,130],
[136,0,122,122,132,107,124,131],
[126,128,0,131,120,116,113,136],
[135,128,119,0,129,109,127,124],
[134,118,130,121,0,102,120,121],
[132,143,134,141,148,0,116,127],
[130,126,137,123,130,134,0,134],
[120,119,114,126,129,123,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,130,132,113,122,119,116],
[129,0,131,142,129,127,138,116],
[120,119,0,141,123,139,125,122],
[118,108,109,0,107,97,98,115],
[137,121,127,143,0,118,120,127],
[128,123,111,153,132,0,133,107],
[131,112,125,152,130,117,0,110],
[134,134,128,135,123,143,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,136,96,140,104,122,76],
[149,0,177,163,189,121,148,130],
[114,73,0,100,120,102,65,118],
[154,87,150,0,133,113,121,141],
[110,61,130,117,0,104,96,122],
[146,129,148,137,146,0,103,124],
[128,102,185,129,154,147,0,168],
[174,120,132,109,128,126,82,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,143,132,140,149,137,129],
[136,0,131,144,143,160,119,134],
[107,119,0,125,138,142,115,134],
[118,106,125,0,128,140,108,123],
[110,107,112,122,0,117,109,109],
[101,90,108,110,133,0,118,114],
[113,131,135,142,141,132,0,122],
[121,116,116,127,141,136,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,117,116,116,106,123,107],
[138,0,139,115,128,120,132,128],
[133,111,0,116,135,126,122,127],
[134,135,134,0,142,120,133,124],
[134,122,115,108,0,106,110,114],
[144,130,124,130,144,0,121,129],
[127,118,128,117,140,129,0,116],
[143,122,123,126,136,121,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,91,116,129,147,108,111],
[135,0,115,119,128,132,128,136],
[159,135,0,130,160,137,120,140],
[134,131,120,0,142,133,132,138],
[121,122,90,108,0,126,108,116],
[103,118,113,117,124,0,117,135],
[142,122,130,118,142,133,0,145],
[139,114,110,112,134,115,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,129,119,130,142,129,143],
[128,0,134,121,145,132,118,140],
[121,116,0,115,114,107,104,131],
[131,129,135,0,148,140,106,148],
[120,105,136,102,0,115,119,117],
[108,118,143,110,135,0,107,140],
[121,132,146,144,131,143,0,142],
[107,110,119,102,133,110,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,117,113,110,115,118,127],
[140,0,137,136,124,136,136,132],
[133,113,0,123,126,116,119,132],
[137,114,127,0,114,121,122,123],
[140,126,124,136,0,129,117,138],
[135,114,134,129,121,0,131,130],
[132,114,131,128,133,119,0,128],
[123,118,118,127,112,120,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,130,122,139,123,130,137],
[124,0,116,123,127,119,120,138],
[120,134,0,132,130,127,124,136],
[128,127,118,0,128,121,117,131],
[111,123,120,122,0,117,105,124],
[127,131,123,129,133,0,117,141],
[120,130,126,133,145,133,0,136],
[113,112,114,119,126,109,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,118,106,132,119,102,109],
[124,0,117,132,121,111,84,108],
[132,133,0,130,144,143,125,113],
[144,118,120,0,126,118,117,115],
[118,129,106,124,0,125,103,110],
[131,139,107,132,125,0,89,105],
[148,166,125,133,147,161,0,125],
[141,142,137,135,140,145,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,118,114,158,134,137,134],
[124,0,112,115,143,128,133,129],
[132,138,0,133,146,129,147,124],
[136,135,117,0,155,132,141,129],
[92,107,104,95,0,99,117,109],
[116,122,121,118,151,0,125,118],
[113,117,103,109,133,125,0,115],
[116,121,126,121,141,132,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,128,116,126,132,138,133],
[113,0,107,118,128,113,123,127],
[122,143,0,123,128,118,129,133],
[134,132,127,0,115,118,124,132],
[124,122,122,135,0,121,130,134],
[118,137,132,132,129,0,129,141],
[112,127,121,126,120,121,0,125],
[117,123,117,118,116,109,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,109,103,101,92,101,111],
[156,0,128,138,130,138,122,126],
[141,122,0,128,119,120,133,126],
[147,112,122,0,131,121,125,126],
[149,120,131,119,0,115,125,123],
[158,112,130,129,135,0,121,130],
[149,128,117,125,125,129,0,132],
[139,124,124,124,127,120,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,132,130,128,127,130,125],
[125,0,133,126,131,126,137,129],
[118,117,0,134,140,130,131,128],
[120,124,116,0,131,130,133,120],
[122,119,110,119,0,128,120,124],
[123,124,120,120,122,0,126,124],
[120,113,119,117,130,124,0,126],
[125,121,122,130,126,126,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,126,127,133,135,141,127],
[126,0,120,115,133,136,122,133],
[124,130,0,126,127,140,130,133],
[123,135,124,0,127,128,126,128],
[117,117,123,123,0,123,134,129],
[115,114,110,122,127,0,119,123],
[109,128,120,124,116,131,0,124],
[123,117,117,122,121,127,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,121,117,139,136,145,129],
[117,0,125,123,147,122,140,143],
[129,125,0,130,144,131,142,133],
[133,127,120,0,140,115,129,129],
[111,103,106,110,0,122,126,134],
[114,128,119,135,128,0,126,136],
[105,110,108,121,124,124,0,111],
[121,107,117,121,116,114,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,128,123,132,135,112,148],
[130,0,113,124,138,145,118,157],
[122,137,0,125,151,142,127,143],
[127,126,125,0,149,132,115,128],
[118,112,99,101,0,136,112,119],
[115,105,108,118,114,0,99,118],
[138,132,123,135,138,151,0,142],
[102,93,107,122,131,132,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,95,133,88,120,117,123],
[137,0,82,92,85,103,109,104],
[155,168,0,123,152,144,109,130],
[117,158,127,0,128,137,146,142],
[162,165,98,122,0,136,125,124],
[130,147,106,113,114,0,121,105],
[133,141,141,104,125,129,0,116],
[127,146,120,108,126,145,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,134,141,144,121,115,114],
[140,0,117,142,144,118,134,123],
[116,133,0,155,144,120,114,116],
[109,108,95,0,130,123,109,120],
[106,106,106,120,0,109,110,123],
[129,132,130,127,141,0,120,127],
[135,116,136,141,140,130,0,134],
[136,127,134,130,127,123,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,135,152,143,127,157,127],
[128,0,121,155,115,121,122,129],
[115,129,0,160,127,118,146,124],
[98,95,90,0,96,108,125,85],
[107,135,123,154,0,116,132,111],
[123,129,132,142,134,0,144,123],
[93,128,104,125,118,106,0,103],
[123,121,126,165,139,127,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,129,135,117,125,131],
[114,0,128,114,131,110,122,122],
[124,122,0,110,128,107,127,124],
[121,136,140,0,140,129,140,130],
[115,119,122,110,0,100,131,114],
[133,140,143,121,150,0,145,133],
[125,128,123,110,119,105,0,127],
[119,128,126,120,136,117,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,94,125,133,119,125,142],
[131,0,140,120,121,124,140,136],
[156,110,0,154,139,129,139,132],
[125,130,96,0,119,121,119,113],
[117,129,111,131,0,83,127,126],
[131,126,121,129,167,0,141,127],
[125,110,111,131,123,109,0,123],
[108,114,118,137,124,123,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,161,127,125,143,131,116],
[114,0,130,83,104,139,126,125],
[89,120,0,82,83,114,107,96],
[123,167,168,0,144,172,165,158],
[125,146,167,106,0,163,138,132],
[107,111,136,78,87,0,117,104],
[119,124,143,85,112,133,0,136],
[134,125,154,92,118,146,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,125,128,133,134,140,130],
[115,0,124,140,132,124,122,122],
[125,126,0,128,123,129,122,128],
[122,110,122,0,127,123,108,122],
[117,118,127,123,0,117,120,130],
[116,126,121,127,133,0,123,130],
[110,128,128,142,130,127,0,130],
[120,128,122,128,120,120,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,125,127,130,128,133,128],
[115,0,125,128,120,114,129,121],
[125,125,0,136,126,117,125,123],
[123,122,114,0,108,115,116,116],
[120,130,124,142,0,117,124,109],
[122,136,133,135,133,0,140,129],
[117,121,125,134,126,110,0,121],
[122,129,127,134,141,121,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,120,142,136,134,124,143],
[105,0,112,121,122,125,131,125],
[130,138,0,144,126,124,135,137],
[108,129,106,0,110,136,95,107],
[114,128,124,140,0,144,136,142],
[116,125,126,114,106,0,112,120],
[126,119,115,155,114,138,0,136],
[107,125,113,143,108,130,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,135,114,119,110,135,115],
[119,0,140,133,135,125,130,119],
[115,110,0,125,118,121,122,99],
[136,117,125,0,129,127,120,112],
[131,115,132,121,0,120,132,120],
[140,125,129,123,130,0,126,121],
[115,120,128,130,118,124,0,132],
[135,131,151,138,130,129,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,150,142,172,147,121,153],
[110,0,159,139,110,130,109,121],
[100,91,0,137,96,133,99,125],
[108,111,113,0,86,100,104,121],
[78,140,154,164,0,110,108,120],
[103,120,117,150,140,0,139,148],
[129,141,151,146,142,111,0,154],
[97,129,125,129,130,102,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,126,135,129,132,137,138],
[125,0,131,117,118,140,117,138],
[124,119,0,134,138,130,128,136],
[115,133,116,0,127,132,104,131],
[121,132,112,123,0,133,121,126],
[118,110,120,118,117,0,117,129],
[113,133,122,146,129,133,0,134],
[112,112,114,119,124,121,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,153,128,152,146,129,168,103],
[97,0,129,114,148,129,119,118],
[122,121,0,120,130,121,131,120],
[98,136,130,0,144,128,149,135],
[104,102,120,106,0,104,122,83],
[121,121,129,122,146,0,158,96],
[82,131,119,101,128,92,0,80],
[147,132,130,115,167,154,170,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,132,128,139,136,126,118],
[122,0,132,128,131,140,127,129],
[118,118,0,124,131,134,114,119],
[122,122,126,0,142,136,120,133],
[111,119,119,108,0,124,112,127],
[114,110,116,114,126,0,111,116],
[124,123,136,130,138,139,0,126],
[132,121,131,117,123,134,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,130,121,121,126,107,123],
[128,0,157,112,91,156,131,112],
[120,93,0,99,98,132,111,98],
[129,138,151,0,152,162,112,101],
[129,159,152,98,0,126,120,113],
[124,94,118,88,124,0,83,101],
[143,119,139,138,130,167,0,126],
[127,138,152,149,137,149,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,129,126,145,124,121,121],
[128,0,127,124,140,127,130,119],
[121,123,0,119,136,118,110,125],
[124,126,131,0,137,111,129,116],
[105,110,114,113,0,110,106,110],
[126,123,132,139,140,0,127,120],
[129,120,140,121,144,123,0,118],
[129,131,125,134,140,130,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,101,143,117,74,85,33],
[156,0,106,178,139,168,116,88],
[149,144,0,156,134,168,124,96],
[107,72,94,0,95,108,76,53],
[133,111,116,155,0,137,145,114],
[176,82,82,142,113,0,94,75],
[165,134,126,174,105,156,0,165],
[217,162,154,197,136,175,85,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,117,104,123,120,119,116],
[118,0,124,115,130,131,131,131],
[133,126,0,116,124,122,117,117],
[146,135,134,0,130,143,131,124],
[127,120,126,120,0,121,109,110],
[130,119,128,107,129,0,123,126],
[131,119,133,119,141,127,0,122],
[134,119,133,126,140,124,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,159,121,141,165,130,128],
[117,0,165,137,140,139,141,126],
[91,85,0,93,116,103,99,99],
[129,113,157,0,144,140,140,122],
[109,110,134,106,0,117,105,105],
[85,111,147,110,133,0,131,106],
[120,109,151,110,145,119,0,118],
[122,124,151,128,145,144,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,132,158,128,122,143,111],
[119,0,133,149,109,125,104,115],
[118,117,0,151,107,134,109,127],
[92,101,99,0,101,113,106,114],
[122,141,143,149,0,113,122,106],
[128,125,116,137,137,0,127,132],
[107,146,141,144,128,123,0,154],
[139,135,123,136,144,118,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,117,118,113,112,114,102],
[145,0,129,141,121,135,138,133],
[133,121,0,129,121,131,128,124],
[132,109,121,0,130,119,130,115],
[137,129,129,120,0,128,123,130],
[138,115,119,131,122,0,134,123],
[136,112,122,120,127,116,0,131],
[148,117,126,135,120,127,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,129,131,129,133,123,122],
[131,0,137,140,131,150,122,140],
[121,113,0,129,128,128,118,124],
[119,110,121,0,127,135,107,130],
[121,119,122,123,0,126,131,140],
[117,100,122,115,124,0,114,124],
[127,128,132,143,119,136,0,126],
[128,110,126,120,110,126,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,125,132,120,126,126,119],
[134,0,120,123,130,126,129,132],
[125,130,0,116,125,135,127,141],
[118,127,134,0,124,134,131,135],
[130,120,125,126,0,138,136,134],
[124,124,115,116,112,0,130,133],
[124,121,123,119,114,120,0,128],
[131,118,109,115,116,117,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,121,117,127,123,124,132],
[126,0,116,129,122,111,113,127],
[129,134,0,122,128,132,136,130],
[133,121,128,0,131,129,132,128],
[123,128,122,119,0,128,118,124],
[127,139,118,121,122,0,122,120],
[126,137,114,118,132,128,0,119],
[118,123,120,122,126,130,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,119,129,128,131,139,118],
[110,0,112,123,115,122,117,102],
[131,138,0,133,124,129,120,124],
[121,127,117,0,129,136,125,117],
[122,135,126,121,0,133,118,126],
[119,128,121,114,117,0,112,110],
[111,133,130,125,132,138,0,113],
[132,148,126,133,124,140,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,120,114,124,136,126,124],
[114,0,116,105,113,108,109,116],
[130,134,0,120,125,120,132,127],
[136,145,130,0,116,130,129,118],
[126,137,125,134,0,135,123,134],
[114,142,130,120,115,0,132,119],
[124,141,118,121,127,118,0,116],
[126,134,123,132,116,131,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,119,119,117,124,123,130],
[129,0,113,128,113,113,116,112],
[131,137,0,131,119,134,123,127],
[131,122,119,0,96,123,115,123],
[133,137,131,154,0,123,134,137],
[126,137,116,127,127,0,124,144],
[127,134,127,135,116,126,0,123],
[120,138,123,127,113,106,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,143,137,134,136,125,126],
[108,0,116,118,119,120,108,116],
[107,134,0,116,114,124,115,111],
[113,132,134,0,121,131,109,116],
[116,131,136,129,0,140,118,124],
[114,130,126,119,110,0,131,119],
[125,142,135,141,132,119,0,128],
[124,134,139,134,126,131,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,135,129,132,121,128,131],
[113,0,115,113,121,117,110,99],
[115,135,0,128,125,123,127,124],
[121,137,122,0,140,116,118,113],
[118,129,125,110,0,126,99,112],
[129,133,127,134,124,0,126,132],
[122,140,123,132,151,124,0,133],
[119,151,126,137,138,118,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,130,128,137,117,135,132],
[130,0,129,117,134,134,137,140],
[120,121,0,120,127,123,137,129],
[122,133,130,0,134,138,139,139],
[113,116,123,116,0,118,138,127],
[133,116,127,112,132,0,133,128],
[115,113,113,111,112,117,0,109],
[118,110,121,111,123,122,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,137,148,121,140,133,130],
[112,0,120,117,104,125,121,110],
[113,130,0,127,127,128,123,119],
[102,133,123,0,123,122,122,127],
[129,146,123,127,0,132,134,133],
[110,125,122,128,118,0,123,119],
[117,129,127,128,116,127,0,115],
[120,140,131,123,117,131,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,147,127,115,127,135,137],
[98,0,120,105,112,138,146,136],
[103,130,0,112,116,146,142,135],
[123,145,138,0,126,152,132,150],
[135,138,134,124,0,139,157,145],
[123,112,104,98,111,0,129,143],
[115,104,108,118,93,121,0,129],
[113,114,115,100,105,107,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,94,127,131,136,126,114],
[117,0,102,130,135,111,121,124],
[156,148,0,152,142,137,150,125],
[123,120,98,0,123,100,123,103],
[119,115,108,127,0,132,123,110],
[114,139,113,150,118,0,122,116],
[124,129,100,127,127,128,0,135],
[136,126,125,147,140,134,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,113,111,105,122,114,123],
[143,0,113,114,124,126,127,120],
[137,137,0,132,123,139,140,144],
[139,136,118,0,134,138,127,131],
[145,126,127,116,0,135,134,130],
[128,124,111,112,115,0,121,127],
[136,123,110,123,116,129,0,131],
[127,130,106,119,120,123,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,121,129,117,139,112,131],
[111,0,118,113,102,122,109,116],
[129,132,0,134,123,118,133,141],
[121,137,116,0,120,130,115,130],
[133,148,127,130,0,133,120,146],
[111,128,132,120,117,0,132,128],
[138,141,117,135,130,118,0,127],
[119,134,109,120,104,122,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,144,159,127,138,120,124],
[133,0,149,146,137,125,127,120],
[106,101,0,125,115,122,111,125],
[91,104,125,0,124,113,101,89],
[123,113,135,126,0,123,121,108],
[112,125,128,137,127,0,149,129],
[130,123,139,149,129,101,0,139],
[126,130,125,161,142,121,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,123,125,130,119,126,114],
[121,0,134,124,122,119,123,129],
[127,116,0,125,139,120,123,123],
[125,126,125,0,128,125,126,128],
[120,128,111,122,0,114,130,127],
[131,131,130,125,136,0,140,124],
[124,127,127,124,120,110,0,119],
[136,121,127,122,123,126,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,121,102,100,113,109,139],
[108,0,109,93,96,93,91,107],
[129,141,0,124,125,118,114,119],
[148,157,126,0,104,103,92,105],
[150,154,125,146,0,138,116,139],
[137,157,132,147,112,0,126,110],
[141,159,136,158,134,124,0,132],
[111,143,131,145,111,140,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,123,121,133,161,132,96],
[124,0,135,113,131,161,128,139],
[127,115,0,129,124,146,139,102],
[129,137,121,0,118,145,129,102],
[117,119,126,132,0,145,139,100],
[89,89,104,105,105,0,114,89],
[118,122,111,121,111,136,0,97],
[154,111,148,148,150,161,153,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,130,116,127,117,121,120],
[125,0,130,121,127,134,123,126],
[120,120,0,120,126,126,127,130],
[134,129,130,0,129,129,135,123],
[123,123,124,121,0,124,130,125],
[133,116,124,121,126,0,124,134],
[129,127,123,115,120,126,0,131],
[130,124,120,127,125,116,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,126,123,146,140,137,148],
[109,0,99,111,124,130,129,129],
[124,151,0,136,130,158,136,139],
[127,139,114,0,145,127,130,138],
[104,126,120,105,0,132,125,142],
[110,120,92,123,118,0,113,123],
[113,121,114,120,125,137,0,122],
[102,121,111,112,108,127,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,114,112,112,123,117,125],
[121,0,107,119,121,117,115,128],
[136,143,0,138,125,133,119,132],
[138,131,112,0,119,126,114,133],
[138,129,125,131,0,124,121,132],
[127,133,117,124,126,0,126,131],
[133,135,131,136,129,124,0,134],
[125,122,118,117,118,119,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,114,136,160,126,121,127],
[148,0,130,149,158,152,127,122],
[136,120,0,134,152,124,145,110],
[114,101,116,0,138,134,117,131],
[90,92,98,112,0,100,108,117],
[124,98,126,116,150,0,117,126],
[129,123,105,133,142,133,0,116],
[123,128,140,119,133,124,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,90,113,136,106,131,120,111],
[160,0,148,133,94,137,141,136],
[137,102,0,115,100,96,121,129],
[114,117,135,0,73,134,91,128],
[144,156,150,177,0,141,123,152],
[119,113,154,116,109,0,129,137],
[130,109,129,159,127,121,0,116],
[139,114,121,122,98,113,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,135,128,160,145,132,163],
[128,0,101,119,145,120,123,151],
[115,149,0,125,168,149,154,143],
[122,131,125,0,152,130,138,151],
[90,105,82,98,0,91,93,120],
[105,130,101,120,159,0,136,114],
[118,127,96,112,157,114,0,139],
[87,99,107,99,130,136,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,122,127,119,120,132,130],
[138,0,129,132,133,121,127,133],
[128,121,0,124,126,124,127,125],
[123,118,126,0,118,121,124,135],
[131,117,124,132,0,128,119,131],
[130,129,126,129,122,0,122,131],
[118,123,123,126,131,128,0,127],
[120,117,125,115,119,119,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,126,108,125,132,145,120],
[130,0,138,117,130,136,136,119],
[124,112,0,112,122,132,137,120],
[142,133,138,0,128,143,133,112],
[125,120,128,122,0,140,137,122],
[118,114,118,107,110,0,128,125],
[105,114,113,117,113,122,0,98],
[130,131,130,138,128,125,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,132,113,113,122,129,122],
[133,0,122,111,127,115,124,130],
[118,128,0,114,123,122,128,117],
[137,139,136,0,131,125,135,132],
[137,123,127,119,0,131,125,136],
[128,135,128,125,119,0,133,149],
[121,126,122,115,125,117,0,121],
[128,120,133,118,114,101,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,127,88,117,99,145,105],
[179,0,173,118,155,145,166,119],
[123,77,0,96,113,111,163,82],
[162,132,154,0,139,140,125,163],
[133,95,137,111,0,99,101,81],
[151,105,139,110,151,0,128,90],
[105,84,87,125,149,122,0,104],
[145,131,168,87,169,160,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,153,127,120,147,158,114],
[109,0,124,106,107,102,134,103],
[97,126,0,105,107,118,136,122],
[123,144,145,0,154,153,159,138],
[130,143,143,96,0,150,153,108],
[103,148,132,97,100,0,148,125],
[92,116,114,91,97,102,0,88],
[136,147,128,112,142,125,162,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,125,112,107,122,128,116],
[117,0,116,121,123,127,110,122],
[125,134,0,124,120,123,124,129],
[138,129,126,0,123,129,121,121],
[143,127,130,127,0,133,125,133],
[128,123,127,121,117,0,128,127],
[122,140,126,129,125,122,0,127],
[134,128,121,129,117,123,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,125,134,130,122,124,123],
[133,0,111,127,119,117,122,125],
[125,139,0,123,137,127,132,131],
[116,123,127,0,135,116,116,125],
[120,131,113,115,0,115,119,115],
[128,133,123,134,135,0,136,124],
[126,128,118,134,131,114,0,116],
[127,125,119,125,135,126,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,113,119,108,110,114,115],
[132,0,119,121,119,103,123,118],
[137,131,0,128,145,123,131,131],
[131,129,122,0,130,122,135,123],
[142,131,105,120,0,127,129,122],
[140,147,127,128,123,0,137,123],
[136,127,119,115,121,113,0,115],
[135,132,119,127,128,127,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,114,118,122,123,111,119],
[127,0,131,123,110,133,103,118],
[136,119,0,132,105,117,108,120],
[132,127,118,0,129,139,124,131],
[128,140,145,121,0,135,130,128],
[127,117,133,111,115,0,100,101],
[139,147,142,126,120,150,0,127],
[131,132,130,119,122,149,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,121,125,117,115,119,112],
[138,0,133,134,130,123,143,124],
[129,117,0,127,117,124,125,107],
[125,116,123,0,121,121,125,107],
[133,120,133,129,0,125,139,130],
[135,127,126,129,125,0,131,134],
[131,107,125,125,111,119,0,116],
[138,126,143,143,120,116,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,124,129,125,137,129,128],
[116,0,113,113,119,123,102,119],
[126,137,0,125,137,130,125,121],
[121,137,125,0,135,147,128,122],
[125,131,113,115,0,133,121,128],
[113,127,120,103,117,0,116,105],
[121,148,125,122,129,134,0,125],
[122,131,129,128,122,145,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,136,133,153,137,120,135],
[138,0,155,129,155,137,134,119],
[114,95,0,123,142,131,105,115],
[117,121,127,0,137,137,123,110],
[97,95,108,113,0,112,113,108],
[113,113,119,113,138,0,116,105],
[130,116,145,127,137,134,0,116],
[115,131,135,140,142,145,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,145,129,109,132,107,128],
[143,0,140,118,91,154,105,126],
[105,110,0,119,93,137,95,117],
[121,132,131,0,87,134,104,109],
[141,159,157,163,0,157,116,141],
[118,96,113,116,93,0,103,97],
[143,145,155,146,134,147,0,122],
[122,124,133,141,109,153,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,135,129,113,140,117,114],
[119,0,140,135,115,145,113,128],
[115,110,0,123,120,129,108,107],
[121,115,127,0,106,143,108,95],
[137,135,130,144,0,137,105,123],
[110,105,121,107,113,0,96,90],
[133,137,142,142,145,154,0,116],
[136,122,143,155,127,160,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,120,140,120,117,129,124],
[138,0,114,150,125,134,138,148],
[130,136,0,140,127,124,127,128],
[110,100,110,0,116,116,119,118],
[130,125,123,134,0,120,134,130],
[133,116,126,134,130,0,126,120],
[121,112,123,131,116,124,0,114],
[126,102,122,132,120,130,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,121,98,111,115,82,142],
[141,0,138,147,145,144,145,101],
[129,112,0,72,76,110,145,92],
[152,103,178,0,158,111,181,135],
[139,105,174,92,0,127,126,123],
[135,106,140,139,123,0,133,155],
[168,105,105,69,124,117,0,137],
[108,149,158,115,127,95,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,124,135,124,135,131,112],
[134,0,127,121,128,139,132,118],
[126,123,0,114,119,141,119,117],
[115,129,136,0,128,121,130,106],
[126,122,131,122,0,135,120,113],
[115,111,109,129,115,0,116,126],
[119,118,131,120,130,134,0,122],
[138,132,133,144,137,124,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,127,103,132,123,113,114],
[134,0,144,119,136,137,131,127],
[123,106,0,107,112,114,114,113],
[147,131,143,0,127,130,134,124],
[118,114,138,123,0,134,132,113],
[127,113,136,120,116,0,133,142],
[137,119,136,116,118,117,0,125],
[136,123,137,126,137,108,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,94,120,129,143,73,86,79],
[156,0,151,174,176,129,133,120],
[130,99,0,142,110,113,55,119],
[121,76,108,0,132,69,82,101],
[107,74,140,118,0,74,66,95],
[177,121,137,181,176,0,113,115],
[164,117,195,168,184,137,0,146],
[171,130,131,149,155,135,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,129,107,121,109,117,122],
[141,0,137,134,144,124,139,139],
[121,113,0,113,133,126,132,115],
[143,116,137,0,134,136,140,125],
[129,106,117,116,0,131,128,120],
[141,126,124,114,119,0,126,134],
[133,111,118,110,122,124,0,127],
[128,111,135,125,130,116,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,171,139,139,130,121,143],
[111,0,144,113,110,101,120,116],
[79,106,0,110,91,100,91,114],
[111,137,140,0,122,120,121,133],
[111,140,159,128,0,105,134,126],
[120,149,150,130,145,0,148,151],
[129,130,159,129,116,102,0,111],
[107,134,136,117,124,99,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,124,125,123,126,117,127],
[134,0,125,119,128,116,122,124],
[126,125,0,125,120,126,125,121],
[125,131,125,0,134,130,134,127],
[127,122,130,116,0,121,121,123],
[124,134,124,120,129,0,129,128],
[133,128,125,116,129,121,0,115],
[123,126,129,123,127,122,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,115,121,147,122,142,87],
[120,0,118,154,145,91,103,105],
[135,132,0,127,115,126,121,101],
[129,96,123,0,102,142,134,104],
[103,105,135,148,0,128,126,132],
[128,159,124,108,122,0,133,107],
[108,147,129,116,124,117,0,89],
[163,145,149,146,118,143,161,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,103,154,115,137,136],
[114,0,117,114,125,129,130,138],
[124,133,0,126,143,125,143,139],
[147,136,124,0,122,122,146,143],
[96,125,107,128,0,127,139,130],
[135,121,125,128,123,0,130,145],
[113,120,107,104,111,120,0,111],
[114,112,111,107,120,105,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,159,143,125,181,159,166],
[103,0,137,164,102,160,124,131],
[91,113,0,123,106,129,131,131],
[107,86,127,0,91,102,109,125],
[125,148,144,159,0,151,176,152],
[69,90,121,148,99,0,121,128],
[91,126,119,141,74,129,0,102],
[84,119,119,125,98,122,148,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,139,127,127,123,142,128],
[120,0,116,124,102,126,115,99],
[111,134,0,117,112,113,133,106],
[123,126,133,0,121,122,147,122],
[123,148,138,129,0,143,140,134],
[127,124,137,128,107,0,127,115],
[108,135,117,103,110,123,0,107],
[122,151,144,128,116,135,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,146,132,108,140,146,137],
[124,0,145,137,113,143,134,126],
[104,105,0,109,129,119,136,129],
[118,113,141,0,160,135,144,167],
[142,137,121,90,0,146,120,135],
[110,107,131,115,104,0,133,104],
[104,116,114,106,130,117,0,127],
[113,124,121,83,115,146,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,137,135,142,127,119,131],
[125,0,146,138,141,133,125,133],
[113,104,0,116,121,112,103,115],
[115,112,134,0,128,135,119,116],
[108,109,129,122,0,117,114,107],
[123,117,138,115,133,0,112,114],
[131,125,147,131,136,138,0,125],
[119,117,135,134,143,136,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,114,110,97,116,98,128],
[131,0,111,138,128,152,120,126],
[136,139,0,133,136,153,113,135],
[140,112,117,0,112,132,111,107],
[153,122,114,138,0,139,104,114],
[134,98,97,118,111,0,94,115],
[152,130,137,139,146,156,0,122],
[122,124,115,143,136,135,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,198,98,156,39,146,121,155],
[52,0,61,111,2,111,120,60],
[152,189,0,145,139,153,60,153],
[94,139,105,0,44,153,60,103],
[211,248,111,206,0,168,170,169],
[104,139,97,97,82,0,61,60],
[129,130,190,190,80,189,0,189],
[95,190,97,147,81,190,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,149,118,169,147,139,125],
[111,0,137,99,120,135,116,111],
[101,113,0,117,149,147,119,108],
[132,151,133,0,144,134,120,134],
[81,130,101,106,0,124,110,113],
[103,115,103,116,126,0,103,106],
[111,134,131,130,140,147,0,118],
[125,139,142,116,137,144,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,116,112,111,122,121,107],
[120,0,111,93,146,136,121,87],
[134,139,0,112,120,131,130,127],
[138,157,138,0,125,144,158,124],
[139,104,130,125,0,118,131,111],
[128,114,119,106,132,0,122,94],
[129,129,120,92,119,128,0,118],
[143,163,123,126,139,156,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,125,120,121,129,138,135],
[132,0,134,137,133,135,125,137],
[125,116,0,121,117,129,136,132],
[130,113,129,0,129,138,131,123],
[129,117,133,121,0,118,130,126],
[121,115,121,112,132,0,128,129],
[112,125,114,119,120,122,0,118],
[115,113,118,127,124,121,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,126,140,130,119,134,127],
[116,0,119,127,114,104,125,131],
[124,131,0,136,122,133,119,121],
[110,123,114,0,116,106,106,113],
[120,136,128,134,0,122,131,143],
[131,146,117,144,128,0,133,138],
[116,125,131,144,119,117,0,135],
[123,119,129,137,107,112,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,115,122,120,125,139,137],
[131,0,137,128,127,123,133,137],
[135,113,0,142,125,124,123,135],
[128,122,108,0,116,118,126,125],
[130,123,125,134,0,119,136,129],
[125,127,126,132,131,0,129,135],
[111,117,127,124,114,121,0,125],
[113,113,115,125,121,115,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,126,129,123,129,121,127],
[130,0,105,135,112,132,137,106],
[124,145,0,133,116,138,133,137],
[121,115,117,0,125,123,124,111],
[127,138,134,125,0,139,139,121],
[121,118,112,127,111,0,130,119],
[129,113,117,126,111,120,0,118],
[123,144,113,139,129,131,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,128,122,131,124,131,135],
[123,0,133,109,119,110,123,132],
[122,117,0,116,129,116,113,121],
[128,141,134,0,133,125,136,133],
[119,131,121,117,0,115,126,134],
[126,140,134,125,135,0,128,143],
[119,127,137,114,124,122,0,118],
[115,118,129,117,116,107,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,121,131,136,125,127,129],
[111,0,123,112,125,120,120,124],
[129,127,0,128,132,123,112,125],
[119,138,122,0,137,134,117,130],
[114,125,118,113,0,121,116,114],
[125,130,127,116,129,0,127,126],
[123,130,138,133,134,123,0,130],
[121,126,125,120,136,124,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,120,121,122,113,122,123],
[117,0,115,116,110,115,113,131],
[130,135,0,131,115,108,128,132],
[129,134,119,0,114,116,120,124],
[128,140,135,136,0,126,120,130],
[137,135,142,134,124,0,121,132],
[128,137,122,130,130,129,0,126],
[127,119,118,126,120,118,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,120,111,127,113,110,130],
[146,0,131,117,129,119,138,131],
[130,119,0,125,138,122,124,128],
[139,133,125,0,133,120,121,135],
[123,121,112,117,0,114,117,126],
[137,131,128,130,136,0,115,131],
[140,112,126,129,133,135,0,145],
[120,119,122,115,124,119,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,115,109,126,108,122,110],
[123,0,120,105,109,103,137,124],
[135,130,0,101,122,110,125,115],
[141,145,149,0,124,134,157,119],
[124,141,128,126,0,124,129,120],
[142,147,140,116,126,0,139,125],
[128,113,125,93,121,111,0,107],
[140,126,135,131,130,125,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,110,117,107,104,121,118],
[140,0,117,118,125,115,128,124],
[140,133,0,126,120,136,134,122],
[133,132,124,0,123,124,131,141],
[143,125,130,127,0,122,130,129],
[146,135,114,126,128,0,132,126],
[129,122,116,119,120,118,0,121],
[132,126,128,109,121,124,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,127,126,119,114,116,120],
[138,0,120,139,138,117,135,123],
[123,130,0,135,128,109,133,135],
[124,111,115,0,115,116,119,125],
[131,112,122,135,0,123,126,124],
[136,133,141,134,127,0,127,116],
[134,115,117,131,124,123,0,120],
[130,127,115,125,126,134,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,161,186,116,223,152,169,155],
[89,0,80,76,120,70,76,70],
[64,170,0,58,131,117,94,76],
[134,174,192,0,173,128,116,128],
[27,130,119,77,0,37,59,46],
[98,180,133,122,213,0,161,92],
[81,174,156,134,191,89,0,145],
[95,180,174,122,204,158,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,108,126,130,102,97,109],
[148,0,124,139,146,136,124,127],
[142,126,0,142,127,141,123,129],
[124,111,108,0,135,137,118,133],
[120,104,123,115,0,123,116,117],
[148,114,109,113,127,0,118,115],
[153,126,127,132,134,132,0,122],
[141,123,121,117,133,135,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,129,113,118,116,121,121],
[143,0,136,126,142,124,129,132],
[121,114,0,120,119,118,118,118],
[137,124,130,0,131,131,132,129],
[132,108,131,119,0,125,115,112],
[134,126,132,119,125,0,126,136],
[129,121,132,118,135,124,0,125],
[129,118,132,121,138,114,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,146,133,137,129,124,131],
[107,0,134,118,129,118,115,136],
[104,116,0,108,119,117,100,115],
[117,132,142,0,129,111,119,127],
[113,121,131,121,0,110,114,112],
[121,132,133,139,140,0,130,127],
[126,135,150,131,136,120,0,130],
[119,114,135,123,138,123,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,109,132,101,98,130,125],
[151,0,127,139,121,110,142,135],
[141,123,0,142,129,126,132,139],
[118,111,108,0,120,118,125,126],
[149,129,121,130,0,123,129,140],
[152,140,124,132,127,0,138,143],
[120,108,118,125,121,112,0,123],
[125,115,111,124,110,107,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,120,135,131,135,118,117],
[111,0,112,141,117,114,121,108],
[130,138,0,135,124,137,125,123],
[115,109,115,0,116,102,107,116],
[119,133,126,134,0,137,131,132],
[115,136,113,148,113,0,124,118],
[132,129,125,143,119,126,0,118],
[133,142,127,134,118,132,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,123,115,140,109,124,102],
[115,0,121,112,133,95,125,112],
[127,129,0,108,133,113,123,103],
[135,138,142,0,140,114,144,125],
[110,117,117,110,0,113,116,109],
[141,155,137,136,137,0,143,121],
[126,125,127,106,134,107,0,115],
[148,138,147,125,141,129,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,149,101,123,135,131,136],
[128,0,118,146,146,106,119,126],
[101,132,0,120,123,115,128,131],
[149,104,130,0,147,138,122,132],
[127,104,127,103,0,126,108,134],
[115,144,135,112,124,0,110,112],
[119,131,122,128,142,140,0,147],
[114,124,119,118,116,138,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,124,144,123,127,135,130],
[110,0,115,117,121,105,128,120],
[126,135,0,137,123,127,140,134],
[106,133,113,0,104,117,114,115],
[127,129,127,146,0,125,139,138],
[123,145,123,133,125,0,134,132],
[115,122,110,136,111,116,0,123],
[120,130,116,135,112,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,123,141,153,126,99,105],
[101,0,118,142,137,106,110,125],
[127,132,0,117,142,115,92,66],
[109,108,133,0,137,95,101,113],
[97,113,108,113,0,127,94,73],
[124,144,135,155,123,0,147,115],
[151,140,158,149,156,103,0,108],
[145,125,184,137,177,135,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,104,108,112,115,124,114,154],
[146,0,149,123,132,146,143,147],
[142,101,0,119,115,124,120,129],
[138,127,131,0,116,133,135,131],
[135,118,135,134,0,164,146,145],
[126,104,126,117,86,0,112,112],
[136,107,130,115,104,138,0,136],
[96,103,121,119,105,138,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,161,147,136,124,126,131],
[116,0,144,139,128,124,130,147],
[89,106,0,138,117,115,117,133],
[103,111,112,0,118,116,117,115],
[114,122,133,132,0,150,108,116],
[126,126,135,134,100,0,109,115],
[124,120,133,133,142,141,0,127],
[119,103,117,135,134,135,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,82,148,95,121,112,121,84],
[168,0,119,94,85,69,102,98],
[102,131,0,84,128,26,55,98],
[155,156,166,0,130,136,116,114],
[129,165,122,120,0,105,94,65],
[138,181,224,114,145,0,97,154],
[129,148,195,134,156,153,0,104],
[166,152,152,136,185,96,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,141,115,120,129,131,137],
[114,0,124,121,117,137,125,132],
[109,126,0,136,129,125,126,143],
[135,129,114,0,129,134,132,135],
[130,133,121,121,0,134,129,140],
[121,113,125,116,116,0,109,123],
[119,125,124,118,121,141,0,145],
[113,118,107,115,110,127,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,129,126,129,136,122,122],
[140,0,146,131,138,142,145,123],
[121,104,0,121,119,141,136,125],
[124,119,129,0,121,132,139,122],
[121,112,131,129,0,140,140,116],
[114,108,109,118,110,0,116,119],
[128,105,114,111,110,134,0,113],
[128,127,125,128,134,131,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,86,113,129,98,109,131,105],
[164,0,139,138,101,127,138,123],
[137,111,0,113,100,105,120,130],
[121,112,137,0,98,118,101,116],
[152,149,150,152,0,127,120,162],
[141,123,145,132,123,0,146,132],
[119,112,130,149,130,104,0,139],
[145,127,120,134,88,118,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,144,137,128,124,125,124],
[148,0,134,128,130,117,119,158],
[106,116,0,130,106,128,110,118],
[113,122,120,0,91,115,99,109],
[122,120,144,159,0,150,143,145],
[126,133,122,135,100,0,100,143],
[125,131,140,151,107,150,0,141],
[126,92,132,141,105,107,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,111,135,131,125,128,126],
[130,0,121,129,131,117,127,137],
[139,129,0,137,142,119,134,132],
[115,121,113,0,135,124,125,113],
[119,119,108,115,0,129,121,118],
[125,133,131,126,121,0,134,132],
[122,123,116,125,129,116,0,123],
[124,113,118,137,132,118,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,134,132,132,134,129,122],
[114,0,137,123,128,119,116,122],
[116,113,0,109,102,119,99,128],
[118,127,141,0,130,135,125,147],
[118,122,148,120,0,129,132,140],
[116,131,131,115,121,0,124,123],
[121,134,151,125,118,126,0,140],
[128,128,122,103,110,127,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,133,114,128,135,139,124],
[112,0,125,117,125,113,133,127],
[117,125,0,122,117,116,130,124],
[136,133,128,0,123,125,135,121],
[122,125,133,127,0,123,135,126],
[115,137,134,125,127,0,120,131],
[111,117,120,115,115,130,0,125],
[126,123,126,129,124,119,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,123,125,113,108,124,105],
[148,0,130,143,126,130,143,125],
[127,120,0,126,111,118,125,106],
[125,107,124,0,124,113,120,111],
[137,124,139,126,0,119,131,114],
[142,120,132,137,131,0,137,127],
[126,107,125,130,119,113,0,118],
[145,125,144,139,136,123,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,135,130,138,151,122,121],
[147,0,168,146,130,128,134,118],
[115,82,0,143,126,101,75,99],
[120,104,107,0,88,127,117,85],
[112,120,124,162,0,132,123,129],
[99,122,149,123,118,0,107,124],
[128,116,175,133,127,143,0,126],
[129,132,151,165,121,126,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,119,114,99,110,123,119],
[141,0,140,130,131,121,125,134],
[131,110,0,112,93,101,106,119],
[136,120,138,0,114,107,131,119],
[151,119,157,136,0,135,129,131],
[140,129,149,143,115,0,132,133],
[127,125,144,119,121,118,0,123],
[131,116,131,131,119,117,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,118,124,126,112,127,122],
[134,0,127,125,136,130,145,141],
[132,123,0,125,123,116,124,139],
[126,125,125,0,136,119,153,137],
[124,114,127,114,0,111,142,133],
[138,120,134,131,139,0,139,146],
[123,105,126,97,108,111,0,121],
[128,109,111,113,117,104,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,118,133,132,130,133,143],
[122,0,121,128,132,111,125,133],
[132,129,0,131,141,121,122,138],
[117,122,119,0,140,102,113,133],
[118,118,109,110,0,108,104,112],
[120,139,129,148,142,0,126,129],
[117,125,128,137,146,124,0,131],
[107,117,112,117,138,121,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,126,133,132,141,98,146],
[107,0,125,103,119,113,131,134],
[124,125,0,133,124,121,123,136],
[117,147,117,0,132,149,134,155],
[118,131,126,118,0,137,127,139],
[109,137,129,101,113,0,114,159],
[152,119,127,116,123,136,0,170],
[104,116,114,95,111,91,80,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,118,124,112,116,123,115],
[127,0,132,125,111,124,132,127],
[132,118,0,124,114,125,133,119],
[126,125,126,0,121,128,133,125],
[138,139,136,129,0,125,144,137],
[134,126,125,122,125,0,139,126],
[127,118,117,117,106,111,0,115],
[135,123,131,125,113,124,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,174,111,118,128,183,107],
[127,0,151,118,104,130,126,96],
[76,99,0,64,93,95,78,46],
[139,132,186,0,153,111,184,141],
[132,146,157,97,0,162,155,135],
[122,120,155,139,88,0,148,89],
[67,124,172,66,95,102,0,62],
[143,154,204,109,115,161,188,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,125,124,124,111,122,135],
[117,0,115,119,109,108,116,138],
[125,135,0,116,105,109,137,144],
[126,131,134,0,130,105,133,139],
[126,141,145,120,0,129,133,141],
[139,142,141,145,121,0,139,152],
[128,134,113,117,117,111,0,130],
[115,112,106,111,109,98,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,112,120,117,131,135,122],
[125,0,110,127,122,138,133,113],
[138,140,0,127,128,151,143,125],
[130,123,123,0,135,136,127,116],
[133,128,122,115,0,139,138,107],
[119,112,99,114,111,0,117,106],
[115,117,107,123,112,133,0,105],
[128,137,125,134,143,144,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,108,107,117,134,112,108],
[141,0,112,137,129,157,124,135],
[142,138,0,116,131,133,121,139],
[143,113,134,0,133,159,118,150],
[133,121,119,117,0,156,145,144],
[116,93,117,91,94,0,118,120],
[138,126,129,132,105,132,0,141],
[142,115,111,100,106,130,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,118,126,128,119,127,129],
[125,0,127,122,125,122,153,124],
[132,123,0,127,120,131,135,123],
[124,128,123,0,122,128,137,118],
[122,125,130,128,0,131,131,117],
[131,128,119,122,119,0,133,125],
[123,97,115,113,119,117,0,108],
[121,126,127,132,133,125,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,133,141,115,144,140,117],
[127,0,122,122,112,121,137,110],
[117,128,0,143,91,115,141,125],
[109,128,107,0,110,83,102,115],
[135,138,159,140,0,116,123,133],
[106,129,135,167,134,0,139,128],
[110,113,109,148,127,111,0,113],
[133,140,125,135,117,122,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,135,143,109,131,116,123],
[116,0,128,102,111,99,112,140],
[115,122,0,123,87,108,111,110],
[107,148,127,0,86,84,96,109],
[141,139,163,164,0,125,143,139],
[119,151,142,166,125,0,126,145],
[134,138,139,154,107,124,0,157],
[127,110,140,141,111,105,93,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,141,141,112,145,121,146],
[140,0,132,141,136,161,123,151],
[109,118,0,131,117,153,123,143],
[109,109,119,0,113,157,131,133],
[138,114,133,137,0,161,110,150],
[105,89,97,93,89,0,97,105],
[129,127,127,119,140,153,0,137],
[104,99,107,117,100,145,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,104,119,118,116,117,115],
[137,0,143,134,130,130,125,141],
[146,107,0,135,114,124,113,132],
[131,116,115,0,120,119,109,138],
[132,120,136,130,0,128,112,125],
[134,120,126,131,122,0,113,137],
[133,125,137,141,138,137,0,127],
[135,109,118,112,125,113,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,125,133,139,124,128,132],
[133,0,135,133,137,128,125,124],
[125,115,0,119,127,113,121,119],
[117,117,131,0,130,120,109,117],
[111,113,123,120,0,125,120,110],
[126,122,137,130,125,0,115,119],
[122,125,129,141,130,135,0,127],
[118,126,131,133,140,131,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,120,120,122,123,124,136],
[135,0,137,125,133,130,131,141],
[130,113,0,127,123,120,127,135],
[130,125,123,0,130,118,126,142],
[128,117,127,120,0,117,120,125],
[127,120,130,132,133,0,132,135],
[126,119,123,124,130,118,0,134],
[114,109,115,108,125,115,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,116,117,133,107,125,159],
[112,0,108,114,141,123,125,133],
[134,142,0,125,145,144,152,171],
[133,136,125,0,133,115,140,137],
[117,109,105,117,0,112,114,121],
[143,127,106,135,138,0,127,154],
[125,125,98,110,136,123,0,152],
[91,117,79,113,129,96,98,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,119,131,124,121,119,122],
[117,0,117,120,123,120,120,114],
[131,133,0,127,128,138,130,125],
[119,130,123,0,118,126,122,116],
[126,127,122,132,0,130,121,125],
[129,130,112,124,120,0,107,119],
[131,130,120,128,129,143,0,132],
[128,136,125,134,125,131,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,124,120,109,132,130,122],
[115,0,117,120,106,123,125,123],
[126,133,0,120,115,138,127,120],
[130,130,130,0,126,133,129,124],
[141,144,135,124,0,141,136,127],
[118,127,112,117,109,0,126,117],
[120,125,123,121,114,124,0,115],
[128,127,130,126,123,133,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,135,120,118,148,137],
[114,0,130,114,112,125,142,128],
[124,120,0,117,127,120,139,133],
[115,136,133,0,110,132,142,128],
[130,138,123,140,0,120,150,133],
[132,125,130,118,130,0,143,115],
[102,108,111,108,100,107,0,110],
[113,122,117,122,117,135,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,115,122,111,128,107,97],
[136,0,144,147,125,153,135,134],
[135,106,0,129,129,160,119,112],
[128,103,121,0,126,129,99,89],
[139,125,121,124,0,139,93,102],
[122,97,90,121,111,0,93,93],
[143,115,131,151,157,157,0,127],
[153,116,138,161,148,157,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,190,185,119,179,189,140,129],
[60,0,181,117,143,133,159,129],
[65,69,0,23,100,72,146,62],
[131,133,227,0,96,156,172,133],
[71,107,150,154,0,125,163,163],
[61,117,178,94,125,0,123,136],
[110,91,104,78,87,127,0,54],
[121,121,188,117,87,114,196,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,67,67,108,148,108,99],
[137,0,78,75,127,135,102,94],
[183,172,0,108,127,147,132,125],
[183,175,142,0,119,148,133,187],
[142,123,123,131,0,152,128,105],
[102,115,103,102,98,0,77,102],
[142,148,118,117,122,173,0,138],
[151,156,125,63,145,148,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,87,132,129,107,47,82],
[113,0,107,141,120,133,77,97],
[163,143,0,135,164,144,125,120],
[118,109,115,0,115,96,109,109],
[121,130,86,135,0,71,68,65],
[143,117,106,154,179,0,69,84],
[203,173,125,141,182,181,0,142],
[168,153,130,141,185,166,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,164,90,152,172,138,61,166],
[86,0,123,147,110,171,86,112],
[160,127,0,94,129,130,130,160],
[98,103,156,0,98,119,119,86],
[78,140,121,152,0,121,106,125],
[112,79,120,131,129,0,112,78],
[189,164,120,131,144,138,0,145],
[84,138,90,164,125,172,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,152,94,157,128,87,135,94],
[98,0,74,121,97,81,79,78],
[156,176,0,116,126,108,138,107],
[93,129,134,0,82,113,122,116],
[122,153,124,168,0,123,140,138],
[163,169,142,137,127,0,114,99],
[115,171,112,128,110,136,0,107],
[156,172,143,134,112,151,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,124,137,115,139,112,133],
[129,0,121,130,121,123,117,122],
[126,129,0,136,125,140,127,134],
[113,120,114,0,117,114,118,116],
[135,129,125,133,0,145,126,129],
[111,127,110,136,105,0,124,129],
[138,133,123,132,124,126,0,119],
[117,128,116,134,121,121,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,122,122,129,126,123,134],
[134,0,154,125,145,145,139,134],
[128,96,0,105,129,113,116,117],
[128,125,145,0,148,143,118,149],
[121,105,121,102,0,123,91,117],
[124,105,137,107,127,0,118,116],
[127,111,134,132,159,132,0,148],
[116,116,133,101,133,134,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,135,134,125,131,126,136],
[130,0,140,132,123,122,119,132],
[115,110,0,119,121,118,118,124],
[116,118,131,0,127,121,113,123],
[125,127,129,123,0,121,116,131],
[119,128,132,129,129,0,116,127],
[124,131,132,137,134,134,0,129],
[114,118,126,127,119,123,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,102,118,116,144,129,129],
[116,0,101,93,96,134,129,129],
[148,149,0,137,109,142,151,140],
[132,157,113,0,153,157,149,141],
[134,154,141,97,0,140,150,135],
[106,116,108,93,110,0,114,117],
[121,121,99,101,100,136,0,132],
[121,121,110,109,115,133,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,107,152,146,132,138,129],
[118,0,114,129,139,124,125,134],
[143,136,0,168,162,123,146,137],
[98,121,82,0,116,102,111,116],
[104,111,88,134,0,108,106,110],
[118,126,127,148,142,0,146,142],
[112,125,104,139,144,104,0,136],
[121,116,113,134,140,108,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,122,138,139,104,138,103],
[99,0,106,99,86,88,87,69],
[128,144,0,131,131,125,118,104],
[112,151,119,0,134,97,84,101],
[111,164,119,116,0,99,79,69],
[146,162,125,153,151,0,116,130],
[112,163,132,166,171,134,0,101],
[147,181,146,149,181,120,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,168,130,173,118,146,104,166],
[82,0,106,159,106,109,97,100],
[120,144,0,158,80,136,131,86],
[77,91,92,0,75,75,80,100],
[132,144,170,175,0,137,112,101],
[104,141,114,175,113,0,118,122],
[146,153,119,170,138,132,0,146],
[84,150,164,150,149,128,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,135,119,133,127,130,123],
[127,0,124,119,122,117,129,143],
[115,126,0,135,128,129,132,152],
[131,131,115,0,122,131,132,137],
[117,128,122,128,0,123,145,141],
[123,133,121,119,127,0,138,144],
[120,121,118,118,105,112,0,119],
[127,107,98,113,109,106,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,121,133,127,113,117,104],
[142,0,123,129,138,134,155,134],
[129,127,0,114,121,119,117,123],
[117,121,136,0,131,123,124,108],
[123,112,129,119,0,124,110,118],
[137,116,131,127,126,0,128,102],
[133,95,133,126,140,122,0,126],
[146,116,127,142,132,148,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,134,126,125,129,137,138],
[119,0,113,126,116,112,117,125],
[116,137,0,130,122,121,131,134],
[124,124,120,0,117,123,126,140],
[125,134,128,133,0,132,128,140],
[121,138,129,127,118,0,129,144],
[113,133,119,124,122,121,0,146],
[112,125,116,110,110,106,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,135,138,100,125,137,122],
[118,0,122,143,101,105,140,127],
[115,128,0,131,104,118,144,131],
[112,107,119,0,104,116,120,134],
[150,149,146,146,0,110,143,137],
[125,145,132,134,140,0,152,139],
[113,110,106,130,107,98,0,116],
[128,123,119,116,113,111,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,120,108,111,118,123,128],
[132,0,116,105,123,123,130,116],
[130,134,0,113,124,130,143,129],
[142,145,137,0,141,130,145,124],
[139,127,126,109,0,138,142,134],
[132,127,120,120,112,0,139,126],
[127,120,107,105,108,111,0,113],
[122,134,121,126,116,124,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,121,142,140,136,152,138],
[121,0,136,124,131,127,137,133],
[129,114,0,137,143,134,154,159],
[108,126,113,0,142,121,140,138],
[110,119,107,108,0,124,148,130],
[114,123,116,129,126,0,168,130],
[98,113,96,110,102,82,0,111],
[112,117,91,112,120,120,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,117,143,105,107,116,130],
[140,0,123,138,127,124,151,150],
[133,127,0,119,128,132,127,121],
[107,112,131,0,114,111,118,100],
[145,123,122,136,0,141,137,130],
[143,126,118,139,109,0,132,125],
[134,99,123,132,113,118,0,123],
[120,100,129,150,120,125,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,103,134,134,123,125,140],
[103,0,122,107,123,93,115,127],
[147,128,0,103,107,120,118,123],
[116,143,147,0,139,131,120,132],
[116,127,143,111,0,110,116,108],
[127,157,130,119,140,0,127,137],
[125,135,132,130,134,123,0,121],
[110,123,127,118,142,113,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,129,129,132,131,145,128],
[136,0,133,132,116,131,149,133],
[121,117,0,128,121,143,136,125],
[121,118,122,0,116,133,123,119],
[118,134,129,134,0,137,138,146],
[119,119,107,117,113,0,129,123],
[105,101,114,127,112,121,0,117],
[122,117,125,131,104,127,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,124,115,120,125,124,133],
[123,0,125,125,121,119,126,122],
[126,125,0,130,126,111,125,138],
[135,125,120,0,127,122,134,137],
[130,129,124,123,0,126,133,129],
[125,131,139,128,124,0,104,135],
[126,124,125,116,117,146,0,126],
[117,128,112,113,121,115,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,128,126,125,123,127,133],
[124,0,128,129,122,123,117,123],
[122,122,0,129,124,125,126,130],
[124,121,121,0,115,119,122,123],
[125,128,126,135,0,127,127,129],
[127,127,125,131,123,0,122,126],
[123,133,124,128,123,128,0,133],
[117,127,120,127,121,124,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,124,114,116,134,127,120],
[126,0,120,109,130,126,124,139],
[126,130,0,123,121,126,127,155],
[136,141,127,0,120,143,133,152],
[134,120,129,130,0,134,133,125],
[116,124,124,107,116,0,125,130],
[123,126,123,117,117,125,0,134],
[130,111,95,98,125,120,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,118,139,112,119,130,122],
[116,0,112,116,95,97,126,111],
[132,138,0,141,116,133,138,127],
[111,134,109,0,108,114,131,123],
[138,155,134,142,0,122,132,146],
[131,153,117,136,128,0,147,137],
[120,124,112,119,118,103,0,130],
[128,139,123,127,104,113,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,104,117,113,131,115,114],
[143,0,113,131,152,136,126,136],
[146,137,0,136,133,125,133,135],
[133,119,114,0,126,118,122,130],
[137,98,117,124,0,135,120,117],
[119,114,125,132,115,0,126,122],
[135,124,117,128,130,124,0,127],
[136,114,115,120,133,128,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,127,120,112,105,123,89],
[112,0,128,121,119,90,91,90],
[123,122,0,132,122,97,97,68],
[130,129,118,0,139,130,105,125],
[138,131,128,111,0,129,120,97],
[145,160,153,120,121,0,101,116],
[127,159,153,145,130,149,0,118],
[161,160,182,125,153,134,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,129,129,112,136,124,123],
[126,0,136,132,117,126,121,129],
[121,114,0,131,113,113,112,114],
[121,118,119,0,125,125,122,130],
[138,133,137,125,0,131,135,141],
[114,124,137,125,119,0,130,134],
[126,129,138,128,115,120,0,127],
[127,121,136,120,109,116,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,115,113,141,105,141,116],
[123,0,123,132,113,120,104,113],
[135,127,0,109,142,118,127,128],
[137,118,141,0,132,116,108,118],
[109,137,108,118,0,123,111,92],
[145,130,132,134,127,0,128,116],
[109,146,123,142,139,122,0,122],
[134,137,122,132,158,134,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,140,127,129,126,116,136],
[115,0,123,121,120,109,112,139],
[110,127,0,128,121,114,124,129],
[123,129,122,0,125,103,121,137],
[121,130,129,125,0,112,126,126],
[124,141,136,147,138,0,131,131],
[134,138,126,129,124,119,0,127],
[114,111,121,113,124,119,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,120,143,141,153,148,144],
[107,0,114,131,131,123,123,131],
[130,136,0,126,135,125,142,134],
[107,119,124,0,120,140,129,126],
[109,119,115,130,0,121,126,116],
[97,127,125,110,129,0,142,119],
[102,127,108,121,124,108,0,115],
[106,119,116,124,134,131,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,116,143,121,98,124,127],
[138,0,130,155,130,115,124,151],
[134,120,0,137,134,106,118,117],
[107,95,113,0,119,96,124,119],
[129,120,116,131,0,123,118,117],
[152,135,144,154,127,0,125,120],
[126,126,132,126,132,125,0,143],
[123,99,133,131,133,130,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,135,131,140,133,143,122],
[121,0,134,131,136,132,130,123],
[115,116,0,125,123,137,131,129],
[119,119,125,0,125,122,128,122],
[110,114,127,125,0,132,113,125],
[117,118,113,128,118,0,124,113],
[107,120,119,122,137,126,0,120],
[128,127,121,128,125,137,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,118,119,120,121,112,117],
[140,0,137,135,138,137,131,116],
[132,113,0,132,134,117,129,134],
[131,115,118,0,132,118,125,129],
[130,112,116,118,0,115,121,120],
[129,113,133,132,135,0,132,129],
[138,119,121,125,129,118,0,122],
[133,134,116,121,130,121,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,138,140,135,131,128,142],
[128,0,147,144,137,129,125,140],
[112,103,0,132,120,123,117,123],
[110,106,118,0,116,115,104,140],
[115,113,130,134,0,115,105,124],
[119,121,127,135,135,0,118,134],
[122,125,133,146,145,132,0,136],
[108,110,127,110,126,116,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,108,150,115,147,121,118],
[122,0,125,140,129,148,118,129],
[142,125,0,136,112,150,125,128],
[100,110,114,0,104,157,102,135],
[135,121,138,146,0,158,139,138],
[103,102,100,93,92,0,111,119],
[129,132,125,148,111,139,0,121],
[132,121,122,115,112,131,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,130,129,132,124,123,135],
[123,0,115,125,129,126,119,133],
[120,135,0,124,122,128,116,128],
[121,125,126,0,133,142,127,126],
[118,121,128,117,0,124,111,129],
[126,124,122,108,126,0,114,121],
[127,131,134,123,139,136,0,134],
[115,117,122,124,121,129,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,148,108,124,138,127,135],
[125,0,119,127,124,130,132,141],
[102,131,0,104,130,106,122,131],
[142,123,146,0,139,129,138,125],
[126,126,120,111,0,129,125,137],
[112,120,144,121,121,0,114,142],
[123,118,128,112,125,136,0,116],
[115,109,119,125,113,108,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,113,113,122,121,113,120],
[137,0,124,140,137,118,126,126],
[137,126,0,130,137,132,117,129],
[137,110,120,0,127,115,117,127],
[128,113,113,123,0,116,118,124],
[129,132,118,135,134,0,127,142],
[137,124,133,133,132,123,0,127],
[130,124,121,123,126,108,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,93,150,103,162,163,130,125],
[157,0,119,110,157,159,143,102],
[100,131,0,83,85,110,116,83],
[147,140,167,0,149,157,170,106],
[88,93,165,101,0,131,110,132],
[87,91,140,93,119,0,98,102],
[120,107,134,80,140,152,0,128],
[125,148,167,144,118,148,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,119,123,117,146,151,95],
[142,0,140,116,133,145,124,127],
[131,110,0,108,126,131,130,137],
[127,134,142,0,135,126,142,125],
[133,117,124,115,0,122,127,125],
[104,105,119,124,128,0,126,98],
[99,126,120,108,123,124,0,103],
[155,123,113,125,125,152,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,98,145,139,138,121,133],
[106,0,118,137,118,112,121,112],
[152,132,0,141,132,143,128,118],
[105,113,109,0,118,118,109,106],
[111,132,118,132,0,126,106,111],
[112,138,107,132,124,0,105,121],
[129,129,122,141,144,145,0,144],
[117,138,132,144,139,129,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,151,150,136,149,144,172],
[144,0,130,101,156,159,121,141],
[99,120,0,116,123,109,125,135],
[100,149,134,0,159,149,167,130],
[114,94,127,91,0,130,121,142],
[101,91,141,101,120,0,118,106],
[106,129,125,83,129,132,0,120],
[78,109,115,120,108,144,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,100,127,129,142,125,121],
[125,0,110,118,117,139,122,125],
[150,140,0,132,128,150,130,118],
[123,132,118,0,115,136,139,130],
[121,133,122,135,0,144,139,128],
[108,111,100,114,106,0,132,114],
[125,128,120,111,111,118,0,122],
[129,125,132,120,122,136,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,119,123,129,133,132,131],
[119,0,118,108,120,134,116,119],
[131,132,0,128,133,130,126,124],
[127,142,122,0,129,132,126,132],
[121,130,117,121,0,129,116,116],
[117,116,120,118,121,0,125,121],
[118,134,124,124,134,125,0,122],
[119,131,126,118,134,129,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,124,125,141,111,128,122],
[127,0,119,138,130,127,121,113],
[126,131,0,122,130,103,139,121],
[125,112,128,0,132,111,121,115],
[109,120,120,118,0,118,128,120],
[139,123,147,139,132,0,142,129],
[122,129,111,129,122,108,0,113],
[128,137,129,135,130,121,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,97,58,87,128,69,73],
[149,0,127,138,99,143,113,128],
[153,123,0,134,124,133,114,96],
[192,112,116,0,105,122,114,83],
[163,151,126,145,0,117,150,142],
[122,107,117,128,133,0,109,105],
[181,137,136,136,100,141,0,142],
[177,122,154,167,108,145,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 250, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_250.csv", index=False, header=False)