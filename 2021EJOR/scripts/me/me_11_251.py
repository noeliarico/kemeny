
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,132,121,131,130,106,118,122,111,122,122],
[119,0,115,136,125,124,126,134,112,125,125],
[130,136,0,139,121,121,123,112,110,132,110],
[120,115,112,0,126,121,106,135,105,117,119],
[121,126,130,125,0,107,116,130,105,124,119],
[145,127,130,130,144,0,122,140,130,139,128],
[133,125,128,145,135,129,0,136,122,131,138],
[129,117,139,116,121,111,115,0,105,132,126],
[140,139,141,146,146,121,129,146,0,151,127],
[129,126,119,134,127,112,120,119,100,0,132],
[129,126,141,132,132,123,113,125,124,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,135,131,132,119,118,128,130,126,127],
[119,0,131,116,117,115,124,122,130,114,115],
[116,120,0,110,112,110,110,109,125,112,115],
[120,135,141,0,130,128,128,129,141,136,134],
[119,134,139,121,0,113,125,130,126,132,120],
[132,136,141,123,138,0,133,132,138,136,130],
[133,127,141,123,126,118,0,125,130,127,122],
[123,129,142,122,121,119,126,0,136,120,124],
[121,121,126,110,125,113,121,115,0,119,117],
[125,137,139,115,119,115,124,131,132,0,124],
[124,136,136,117,131,121,129,127,134,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,126,127,132,130,124,121,132,140,128],
[115,0,119,115,114,125,121,116,119,125,102],
[125,132,0,124,118,122,137,112,120,137,116],
[124,136,127,0,136,131,130,120,134,134,120],
[119,137,133,115,0,129,134,116,115,129,104],
[121,126,129,120,122,0,117,122,127,134,125],
[127,130,114,121,117,134,0,120,125,125,123],
[130,135,139,131,135,129,131,0,130,138,123],
[119,132,131,117,136,124,126,121,0,133,115],
[111,126,114,117,122,117,126,113,118,0,113],
[123,149,135,131,147,126,128,128,136,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,122,114,113,113,113,118,118,128,102],
[146,0,140,129,136,137,133,139,135,133,120],
[129,111,0,120,120,122,127,138,126,125,126],
[137,122,131,0,125,126,121,133,117,121,117],
[138,115,131,126,0,127,118,114,119,126,116],
[138,114,129,125,124,0,126,131,130,121,114],
[138,118,124,130,133,125,0,131,133,134,113],
[133,112,113,118,137,120,120,0,123,132,110],
[133,116,125,134,132,121,118,128,0,126,121],
[123,118,126,130,125,130,117,119,125,0,119],
[149,131,125,134,135,137,138,141,130,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,126,121,99,113,138,135,97,118,141],
[148,0,100,126,94,114,138,127,100,144,126],
[125,151,0,143,145,121,146,143,124,139,150],
[130,125,108,0,116,136,144,137,125,144,144],
[152,157,106,135,0,142,153,167,131,144,156],
[138,137,130,115,109,0,145,150,140,133,132],
[113,113,105,107,98,106,0,123,108,110,119],
[116,124,108,114,84,101,128,0,116,131,134],
[154,151,127,126,120,111,143,135,0,146,152],
[133,107,112,107,107,118,141,120,105,0,141],
[110,125,101,107,95,119,132,117,99,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,132,131,123,139,127,118,116,121,114],
[112,0,132,131,115,134,120,105,123,119,109],
[119,119,0,139,112,133,116,109,120,111,111],
[120,120,112,0,111,129,125,107,119,118,109],
[128,136,139,140,0,143,123,119,128,133,113],
[112,117,118,122,108,0,109,99,111,111,111],
[124,131,135,126,128,142,0,125,120,129,126],
[133,146,142,144,132,152,126,0,127,141,119],
[135,128,131,132,123,140,131,124,0,127,118],
[130,132,140,133,118,140,122,110,124,0,117],
[137,142,140,142,138,140,125,132,133,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,105,129,136,144,134,122,112,90,143],
[137,0,124,141,127,145,138,110,117,121,128],
[146,127,0,157,154,146,138,119,146,140,143],
[122,110,94,0,107,113,126,109,103,115,93],
[115,124,97,144,0,155,138,113,120,115,110],
[107,106,105,138,96,0,123,89,98,88,105],
[117,113,113,125,113,128,0,92,115,110,111],
[129,141,132,142,138,162,159,0,123,125,111],
[139,134,105,148,131,153,136,128,0,102,128],
[161,130,111,136,136,163,141,126,149,0,128],
[108,123,108,158,141,146,140,140,123,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,150,115,139,130,149,127,118,140,113],
[123,0,121,117,120,105,119,136,110,110,106],
[101,130,0,119,115,107,124,123,111,115,98],
[136,134,132,0,123,136,136,145,126,141,132],
[112,131,136,128,0,140,133,141,126,139,139],
[121,146,144,115,111,0,141,141,128,143,123],
[102,132,127,115,118,110,0,110,123,122,112],
[124,115,128,106,110,110,141,0,101,121,113],
[133,141,140,125,125,123,128,150,0,130,114],
[111,141,136,110,112,108,129,130,121,0,124],
[138,145,153,119,112,128,139,138,137,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,136,136,121,128,141,131,130,136,126],
[125,0,130,143,125,117,138,127,128,124,135],
[115,121,0,138,124,117,130,122,129,125,123],
[115,108,113,0,110,115,121,119,118,104,115],
[130,126,127,141,0,126,136,130,134,119,118],
[123,134,134,136,125,0,131,127,141,126,122],
[110,113,121,130,115,120,0,114,129,112,116],
[120,124,129,132,121,124,137,0,129,123,116],
[121,123,122,133,117,110,122,122,0,124,121],
[115,127,126,147,132,125,139,128,127,0,128],
[125,116,128,136,133,129,135,135,130,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,116,132,135,124,124,124,129,120,127],
[134,0,112,118,124,136,119,122,114,125,119],
[135,139,0,137,138,131,139,124,139,127,130],
[119,133,114,0,139,134,125,116,123,120,130],
[116,127,113,112,0,127,106,112,118,116,115],
[127,115,120,117,124,0,125,114,123,124,119],
[127,132,112,126,145,126,0,127,122,116,128],
[127,129,127,135,139,137,124,0,131,136,135],
[122,137,112,128,133,128,129,120,0,128,129],
[131,126,124,131,135,127,135,115,123,0,129],
[124,132,121,121,136,132,123,116,122,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,141,152,141,151,131,118,124,127,129],
[102,0,122,127,138,138,130,120,135,107,129],
[110,129,0,153,126,135,148,144,125,133,143],
[99,124,98,0,115,139,116,95,121,94,110],
[110,113,125,136,0,123,126,103,110,110,130],
[100,113,116,112,128,0,115,116,106,118,113],
[120,121,103,135,125,136,0,123,111,119,140],
[133,131,107,156,148,135,128,0,132,112,127],
[127,116,126,130,141,145,140,119,0,122,139],
[124,144,118,157,141,133,132,139,129,0,124],
[122,122,108,141,121,138,111,124,112,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,112,112,110,104,109,117,112,112,112],
[140,0,128,130,121,129,127,128,122,135,133],
[139,123,0,132,122,125,123,121,124,129,125],
[139,121,119,0,110,121,124,112,116,122,114],
[141,130,129,141,0,127,125,138,126,128,144],
[147,122,126,130,124,0,113,129,124,132,118],
[142,124,128,127,126,138,0,120,123,126,129],
[134,123,130,139,113,122,131,0,114,132,118],
[139,129,127,135,125,127,128,137,0,125,135],
[139,116,122,129,123,119,125,119,126,0,118],
[139,118,126,137,107,133,122,133,116,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,116,131,126,109,121,122,118,123,119],
[131,0,133,132,131,115,126,129,132,124,138],
[135,118,0,131,125,116,113,128,130,111,120],
[120,119,120,0,104,113,98,128,112,112,115],
[125,120,126,147,0,100,111,116,125,118,141],
[142,136,135,138,151,0,125,157,138,128,148],
[130,125,138,153,140,126,0,129,124,121,133],
[129,122,123,123,135,94,122,0,113,123,134],
[133,119,121,139,126,113,127,138,0,114,138],
[128,127,140,139,133,123,130,128,137,0,139],
[132,113,131,136,110,103,118,117,113,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,121,128,128,116,134,125,119,123,127],
[121,0,112,128,126,105,133,133,125,120,121],
[130,139,0,130,133,119,137,143,130,120,125],
[123,123,121,0,127,116,126,131,122,116,120],
[123,125,118,124,0,114,128,123,122,122,116],
[135,146,132,135,137,0,136,133,133,122,129],
[117,118,114,125,123,115,0,119,121,117,115],
[126,118,108,120,128,118,132,0,121,120,127],
[132,126,121,129,129,118,130,130,0,124,118],
[128,131,131,135,129,129,134,131,127,0,122],
[124,130,126,131,135,122,136,124,133,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,118,121,113,119,119,111,115,135,126],
[142,0,125,113,127,130,136,116,124,145,141],
[133,126,0,130,127,146,139,124,119,152,136],
[130,138,121,0,130,125,134,130,113,148,141],
[138,124,124,121,0,114,119,111,119,130,146],
[132,121,105,126,137,0,127,122,132,140,131],
[132,115,112,117,132,124,0,115,121,134,132],
[140,135,127,121,140,129,136,0,123,150,151],
[136,127,132,138,132,119,130,128,0,135,143],
[116,106,99,103,121,111,117,101,116,0,114],
[125,110,115,110,105,120,119,100,108,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,101,106,120,109,107,88,104,116,106],
[120,0,124,119,138,131,115,108,122,118,123],
[150,127,0,129,125,133,116,120,125,123,112],
[145,132,122,0,130,125,129,125,115,123,139],
[131,113,126,121,0,120,110,117,118,115,127],
[142,120,118,126,131,0,104,114,116,111,129],
[144,136,135,122,141,147,0,123,135,150,120],
[163,143,131,126,134,137,128,0,119,135,138],
[147,129,126,136,133,135,116,132,0,116,129],
[135,133,128,128,136,140,101,116,135,0,138],
[145,128,139,112,124,122,131,113,122,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,116,113,163,106,122,132,126,103,117,144],
[135,0,145,132,115,113,122,159,119,116,144],
[138,106,0,114,107,114,131,116,129,135,148],
[88,119,137,0,134,125,134,145,119,117,145],
[145,136,144,117,0,123,121,127,135,107,160],
[129,138,137,126,128,0,146,137,115,119,144],
[119,129,120,117,130,105,0,135,112,99,146],
[125,92,135,106,124,114,116,0,115,103,136],
[148,132,122,132,116,136,139,136,0,114,161],
[134,135,116,134,144,132,152,148,137,0,148],
[107,107,103,106,91,107,105,115,90,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,124,132,122,129,135,135,127,128,139],
[130,0,131,133,133,124,121,139,134,130,131],
[127,120,0,147,132,127,128,126,133,126,130],
[119,118,104,0,124,132,132,126,133,113,128],
[129,118,119,127,0,131,131,133,127,125,133],
[122,127,124,119,120,0,127,130,111,120,133],
[116,130,123,119,120,124,0,121,132,125,132],
[116,112,125,125,118,121,130,0,127,127,137],
[124,117,118,118,124,140,119,124,0,119,128],
[123,121,125,138,126,131,126,124,132,0,134],
[112,120,121,123,118,118,119,114,123,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,134,118,123,123,123,130,128,110,126],
[142,0,139,125,132,130,139,132,146,127,133],
[117,112,0,124,120,121,127,115,128,118,133],
[133,126,127,0,123,124,117,123,133,123,118],
[128,119,131,128,0,129,126,134,136,127,133],
[128,121,130,127,122,0,128,133,136,119,139],
[128,112,124,134,125,123,0,123,136,114,123],
[121,119,136,128,117,118,128,0,138,117,124],
[123,105,123,118,115,115,115,113,0,113,114],
[141,124,133,128,124,132,137,134,138,0,147],
[125,118,118,133,118,112,128,127,137,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,132,129,134,129,140,127,126,131,120],
[134,0,138,127,141,130,119,128,122,134,141],
[119,113,0,121,128,121,127,118,124,123,110],
[122,124,130,0,137,123,123,112,123,137,134],
[117,110,123,114,0,112,114,116,114,119,115],
[122,121,130,128,139,0,125,117,120,133,124],
[111,132,124,128,137,126,0,140,117,114,122],
[124,123,133,139,135,134,111,0,132,133,120],
[125,129,127,128,137,131,134,119,0,125,131],
[120,117,128,114,132,118,137,118,126,0,120],
[131,110,141,117,136,127,129,131,120,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,142,129,136,142,131,144,133,150,127],
[127,0,117,96,125,148,108,134,137,131,108],
[109,134,0,112,97,128,105,140,120,160,101],
[122,155,139,0,147,163,145,167,145,170,142],
[115,126,154,104,0,140,119,153,128,141,118],
[109,103,123,88,111,0,115,150,128,138,134],
[120,143,146,106,132,136,0,135,148,133,131],
[107,117,111,84,98,101,116,0,123,111,104],
[118,114,131,106,123,123,103,128,0,115,113],
[101,120,91,81,110,113,118,140,136,0,98],
[124,143,150,109,133,117,120,147,138,153,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,132,124,122,121,127,127,125,130,116],
[125,0,138,114,122,132,129,136,121,128,111],
[119,113,0,120,118,120,126,130,125,129,127],
[127,137,131,0,130,126,125,139,137,140,119],
[129,129,133,121,0,129,134,133,123,131,128],
[130,119,131,125,122,0,133,142,139,138,115],
[124,122,125,126,117,118,0,134,117,137,114],
[124,115,121,112,118,109,117,0,104,131,103],
[126,130,126,114,128,112,134,147,0,134,129],
[121,123,122,111,120,113,114,120,117,0,101],
[135,140,124,132,123,136,137,148,122,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,124,144,141,141,129,122,138,120,154],
[126,0,135,142,114,138,136,123,112,114,103],
[127,116,0,148,120,110,146,99,118,102,116],
[107,109,103,0,96,113,122,96,93,91,101],
[110,137,131,155,0,115,122,137,98,125,124],
[110,113,141,138,136,0,103,119,98,118,125],
[122,115,105,129,129,148,0,124,112,99,127],
[129,128,152,155,114,132,127,0,135,118,132],
[113,139,133,158,153,153,139,116,0,126,129],
[131,137,149,160,126,133,152,133,125,0,143],
[97,148,135,150,127,126,124,119,122,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,122,134,122,122,132,135,112,134,133],
[113,0,126,133,130,120,130,120,112,132,133],
[129,125,0,121,127,127,133,134,120,131,146],
[117,118,130,0,106,111,128,115,121,127,128],
[129,121,124,145,0,117,133,126,120,129,136],
[129,131,124,140,134,0,135,123,126,130,137],
[119,121,118,123,118,116,0,129,128,133,129],
[116,131,117,136,125,128,122,0,120,120,129],
[139,139,131,130,131,125,123,131,0,137,138],
[117,119,120,124,122,121,118,131,114,0,124],
[118,118,105,123,115,114,122,122,113,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,108,127,165,162,126,158,146,152,128],
[88,0,82,152,76,108,81,118,127,99,88],
[143,169,0,160,115,137,149,152,139,159,132],
[124,99,91,0,137,68,127,142,96,127,101],
[86,175,136,114,0,149,77,170,144,149,139],
[89,143,114,183,102,0,89,118,136,166,121],
[125,170,102,124,174,162,0,177,124,151,166],
[93,133,99,109,81,133,74,0,138,165,158],
[105,124,112,155,107,115,127,113,0,167,121],
[99,152,92,124,102,85,100,86,84,0,93],
[123,163,119,150,112,130,85,93,130,158,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,120,136,124,140,136,137,128,126,122],
[112,0,113,113,110,121,121,120,103,113,109],
[131,138,0,137,111,132,126,125,112,120,108],
[115,138,114,0,102,132,129,119,118,111,125],
[127,141,140,149,0,135,141,138,133,125,136],
[111,130,119,119,116,0,141,124,117,117,118],
[115,130,125,122,110,110,0,115,102,117,129],
[114,131,126,132,113,127,136,0,123,114,123],
[123,148,139,133,118,134,149,128,0,134,135],
[125,138,131,140,126,134,134,137,117,0,126],
[129,142,143,126,115,133,122,128,116,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,133,124,138,131,132,122,121,129,134],
[124,0,140,132,139,131,131,130,131,129,132],
[118,111,0,123,122,122,121,114,113,122,131],
[127,119,128,0,122,118,141,117,114,119,125],
[113,112,129,129,0,141,132,122,124,126,133],
[120,120,129,133,110,0,123,127,122,123,112],
[119,120,130,110,119,128,0,127,125,116,120],
[129,121,137,134,129,124,124,0,113,127,139],
[130,120,138,137,127,129,126,138,0,124,131],
[122,122,129,132,125,128,135,124,127,0,130],
[117,119,120,126,118,139,131,112,120,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,121,133,130,105,119,127,116,123,110],
[126,0,92,117,103,81,102,118,121,110,101],
[130,159,0,134,141,118,126,148,124,130,134],
[118,134,117,0,132,103,115,122,131,115,112],
[121,148,110,119,0,87,125,140,101,125,108],
[146,170,133,148,164,0,136,147,138,151,121],
[132,149,125,136,126,115,0,121,125,118,131],
[124,133,103,129,111,104,130,0,111,134,91],
[135,130,127,120,150,113,126,140,0,141,127],
[128,141,121,136,126,100,133,117,110,0,110],
[141,150,117,139,143,130,120,160,124,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,137,122,130,123,141,123,115,139,122],
[122,0,130,127,127,130,143,129,120,134,130],
[114,121,0,123,124,124,131,113,113,134,130],
[129,124,128,0,130,137,142,126,124,134,138],
[121,124,127,121,0,120,150,118,134,138,146],
[128,121,127,114,131,0,151,121,111,133,132],
[110,108,120,109,101,100,0,98,107,117,108],
[128,122,138,125,133,130,153,0,116,129,155],
[136,131,138,127,117,140,144,135,0,137,135],
[112,117,117,117,113,118,134,122,114,0,123],
[129,121,121,113,105,119,143,96,116,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,115,115,121,125,126,118,117,136,125],
[137,0,117,111,118,126,117,109,133,133,129],
[136,134,0,133,121,131,134,129,131,133,141],
[136,140,118,0,134,135,133,134,134,144,135],
[130,133,130,117,0,139,133,131,142,134,136],
[126,125,120,116,112,0,117,120,123,116,128],
[125,134,117,118,118,134,0,119,117,134,126],
[133,142,122,117,120,131,132,0,131,140,135],
[134,118,120,117,109,128,134,120,0,127,134],
[115,118,118,107,117,135,117,111,124,0,117],
[126,122,110,116,115,123,125,116,117,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,113,117,106,98,90,118,127,129,116],
[142,0,133,123,136,124,122,152,145,136,126],
[138,118,0,101,105,100,97,122,139,134,123],
[134,128,150,0,123,120,107,139,133,132,143],
[145,115,146,128,0,130,109,137,142,142,137],
[153,127,151,131,121,0,130,143,146,146,132],
[161,129,154,144,142,121,0,144,157,153,149],
[133,99,129,112,114,108,107,0,113,120,119],
[124,106,112,118,109,105,94,138,0,126,119],
[122,115,117,119,109,105,98,131,125,0,134],
[135,125,128,108,114,119,102,132,132,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,146,160,152,132,158,161,143,124,131],
[153,0,152,110,122,178,146,123,163,159,53],
[105,99,0,102,108,91,115,86,166,95,52],
[91,141,149,0,111,148,122,92,88,149,123],
[99,129,143,140,0,131,130,112,159,175,57],
[119,73,160,103,120,0,123,103,167,176,85],
[93,105,136,129,121,128,0,120,100,102,151],
[90,128,165,159,139,148,131,0,145,136,120],
[108,88,85,163,92,84,151,106,0,113,51],
[127,92,156,102,76,75,149,115,138,0,83],
[120,198,199,128,194,166,100,131,200,168,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,126,117,102,104,93,139,119,120,88],
[133,0,133,133,125,119,122,115,128,132,100],
[125,118,0,142,120,128,95,127,110,133,112],
[134,118,109,0,120,115,121,121,121,122,110],
[149,126,131,131,0,106,114,128,113,130,118],
[147,132,123,136,145,0,139,147,155,153,134],
[158,129,156,130,137,112,0,145,125,127,112],
[112,136,124,130,123,104,106,0,128,122,91],
[132,123,141,130,138,96,126,123,0,125,107],
[131,119,118,129,121,98,124,129,126,0,106],
[163,151,139,141,133,117,139,160,144,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,137,111,117,132,112,142,136,126,108],
[141,0,138,123,125,140,124,143,133,145,134],
[114,113,0,113,116,121,124,129,126,114,108],
[140,128,138,0,114,132,130,134,143,139,122],
[134,126,135,137,0,121,127,124,135,131,102],
[119,111,130,119,130,0,107,136,114,118,118],
[139,127,127,121,124,144,0,137,134,125,112],
[109,108,122,117,127,115,114,0,135,125,100],
[115,118,125,108,116,137,117,116,0,110,115],
[125,106,137,112,120,133,126,126,141,0,126],
[143,117,143,129,149,133,139,151,136,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,135,126,133,148,116,131,126,131,119],
[130,0,154,133,129,141,135,147,156,166,125],
[116,97,0,110,107,121,105,111,139,125,122],
[125,118,141,0,119,139,106,136,129,139,148],
[118,122,144,132,0,127,135,142,124,122,117],
[103,110,130,112,124,0,112,135,136,136,124],
[135,116,146,145,116,139,0,165,148,141,136],
[120,104,140,115,109,116,86,0,123,113,104],
[125,95,112,122,127,115,103,128,0,118,120],
[120,85,126,112,129,115,110,138,133,0,125],
[132,126,129,103,134,127,115,147,131,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,122,138,118,127,142,129,125,120,130],
[131,0,127,131,120,141,143,127,141,124,137],
[129,124,0,127,117,131,140,123,126,126,132],
[113,120,124,0,118,129,132,127,131,112,136],
[133,131,134,133,0,134,148,132,133,124,144],
[124,110,120,122,117,0,127,123,123,115,129],
[109,108,111,119,103,124,0,116,125,117,119],
[122,124,128,124,119,128,135,0,126,112,131],
[126,110,125,120,118,128,126,125,0,110,128],
[131,127,125,139,127,136,134,139,141,0,149],
[121,114,119,115,107,122,132,120,123,102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,170,129,144,131,128,173,139,134,116],
[108,0,130,121,148,99,130,150,127,123,115],
[81,121,0,110,124,112,103,126,105,94,86],
[122,130,141,0,152,149,107,123,191,100,140],
[107,103,127,99,0,91,100,107,102,101,116],
[120,152,139,102,160,0,121,141,167,127,130],
[123,121,148,144,151,130,0,148,146,143,125],
[78,101,125,128,144,110,103,0,133,118,102],
[112,124,146,60,149,84,105,118,0,114,103],
[117,128,157,151,150,124,108,133,137,0,123],
[135,136,165,111,135,121,126,149,148,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,83,141,106,137,95,92,142,138,145,154],
[168,0,153,139,164,124,155,171,177,143,171],
[110,98,0,110,124,132,158,107,155,153,145],
[145,112,141,0,154,109,118,150,126,171,167],
[114,87,127,97,0,102,108,128,138,95,128],
[156,127,119,142,149,0,165,158,153,180,151],
[159,96,93,133,143,86,0,106,144,125,141],
[109,80,144,101,123,93,145,0,142,129,126],
[113,74,96,125,113,98,107,109,0,136,135],
[106,108,98,80,156,71,126,122,115,0,123],
[97,80,106,84,123,100,110,125,116,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,113,112,129,104,111,104,113,98,117],
[136,0,118,128,132,116,131,106,128,127,132],
[138,133,0,131,130,121,131,121,135,114,134],
[139,123,120,0,125,103,126,122,120,116,132],
[122,119,121,126,0,108,123,112,124,116,135],
[147,135,130,148,143,0,129,120,135,124,132],
[140,120,120,125,128,122,0,123,133,111,135],
[147,145,130,129,139,131,128,0,127,112,141],
[138,123,116,131,127,116,118,124,0,124,126],
[153,124,137,135,135,127,140,139,127,0,142],
[134,119,117,119,116,119,116,110,125,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,130,149,138,139,129,125,141,140,174],
[129,0,105,128,115,151,139,140,146,138,143],
[121,146,0,139,103,129,138,113,104,129,161],
[102,123,112,0,113,141,130,119,127,106,157],
[113,136,148,138,0,152,159,138,137,126,137],
[112,100,122,110,99,0,111,107,131,142,142],
[122,112,113,121,92,140,0,118,129,112,141],
[126,111,138,132,113,144,133,0,127,121,117],
[110,105,147,124,114,120,122,124,0,121,155],
[111,113,122,145,125,109,139,130,130,0,158],
[77,108,90,94,114,109,110,134,96,93,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,122,118,127,127,121,147,122,123,111],
[127,0,125,112,133,129,122,143,122,133,123],
[129,126,0,122,128,121,123,144,115,128,115],
[133,139,129,0,135,126,126,145,124,131,127],
[124,118,123,116,0,128,126,133,122,117,120],
[124,122,130,125,123,0,130,142,122,137,126],
[130,129,128,125,125,121,0,131,120,126,113],
[104,108,107,106,118,109,120,0,115,116,96],
[129,129,136,127,129,129,131,136,0,134,119],
[128,118,123,120,134,114,125,135,117,0,110],
[140,128,136,124,131,125,138,155,132,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,129,127,129,135,115,133,135,129,136],
[121,0,115,111,113,124,115,125,128,125,122],
[122,136,0,122,133,139,126,136,139,136,131],
[124,140,129,0,136,142,125,138,127,124,131],
[122,138,118,115,0,138,115,128,125,135,121],
[116,127,112,109,113,0,120,125,119,120,115],
[136,136,125,126,136,131,0,131,131,133,127],
[118,126,115,113,123,126,120,0,121,135,124],
[116,123,112,124,126,132,120,130,0,126,118],
[122,126,115,127,116,131,118,116,125,0,113],
[115,129,120,120,130,136,124,127,133,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,124,131,123,134,133,124,129,123,131],
[130,0,121,132,130,130,127,135,134,136,140],
[127,130,0,128,124,121,122,126,127,126,127],
[120,119,123,0,119,132,120,120,125,121,134],
[128,121,127,132,0,125,123,112,128,121,134],
[117,121,130,119,126,0,127,133,125,121,131],
[118,124,129,131,128,124,0,116,129,126,128],
[127,116,125,131,139,118,135,0,129,133,128],
[122,117,124,126,123,126,122,122,0,123,126],
[128,115,125,130,130,130,125,118,128,0,128],
[120,111,124,117,117,120,123,123,125,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,130,128,135,129,133,132,116,126,136],
[129,0,130,124,122,129,144,135,129,134,128],
[121,121,0,120,115,130,127,121,120,111,125],
[123,127,131,0,126,125,126,132,112,126,132],
[116,129,136,125,0,129,130,125,111,120,120],
[122,122,121,126,122,0,120,127,114,113,118],
[118,107,124,125,121,131,0,125,115,109,126],
[119,116,130,119,126,124,126,0,115,110,122],
[135,122,131,139,140,137,136,136,0,124,138],
[125,117,140,125,131,138,142,141,127,0,144],
[115,123,126,119,131,133,125,129,113,107,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,155,123,139,153,111,116,130,137,150],
[116,0,122,128,129,115,119,128,122,140,154],
[96,129,0,110,118,117,89,121,101,124,128],
[128,123,141,0,154,136,106,132,122,124,142],
[112,122,133,97,0,118,109,101,116,116,110],
[98,136,134,115,133,0,125,117,119,117,137],
[140,132,162,145,142,126,0,138,124,142,154],
[135,123,130,119,150,134,113,0,114,129,151],
[121,129,150,129,135,132,127,137,0,120,154],
[114,111,127,127,135,134,109,122,131,0,148],
[101,97,123,109,141,114,97,100,97,103,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,119,116,128,113,118,112,120,104,122],
[119,0,110,109,127,120,111,123,117,111,123],
[132,141,0,129,138,126,112,118,125,123,136],
[135,142,122,0,129,136,130,129,135,129,113],
[123,124,113,122,0,103,108,104,111,100,119],
[138,131,125,115,148,0,128,118,130,128,133],
[133,140,139,121,143,123,0,122,128,118,126],
[139,128,133,122,147,133,129,0,127,132,142],
[131,134,126,116,140,121,123,124,0,123,129],
[147,140,128,122,151,123,133,119,128,0,125],
[129,128,115,138,132,118,125,109,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,103,138,115,104,132,100,122,121,139],
[112,0,102,125,96,112,117,131,106,102,104],
[148,149,0,142,143,126,139,125,130,124,134],
[113,126,109,0,100,111,113,119,101,116,128],
[136,155,108,151,0,132,139,154,125,144,136],
[147,139,125,140,119,0,124,130,119,130,133],
[119,134,112,138,112,127,0,123,107,118,111],
[151,120,126,132,97,121,128,0,114,127,134],
[129,145,121,150,126,132,144,137,0,128,128],
[130,149,127,135,107,121,133,124,123,0,108],
[112,147,117,123,115,118,140,117,123,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,72,72,117,84,92,84,110,51,75],
[136,0,90,111,115,109,117,99,125,78,105],
[179,161,0,133,146,133,116,82,126,111,113],
[179,140,118,0,152,135,136,157,118,103,172],
[134,136,105,99,0,110,143,85,97,124,137],
[167,142,118,116,141,0,119,81,106,121,141],
[159,134,135,115,108,132,0,85,93,141,144],
[167,152,169,94,166,170,166,0,105,113,159],
[141,126,125,133,154,145,158,146,0,131,179],
[200,173,140,148,127,130,110,138,120,0,159],
[176,146,138,79,114,110,107,92,72,92,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,132,124,138,141,130,108,116,122,126],
[127,0,135,142,136,145,153,116,133,121,135],
[119,116,0,126,134,127,122,100,112,107,121],
[127,109,125,0,147,137,127,122,123,131,125],
[113,115,117,104,0,122,119,108,102,112,112],
[110,106,124,114,129,0,120,104,111,124,122],
[121,98,129,124,132,131,0,107,118,119,122],
[143,135,151,129,143,147,144,0,117,137,136],
[135,118,139,128,149,140,133,134,0,125,136],
[129,130,144,120,139,127,132,114,126,0,135],
[125,116,130,126,139,129,129,115,115,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,125,139,98,150,127,107,110,141,124],
[128,0,169,114,131,176,166,98,119,139,134],
[126,82,0,109,91,136,117,88,130,150,126],
[112,137,142,0,116,139,143,97,123,140,138],
[153,120,160,135,0,162,98,129,150,149,143],
[101,75,115,112,89,0,119,87,108,112,108],
[124,85,134,108,153,132,0,111,119,146,137],
[144,153,163,154,122,164,140,0,178,158,128],
[141,132,121,128,101,143,132,73,0,168,128],
[110,112,101,111,102,139,105,93,83,0,137],
[127,117,125,113,108,143,114,123,123,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,119,150,146,127,139,140,130,136,135],
[121,0,123,130,144,125,132,119,114,125,127],
[132,128,0,136,144,123,136,126,118,135,122],
[101,121,115,0,128,103,121,120,117,121,108],
[105,107,107,123,0,96,114,103,118,118,105],
[124,126,128,148,155,0,138,134,131,144,124],
[112,119,115,130,137,113,0,113,108,114,117],
[111,132,125,131,148,117,138,0,133,121,104],
[121,137,133,134,133,120,143,118,0,135,121],
[115,126,116,130,133,107,137,130,116,0,121],
[116,124,129,143,146,127,134,147,130,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,132,134,117,110,123,127,129,119,142],
[133,0,141,136,134,129,130,125,137,119,131],
[119,110,0,123,118,114,119,114,121,109,130],
[117,115,128,0,111,106,124,104,109,113,127],
[134,117,133,140,0,115,128,132,128,120,132],
[141,122,137,145,136,0,127,122,136,125,141],
[128,121,132,127,123,124,0,122,135,125,127],
[124,126,137,147,119,129,129,0,138,128,132],
[122,114,130,142,123,115,116,113,0,114,126],
[132,132,142,138,131,126,126,123,137,0,141],
[109,120,121,124,119,110,124,119,125,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,128,144,142,124,124,126,115,124,127],
[119,0,124,124,138,121,132,123,106,109,128],
[123,127,0,123,126,110,111,119,124,101,118],
[107,127,128,0,134,123,126,124,118,114,123],
[109,113,125,117,0,111,129,126,107,107,126],
[127,130,141,128,140,0,126,135,118,126,133],
[127,119,140,125,122,125,0,136,113,116,130],
[125,128,132,127,125,116,115,0,126,115,129],
[136,145,127,133,144,133,138,125,0,128,136],
[127,142,150,137,144,125,135,136,123,0,135],
[124,123,133,128,125,118,121,122,115,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,137,130,134,136,126,138,141,121,122],
[118,0,144,133,118,129,133,144,145,115,127],
[114,107,0,133,125,111,109,116,125,112,113],
[121,118,118,0,117,121,119,125,141,112,129],
[117,133,126,134,0,116,128,133,134,119,126],
[115,122,140,130,135,0,125,132,137,120,124],
[125,118,142,132,123,126,0,138,128,130,131],
[113,107,135,126,118,119,113,0,117,116,115],
[110,106,126,110,117,114,123,134,0,109,109],
[130,136,139,139,132,131,121,135,142,0,136],
[129,124,138,122,125,127,120,136,142,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,127,120,126,117,137,124,119,123,125],
[137,0,130,124,133,127,134,126,116,134,128],
[124,121,0,126,127,133,137,120,115,128,118],
[131,127,125,0,139,113,132,134,117,128,113],
[125,118,124,112,0,123,118,111,106,141,125],
[134,124,118,138,128,0,134,124,118,136,116],
[114,117,114,119,133,117,0,125,106,124,120],
[127,125,131,117,140,127,126,0,129,127,123],
[132,135,136,134,145,133,145,122,0,130,123],
[128,117,123,123,110,115,127,124,121,0,125],
[126,123,133,138,126,135,131,128,128,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,166,136,121,147,100,127,110,131,92,165],
[85,0,129,101,135,95,99,105,125,101,113],
[115,122,0,155,117,105,93,109,130,131,137],
[130,150,96,0,138,117,104,100,104,87,132],
[104,116,134,113,0,101,115,119,122,81,106],
[151,156,146,134,150,0,98,112,151,97,138],
[124,152,158,147,136,153,0,101,127,101,138],
[141,146,142,151,132,139,150,0,143,110,166],
[120,126,121,147,129,100,124,108,0,144,137],
[159,150,120,164,170,154,150,141,107,0,175],
[86,138,114,119,145,113,113,85,114,76,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,122,121,115,125,141,134,136,125,142],
[111,0,123,122,116,116,129,123,122,119,140],
[129,128,0,118,127,124,127,126,119,125,143],
[130,129,133,0,113,127,142,133,137,131,144],
[136,135,124,138,0,125,139,137,128,135,134],
[126,135,127,124,126,0,141,126,131,128,150],
[110,122,124,109,112,110,0,118,119,118,135],
[117,128,125,118,114,125,133,0,118,118,135],
[115,129,132,114,123,120,132,133,0,125,131],
[126,132,126,120,116,123,133,133,126,0,142],
[109,111,108,107,117,101,116,116,120,109,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,93,112,133,135,139,105,131,119,128],
[130,0,122,101,121,114,134,102,120,92,125],
[158,129,0,134,124,146,153,148,153,143,160],
[139,150,117,0,131,113,157,133,150,153,153],
[118,130,127,120,0,137,145,118,140,134,120],
[116,137,105,138,114,0,118,146,140,118,128],
[112,117,98,94,106,133,0,117,123,122,95],
[146,149,103,118,133,105,134,0,149,125,138],
[120,131,98,101,111,111,128,102,0,125,127],
[132,159,108,98,117,133,129,126,126,0,141],
[123,126,91,98,131,123,156,113,124,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,113,117,112,140,163,89,129,126,95],
[137,0,130,95,125,128,139,138,153,139,97],
[138,121,0,101,93,135,131,151,122,136,127],
[134,156,150,0,142,169,193,164,146,136,106],
[139,126,158,109,0,171,194,184,174,167,115],
[111,123,116,82,80,0,144,87,132,145,143],
[88,112,120,58,57,107,0,121,141,128,82],
[162,113,100,87,67,164,130,0,78,148,102],
[122,98,129,105,77,119,110,173,0,142,65],
[125,112,115,115,84,106,123,103,109,0,83],
[156,154,124,145,136,108,169,149,186,168,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,130,122,130,134,118,128,119,128,129],
[118,0,121,121,117,125,117,119,121,123,123],
[121,130,0,126,126,127,116,128,126,133,131],
[129,130,125,0,126,127,127,126,110,129,122],
[121,134,125,125,0,127,111,112,118,114,127],
[117,126,124,124,124,0,118,122,120,112,122],
[133,134,135,124,140,133,0,126,123,136,134],
[123,132,123,125,139,129,125,0,117,122,136],
[132,130,125,141,133,131,128,134,0,125,129],
[123,128,118,122,137,139,115,129,126,0,132],
[122,128,120,129,124,129,117,115,122,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,122,128,129,123,121,132,113,141,115],
[125,0,127,131,135,121,132,133,130,138,129],
[129,124,0,137,119,126,126,124,117,134,121],
[123,120,114,0,122,119,121,123,125,123,120],
[122,116,132,129,0,114,131,121,126,140,110],
[128,130,125,132,137,0,130,131,137,146,123],
[130,119,125,130,120,121,0,133,116,133,118],
[119,118,127,128,130,120,118,0,115,138,112],
[138,121,134,126,125,114,135,136,0,143,126],
[110,113,117,128,111,105,118,113,108,0,111],
[136,122,130,131,141,128,133,139,125,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,148,127,122,106,155,129,116,109,139,134],
[103,0,105,120,112,125,119,120,113,120,122],
[124,146,0,129,126,141,120,129,120,135,142],
[129,131,122,0,126,139,112,127,130,138,138],
[145,139,125,125,0,156,120,138,127,151,147],
[96,126,110,112,95,0,121,116,106,118,102],
[122,132,131,139,131,130,0,135,121,142,142],
[135,131,122,124,113,135,116,0,117,135,137],
[142,138,131,121,124,145,130,134,0,141,147],
[112,131,116,113,100,133,109,116,110,0,122],
[117,129,109,113,104,149,109,114,104,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,112,140,120,112,115,118,119,123,118],
[140,0,125,139,123,143,128,123,123,121,133],
[139,126,0,148,126,120,122,126,119,126,119],
[111,112,103,0,107,115,104,94,126,119,105],
[131,128,125,144,0,126,115,117,135,131,120],
[139,108,131,136,125,0,115,122,116,128,114],
[136,123,129,147,136,136,0,124,125,136,137],
[133,128,125,157,134,129,127,0,129,141,127],
[132,128,132,125,116,135,126,122,0,131,129],
[128,130,125,132,120,123,115,110,120,0,122],
[133,118,132,146,131,137,114,124,122,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,136,128,139,141,135,145,125,131,126],
[129,0,144,117,131,141,131,149,127,113,117],
[115,107,0,99,127,123,121,134,108,110,97],
[123,134,152,0,148,142,138,153,128,128,124],
[112,120,124,103,0,129,130,130,113,105,103],
[110,110,128,109,122,0,123,130,113,112,99],
[116,120,130,113,121,128,0,121,121,122,100],
[106,102,117,98,121,121,130,0,106,104,110],
[126,124,143,123,138,138,130,145,0,129,116],
[120,138,141,123,146,139,129,147,122,0,118],
[125,134,154,127,148,152,151,141,135,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,127,123,116,110,127,128,124,124,130],
[136,0,126,129,132,133,144,140,137,141,124],
[124,125,0,122,132,134,125,131,127,132,127],
[128,122,129,0,133,120,133,125,132,135,128],
[135,119,119,118,0,121,120,133,127,124,121],
[141,118,117,131,130,0,133,131,127,138,130],
[124,107,126,118,131,118,0,141,117,120,124],
[123,111,120,126,118,120,110,0,115,127,112],
[127,114,124,119,124,124,134,136,0,127,125],
[127,110,119,116,127,113,131,124,124,0,114],
[121,127,124,123,130,121,127,139,126,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,141,124,121,132,126,143,116,111,130],
[127,0,138,134,126,134,138,143,118,128,131],
[110,113,0,120,125,131,126,138,120,113,125],
[127,117,131,0,135,123,131,129,119,111,131],
[130,125,126,116,0,119,116,126,112,110,128],
[119,117,120,128,132,0,141,126,113,123,130],
[125,113,125,120,135,110,0,122,110,116,128],
[108,108,113,122,125,125,129,0,120,119,118],
[135,133,131,132,139,138,141,131,0,122,139],
[140,123,138,140,141,128,135,132,129,0,127],
[121,120,126,120,123,121,123,133,112,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,123,130,117,108,137,117,131,139,124],
[137,0,113,129,133,143,140,124,148,153,126],
[128,138,0,140,131,139,125,150,131,143,136],
[121,122,111,0,123,126,105,127,134,120,116],
[134,118,120,128,0,123,118,112,128,125,131],
[143,108,112,125,128,0,128,143,137,143,128],
[114,111,126,146,133,123,0,134,136,117,132],
[134,127,101,124,139,108,117,0,131,151,106],
[120,103,120,117,123,114,115,120,0,127,97],
[112,98,108,131,126,108,134,100,124,0,114],
[127,125,115,135,120,123,119,145,154,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,113,111,124,141,106,117,140,141,124],
[118,0,94,106,121,137,102,99,98,114,106],
[138,157,0,136,157,167,124,145,138,153,142],
[140,145,115,0,162,153,132,128,141,137,134],
[127,130,94,89,0,149,115,105,135,119,123],
[110,114,84,98,102,0,102,99,103,129,124],
[145,149,127,119,136,149,0,116,120,150,153],
[134,152,106,123,146,152,135,0,160,154,171],
[111,153,113,110,116,148,131,91,0,124,129],
[110,137,98,114,132,122,101,97,127,0,143],
[127,145,109,117,128,127,98,80,122,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,125,122,115,120,127,114,126,116,129],
[119,0,120,120,119,119,122,125,128,111,117],
[126,131,0,121,120,117,131,133,126,113,127],
[129,131,130,0,123,126,129,135,127,126,140],
[136,132,131,128,0,132,129,131,123,117,128],
[131,132,134,125,119,0,128,131,130,113,137],
[124,129,120,122,122,123,0,127,117,108,119],
[137,126,118,116,120,120,124,0,124,113,125],
[125,123,125,124,128,121,134,127,0,117,125],
[135,140,138,125,134,138,143,138,134,0,135],
[122,134,124,111,123,114,132,126,126,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,144,114,121,134,148,153,146,132,138],
[88,0,110,97,95,83,123,118,81,89,111],
[107,141,0,114,115,113,113,126,109,105,128],
[137,154,137,0,125,120,114,143,135,112,119],
[130,156,136,126,0,120,130,152,152,112,128],
[117,168,138,131,131,0,133,154,110,103,147],
[103,128,138,137,121,118,0,149,103,113,113],
[98,133,125,108,99,97,102,0,103,111,119],
[105,170,142,116,99,141,148,148,0,115,143],
[119,162,146,139,139,148,138,140,136,0,155],
[113,140,123,132,123,104,138,132,108,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,112,138,129,125,95,135,117,146,123],
[124,0,133,124,108,116,107,118,132,136,122],
[139,118,0,143,128,139,127,143,111,133,136],
[113,127,108,0,108,125,93,135,114,129,115],
[122,143,123,143,0,151,115,152,133,138,129],
[126,135,112,126,100,0,115,147,121,129,124],
[156,144,124,158,136,136,0,158,131,159,127],
[116,133,108,116,99,104,93,0,117,113,113],
[134,119,140,137,118,130,120,134,0,137,108],
[105,115,118,122,113,122,92,138,114,0,129],
[128,129,115,136,122,127,124,138,143,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,117,136,110,110,127,144,133,112,110],
[127,0,135,139,121,134,119,147,136,124,120],
[134,116,0,121,104,107,133,116,118,119,94],
[115,112,130,0,112,103,110,125,130,109,111],
[141,130,147,139,0,122,121,132,134,129,120],
[141,117,144,148,129,0,146,146,143,133,136],
[124,132,118,141,130,105,0,152,136,120,118],
[107,104,135,126,119,105,99,0,118,100,107],
[118,115,133,121,117,108,115,133,0,97,108],
[139,127,132,142,122,118,131,151,154,0,129],
[141,131,157,140,131,115,133,144,143,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,116,141,119,137,132,127,124,125,125],
[133,0,118,133,118,131,151,127,125,122,130],
[135,133,0,138,131,148,141,136,136,116,121],
[110,118,113,0,120,125,126,122,121,116,104],
[132,133,120,131,0,138,141,131,127,129,132],
[114,120,103,126,113,0,127,121,121,111,113],
[119,100,110,125,110,124,0,117,104,111,106],
[124,124,115,129,120,130,134,0,122,112,114],
[127,126,115,130,124,130,147,129,0,125,120],
[126,129,135,135,122,140,140,139,126,0,126],
[126,121,130,147,119,138,145,137,131,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,153,173,128,135,111,131,138,147,130],
[120,0,124,113,118,146,89,93,95,129,116],
[98,127,0,112,145,125,61,75,84,104,124],
[78,138,139,0,103,126,70,63,72,111,99],
[123,133,106,148,0,145,94,106,117,137,118],
[116,105,126,125,106,0,87,110,113,147,126],
[140,162,190,181,157,164,0,100,150,167,170],
[120,158,176,188,145,141,151,0,146,157,174],
[113,156,167,179,134,138,101,105,0,131,150],
[104,122,147,140,114,104,84,94,120,0,106],
[121,135,127,152,133,125,81,77,101,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,136,115,111,119,102,114,134,129,116],
[117,0,107,106,106,130,109,142,136,145,127],
[115,144,0,98,111,135,113,119,126,110,131],
[136,145,153,0,142,158,131,141,149,150,123],
[140,145,140,109,0,126,109,136,133,126,117],
[132,121,116,93,125,0,120,124,142,130,116],
[149,142,138,120,142,131,0,153,154,175,138],
[137,109,132,110,115,127,98,0,143,128,120],
[117,115,125,102,118,109,97,108,0,122,115],
[122,106,141,101,125,121,76,123,129,0,105],
[135,124,120,128,134,135,113,131,136,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,123,136,127,122,121,121,138,117,126],
[137,0,125,121,123,108,147,135,132,132,119],
[128,126,0,142,110,126,123,115,117,129,119],
[115,130,109,0,113,128,117,137,148,133,119],
[124,128,141,138,0,135,128,144,138,132,140],
[129,143,125,123,116,0,142,145,139,130,139],
[130,104,128,134,123,109,0,136,130,129,102],
[130,116,136,114,107,106,115,0,130,124,115],
[113,119,134,103,113,112,121,121,0,119,119],
[134,119,122,118,119,121,122,127,132,0,120],
[125,132,132,132,111,112,149,136,132,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,133,134,132,130,123,119,132,117,112],
[145,0,125,148,152,138,145,137,131,126,134],
[118,126,0,136,130,130,113,126,113,101,134],
[117,103,115,0,137,127,118,115,109,108,119],
[119,99,121,114,0,131,110,120,116,117,114],
[121,113,121,124,120,0,121,119,125,103,127],
[128,106,138,133,141,130,0,112,113,103,135],
[132,114,125,136,131,132,139,0,124,109,125],
[119,120,138,142,135,126,138,127,0,102,122],
[134,125,150,143,134,148,148,142,149,0,138],
[139,117,117,132,137,124,116,126,129,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,117,105,133,118,157,127,133,134,128],
[126,0,100,117,132,114,120,123,129,119,110],
[134,151,0,134,139,129,150,143,140,120,151],
[146,134,117,0,139,119,136,153,86,109,125],
[118,119,112,112,0,102,145,115,112,109,130],
[133,137,122,132,149,0,164,139,132,158,139],
[94,131,101,115,106,87,0,129,99,105,100],
[124,128,108,98,136,112,122,0,116,107,127],
[118,122,111,165,139,119,152,135,0,112,139],
[117,132,131,142,142,93,146,144,139,0,131],
[123,141,100,126,121,112,151,124,112,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,108,130,108,102,111,111,111,117,115],
[136,0,117,107,99,107,114,108,116,110,125],
[143,134,0,139,98,107,106,114,126,110,112],
[121,144,112,0,117,112,125,136,123,128,123],
[143,152,153,134,0,133,123,156,130,134,131],
[149,144,144,139,118,0,134,136,125,119,129],
[140,137,145,126,128,117,0,141,124,139,127],
[140,143,137,115,95,115,110,0,134,133,123],
[140,135,125,128,121,126,127,117,0,123,126],
[134,141,141,123,117,132,112,118,128,0,123],
[136,126,139,128,120,122,124,128,125,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,115,120,106,109,122,110,96,127,122],
[140,0,140,135,132,122,132,127,126,143,138],
[136,111,0,140,132,122,122,125,114,137,135],
[131,116,111,0,123,116,118,111,120,119,132],
[145,119,119,128,0,110,121,105,112,128,124],
[142,129,129,135,141,0,126,123,109,139,124],
[129,119,129,133,130,125,0,114,123,139,129],
[141,124,126,140,146,128,137,0,116,131,128],
[155,125,137,131,139,142,128,135,0,159,139],
[124,108,114,132,123,112,112,120,92,0,121],
[129,113,116,119,127,127,122,123,112,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,123,121,104,124,109,120,105,118,102],
[137,0,134,122,131,143,131,136,143,130,116],
[128,117,0,141,118,134,113,143,131,113,105],
[130,129,110,0,100,129,108,115,130,114,109],
[147,120,133,151,0,156,132,139,140,130,129],
[127,108,117,122,95,0,113,119,117,104,97],
[142,120,138,143,119,138,0,147,135,129,109],
[131,115,108,136,112,132,104,0,121,108,104],
[146,108,120,121,111,134,116,130,0,99,115],
[133,121,138,137,121,147,122,143,152,0,111],
[149,135,146,142,122,154,142,147,136,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,104,123,110,109,108,107,121,119,121],
[137,0,131,118,133,117,123,134,132,119,116],
[147,120,0,125,124,125,133,136,143,129,134],
[128,133,126,0,129,128,122,128,134,135,130],
[141,118,127,122,0,126,112,121,137,128,119],
[142,134,126,123,125,0,125,135,145,133,122],
[143,128,118,129,139,126,0,133,144,137,125],
[144,117,115,123,130,116,118,0,134,143,132],
[130,119,108,117,114,106,107,117,0,121,116],
[132,132,122,116,123,118,114,108,130,0,122],
[130,135,117,121,132,129,126,119,135,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,103,112,129,128,122,115,112,123,121,124],
[148,0,122,155,133,141,139,141,140,141,143],
[139,129,0,138,144,118,127,135,132,144,135],
[122,96,113,0,129,115,112,103,121,120,117],
[123,118,107,122,0,118,115,109,130,124,126],
[129,110,133,136,133,0,138,122,122,134,141],
[136,112,124,139,136,113,0,117,132,116,132],
[139,110,116,148,142,129,134,0,119,149,122],
[128,111,119,130,121,129,119,132,0,138,117],
[130,110,107,131,127,117,135,102,113,0,103],
[127,108,116,134,125,110,119,129,134,148,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,120,135,135,125,133,127,132,132,139],
[110,0,113,129,124,118,120,112,121,118,120],
[131,138,0,134,125,128,129,128,127,132,140],
[116,122,117,0,126,123,121,125,117,105,133],
[116,127,126,125,0,123,135,112,115,119,124],
[126,133,123,128,128,0,118,116,126,127,134],
[118,131,122,130,116,133,0,118,127,112,122],
[124,139,123,126,139,135,133,0,124,132,129],
[119,130,124,134,136,125,124,127,0,124,127],
[119,133,119,146,132,124,139,119,127,0,143],
[112,131,111,118,127,117,129,122,124,108,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,127,132,135,134,118,149,134,151,128],
[125,0,127,113,105,125,108,132,126,129,114],
[124,124,0,111,99,137,107,131,111,125,108],
[119,138,140,0,118,131,106,125,134,142,141],
[116,146,152,133,0,133,147,143,137,134,147],
[117,126,114,120,118,0,116,144,134,120,106],
[133,143,144,145,104,135,0,144,143,117,136],
[102,119,120,126,108,107,107,0,133,110,112],
[117,125,140,117,114,117,108,118,0,130,109],
[100,122,126,109,117,131,134,141,121,0,132],
[123,137,143,110,104,145,115,139,142,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,108,122,129,135,133,129,127,133,127,126],
[143,0,145,139,150,134,142,139,131,126,122],
[129,106,0,133,146,135,129,142,119,124,115],
[122,112,118,0,122,112,103,124,117,117,103],
[116,101,105,129,0,112,108,132,122,112,107],
[118,117,116,139,139,0,122,126,131,124,122],
[122,109,122,148,143,129,0,123,125,131,120],
[124,112,109,127,119,125,128,0,138,111,118],
[118,120,132,134,129,120,126,113,0,118,120],
[124,125,127,134,139,127,120,140,133,0,120],
[125,129,136,148,144,129,131,133,131,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,143,125,140,134,131,132,127,135,136],
[138,0,140,132,126,139,133,121,138,141,136],
[108,111,0,119,116,118,124,114,127,116,135],
[126,119,132,0,127,141,122,126,130,131,137],
[111,125,135,124,0,134,120,124,129,118,125],
[117,112,133,110,117,0,125,114,120,124,134],
[120,118,127,129,131,126,0,120,122,123,124],
[119,130,137,125,127,137,131,0,128,125,136],
[124,113,124,121,122,131,129,123,0,122,126],
[116,110,135,120,133,127,128,126,129,0,137],
[115,115,116,114,126,117,127,115,125,114,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,157,164,159,178,143,155,161,144,140],
[137,0,133,132,129,137,115,120,122,132,138],
[94,118,0,135,120,136,111,121,125,129,132],
[87,119,116,0,120,139,109,128,134,133,115],
[92,122,131,131,0,136,128,116,122,133,139],
[73,114,115,112,115,0,108,114,119,106,106],
[108,136,140,142,123,143,0,127,124,140,131],
[96,131,130,123,135,137,124,0,138,145,151],
[90,129,126,117,129,132,127,113,0,133,113],
[107,119,122,118,118,145,111,106,118,0,106],
[111,113,119,136,112,145,120,100,138,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,122,120,141,123,127,132,122,115,109],
[125,0,133,141,122,139,157,153,133,137,136],
[129,118,0,136,108,138,124,128,120,120,107],
[131,110,115,0,115,119,119,127,106,118,106],
[110,129,143,136,0,134,139,130,133,137,127],
[128,112,113,132,117,0,130,131,112,116,109],
[124,94,127,132,112,121,0,137,121,135,114],
[119,98,123,124,121,120,114,0,124,99,105],
[129,118,131,145,118,139,130,127,0,123,136],
[136,114,131,133,114,135,116,152,128,0,115],
[142,115,144,145,124,142,137,146,115,136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,148,132,124,124,135,139,124,139,145],
[118,0,133,122,130,128,134,143,133,127,135],
[103,118,0,111,118,124,108,121,108,124,129],
[119,129,140,0,132,124,118,124,117,130,139],
[127,121,133,119,0,124,126,125,141,116,139],
[127,123,127,127,127,0,134,127,137,130,139],
[116,117,143,133,125,117,0,128,130,132,140],
[112,108,130,127,126,124,123,0,119,124,129],
[127,118,143,134,110,114,121,132,0,136,137],
[112,124,127,121,135,121,119,127,115,0,127],
[106,116,122,112,112,112,111,122,114,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,142,122,107,113,129,148,99,141,124],
[107,0,82,99,144,106,92,132,127,123,109],
[109,169,0,129,141,142,128,140,138,118,119],
[129,152,122,0,125,162,141,113,159,147,97],
[144,107,110,126,0,131,133,113,130,135,138],
[138,145,109,89,120,0,138,151,156,89,79],
[122,159,123,110,118,113,0,105,145,101,91],
[103,119,111,138,138,100,146,0,98,114,87],
[152,124,113,92,121,95,106,153,0,116,108],
[110,128,133,104,116,162,150,137,135,0,123],
[127,142,132,154,113,172,160,164,143,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,126,108,110,121,123,110,123,121,118],
[131,0,150,130,126,141,130,122,124,144,138],
[125,101,0,100,105,110,120,108,120,120,105],
[143,121,151,0,115,121,129,125,133,137,139],
[141,125,146,136,0,134,147,126,134,130,133],
[130,110,141,130,117,0,121,119,117,136,123],
[128,121,131,122,104,130,0,113,131,135,129],
[141,129,143,126,125,132,138,0,135,133,136],
[128,127,131,118,117,134,120,116,0,135,124],
[130,107,131,114,121,115,116,118,116,0,111],
[133,113,146,112,118,128,122,115,127,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,122,159,146,120,129,126,127,126,148],
[126,0,127,152,150,121,149,139,141,143,154],
[129,124,0,155,164,129,127,140,139,126,149],
[92,99,96,0,137,98,113,112,121,104,118],
[105,101,87,114,0,103,114,89,103,107,117],
[131,130,122,153,148,0,136,117,148,123,145],
[122,102,124,138,137,115,0,127,131,118,144],
[125,112,111,139,162,134,124,0,142,123,156],
[124,110,112,130,148,103,120,109,0,120,144],
[125,108,125,147,144,128,133,128,131,0,136],
[103,97,102,133,134,106,107,95,107,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,130,126,131,120,119,128,123,106,135],
[138,0,122,126,122,128,124,126,127,135,139],
[121,129,0,136,128,140,117,135,125,135,132],
[125,125,115,0,124,130,114,106,111,109,118],
[120,129,123,127,0,127,130,133,125,130,129],
[131,123,111,121,124,0,114,109,98,106,137],
[132,127,134,137,121,137,0,138,115,117,138],
[123,125,116,145,118,142,113,0,111,134,133],
[128,124,126,140,126,153,136,140,0,129,142],
[145,116,116,142,121,145,134,117,122,0,125],
[116,112,119,133,122,114,113,118,109,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,127,127,131,139,124,117,125,134,130],
[118,0,115,118,107,133,117,115,122,132,132],
[124,136,0,120,126,124,135,123,125,134,137],
[124,133,131,0,114,141,130,132,129,140,142],
[120,144,125,137,0,149,134,130,129,132,139],
[112,118,127,110,102,0,116,101,122,128,138],
[127,134,116,121,117,135,0,111,126,134,137],
[134,136,128,119,121,150,140,0,135,137,141],
[126,129,126,122,122,129,125,116,0,126,126],
[117,119,117,111,119,123,117,114,125,0,129],
[121,119,114,109,112,113,114,110,125,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,192,119,130,155,113,158,115,172,152],
[100,0,144,126,126,131,125,132,137,105,135],
[59,107,0,95,136,100,92,80,104,110,123],
[132,125,156,0,111,146,146,150,144,138,100],
[121,125,115,140,0,142,129,137,148,133,126],
[96,120,151,105,109,0,146,128,144,135,134],
[138,126,159,105,122,105,0,117,151,147,160],
[93,119,171,101,114,123,134,0,93,145,170],
[136,114,147,107,103,107,100,158,0,120,119],
[79,146,141,113,118,116,104,106,131,0,118],
[99,116,128,151,125,117,91,81,132,133,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,119,106,126,119,119,128,118,127,122],
[130,0,131,130,142,123,129,131,121,136,128],
[132,120,0,118,130,118,130,127,119,132,123],
[145,121,133,0,132,112,130,137,132,143,136],
[125,109,121,119,0,115,122,124,113,124,121],
[132,128,133,139,136,0,121,131,119,139,119],
[132,122,121,121,129,130,0,134,117,128,131],
[123,120,124,114,127,120,117,0,112,130,124],
[133,130,132,119,138,132,134,139,0,131,135],
[124,115,119,108,127,112,123,121,120,0,123],
[129,123,128,115,130,132,120,127,116,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,130,110,107,125,124,107,106,117,132],
[131,0,136,129,116,131,124,119,121,110,121],
[121,115,0,110,107,100,111,104,105,108,119],
[141,122,141,0,123,131,137,119,121,112,143],
[144,135,144,128,0,134,127,120,133,137,136],
[126,120,151,120,117,0,134,110,115,113,133],
[127,127,140,114,124,117,0,113,113,123,139],
[144,132,147,132,131,141,138,0,126,122,145],
[145,130,146,130,118,136,138,125,0,138,136],
[134,141,143,139,114,138,128,129,113,0,134],
[119,130,132,108,115,118,112,106,115,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,125,126,128,110,121,129,141,115,124],
[111,0,133,121,99,109,124,123,126,118,111],
[126,118,0,113,115,105,110,132,123,110,130],
[125,130,138,0,118,125,127,127,128,118,135],
[123,152,136,133,0,126,126,125,135,123,137],
[141,142,146,126,125,0,140,134,136,152,140],
[130,127,141,124,125,111,0,122,135,127,137],
[122,128,119,124,126,117,129,0,137,114,140],
[110,125,128,123,116,115,116,114,0,132,129],
[136,133,141,133,128,99,124,137,119,0,138],
[127,140,121,116,114,111,114,111,122,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,112,128,126,132,131,146,134,130,118],
[122,0,99,120,135,111,117,115,117,104,123],
[139,152,0,118,142,133,122,120,125,130,137],
[123,131,133,0,147,137,121,139,123,111,154],
[125,116,109,104,0,120,127,112,146,112,131],
[119,140,118,114,131,0,106,122,115,93,128],
[120,134,129,130,124,145,0,126,136,115,140],
[105,136,131,112,139,129,125,0,125,105,106],
[117,134,126,128,105,136,115,126,0,115,116],
[121,147,121,140,139,158,136,146,136,0,135],
[133,128,114,97,120,123,111,145,135,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,109,127,184,129,136,139,115,156,143],
[123,0,114,174,167,109,124,120,131,160,168],
[142,137,0,168,164,121,165,117,121,126,153],
[124,77,83,0,141,114,121,108,118,128,124],
[67,84,87,110,0,85,97,86,91,87,110],
[122,142,130,137,166,0,147,124,114,159,155],
[115,127,86,130,154,104,0,107,128,116,178],
[112,131,134,143,165,127,144,0,136,152,143],
[136,120,130,133,160,137,123,115,0,158,141],
[95,91,125,123,164,92,135,99,93,0,153],
[108,83,98,127,141,96,73,108,110,98,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,136,149,143,130,141,125,127,140,134],
[126,0,129,118,118,116,146,112,120,123,131],
[115,122,0,126,126,112,135,113,126,126,132],
[102,133,125,0,120,131,126,111,111,121,132],
[108,133,125,131,0,123,137,129,121,130,138],
[121,135,139,120,128,0,139,119,133,139,142],
[110,105,116,125,114,112,0,113,114,119,124],
[126,139,138,140,122,132,138,0,131,134,136],
[124,131,125,140,130,118,137,120,0,144,133],
[111,128,125,130,121,112,132,117,107,0,127],
[117,120,119,119,113,109,127,115,118,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,148,130,101,119,126,129,132,121,135],
[125,0,126,121,115,117,132,132,128,109,117],
[103,125,0,116,122,126,127,142,132,126,129],
[121,130,135,0,118,127,140,129,139,117,140],
[150,136,129,133,0,123,140,127,154,128,131],
[132,134,125,124,128,0,141,125,134,115,121],
[125,119,124,111,111,110,0,123,129,102,126],
[122,119,109,122,124,126,128,0,127,105,120],
[119,123,119,112,97,117,122,124,0,111,111],
[130,142,125,134,123,136,149,146,140,0,130],
[116,134,122,111,120,130,125,131,140,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,133,106,133,146,129,128,111,123,132],
[129,0,119,104,119,139,111,115,124,103,131],
[118,132,0,118,132,127,117,112,102,97,133],
[145,147,133,0,157,152,133,118,141,126,143],
[118,132,119,94,0,128,94,101,108,98,120],
[105,112,124,99,123,0,100,105,92,82,113],
[122,140,134,118,157,151,0,121,129,112,155],
[123,136,139,133,150,146,130,0,131,99,127],
[140,127,149,110,143,159,122,120,0,126,143],
[128,148,154,125,153,169,139,152,125,0,155],
[119,120,118,108,131,138,96,124,108,96,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,126,110,136,132,112,160,130,118,128],
[128,0,98,127,131,110,120,145,126,134,143],
[125,153,0,119,152,169,138,126,128,108,125],
[141,124,132,0,139,153,151,172,130,112,116],
[115,120,99,112,0,142,142,123,110,129,118],
[119,141,82,98,109,0,153,123,115,89,130],
[139,131,113,100,109,98,0,133,128,111,102],
[91,106,125,79,128,128,118,0,93,114,119],
[121,125,123,121,141,136,123,158,0,124,125],
[133,117,143,139,122,162,140,137,127,0,141],
[123,108,126,135,133,121,149,132,126,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,128,122,124,117,123,116,110,141,117,129],
[123,0,115,119,124,119,120,119,147,137,119],
[129,136,0,136,143,136,134,142,142,125,128],
[127,132,115,0,126,132,136,137,158,132,133],
[134,127,108,125,0,119,120,117,144,140,112],
[128,132,115,119,132,0,138,124,125,130,126],
[135,131,117,115,131,113,0,129,143,143,126],
[141,132,109,114,134,127,122,0,144,128,121],
[110,104,109,93,107,126,108,107,0,100,101],
[134,114,126,119,111,121,108,123,151,0,116],
[122,132,123,118,139,125,125,130,150,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,127,124,117,130,124,131,127,129,140],
[136,0,138,129,132,137,123,137,123,132,141],
[124,113,0,127,123,120,125,130,120,126,131],
[127,122,124,0,132,115,119,129,130,126,128],
[134,119,128,119,0,125,114,134,128,122,133],
[121,114,131,136,126,0,119,125,125,127,124],
[127,128,126,132,137,132,0,132,135,123,143],
[120,114,121,122,117,126,119,0,130,120,118],
[124,128,131,121,123,126,116,121,0,117,126],
[122,119,125,125,129,124,128,131,134,0,132],
[111,110,120,123,118,127,108,133,125,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,111,133,150,137,149,98,131,137,135],
[131,0,128,126,122,151,153,113,121,113,128],
[140,123,0,135,168,151,148,116,164,132,145],
[118,125,116,0,116,154,130,109,148,118,150],
[101,129,83,135,0,130,130,101,139,123,131],
[114,100,100,97,121,0,116,126,130,121,110],
[102,98,103,121,121,135,0,110,123,108,115],
[153,138,135,142,150,125,141,0,151,143,145],
[120,130,87,103,112,121,128,100,0,103,123],
[114,138,119,133,128,130,143,108,148,0,131],
[116,123,106,101,120,141,136,106,128,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,107,119,125,127,113,131,124,113,129],
[130,0,123,121,116,127,126,127,109,117,122],
[144,128,0,117,114,133,143,134,111,116,120],
[132,130,134,0,131,128,126,124,128,116,140],
[126,135,137,120,0,131,138,134,123,126,126],
[124,124,118,123,120,0,131,119,122,114,129],
[138,125,108,125,113,120,0,124,112,110,122],
[120,124,117,127,117,132,127,0,109,114,114],
[127,142,140,123,128,129,139,142,0,119,140],
[138,134,135,135,125,137,141,137,132,0,141],
[122,129,131,111,125,122,129,137,111,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,128,133,139,143,131,129,131,135,113],
[125,0,130,138,120,139,126,125,133,123,120],
[123,121,0,128,129,125,127,125,141,133,117],
[118,113,123,0,133,138,118,115,135,129,123],
[112,131,122,118,0,127,118,116,126,137,115],
[108,112,126,113,124,0,115,111,118,125,108],
[120,125,124,133,133,136,0,122,147,146,127],
[122,126,126,136,135,140,129,0,135,127,129],
[120,118,110,116,125,133,104,116,0,123,113],
[116,128,118,122,114,126,105,124,128,0,111],
[138,131,134,128,136,143,124,122,138,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,147,128,123,124,136,128,125,131,144,134],
[104,0,127,113,115,127,101,115,107,113,123],
[123,124,0,122,121,122,117,120,110,125,131],
[128,138,129,0,125,117,123,123,123,129,131],
[127,136,130,126,0,129,115,126,121,126,139],
[115,124,129,134,122,0,112,127,131,139,141],
[123,150,134,128,136,139,0,129,132,134,146],
[126,136,131,128,125,124,122,0,118,129,125],
[120,144,141,128,130,120,119,133,0,136,146],
[107,138,126,122,125,112,117,122,115,0,121],
[117,128,120,120,112,110,105,126,105,130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,107,108,107,114,133,123,120,108,122,96],
[144,0,104,132,121,133,128,132,121,128,112],
[143,147,0,125,122,127,124,126,113,130,130],
[144,119,126,0,122,128,122,141,130,127,124],
[137,130,129,129,0,130,140,113,115,136,110],
[118,118,124,123,121,0,120,118,117,118,108],
[128,123,127,129,111,131,0,123,121,132,112],
[131,119,125,110,138,133,128,0,118,131,120],
[143,130,138,121,136,134,130,133,0,139,123],
[129,123,121,124,115,133,119,120,112,0,111],
[155,139,121,127,141,143,139,131,128,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,112,135,124,136,139,125,102,145,143,132],
[139,0,126,138,169,139,122,120,130,140,170],
[116,125,0,107,120,119,121,110,104,112,140],
[127,113,144,0,116,133,139,118,126,117,166],
[115,82,131,135,0,133,101,108,120,125,136],
[112,112,132,118,118,0,137,120,150,123,128],
[126,129,130,112,150,114,0,128,124,130,144],
[149,131,141,133,143,131,123,0,137,131,161],
[106,121,147,125,131,101,127,114,0,121,117],
[108,111,139,134,126,128,121,120,130,0,135],
[119,81,111,85,115,123,107,90,134,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,127,119,122,120,121,123,117,120,128],
[120,0,128,123,127,127,127,129,129,115,118],
[124,123,0,125,116,125,129,129,124,118,118],
[132,128,126,0,121,126,131,120,134,126,127],
[129,124,135,130,0,121,122,122,129,133,120],
[131,124,126,125,130,0,128,133,125,108,121],
[130,124,122,120,129,123,0,127,125,116,123],
[128,122,122,131,129,118,124,0,120,115,131],
[134,122,127,117,122,126,126,131,0,115,125],
[131,136,133,125,118,143,135,136,136,0,126],
[123,133,133,124,131,130,128,120,126,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,127,146,126,122,127,141,138,135,131],
[118,0,141,139,115,104,134,124,131,127,129],
[124,110,0,145,131,107,126,129,131,125,121],
[105,112,106,0,108,104,126,123,118,119,96],
[125,136,120,143,0,103,128,122,132,125,116],
[129,147,144,147,148,0,146,142,141,142,122],
[124,117,125,125,123,105,0,131,129,124,114],
[110,127,122,128,129,109,120,0,124,117,118],
[113,120,120,133,119,110,122,127,0,115,115],
[116,124,126,132,126,109,127,134,136,0,120],
[120,122,130,155,135,129,137,133,136,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,134,117,131,145,139,129,153,132,123],
[125,0,118,128,135,137,124,100,144,126,102],
[117,133,0,119,137,147,138,124,134,132,128],
[134,123,132,0,131,120,126,114,133,116,108],
[120,116,114,120,0,114,124,109,141,126,111],
[106,114,104,131,137,0,110,112,112,106,96],
[112,127,113,125,127,141,0,121,134,116,111],
[122,151,127,137,142,139,130,0,136,129,106],
[98,107,117,118,110,139,117,115,0,115,125],
[119,125,119,135,125,145,135,122,136,0,116],
[128,149,123,143,140,155,140,145,126,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,177,159,175,126,154,234,146,192,114,191],
[74,0,132,125,116,80,145,86,119,116,99],
[92,119,0,165,92,110,160,87,114,127,93],
[76,126,86,0,62,118,141,48,122,91,72],
[125,135,159,189,0,119,176,130,160,104,143],
[97,171,141,133,132,0,151,94,142,106,123],
[17,106,91,110,75,100,0,62,80,97,48],
[105,165,164,203,121,157,189,0,169,146,149],
[59,132,137,129,91,109,171,82,0,88,115],
[137,135,124,160,147,145,154,105,163,0,134],
[60,152,158,179,108,128,203,102,136,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,134,141,141,133,120,130,142,143,125],
[131,0,126,124,132,128,129,126,134,144,130],
[117,125,0,134,128,122,128,136,127,127,124],
[110,127,117,0,134,118,115,113,128,129,123],
[110,119,123,117,0,114,117,113,129,123,121],
[118,123,129,133,137,0,118,119,134,128,121],
[131,122,123,136,134,133,0,118,129,137,114],
[121,125,115,138,138,132,133,0,126,125,125],
[109,117,124,123,122,117,122,125,0,126,118],
[108,107,124,122,128,123,114,126,125,0,114],
[126,121,127,128,130,130,137,126,133,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,134,131,129,116,136,129,124,129,131],
[122,0,122,117,127,128,118,123,116,128,127],
[117,129,0,132,132,126,132,132,125,135,130],
[120,134,119,0,127,120,118,126,125,136,121],
[122,124,119,124,0,130,131,129,128,134,124],
[135,123,125,131,121,0,114,143,126,130,114],
[115,133,119,133,120,137,0,123,131,138,130],
[122,128,119,125,122,108,128,0,109,127,112],
[127,135,126,126,123,125,120,142,0,135,131],
[122,123,116,115,117,121,113,124,116,0,110],
[120,124,121,130,127,137,121,139,120,141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,136,141,109,127,133,135,134,122,140],
[118,0,146,104,106,123,116,128,131,131,153],
[115,105,0,105,94,108,101,98,100,108,124],
[110,147,146,0,114,123,108,132,128,131,149],
[142,145,157,137,0,145,118,142,138,144,134],
[124,128,143,128,106,0,117,126,138,130,123],
[118,135,150,143,133,134,0,128,130,139,130],
[116,123,153,119,109,125,123,0,134,132,143],
[117,120,151,123,113,113,121,117,0,141,134],
[129,120,143,120,107,121,112,119,110,0,136],
[111,98,127,102,117,128,121,108,117,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,134,139,127,138,118,128,129,126,137],
[127,0,130,124,144,127,121,125,135,120,136],
[117,121,0,122,134,131,118,115,132,108,137],
[112,127,129,0,127,129,119,127,133,114,132],
[124,107,117,124,0,120,120,116,134,130,128],
[113,124,120,122,131,0,114,127,127,119,119],
[133,130,133,132,131,137,0,120,143,121,132],
[123,126,136,124,135,124,131,0,131,107,127],
[122,116,119,118,117,124,108,120,0,118,127],
[125,131,143,137,121,132,130,144,133,0,139],
[114,115,114,119,123,132,119,124,124,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,124,130,122,121,128,115,118,121,121],
[120,0,125,134,126,126,126,120,130,122,115],
[127,126,0,118,132,128,131,115,121,125,124],
[121,117,133,0,121,124,131,118,119,115,122],
[129,125,119,130,0,120,120,115,121,120,116],
[130,125,123,127,131,0,118,117,124,108,118],
[123,125,120,120,131,133,0,117,123,112,119],
[136,131,136,133,136,134,134,0,137,133,117],
[133,121,130,132,130,127,128,114,0,111,116],
[130,129,126,136,131,143,139,118,140,0,127],
[130,136,127,129,135,133,132,134,135,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,132,127,117,131,126,135,122,133,140],
[134,0,112,118,118,142,111,143,108,123,151],
[119,139,0,117,129,122,104,142,101,132,146],
[124,133,134,0,130,133,115,133,96,141,148],
[134,133,122,121,0,150,117,147,128,142,138],
[120,109,129,118,101,0,103,127,98,129,127],
[125,140,147,136,134,148,0,124,114,120,135],
[116,108,109,118,104,124,127,0,92,134,136],
[129,143,150,155,123,153,137,159,0,148,165],
[118,128,119,110,109,122,131,117,103,0,127],
[111,100,105,103,113,124,116,115,86,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,125,125,124,127,124,119,120,125,109],
[122,0,122,132,126,121,129,115,123,138,122],
[126,129,0,129,125,118,126,112,117,133,115],
[126,119,122,0,123,125,126,128,119,143,116],
[127,125,126,128,0,120,125,128,119,129,124],
[124,130,133,126,131,0,123,128,127,139,121],
[127,122,125,125,126,128,0,124,123,133,112],
[132,136,139,123,123,123,127,0,121,133,127],
[131,128,134,132,132,124,128,130,0,144,121],
[126,113,118,108,122,112,118,118,107,0,112],
[142,129,136,135,127,130,139,124,130,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,141,168,121,118,166,119,149,107,133,97],
[110,0,180,132,143,177,124,151,114,137,119],
[83,71,0,124,61,135,116,111,127,92,92],
[130,119,127,0,114,136,117,138,115,105,113],
[133,108,190,137,0,171,107,146,166,113,136],
[85,74,116,115,80,0,103,98,122,86,103],
[132,127,135,134,144,148,0,144,132,137,121],
[102,100,140,113,105,153,107,0,115,125,90],
[144,137,124,136,85,129,119,136,0,119,154],
[118,114,159,146,138,165,114,126,132,0,97],
[154,132,159,138,115,148,130,161,97,154,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,144,135,143,114,117,134,132,117,142],
[121,0,123,123,144,113,113,125,123,117,126],
[107,128,0,109,120,106,117,116,126,124,119],
[116,128,142,0,130,127,118,132,126,135,133],
[108,107,131,121,0,114,121,114,120,112,120],
[137,138,145,124,137,0,145,138,135,139,128],
[134,138,134,133,130,106,0,143,137,122,139],
[117,126,135,119,137,113,108,0,126,122,126],
[119,128,125,125,131,116,114,125,0,129,136],
[134,134,127,116,139,112,129,129,122,0,119],
[109,125,132,118,131,123,112,125,115,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,111,116,137,138,122,124,122,118,125],
[133,0,129,120,132,152,120,124,118,125,131],
[140,122,0,137,141,143,130,134,122,127,130],
[135,131,114,0,139,138,127,128,125,119,133],
[114,119,110,112,0,128,113,122,113,120,118],
[113,99,108,113,123,0,114,122,106,114,110],
[129,131,121,124,138,137,0,132,121,127,129],
[127,127,117,123,129,129,119,0,112,114,121],
[129,133,129,126,138,145,130,139,0,121,122],
[133,126,124,132,131,137,124,137,130,0,135],
[126,120,121,118,133,141,122,130,129,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,121,128,127,125,127,144,135,152,132],
[106,0,109,111,104,117,124,138,121,123,124],
[130,142,0,132,131,120,132,146,138,125,120],
[123,140,119,0,125,117,127,152,147,134,128],
[124,147,120,126,0,127,129,153,137,133,134],
[126,134,131,134,124,0,137,149,133,138,126],
[124,127,119,124,122,114,0,154,132,124,128],
[107,113,105,99,98,102,97,0,108,114,111],
[116,130,113,104,114,118,119,143,0,124,116],
[99,128,126,117,118,113,127,137,127,0,128],
[119,127,131,123,117,125,123,140,135,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,139,124,129,128,142,127,124,128,144],
[116,0,137,112,131,119,133,121,120,128,134],
[112,114,0,108,123,103,129,104,116,116,124],
[127,139,143,0,131,116,137,116,127,130,127],
[122,120,128,120,0,129,116,112,116,121,121],
[123,132,148,135,122,0,137,127,117,130,134],
[109,118,122,114,135,114,0,110,119,121,120],
[124,130,147,135,139,124,141,0,130,135,129],
[127,131,135,124,135,134,132,121,0,135,140],
[123,123,135,121,130,121,130,116,116,0,134],
[107,117,127,124,130,117,131,122,111,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,124,123,116,114,120,124,118,129,140],
[131,0,117,120,128,106,117,128,117,134,117],
[127,134,0,125,118,117,128,122,113,138,141],
[128,131,126,0,128,121,140,135,117,127,140],
[135,123,133,123,0,132,120,127,142,148,146],
[137,145,134,130,119,0,141,134,119,135,147],
[131,134,123,111,131,110,0,130,98,119,123],
[127,123,129,116,124,117,121,0,104,122,136],
[133,134,138,134,109,132,153,147,0,137,147],
[122,117,113,124,103,116,132,129,114,0,128],
[111,134,110,111,105,104,128,115,104,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,120,132,125,124,126,135,119,135,114],
[111,0,119,126,124,126,122,137,121,128,120],
[131,132,0,126,125,131,118,132,113,128,124],
[119,125,125,0,120,122,127,123,111,133,115],
[126,127,126,131,0,126,132,141,125,136,130],
[127,125,120,129,125,0,133,127,128,132,120],
[125,129,133,124,119,118,0,119,112,125,120],
[116,114,119,128,110,124,132,0,118,121,110],
[132,130,138,140,126,123,139,133,0,130,123],
[116,123,123,118,115,119,126,130,121,0,116],
[137,131,127,136,121,131,131,141,128,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,131,119,123,127,117,114,110,115,117],
[128,0,131,131,124,126,123,128,128,128,115],
[120,120,0,125,127,129,121,137,122,128,121],
[132,120,126,0,116,121,111,127,114,120,116],
[128,127,124,135,0,118,115,130,119,119,120],
[124,125,122,130,133,0,129,126,130,124,113],
[134,128,130,140,136,122,0,139,132,141,120],
[137,123,114,124,121,125,112,0,124,123,112],
[141,123,129,137,132,121,119,127,0,124,129],
[136,123,123,131,132,127,110,128,127,0,125],
[134,136,130,135,131,138,131,139,122,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,115,121,114,115,106,109,102,109,112,109],
[136,0,127,138,128,123,125,114,129,123,126],
[130,124,0,129,136,124,138,133,138,127,123],
[137,113,122,0,123,106,106,103,122,120,106],
[136,123,115,128,0,135,114,125,120,134,121],
[145,128,127,145,116,0,125,126,117,124,119],
[142,126,113,145,137,126,0,119,136,131,117],
[149,137,118,148,126,125,132,0,140,133,122],
[142,122,113,129,131,134,115,111,0,115,118],
[139,128,124,131,117,127,120,118,136,0,130],
[142,125,128,145,130,132,134,129,133,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,106,111,118,104,112,113,115,96,121,120],
[145,0,121,123,123,123,123,121,117,122,135],
[140,130,0,126,122,115,126,120,115,115,127],
[133,128,125,0,124,115,121,127,124,122,124],
[147,128,129,127,0,126,128,129,118,125,133],
[139,128,136,136,125,0,134,134,123,124,121],
[138,128,125,130,123,117,0,124,119,121,132],
[136,130,131,124,122,117,127,0,135,128,146],
[155,134,136,127,133,128,132,116,0,136,127],
[130,129,136,129,126,127,130,123,115,0,132],
[131,116,124,127,118,130,119,105,124,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,134,139,122,116,102,114,115,126,132],
[122,0,141,133,124,134,107,122,122,129,136],
[117,110,0,109,107,115,105,119,118,118,114],
[112,118,142,0,118,125,110,121,114,114,132],
[129,127,144,133,0,130,121,130,117,132,125],
[135,117,136,126,121,0,106,114,128,128,126],
[149,144,146,141,130,145,0,123,126,139,141],
[137,129,132,130,121,137,128,0,133,128,129],
[136,129,133,137,134,123,125,118,0,130,132],
[125,122,133,137,119,123,112,123,121,0,127],
[119,115,137,119,126,125,110,122,119,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,130,130,135,117,117,120,117,105,127],
[116,0,114,127,127,109,116,114,105,115,112],
[121,137,0,131,137,101,122,119,117,113,125],
[121,124,120,0,117,111,108,126,112,110,104],
[116,124,114,134,0,111,124,115,105,115,116],
[134,142,150,140,140,0,131,143,120,138,142],
[134,135,129,143,127,120,0,135,132,124,123],
[131,137,132,125,136,108,116,0,127,126,132],
[134,146,134,139,146,131,119,124,0,131,128],
[146,136,138,141,136,113,127,125,120,0,131],
[124,139,126,147,135,109,128,119,123,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,110,113,128,147,117,143,129,120,120],
[126,0,112,100,129,139,111,129,126,120,110],
[141,139,0,115,131,149,135,153,138,124,122],
[138,151,136,0,134,147,126,165,140,120,145],
[123,122,120,117,0,141,114,136,132,117,117],
[104,112,102,104,110,0,91,122,124,101,106],
[134,140,116,125,137,160,0,155,141,120,138],
[108,122,98,86,115,129,96,0,116,92,113],
[122,125,113,111,119,127,110,135,0,109,103],
[131,131,127,131,134,150,131,159,142,0,125],
[131,141,129,106,134,145,113,138,148,126,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,149,142,137,126,138,118,137,137],
[124,0,124,134,128,123,126,140,113,126,120],
[128,127,0,135,128,133,124,143,127,132,134],
[102,117,116,0,121,111,111,116,107,121,113],
[109,123,123,130,0,123,121,124,104,120,120],
[114,128,118,140,128,0,125,126,125,125,114],
[125,125,127,140,130,126,0,132,112,118,114],
[113,111,108,135,127,125,119,0,108,114,116],
[133,138,124,144,147,126,139,143,0,130,131],
[114,125,119,130,131,126,133,137,121,0,124],
[114,131,117,138,131,137,137,135,120,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,116,127,141,135,123,122,134,111,134],
[122,0,114,132,133,116,130,115,125,111,122],
[135,137,0,137,134,131,122,119,129,117,132],
[124,119,114,0,122,114,125,124,129,112,122],
[110,118,117,129,0,116,120,118,117,119,120],
[116,135,120,137,135,0,117,131,125,126,129],
[128,121,129,126,131,134,0,134,128,117,131],
[129,136,132,127,133,120,117,0,129,124,129],
[117,126,122,122,134,126,123,122,0,117,130],
[140,140,134,139,132,125,134,127,134,0,140],
[117,129,119,129,131,122,120,122,121,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,131,125,127,121,126,120,123,136,126,130],
[120,0,124,121,121,124,126,118,134,109,132],
[126,127,0,137,134,124,128,139,138,130,132],
[124,130,114,0,125,120,112,126,128,112,123],
[130,130,117,126,0,127,118,124,134,123,134],
[125,127,127,131,124,0,125,119,126,125,122],
[131,125,123,139,133,126,0,137,138,127,132],
[128,133,112,125,127,132,114,0,138,121,124],
[115,117,113,123,117,125,113,113,0,119,110],
[125,142,121,139,128,126,124,130,132,0,133],
[121,119,119,128,117,129,119,127,141,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,139,146,131,125,140,133,136,128,130,125],
[112,0,124,129,115,123,127,123,123,107,128],
[105,127,0,119,124,132,124,126,116,125,121],
[120,122,132,0,120,134,124,124,126,119,129],
[126,136,127,131,0,133,128,129,128,114,124],
[111,128,119,117,118,0,123,123,118,115,123],
[118,124,127,127,123,128,0,136,131,116,131],
[115,128,125,127,122,128,115,0,122,117,117],
[123,128,135,125,123,133,120,129,0,112,130],
[121,144,126,132,137,136,135,134,139,0,134],
[126,123,130,122,127,128,120,134,121,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,129,127,122,113,131,115,124,120,118],
[130,0,148,134,127,128,140,130,122,133,123],
[122,103,0,120,119,117,127,100,111,128,118],
[124,117,131,0,117,123,131,119,118,139,129],
[129,124,132,134,0,129,138,115,115,132,125],
[138,123,134,128,122,0,148,118,126,130,129],
[120,111,124,120,113,103,0,111,105,122,125],
[136,121,151,132,136,133,140,0,124,139,120],
[127,129,140,133,136,125,146,127,0,137,133],
[131,118,123,112,119,121,129,112,114,0,114],
[133,128,133,122,126,122,126,131,118,137,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,143,158,132,115,127,139,142,129,127,130],
[108,0,139,129,117,122,142,135,110,115,119],
[93,112,0,106,96,107,115,112,78,96,102],
[119,122,145,0,118,113,137,146,101,105,126],
[136,134,155,133,0,122,141,151,119,129,135],
[124,129,144,138,129,0,141,150,125,120,125],
[112,109,136,114,110,110,0,146,104,109,114],
[109,116,139,105,100,101,105,0,88,90,110],
[122,141,173,150,132,126,147,163,0,129,139],
[124,136,155,146,122,131,142,161,122,0,161],
[121,132,149,125,116,126,137,141,112,90,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,129,127,131,112,137,127,133,126,124,121],
[122,0,132,133,122,130,123,117,122,128,114],
[124,119,0,131,118,137,130,128,122,129,116],
[120,118,120,0,116,139,122,122,117,117,112],
[139,129,133,135,0,148,142,125,133,136,130],
[114,121,114,112,103,0,118,115,119,110,117],
[124,128,121,129,109,133,0,117,118,128,124],
[118,134,123,129,126,136,134,0,121,139,128],
[125,129,129,134,118,132,133,130,0,131,126],
[127,123,122,134,115,141,123,112,120,0,117],
[130,137,135,139,121,134,127,123,125,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,103,125,119,129,137,134,140,122,136],
[131,0,119,121,123,126,120,135,119,126,132],
[148,132,0,141,124,143,123,141,152,150,151],
[126,130,110,0,139,122,132,120,149,139,156],
[132,128,127,112,0,131,123,137,145,136,139],
[122,125,108,129,120,0,97,128,117,135,144],
[114,131,128,119,128,154,0,125,139,138,144],
[117,116,110,131,114,123,126,0,141,118,127],
[111,132,99,102,106,134,112,110,0,118,126],
[129,125,101,112,115,116,113,133,133,0,136],
[115,119,100,95,112,107,107,124,125,115,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,120,139,133,108,137,126,143,118,175],
[130,0,132,143,137,129,133,122,136,143,172],
[131,119,0,118,139,113,129,108,118,114,164],
[112,108,133,0,136,97,138,115,137,124,156],
[118,114,112,115,0,108,111,129,141,133,178],
[143,122,138,154,143,0,140,127,144,134,172],
[114,118,122,113,140,111,0,119,139,130,155],
[125,129,143,136,122,124,132,0,143,120,161],
[108,115,133,114,110,107,112,108,0,117,157],
[133,108,137,127,118,117,121,131,134,0,146],
[76,79,87,95,73,79,96,90,94,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,131,144,130,123,133,137,136,125,129],
[126,0,125,140,124,118,131,128,127,131,124],
[120,126,0,137,124,128,133,134,122,127,112],
[107,111,114,0,118,123,122,118,111,116,112],
[121,127,127,133,0,123,139,131,132,124,124],
[128,133,123,128,128,0,137,137,131,121,123],
[118,120,118,129,112,114,0,128,124,119,118],
[114,123,117,133,120,114,123,0,121,116,119],
[115,124,129,140,119,120,127,130,0,122,123],
[126,120,124,135,127,130,132,135,129,0,128],
[122,127,139,139,127,128,133,132,128,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,122,131,140,125,131,130,137,109,135],
[129,0,132,126,144,138,114,127,133,119,128],
[129,119,0,127,122,118,114,123,123,125,123],
[120,125,124,0,126,115,115,124,128,115,111],
[111,107,129,125,0,121,112,103,115,116,126],
[126,113,133,136,130,0,129,138,139,136,129],
[120,137,137,136,139,122,0,121,136,124,124],
[121,124,128,127,148,113,130,0,134,119,140],
[114,118,128,123,136,112,115,117,0,118,117],
[142,132,126,136,135,115,127,132,133,0,130],
[116,123,128,140,125,122,127,111,134,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,112,127,110,116,125,120,118,122,128],
[128,0,123,123,123,127,129,130,118,129,130],
[139,128,0,131,129,129,131,134,137,120,133],
[124,128,120,0,115,123,127,121,117,122,124],
[141,128,122,136,0,129,127,136,132,131,138],
[135,124,122,128,122,0,131,133,130,131,127],
[126,122,120,124,124,120,0,120,118,117,123],
[131,121,117,130,115,118,131,0,131,119,127],
[133,133,114,134,119,121,133,120,0,120,118],
[129,122,131,129,120,120,134,132,131,0,131],
[123,121,118,127,113,124,128,124,133,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,133,135,132,130,121,128,122,123,139],
[131,0,141,124,129,137,122,116,124,125,149],
[118,110,0,127,124,130,114,115,119,122,136],
[116,127,124,0,131,125,127,118,115,114,139],
[119,122,127,120,0,135,128,113,118,129,145],
[121,114,121,126,116,0,114,117,119,116,138],
[130,129,137,124,123,137,0,117,132,129,141],
[123,135,136,133,138,134,134,0,125,122,150],
[129,127,132,136,133,132,119,126,0,130,147],
[128,126,129,137,122,135,122,129,121,0,147],
[112,102,115,112,106,113,110,101,104,104,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,185,136,125,116,148,184,119,145,144,171],
[66,0,103,88,79,104,125,96,63,149,115],
[115,148,0,146,99,119,145,134,108,133,161],
[126,163,105,0,88,82,150,115,69,107,102],
[135,172,152,163,0,207,148,190,114,180,204],
[103,147,132,169,44,0,139,169,108,111,201],
[67,126,106,101,103,112,0,67,45,81,117],
[132,155,117,136,61,82,184,0,95,128,107],
[106,188,143,182,137,143,206,156,0,129,187],
[107,102,118,144,71,140,170,123,122,0,165],
[80,136,90,149,47,50,134,144,64,86,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,114,137,116,126,127,120,118,118,110,130],
[137,0,140,132,130,136,133,141,145,126,119],
[114,111,0,111,123,124,114,121,120,113,124],
[135,119,140,0,133,146,129,139,131,139,129],
[125,121,128,118,0,127,127,116,128,111,125],
[124,115,127,105,124,0,111,116,117,111,119],
[131,118,137,122,124,140,0,131,131,118,125],
[133,110,130,112,135,135,120,0,131,106,115],
[133,106,131,120,123,134,120,120,0,110,111],
[141,125,138,112,140,140,133,145,141,0,135],
[121,132,127,122,126,132,126,136,140,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,145,126,123,125,114,119,134,128,128,133],
[106,0,125,131,122,111,119,132,137,119,124],
[125,126,0,124,119,111,123,128,133,130,130],
[128,120,127,0,122,126,122,136,120,131,129],
[126,129,132,129,0,131,142,142,141,135,125],
[137,140,140,125,120,0,126,139,132,132,127],
[132,132,128,129,109,125,0,139,126,133,123],
[117,119,123,115,109,112,112,0,126,110,117],
[123,114,118,131,110,119,125,125,0,125,120],
[123,132,121,120,116,119,118,141,126,0,116],
[118,127,121,122,126,124,128,134,131,135,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,123,130,113,126,131,130,116,133,118],
[140,0,137,135,129,135,126,135,132,133,120],
[128,114,0,125,120,117,120,129,121,127,103],
[121,116,126,0,128,130,128,129,121,130,117],
[138,122,131,123,0,132,122,129,133,129,129],
[125,116,134,121,119,0,124,125,124,128,122],
[120,125,131,123,129,127,0,144,132,119,129],
[121,116,122,122,122,126,107,0,119,139,114],
[135,119,130,130,118,127,119,132,0,132,121],
[118,118,124,121,122,123,132,112,119,0,102],
[133,131,148,134,122,129,122,137,130,149,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,105,101,107,91,95,110,114,109,107,112],
[146,0,134,125,113,120,109,127,150,137,120],
[150,117,0,139,127,129,122,149,127,146,146],
[144,126,112,0,115,103,130,126,131,142,116],
[160,138,124,136,0,119,123,128,151,147,114],
[156,131,122,148,132,0,126,139,133,142,135],
[141,142,129,121,128,125,0,134,138,143,121],
[137,124,102,125,123,112,117,0,115,136,121],
[142,101,124,120,100,118,113,136,0,132,112],
[144,114,105,109,104,109,108,115,119,0,111],
[139,131,105,135,137,116,130,130,139,140,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,102,93,112,134,113,105,111,95,119,106],
[149,0,137,141,147,137,122,139,123,147,147],
[158,114,0,154,136,130,153,124,126,144,129],
[139,110,97,0,124,114,125,116,111,121,115],
[117,104,115,127,0,121,111,114,93,128,121],
[138,114,121,137,130,0,141,134,122,137,139],
[146,129,98,126,140,110,0,126,105,147,116],
[140,112,127,135,137,117,125,0,112,142,119],
[156,128,125,140,158,129,146,139,0,152,139],
[132,104,107,130,123,114,104,109,99,0,109],
[145,104,122,136,130,112,135,132,112,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,131,117,117,127,126,126,113,125,119],
[119,0,126,106,116,122,120,109,110,112,119],
[120,125,0,109,117,121,119,118,117,119,118],
[134,145,142,0,119,128,129,140,124,138,129],
[134,135,134,132,0,136,116,134,127,128,116],
[124,129,130,123,115,0,105,120,110,121,112],
[125,131,132,122,135,146,0,127,134,132,126],
[125,142,133,111,117,131,124,0,118,126,138],
[138,141,134,127,124,141,117,133,0,128,123],
[126,139,132,113,123,130,119,125,123,0,120],
[132,132,133,122,135,139,125,113,128,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,130,120,132,134,125,134,126,130,117],
[121,0,118,129,122,126,123,128,113,121,114],
[121,133,0,114,123,123,124,124,111,125,110],
[131,122,137,0,133,121,127,125,125,134,113],
[119,129,128,118,0,129,118,123,112,123,114],
[117,125,128,130,122,0,126,122,124,128,115],
[126,128,127,124,133,125,0,127,119,119,117],
[117,123,127,126,128,129,124,0,117,129,108],
[125,138,140,126,139,127,132,134,0,138,120],
[121,130,126,117,128,123,132,122,113,0,130],
[134,137,141,138,137,136,134,143,131,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,110,126,127,131,110,95,131,109,134,127],
[141,0,139,147,148,126,106,131,126,126,128],
[125,112,0,145,114,121,136,136,118,145,141],
[124,104,106,0,126,127,112,124,125,126,141],
[120,103,137,125,0,122,97,126,126,119,132],
[141,125,130,124,129,0,111,127,135,143,124],
[156,145,115,139,154,140,0,159,135,152,152],
[120,120,115,127,125,124,92,0,96,129,124],
[142,125,133,126,125,116,116,155,0,133,147],
[117,125,106,125,132,108,99,122,118,0,127],
[124,123,110,110,119,127,99,127,104,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,151,158,87,145,143,154,107,150,162,185],
[100,0,124,79,98,86,144,97,136,120,124],
[93,127,0,79,84,72,97,104,115,119,109],
[164,172,172,0,206,141,153,122,147,166,143],
[106,153,167,45,0,107,138,115,150,148,140],
[108,165,179,110,144,0,153,133,202,152,159],
[97,107,154,98,113,98,0,121,112,119,123],
[144,154,147,129,136,118,130,0,173,142,143],
[101,115,136,104,101,49,139,78,0,107,104],
[89,131,132,85,103,99,132,109,144,0,130],
[66,127,142,108,111,92,128,108,147,121,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,118,126,106,112,114,130,109,110,110,123],
[133,0,128,108,105,118,132,122,125,110,142],
[125,123,0,119,107,132,138,121,124,119,134],
[145,143,132,0,122,144,135,132,131,131,142],
[139,146,144,129,0,139,142,150,144,123,140],
[137,133,119,107,112,0,137,134,137,109,125],
[121,119,113,116,109,114,0,120,111,119,129],
[142,129,130,119,101,117,131,0,125,111,124],
[141,126,127,120,107,114,140,126,0,105,134],
[141,141,132,120,128,142,132,140,146,0,127],
[128,109,117,109,111,126,122,127,117,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,109,143,128,145,159,121,146,134,156,137],
[142,0,180,148,160,142,134,135,133,154,124],
[108,71,0,125,120,98,97,84,109,115,102],
[123,103,126,0,106,111,92,124,120,121,117],
[106,91,131,145,0,106,74,115,123,121,118],
[92,109,153,140,145,0,114,116,132,167,108],
[130,117,154,159,177,137,0,149,146,185,152],
[105,116,167,127,136,135,102,0,122,150,131],
[117,118,142,131,128,119,105,129,0,146,128],
[95,97,136,130,130,84,66,101,105,0,101],
[114,127,149,134,133,143,99,120,123,150,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,169,111,162,129,161,118,117,142,125,124],
[82,0,107,127,93,143,113,117,133,123,119],
[140,144,0,159,132,153,110,130,140,146,151],
[89,124,92,0,85,138,107,88,107,121,87],
[122,158,119,166,0,124,148,140,151,153,140],
[90,108,98,113,127,0,105,130,153,143,122],
[133,138,141,144,103,146,0,137,141,153,138],
[134,134,121,163,111,121,114,0,149,158,118],
[109,118,111,144,100,98,110,102,0,116,109],
[126,128,105,130,98,108,98,93,135,0,100],
[127,132,100,164,111,129,113,133,142,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,115,159,129,110,136,116,160,111,146],
[129,0,109,122,138,141,122,142,174,104,111],
[136,142,0,162,121,145,150,152,166,142,115],
[92,129,89,0,99,97,87,110,147,122,108],
[122,113,130,152,0,139,133,127,180,118,110],
[141,110,106,154,112,0,109,122,170,115,109],
[115,129,101,164,118,142,0,135,160,125,130],
[135,109,99,141,124,129,116,0,138,117,128],
[91,77,85,104,71,81,91,113,0,97,81],
[140,147,109,129,133,136,126,134,154,0,132],
[105,140,136,143,141,142,121,123,170,119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,121,118,126,115,123,99,107,109,113,143],
[130,0,112,141,119,106,132,115,123,126,120],
[133,139,0,130,106,121,120,109,125,107,137],
[125,110,121,0,104,103,96,112,105,112,118],
[136,132,145,147,0,128,118,115,121,125,136],
[128,145,130,148,123,0,113,129,125,125,155],
[152,119,131,155,133,138,0,124,107,134,155],
[144,136,142,139,136,122,127,0,127,143,148],
[142,128,126,146,130,126,144,124,0,131,143],
[138,125,144,139,126,126,117,108,120,0,139],
[108,131,114,133,115,96,96,103,108,112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,137,117,113,107,107,115,118,112,125],
[132,0,143,119,127,114,114,119,133,110,125],
[114,108,0,119,132,114,120,106,125,110,124],
[134,132,132,0,132,130,128,127,145,121,141],
[138,124,119,119,0,118,129,120,136,105,129],
[144,137,137,121,133,0,125,134,133,118,139],
[144,137,131,123,122,126,0,134,144,125,137],
[136,132,145,124,131,117,117,0,126,135,135],
[133,118,126,106,115,118,107,125,0,111,128],
[139,141,141,130,146,133,126,116,140,0,131],
[126,126,127,110,122,112,114,116,123,120,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,127,123,123,125,127,115,132,119,126,113],
[124,0,117,132,125,119,121,128,118,125,118],
[128,134,0,129,125,136,127,127,122,118,117],
[128,119,122,0,125,130,123,136,125,130,120],
[126,126,126,126,0,121,114,133,112,122,128],
[124,132,115,121,130,0,123,132,115,126,122],
[136,130,124,128,137,128,0,134,121,138,121],
[119,123,124,115,118,119,117,0,113,123,117],
[132,133,129,126,139,136,130,138,0,125,130],
[125,126,133,121,129,125,113,128,126,0,119],
[138,133,134,131,123,129,130,134,121,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,130,114,136,124,135,141,145,135,133],
[115,0,127,125,125,131,115,131,133,121,124],
[121,124,0,118,114,124,129,127,138,123,139],
[137,126,133,0,125,122,129,126,125,132,141],
[115,126,137,126,0,137,129,139,142,122,133],
[127,120,127,129,114,0,116,127,133,119,134],
[116,136,122,122,122,135,0,132,138,116,136],
[110,120,124,125,112,124,119,0,130,113,130],
[106,118,113,126,109,118,113,121,0,116,131],
[116,130,128,119,129,132,135,138,135,0,140],
[118,127,112,110,118,117,115,121,120,111,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,122,116,123,117,133,123,127,117,113,126],
[129,0,116,115,116,128,127,125,137,124,119],
[135,135,0,123,132,123,134,131,144,125,131],
[128,136,128,0,127,134,138,123,134,132,137],
[134,135,119,124,0,132,136,119,140,128,132],
[118,123,128,117,119,0,130,114,130,110,122],
[128,124,117,113,115,121,0,119,130,127,129],
[124,126,120,128,132,137,132,0,137,122,138],
[134,114,107,117,111,121,121,114,0,114,127],
[138,127,126,119,123,141,124,129,137,0,145],
[125,132,120,114,119,129,122,113,124,106,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,123,114,117,106,137,132,121,117,117,120],
[128,0,127,137,124,147,145,130,128,136,129],
[137,124,0,138,134,145,148,137,136,126,134],
[134,114,113,0,118,125,135,113,110,119,123],
[145,127,117,133,0,141,132,128,130,137,130],
[114,104,106,126,110,0,124,110,110,108,128],
[119,106,103,116,119,127,0,119,117,114,106],
[130,121,114,138,123,141,132,0,133,122,122],
[134,123,115,141,121,141,134,118,0,117,134],
[134,115,125,132,114,143,137,129,134,0,128],
[131,122,117,128,121,123,145,129,117,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,127,132,126,137,128,131,117,130,142],
[116,0,112,115,115,124,122,123,118,115,121],
[124,139,0,129,130,131,135,143,126,131,136],
[119,136,122,0,133,128,141,131,134,142,136],
[125,136,121,118,0,124,128,132,122,130,131],
[114,127,120,123,127,0,136,126,125,119,127],
[123,129,116,110,123,115,0,126,127,126,132],
[120,128,108,120,119,125,125,0,111,128,128],
[134,133,125,117,129,126,124,140,0,134,136],
[121,136,120,109,121,132,125,123,117,0,128],
[109,130,115,115,120,124,119,123,115,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,144,133,119,137,137,141,131,122,137],
[116,0,123,133,126,128,133,123,121,121,126],
[107,128,0,115,112,111,120,120,116,116,124],
[118,118,136,0,109,124,121,118,119,113,122],
[132,125,139,142,0,143,143,138,136,135,139],
[114,123,140,127,108,0,125,128,128,116,135],
[114,118,131,130,108,126,0,116,118,123,122],
[110,128,131,133,113,123,135,0,114,126,124],
[120,130,135,132,115,123,133,137,0,123,129],
[129,130,135,138,116,135,128,125,128,0,126],
[114,125,127,129,112,116,129,127,122,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,138,138,127,139,139,125,122,122,128,113],
[113,0,146,116,115,105,117,107,101,146,108],
[113,105,0,107,127,92,114,101,100,117,111],
[124,135,144,0,123,133,112,97,124,118,115],
[112,136,124,128,0,115,139,96,113,122,119],
[112,146,159,118,136,0,120,118,113,139,139],
[126,134,137,139,112,131,0,94,132,136,113],
[129,144,150,154,155,133,157,0,119,150,102],
[129,150,151,127,138,138,119,132,0,137,154],
[123,105,134,133,129,112,115,101,114,0,106],
[138,143,140,136,132,112,138,149,97,145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,144,116,127,117,115,121,125,123,123,122],
[107,0,122,134,112,112,118,117,115,120,120],
[135,129,0,137,126,134,128,124,133,136,126],
[124,117,114,0,113,110,113,98,112,110,106],
[134,139,125,138,0,129,138,135,119,130,123],
[136,139,117,141,122,0,119,114,116,129,112],
[130,133,123,138,113,132,0,102,124,128,126],
[126,134,127,153,116,137,149,0,140,146,133],
[128,136,118,139,132,135,127,111,0,112,131],
[128,131,115,141,121,122,123,105,139,0,126],
[129,131,125,145,128,139,125,118,120,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,142,125,126,125,144,110,107,128,113,130],
[109,0,105,99,112,115,94,97,105,100,109],
[126,146,0,120,129,134,124,113,127,106,136],
[125,152,131,0,117,129,125,122,128,112,131],
[126,139,122,134,0,127,117,121,128,119,137],
[107,136,117,122,124,0,124,108,118,111,135],
[141,157,127,126,134,127,0,125,133,114,130],
[144,154,138,129,130,143,126,0,125,126,150],
[123,146,124,123,123,133,118,126,0,125,128],
[138,151,145,139,132,140,137,125,126,0,138],
[121,142,115,120,114,116,121,101,123,113,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,91,117,87,117,96,80,75,88,125,107],
[160,0,113,114,126,142,118,85,133,93,139],
[134,138,0,102,116,122,104,99,132,106,163],
[164,137,149,0,107,110,111,149,129,106,143],
[134,125,135,144,0,113,97,125,156,103,146],
[155,109,129,141,138,0,114,130,143,113,165],
[171,133,147,140,154,137,0,92,172,156,174],
[176,166,152,102,126,121,159,0,127,128,160],
[163,118,119,122,95,108,79,124,0,116,125],
[126,158,145,145,148,138,95,123,135,0,166],
[144,112,88,108,105,86,77,91,126,85,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,136,129,118,117,115,129,129,120,118],
[138,0,114,119,124,110,130,126,118,119,117],
[115,137,0,136,139,135,145,125,121,131,131],
[122,132,115,0,130,129,137,123,129,135,128],
[133,127,112,121,0,117,128,121,126,123,111],
[134,141,116,122,134,0,134,118,124,118,114],
[136,121,106,114,123,117,0,119,124,121,128],
[122,125,126,128,130,133,132,0,128,117,120],
[122,133,130,122,125,127,127,123,0,123,123],
[131,132,120,116,128,133,130,134,128,0,119],
[133,134,120,123,140,137,123,131,128,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,111,119,117,126,121,121,122,136,125],
[115,0,114,109,123,122,118,116,110,122,110],
[140,137,0,129,139,125,121,125,118,138,127],
[132,142,122,0,132,128,130,119,125,134,139],
[134,128,112,119,0,124,110,119,126,120,116],
[125,129,126,123,127,0,125,128,130,133,117],
[130,133,130,121,141,126,0,120,137,126,130],
[130,135,126,132,132,123,131,0,125,131,122],
[129,141,133,126,125,121,114,126,0,131,118],
[115,129,113,117,131,118,125,120,120,0,117],
[126,141,124,112,135,134,121,129,133,134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,133,121,109,117,124,140,115,118,166,152],
[118,0,134,106,127,149,147,94,139,150,164],
[130,117,0,149,131,152,142,108,134,163,145],
[142,145,102,0,125,134,152,121,128,149,140],
[134,124,120,126,0,150,140,126,131,158,168],
[127,102,99,117,101,0,121,101,104,127,128],
[111,104,109,99,111,130,0,95,114,114,149],
[136,157,143,130,125,150,156,0,130,167,158],
[133,112,117,123,120,147,137,121,0,142,137],
[85,101,88,102,93,124,137,84,109,0,119],
[99,87,106,111,83,123,102,93,114,132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,125,127,130,135,114,129,129,123,138,142],
[126,0,140,126,141,134,141,138,121,127,132],
[124,111,0,128,116,120,133,129,112,124,105],
[121,125,123,0,134,123,130,136,106,129,121],
[116,110,135,117,0,133,120,130,113,121,118],
[137,117,131,128,118,0,120,131,117,132,137],
[122,110,118,121,131,131,0,134,113,121,129],
[122,113,122,115,121,120,117,0,123,128,114],
[128,130,139,145,138,134,138,128,0,141,124],
[113,124,127,122,130,119,130,123,110,0,123],
[109,119,146,130,133,114,122,137,127,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,135,107,129,119,119,135,126,100,132,123],
[116,0,128,116,130,114,117,104,130,123,109],
[144,123,0,133,126,111,123,119,131,130,118],
[122,135,118,0,141,130,118,128,120,138,119],
[132,121,125,110,0,119,112,129,116,138,115],
[132,137,140,121,132,0,124,122,134,150,137],
[116,134,128,133,139,127,0,114,121,127,112],
[125,147,132,123,122,129,137,0,138,129,126],
[151,121,120,131,135,117,130,113,0,142,120],
[119,128,121,113,113,101,124,122,109,0,113],
[128,142,133,132,136,114,139,125,131,138,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,132,124,116,106,120,111,116,116,116,127],
[119,0,132,114,111,116,129,113,137,118,125],
[127,119,0,118,110,119,126,112,117,115,131],
[135,137,133,0,118,114,133,119,134,112,128],
[145,140,141,133,0,130,147,141,147,125,136],
[131,135,132,137,121,0,144,141,136,146,156],
[140,122,125,118,104,107,0,113,132,108,126],
[135,138,139,132,110,110,138,0,139,119,131],
[135,114,134,117,104,115,119,112,0,126,112],
[135,133,136,139,126,105,143,132,125,0,133],
[124,126,120,123,115,95,125,120,139,118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,139,128,130,144,114,136,112,120,115],
[132,0,127,127,134,139,122,138,117,117,110],
[112,124,0,120,130,139,114,128,95,118,118],
[123,124,131,0,134,134,123,134,113,114,113],
[121,117,121,117,0,131,117,113,100,110,98],
[107,112,112,117,120,0,117,112,92,108,111],
[137,129,137,128,134,134,0,130,120,106,115],
[115,113,123,117,138,139,121,0,104,112,113],
[139,134,156,138,151,159,131,147,0,119,138],
[131,134,133,137,141,143,145,139,132,0,124],
[136,141,133,138,153,140,136,138,113,127,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,111,102,127,99,121,114,103,162,94,127],
[140,0,127,147,158,137,157,103,160,118,157],
[149,124,0,158,124,145,129,131,149,120,162],
[124,104,93,0,108,125,124,106,129,95,150],
[152,93,127,143,0,138,129,118,141,133,162],
[130,114,106,126,113,0,123,104,151,137,143],
[137,94,122,127,122,128,0,98,143,107,127],
[148,148,120,145,133,147,153,0,173,143,158],
[89,91,102,122,110,100,108,78,0,86,103],
[157,133,131,156,118,114,144,108,165,0,146],
[124,94,89,101,89,108,124,93,148,105,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,119,112,133,135,112,124,116,118,127,128],
[132,0,120,145,151,118,134,125,117,139,134],
[139,131,0,150,142,128,126,132,109,125,126],
[118,106,101,0,131,107,124,113,105,119,99],
[116,100,109,120,0,114,107,102,103,126,118],
[139,133,123,144,137,0,139,123,115,140,142],
[127,117,125,127,144,112,0,119,129,121,122],
[135,126,119,138,149,128,132,0,123,134,131],
[133,134,142,146,148,136,122,128,0,143,133],
[124,112,126,132,125,111,130,117,108,0,126],
[123,117,125,152,133,109,129,120,118,125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,124,113,108,119,133,120,123,121,130,123],
[127,0,124,120,132,137,112,133,128,134,115],
[138,127,0,122,130,137,116,127,114,137,123],
[143,131,129,0,132,140,128,120,116,139,132],
[132,119,121,119,0,131,119,123,113,132,125],
[118,114,114,111,120,0,109,120,101,132,118],
[131,139,135,123,132,142,0,124,119,142,133],
[128,118,124,131,128,131,127,0,122,135,120],
[130,123,137,135,138,150,132,129,0,143,132],
[121,117,114,112,119,119,109,116,108,0,122],
[128,136,128,119,126,133,118,131,119,129,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,178,145,152,160,137,127,117,172,146,201],
[73,0,161,108,98,123,147,115,110,83,132],
[106,90,0,123,147,114,96,82,128,72,157],
[99,143,128,0,141,122,155,93,118,103,149],
[91,153,104,110,0,110,153,93,107,85,122],
[114,128,137,129,141,0,133,94,141,112,146],
[124,104,155,96,98,118,0,95,98,115,169],
[134,136,169,158,158,157,156,0,152,123,184],
[79,141,123,133,144,110,153,99,0,70,169],
[105,168,179,148,166,139,136,128,181,0,214],
[50,119,94,102,129,105,82,67,82,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,112,140,137,121,113,126,143,124,138],
[121,0,108,128,135,127,116,117,138,116,124],
[139,143,0,140,139,136,120,123,154,123,120],
[111,123,111,0,123,107,110,116,125,113,100],
[114,116,112,128,0,116,116,114,126,119,118],
[130,124,115,144,135,0,119,117,138,120,132],
[138,135,131,141,135,132,0,123,143,134,135],
[125,134,128,135,137,134,128,0,140,139,129],
[108,113,97,126,125,113,108,111,0,120,121],
[127,135,128,138,132,131,117,112,131,0,129],
[113,127,131,151,133,119,116,122,130,122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,120,129,134,119,120,117,135,126,124,120],
[131,0,130,150,135,130,141,133,123,124,125],
[122,121,0,139,131,127,114,129,114,119,122],
[117,101,112,0,119,120,110,124,105,114,120],
[132,116,120,132,0,121,128,125,121,124,125],
[131,121,124,131,130,0,134,141,114,123,129],
[134,110,137,141,123,117,0,134,118,128,128],
[116,118,122,127,126,110,117,0,110,121,112],
[125,128,137,146,130,137,133,141,0,131,131],
[127,127,132,137,127,128,123,130,120,0,128],
[131,126,129,131,126,122,123,139,120,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,146,144,129,120,147,202,122,134,144,137],
[105,0,99,104,115,150,141,108,159,114,98],
[107,152,0,93,135,143,128,84,112,119,85],
[122,147,158,0,138,151,151,100,150,125,106],
[131,136,116,113,0,126,161,108,105,113,72],
[104,101,108,100,125,0,146,76,104,88,96],
[49,110,123,100,90,105,0,70,126,116,87],
[129,143,167,151,143,175,181,0,172,140,124],
[117,92,139,101,146,147,125,79,0,107,85],
[107,137,132,126,138,163,135,111,144,0,105],
[114,153,166,145,179,155,164,127,166,146,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,108,104,96,99,123,111,146,117,120],
[150,0,118,129,127,136,137,140,165,139,133],
[143,133,0,130,128,136,138,110,147,117,117],
[147,122,121,0,136,129,118,107,156,115,142],
[155,124,123,115,0,140,141,130,147,132,128],
[152,115,115,122,111,0,136,117,143,108,134],
[128,114,113,133,110,115,0,115,149,124,132],
[140,111,141,144,121,134,136,0,160,132,137],
[105,86,104,95,104,108,102,91,0,111,109],
[134,112,134,136,119,143,127,119,140,0,135],
[131,118,134,109,123,117,119,114,142,116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,141,128,152,121,138,124,113,120,135],
[117,0,158,121,126,129,122,159,124,121,123],
[110,93,0,114,96,102,99,109,100,79,121],
[123,130,137,0,124,130,114,133,122,123,132],
[99,125,155,127,0,118,131,134,134,107,129],
[130,122,149,121,133,0,138,129,106,102,128],
[113,129,152,137,120,113,0,117,107,122,116],
[127,92,142,118,117,122,134,0,109,126,104],
[138,127,151,129,117,145,144,142,0,103,142],
[131,130,172,128,144,149,129,125,148,0,141],
[116,128,130,119,122,123,135,147,109,110,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,99,117,112,119,98,100,117,115,108,95],
[152,0,149,123,124,139,121,127,152,126,116],
[134,102,0,110,107,101,121,100,120,95,111],
[139,128,141,0,107,125,114,110,127,111,105],
[132,127,144,144,0,122,131,127,139,129,123],
[153,112,150,126,129,0,135,146,130,140,128],
[151,130,130,137,120,116,0,100,154,115,136],
[134,124,151,141,124,105,151,0,148,144,129],
[136,99,131,124,112,121,97,103,0,97,107],
[143,125,156,140,122,111,136,107,154,0,128],
[156,135,140,146,128,123,115,122,144,123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,132,131,134,132,134,123,136,127,133],
[138,0,130,129,149,126,134,130,134,123,142],
[119,121,0,112,121,112,128,110,121,129,118],
[120,122,139,0,130,131,142,134,136,130,135],
[117,102,130,121,0,123,130,121,125,124,117],
[119,125,139,120,128,0,130,121,124,133,130],
[117,117,123,109,121,121,0,118,115,115,123],
[128,121,141,117,130,130,133,0,126,120,140],
[115,117,130,115,126,127,136,125,0,117,130],
[124,128,122,121,127,118,136,131,134,0,127],
[118,109,133,116,134,121,128,111,121,124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,117,120,116,123,122,117,128,125,126,125],
[134,0,137,129,140,128,124,144,133,127,129],
[131,114,0,137,121,124,116,134,125,123,122],
[135,122,114,0,129,122,128,131,130,126,128],
[128,111,130,122,0,110,109,127,126,121,118],
[129,123,127,129,141,0,124,134,122,129,130],
[134,127,135,123,142,127,0,144,140,130,138],
[123,107,117,120,124,117,107,0,114,109,116],
[126,118,126,121,125,129,111,137,0,123,116],
[125,124,128,125,130,122,121,142,128,0,123],
[126,122,129,123,133,121,113,135,135,128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,134,123,123,96,107,146,133,139,125],
[117,0,119,156,122,122,129,164,122,135,132],
[117,132,0,140,105,111,104,132,122,95,126],
[128,95,111,0,89,94,108,109,98,123,100],
[128,129,146,162,0,114,135,154,139,162,157],
[155,129,140,157,137,0,119,159,176,135,145],
[144,122,147,143,116,132,0,144,141,147,146],
[105,87,119,142,97,92,107,0,109,140,117],
[118,129,129,153,112,75,110,142,0,142,113],
[112,116,156,128,89,116,104,111,109,0,100],
[126,119,125,151,94,106,105,134,138,151,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,134,117,115,98,121,120,95,102,113,111],
[117,0,138,118,111,125,115,104,123,111,104],
[134,113,0,133,114,122,128,114,119,121,127],
[136,133,118,0,122,126,126,126,112,122,125],
[153,140,137,129,0,139,125,132,141,140,141],
[130,126,129,125,112,0,113,110,119,131,128],
[131,136,123,125,126,138,0,92,122,131,110],
[156,147,137,125,119,141,159,0,134,125,142],
[149,128,132,139,110,132,129,117,0,128,118],
[138,140,130,129,111,120,120,126,123,0,120],
[140,147,124,126,110,123,141,109,133,131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,150,119,107,124,103,118,130,126,146,117],
[101,0,111,100,111,104,109,117,127,130,120],
[132,140,0,113,113,98,122,131,110,130,115],
[144,151,138,0,141,130,139,135,137,128,125],
[127,140,138,110,0,128,122,139,135,157,133],
[148,147,153,121,123,0,131,142,140,142,130],
[133,142,129,112,129,120,0,124,135,135,115],
[121,134,120,116,112,109,127,0,122,129,120],
[125,124,141,114,116,111,116,129,0,145,127],
[105,121,121,123,94,109,116,122,106,0,99],
[134,131,136,126,118,121,136,131,124,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,140,125,145,129,158,140,148,125,136,146],
[111,0,137,138,117,149,127,130,110,129,121],
[126,114,0,148,140,134,152,153,112,129,111],
[106,113,103,0,126,128,129,135,101,113,124],
[122,134,111,125,0,142,138,137,120,119,110],
[93,102,117,123,109,0,125,122,109,116,115],
[111,124,99,122,113,126,0,113,106,116,98],
[103,121,98,116,114,129,138,0,104,105,105],
[126,141,139,150,131,142,145,147,0,129,120],
[115,122,122,138,132,135,135,146,122,0,112],
[105,130,140,127,141,136,153,146,131,139,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,126,130,140,130,134,133,130,125,134,133],
[125,0,142,135,138,141,137,140,133,129,139],
[121,109,0,130,121,119,128,134,125,117,129],
[111,116,121,0,130,124,130,122,119,106,127],
[121,113,130,121,0,132,133,137,121,114,124],
[117,110,132,127,119,0,127,135,118,121,127],
[118,114,123,121,118,124,0,124,121,118,134],
[121,111,117,129,114,116,127,0,123,118,133],
[126,118,126,132,130,133,130,128,0,121,147],
[117,122,134,145,137,130,133,133,130,0,134],
[118,112,122,124,127,124,117,118,104,117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 251, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_11_251.csv", index=False, header=False)