
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,117,130,133,112,86,134,108,162],
[134,0,123,152,132,122,111,99,147],
[121,128,0,126,101,96,128,118,163],
[118,99,125,0,86,109,129,101,150],
[139,119,150,165,0,114,143,138,163],
[165,129,155,142,137,0,119,120,179],
[117,140,123,122,108,132,0,124,186],
[143,152,133,150,113,131,127,0,189],
[89,104,88,101,88,72,65,62,0]])



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
result = np.append(np.array([9, 251, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,132,128,123,122,138,138,121],
[114,0,113,131,117,123,134,129,126],
[119,138,0,135,130,130,129,148,128],
[123,120,116,0,108,118,121,110,134],
[128,134,121,143,0,124,135,131,121],
[129,128,121,133,127,0,132,121,127],
[113,117,122,130,116,119,0,119,131],
[113,122,103,141,120,130,132,0,132],
[130,125,123,117,130,124,120,119,0]])



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
result = np.append(np.array([9, 251, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,125,138,125,130,122,120],
[124,0,131,133,135,129,145,131,129],
[128,120,0,132,136,123,134,127,120],
[126,118,119,0,131,117,145,133,112],
[113,116,115,120,0,116,130,116,106],
[126,122,128,134,135,0,133,137,131],
[121,106,117,106,121,118,0,121,104],
[129,120,124,118,135,114,130,0,117],
[131,122,131,139,145,120,147,134,0]])



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
result = np.append(np.array([9, 251, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,126,118,103,118,139,143,120],
[114,0,99,119,110,114,111,145,126],
[125,152,0,137,113,105,103,144,132],
[133,132,114,0,118,127,129,135,105],
[148,141,138,133,0,129,122,156,116],
[133,137,146,124,122,0,154,168,142],
[112,140,148,122,129,97,0,137,143],
[108,106,107,116,95,83,114,0,134],
[131,125,119,146,135,109,108,117,0]])



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
result = np.append(np.array([9, 251, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,125,119,133,130,131,129,139],
[123,0,113,123,129,129,128,120,146],
[126,138,0,118,122,134,137,128,142],
[132,128,133,0,136,123,139,131,141],
[118,122,129,115,0,129,130,127,144],
[121,122,117,128,122,0,127,123,137],
[120,123,114,112,121,124,0,113,138],
[122,131,123,120,124,128,138,0,136],
[112,105,109,110,107,114,113,115,0]])



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
result = np.append(np.array([9, 251, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,125,127,116,132,133,113,118],
[128,0,122,126,124,123,117,130,122],
[126,129,0,121,122,129,123,130,119],
[124,125,130,0,127,137,126,121,110],
[135,127,129,124,0,123,129,115,113],
[119,128,122,114,128,0,117,118,116],
[118,134,128,125,122,134,0,121,125],
[138,121,121,130,136,133,130,0,127],
[133,129,132,141,138,135,126,124,0]])



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
result = np.append(np.array([9, 251, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,123,138,122,128,117,124,126],
[115,0,125,125,123,118,128,120,110],
[128,126,0,129,124,117,122,118,127],
[113,126,122,0,120,121,117,109,115],
[129,128,127,131,0,120,121,114,116],
[123,133,134,130,131,0,125,122,120],
[134,123,129,134,130,126,0,123,116],
[127,131,133,142,137,129,128,0,124],
[125,141,124,136,135,131,135,127,0]])



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
result = np.append(np.array([9, 251, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,105,106,104,98,106,119,134],
[128,0,128,139,141,121,155,146,144],
[146,123,0,99,139,127,126,148,119],
[145,112,152,0,129,141,160,159,168],
[147,110,112,122,0,135,114,137,121],
[153,130,124,110,116,0,127,150,122],
[145,96,125,91,137,124,0,133,109],
[132,105,103,92,114,101,118,0,141],
[117,107,132,83,130,129,142,110,0]])



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
result = np.append(np.array([9, 251, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,137,141,125,113,167,132,130],
[129,0,120,150,132,130,149,137,136],
[114,131,0,108,117,126,116,125,134],
[110,101,143,0,108,108,138,98,119],
[126,119,134,143,0,127,139,129,130],
[138,121,125,143,124,0,148,104,157],
[84,102,135,113,112,103,0,111,130],
[119,114,126,153,122,147,140,0,138],
[121,115,117,132,121,94,121,113,0]])



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
result = np.append(np.array([9, 251, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,141,107,129,108,134,94,144],
[126,0,135,99,148,154,144,106,134],
[110,116,0,82,99,91,122,127,111],
[144,152,169,0,114,139,155,150,129],
[122,103,152,137,0,118,149,135,130],
[143,97,160,112,133,0,159,128,130],
[117,107,129,96,102,92,0,119,110],
[157,145,124,101,116,123,132,0,107],
[107,117,140,122,121,121,141,144,0]])



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
result = np.append(np.array([9, 251, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,132,123,113,130,135,121,121],
[115,0,101,112,101,110,110,113,104],
[119,150,0,112,114,118,135,133,129],
[128,139,139,0,120,129,134,137,122],
[138,150,137,131,0,119,137,128,128],
[121,141,133,122,132,0,126,127,120],
[116,141,116,117,114,125,0,120,114],
[130,138,118,114,123,124,131,0,123],
[130,147,122,129,123,131,137,128,0]])



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
result = np.append(np.array([9, 251, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,120,116,117,126,124,118,110],
[138,0,133,122,121,125,126,127,134],
[131,118,0,126,116,134,110,126,109],
[135,129,125,0,118,133,134,125,123],
[134,130,135,133,0,126,134,116,114],
[125,126,117,118,125,0,122,123,114],
[127,125,141,117,117,129,0,125,116],
[133,124,125,126,135,128,126,0,129],
[141,117,142,128,137,137,135,122,0]])



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
result = np.append(np.array([9, 251, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,80,103,87,103,68,112,162,107],
[171,0,148,162,136,109,163,182,172],
[148,103,0,138,84,120,129,195,127],
[164,89,113,0,97,69,109,174,154],
[148,115,167,154,0,144,162,198,208],
[183,142,131,182,107,0,178,181,177],
[139,88,122,142,89,73,0,107,121],
[89,69,56,77,53,70,144,0,108],
[144,79,124,97,43,74,130,143,0]])



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
result = np.append(np.array([9, 251, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,121,134,127,130,131,133,127],
[124,0,128,128,133,122,134,133,137],
[130,123,0,134,126,128,133,129,122],
[117,123,117,0,125,130,127,124,116],
[124,118,125,126,0,123,130,130,139],
[121,129,123,121,128,0,120,123,126],
[120,117,118,124,121,131,0,133,128],
[118,118,122,127,121,128,118,0,123],
[124,114,129,135,112,125,123,128,0]])



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
result = np.append(np.array([9, 251, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,135,113,133,132,111,106,96],
[117,0,104,121,118,107,98,112,89],
[116,147,0,129,122,114,138,113,102],
[138,130,122,0,131,134,122,114,103],
[118,133,129,120,0,117,107,99,96],
[119,144,137,117,134,0,143,100,65],
[140,153,113,129,144,108,0,150,82],
[145,139,138,137,152,151,101,0,132],
[155,162,149,148,155,186,169,119,0]])



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
result = np.append(np.array([9, 251, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,119,142,124,125,135,147,132],
[128,0,116,136,114,128,127,130,101],
[132,135,0,131,119,122,133,138,122],
[109,115,120,0,132,106,125,127,114],
[127,137,132,119,0,118,131,122,143],
[126,123,129,145,133,0,134,143,114],
[116,124,118,126,120,117,0,111,108],
[104,121,113,124,129,108,140,0,113],
[119,150,129,137,108,137,143,138,0]])



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
result = np.append(np.array([9, 251, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,134,115,128,145,129,139,147],
[143,0,139,145,171,116,152,178,163],
[117,112,0,150,124,141,154,133,156],
[136,106,101,0,115,102,137,135,163],
[123,80,127,136,0,117,143,151,164],
[106,135,110,149,134,0,146,152,163],
[122,99,97,114,108,105,0,138,153],
[112,73,118,116,100,99,113,0,137],
[104,88,95,88,87,88,98,114,0]])



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
result = np.append(np.array([9, 251, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,142,128,126,121,133,127,123],
[121,0,124,134,116,125,125,124,129],
[109,127,0,125,118,120,140,123,117],
[123,117,126,0,118,120,123,130,120],
[125,135,133,133,0,129,140,131,135],
[130,126,131,131,122,0,132,127,124],
[118,126,111,128,111,119,0,118,119],
[124,127,128,121,120,124,133,0,124],
[128,122,134,131,116,127,132,127,0]])



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
result = np.append(np.array([9, 251, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,138,127,87,108,108,88,121],
[133,0,160,128,104,143,131,108,102],
[113,91,0,127,70,90,84,110,80],
[124,123,124,0,122,125,96,122,109],
[164,147,181,129,0,150,135,125,134],
[143,108,161,126,101,0,118,139,101],
[143,120,167,155,116,133,0,119,127],
[163,143,141,129,126,112,132,0,127],
[130,149,171,142,117,150,124,124,0]])



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
result = np.append(np.array([9, 251, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,128,133,116,129,118,123,122],
[136,0,111,124,118,126,115,126,105],
[123,140,0,123,128,143,123,131,113],
[118,127,128,0,107,142,110,122,103],
[135,133,123,144,0,131,118,133,126],
[122,125,108,109,120,0,130,121,114],
[133,136,128,141,133,121,0,126,114],
[128,125,120,129,118,130,125,0,107],
[129,146,138,148,125,137,137,144,0]])



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
result = np.append(np.array([9, 251, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,139,133,127,131,130,134,129],
[127,0,127,105,125,140,141,135,121],
[112,124,0,127,117,132,130,128,112],
[118,146,124,0,136,144,134,135,133],
[124,126,134,115,0,130,127,143,120],
[120,111,119,107,121,0,114,128,113],
[121,110,121,117,124,137,0,126,115],
[117,116,123,116,108,123,125,0,104],
[122,130,139,118,131,138,136,147,0]])



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
result = np.append(np.array([9, 251, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,123,118,115,120,109,166,104],
[151,0,147,153,117,149,115,158,127],
[128,104,0,130,115,139,96,143,120],
[133,98,121,0,139,133,95,160,139],
[136,134,136,112,0,162,115,190,109],
[131,102,112,118,89,0,123,138,102],
[142,136,155,156,136,128,0,149,116],
[85,93,108,91,61,113,102,0,76],
[147,124,131,112,142,149,135,175,0]])



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
result = np.append(np.array([9, 251, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,96,109,121,112,106,104,97],
[131,0,115,131,134,123,127,132,105],
[155,136,0,138,119,132,144,126,122],
[142,120,113,0,133,131,121,143,105],
[130,117,132,118,0,130,121,135,110],
[139,128,119,120,121,0,134,120,131],
[145,124,107,130,130,117,0,136,105],
[147,119,125,108,116,131,115,0,117],
[154,146,129,146,141,120,146,134,0]])



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
result = np.append(np.array([9, 251, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,133,135,125,130,119,129,127],
[104,0,119,121,122,112,107,105,119],
[118,132,0,120,115,125,115,123,130],
[116,130,131,0,127,116,121,133,128],
[126,129,136,124,0,127,117,136,131],
[121,139,126,135,124,0,111,132,134],
[132,144,136,130,134,140,0,126,121],
[122,146,128,118,115,119,125,0,122],
[124,132,121,123,120,117,130,129,0]])



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
result = np.append(np.array([9, 251, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,125,153,128,149,135,132,123],
[107,0,117,128,126,127,115,118,121],
[126,134,0,143,137,147,133,123,138],
[98,123,108,0,115,121,103,117,97],
[123,125,114,136,0,131,106,118,113],
[102,124,104,130,120,0,112,122,112],
[116,136,118,148,145,139,0,139,134],
[119,133,128,134,133,129,112,0,124],
[128,130,113,154,138,139,117,127,0]])



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
result = np.append(np.array([9, 251, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,125,137,143,135,138,139,142],
[120,0,126,137,132,135,127,140,119],
[126,125,0,132,121,133,120,145,125],
[114,114,119,0,134,119,130,136,126],
[108,119,130,117,0,124,126,133,120],
[116,116,118,132,127,0,120,128,116],
[113,124,131,121,125,131,0,143,117],
[112,111,106,115,118,123,108,0,112],
[109,132,126,125,131,135,134,139,0]])



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
result = np.append(np.array([9, 251, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,121,112,97,165,126,110,110],
[151,0,135,115,134,200,113,84,125],
[130,116,0,111,142,169,114,135,135],
[139,136,140,0,141,174,132,112,147],
[154,117,109,110,0,117,119,134,154],
[86,51,82,77,134,0,76,68,89],
[125,138,137,119,132,175,0,124,107],
[141,167,116,139,117,183,127,0,130],
[141,126,116,104,97,162,144,121,0]])



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
result = np.append(np.array([9, 251, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,134,166,166,105,122,107,152],
[129,0,70,150,137,121,106,119,88],
[117,181,0,190,117,101,126,129,116],
[85,101,61,0,93,61,42,73,61],
[85,114,134,158,0,111,124,67,114],
[146,130,150,190,140,0,151,132,106],
[129,145,125,209,127,100,0,109,113],
[144,132,122,178,184,119,142,0,106],
[99,163,135,190,137,145,138,145,0]])



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
result = np.append(np.array([9, 251, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,132,122,138,134,138,115,133],
[125,0,128,127,128,132,133,117,119],
[119,123,0,115,122,110,130,123,128],
[129,124,136,0,122,133,124,132,125],
[113,123,129,129,0,112,124,116,118],
[117,119,141,118,139,0,134,128,126],
[113,118,121,127,127,117,0,112,121],
[136,134,128,119,135,123,139,0,128],
[118,132,123,126,133,125,130,123,0]])



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
result = np.append(np.array([9, 251, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,148,95,127,114,106,114,100],
[141,0,148,117,129,112,109,130,149],
[103,103,0,92,103,106,78,122,103],
[156,134,159,0,116,124,111,132,132],
[124,122,148,135,0,115,138,125,131],
[137,139,145,127,136,0,133,141,112],
[145,142,173,140,113,118,0,163,135],
[137,121,129,119,126,110,88,0,104],
[151,102,148,119,120,139,116,147,0]])



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
result = np.append(np.array([9, 251, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,158,141,148,151,164,145,122],
[101,0,129,122,136,119,139,117,128],
[93,122,0,104,115,144,115,97,95],
[110,129,147,0,147,121,152,127,131],
[103,115,136,104,0,112,149,110,129],
[100,132,107,130,139,0,142,121,115],
[87,112,136,99,102,109,0,114,86],
[106,134,154,124,141,130,137,0,114],
[129,123,156,120,122,136,165,137,0]])



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
result = np.append(np.array([9, 251, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,143,134,129,138,133,120,124],
[110,0,104,106,107,130,117,113,111],
[108,147,0,127,98,125,111,115,126],
[117,145,124,0,106,122,124,118,122],
[122,144,153,145,0,151,136,132,126],
[113,121,126,129,100,0,113,112,115],
[118,134,140,127,115,138,0,114,120],
[131,138,136,133,119,139,137,0,129],
[127,140,125,129,125,136,131,122,0]])



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
result = np.append(np.array([9, 251, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,112,108,116,120,131,129,127],
[114,0,82,102,121,133,113,96,111],
[139,169,0,135,162,156,142,141,119],
[143,149,116,0,156,128,140,129,124],
[135,130,89,95,0,106,130,124,114],
[131,118,95,123,145,0,92,112,122],
[120,138,109,111,121,159,0,105,128],
[122,155,110,122,127,139,146,0,119],
[124,140,132,127,137,129,123,132,0]])



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
result = np.append(np.array([9, 251, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,120,108,127,134,114,130,137],
[125,0,115,113,108,139,120,122,137],
[131,136,0,114,135,155,122,130,147],
[143,138,137,0,126,157,116,128,142],
[124,143,116,125,0,136,136,136,140],
[117,112,96,94,115,0,118,105,119],
[137,131,129,135,115,133,0,134,129],
[121,129,121,123,115,146,117,0,142],
[114,114,104,109,111,132,122,109,0]])



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
result = np.append(np.array([9, 251, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,115,117,131,124,136,112,125],
[123,0,119,131,122,128,136,113,106],
[136,132,0,123,131,114,131,122,127],
[134,120,128,0,130,133,142,114,120],
[120,129,120,121,0,119,124,106,116],
[127,123,137,118,132,0,130,119,126],
[115,115,120,109,127,121,0,123,112],
[139,138,129,137,145,132,128,0,107],
[126,145,124,131,135,125,139,144,0]])



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
result = np.append(np.array([9, 251, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,121,113,114,129,132,124,115],
[131,0,129,124,118,144,139,133,113],
[130,122,0,113,119,132,124,131,124],
[138,127,138,0,132,133,139,139,124],
[137,133,132,119,0,139,129,127,131],
[122,107,119,118,112,0,131,121,114],
[119,112,127,112,122,120,0,121,120],
[127,118,120,112,124,130,130,0,125],
[136,138,127,127,120,137,131,126,0]])



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
result = np.append(np.array([9, 251, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,69,79,78,67,155,80,78],
[177,0,110,127,114,121,206,151,140],
[182,141,0,116,145,153,172,138,181],
[172,124,135,0,155,144,192,150,155],
[173,137,106,96,0,144,186,140,180],
[184,130,98,107,107,0,202,153,159],
[96,45,79,59,65,49,0,94,85],
[171,100,113,101,111,98,157,0,116],
[173,111,70,96,71,92,166,135,0]])



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
result = np.append(np.array([9, 251, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,114,138,126,134,139,142,112],
[133,0,116,142,142,140,129,141,129],
[137,135,0,149,120,131,127,133,136],
[113,109,102,0,115,128,123,129,111],
[125,109,131,136,0,133,116,127,136],
[117,111,120,123,118,0,109,115,116],
[112,122,124,128,135,142,0,130,99],
[109,110,118,122,124,136,121,0,113],
[139,122,115,140,115,135,152,138,0]])



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
result = np.append(np.array([9, 251, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,141,142,128,133,126,144,127],
[130,0,130,125,131,133,121,144,130],
[110,121,0,134,124,115,114,127,113],
[109,126,117,0,116,113,114,131,116],
[123,120,127,135,0,116,123,138,121],
[118,118,136,138,135,0,126,129,125],
[125,130,137,137,128,125,0,133,127],
[107,107,124,120,113,122,118,0,109],
[124,121,138,135,130,126,124,142,0]])



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
result = np.append(np.array([9, 251, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,133,121,146,135,137,130,140],
[123,0,142,128,134,139,143,128,121],
[118,109,0,104,115,119,125,106,125],
[130,123,147,0,143,120,126,121,128],
[105,117,136,108,0,129,112,127,121],
[116,112,132,131,122,0,113,120,136],
[114,108,126,125,139,138,0,119,122],
[121,123,145,130,124,131,132,0,123],
[111,130,126,123,130,115,129,128,0]])



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
result = np.append(np.array([9, 251, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,134,134,119,118,129,130,131],
[117,0,134,134,106,125,117,130,124],
[117,117,0,116,118,98,110,115,132],
[117,117,135,0,105,114,109,122,128],
[132,145,133,146,0,129,120,130,139],
[133,126,153,137,122,0,131,125,136],
[122,134,141,142,131,120,0,128,131],
[121,121,136,129,121,126,123,0,122],
[120,127,119,123,112,115,120,129,0]])



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
result = np.append(np.array([9, 251, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,96,77,130,123,79,119,83,91],
[155,0,124,122,147,128,158,112,129],
[174,127,0,129,125,108,143,127,123],
[121,129,122,0,149,87,159,96,87],
[128,104,126,102,0,80,163,102,108],
[172,123,143,164,171,0,140,147,139],
[132,93,108,92,88,111,0,100,113],
[168,139,124,155,149,104,151,0,134],
[160,122,128,164,143,112,138,117,0]])



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
result = np.append(np.array([9, 251, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,133,125,118,130,127,125,132],
[117,0,111,115,127,127,121,123,119],
[118,140,0,123,127,121,129,124,120],
[126,136,128,0,136,132,118,140,127],
[133,124,124,115,0,127,110,136,129],
[121,124,130,119,124,0,121,134,115],
[124,130,122,133,141,130,0,130,143],
[126,128,127,111,115,117,121,0,122],
[119,132,131,124,122,136,108,129,0]])



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
result = np.append(np.array([9, 251, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,117,132,127,126,132,121,141],
[124,0,113,153,118,147,123,137,142],
[134,138,0,132,109,149,127,130,136],
[119,98,119,0,123,130,119,129,119],
[124,133,142,128,0,154,141,141,151],
[125,104,102,121,97,0,118,128,127],
[119,128,124,132,110,133,0,116,125],
[130,114,121,122,110,123,135,0,127],
[110,109,115,132,100,124,126,124,0]])



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
result = np.append(np.array([9, 251, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,113,127,125,133,126,112,96],
[123,0,110,119,118,124,126,125,108],
[138,141,0,142,109,125,143,122,117],
[124,132,109,0,119,118,126,129,112],
[126,133,142,132,0,139,129,111,127],
[118,127,126,133,112,0,123,116,116],
[125,125,108,125,122,128,0,118,107],
[139,126,129,122,140,135,133,0,122],
[155,143,134,139,124,135,144,129,0]])



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
result = np.append(np.array([9, 251, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,132,123,132,131,118,126,119],
[135,0,121,130,129,136,120,104,113],
[119,130,0,123,132,119,119,121,117],
[128,121,128,0,142,142,130,131,125],
[119,122,119,109,0,123,112,114,109],
[120,115,132,109,128,0,115,124,120],
[133,131,132,121,139,136,0,122,133],
[125,147,130,120,137,127,129,0,127],
[132,138,134,126,142,131,118,124,0]])



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
result = np.append(np.array([9, 251, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,119,169,108,129,114,127,135],
[130,0,84,122,101,115,79,122,118],
[132,167,0,165,130,161,116,155,141],
[82,129,86,0,133,125,120,112,160],
[143,150,121,118,0,155,92,127,147],
[122,136,90,126,96,0,121,116,137],
[137,172,135,131,159,130,0,113,109],
[124,129,96,139,124,135,138,0,141],
[116,133,110,91,104,114,142,110,0]])



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
result = np.append(np.array([9, 251, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,149,133,128,144,117,129,128],
[132,0,141,140,116,130,110,127,142],
[102,110,0,118,112,110,107,111,101],
[118,111,133,0,127,124,117,115,112],
[123,135,139,124,0,137,126,126,118],
[107,121,141,127,114,0,99,120,121],
[134,141,144,134,125,152,0,141,150],
[122,124,140,136,125,131,110,0,128],
[123,109,150,139,133,130,101,123,0]])



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
result = np.append(np.array([9, 251, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,114,117,127,117,94,105,112],
[137,0,129,125,110,117,100,107,118],
[137,122,0,131,134,119,110,119,132],
[134,126,120,0,130,123,111,124,130],
[124,141,117,121,0,116,100,102,112],
[134,134,132,128,135,0,111,115,133],
[157,151,141,140,151,140,0,120,138],
[146,144,132,127,149,136,131,0,124],
[139,133,119,121,139,118,113,127,0]])



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
result = np.append(np.array([9, 251, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,171,188,127,129,170,205,158,117],
[80,0,142,123,96,143,150,90,79],
[63,109,0,116,88,108,117,90,90],
[124,128,135,0,96,164,141,112,126],
[122,155,163,155,0,145,178,135,115],
[81,108,143,87,106,0,116,102,92],
[46,101,134,110,73,135,0,109,79],
[93,161,161,139,116,149,142,0,107],
[134,172,161,125,136,159,172,144,0]])



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
result = np.append(np.array([9, 251, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,172,142,94,124,136,169,112,145],
[79,0,103,36,57,91,140,0,82],
[109,148,0,69,61,94,143,139,114],
[157,215,182,0,91,169,209,112,182],
[127,194,190,160,0,112,191,194,160],
[115,160,157,82,139,0,145,127,160],
[82,111,108,42,60,106,0,78,111],
[139,251,112,139,57,124,173,0,112],
[106,169,137,69,91,91,140,139,0]])



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
result = np.append(np.array([9, 251, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,112,119,122,114,118,135,119],
[140,0,134,130,122,132,120,131,122],
[139,117,0,126,134,138,137,145,130],
[132,121,125,0,127,131,138,145,122],
[129,129,117,124,0,131,128,132,129],
[137,119,113,120,120,0,117,142,128],
[133,131,114,113,123,134,0,150,125],
[116,120,106,106,119,109,101,0,115],
[132,129,121,129,122,123,126,136,0]])



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
result = np.append(np.array([9, 251, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,125,141,115,116,107,120,117],
[124,0,132,124,127,113,103,137,141],
[126,119,0,123,113,105,120,121,117],
[110,127,128,0,104,130,120,97,134],
[136,124,138,147,0,122,116,130,106],
[135,138,146,121,129,0,137,105,111],
[144,148,131,131,135,114,0,138,143],
[131,114,130,154,121,146,113,0,149],
[134,110,134,117,145,140,108,102,0]])



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
result = np.append(np.array([9, 251, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,110,127,119,126,110,123,107],
[153,0,143,145,132,142,141,155,123],
[141,108,0,135,119,149,125,134,114],
[124,106,116,0,109,126,113,117,112],
[132,119,132,142,0,151,129,144,119],
[125,109,102,125,100,0,118,126,111],
[141,110,126,138,122,133,0,148,128],
[128,96,117,134,107,125,103,0,121],
[144,128,137,139,132,140,123,130,0]])



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
result = np.append(np.array([9, 251, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,122,134,129,129,127,125,131],
[122,0,141,135,129,135,128,122,134],
[129,110,0,125,122,121,119,126,132],
[117,116,126,0,122,118,127,122,130],
[122,122,129,129,0,121,115,133,126],
[122,116,130,133,130,0,125,119,120],
[124,123,132,124,136,126,0,129,132],
[126,129,125,129,118,132,122,0,127],
[120,117,119,121,125,131,119,124,0]])



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
result = np.append(np.array([9, 251, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,104,102,113,105,132,101,102],
[145,0,116,125,136,117,143,123,130],
[147,135,0,133,141,145,145,129,120],
[149,126,118,0,152,127,131,137,118],
[138,115,110,99,0,110,120,106,110],
[146,134,106,124,141,0,158,127,133],
[119,108,106,120,131,93,0,126,100],
[150,128,122,114,145,124,125,0,122],
[149,121,131,133,141,118,151,129,0]])



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
result = np.append(np.array([9, 251, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,135,130,128,136,119,120,141],
[121,0,118,124,121,121,129,125,133],
[116,133,0,125,124,132,134,121,121],
[121,127,126,0,129,132,121,130,125],
[123,130,127,122,0,126,130,128,125],
[115,130,119,119,125,0,128,126,117],
[132,122,117,130,121,123,0,109,114],
[131,126,130,121,123,125,142,0,115],
[110,118,130,126,126,134,137,136,0]])



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
result = np.append(np.array([9, 251, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,140,155,115,143,146,132,107],
[107,0,137,145,109,135,151,133,115],
[111,114,0,139,123,143,144,127,131],
[96,106,112,0,93,127,124,106,117],
[136,142,128,158,0,159,136,118,112],
[108,116,108,124,92,0,135,113,110],
[105,100,107,127,115,116,0,113,105],
[119,118,124,145,133,138,138,0,100],
[144,136,120,134,139,141,146,151,0]])



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
result = np.append(np.array([9, 251, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,127,119,126,130,119,116,123],
[129,0,135,126,138,136,110,137,139],
[124,116,0,123,124,119,116,121,118],
[132,125,128,0,133,119,126,122,129],
[125,113,127,118,0,119,108,128,125],
[121,115,132,132,132,0,112,123,124],
[132,141,135,125,143,139,0,136,137],
[135,114,130,129,123,128,115,0,123],
[128,112,133,122,126,127,114,128,0]])



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
result = np.append(np.array([9, 251, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,154,157,125,124,148,148,135],
[109,0,170,156,65,100,118,148,109],
[97,81,0,120,78,78,110,122,108],
[94,95,131,0,86,83,81,153,71],
[126,186,173,165,0,121,172,192,145],
[127,151,173,168,130,0,110,200,139],
[103,133,141,170,79,141,0,154,125],
[103,103,129,98,59,51,97,0,66],
[116,142,143,180,106,112,126,185,0]])



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
result = np.append(np.array([9, 251, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,139,129,133,132,127,117,131],
[134,0,129,122,132,133,115,123,120],
[112,122,0,124,127,127,113,110,121],
[122,129,127,0,133,129,132,119,132],
[118,119,124,118,0,130,118,110,125],
[119,118,124,122,121,0,139,122,121],
[124,136,138,119,133,112,0,128,127],
[134,128,141,132,141,129,123,0,143],
[120,131,130,119,126,130,124,108,0]])



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
result = np.append(np.array([9, 251, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,117,129,118,128,132,128,133],
[135,0,123,125,129,135,138,139,135],
[134,128,0,137,125,136,142,134,135],
[122,126,114,0,127,123,121,129,118],
[133,122,126,124,0,131,126,138,132],
[123,116,115,128,120,0,127,138,133],
[119,113,109,130,125,124,0,135,136],
[123,112,117,122,113,113,116,0,128],
[118,116,116,133,119,118,115,123,0]])



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
result = np.append(np.array([9, 251, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,127,132,130,127,114,116,141],
[127,0,127,135,144,138,137,115,136],
[124,124,0,124,131,152,129,128,122],
[119,116,127,0,127,132,117,103,120],
[121,107,120,124,0,130,141,101,120],
[124,113,99,119,121,0,109,104,126],
[137,114,122,134,110,142,0,111,129],
[135,136,123,148,150,147,140,0,158],
[110,115,129,131,131,125,122,93,0]])



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
result = np.append(np.array([9, 251, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,125,137,147,131,127,127,131],
[124,0,124,118,125,129,128,117,123],
[126,127,0,121,144,137,118,123,134],
[114,133,130,0,132,129,120,129,140],
[104,126,107,119,0,124,126,116,120],
[120,122,114,122,127,0,124,113,127],
[124,123,133,131,125,127,0,117,126],
[124,134,128,122,135,138,134,0,131],
[120,128,117,111,131,124,125,120,0]])



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
result = np.append(np.array([9, 251, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,91,143,133,137,120,107,92,86],
[160,0,145,90,125,117,123,121,107],
[108,106,0,124,147,125,151,120,118],
[118,161,127,0,121,111,108,156,111],
[114,126,104,130,0,111,84,103,114],
[131,134,126,140,140,0,84,130,91],
[144,128,100,143,167,167,0,106,147],
[159,130,131,95,148,121,145,0,114],
[165,144,133,140,137,160,104,137,0]])



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
result = np.append(np.array([9, 251, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,110,122,133,128,134,112,140],
[116,0,98,117,100,126,112,135,128],
[141,153,0,157,116,130,139,133,137],
[129,134,94,0,112,128,105,118,124],
[118,151,135,139,0,142,112,124,143],
[123,125,121,123,109,0,106,111,123],
[117,139,112,146,139,145,0,119,139],
[139,116,118,133,127,140,132,0,146],
[111,123,114,127,108,128,112,105,0]])



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
result = np.append(np.array([9, 251, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,121,132,102,115,126,112,110],
[135,0,131,146,138,127,130,130,118],
[130,120,0,132,131,129,119,131,127],
[119,105,119,0,103,113,116,116,113],
[149,113,120,148,0,133,146,124,112],
[136,124,122,138,118,0,125,126,120],
[125,121,132,135,105,126,0,125,130],
[139,121,120,135,127,125,126,0,126],
[141,133,124,138,139,131,121,125,0]])



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
result = np.append(np.array([9, 251, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,112,141,92,110,123,128,142],
[136,0,113,114,84,113,111,116,106],
[139,138,0,145,117,129,114,121,151],
[110,137,106,0,81,114,70,115,117],
[159,167,134,170,0,125,105,117,178],
[141,138,122,137,126,0,123,123,171],
[128,140,137,181,146,128,0,100,130],
[123,135,130,136,134,128,151,0,146],
[109,145,100,134,73,80,121,105,0]])



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
result = np.append(np.array([9, 251, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,122,125,119,119,122,123,125],
[126,0,123,120,116,117,110,117,111],
[129,128,0,123,122,136,130,122,132],
[126,131,128,0,124,121,126,133,127],
[132,135,129,127,0,127,126,126,124],
[132,134,115,130,124,0,125,129,132],
[129,141,121,125,125,126,0,118,133],
[128,134,129,118,125,122,133,0,128],
[126,140,119,124,127,119,118,123,0]])



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
result = np.append(np.array([9, 251, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,133,143,127,130,127,122,128],
[141,0,129,132,137,121,139,127,139],
[118,122,0,119,118,130,121,116,129],
[108,119,132,0,114,123,119,128,131],
[124,114,133,137,0,126,135,126,128],
[121,130,121,128,125,0,130,125,121],
[124,112,130,132,116,121,0,121,115],
[129,124,135,123,125,126,130,0,132],
[123,112,122,120,123,130,136,119,0]])



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
result = np.append(np.array([9, 251, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,120,125,114,119,121,118,116],
[135,0,129,127,129,127,126,137,124],
[131,122,0,125,117,128,132,116,114],
[126,124,126,0,117,128,128,118,121],
[137,122,134,134,0,132,131,133,129],
[132,124,123,123,119,0,119,121,127],
[130,125,119,123,120,132,0,130,118],
[133,114,135,133,118,130,121,0,113],
[135,127,137,130,122,124,133,138,0]])



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
result = np.append(np.array([9, 251, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,134,125,114,128,119,109],
[115,0,117,139,126,110,122,129,111],
[125,134,0,137,127,99,143,134,109],
[117,112,114,0,127,123,145,103,112],
[126,125,124,124,0,128,134,117,102],
[137,141,152,128,123,0,126,142,142],
[123,129,108,106,117,125,0,123,107],
[132,122,117,148,134,109,128,0,108],
[142,140,142,139,149,109,144,143,0]])



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
result = np.append(np.array([9, 251, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,131,116,113,140,128,116,134],
[134,0,127,130,122,136,123,129,127],
[120,124,0,107,130,118,141,113,131],
[135,121,144,0,126,126,112,105,128],
[138,129,121,125,0,121,124,125,114],
[111,115,133,125,130,0,102,108,118],
[123,128,110,139,127,149,0,122,130],
[135,122,138,146,126,143,129,0,135],
[117,124,120,123,137,133,121,116,0]])



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
result = np.append(np.array([9, 251, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,145,108,113,122,109,121,121],
[128,0,156,105,133,135,138,120,124],
[106,95,0,110,96,99,120,102,108],
[143,146,141,0,127,147,132,129,122],
[138,118,155,124,0,156,132,124,140],
[129,116,152,104,95,0,125,108,118],
[142,113,131,119,119,126,0,124,128],
[130,131,149,122,127,143,127,0,129],
[130,127,143,129,111,133,123,122,0]])



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
result = np.append(np.array([9, 251, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,133,108,117,130,98,117,116],
[135,0,125,90,122,150,110,102,115],
[118,126,0,120,132,150,137,112,111],
[143,161,131,0,141,130,125,122,95],
[134,129,119,110,0,122,100,99,134],
[121,101,101,121,129,0,116,109,86],
[153,141,114,126,151,135,0,112,103],
[134,149,139,129,152,142,139,0,120],
[135,136,140,156,117,165,148,131,0]])



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
result = np.append(np.array([9, 251, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,122,125,125,127,111,119,121],
[131,0,133,129,134,127,125,134,126],
[129,118,0,130,132,114,121,142,123],
[126,122,121,0,132,103,130,135,118],
[126,117,119,119,0,112,119,136,130],
[124,124,137,148,139,0,125,133,126],
[140,126,130,121,132,126,0,128,119],
[132,117,109,116,115,118,123,0,127],
[130,125,128,133,121,125,132,124,0]])



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
result = np.append(np.array([9, 251, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,130,138,123,120,122,133,126],
[120,0,130,137,134,119,130,118,124],
[121,121,0,128,122,124,128,121,116],
[113,114,123,0,126,110,118,122,122],
[128,117,129,125,0,130,127,126,128],
[131,132,127,141,121,0,139,124,134],
[129,121,123,133,124,112,0,117,128],
[118,133,130,129,125,127,134,0,119],
[125,127,135,129,123,117,123,132,0]])



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
result = np.append(np.array([9, 251, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,127,107,114,117,134,133,123],
[131,0,122,121,114,117,126,124,124],
[124,129,0,117,112,124,118,136,136],
[144,130,134,0,116,133,128,150,149],
[137,137,139,135,0,122,133,146,142],
[134,134,127,118,129,0,122,137,131],
[117,125,133,123,118,129,0,132,126],
[118,127,115,101,105,114,119,0,116],
[128,127,115,102,109,120,125,135,0]])



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
result = np.append(np.array([9, 251, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,112,152,135,126,137,136,111],
[135,0,120,145,145,126,136,146,121],
[139,131,0,151,148,138,134,145,123],
[99,106,100,0,118,108,116,113,113],
[116,106,103,133,0,110,122,127,106],
[125,125,113,143,141,0,127,122,129],
[114,115,117,135,129,124,0,126,115],
[115,105,106,138,124,129,125,0,98],
[140,130,128,138,145,122,136,153,0]])



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
result = np.append(np.array([9, 251, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,160,130,150,151,90,148,123],
[144,0,156,170,173,163,111,170,135],
[91,95,0,135,137,130,90,114,115],
[121,81,116,0,124,140,126,123,110],
[101,78,114,127,0,144,95,125,122],
[100,88,121,111,107,0,92,98,92],
[161,140,161,125,156,159,0,171,150],
[103,81,137,128,126,153,80,0,126],
[128,116,136,141,129,159,101,125,0]])



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
result = np.append(np.array([9, 251, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,114,122,124,134,121,112,116],
[128,0,120,130,128,124,132,120,134],
[137,131,0,137,136,135,127,127,125],
[129,121,114,0,120,131,115,105,126],
[127,123,115,131,0,141,129,124,130],
[117,127,116,120,110,0,125,111,118],
[130,119,124,136,122,126,0,111,126],
[139,131,124,146,127,140,140,0,132],
[135,117,126,125,121,133,125,119,0]])



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
result = np.append(np.array([9, 251, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,128,139,112,138,134,110,118],
[116,0,136,114,129,127,128,134,116],
[123,115,0,128,124,144,145,146,133],
[112,137,123,0,116,130,123,104,116],
[139,122,127,135,0,132,112,124,128],
[113,124,107,121,119,0,122,106,128],
[117,123,106,128,139,129,0,118,122],
[141,117,105,147,127,145,133,0,127],
[133,135,118,135,123,123,129,124,0]])



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
result = np.append(np.array([9, 251, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,114,136,126,123,124,125,123],
[130,0,125,131,129,134,126,130,129],
[137,126,0,134,126,125,131,127,127],
[115,120,117,0,115,110,129,116,120],
[125,122,125,136,0,119,138,110,119],
[128,117,126,141,132,0,128,129,135],
[127,125,120,122,113,123,0,104,117],
[126,121,124,135,141,122,147,0,132],
[128,122,124,131,132,116,134,119,0]])



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
result = np.append(np.array([9, 251, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,129,133,117,119,133,126,122],
[128,0,162,137,132,139,157,131,104],
[122,89,0,115,98,122,128,126,104],
[118,114,136,0,94,136,135,132,113],
[134,119,153,157,0,158,150,129,130],
[132,112,129,115,93,0,122,118,82],
[118,94,123,116,101,129,0,104,102],
[125,120,125,119,122,133,147,0,102],
[129,147,147,138,121,169,149,149,0]])



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
result = np.append(np.array([9, 251, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,140,120,126,151,136,151,144],
[122,0,152,132,119,127,148,152,131],
[111,99,0,94,97,118,110,136,121],
[131,119,157,0,109,117,129,144,123],
[125,132,154,142,0,145,170,137,127],
[100,124,133,134,106,0,143,124,121],
[115,103,141,122,81,108,0,138,102],
[100,99,115,107,114,127,113,0,90],
[107,120,130,128,124,130,149,161,0]])



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
result = np.append(np.array([9, 251, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,113,105,87,113,136,136,105],
[115,0,131,85,112,125,125,117,109],
[138,120,0,95,109,115,113,126,96],
[146,166,156,0,128,140,121,124,129],
[164,139,142,123,0,139,149,155,151],
[138,126,136,111,112,0,131,146,139],
[115,126,138,130,102,120,0,151,142],
[115,134,125,127,96,105,100,0,121],
[146,142,155,122,100,112,109,130,0]])



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
result = np.append(np.array([9, 251, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,125,141,133,143,129,123,125],
[126,0,122,126,132,131,131,132,128],
[126,129,0,126,129,143,128,120,123],
[110,125,125,0,129,139,124,126,109],
[118,119,122,122,0,138,125,120,128],
[108,120,108,112,113,0,125,125,109],
[122,120,123,127,126,126,0,118,125],
[128,119,131,125,131,126,133,0,115],
[126,123,128,142,123,142,126,136,0]])



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
result = np.append(np.array([9, 251, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,134,121,124,133,124,119,93],
[137,0,164,148,144,130,123,136,132],
[117,87,0,107,94,112,93,119,102],
[130,103,144,0,113,146,112,109,120],
[127,107,157,138,0,128,130,117,104],
[118,121,139,105,123,0,117,120,106],
[127,128,158,139,121,134,0,112,120],
[132,115,132,142,134,131,139,0,136],
[158,119,149,131,147,145,131,115,0]])



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
result = np.append(np.array([9, 251, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,89,144,165,92,75,195,135,151],
[162,0,112,204,144,171,221,198,198],
[107,139,0,169,169,152,169,169,152],
[86,47,82,0,69,125,113,141,95],
[159,107,82,182,0,125,199,198,198],
[176,80,99,126,126,0,156,146,158],
[56,30,82,138,52,95,0,66,77],
[116,53,82,110,53,105,185,0,188],
[100,53,99,156,53,93,174,63,0]])



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
result = np.append(np.array([9, 251, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,76,123,76,136,147,128,103],
[115,0,109,166,113,122,100,137,99],
[175,142,0,164,96,149,110,125,70],
[128,85,87,0,115,100,100,114,88],
[175,138,155,136,0,121,110,112,179],
[115,129,102,151,130,0,93,127,88],
[104,151,141,151,141,158,0,134,155],
[123,114,126,137,139,124,117,0,141],
[148,152,181,163,72,163,96,110,0]])



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
result = np.append(np.array([9, 251, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,122,120,133,134,111,108,114],
[112,0,113,108,105,119,100,103,111],
[129,138,0,124,135,138,125,131,124],
[131,143,127,0,136,129,123,121,133],
[118,146,116,115,0,121,127,119,117],
[117,132,113,122,130,0,129,110,115],
[140,151,126,128,124,122,0,111,118],
[143,148,120,130,132,141,140,0,121],
[137,140,127,118,134,136,133,130,0]])



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
result = np.append(np.array([9, 251, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,141,142,109,112,87,106,122],
[144,0,159,163,131,130,141,159,113],
[110,92,0,148,119,123,137,103,91],
[109,88,103,0,94,115,124,120,79],
[142,120,132,157,0,120,133,131,88],
[139,121,128,136,131,0,146,129,152],
[164,110,114,127,118,105,0,101,121],
[145,92,148,131,120,122,150,0,110],
[129,138,160,172,163,99,130,141,0]])



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
result = np.append(np.array([9, 251, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,130,122,114,138,127,130,133],
[127,0,132,120,128,121,137,121,131],
[121,119,0,122,119,128,135,130,130],
[129,131,129,0,120,133,141,132,128],
[137,123,132,131,0,136,130,137,139],
[113,130,123,118,115,0,120,126,134],
[124,114,116,110,121,131,0,123,135],
[121,130,121,119,114,125,128,0,139],
[118,120,121,123,112,117,116,112,0]])



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
result = np.append(np.array([9, 251, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,135,142,119,119,128,131,131],
[117,0,126,137,122,124,109,122,129],
[116,125,0,133,122,108,99,133,124],
[109,114,118,0,110,108,101,110,107],
[132,129,129,141,0,128,111,132,143],
[132,127,143,143,123,0,122,120,124],
[123,142,152,150,140,129,0,135,140],
[120,129,118,141,119,131,116,0,128],
[120,122,127,144,108,127,111,123,0]])



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
result = np.append(np.array([9, 251, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,163,129,153,141,141,137,100],
[88,0,129,103,113,110,83,100,94],
[88,122,0,104,118,93,96,101,94],
[122,148,147,0,144,122,112,151,97],
[98,138,133,107,0,123,104,92,88],
[110,141,158,129,128,0,132,124,75],
[110,168,155,139,147,119,0,129,131],
[114,151,150,100,159,127,122,0,112],
[151,157,157,154,163,176,120,139,0]])



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
result = np.append(np.array([9, 251, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,100,105,109,131,123,123,129],
[141,0,118,118,111,135,118,132,141],
[151,133,0,131,128,129,117,128,156],
[146,133,120,0,125,144,125,130,150],
[142,140,123,126,0,131,111,130,148],
[120,116,122,107,120,0,129,120,136],
[128,133,134,126,140,122,0,134,129],
[128,119,123,121,121,131,117,0,140],
[122,110,95,101,103,115,122,111,0]])



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
result = np.append(np.array([9, 251, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,115,123,132,143,115,117,133],
[122,0,113,132,120,125,121,112,117],
[136,138,0,147,138,145,131,107,148],
[128,119,104,0,130,139,124,122,121],
[119,131,113,121,0,123,122,104,117],
[108,126,106,112,128,0,136,113,123],
[136,130,120,127,129,115,0,116,119],
[134,139,144,129,147,138,135,0,120],
[118,134,103,130,134,128,132,131,0]])



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
result = np.append(np.array([9, 251, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,114,137,124,118,150,118,122],
[148,0,120,136,128,137,148,133,114],
[137,131,0,125,138,138,145,152,124],
[114,115,126,0,130,146,143,119,124],
[127,123,113,121,0,111,137,127,137],
[133,114,113,105,140,0,124,118,135],
[101,103,106,108,114,127,0,114,117],
[133,118,99,132,124,133,137,0,123],
[129,137,127,127,114,116,134,128,0]])



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
result = np.append(np.array([9, 251, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,123,139,117,122,137,127,131],
[121,0,121,122,120,123,121,113,128],
[128,130,0,132,118,120,120,122,131],
[112,129,119,0,120,119,128,118,121],
[134,131,133,131,0,130,123,134,133],
[129,128,131,132,121,0,124,132,119],
[114,130,131,123,128,127,0,118,129],
[124,138,129,133,117,119,133,0,128],
[120,123,120,130,118,132,122,123,0]])



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
result = np.append(np.array([9, 251, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,121,133,113,131,127,142,127],
[111,0,126,114,108,123,122,135,116],
[130,125,0,139,126,123,124,140,129],
[118,137,112,0,121,139,125,126,124],
[138,143,125,130,0,138,148,139,139],
[120,128,128,112,113,0,121,122,118],
[124,129,127,126,103,130,0,138,133],
[109,116,111,125,112,129,113,0,113],
[124,135,122,127,112,133,118,138,0]])



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
result = np.append(np.array([9, 251, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,146,99,161,132,129,119,109],
[109,0,153,91,84,142,114,110,140],
[105,98,0,142,139,110,121,110,130],
[152,160,109,0,160,139,135,95,120],
[90,167,112,91,0,135,108,78,97],
[119,109,141,112,116,0,156,158,109],
[122,137,130,116,143,95,0,142,103],
[132,141,141,156,173,93,109,0,141],
[142,111,121,131,154,142,148,110,0]])



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
result = np.append(np.array([9, 251, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,95,166,181,151,112,142,189],
[88,0,96,150,114,107,133,88,138],
[156,155,0,151,167,181,156,67,158],
[85,101,100,0,133,120,87,77,169],
[70,137,84,118,0,136,105,112,178],
[100,144,70,131,115,0,139,77,169],
[139,118,95,164,146,112,0,132,165],
[109,163,184,174,139,174,119,0,152],
[62,113,93,82,73,82,86,99,0]])



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
result = np.append(np.array([9, 251, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,102,125,139,141,117,120,135],
[122,0,106,102,117,128,118,119,105],
[149,145,0,138,147,150,146,142,124],
[126,149,113,0,128,143,134,118,122],
[112,134,104,123,0,151,133,133,114],
[110,123,101,108,100,0,111,118,106],
[134,133,105,117,118,140,0,126,104],
[131,132,109,133,118,133,125,0,116],
[116,146,127,129,137,145,147,135,0]])



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
result = np.append(np.array([9, 251, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,136,124,127,136,131,127,138],
[131,0,136,119,116,129,133,132,128],
[115,115,0,124,116,130,122,126,128],
[127,132,127,0,121,135,130,119,131],
[124,135,135,130,0,136,141,130,141],
[115,122,121,116,115,0,126,130,125],
[120,118,129,121,110,125,0,120,128],
[124,119,125,132,121,121,131,0,127],
[113,123,123,120,110,126,123,124,0]])



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
result = np.append(np.array([9, 251, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,121,127,175,148,132,160,125],
[115,0,144,145,141,147,137,151,134],
[130,107,0,138,146,142,123,129,146],
[124,106,113,0,145,119,130,129,123],
[76,110,105,106,0,112,105,114,100],
[103,104,109,132,139,0,121,119,121],
[119,114,128,121,146,130,0,131,117],
[91,100,122,122,137,132,120,0,106],
[126,117,105,128,151,130,134,145,0]])



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
result = np.append(np.array([9, 251, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,170,132,106,149,159,151,151,110],
[81,0,37,51,114,125,110,59,56],
[119,214,0,132,170,168,169,131,165],
[145,200,119,0,167,164,153,125,127],
[102,137,81,84,0,130,108,115,107],
[92,126,83,87,121,0,113,89,127],
[100,141,82,98,143,138,0,105,116],
[100,192,120,126,136,162,146,0,137],
[141,195,86,124,144,124,135,114,0]])



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
result = np.append(np.array([9, 251, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,161,7,83,7,7,168],
[244,0,159,161,168,110,7,83,195],
[244,92,0,161,92,110,92,83,168],
[90,90,90,0,90,34,7,34,110],
[244,83,159,161,0,110,83,83,168],
[168,141,141,217,141,0,141,56,217],
[244,244,159,244,168,110,0,159,251],
[244,168,168,217,168,195,92,0,251],
[83,56,83,141,83,34,0,0,0]])



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
result = np.append(np.array([9, 251, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,126,132,125,124,138,120,136],
[119,0,121,125,114,114,127,115,134],
[125,130,0,132,123,120,139,115,127],
[119,126,119,0,119,118,129,112,120],
[126,137,128,132,0,128,138,125,135],
[127,137,131,133,123,0,146,123,136],
[113,124,112,122,113,105,0,114,121],
[131,136,136,139,126,128,137,0,123],
[115,117,124,131,116,115,130,128,0]])



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
result = np.append(np.array([9, 251, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,132,122,122,116,113,134,131],
[130,0,134,133,125,126,125,140,129],
[119,117,0,118,115,113,103,123,127],
[129,118,133,0,118,118,113,123,130],
[129,126,136,133,0,119,128,142,135],
[135,125,138,133,132,0,139,132,139],
[138,126,148,138,123,112,0,142,138],
[117,111,128,128,109,119,109,0,119],
[120,122,124,121,116,112,113,132,0]])



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
result = np.append(np.array([9, 251, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,116,116,128,113,124,135,128],
[131,0,128,124,136,102,134,137,134],
[135,123,0,148,146,131,127,138,126],
[135,127,103,0,133,119,121,149,141],
[123,115,105,118,0,109,120,131,121],
[138,149,120,132,142,0,131,138,130],
[127,117,124,130,131,120,0,138,132],
[116,114,113,102,120,113,113,0,109],
[123,117,125,110,130,121,119,142,0]])



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
result = np.append(np.array([9, 251, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,125,127,129,135,136,139,127],
[115,0,132,133,116,129,127,128,114],
[126,119,0,139,124,129,121,122,103],
[124,118,112,0,108,129,121,128,118],
[122,135,127,143,0,128,148,133,120],
[116,122,122,122,123,0,119,127,106],
[115,124,130,130,103,132,0,125,111],
[112,123,129,123,118,124,126,0,119],
[124,137,148,133,131,145,140,132,0]])



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
result = np.append(np.array([9, 251, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,125,140,171,147,130,155,159],
[153,0,131,119,143,134,139,134,187],
[126,120,0,130,136,130,146,154,137],
[111,132,121,0,144,114,122,142,162],
[80,108,115,107,0,86,108,108,130],
[104,117,121,137,165,0,121,127,171],
[121,112,105,129,143,130,0,133,133],
[96,117,97,109,143,124,118,0,173],
[92,64,114,89,121,80,118,78,0]])



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
result = np.append(np.array([9, 251, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,106,132,124,126,129,122,117],
[145,0,117,135,120,121,144,136,121],
[145,134,0,136,139,144,143,149,124],
[119,116,115,0,128,126,118,113,119],
[127,131,112,123,0,135,126,129,133],
[125,130,107,125,116,0,141,120,125],
[122,107,108,133,125,110,0,122,116],
[129,115,102,138,122,131,129,0,129],
[134,130,127,132,118,126,135,122,0]])



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
result = np.append(np.array([9, 251, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,131,127,131,124,130,134,118],
[122,0,137,140,131,133,118,126,123],
[120,114,0,119,118,118,126,120,114],
[124,111,132,0,117,112,114,108,94],
[120,120,133,134,0,130,125,120,122],
[127,118,133,139,121,0,129,128,126],
[121,133,125,137,126,122,0,124,109],
[117,125,131,143,131,123,127,0,113],
[133,128,137,157,129,125,142,138,0]])



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
result = np.append(np.array([9, 251, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,112,123,131,132,146,131,115],
[123,0,115,125,135,133,133,134,125],
[139,136,0,125,141,142,145,132,131],
[128,126,126,0,138,133,137,132,125],
[120,116,110,113,0,126,127,124,112],
[119,118,109,118,125,0,127,122,115],
[105,118,106,114,124,124,0,122,111],
[120,117,119,119,127,129,129,0,112],
[136,126,120,126,139,136,140,139,0]])



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
result = np.append(np.array([9, 251, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,129,128,118,133,127,150,100],
[124,0,131,118,117,110,110,139,130],
[122,120,0,114,112,132,97,125,128],
[123,133,137,0,122,117,126,171,144],
[133,134,139,129,0,129,119,156,118],
[118,141,119,134,122,0,110,152,128],
[124,141,154,125,132,141,0,153,126],
[101,112,126,80,95,99,98,0,107],
[151,121,123,107,133,123,125,144,0]])



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
result = np.append(np.array([9, 251, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,129,103,130,135,125,131,124],
[128,0,139,111,108,141,127,115,133],
[122,112,0,130,122,136,133,137,126],
[148,140,121,0,128,156,152,133,135],
[121,143,129,123,0,148,123,140,151],
[116,110,115,95,103,0,117,120,108],
[126,124,118,99,128,134,0,127,122],
[120,136,114,118,111,131,124,0,118],
[127,118,125,116,100,143,129,133,0]])



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
result = np.append(np.array([9, 251, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,107,93,126,113,92,107,116],
[140,0,116,120,103,113,121,126,112],
[144,135,0,108,128,142,125,130,133],
[158,131,143,0,123,132,126,137,115],
[125,148,123,128,0,128,143,132,108],
[138,138,109,119,123,0,125,128,107],
[159,130,126,125,108,126,0,121,128],
[144,125,121,114,119,123,130,0,120],
[135,139,118,136,143,144,123,131,0]])



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
result = np.append(np.array([9, 251, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,110,132,127,111,123,123,124],
[118,0,128,127,114,109,130,122,129],
[141,123,0,145,139,110,128,138,129],
[119,124,106,0,124,109,103,127,121],
[124,137,112,127,0,107,110,104,116],
[140,142,141,142,144,0,131,129,121],
[128,121,123,148,141,120,0,123,113],
[128,129,113,124,147,122,128,0,125],
[127,122,122,130,135,130,138,126,0]])



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
result = np.append(np.array([9, 251, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,138,132,128,126,106,117,125],
[137,0,131,142,139,124,121,122,128],
[113,120,0,134,124,134,118,132,120],
[119,109,117,0,124,120,118,129,117],
[123,112,127,127,0,136,109,127,117],
[125,127,117,131,115,0,127,110,124],
[145,130,133,133,142,124,0,141,122],
[134,129,119,122,124,141,110,0,120],
[126,123,131,134,134,127,129,131,0]])



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
result = np.append(np.array([9, 251, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,114,158,115,135,150,104,119],
[119,0,116,113,130,109,133,101,123],
[137,135,0,132,92,143,149,123,121],
[93,138,119,0,111,120,154,125,125],
[136,121,159,140,0,141,155,141,143],
[116,142,108,131,110,0,158,118,135],
[101,118,102,97,96,93,0,100,108],
[147,150,128,126,110,133,151,0,153],
[132,128,130,126,108,116,143,98,0]])



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
result = np.append(np.array([9, 251, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,116,105,130,128,122,132,125],
[131,0,128,133,114,143,129,120,132],
[135,123,0,120,120,139,116,117,131],
[146,118,131,0,126,141,131,136,126],
[121,137,131,125,0,137,127,124,133],
[123,108,112,110,114,0,112,109,109],
[129,122,135,120,124,139,0,118,131],
[119,131,134,115,127,142,133,0,125],
[126,119,120,125,118,142,120,126,0]])



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
result = np.append(np.array([9, 251, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,91,130,137,112,116,133,114,128],
[160,0,148,133,147,123,163,150,154],
[121,103,0,147,123,108,135,121,131],
[114,118,104,0,128,105,121,123,129],
[139,104,128,123,0,113,120,112,142],
[135,128,143,146,138,0,137,119,164],
[118,88,116,130,131,114,0,104,119],
[137,101,130,128,139,132,147,0,127],
[123,97,120,122,109,87,132,124,0]])



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
result = np.append(np.array([9, 251, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,127,127,135,138,119,138,123],
[121,0,127,135,127,131,132,138,123],
[124,124,0,129,125,130,124,135,131],
[124,116,122,0,126,124,124,132,115],
[116,124,126,125,0,138,129,132,123],
[113,120,121,127,113,0,119,122,120],
[132,119,127,127,122,132,0,130,131],
[113,113,116,119,119,129,121,0,111],
[128,128,120,136,128,131,120,140,0]])



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
result = np.append(np.array([9, 251, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,125,131,123,121,115,122,119],
[128,0,124,130,130,117,116,122,114],
[126,127,0,124,138,113,115,120,113],
[120,121,127,0,128,120,121,116,113],
[128,121,113,123,0,120,109,118,110],
[130,134,138,131,131,0,126,125,126],
[136,135,136,130,142,125,0,127,118],
[129,129,131,135,133,126,124,0,118],
[132,137,138,138,141,125,133,133,0]])



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
result = np.append(np.array([9, 251, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,151,125,115,134,139,122,144],
[116,0,130,125,114,117,114,108,108],
[100,121,0,113,104,120,127,102,114],
[126,126,138,0,103,115,108,106,131],
[136,137,147,148,0,128,138,119,147],
[117,134,131,136,123,0,133,126,132],
[112,137,124,143,113,118,0,103,117],
[129,143,149,145,132,125,148,0,145],
[107,143,137,120,104,119,134,106,0]])



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
result = np.append(np.array([9, 251, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,154,120,113,106,149,100,121,101],
[97,0,127,105,76,184,90,70,78],
[131,124,0,95,97,177,92,95,95],
[138,146,156,0,92,147,123,115,93],
[145,175,154,159,0,175,115,161,125],
[102,67,74,104,76,0,82,80,53],
[151,161,159,128,136,169,0,106,128],
[130,181,156,136,90,171,145,0,93],
[150,173,156,158,126,198,123,158,0]])



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
result = np.append(np.array([9, 251, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,126,125,116,150,132,144,137],
[133,0,134,131,131,131,124,139,143],
[125,117,0,107,122,134,128,138,140],
[126,120,144,0,128,137,112,143,136],
[135,120,129,123,0,138,123,133,134],
[101,120,117,114,113,0,112,135,122],
[119,127,123,139,128,139,0,145,138],
[107,112,113,108,118,116,106,0,125],
[114,108,111,115,117,129,113,126,0]])



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
result = np.append(np.array([9, 251, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,125,125,124,143,116,139,123],
[111,0,110,129,116,131,108,119,111],
[126,141,0,145,139,144,118,130,140],
[126,122,106,0,130,130,128,126,126],
[127,135,112,121,0,137,111,120,120],
[108,120,107,121,114,0,117,111,112],
[135,143,133,123,140,134,0,140,138],
[112,132,121,125,131,140,111,0,112],
[128,140,111,125,131,139,113,139,0]])



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
result = np.append(np.array([9, 251, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,123,150,143,144,130,139,128],
[131,0,128,142,126,131,125,128,129],
[128,123,0,137,127,123,129,132,126],
[101,109,114,0,112,122,120,120,122],
[108,125,124,139,0,137,115,130,138],
[107,120,128,129,114,0,120,122,131],
[121,126,122,131,136,131,0,132,123],
[112,123,119,131,121,129,119,0,130],
[123,122,125,129,113,120,128,121,0]])



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
result = np.append(np.array([9, 251, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,138,152,132,118,136,145,143],
[126,0,130,138,147,144,124,143,149],
[113,121,0,141,137,114,126,140,134],
[99,113,110,0,125,101,122,143,128],
[119,104,114,126,0,118,112,138,138],
[133,107,137,150,133,0,141,138,136],
[115,127,125,129,139,110,0,126,128],
[106,108,111,108,113,113,125,0,116],
[108,102,117,123,113,115,123,135,0]])



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
result = np.append(np.array([9, 251, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,118,109,122,122,132,111,122],
[124,0,119,123,123,113,111,127,122],
[133,132,0,146,116,111,112,116,120],
[142,128,105,0,124,119,114,106,113],
[129,128,135,127,0,143,115,110,124],
[129,138,140,132,108,0,113,114,124],
[119,140,139,137,136,138,0,123,148],
[140,124,135,145,141,137,128,0,133],
[129,129,131,138,127,127,103,118,0]])



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
result = np.append(np.array([9, 251, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,134,136,129,132,141,139,123],
[120,0,139,130,121,129,128,114,127],
[117,112,0,130,114,115,114,125,124],
[115,121,121,0,117,126,122,124,122],
[122,130,137,134,0,132,133,137,128],
[119,122,136,125,119,0,123,131,126],
[110,123,137,129,118,128,0,124,128],
[112,137,126,127,114,120,127,0,120],
[128,124,127,129,123,125,123,131,0]])



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
result = np.append(np.array([9, 251, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,124,117,133,126,120,129,134],
[127,0,117,131,138,126,137,121,139],
[127,134,0,134,137,128,121,123,141],
[134,120,117,0,126,128,129,119,136],
[118,113,114,125,0,128,125,119,131],
[125,125,123,123,123,0,123,124,138],
[131,114,130,122,126,128,0,116,129],
[122,130,128,132,132,127,135,0,140],
[117,112,110,115,120,113,122,111,0]])



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
result = np.append(np.array([9, 251, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,126,123,121,116,119,114,134],
[138,0,129,140,123,124,142,131,133],
[125,122,0,125,120,125,117,144,125],
[128,111,126,0,114,95,139,123,126],
[130,128,131,137,0,127,131,125,135],
[135,127,126,156,124,0,124,140,153],
[132,109,134,112,120,127,0,124,109],
[137,120,107,128,126,111,127,0,120],
[117,118,126,125,116,98,142,131,0]])



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
result = np.append(np.array([9, 251, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,147,132,130,142,127,159,122],
[118,0,149,112,136,131,128,132,122],
[104,102,0,112,105,127,107,116,107],
[119,139,139,0,131,136,127,143,130],
[121,115,146,120,0,145,127,143,113],
[109,120,124,115,106,0,121,124,123],
[124,123,144,124,124,130,0,123,132],
[92,119,135,108,108,127,128,0,114],
[129,129,144,121,138,128,119,137,0]])



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
result = np.append(np.array([9, 251, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,118,122,124,129,126,117,123],
[126,0,124,123,131,137,124,122,122],
[133,127,0,120,125,131,137,126,124],
[129,128,131,0,127,127,128,116,123],
[127,120,126,124,0,114,114,106,118],
[122,114,120,124,137,0,135,112,119],
[125,127,114,123,137,116,0,115,119],
[134,129,125,135,145,139,136,0,129],
[128,129,127,128,133,132,132,122,0]])



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
result = np.append(np.array([9, 251, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,141,121,123,133,136,132,141],
[131,0,127,113,128,126,126,122,140],
[110,124,0,129,125,117,123,127,133],
[130,138,122,0,127,132,128,128,134],
[128,123,126,124,0,131,133,140,135],
[118,125,134,119,120,0,121,128,133],
[115,125,128,123,118,130,0,126,126],
[119,129,124,123,111,123,125,0,135],
[110,111,118,117,116,118,125,116,0]])



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
result = np.append(np.array([9, 251, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,112,135,145,137,123,139,124],
[115,0,109,102,104,129,106,123,93],
[139,142,0,140,140,154,126,120,119],
[116,149,111,0,117,138,114,112,111],
[106,147,111,134,0,138,118,112,114],
[114,122,97,113,113,0,108,109,104],
[128,145,125,137,133,143,0,131,137],
[112,128,131,139,139,142,120,0,124],
[127,158,132,140,137,147,114,127,0]])



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
result = np.append(np.array([9, 251, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,115,114,141,123,120,120,141],
[127,0,102,129,138,138,127,119,130],
[136,149,0,116,148,151,130,135,140],
[137,122,135,0,143,134,123,126,132],
[110,113,103,108,0,129,105,99,131],
[128,113,100,117,122,0,114,113,126],
[131,124,121,128,146,137,0,121,141],
[131,132,116,125,152,138,130,0,138],
[110,121,111,119,120,125,110,113,0]])



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
result = np.append(np.array([9, 251, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,149,125,132,117,102,128,109],
[116,0,149,101,139,107,107,131,126],
[102,102,0,113,128,113,94,120,87],
[126,150,138,0,144,121,138,126,109],
[119,112,123,107,0,105,111,142,115],
[134,144,138,130,146,0,125,155,139],
[149,144,157,113,140,126,0,154,140],
[123,120,131,125,109,96,97,0,113],
[142,125,164,142,136,112,111,138,0]])



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
result = np.append(np.array([9, 251, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,129,138,127,136,119,125,132],
[123,0,132,128,135,117,129,129,122],
[122,119,0,122,120,121,114,114,137],
[113,123,129,0,123,122,129,131,132],
[124,116,131,128,0,116,125,125,135],
[115,134,130,129,135,0,134,122,129],
[132,122,137,122,126,117,0,117,152],
[126,122,137,120,126,129,134,0,138],
[119,129,114,119,116,122,99,113,0]])



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
result = np.append(np.array([9, 251, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,142,134,133,124,124,130,141],
[115,0,131,131,128,135,140,132,143],
[109,120,0,120,125,134,114,113,122],
[117,120,131,0,123,111,129,119,118],
[118,123,126,128,0,116,130,120,125],
[127,116,117,140,135,0,128,120,126],
[127,111,137,122,121,123,0,123,119],
[121,119,138,132,131,131,128,0,125],
[110,108,129,133,126,125,132,126,0]])



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
result = np.append(np.array([9, 251, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,119,122,127,117,124,112,123],
[123,0,129,126,118,122,121,119,115],
[132,122,0,122,126,120,116,118,126],
[129,125,129,0,119,116,123,123,108],
[124,133,125,132,0,119,119,123,120],
[134,129,131,135,132,0,128,125,125],
[127,130,135,128,132,123,0,133,123],
[139,132,133,128,128,126,118,0,126],
[128,136,125,143,131,126,128,125,0]])



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
result = np.append(np.array([9, 251, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,136,145,146,140,129,139,120],
[115,0,113,116,129,127,117,139,106],
[115,138,0,117,117,129,110,123,117],
[106,135,134,0,125,119,123,116,117],
[105,122,134,126,0,126,113,124,107],
[111,124,122,132,125,0,125,146,133],
[122,134,141,128,138,126,0,130,135],
[112,112,128,135,127,105,121,0,103],
[131,145,134,134,144,118,116,148,0]])



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
result = np.append(np.array([9, 251, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,129,131,123,122,142,128,126],
[113,0,120,122,115,123,118,122,119],
[122,131,0,124,127,133,123,130,117],
[120,129,127,0,126,132,139,112,118],
[128,136,124,125,0,129,122,119,115],
[129,128,118,119,122,0,124,120,112],
[109,133,128,112,129,127,0,116,119],
[123,129,121,139,132,131,135,0,118],
[125,132,134,133,136,139,132,133,0]])



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
result = np.append(np.array([9, 251, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,119,114,111,123,124,124,114],
[140,0,145,123,134,126,134,133,125],
[132,106,0,114,119,110,112,116,106],
[137,128,137,0,125,123,135,137,114],
[140,117,132,126,0,123,121,128,125],
[128,125,141,128,128,0,137,139,137],
[127,117,139,116,130,114,0,119,120],
[127,118,135,114,123,112,132,0,123],
[137,126,145,137,126,114,131,128,0]])



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
result = np.append(np.array([9, 251, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,120,116,125,115,114,109,120],
[134,0,125,125,128,140,98,118,121],
[131,126,0,127,134,140,124,133,133],
[135,126,124,0,133,128,107,129,123],
[126,123,117,118,0,131,112,110,123],
[136,111,111,123,120,0,115,121,120],
[137,153,127,144,139,136,0,125,137],
[142,133,118,122,141,130,126,0,130],
[131,130,118,128,128,131,114,121,0]])



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
result = np.append(np.array([9, 251, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,146,143,125,134,134,127,123],
[106,0,113,132,106,114,107,112,118],
[105,138,0,131,103,123,118,144,120],
[108,119,120,0,111,111,126,124,115],
[126,145,148,140,0,139,116,113,114],
[117,137,128,140,112,0,113,121,118],
[117,144,133,125,135,138,0,145,134],
[124,139,107,127,138,130,106,0,105],
[128,133,131,136,137,133,117,146,0]])



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
result = np.append(np.array([9, 251, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,147,150,151,139,150,123,145],
[103,0,124,125,113,115,128,111,115],
[104,127,0,114,115,115,131,137,126],
[101,126,137,0,126,116,133,123,117],
[100,138,136,125,0,142,148,136,130],
[112,136,136,135,109,0,156,129,134],
[101,123,120,118,103,95,0,109,107],
[128,140,114,128,115,122,142,0,119],
[106,136,125,134,121,117,144,132,0]])



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
result = np.append(np.array([9, 251, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,121,121,112,122,129,156,144],
[117,0,116,138,108,170,116,120,128],
[130,135,0,157,145,169,119,174,128],
[130,113,94,0,92,121,116,123,117],
[139,143,106,159,0,175,135,170,166],
[129,81,82,130,76,0,105,119,120],
[122,135,132,135,116,146,0,152,148],
[95,131,77,128,81,132,99,0,137],
[107,123,123,134,85,131,103,114,0]])



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
result = np.append(np.array([9, 251, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,137,125,146,147,175,152,143,164],
[114,0,129,162,164,147,126,134,144],
[126,122,0,150,132,157,138,118,141],
[105,89,101,0,115,128,118,103,135],
[104,87,119,136,0,128,133,113,137],
[76,104,94,123,123,0,119,112,143],
[99,125,113,133,118,132,0,113,128],
[108,117,133,148,138,139,138,0,148],
[87,107,110,116,114,108,123,103,0]])



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
result = np.append(np.array([9, 251, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,98,106,109,195,162,154,176],
[148,0,93,130,101,206,122,159,170],
[153,158,0,149,133,149,148,122,202],
[145,121,102,0,95,220,148,146,196],
[142,150,118,156,0,204,198,153,196],
[56,45,102,31,47,0,61,48,54],
[89,129,103,103,53,190,0,153,196],
[97,92,129,105,98,203,98,0,185],
[75,81,49,55,55,197,55,66,0]])



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
result = np.append(np.array([9, 251, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,177,94,235,165,132,239,151,184],
[74,0,134,134,127,27,168,113,119],
[157,117,0,145,71,110,145,90,90],
[16,117,106,0,117,144,132,77,90],
[86,124,180,134,0,113,101,113,86],
[119,224,141,107,138,0,174,119,119],
[12,83,106,119,150,77,0,50,123],
[100,138,161,174,138,132,201,0,190],
[67,132,161,161,165,132,128,61,0]])



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
result = np.append(np.array([9, 251, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,106,130,116,115,117,112,111],
[148,0,128,128,137,123,128,122,116],
[145,123,0,144,133,122,135,134,128],
[121,123,107,0,128,112,114,115,112],
[135,114,118,123,0,117,128,108,115],
[136,128,129,139,134,0,132,133,117],
[134,123,116,137,123,119,0,125,125],
[139,129,117,136,143,118,126,0,109],
[140,135,123,139,136,134,126,142,0]])



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
result = np.append(np.array([9, 251, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,130,162,199,156,160,195,106],
[140,0,161,148,165,165,171,182,112],
[121,90,0,137,207,139,133,166,91],
[89,103,114,0,165,128,137,185,139],
[52,86,44,86,0,108,110,112,75],
[95,86,112,123,143,0,126,140,100],
[91,80,118,114,141,125,0,109,107],
[56,69,85,66,139,111,142,0,83],
[145,139,160,112,176,151,144,168,0]])



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
result = np.append(np.array([9, 251, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,128,143,136,143,124,134,135],
[116,0,130,139,116,124,137,131,145],
[123,121,0,124,130,137,134,133,128],
[108,112,127,0,126,122,115,135,113],
[115,135,121,125,0,126,127,123,129],
[108,127,114,129,125,0,122,132,123],
[127,114,117,136,124,129,0,127,117],
[117,120,118,116,128,119,124,0,115],
[116,106,123,138,122,128,134,136,0]])



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
result = np.append(np.array([9, 251, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,122,138,114,145,126,145,129],
[113,0,111,128,116,130,116,125,111],
[129,140,0,134,111,135,115,136,131],
[113,123,117,0,123,128,122,119,109],
[137,135,140,128,0,138,122,140,137],
[106,121,116,123,113,0,106,118,113],
[125,135,136,129,129,145,0,138,130],
[106,126,115,132,111,133,113,0,135],
[122,140,120,142,114,138,121,116,0]])



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
result = np.append(np.array([9, 251, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,109,117,113,112,117,110,118],
[144,0,117,128,116,125,120,113,124],
[142,134,0,135,122,122,134,126,137],
[134,123,116,0,115,120,131,120,127],
[138,135,129,136,0,134,129,125,133],
[139,126,129,131,117,0,120,120,136],
[134,131,117,120,122,131,0,119,123],
[141,138,125,131,126,131,132,0,139],
[133,127,114,124,118,115,128,112,0]])



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
result = np.append(np.array([9, 251, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,126,117,110,138,126,144,132],
[123,0,112,121,128,125,131,129,120],
[125,139,0,134,139,135,127,145,136],
[134,130,117,0,131,138,105,132,118],
[141,123,112,120,0,130,121,143,132],
[113,126,116,113,121,0,97,123,114],
[125,120,124,146,130,154,0,158,127],
[107,122,106,119,108,128,93,0,97],
[119,131,115,133,119,137,124,154,0]])



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
result = np.append(np.array([9, 251, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,114,142,130,124,124,133,139],
[125,0,117,134,135,125,130,120,137],
[137,134,0,141,129,137,126,122,137],
[109,117,110,0,114,115,111,111,122],
[121,116,122,137,0,122,120,120,137],
[127,126,114,136,129,0,116,124,137],
[127,121,125,140,131,135,0,117,142],
[118,131,129,140,131,127,134,0,124],
[112,114,114,129,114,114,109,127,0]])



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
result = np.append(np.array([9, 251, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,137,132,115,126,127,128,110],
[117,0,135,125,109,122,115,120,114],
[114,116,0,117,96,114,104,109,110],
[119,126,134,0,121,126,113,130,105],
[136,142,155,130,0,134,128,122,133],
[125,129,137,125,117,0,115,110,119],
[124,136,147,138,123,136,0,137,118],
[123,131,142,121,129,141,114,0,122],
[141,137,141,146,118,132,133,129,0]])



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
result = np.append(np.array([9, 251, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,112,116,130,115,120,134,119],
[121,0,116,105,130,117,119,123,109],
[139,135,0,120,128,121,132,136,116],
[135,146,131,0,145,129,133,148,125],
[121,121,123,106,0,107,129,133,115],
[136,134,130,122,144,0,140,157,135],
[131,132,119,118,122,111,0,127,124],
[117,128,115,103,118,94,124,0,107],
[132,142,135,126,136,116,127,144,0]])



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
result = np.append(np.array([9, 251, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,153,123,126,126,136,148,124],
[115,0,158,144,133,123,156,154,124],
[98,93,0,119,114,124,133,127,105],
[128,107,132,0,132,120,133,132,150],
[125,118,137,119,0,116,134,130,132],
[125,128,127,131,135,0,145,140,145],
[115,95,118,118,117,106,0,123,112],
[103,97,124,119,121,111,128,0,115],
[127,127,146,101,119,106,139,136,0]])



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
result = np.append(np.array([9, 251, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,137,122,121,121,128,118,125],
[125,0,116,124,113,114,122,128,120],
[114,135,0,127,116,119,126,125,122],
[129,127,124,0,131,123,129,127,126],
[130,138,135,120,0,129,130,133,145],
[130,137,132,128,122,0,133,128,131],
[123,129,125,122,121,118,0,111,123],
[133,123,126,124,118,123,140,0,123],
[126,131,129,125,106,120,128,128,0]])



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
result = np.append(np.array([9, 251, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,159,90,116,168,110,91,116,76],
[92,0,121,115,148,87,93,60,49],
[161,130,0,134,106,131,129,124,90],
[135,136,117,0,137,131,129,104,69],
[83,103,145,114,0,110,97,104,70],
[141,164,120,120,141,0,168,131,158],
[160,158,122,122,154,83,0,150,103],
[135,191,127,147,147,120,101,0,151],
[175,202,161,182,181,93,148,100,0]])



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
result = np.append(np.array([9, 251, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,128,141,131,132,138,137,141],
[129,0,134,136,128,128,125,138,109],
[123,117,0,130,120,127,114,135,124],
[110,115,121,0,106,109,100,120,107],
[120,123,131,145,0,125,122,138,133],
[119,123,124,142,126,0,117,129,133],
[113,126,137,151,129,134,0,143,128],
[114,113,116,131,113,122,108,0,112],
[110,142,127,144,118,118,123,139,0]])



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
result = np.append(np.array([9, 251, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,120,141,117,122,145,115,114],
[120,0,131,138,112,119,147,101,134],
[131,120,0,130,118,118,116,95,106],
[110,113,121,0,113,104,115,106,120],
[134,139,133,138,0,120,147,105,139],
[129,132,133,147,131,0,143,129,106],
[106,104,135,136,104,108,0,96,103],
[136,150,156,145,146,122,155,0,132],
[137,117,145,131,112,145,148,119,0]])



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
result = np.append(np.array([9, 251, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,110,116,112,123,125,118,115],
[116,0,114,114,104,116,115,109,109],
[141,137,0,115,117,119,120,115,111],
[135,137,136,0,133,133,139,134,120],
[139,147,134,118,0,127,131,122,132],
[128,135,132,118,124,0,120,109,121],
[126,136,131,112,120,131,0,125,128],
[133,142,136,117,129,142,126,0,122],
[136,142,140,131,119,130,123,129,0]])



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
result = np.append(np.array([9, 251, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,159,135,177,114,135,167,206,160],
[92,0,85,149,85,109,138,149,110],
[116,166,0,138,117,106,191,149,191],
[74,102,113,0,82,126,134,113,95],
[137,166,134,169,0,102,201,184,127],
[116,142,145,125,149,0,167,119,104],
[84,113,60,117,50,84,0,92,96],
[45,102,102,138,67,132,159,0,120],
[91,141,60,156,124,147,155,131,0]])



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
result = np.append(np.array([9, 251, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,141,139,145,132,119,151,111],
[116,0,124,132,117,127,125,145,118],
[110,127,0,139,132,134,130,137,105],
[112,119,112,0,133,131,130,130,131],
[106,134,119,118,0,125,100,145,115],
[119,124,117,120,126,0,120,155,103],
[132,126,121,121,151,131,0,149,130],
[100,106,114,121,106,96,102,0,102],
[140,133,146,120,136,148,121,149,0]])



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
result = np.append(np.array([9, 251, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,116,103,112,105,117,113,104],
[148,0,129,126,136,129,123,134,129],
[135,122,0,112,131,106,108,108,119],
[148,125,139,0,141,136,135,114,137],
[139,115,120,110,0,122,123,113,118],
[146,122,145,115,129,0,119,122,115],
[134,128,143,116,128,132,0,126,133],
[138,117,143,137,138,129,125,0,116],
[147,122,132,114,133,136,118,135,0]])



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
result = np.append(np.array([9, 251, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,119,129,127,118,119,133,125],
[136,0,125,124,135,135,128,129,119],
[132,126,0,139,136,130,125,138,130],
[122,127,112,0,123,126,125,132,117],
[124,116,115,128,0,131,113,128,116],
[133,116,121,125,120,0,129,138,131],
[132,123,126,126,138,122,0,131,121],
[118,122,113,119,123,113,120,0,120],
[126,132,121,134,135,120,130,131,0]])



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
result = np.append(np.array([9, 251, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,126,125,126,141,124,117,104],
[120,0,122,120,125,129,133,125,103],
[125,129,0,123,128,139,124,122,127],
[126,131,128,0,116,143,128,124,119],
[125,126,123,135,0,144,129,131,138],
[110,122,112,108,107,0,107,108,91],
[127,118,127,123,122,144,0,132,110],
[134,126,129,127,120,143,119,0,113],
[147,148,124,132,113,160,141,138,0]])



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
result = np.append(np.array([9, 251, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,117,118,125,116,117,116,133],
[126,0,129,130,131,121,115,122,138],
[134,122,0,133,123,115,106,128,134],
[133,121,118,0,124,126,127,124,136],
[126,120,128,127,0,121,120,130,131],
[135,130,136,125,130,0,119,124,135],
[134,136,145,124,131,132,0,131,139],
[135,129,123,127,121,127,120,0,133],
[118,113,117,115,120,116,112,118,0]])



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
result = np.append(np.array([9, 251, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,110,125,115,115,124,122,140],
[119,0,114,132,131,117,125,115,124],
[141,137,0,145,131,135,125,122,142],
[126,119,106,0,131,120,129,128,121],
[136,120,120,120,0,122,118,125,118],
[136,134,116,131,129,0,144,134,142],
[127,126,126,122,133,107,0,113,143],
[129,136,129,123,126,117,138,0,126],
[111,127,109,130,133,109,108,125,0]])



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
result = np.append(np.array([9, 251, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,129,115,132,142,131,128,116],
[116,0,125,122,129,135,123,135,123],
[122,126,0,130,118,142,135,140,137],
[136,129,121,0,126,145,126,133,135],
[119,122,133,125,0,136,143,130,126],
[109,116,109,106,115,0,112,119,107],
[120,128,116,125,108,139,0,130,122],
[123,116,111,118,121,132,121,0,120],
[135,128,114,116,125,144,129,131,0]])



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
result = np.append(np.array([9, 251, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,142,125,124,122,138,134,127],
[125,0,116,118,112,107,125,129,110],
[109,135,0,110,109,113,111,129,113],
[126,133,141,0,127,112,125,127,128],
[127,139,142,124,0,128,131,149,134],
[129,144,138,139,123,0,139,141,130],
[113,126,140,126,120,112,0,123,124],
[117,122,122,124,102,110,128,0,111],
[124,141,138,123,117,121,127,140,0]])



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
result = np.append(np.array([9, 251, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,104,95,103,113,112,96,119],
[172,0,136,132,135,124,147,148,154],
[147,115,0,118,117,109,136,115,136],
[156,119,133,0,139,115,144,127,139],
[148,116,134,112,0,131,134,125,149],
[138,127,142,136,120,0,148,135,136],
[139,104,115,107,117,103,0,118,124],
[155,103,136,124,126,116,133,0,138],
[132,97,115,112,102,115,127,113,0]])



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
result = np.append(np.array([9, 251, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,129,129,114,132,154,125,137],
[100,0,110,112,113,103,116,119,121],
[122,141,0,140,121,134,128,136,142],
[122,139,111,0,126,118,115,141,134],
[137,138,130,125,0,132,142,111,148],
[119,148,117,133,119,0,125,126,113],
[97,135,123,136,109,126,0,127,133],
[126,132,115,110,140,125,124,0,138],
[114,130,109,117,103,138,118,113,0]])



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
result = np.append(np.array([9, 251, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,118,118,104,125,128,120,121],
[137,0,123,112,114,131,148,119,130],
[133,128,0,119,98,140,116,117,121],
[133,139,132,0,120,149,157,145,135],
[147,137,153,131,0,150,154,120,135],
[126,120,111,102,101,0,120,110,115],
[123,103,135,94,97,131,0,112,137],
[131,132,134,106,131,141,139,0,125],
[130,121,130,116,116,136,114,126,0]])



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
result = np.append(np.array([9, 251, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,124,128,106,130,124,132,130],
[117,0,123,109,114,113,146,129,132],
[127,128,0,128,116,134,127,140,119],
[123,142,123,0,128,99,149,104,138],
[145,137,135,123,0,126,139,148,170],
[121,138,117,152,125,0,160,125,130],
[127,105,124,102,112,91,0,124,128],
[119,122,111,147,103,126,127,0,132],
[121,119,132,113,81,121,123,119,0]])



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
result = np.append(np.array([9, 251, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,115,128,118,125,162,121,144],
[126,0,131,123,140,128,171,115,152],
[136,120,0,110,132,131,144,98,135],
[123,128,141,0,120,139,151,140,148],
[133,111,119,131,0,126,137,127,124],
[126,123,120,112,125,0,138,120,126],
[89,80,107,100,114,113,0,95,122],
[130,136,153,111,124,131,156,0,139],
[107,99,116,103,127,125,129,112,0]])



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
result = np.append(np.array([9, 251, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,124,148,132,132,137,125,123],
[132,0,123,135,136,134,128,132,136],
[127,128,0,137,113,127,132,119,116],
[103,116,114,0,112,116,121,121,132],
[119,115,138,139,0,128,129,134,136],
[119,117,124,135,123,0,127,117,117],
[114,123,119,130,122,124,0,114,121],
[126,119,132,130,117,134,137,0,138],
[128,115,135,119,115,134,130,113,0]])



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
result = np.append(np.array([9, 251, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,116,124,126,123,138,104,113],
[129,0,119,116,130,126,144,133,128],
[135,132,0,119,137,119,131,127,127],
[127,135,132,0,121,126,145,133,123],
[125,121,114,130,0,125,133,139,119],
[128,125,132,125,126,0,152,139,125],
[113,107,120,106,118,99,0,111,95],
[147,118,124,118,112,112,140,0,128],
[138,123,124,128,132,126,156,123,0]])



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
result = np.append(np.array([9, 251, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,165,105,144,151,133,145,138],
[123,0,119,144,126,126,109,151,133],
[86,132,0,103,176,155,102,136,103],
[146,107,148,0,133,137,173,124,152],
[107,125,75,118,0,104,129,138,116],
[100,125,96,114,147,0,115,115,75],
[118,142,149,78,122,136,0,121,126],
[106,100,115,127,113,136,130,0,136],
[113,118,148,99,135,176,125,115,0]])



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
result = np.append(np.array([9, 251, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,127,141,147,143,115,149,144],
[124,0,133,119,126,132,115,125,134],
[124,118,0,128,122,136,102,127,142],
[110,132,123,0,125,125,106,109,129],
[104,125,129,126,0,121,118,121,127],
[108,119,115,126,130,0,120,113,141],
[136,136,149,145,133,131,0,125,163],
[102,126,124,142,130,138,126,0,136],
[107,117,109,122,124,110,88,115,0]])



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
result = np.append(np.array([9, 251, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,122,110,100,119,128,120,105],
[132,0,124,130,116,127,122,137,126],
[129,127,0,123,120,121,132,129,106],
[141,121,128,0,116,132,127,134,114],
[151,135,131,135,0,127,127,139,119],
[132,124,130,119,124,0,142,127,117],
[123,129,119,124,124,109,0,114,119],
[131,114,122,117,112,124,137,0,121],
[146,125,145,137,132,134,132,130,0]])



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
result = np.append(np.array([9, 251, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,139,119,128,131,121,127,114],
[125,0,130,128,133,134,122,131,120],
[112,121,0,116,122,115,117,121,122],
[132,123,135,0,137,129,125,140,117],
[123,118,129,114,0,113,116,120,113],
[120,117,136,122,138,0,125,119,127],
[130,129,134,126,135,126,0,128,120],
[124,120,130,111,131,132,123,0,120],
[137,131,129,134,138,124,131,131,0]])



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
result = np.append(np.array([9, 251, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,95,23,50,37,47,37,141,23],
[156,0,72,37,47,47,69,83,26],
[228,179,0,102,37,124,114,163,131],
[201,214,149,0,37,159,103,149,55],
[214,204,214,214,0,146,149,139,110],
[204,204,127,92,105,0,124,172,100],
[214,182,137,148,102,127,0,185,88],
[110,168,88,102,112,79,66,0,120],
[228,225,120,196,141,151,163,131,0]])



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
result = np.append(np.array([9, 251, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,132,125,131,125,121,130,129],
[113,0,122,116,123,106,123,131,116],
[119,129,0,128,121,115,119,121,116],
[126,135,123,0,129,122,131,140,129],
[120,128,130,122,0,121,128,129,120],
[126,145,136,129,130,0,130,124,128],
[130,128,132,120,123,121,0,127,130],
[121,120,130,111,122,127,124,0,120],
[122,135,135,122,131,123,121,131,0]])



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
result = np.append(np.array([9, 251, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,122,126,107,103,122,113,118],
[119,0,123,125,117,120,123,125,135],
[129,128,0,134,130,123,130,126,137],
[125,126,117,0,117,115,123,113,116],
[144,134,121,134,0,121,137,116,139],
[148,131,128,136,130,0,138,122,142],
[129,128,121,128,114,113,0,118,121],
[138,126,125,138,135,129,133,0,139],
[133,116,114,135,112,109,130,112,0]])



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
result = np.append(np.array([9, 251, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,168,139,176,175,64,64,119],
[118,0,63,81,89,175,0,89,89],
[83,188,0,136,146,140,55,89,89],
[112,170,115,0,118,112,170,113,176],
[75,162,105,133,0,132,93,86,86],
[76,76,111,139,119,0,64,64,64],
[187,251,196,81,158,187,0,147,204],
[187,162,162,138,165,187,104,0,204],
[132,162,162,75,165,187,47,47,0]])



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
result = np.append(np.array([9, 251, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,121,113,122,123,120,131,124],
[130,0,130,119,122,127,119,127,128],
[130,121,0,124,115,127,119,111,127],
[138,132,127,0,134,142,124,126,131],
[129,129,136,117,0,138,142,132,132],
[128,124,124,109,113,0,119,119,114],
[131,132,132,127,109,132,0,123,120],
[120,124,140,125,119,132,128,0,117],
[127,123,124,120,119,137,131,134,0]])



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
result = np.append(np.array([9, 251, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,112,131,124,139,113,132,132],
[107,0,108,130,124,119,116,124,110],
[139,143,0,129,124,118,131,126,145],
[120,121,122,0,111,129,126,123,118],
[127,127,127,140,0,118,117,116,129],
[112,132,133,122,133,0,123,118,117],
[138,135,120,125,134,128,0,136,127],
[119,127,125,128,135,133,115,0,131],
[119,141,106,133,122,134,124,120,0]])



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
result = np.append(np.array([9, 251, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,121,134,81,121,114,121,113],
[109,0,102,104,102,104,108,112,77],
[130,149,0,142,136,146,138,143,120],
[117,147,109,0,103,142,144,126,94],
[170,149,115,148,0,162,149,171,135],
[130,147,105,109,89,0,130,127,116],
[137,143,113,107,102,121,0,135,124],
[130,139,108,125,80,124,116,0,91],
[138,174,131,157,116,135,127,160,0]])



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
result = np.append(np.array([9, 251, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,123,136,129,117,125,114,125],
[121,0,126,132,119,128,122,127,122],
[128,125,0,142,134,122,132,130,135],
[115,119,109,0,118,120,113,115,106],
[122,132,117,133,0,120,118,119,130],
[134,123,129,131,131,0,128,123,132],
[126,129,119,138,133,123,0,127,129],
[137,124,121,136,132,128,124,0,136],
[126,129,116,145,121,119,122,115,0]])



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
result = np.append(np.array([9, 251, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,116,129,134,130,151,132,144],
[137,0,127,130,130,107,131,150,137],
[135,124,0,161,136,121,162,141,118],
[122,121,90,0,119,121,116,111,122],
[117,121,115,132,0,123,144,134,132],
[121,144,130,130,128,0,138,135,145],
[100,120,89,135,107,113,0,113,110],
[119,101,110,140,117,116,138,0,130],
[107,114,133,129,119,106,141,121,0]])



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
result = np.append(np.array([9, 251, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,122,133,130,118,149,134,123],
[127,0,118,124,105,109,124,122,120],
[129,133,0,134,146,121,161,125,123],
[118,127,117,0,131,107,144,111,138],
[121,146,105,120,0,101,143,124,113],
[133,142,130,144,150,0,156,128,122],
[102,127,90,107,108,95,0,88,94],
[117,129,126,140,127,123,163,0,125],
[128,131,128,113,138,129,157,126,0]])



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
result = np.append(np.array([9, 251, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,125,128,144,124,154,147,142],
[107,0,129,108,120,128,144,100,113],
[126,122,0,118,146,113,164,124,137],
[123,143,133,0,143,138,162,154,156],
[107,131,105,108,0,125,134,114,105],
[127,123,138,113,126,0,141,122,131],
[97,107,87,89,117,110,0,66,120],
[104,151,127,97,137,129,185,0,132],
[109,138,114,95,146,120,131,119,0]])



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
result = np.append(np.array([9, 251, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_9_251.csv", index=False, header=False)