
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,267,271,264,268,237,240,247,248,252,250],
[234,0,251,244,236,236,244,251,242,235,232],
[230,250,0,237,237,229,236,217,235,242,226],
[237,257,264,0,269,258,246,261,264,257,264],
[233,265,264,232,0,220,241,250,236,252,231],
[264,265,272,243,281,0,254,258,264,270,251],
[261,257,265,255,260,247,0,250,256,254,250],
[254,250,284,240,251,243,251,0,255,251,248],
[253,259,266,237,265,237,245,246,0,253,241],
[249,266,259,244,249,231,247,250,248,0,252],
[251,269,275,237,270,250,251,253,260,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,266,279,271,277,226,257,263,271,260],
[233,0,250,225,253,233,215,225,243,264,189],
[235,251,0,248,255,232,252,225,242,277,240],
[222,276,253,0,277,259,207,273,262,257,214],
[230,248,246,224,0,260,212,226,226,223,211],
[224,268,269,242,241,0,229,253,268,258,258],
[275,286,249,294,289,272,0,269,272,274,262],
[244,276,276,228,275,248,232,0,255,259,235],
[238,258,259,239,275,233,229,246,0,252,236],
[230,237,224,244,278,243,227,242,249,0,229],
[241,312,261,287,290,243,239,266,265,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,257,227,237,229,217,245,244,248,223],
[283,0,293,257,286,269,271,272,266,257,248],
[244,208,0,226,226,230,244,263,238,238,227],
[274,244,275,0,256,245,255,274,251,251,251],
[264,215,275,245,0,234,244,229,229,244,225],
[272,232,271,256,267,0,254,265,263,243,243],
[284,230,257,246,257,247,0,260,266,258,240],
[256,229,238,227,272,236,241,0,234,257,232],
[257,235,263,250,272,238,235,267,0,242,236],
[253,244,263,250,257,258,243,244,259,0,255],
[278,253,274,250,276,258,261,269,265,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,275,267,235,214,276,253,257,265,272],
[225,0,233,255,209,211,219,215,208,237,225],
[226,268,0,261,235,219,247,227,220,231,275],
[234,246,240,0,229,250,243,225,232,274,251],
[266,292,266,272,0,269,284,260,245,268,265],
[287,290,282,251,232,0,269,243,275,265,255],
[225,282,254,258,217,232,0,259,262,245,254],
[248,286,274,276,241,258,242,0,267,266,278],
[244,293,281,269,256,226,239,234,0,265,269],
[236,264,270,227,233,236,256,235,236,0,249],
[229,276,226,250,236,246,247,223,232,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,240,228,243,237,222,251,226,238,255],
[259,0,248,241,253,265,232,261,255,237,254],
[261,253,0,235,260,250,229,243,239,246,234],
[273,260,266,0,268,252,253,266,260,243,256],
[258,248,241,233,0,250,234,256,245,236,236],
[264,236,251,249,251,0,234,244,248,241,232],
[279,269,272,248,267,267,0,273,267,262,263],
[250,240,258,235,245,257,228,0,251,233,237],
[275,246,262,241,256,253,234,250,0,253,254],
[263,264,255,258,265,260,239,268,248,0,234],
[246,247,267,245,265,269,238,264,247,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,266,241,251,269,259,265,253,233,253],
[235,0,258,224,223,275,233,221,247,208,245],
[235,243,0,238,246,300,223,245,252,255,259],
[260,277,263,0,253,270,261,231,263,240,262],
[250,278,255,248,0,297,249,275,263,250,274],
[232,226,201,231,204,0,225,239,221,203,232],
[242,268,278,240,252,276,0,259,265,245,262],
[236,280,256,270,226,262,242,0,252,253,283],
[248,254,249,238,238,280,236,249,0,252,272],
[268,293,246,261,251,298,256,248,249,0,274],
[248,256,242,239,227,269,239,218,229,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,251,265,265,266,265,254,244,249,257],
[245,0,236,252,254,262,243,254,236,247,248],
[250,265,0,274,257,265,282,255,259,259,261],
[236,249,227,0,251,259,252,232,239,228,243],
[236,247,244,250,0,256,235,244,233,236,239],
[235,239,236,242,245,0,248,241,234,243,234],
[236,258,219,249,266,253,0,260,234,244,260],
[247,247,246,269,257,260,241,0,250,248,250],
[257,265,242,262,268,267,267,251,0,258,264],
[252,254,242,273,265,258,257,253,243,0,246],
[244,253,240,258,262,267,241,251,237,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,230,241,227,216,238,228,233,220,214],
[276,0,249,267,243,271,252,245,254,253,256],
[271,252,0,254,235,249,229,241,254,244,233],
[260,234,247,0,204,225,226,226,233,217,213],
[274,258,266,297,0,240,242,259,266,241,265],
[285,230,252,276,261,0,230,266,262,245,247],
[263,249,272,275,259,271,0,243,251,252,252],
[273,256,260,275,242,235,258,0,236,258,245],
[268,247,247,268,235,239,250,265,0,229,252],
[281,248,257,284,260,256,249,243,272,0,242],
[287,245,268,288,236,254,249,256,249,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,228,241,223,245,237,218,216,226,246],
[260,0,233,242,214,246,243,225,239,258,259],
[273,268,0,254,243,278,243,253,253,268,267],
[260,259,247,0,238,246,239,255,230,260,272],
[278,287,258,263,0,250,247,249,247,250,278],
[256,255,223,255,251,0,231,222,243,238,252],
[264,258,258,262,254,270,0,250,251,270,265],
[283,276,248,246,252,279,251,0,247,261,282],
[285,262,248,271,254,258,250,254,0,241,279],
[275,243,233,241,251,263,231,240,260,0,254],
[255,242,234,229,223,249,236,219,222,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,262,275,280,242,235,271,258,248,254],
[267,0,261,258,293,250,249,284,265,260,285],
[239,240,0,261,271,227,263,255,259,260,259],
[226,243,240,0,274,216,211,253,236,253,241],
[221,208,230,227,0,216,191,231,233,233,225],
[259,251,274,285,285,0,242,268,263,258,263],
[266,252,238,290,310,259,0,269,277,262,281],
[230,217,246,248,270,233,232,0,241,231,256],
[243,236,242,265,268,238,224,260,0,254,269],
[253,241,241,248,268,243,239,270,247,0,246],
[247,216,242,260,276,238,220,245,232,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,283,239,315,253,250,261,259,279,252,224],
[218,0,221,227,205,230,198,192,228,207,193],
[262,280,0,295,218,267,231,241,245,259,233],
[186,274,206,0,227,225,199,195,225,204,202],
[248,296,283,274,0,294,246,252,266,256,207],
[251,271,234,276,207,0,229,250,249,248,193],
[240,303,270,302,255,272,0,260,274,268,245],
[242,309,260,306,249,251,241,0,278,269,256],
[222,273,256,276,235,252,227,223,0,256,212],
[249,294,242,297,245,253,233,232,245,0,227],
[277,308,268,299,294,308,256,245,289,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,276,261,292,286,280,240,266,267,290],
[249,0,251,234,264,285,265,246,221,244,276],
[225,250,0,235,306,277,268,284,268,236,302],
[240,267,266,0,300,290,285,273,261,204,308],
[209,237,195,201,0,265,201,234,214,202,254],
[215,216,224,211,236,0,232,216,243,224,279],
[221,236,233,216,300,269,0,282,261,209,295],
[261,255,217,228,267,285,219,0,261,242,257],
[235,280,233,240,287,258,240,240,0,220,304],
[234,257,265,297,299,277,292,259,281,0,297],
[211,225,199,193,247,222,206,244,197,204,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,302,271,253,268,266,249,263,261,273],
[253,0,280,264,272,245,265,256,276,255,286],
[199,221,0,244,244,228,229,232,230,229,241],
[230,237,257,0,266,250,236,272,261,244,269],
[248,229,257,235,0,230,247,257,258,253,235],
[233,256,273,251,271,0,261,274,275,270,268],
[235,236,272,265,254,240,0,256,262,240,261],
[252,245,269,229,244,227,245,0,248,232,267],
[238,225,271,240,243,226,239,253,0,219,262],
[240,246,272,257,248,231,261,269,282,0,272],
[228,215,260,232,266,233,240,234,239,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,242,245,239,249,254,258,243,235,252],
[275,0,253,256,259,248,260,273,275,252,257],
[259,248,0,269,252,262,271,243,269,246,255],
[256,245,232,0,247,261,248,250,269,226,243],
[262,242,249,254,0,263,264,260,261,251,259],
[252,253,239,240,238,0,251,251,239,226,251],
[247,241,230,253,237,250,0,238,258,235,242],
[243,228,258,251,241,250,263,0,257,250,259],
[258,226,232,232,240,262,243,244,0,221,245],
[266,249,255,275,250,275,266,251,280,0,271],
[249,244,246,258,242,250,259,242,256,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,298,265,269,254,259,256,248,297,264],
[243,0,271,246,290,246,242,221,261,287,231],
[203,230,0,243,239,231,198,205,222,276,234],
[236,255,258,0,261,244,252,232,243,233,250],
[232,211,262,240,0,233,229,227,213,262,219],
[247,255,270,257,268,0,247,230,229,262,262],
[242,259,303,249,272,254,0,233,231,261,257],
[245,280,296,269,274,271,268,0,286,294,272],
[253,240,279,258,288,272,270,215,0,269,258],
[204,214,225,268,239,239,240,207,232,0,237],
[237,270,267,251,282,239,244,229,243,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,247,256,242,252,251,258,248,236,248],
[248,0,258,246,247,252,271,254,248,262,252],
[254,243,0,238,254,251,261,260,248,261,246],
[245,255,263,0,249,243,272,258,253,250,263],
[259,254,247,252,0,249,274,273,254,257,261],
[249,249,250,258,252,0,274,266,250,259,246],
[250,230,240,229,227,227,0,250,244,245,249],
[243,247,241,243,228,235,251,0,237,243,237],
[253,253,253,248,247,251,257,264,0,261,245],
[265,239,240,251,244,242,256,258,240,0,253],
[253,249,255,238,240,255,252,264,256,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,254,249,262,237,260,266,257,263,234],
[260,0,250,248,264,264,237,264,249,272,258],
[247,251,0,235,250,247,246,268,255,251,227],
[252,253,266,0,263,244,243,263,262,274,255],
[239,237,251,238,0,246,230,263,242,250,241],
[264,237,254,257,255,0,252,284,256,279,259],
[241,264,255,258,271,249,0,289,267,248,258],
[235,237,233,238,238,217,212,0,256,229,228],
[244,252,246,239,259,245,234,245,0,257,239],
[238,229,250,227,251,222,253,272,244,0,226],
[267,243,274,246,260,242,243,273,262,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,239,279,247,290,253,244,248,235,296],
[279,0,262,269,278,296,260,233,195,230,222],
[262,239,0,270,242,249,286,214,232,223,257],
[222,232,231,0,219,253,269,240,205,206,226],
[254,223,259,282,0,259,255,233,201,223,235],
[211,205,252,248,242,0,218,239,184,251,264],
[248,241,215,232,246,283,0,229,224,192,244],
[257,268,287,261,268,262,272,0,256,250,262],
[253,306,269,296,300,317,277,245,0,263,278],
[266,271,278,295,278,250,309,251,238,0,295],
[205,279,244,275,266,237,257,239,223,206,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,258,248,250,278,254,258,256,255,246],
[239,0,243,230,238,254,227,253,226,251,235],
[243,258,0,236,238,256,237,252,224,256,227],
[253,271,265,0,242,269,222,253,252,257,252],
[251,263,263,259,0,272,248,240,253,262,249],
[223,247,245,232,229,0,230,234,230,241,232],
[247,274,264,279,253,271,0,245,253,272,264],
[243,248,249,248,261,267,256,0,249,245,235],
[245,275,277,249,248,271,248,252,0,266,245],
[246,250,245,244,239,260,229,256,235,0,241],
[255,266,274,249,252,269,237,266,256,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,258,250,249,235,260,248,253,252,238],
[240,0,247,237,236,240,263,238,258,245,236],
[243,254,0,238,251,227,258,245,246,247,248],
[251,264,263,0,255,243,266,267,257,250,253],
[252,265,250,246,0,226,273,255,247,254,255],
[266,261,274,258,275,0,302,265,260,275,242],
[241,238,243,235,228,199,0,226,243,238,234],
[253,263,256,234,246,236,275,0,249,268,246],
[248,243,255,244,254,241,258,252,0,251,243],
[249,256,254,251,247,226,263,233,250,0,238],
[263,265,253,248,246,259,267,255,258,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,229,240,247,221,270,240,236,271,262],
[256,0,247,255,249,251,262,247,240,270,263],
[272,254,0,248,264,252,267,252,249,281,267],
[261,246,253,0,237,247,285,251,249,266,262],
[254,252,237,264,0,244,276,254,268,269,272],
[280,250,249,254,257,0,277,253,241,276,270],
[231,239,234,216,225,224,0,217,235,263,233],
[261,254,249,250,247,248,284,0,250,263,265],
[265,261,252,252,233,260,266,251,0,280,254],
[230,231,220,235,232,225,238,238,221,0,233],
[239,238,234,239,229,231,268,236,247,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,172,187,267,219,185,193,217,233,199,196],
[329,0,173,264,270,252,249,197,246,207,211],
[314,328,0,322,304,218,223,257,240,257,272],
[234,237,179,0,241,204,181,204,214,223,198],
[282,231,197,260,0,212,239,219,245,208,195],
[316,249,283,297,289,0,232,228,271,223,231],
[308,252,278,320,262,269,0,255,289,273,186],
[284,304,244,297,282,273,246,0,233,234,288],
[268,255,261,287,256,230,212,268,0,255,234],
[302,294,244,278,293,278,228,267,246,0,266],
[305,290,229,303,306,270,315,213,267,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,219,235,238,236,231,253,220,238,225],
[269,0,247,252,257,257,270,262,257,268,243],
[282,254,0,283,257,251,246,244,237,258,257],
[266,249,218,0,230,238,245,246,234,239,251],
[263,244,244,271,0,251,247,251,240,256,258],
[265,244,250,263,250,0,263,246,242,266,258],
[270,231,255,256,254,238,0,260,227,247,245],
[248,239,257,255,250,255,241,0,233,246,246],
[281,244,264,267,261,259,274,268,0,267,269],
[263,233,243,262,245,235,254,255,234,0,251],
[276,258,244,250,243,243,256,255,232,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,246,268,243,269,276,264,255,256,256],
[257,0,255,247,245,277,274,251,273,267,270],
[255,246,0,246,234,266,266,246,256,239,262],
[233,254,255,0,240,271,253,265,257,244,272],
[258,256,267,261,0,270,281,254,262,250,273],
[232,224,235,230,231,0,240,233,243,241,247],
[225,227,235,248,220,261,0,251,248,249,242],
[237,250,255,236,247,268,250,0,252,245,247],
[246,228,245,244,239,258,253,249,0,239,259],
[245,234,262,257,251,260,252,256,262,0,277],
[245,231,239,229,228,254,259,254,242,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,244,240,246,227,237,213,242,222,255],
[256,0,237,255,257,242,269,225,252,248,252],
[257,264,0,260,251,244,255,235,245,240,257],
[261,246,241,0,236,235,250,232,232,236,266],
[255,244,250,265,0,247,263,236,242,237,276],
[274,259,257,266,254,0,257,225,263,262,257],
[264,232,246,251,238,244,0,233,249,235,257],
[288,276,266,269,265,276,268,0,264,244,279],
[259,249,256,269,259,238,252,237,0,264,265],
[279,253,261,265,264,239,266,257,237,0,265],
[246,249,244,235,225,244,244,222,236,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,266,230,240,256,266,260,242,281,270],
[271,0,249,221,223,254,253,250,253,287,231],
[235,252,0,231,209,262,263,235,237,243,254],
[271,280,270,0,222,256,267,274,226,289,279],
[261,278,292,279,0,290,262,275,248,290,277],
[245,247,239,245,211,0,230,250,228,232,243],
[235,248,238,234,239,271,0,248,224,240,261],
[241,251,266,227,226,251,253,0,226,250,260],
[259,248,264,275,253,273,277,275,0,281,272],
[220,214,258,212,211,269,261,251,220,0,257],
[231,270,247,222,224,258,240,241,229,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,246,254,261,254,255,226,251,258,268],
[250,0,245,258,255,257,269,246,250,249,250],
[255,256,0,266,280,265,253,234,255,250,267],
[247,243,235,0,264,263,260,247,258,259,256],
[240,246,221,237,0,240,249,234,224,247,240],
[247,244,236,238,261,0,253,233,247,261,257],
[246,232,248,241,252,248,0,231,229,242,246],
[275,255,267,254,267,268,270,0,250,271,269],
[250,251,246,243,277,254,272,251,0,251,267],
[243,252,251,242,254,240,259,230,250,0,248],
[233,251,234,245,261,244,255,232,234,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,162,158,253,113,280,206,241,196,142,297],
[339,0,251,156,271,227,291,322,221,138,193],
[343,250,0,279,220,274,279,239,350,193,349],
[248,345,222,0,263,241,323,277,216,267,231],
[388,230,281,238,0,276,340,238,221,322,277],
[221,274,227,260,225,0,278,241,203,250,244],
[295,210,222,178,161,223,0,214,225,245,206],
[260,179,262,224,263,260,287,0,289,205,185],
[305,280,151,285,280,298,276,212,0,174,323],
[359,363,308,234,179,251,256,296,327,0,269],
[204,308,152,270,224,257,295,316,178,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,251,240,263,291,259,252,236,266,251],
[244,0,264,252,244,277,272,237,247,277,268],
[250,237,0,231,238,270,251,239,239,259,249],
[261,249,270,0,241,283,259,248,255,286,255],
[238,257,263,260,0,263,254,233,235,273,264],
[210,224,231,218,238,0,250,240,196,248,229],
[242,229,250,242,247,251,0,247,224,283,253],
[249,264,262,253,268,261,254,0,238,266,256],
[265,254,262,246,266,305,277,263,0,283,282],
[235,224,242,215,228,253,218,235,218,0,232],
[250,233,252,246,237,272,248,245,219,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,241,269,261,248,253,270,249,260,249],
[257,0,252,247,262,259,260,242,239,246,249],
[260,249,0,262,265,255,267,250,240,279,252],
[232,254,239,0,255,240,250,253,233,247,225],
[240,239,236,246,0,226,230,244,240,245,230],
[253,242,246,261,275,0,266,259,240,264,238],
[248,241,234,251,271,235,0,254,238,254,249],
[231,259,251,248,257,242,247,0,267,249,211],
[252,262,261,268,261,261,263,234,0,269,245],
[241,255,222,254,256,237,247,252,232,0,244],
[252,252,249,276,271,263,252,290,256,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,255,268,247,245,246,252,256,231,271],
[263,0,278,265,274,277,261,247,252,229,266],
[246,223,0,242,245,251,224,229,253,211,254],
[233,236,259,0,245,240,248,243,230,218,249],
[254,227,256,256,0,242,243,262,246,230,258],
[256,224,250,261,259,0,234,241,250,226,271],
[255,240,277,253,258,267,0,253,261,258,254],
[249,254,272,258,239,260,248,0,259,226,270],
[245,249,248,271,255,251,240,242,0,229,255],
[270,272,290,283,271,275,243,275,272,0,293],
[230,235,247,252,243,230,247,231,246,208,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,303,234,199,262,257,293,270,299,326,278],
[198,0,230,237,205,251,316,258,250,365,315],
[267,271,0,258,202,252,290,198,303,302,284],
[302,264,243,0,207,288,218,266,269,321,323],
[239,296,299,294,0,293,292,292,336,334,381],
[244,250,249,213,208,0,263,231,275,276,316],
[208,185,211,283,209,238,0,248,245,355,289],
[231,243,303,235,209,270,253,0,289,325,272],
[202,251,198,232,165,226,256,212,0,348,289],
[175,136,199,180,167,225,146,176,153,0,189],
[223,186,217,178,120,185,212,229,212,312,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,227,234,241,217,249,215,238,237,238],
[284,0,241,243,273,246,269,253,212,263,281],
[274,260,0,275,272,201,274,289,260,245,253],
[267,258,226,0,254,233,247,225,229,229,246],
[260,228,229,247,0,231,212,242,211,229,263],
[284,255,300,268,270,0,258,224,248,268,269],
[252,232,227,254,289,243,0,258,269,245,231],
[286,248,212,276,259,277,243,0,235,245,252],
[263,289,241,272,290,253,232,266,0,256,252],
[264,238,256,272,272,233,256,256,245,0,260],
[263,220,248,255,238,232,270,249,249,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,242,231,238,240,244,239,229,239,241],
[242,0,248,231,251,266,250,245,216,250,251],
[259,253,0,254,254,260,239,252,242,260,249],
[270,270,247,0,248,265,246,245,234,266,245],
[263,250,247,253,0,267,247,236,240,262,248],
[261,235,241,236,234,0,225,240,228,253,234],
[257,251,262,255,254,276,0,260,237,270,267],
[262,256,249,256,265,261,241,0,258,260,248],
[272,285,259,267,261,273,264,243,0,287,254],
[262,251,241,235,239,248,231,241,214,0,251],
[260,250,252,256,253,267,234,253,247,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,268,267,244,271,254,268,229,252,266],
[245,0,281,226,235,240,253,260,237,224,252],
[233,220,0,226,231,233,229,256,227,204,237],
[234,275,275,0,254,262,249,273,254,247,269],
[257,266,270,247,0,257,240,278,239,220,270],
[230,261,268,239,244,0,249,267,222,213,262],
[247,248,272,252,261,252,0,223,245,213,262],
[233,241,245,228,223,234,278,0,237,218,257],
[272,264,274,247,262,279,256,264,0,288,278],
[249,277,297,254,281,288,288,283,213,0,280],
[235,249,264,232,231,239,239,244,223,221,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,250,250,250,268,239,246,223,262,257],
[248,0,243,248,255,247,243,250,250,260,260],
[251,258,0,252,257,262,233,256,249,249,261],
[251,253,249,0,259,257,232,250,238,244,259],
[251,246,244,242,0,249,242,238,244,259,247],
[233,254,239,244,252,0,233,243,251,256,244],
[262,258,268,269,259,268,0,276,250,274,267],
[255,251,245,251,263,258,225,0,236,262,259],
[278,251,252,263,257,250,251,265,0,266,272],
[239,241,252,257,242,245,227,239,235,0,241],
[244,241,240,242,254,257,234,242,229,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,251,267,258,264,265,260,233,248,247],
[263,0,275,262,260,286,273,271,255,235,266],
[250,226,0,240,251,255,251,264,225,238,225],
[234,239,261,0,241,269,251,251,250,250,248],
[243,241,250,260,0,273,252,253,243,235,228],
[237,215,246,232,228,0,239,257,231,226,224],
[236,228,250,250,249,262,0,247,244,237,240],
[241,230,237,250,248,244,254,0,233,242,245],
[268,246,276,251,258,270,257,268,0,254,259],
[253,266,263,251,266,275,264,259,247,0,253],
[254,235,276,253,273,277,261,256,242,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,243,224,289,222,299,283,276,231,280],
[252,0,265,223,272,262,311,316,247,250,253],
[258,236,0,238,282,262,287,254,261,244,279],
[277,278,263,0,289,248,323,318,302,294,296],
[212,229,219,212,0,228,256,304,235,231,236],
[279,239,239,253,273,0,281,281,262,275,268],
[202,190,214,178,245,220,0,265,239,205,251],
[218,185,247,183,197,220,236,0,222,209,221],
[225,254,240,199,266,239,262,279,0,231,292],
[270,251,257,207,270,226,296,292,270,0,255],
[221,248,222,205,265,233,250,280,209,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,253,240,232,237,233,254,226,229,253],
[260,0,252,239,249,239,251,252,244,245,235],
[248,249,0,238,254,253,252,256,234,239,243],
[261,262,263,0,269,254,269,260,251,248,258],
[269,252,247,232,0,231,236,252,241,228,248],
[264,262,248,247,270,0,261,265,244,251,260],
[268,250,249,232,265,240,0,253,243,237,249],
[247,249,245,241,249,236,248,0,243,244,240],
[275,257,267,250,260,257,258,258,0,236,248],
[272,256,262,253,273,250,264,257,265,0,242],
[248,266,258,243,253,241,252,261,253,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,286,250,262,260,253,250,243,275,264],
[248,0,269,263,259,273,275,246,285,286,281],
[215,232,0,230,236,245,238,214,266,276,236],
[251,238,271,0,232,254,233,245,253,251,242],
[239,242,265,269,0,234,226,257,255,254,272],
[241,228,256,247,267,0,254,262,245,262,266],
[248,226,263,268,275,247,0,223,264,281,255],
[251,255,287,256,244,239,278,0,264,289,277],
[258,216,235,248,246,256,237,237,0,240,276],
[226,215,225,250,247,239,220,212,261,0,239],
[237,220,265,259,229,235,246,224,225,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,254,237,211,221,260,212,244,230,235],
[254,0,263,248,237,230,270,247,278,232,260],
[247,238,0,211,225,208,266,237,253,229,246],
[264,253,290,0,230,238,276,278,253,251,269],
[290,264,276,271,0,262,286,271,260,246,266],
[280,271,293,263,239,0,295,259,277,246,290],
[241,231,235,225,215,206,0,215,226,191,225],
[289,254,264,223,230,242,286,0,263,219,258],
[257,223,248,248,241,224,275,238,0,227,253],
[271,269,272,250,255,255,310,282,274,0,256],
[266,241,255,232,235,211,276,243,248,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,262,258,270,241,268,270,256,247,257],
[242,0,300,263,232,261,263,239,260,268,252],
[239,201,0,247,233,221,259,240,228,243,245],
[243,238,254,0,252,244,245,271,231,234,240],
[231,269,268,249,0,249,253,252,248,235,253],
[260,240,280,257,252,0,263,275,236,249,250],
[233,238,242,256,248,238,0,240,230,248,239],
[231,262,261,230,249,226,261,0,234,243,254],
[245,241,273,270,253,265,271,267,0,249,241],
[254,233,258,267,266,252,253,258,252,0,268],
[244,249,256,261,248,251,262,247,260,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,279,158,297,267,154,256,209,203,162],
[275,0,272,233,258,222,238,197,268,221,155],
[222,229,0,313,276,310,162,313,279,291,213],
[343,268,188,0,249,282,226,255,202,198,175],
[204,243,225,252,0,303,188,199,264,233,240],
[234,279,191,219,198,0,180,257,133,280,228],
[347,263,339,275,313,321,0,293,218,263,301],
[245,304,188,246,302,244,208,0,176,278,236],
[292,233,222,299,237,368,283,325,0,331,307],
[298,280,210,303,268,221,238,223,170,0,253],
[339,346,288,326,261,273,200,265,194,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,210,312,282,264,240,258,302,286,270,259],
[291,0,302,302,271,247,283,300,248,316,258],
[189,199,0,227,224,220,239,223,235,246,201],
[219,199,274,0,275,234,252,276,276,276,219],
[237,230,277,226,0,247,252,240,273,291,262],
[261,254,281,267,254,0,258,273,269,292,238],
[243,218,262,249,249,243,0,224,289,270,250],
[199,201,278,225,261,228,277,0,281,289,225],
[215,253,266,225,228,232,212,220,0,288,238],
[231,185,255,225,210,209,231,212,213,0,221],
[242,243,300,282,239,263,251,276,263,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,241,252,237,244,257,251,233,258,248],
[242,0,240,232,220,243,250,241,252,227,233],
[260,261,0,258,255,258,246,245,241,240,243],
[249,269,243,0,232,247,237,253,255,252,256],
[264,281,246,269,0,250,264,258,243,253,251],
[257,258,243,254,251,0,248,258,227,243,249],
[244,251,255,264,237,253,0,238,233,248,236],
[250,260,256,248,243,243,263,0,238,230,253],
[268,249,260,246,258,274,268,263,0,265,267],
[243,274,261,249,248,258,253,271,236,0,252],
[253,268,258,245,250,252,265,248,234,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,249,276,266,258,250,245,273,264,280],
[232,0,260,266,247,249,223,253,254,216,258],
[252,241,0,270,246,254,248,261,279,247,259],
[225,235,231,0,229,236,235,208,245,232,251],
[235,254,255,272,0,259,243,241,263,251,260],
[243,252,247,265,242,0,253,246,255,251,260],
[251,278,253,266,258,248,0,251,255,249,280],
[256,248,240,293,260,255,250,0,267,273,261],
[228,247,222,256,238,246,246,234,0,242,239],
[237,285,254,269,250,250,252,228,259,0,259],
[221,243,242,250,241,241,221,240,262,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,275,235,253,239,268,264,252,292,293],
[265,0,253,259,308,256,285,244,252,273,250],
[226,248,0,218,279,202,323,233,264,250,248],
[266,242,283,0,283,237,289,276,262,276,286],
[248,193,222,218,0,191,249,238,213,213,238],
[262,245,299,264,310,0,290,272,272,250,268],
[233,216,178,212,252,211,0,205,221,212,209],
[237,257,268,225,263,229,296,0,259,212,266],
[249,249,237,239,288,229,280,242,0,250,264],
[209,228,251,225,288,251,289,289,251,0,263],
[208,251,253,215,263,233,292,235,237,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,243,275,252,254,273,264,249,278,263],
[263,0,262,249,263,244,247,245,263,265,238],
[258,239,0,264,258,257,263,253,255,270,221],
[226,252,237,0,261,235,250,249,246,265,240],
[249,238,243,240,0,232,256,244,249,257,243],
[247,257,244,266,269,0,274,279,238,272,242],
[228,254,238,251,245,227,0,245,232,236,235],
[237,256,248,252,257,222,256,0,253,273,259],
[252,238,246,255,252,263,269,248,0,267,254],
[223,236,231,236,244,229,265,228,234,0,231],
[238,263,280,261,258,259,266,242,247,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,268,235,244,241,239,251,244,257,242],
[261,0,279,258,236,253,264,253,249,258,252],
[233,222,0,242,236,227,256,239,240,235,251],
[266,243,259,0,247,258,237,250,243,250,250],
[257,265,265,254,0,274,240,256,260,253,252],
[260,248,274,243,227,0,255,248,248,260,253],
[262,237,245,264,261,246,0,243,245,266,249],
[250,248,262,251,245,253,258,0,253,250,247],
[257,252,261,258,241,253,256,248,0,256,255],
[244,243,266,251,248,241,235,251,245,0,257],
[259,249,250,251,249,248,252,254,246,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,262,260,242,241,252,253,244,268,250],
[259,0,271,272,255,243,244,258,257,277,266],
[239,230,0,247,219,228,236,254,238,253,237],
[241,229,254,0,227,236,238,244,232,261,248],
[259,246,282,274,0,258,257,280,252,284,261],
[260,258,273,265,243,0,247,261,257,272,240],
[249,257,265,263,244,254,0,258,258,275,266],
[248,243,247,257,221,240,243,0,251,262,249],
[257,244,263,269,249,244,243,250,0,267,261],
[233,224,248,240,217,229,226,239,234,0,226],
[251,235,264,253,240,261,235,252,240,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,259,271,278,246,267,260,249,264,251],
[255,0,255,262,269,233,258,250,264,260,262],
[242,246,0,265,268,246,253,246,264,261,251],
[230,239,236,0,259,226,237,236,247,251,252],
[223,232,233,242,0,232,242,236,243,245,230],
[255,268,255,275,269,0,273,242,267,273,260],
[234,243,248,264,259,228,0,241,270,249,250],
[241,251,255,265,265,259,260,0,260,262,248],
[252,237,237,254,258,234,231,241,0,254,258],
[237,241,240,250,256,228,252,239,247,0,233],
[250,239,250,249,271,241,251,253,243,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,258,264,270,255,253,264,269,235,269],
[257,0,253,261,249,262,243,258,245,245,256],
[243,248,0,244,249,252,230,246,244,241,240],
[237,240,257,0,240,258,236,240,250,235,240],
[231,252,252,261,0,251,246,246,254,246,257],
[246,239,249,243,250,0,261,248,257,246,247],
[248,258,271,265,255,240,0,251,264,252,251],
[237,243,255,261,255,253,250,0,254,250,247],
[232,256,257,251,247,244,237,247,0,236,243],
[266,256,260,266,255,255,249,251,265,0,255],
[232,245,261,261,244,254,250,254,258,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,254,231,244,257,256,245,246,249,272],
[264,0,259,266,291,230,280,248,277,258,255],
[247,242,0,231,206,224,253,248,223,252,225],
[270,235,270,0,258,236,250,262,271,244,254],
[257,210,295,243,0,249,243,270,245,255,243],
[244,271,277,265,252,0,245,271,245,256,246],
[245,221,248,251,258,256,0,241,257,239,252],
[256,253,253,239,231,230,260,0,243,222,256],
[255,224,278,230,256,256,244,258,0,239,233],
[252,243,249,257,246,245,262,279,262,0,233],
[229,246,276,247,258,255,249,245,268,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,223,254,257,226,225,243,265,241,255],
[256,0,247,256,220,243,262,253,242,244,249],
[278,254,0,252,252,243,228,275,260,244,266],
[247,245,249,0,238,255,243,253,252,244,259],
[244,281,249,263,0,262,257,252,252,252,278],
[275,258,258,246,239,0,250,245,241,261,267],
[276,239,273,258,244,251,0,247,259,241,279],
[258,248,226,248,249,256,254,0,269,235,266],
[236,259,241,249,249,260,242,232,0,259,259],
[260,257,257,257,249,240,260,266,242,0,273],
[246,252,235,242,223,234,222,235,242,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,229,241,235,262,237,247,258,251,226],
[253,0,223,238,254,293,247,247,254,263,221],
[272,278,0,245,298,315,296,279,276,284,257],
[260,263,256,0,305,323,317,274,275,273,247],
[266,247,203,196,0,270,252,230,238,243,217],
[239,208,186,178,231,0,226,195,224,249,206],
[264,254,205,184,249,275,0,240,232,234,189],
[254,254,222,227,271,306,261,0,287,283,235],
[243,247,225,226,263,277,269,214,0,264,221],
[250,238,217,228,258,252,267,218,237,0,221],
[275,280,244,254,284,295,312,266,280,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,270,260,265,259,263,254,250,268,259],
[251,0,235,228,232,237,261,238,236,243,246],
[231,266,0,243,261,245,280,249,246,254,261],
[241,273,258,0,255,266,262,246,243,254,270],
[236,269,240,246,0,249,253,243,258,242,255],
[242,264,256,235,252,0,267,239,252,254,264],
[238,240,221,239,248,234,0,243,240,231,257],
[247,263,252,255,258,262,258,0,255,241,260],
[251,265,255,258,243,249,261,246,0,267,254],
[233,258,247,247,259,247,270,260,234,0,254],
[242,255,240,231,246,237,244,241,247,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,253,267,237,278,261,263,258,270,283],
[232,0,220,248,208,224,236,241,237,244,250],
[248,281,0,267,231,269,247,277,261,263,271],
[234,253,234,0,207,253,222,218,233,256,244],
[264,293,270,294,0,277,247,280,267,284,280],
[223,277,232,248,224,0,247,258,260,255,264],
[240,265,254,279,254,254,0,261,256,248,285],
[238,260,224,283,221,243,240,0,258,264,274],
[243,264,240,268,234,241,245,243,0,275,273],
[231,257,238,245,217,246,253,237,226,0,272],
[218,251,230,257,221,237,216,227,228,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,288,272,243,276,281,267,247,291,278,248],
[213,0,289,204,206,273,236,206,256,243,223],
[229,212,0,251,217,267,262,204,209,293,211],
[258,297,250,0,238,250,233,232,290,280,220],
[225,295,284,263,0,249,259,227,265,280,254],
[220,228,234,251,252,0,233,227,225,232,221],
[234,265,239,268,242,268,0,233,225,283,209],
[254,295,297,269,274,274,268,0,251,290,238],
[210,245,292,211,236,276,276,250,0,267,242],
[223,258,208,221,221,269,218,211,234,0,219],
[253,278,290,281,247,280,292,263,259,282,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,284,231,254,249,251,279,281,280,276],
[251,0,243,266,243,249,235,228,238,234,275],
[217,258,0,210,220,269,233,230,219,238,230],
[270,235,291,0,257,244,246,251,251,242,276],
[247,258,281,244,0,257,250,247,277,272,275],
[252,252,232,257,244,0,222,220,238,217,241],
[250,266,268,255,251,279,0,266,254,270,304],
[222,273,271,250,254,281,235,0,260,224,270],
[220,263,282,250,224,263,247,241,0,255,264],
[221,267,263,259,229,284,231,277,246,0,277],
[225,226,271,225,226,260,197,231,237,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,349,349,289,344,344,287,205,203,437,285],
[152,0,257,117,164,131,270,196,136,290,183],
[152,244,0,128,264,203,145,190,135,203,227],
[212,384,373,0,335,335,311,196,340,308,283],
[157,337,237,166,0,168,275,201,195,208,256],
[157,370,298,166,333,0,220,306,136,290,211],
[214,231,356,190,226,281,0,257,138,347,326],
[296,305,311,305,300,195,244,0,189,347,236],
[298,365,366,161,306,365,363,312,0,349,357],
[64,211,298,193,293,211,154,154,152,0,203],
[216,318,274,218,245,290,175,265,144,298,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,243,253,252,251,253,262,270,256,252],
[251,0,232,233,248,240,235,252,254,260,250],
[258,269,0,254,253,245,266,270,279,263,251],
[248,268,247,0,269,238,244,262,271,249,247],
[249,253,248,232,0,234,226,256,245,250,249],
[250,261,256,263,267,0,245,274,278,269,252],
[248,266,235,257,275,256,0,267,281,263,270],
[239,249,231,239,245,227,234,0,260,250,229],
[231,247,222,230,256,223,220,241,0,240,237],
[245,241,238,252,251,232,238,251,261,0,242],
[249,251,250,254,252,249,231,272,264,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,249,268,244,278,261,258,253,260,249],
[247,0,257,263,240,257,245,256,243,241,239],
[252,244,0,262,239,262,244,255,245,266,234],
[233,238,239,0,254,251,247,241,251,241,245],
[257,261,262,247,0,262,246,256,258,281,254],
[223,244,239,250,239,0,239,232,221,250,244],
[240,256,257,254,255,262,0,242,256,258,252],
[243,245,246,260,245,269,259,0,244,244,250],
[248,258,256,250,243,280,245,257,0,257,247],
[241,260,235,260,220,251,243,257,244,0,237],
[252,262,267,256,247,257,249,251,254,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,240,245,251,278,243,251,227,251,233],
[276,0,247,289,288,281,258,276,265,249,265],
[261,254,0,237,240,252,242,247,236,228,261],
[256,212,264,0,255,259,254,242,248,227,260],
[250,213,261,246,0,247,233,231,224,246,239],
[223,220,249,242,254,0,262,255,257,223,228],
[258,243,259,247,268,239,0,247,246,239,244],
[250,225,254,259,270,246,254,0,226,229,273],
[274,236,265,253,277,244,255,275,0,241,234],
[250,252,273,274,255,278,262,272,260,0,260],
[268,236,240,241,262,273,257,228,267,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,252,237,250,237,255,235,253,239,258],
[247,0,272,257,254,262,266,242,267,225,245],
[249,229,0,251,224,254,250,255,255,224,227],
[264,244,250,0,234,241,249,243,267,237,250],
[251,247,277,267,0,259,254,258,277,253,258],
[264,239,247,260,242,0,253,245,226,215,235],
[246,235,251,252,247,248,0,237,250,221,242],
[266,259,246,258,243,256,264,0,254,222,271],
[248,234,246,234,224,275,251,247,0,213,252],
[262,276,277,264,248,286,280,279,288,0,270],
[243,256,274,251,243,266,259,230,249,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,275,268,252,254,258,237,271,246,256],
[231,0,296,287,246,232,253,225,260,249,268],
[226,205,0,243,248,212,242,213,243,218,230],
[233,214,258,0,245,210,244,234,221,230,216],
[249,255,253,256,0,234,242,232,257,240,239],
[247,269,289,291,267,0,284,225,265,261,236],
[243,248,259,257,259,217,0,232,271,229,230],
[264,276,288,267,269,276,269,0,275,246,265],
[230,241,258,280,244,236,230,226,0,231,235],
[255,252,283,271,261,240,272,255,270,0,240],
[245,233,271,285,262,265,271,236,266,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,304,290,250,227,208,281,200,310,220],
[238,0,292,230,276,195,221,210,268,296,258],
[197,209,0,193,221,196,156,134,214,278,200],
[211,271,308,0,280,225,243,216,259,313,251],
[251,225,280,221,0,202,265,190,208,278,195],
[274,306,305,276,299,0,218,219,221,266,273],
[293,280,345,258,236,283,0,244,286,327,234],
[220,291,367,285,311,282,257,0,281,357,253],
[301,233,287,242,293,280,215,220,0,258,267],
[191,205,223,188,223,235,174,144,243,0,205],
[281,243,301,250,306,228,267,248,234,296,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,218,251,251,228,207,214,236,241,216],
[234,0,229,221,272,219,204,275,230,193,248],
[283,272,0,264,275,265,255,251,265,235,291],
[250,280,237,0,244,252,195,241,251,206,237],
[250,229,226,257,0,245,192,242,248,192,234],
[273,282,236,249,256,0,238,259,273,232,259],
[294,297,246,306,309,263,0,272,307,278,297],
[287,226,250,260,259,242,229,0,275,250,237],
[265,271,236,250,253,228,194,226,0,206,251],
[260,308,266,295,309,269,223,251,295,0,279],
[285,253,210,264,267,242,204,264,250,222,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,267,265,257,257,251,250,262,247,254],
[247,0,256,238,254,252,237,252,252,248,250],
[234,245,0,237,256,259,237,234,243,240,250],
[236,263,264,0,257,256,240,258,253,257,252],
[244,247,245,244,0,253,237,243,244,252,239],
[244,249,242,245,248,0,229,240,265,241,235],
[250,264,264,261,264,272,0,247,265,259,259],
[251,249,267,243,258,261,254,0,251,243,239],
[239,249,258,248,257,236,236,250,0,250,245],
[254,253,261,244,249,260,242,258,251,0,248],
[247,251,251,249,262,266,242,262,256,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,266,246,246,245,237,250,238,246,239],
[248,0,266,253,255,246,249,238,230,259,246],
[235,235,0,228,222,221,239,226,225,245,233],
[255,248,273,0,240,254,242,253,239,258,246],
[255,246,279,261,0,269,254,250,251,257,257],
[256,255,280,247,232,0,250,253,238,263,243],
[264,252,262,259,247,251,0,255,241,256,255],
[251,263,275,248,251,248,246,0,232,254,250],
[263,271,276,262,250,263,260,269,0,277,262],
[255,242,256,243,244,238,245,247,224,0,231],
[262,255,268,255,244,258,246,251,239,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,254,257,264,235,249,257,247,243,256],
[256,0,255,259,252,258,254,268,263,236,274],
[247,246,0,222,262,255,248,251,264,237,252],
[244,242,279,0,262,252,249,260,270,247,268],
[237,249,239,239,0,248,237,265,253,228,253],
[266,243,246,249,253,0,242,256,265,253,259],
[252,247,253,252,264,259,0,280,280,256,270],
[244,233,250,241,236,245,221,0,251,216,242],
[254,238,237,231,248,236,221,250,0,228,233],
[258,265,264,254,273,248,245,285,273,0,258],
[245,227,249,233,248,242,231,259,268,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,217,227,258,243,231,253,225,234,224],
[265,0,246,255,250,282,238,263,239,247,247],
[284,255,0,264,258,282,266,285,242,255,248],
[274,246,237,0,245,256,251,265,233,243,260],
[243,251,243,256,0,256,236,260,230,237,230],
[258,219,219,245,245,0,235,257,215,247,215],
[270,263,235,250,265,266,0,269,245,261,258],
[248,238,216,236,241,244,232,0,218,226,229],
[276,262,259,268,271,286,256,283,0,254,240],
[267,254,246,258,264,254,240,275,247,0,265],
[277,254,253,241,271,286,243,272,261,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,253,248,266,263,224,245,241,238,255],
[245,0,248,260,247,244,254,259,257,252,216],
[248,253,0,265,270,260,244,247,264,263,258],
[253,241,236,0,242,235,241,256,253,247,228],
[235,254,231,259,0,235,232,259,252,251,223],
[238,257,241,266,266,0,248,248,259,258,211],
[277,247,257,260,269,253,0,283,271,251,217],
[256,242,254,245,242,253,218,0,245,249,227],
[260,244,237,248,249,242,230,256,0,238,220],
[263,249,238,254,250,243,250,252,263,0,235],
[246,285,243,273,278,290,284,274,281,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,207,236,233,221,212,211,207,221,222,224],
[294,0,254,259,248,254,237,237,244,239,248],
[265,247,0,245,242,221,254,231,245,229,229],
[268,242,256,0,253,230,236,244,266,236,228],
[280,253,259,248,0,256,243,252,245,243,246],
[289,247,280,271,245,0,255,243,256,249,238],
[290,264,247,265,258,246,0,238,259,250,248],
[294,264,270,257,249,258,263,0,273,262,268],
[280,257,256,235,256,245,242,228,0,258,231],
[279,262,272,265,258,252,251,239,243,0,256],
[277,253,272,273,255,263,253,233,270,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,245,279,258,315,260,250,176,233,224],
[250,0,242,272,318,301,270,241,255,265,307],
[256,259,0,262,267,318,245,220,257,240,191],
[222,229,239,0,248,276,289,264,206,248,241],
[243,183,234,253,0,303,279,224,235,237,263],
[186,200,183,225,198,0,227,254,195,216,202],
[241,231,256,212,222,274,0,261,178,245,160],
[251,260,281,237,277,247,240,0,264,251,286],
[325,246,244,295,266,306,323,237,0,269,290],
[268,236,261,253,264,285,256,250,232,0,208],
[277,194,310,260,238,299,341,215,211,293,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,231,252,237,209,221,249,217,222,233],
[250,0,218,234,230,216,222,236,224,222,224],
[270,283,0,249,248,215,242,257,234,229,253],
[249,267,252,0,244,242,236,261,243,241,218],
[264,271,253,257,0,228,261,250,220,233,239],
[292,285,286,259,273,0,257,289,246,272,266],
[280,279,259,265,240,244,0,261,260,242,247],
[252,265,244,240,251,212,240,0,247,245,257],
[284,277,267,258,281,255,241,254,0,235,248],
[279,279,272,260,268,229,259,256,266,0,262],
[268,277,248,283,262,235,254,244,253,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,244,250,248,238,259,248,271,255,259],
[241,0,251,262,239,252,253,265,261,244,254],
[257,250,0,280,246,260,276,266,271,265,270],
[251,239,221,0,233,242,247,257,254,224,250],
[253,262,255,268,0,259,271,268,278,240,273],
[263,249,241,259,242,0,256,258,259,246,256],
[242,248,225,254,230,245,0,248,251,233,244],
[253,236,235,244,233,243,253,0,259,231,240],
[230,240,230,247,223,242,250,242,0,241,246],
[246,257,236,277,261,255,268,270,260,0,247],
[242,247,231,251,228,245,257,261,255,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,261,253,251,260,249,261,247,249,239],
[239,0,242,249,248,252,261,243,248,203,256],
[240,259,0,252,264,252,270,285,258,253,260],
[248,252,249,0,249,262,238,247,247,221,251],
[250,253,237,252,0,254,250,252,249,214,251],
[241,249,249,239,247,0,261,249,237,232,241],
[252,240,231,263,251,240,0,257,268,224,261],
[240,258,216,254,249,252,244,0,252,225,230],
[254,253,243,254,252,264,233,249,0,220,255],
[252,298,248,280,287,269,277,276,281,0,276],
[262,245,241,250,250,260,240,271,246,225,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,230,258,245,256,237,241,261,256,237],
[271,0,260,278,272,269,269,245,270,257,270],
[271,241,0,240,275,265,282,232,256,258,259],
[243,223,261,0,268,247,246,219,254,277,239],
[256,229,226,233,0,246,242,223,254,227,232],
[245,232,236,254,255,0,257,240,261,245,236],
[264,232,219,255,259,244,0,239,249,261,246],
[260,256,269,282,278,261,262,0,274,256,244],
[240,231,245,247,247,240,252,227,0,252,235],
[245,244,243,224,274,256,240,245,249,0,229],
[264,231,242,262,269,265,255,257,266,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,273,255,249,256,270,261,253,268,260],
[217,0,261,239,245,238,253,255,228,244,237],
[228,240,0,227,226,225,239,232,209,234,233],
[246,262,274,0,247,237,254,259,236,246,249],
[252,256,275,254,0,237,257,261,227,257,252],
[245,263,276,264,264,0,272,275,250,249,244],
[231,248,262,247,244,229,0,265,222,238,255],
[240,246,269,242,240,226,236,0,235,240,242],
[248,273,292,265,274,251,279,266,0,245,275],
[233,257,267,255,244,252,263,261,256,0,264],
[241,264,268,252,249,257,246,259,226,237,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,346,280,309,252,297,246,262,256,262,223],
[155,0,164,227,107,267,193,249,219,208,248],
[221,337,0,254,241,271,220,303,225,170,192],
[192,274,247,0,241,374,288,355,359,330,316],
[249,394,260,260,0,319,307,271,259,271,312],
[204,234,230,127,182,0,240,361,171,224,287],
[255,308,281,213,194,261,0,277,259,223,302],
[239,252,198,146,230,140,224,0,108,135,284],
[245,282,276,142,242,330,242,393,0,176,277],
[239,293,331,171,230,277,278,366,325,0,325],
[278,253,309,185,189,214,199,217,224,176,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,266,252,248,244,258,248,268,237,273],
[245,0,239,264,236,239,254,227,249,245,263],
[235,262,0,242,244,239,252,226,233,239,245],
[249,237,259,0,249,251,250,241,240,235,262],
[253,265,257,252,0,242,263,243,254,255,267],
[257,262,262,250,259,0,262,256,264,250,257],
[243,247,249,251,238,239,0,250,261,243,263],
[253,274,275,260,258,245,251,0,254,246,274],
[233,252,268,261,247,237,240,247,0,255,262],
[264,256,262,266,246,251,258,255,246,0,274],
[228,238,256,239,234,244,238,227,239,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,248,255,259,263,253,248,250,230,261],
[261,0,253,257,258,263,246,247,230,242,254],
[253,248,0,227,240,259,235,236,241,253,257],
[246,244,274,0,252,273,255,247,251,238,250],
[242,243,261,249,0,244,258,220,243,230,251],
[238,238,242,228,257,0,256,228,245,239,233],
[248,255,266,246,243,245,0,235,241,237,236],
[253,254,265,254,281,273,266,0,269,245,275],
[251,271,260,250,258,256,260,232,0,245,268],
[271,259,248,263,271,262,264,256,256,0,270],
[240,247,244,251,250,268,265,226,233,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,235,238,279,242,270,248,244,228,255],
[273,0,266,227,267,237,275,255,266,246,254],
[266,235,0,243,260,247,241,254,244,255,251],
[263,274,258,0,284,233,251,245,254,250,246],
[222,234,241,217,0,236,263,219,242,247,210],
[259,264,254,268,265,0,264,285,280,259,248],
[231,226,260,250,238,237,0,237,248,234,232],
[253,246,247,256,282,216,264,0,269,253,273],
[257,235,257,247,259,221,253,232,0,251,238],
[273,255,246,251,254,242,267,248,250,0,252],
[246,247,250,255,291,253,269,228,263,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,255,258,251,273,265,248,261,261,250],
[258,0,270,247,270,269,265,263,278,279,274],
[246,231,0,265,273,273,258,259,258,274,252],
[243,254,236,0,272,271,268,246,240,269,249],
[250,231,228,229,0,265,259,253,249,267,256],
[228,232,228,230,236,0,241,229,237,259,257],
[236,236,243,233,242,260,0,230,247,262,255],
[253,238,242,255,248,272,271,0,250,271,240],
[240,223,243,261,252,264,254,251,0,261,246],
[240,222,227,232,234,242,239,230,240,0,242],
[251,227,249,252,245,244,246,261,255,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,247,255,240,258,241,238,242,238,239],
[287,0,260,266,250,252,263,269,257,252,243],
[254,241,0,251,248,250,226,252,247,249,258],
[246,235,250,0,242,246,230,252,241,254,244],
[261,251,253,259,0,261,247,231,263,249,260],
[243,249,251,255,240,0,233,251,249,259,263],
[260,238,275,271,254,268,0,257,236,252,259],
[263,232,249,249,270,250,244,0,255,246,245],
[259,244,254,260,238,252,265,246,0,238,252],
[263,249,252,247,252,242,249,255,263,0,262],
[262,258,243,257,241,238,242,256,249,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,270,251,252,230,246,238,245,268,251],
[242,0,259,239,249,224,245,238,242,248,243],
[231,242,0,225,247,238,227,231,247,252,229],
[250,262,276,0,247,270,258,253,249,267,250],
[249,252,254,254,0,252,268,255,231,269,275],
[271,277,263,231,249,0,246,257,253,271,254],
[255,256,274,243,233,255,0,245,261,267,237],
[263,263,270,248,246,244,256,0,257,253,261],
[256,259,254,252,270,248,240,244,0,291,255],
[233,253,249,234,232,230,234,248,210,0,243],
[250,258,272,251,226,247,264,240,246,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,204,249,227,213,235,244,228,253,244],
[254,0,243,259,248,254,201,275,285,265,239],
[297,258,0,269,310,267,269,286,247,298,282],
[252,242,232,0,254,224,227,259,267,277,217],
[274,253,191,247,0,233,220,240,248,298,198],
[288,247,234,277,268,0,247,260,241,288,238],
[266,300,232,274,281,254,0,270,274,281,243],
[257,226,215,242,261,241,231,0,207,259,228],
[273,216,254,234,253,260,227,294,0,290,228],
[248,236,203,224,203,213,220,242,211,0,229],
[257,262,219,284,303,263,258,273,273,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,113,124,259,179,8,128,196,113,233,125],
[388,0,198,324,250,274,178,270,192,200,253],
[377,303,0,364,356,259,126,259,252,326,280],
[242,177,137,0,199,8,191,116,141,149,146],
[322,251,145,302,0,133,125,196,147,221,154],
[493,227,242,493,368,0,296,314,318,318,243],
[373,323,375,310,376,205,0,204,272,325,205],
[305,231,242,385,305,187,297,0,180,254,200],
[388,309,249,360,354,183,229,321,0,324,249],
[268,301,175,352,280,183,176,247,177,0,125],
[376,248,221,355,347,258,296,301,252,376,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,251,250,251,261,284,269,245,280,247],
[231,0,256,219,232,252,254,202,228,207,249],
[250,245,0,222,254,258,264,240,256,266,260],
[251,282,279,0,259,252,258,260,236,256,253],
[250,269,247,242,0,262,249,263,256,253,242],
[240,249,243,249,239,0,228,236,236,265,221],
[217,247,237,243,252,273,0,235,230,239,241],
[232,299,261,241,238,265,266,0,262,245,259],
[256,273,245,265,245,265,271,239,0,235,232],
[221,294,235,245,248,236,262,256,266,0,227],
[254,252,241,248,259,280,260,242,269,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,262,234,250,265,239,263,238,237,221],
[253,0,247,249,235,262,237,252,224,230,236],
[239,254,0,235,237,240,241,243,225,232,226],
[267,252,266,0,256,252,256,254,255,256,233],
[251,266,264,245,0,265,243,247,245,237,235],
[236,239,261,249,236,0,240,237,239,237,221],
[262,264,260,245,258,261,0,262,257,239,238],
[238,249,258,247,254,264,239,0,233,240,241],
[263,277,276,246,256,262,244,268,0,259,230],
[264,271,269,245,264,264,262,261,242,0,263],
[280,265,275,268,266,280,263,260,271,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,265,260,244,251,256,253,262,248,251],
[249,0,256,248,242,241,252,249,249,232,248],
[236,245,0,253,235,218,239,250,234,243,246],
[241,253,248,0,240,238,236,243,252,238,246],
[257,259,266,261,0,245,247,259,255,253,244],
[250,260,283,263,256,0,261,258,279,267,258],
[245,249,262,265,254,240,0,259,260,251,250],
[248,252,251,258,242,243,242,0,243,242,253],
[239,252,267,249,246,222,241,258,0,236,255],
[253,269,258,263,248,234,250,259,265,0,247],
[250,253,255,255,257,243,251,248,246,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,233,244,264,237,256,237,245,229,263],
[255,0,247,229,226,230,248,253,251,231,241],
[268,254,0,263,245,242,258,246,250,243,261],
[257,272,238,0,226,255,234,252,241,249,241],
[237,275,256,275,0,250,257,274,269,245,241],
[264,271,259,246,251,0,251,268,275,249,244],
[245,253,243,267,244,250,0,259,250,252,253],
[264,248,255,249,227,233,242,0,249,247,257],
[256,250,251,260,232,226,251,252,0,234,246],
[272,270,258,252,256,252,249,254,267,0,243],
[238,260,240,260,260,257,248,244,255,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,245,246,256,242,244,250,252,253,245],
[258,0,250,257,239,230,257,251,256,276,244],
[256,251,0,246,242,236,252,239,229,251,247],
[255,244,255,0,254,247,240,242,242,255,232],
[245,262,259,247,0,237,259,246,249,266,243],
[259,271,265,254,264,0,250,256,262,258,259],
[257,244,249,261,242,251,0,269,255,260,245],
[251,250,262,259,255,245,232,0,262,255,250],
[249,245,272,259,252,239,246,239,0,259,235],
[248,225,250,246,235,243,241,246,242,0,241],
[256,257,254,269,258,242,256,251,266,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,268,232,252,270,251,262,270,272,266],
[241,0,248,235,241,268,243,258,244,241,241],
[233,253,0,228,232,272,244,263,245,253,271],
[269,266,273,0,251,273,250,254,267,270,281],
[249,260,269,250,0,269,246,265,265,251,270],
[231,233,229,228,232,0,218,252,239,250,249],
[250,258,257,251,255,283,0,264,259,259,276],
[239,243,238,247,236,249,237,0,248,247,257],
[231,257,256,234,236,262,242,253,0,240,262],
[229,260,248,231,250,251,242,254,261,0,271],
[235,260,230,220,231,252,225,244,239,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,245,231,234,234,231,228,241,214,236],
[274,0,260,240,246,259,258,251,278,259,250],
[256,241,0,227,242,232,253,238,268,232,249],
[270,261,274,0,257,261,264,243,269,257,274],
[267,255,259,244,0,246,261,229,283,248,257],
[267,242,269,240,255,0,254,225,273,229,251],
[270,243,248,237,240,247,0,238,263,252,264],
[273,250,263,258,272,276,263,0,275,251,282],
[260,223,233,232,218,228,238,226,0,227,244],
[287,242,269,244,253,272,249,250,274,0,271],
[265,251,252,227,244,250,237,219,257,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,270,259,250,272,282,272,260,246,218],
[256,0,269,269,261,264,264,253,265,268,245],
[231,232,0,237,246,255,246,244,262,224,241],
[242,232,264,0,271,269,267,262,286,252,253],
[251,240,255,230,0,253,244,233,250,243,235],
[229,237,246,232,248,0,270,253,267,250,223],
[219,237,255,234,257,231,0,234,277,244,229],
[229,248,257,239,268,248,267,0,281,266,230],
[241,236,239,215,251,234,224,220,0,259,233],
[255,233,277,249,258,251,257,235,242,0,215],
[283,256,260,248,266,278,272,271,268,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,274,237,266,245,231,240,238,254,270],
[266,0,246,232,267,235,272,257,234,280,232],
[227,255,0,242,272,233,257,254,228,257,261],
[264,269,259,0,269,250,271,255,265,283,262],
[235,234,229,232,0,241,237,244,221,258,251],
[256,266,268,251,260,0,250,271,257,254,247],
[270,229,244,230,264,251,0,245,261,253,263],
[261,244,247,246,257,230,256,0,212,252,261],
[263,267,273,236,280,244,240,289,0,269,270],
[247,221,244,218,243,247,248,249,232,0,248],
[231,269,240,239,250,254,238,240,231,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,223,240,269,205,227,245,242,309,268],
[238,0,187,265,274,247,233,261,271,316,230],
[278,314,0,273,298,279,245,298,291,305,275],
[261,236,228,0,262,248,225,270,266,297,232],
[232,227,203,239,0,213,220,249,252,313,227],
[296,254,222,253,288,0,270,296,268,325,270],
[274,268,256,276,281,231,0,265,247,288,264],
[256,240,203,231,252,205,236,0,276,286,263],
[259,230,210,235,249,233,254,225,0,269,234],
[192,185,196,204,188,176,213,215,232,0,199],
[233,271,226,269,274,231,237,238,267,302,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,263,246,249,252,260,256,259,258,254],
[251,0,244,254,261,245,261,247,261,252,241],
[238,257,0,242,253,236,256,243,255,238,248],
[255,247,259,0,249,245,246,249,263,250,240],
[252,240,248,252,0,253,251,253,262,253,242],
[249,256,265,256,248,0,250,262,276,261,263],
[241,240,245,255,250,251,0,254,259,268,243],
[245,254,258,252,248,239,247,0,248,255,241],
[242,240,246,238,239,225,242,253,0,240,234],
[243,249,263,251,248,240,233,246,261,0,228],
[247,260,253,261,259,238,258,260,267,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,257,270,265,244,223,234,252,262,232],
[229,0,236,241,243,223,217,218,217,227,230],
[244,265,0,256,264,235,238,227,229,237,222],
[231,260,245,0,254,248,227,205,231,228,232],
[236,258,237,247,0,252,246,233,205,252,225],
[257,278,266,253,249,0,246,236,236,248,235],
[278,284,263,274,255,255,0,218,254,226,251],
[267,283,274,296,268,265,283,0,250,284,260],
[249,284,272,270,296,265,247,251,0,259,275],
[239,274,264,273,249,253,275,217,242,0,246],
[269,271,279,269,276,266,250,241,226,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,241,258,241,245,237,256,250,246,246],
[227,0,236,253,244,232,235,252,236,234,241],
[260,265,0,262,269,260,251,257,263,248,254],
[243,248,239,0,249,241,233,240,252,246,246],
[260,257,232,252,0,251,245,274,242,255,257],
[256,269,241,260,250,0,241,250,242,264,240],
[264,266,250,268,256,260,0,248,266,259,262],
[245,249,244,261,227,251,253,0,244,261,251],
[251,265,238,249,259,259,235,257,0,250,248],
[255,267,253,255,246,237,242,240,251,0,229],
[255,260,247,255,244,261,239,250,253,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,239,249,271,247,216,247,290,239,261],
[265,0,249,187,256,230,245,260,262,218,240],
[262,252,0,254,262,276,264,240,281,253,298],
[252,314,247,0,276,278,267,253,289,232,241],
[230,245,239,225,0,221,222,233,269,228,265],
[254,271,225,223,280,0,248,242,298,248,257],
[285,256,237,234,279,253,0,275,285,235,243],
[254,241,261,248,268,259,226,0,261,220,280],
[211,239,220,212,232,203,216,240,0,211,242],
[262,283,248,269,273,253,266,281,290,0,273],
[240,261,203,260,236,244,258,221,259,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,243,219,231,249,273,274,250,249,225],
[246,0,239,222,254,244,248,266,268,243,242],
[258,262,0,245,251,251,276,283,270,261,229],
[282,279,256,0,277,237,278,277,265,238,250],
[270,247,250,224,0,237,256,278,284,236,228],
[252,257,250,264,264,0,266,280,259,204,226],
[228,253,225,223,245,235,0,227,232,227,223],
[227,235,218,224,223,221,274,0,255,205,243],
[251,233,231,236,217,242,269,246,0,220,215],
[252,258,240,263,265,297,274,296,281,0,263],
[276,259,272,251,273,275,278,258,286,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,189,230,244,234,250,236,257,261,274],
[229,0,258,192,219,264,248,227,271,267,260],
[312,243,0,289,262,267,276,267,263,298,290],
[271,309,212,0,267,273,325,221,316,247,303],
[257,282,239,234,0,283,225,220,309,262,275],
[267,237,234,228,218,0,280,243,291,244,281],
[251,253,225,176,276,221,0,222,272,212,265],
[265,274,234,280,281,258,279,0,294,231,262],
[244,230,238,185,192,210,229,207,0,221,221],
[240,234,203,254,239,257,289,270,280,0,301],
[227,241,211,198,226,220,236,239,280,200,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,173,168,146,178,196,212,154,206,186],
[274,0,210,195,201,209,224,179,147,225,199],
[328,291,0,226,224,198,224,272,171,272,253],
[333,306,275,0,215,263,289,245,200,284,279],
[355,300,277,286,0,190,269,259,257,221,245],
[323,292,303,238,311,0,290,262,256,228,243],
[305,277,277,212,232,211,0,234,220,229,282],
[289,322,229,256,242,239,267,0,216,266,225],
[347,354,330,301,244,245,281,285,0,275,261],
[295,276,229,217,280,273,272,235,226,0,235],
[315,302,248,222,256,258,219,276,240,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,246,194,227,244,235,267,222,258,236],
[260,0,214,239,192,289,214,212,200,239,207],
[255,287,0,231,226,255,252,275,265,242,226],
[307,262,270,0,208,262,256,263,266,172,266],
[274,309,275,293,0,246,295,303,221,316,237],
[257,212,246,239,255,0,242,201,238,242,221],
[266,287,249,245,206,259,0,241,227,283,225],
[234,289,226,238,198,300,260,0,223,298,217],
[279,301,236,235,280,263,274,278,0,304,286],
[243,262,259,329,185,259,218,203,197,0,246],
[265,294,275,235,264,280,276,284,215,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,305,237,233,243,261,211,172,305,260,236],
[196,0,172,162,259,211,171,221,293,245,196],
[264,329,0,265,285,280,203,259,301,322,300],
[268,339,236,0,266,281,240,236,306,296,259],
[258,242,216,235,0,303,271,299,270,341,243],
[240,290,221,220,198,0,259,228,247,290,202],
[290,330,298,261,230,242,0,286,275,332,296],
[329,280,242,265,202,273,215,0,314,258,209],
[196,208,200,195,231,254,226,187,0,279,191],
[241,256,179,205,160,211,169,243,222,0,220],
[265,305,201,242,258,299,205,292,310,281,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,206,223,255,247,261,250,280,254,280,171],
[295,0,254,280,256,259,253,281,273,263,213],
[278,247,0,264,242,292,254,321,254,295,276],
[246,221,237,0,229,205,222,231,227,292,170],
[254,245,259,272,0,247,210,270,215,253,253],
[240,242,209,296,254,0,212,247,257,286,206],
[251,248,247,279,291,289,0,322,242,277,290],
[221,220,180,270,231,254,179,0,211,236,166],
[247,228,247,274,286,244,259,290,0,299,255],
[221,238,206,209,248,215,224,265,202,0,211],
[330,288,225,331,248,295,211,335,246,290,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,243,245,261,249,253,253,273,252,268],
[245,0,255,253,264,262,252,249,259,254,257],
[258,246,0,254,268,255,246,244,265,244,250],
[256,248,247,0,264,244,251,236,244,240,253],
[240,237,233,237,0,241,246,235,244,242,238],
[252,239,246,257,260,0,247,241,242,247,255],
[248,249,255,250,255,254,0,242,248,255,258],
[248,252,257,265,266,260,259,0,266,268,269],
[228,242,236,257,257,259,253,235,0,238,251],
[249,247,257,261,259,254,246,233,263,0,268],
[233,244,251,248,263,246,243,232,250,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,254,272,262,265,254,259,277,255,267],
[254,0,224,267,261,250,235,271,271,257,262],
[247,277,0,264,263,258,255,268,266,276,272],
[229,234,237,0,244,245,259,254,266,247,250],
[239,240,238,257,0,255,237,234,241,242,247],
[236,251,243,256,246,0,251,236,255,257,247],
[247,266,246,242,264,250,0,246,259,251,251],
[242,230,233,247,267,265,255,0,267,243,268],
[224,230,235,235,260,246,242,234,0,254,238],
[246,244,225,254,259,244,250,258,247,0,259],
[234,239,229,251,254,254,250,233,263,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,245,254,243,224,253,226,255,249,248],
[253,0,259,263,238,242,242,245,253,241,240],
[256,242,0,234,204,232,243,237,237,223,255],
[247,238,267,0,237,250,256,246,238,230,235],
[258,263,297,264,0,247,256,251,288,262,268],
[277,259,269,251,254,0,263,271,260,233,263],
[248,259,258,245,245,238,0,234,253,228,237],
[275,256,264,255,250,230,267,0,266,240,259],
[246,248,264,263,213,241,248,235,0,207,269],
[252,260,278,271,239,268,273,261,294,0,266],
[253,261,246,266,233,238,264,242,232,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,246,259,246,262,236,259,265,253,263],
[276,0,265,274,286,268,250,272,279,263,273],
[255,236,0,266,244,248,247,242,254,253,257],
[242,227,235,0,244,255,255,248,248,256,253],
[255,215,257,257,0,252,233,253,255,267,263],
[239,233,253,246,249,0,240,236,244,256,256],
[265,251,254,246,268,261,0,272,265,260,275],
[242,229,259,253,248,265,229,0,240,235,253],
[236,222,247,253,246,257,236,261,0,252,244],
[248,238,248,245,234,245,241,266,249,0,245],
[238,228,244,248,238,245,226,248,257,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,238,218,244,216,218,221,252,228,218],
[267,0,239,243,266,229,262,250,268,239,256],
[263,262,0,257,297,251,293,256,258,214,270],
[283,258,244,0,275,254,283,257,277,249,279],
[257,235,204,226,0,232,233,255,255,253,247],
[285,272,250,247,269,0,274,262,275,257,270],
[283,239,208,218,268,227,0,237,248,249,258],
[280,251,245,244,246,239,264,0,265,247,243],
[249,233,243,224,246,226,253,236,0,237,215],
[273,262,287,252,248,244,252,254,264,0,247],
[283,245,231,222,254,231,243,258,286,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,253,263,297,258,263,263,245,281,254],
[252,0,274,266,269,255,267,277,264,259,250],
[248,227,0,246,246,249,251,279,250,258,276],
[238,235,255,0,258,215,248,271,270,243,267],
[204,232,255,243,0,236,244,259,244,245,253],
[243,246,252,286,265,0,239,281,263,258,262],
[238,234,250,253,257,262,0,251,249,249,270],
[238,224,222,230,242,220,250,0,263,242,257],
[256,237,251,231,257,238,252,238,0,251,258],
[220,242,243,258,256,243,252,259,250,0,269],
[247,251,225,234,248,239,231,244,243,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,279,321,279,324,265,240,303,252,229,233],
[222,0,297,242,275,192,196,286,217,240,196],
[180,204,0,216,212,224,172,216,211,205,208],
[222,259,285,0,281,286,205,262,264,230,274],
[177,226,289,220,0,189,193,228,175,197,209],
[236,309,277,215,312,0,244,284,238,203,220],
[261,305,329,296,308,257,0,323,241,289,295],
[198,215,285,239,273,217,178,0,232,228,215],
[249,284,290,237,326,263,260,269,0,230,206],
[272,261,296,271,304,298,212,273,271,0,234],
[268,305,293,227,292,281,206,286,295,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,247,241,243,242,246,235,245,239,262],
[250,0,267,258,243,249,252,241,246,262,262],
[254,234,0,239,240,256,246,240,241,251,250],
[260,243,262,0,247,248,262,252,258,257,252],
[258,258,261,254,0,254,253,245,249,251,258],
[259,252,245,253,247,0,255,252,246,242,264],
[255,249,255,239,248,246,0,245,249,245,255],
[266,260,261,249,256,249,256,0,260,255,249],
[256,255,260,243,252,255,252,241,0,258,255],
[262,239,250,244,250,259,256,246,243,0,242],
[239,239,251,249,243,237,246,252,246,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,30,167,122,331,289,211,141,44,150],
[501,0,226,322,259,348,322,211,414,198,320],
[471,275,0,303,275,317,320,329,275,179,318],
[334,179,198,0,301,303,197,209,197,198,362],
[379,242,226,200,0,242,322,209,214,196,240],
[170,153,184,198,259,0,320,207,153,154,198],
[212,179,181,304,179,181,0,346,195,196,223],
[290,290,172,292,292,294,155,0,290,274,290],
[360,87,226,304,287,348,306,211,0,224,318],
[457,303,322,303,305,347,305,227,277,0,442],
[351,181,183,139,261,303,278,211,183,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,244,265,257,259,260,259,238,260,253],
[254,0,247,269,276,285,268,257,252,273,247],
[257,254,0,269,245,285,264,262,252,252,241],
[236,232,232,0,252,256,234,253,231,238,232],
[244,225,256,249,0,261,243,239,237,244,219],
[242,216,216,245,240,0,240,236,222,244,221],
[241,233,237,267,258,261,0,244,242,243,227],
[242,244,239,248,262,265,257,0,243,242,233],
[263,249,249,270,264,279,259,258,0,268,235],
[241,228,249,263,257,257,258,259,233,0,229],
[248,254,260,269,282,280,274,268,266,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,345,245,220,175,292,158,189,232,241],
[272,0,245,289,241,206,255,195,258,223,270],
[156,256,0,212,202,226,235,147,219,208,217],
[256,212,289,0,192,210,272,170,293,211,244],
[281,260,299,309,0,267,289,298,323,249,270],
[326,295,275,291,234,0,352,282,352,283,255],
[209,246,266,229,212,149,0,224,291,231,213],
[343,306,354,331,203,219,277,0,336,279,255],
[312,243,282,208,178,149,210,165,0,227,179],
[269,278,293,290,252,218,270,222,274,0,183],
[260,231,284,257,231,246,288,246,322,318,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,234,252,243,257,233,246,241,243,248],
[241,0,233,242,228,247,226,230,236,233,239],
[267,268,0,258,235,265,248,243,257,259,259],
[249,259,243,0,242,260,254,236,253,254,254],
[258,273,266,259,0,277,262,259,264,248,260],
[244,254,236,241,224,0,240,245,242,232,254],
[268,275,253,247,239,261,0,263,248,240,250],
[255,271,258,265,242,256,238,0,254,253,257],
[260,265,244,248,237,259,253,247,0,256,255],
[258,268,242,247,253,269,261,248,245,0,255],
[253,262,242,247,241,247,251,244,246,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,236,254,230,252,252,237,277,250,257],
[247,0,254,241,230,247,231,236,284,237,267],
[265,247,0,264,253,250,253,254,288,235,272],
[247,260,237,0,219,260,232,237,241,235,254],
[271,271,248,282,0,274,259,261,283,274,271],
[249,254,251,241,227,0,247,235,262,233,236],
[249,270,248,269,242,254,0,248,279,256,286],
[264,265,247,264,240,266,253,0,274,255,272],
[224,217,213,260,218,239,222,227,0,216,244],
[251,264,266,266,227,268,245,246,285,0,266],
[244,234,229,247,230,265,215,229,257,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,248,241,242,226,244,244,222,255,238],
[273,0,255,265,253,246,251,255,241,249,257],
[253,246,0,243,244,231,237,251,222,246,238],
[260,236,258,0,261,244,242,244,234,238,242],
[259,248,257,240,0,236,252,246,233,253,247],
[275,255,270,257,265,0,247,246,241,245,255],
[257,250,264,259,249,254,0,251,260,248,264],
[257,246,250,257,255,255,250,0,228,243,237],
[279,260,279,267,268,260,241,273,0,267,269],
[246,252,255,263,248,256,253,258,234,0,245],
[263,244,263,259,254,246,237,264,232,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,293,241,301,293,277,311,295,283,269,277],
[208,0,238,266,238,264,224,233,229,209,313],
[260,263,0,278,255,238,253,259,252,257,311],
[200,235,223,0,285,250,262,224,278,220,282],
[208,263,246,216,0,239,251,234,217,262,300],
[224,237,263,251,262,0,245,247,264,245,315],
[190,277,248,239,250,256,0,235,206,188,316],
[206,268,242,277,267,254,266,0,248,223,321],
[218,272,249,223,284,237,295,253,0,226,281],
[232,292,244,281,239,256,313,278,275,0,312],
[224,188,190,219,201,186,185,180,220,189,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,315,292,248,297,286,279,303,275,305,276],
[186,0,264,228,262,256,220,264,213,234,240],
[209,237,0,239,244,234,216,229,197,244,203],
[253,273,262,0,272,286,263,295,256,277,235],
[204,239,257,229,0,274,247,268,194,232,240],
[215,245,267,215,227,0,232,279,209,258,192],
[222,281,285,238,254,269,0,285,237,262,240],
[198,237,272,206,233,222,216,0,204,255,185],
[226,288,304,245,307,292,264,297,0,306,258],
[196,267,257,224,269,243,239,246,195,0,231],
[225,261,298,266,261,309,261,316,243,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,244,270,254,248,274,239,251,242,237],
[262,0,250,246,242,245,249,236,254,250,236],
[257,251,0,268,256,261,283,242,256,233,246],
[231,255,233,0,236,242,279,228,244,234,224],
[247,259,245,265,0,241,264,231,255,251,259],
[253,256,240,259,260,0,255,225,224,239,237],
[227,252,218,222,237,246,0,204,241,224,230],
[262,265,259,273,270,276,297,0,257,249,253],
[250,247,245,257,246,277,260,244,0,244,247],
[259,251,268,267,250,262,277,252,257,0,259],
[264,265,255,277,242,264,271,248,254,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,252,275,246,242,274,262,267,254,228],
[238,0,225,253,222,208,243,248,237,243,239],
[249,276,0,266,243,246,261,253,242,256,229],
[226,248,235,0,226,219,224,263,224,241,225],
[255,279,258,275,0,260,265,302,245,281,235],
[259,293,255,282,241,0,242,244,249,250,233],
[227,258,240,277,236,259,0,260,226,269,261],
[239,253,248,238,199,257,241,0,212,248,251],
[234,264,259,277,256,252,275,289,0,264,256],
[247,258,245,260,220,251,232,253,237,0,239],
[273,262,272,276,266,268,240,250,245,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,266,267,259,270,263,250,266,264,256],
[240,0,255,247,242,269,252,256,260,248,249],
[235,246,0,252,250,247,245,253,243,254,242],
[234,254,249,0,257,256,243,257,269,245,241],
[242,259,251,244,0,263,236,245,262,256,240],
[231,232,254,245,238,0,247,234,239,241,241],
[238,249,256,258,265,254,0,247,245,250,246],
[251,245,248,244,256,267,254,0,242,260,245],
[235,241,258,232,239,262,256,259,0,242,243],
[237,253,247,256,245,260,251,241,259,0,242],
[245,252,259,260,261,260,255,256,258,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,237,242,238,250,256,250,231,245,244],
[262,0,251,238,245,250,252,251,239,239,236],
[264,250,0,279,240,249,243,261,240,256,242],
[259,263,222,0,244,247,261,261,232,264,244],
[263,256,261,257,0,269,242,261,274,259,242],
[251,251,252,254,232,0,255,249,251,234,239],
[245,249,258,240,259,246,0,267,250,247,234],
[251,250,240,240,240,252,234,0,247,235,239],
[270,262,261,269,227,250,251,254,0,233,254],
[256,262,245,237,242,267,254,266,268,0,237],
[257,265,259,257,259,262,267,262,247,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,259,233,244,239,262,235,260,253,252],
[255,0,256,242,247,256,274,253,263,265,262],
[242,245,0,248,249,247,254,238,250,248,254],
[268,259,253,0,262,266,248,253,259,276,276],
[257,254,252,239,0,245,249,241,246,262,265],
[262,245,254,235,256,0,254,238,252,263,247],
[239,227,247,253,252,247,0,228,250,250,250],
[266,248,263,248,260,263,273,0,257,261,259],
[241,238,251,242,255,249,251,244,0,258,270],
[248,236,253,225,239,238,251,240,243,0,245],
[249,239,247,225,236,254,251,242,231,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,222,241,247,253,250,247,246,250,242],
[269,0,250,239,259,262,248,251,262,251,249],
[279,251,0,264,263,262,253,249,263,266,258],
[260,262,237,0,280,262,258,234,268,259,260],
[254,242,238,221,0,250,238,238,251,252,246],
[248,239,239,239,251,0,240,247,248,244,247],
[251,253,248,243,263,261,0,256,246,252,253],
[254,250,252,267,263,254,245,0,249,264,249],
[255,239,238,233,250,253,255,252,0,250,251],
[251,250,235,242,249,257,249,237,251,0,253],
[259,252,243,241,255,254,248,252,250,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,232,249,238,242,240,229,254,235,244],
[271,0,237,257,253,247,244,238,270,242,257],
[269,264,0,273,248,283,266,263,272,265,277],
[252,244,228,0,232,243,255,239,235,246,248],
[263,248,253,269,0,260,262,269,267,268,260],
[259,254,218,258,241,0,257,254,258,258,251],
[261,257,235,246,239,244,0,250,256,252,253],
[272,263,238,262,232,247,251,0,256,244,253],
[247,231,229,266,234,243,245,245,0,247,245],
[266,259,236,255,233,243,249,257,254,0,247],
[257,244,224,253,241,250,248,248,256,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,258,267,300,259,259,249,289,268,250],
[245,0,231,268,264,243,261,283,272,279,255],
[243,270,0,270,263,241,263,270,276,249,259],
[234,233,231,0,231,201,236,241,248,248,226],
[201,237,238,270,0,246,232,233,261,228,244],
[242,258,260,300,255,0,263,270,270,253,261],
[242,240,238,265,269,238,0,243,273,247,234],
[252,218,231,260,268,231,258,0,254,250,257],
[212,229,225,253,240,231,228,247,0,241,226],
[233,222,252,253,273,248,254,251,260,0,260],
[251,246,242,275,257,240,267,244,275,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,204,245,160,234,303,229,254,231,267],
[273,0,214,214,166,256,320,248,277,279,224],
[297,287,0,249,216,306,297,255,293,216,313],
[256,287,252,0,251,269,268,255,309,213,268],
[341,335,285,250,0,289,363,251,293,297,336],
[267,245,195,232,212,0,300,210,313,171,301],
[198,181,204,233,138,201,0,196,185,266,221],
[272,253,246,246,250,291,305,0,317,275,336],
[247,224,208,192,208,188,316,184,0,178,217],
[270,222,285,288,204,330,235,226,323,0,282],
[234,277,188,233,165,200,280,165,284,219,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,238,279,245,254,250,244,253,237,250],
[268,0,263,263,258,268,283,247,279,257,263],
[263,238,0,284,253,244,266,266,260,266,269],
[222,238,217,0,216,244,252,232,259,235,231],
[256,243,248,285,0,274,267,255,253,275,262],
[247,233,257,257,227,0,254,237,275,223,252],
[251,218,235,249,234,247,0,227,235,223,238],
[257,254,235,269,246,264,274,0,272,249,260],
[248,222,241,242,248,226,266,229,0,236,255],
[264,244,235,266,226,278,278,252,265,0,253],
[251,238,232,270,239,249,263,241,246,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,225,221,234,230,235,250,234,239,234],
[265,0,256,234,237,261,249,250,238,238,242],
[276,245,0,248,245,246,255,255,254,252,238],
[280,267,253,0,246,267,261,285,254,263,278],
[267,264,256,255,0,270,241,250,252,251,269],
[271,240,255,234,231,0,260,267,261,254,264],
[266,252,246,240,260,241,0,259,250,253,254],
[251,251,246,216,251,234,242,0,223,237,268],
[267,263,247,247,249,240,251,278,0,243,257],
[262,263,249,238,250,247,248,264,258,0,254],
[267,259,263,223,232,237,247,233,244,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,253,241,278,271,261,264,268,264,258],
[247,0,249,249,280,260,258,266,259,236,265],
[248,252,0,252,235,234,245,224,248,231,248],
[260,252,249,0,270,280,256,253,260,251,273],
[223,221,266,231,0,264,236,243,261,249,250],
[230,241,267,221,237,0,239,233,248,246,243],
[240,243,256,245,265,262,0,236,241,255,264],
[237,235,277,248,258,268,265,0,259,246,258],
[233,242,253,241,240,253,260,242,0,256,251],
[237,265,270,250,252,255,246,255,245,0,253],
[243,236,253,228,251,258,237,243,250,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,253,286,254,226,251,255,246,248,221],
[253,0,262,277,270,241,256,268,241,255,236],
[248,239,0,261,256,228,257,237,206,245,224],
[215,224,240,0,238,213,239,203,231,217,222],
[247,231,245,263,0,233,245,206,198,239,206],
[275,260,273,288,268,0,251,262,255,270,239],
[250,245,244,262,256,250,0,233,250,237,221],
[246,233,264,298,295,239,268,0,240,241,257],
[255,260,295,270,303,246,251,261,0,256,251],
[253,246,256,284,262,231,264,260,245,0,238],
[280,265,277,279,295,262,280,244,250,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,247,243,242,232,247,242,243,227,241],
[258,0,254,261,244,236,265,252,225,251,276],
[254,247,0,247,233,260,247,251,240,240,247],
[258,240,254,0,234,243,267,237,240,240,242],
[259,257,268,267,0,244,255,260,272,262,269],
[269,265,241,258,257,0,251,252,235,253,248],
[254,236,254,234,246,250,0,259,249,240,252],
[259,249,250,264,241,249,242,0,239,238,247],
[258,276,261,261,229,266,252,262,0,267,273],
[274,250,261,261,239,248,261,263,234,0,244],
[260,225,254,259,232,253,249,254,228,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,231,241,252,251,256,248,258,250,251],
[253,0,233,252,242,244,254,260,270,241,256],
[270,268,0,254,275,274,280,268,274,248,257],
[260,249,247,0,268,278,270,263,283,249,274],
[249,259,226,233,0,253,251,255,268,255,243],
[250,257,227,223,248,0,259,257,263,241,245],
[245,247,221,231,250,242,0,259,256,222,240],
[253,241,233,238,246,244,242,0,262,227,248],
[243,231,227,218,233,238,245,239,0,249,252],
[251,260,253,252,246,260,279,274,252,0,256],
[250,245,244,227,258,256,261,253,249,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,161,229,243,260,176,123,274,207,248,217],
[340,0,334,231,307,273,254,434,213,167,307],
[272,167,0,172,286,211,222,300,249,193,165],
[258,270,329,0,275,192,242,271,285,235,316],
[241,194,215,226,0,154,182,369,283,200,130],
[325,228,290,309,347,0,260,319,294,294,304],
[378,247,279,259,319,241,0,324,386,291,233],
[227,67,201,230,132,182,177,0,178,120,199],
[294,288,252,216,218,207,115,323,0,166,166],
[253,334,308,266,301,207,210,381,335,0,220],
[284,194,336,185,371,197,268,302,335,281,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,212,230,225,214,222,240,228,166,277,200],
[289,0,270,263,218,280,302,297,264,259,296],
[271,231,0,275,271,240,215,281,212,248,281],
[276,238,226,0,247,255,240,314,217,271,230],
[287,283,230,254,0,252,247,267,210,247,275],
[279,221,261,246,249,0,268,286,254,237,231],
[261,199,286,261,254,233,0,308,250,250,247],
[273,204,220,187,234,215,193,0,156,206,207],
[335,237,289,284,291,247,251,345,0,292,260],
[224,242,253,230,254,264,251,295,209,0,233],
[301,205,220,271,226,270,254,294,241,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,257,252,233,228,252,247,227,230,256],
[259,0,260,252,261,257,238,270,240,259,248],
[244,241,0,216,257,214,232,265,242,216,244],
[249,249,285,0,273,269,268,285,275,264,277],
[268,240,244,228,0,237,245,281,238,242,260],
[273,244,287,232,264,0,285,276,243,270,278],
[249,263,269,233,256,216,0,253,247,233,253],
[254,231,236,216,220,225,248,0,233,228,233],
[274,261,259,226,263,258,254,268,0,264,276],
[271,242,285,237,259,231,268,273,237,0,268],
[245,253,257,224,241,223,248,268,225,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,229,214,233,204,269,237,196,240,217],
[242,0,229,251,236,231,282,239,241,251,261],
[272,272,0,211,235,251,275,258,264,304,272],
[287,250,290,0,249,281,304,304,246,258,341],
[268,265,266,252,0,242,262,242,267,279,250],
[297,270,250,220,259,0,296,268,298,307,269],
[232,219,226,197,239,205,0,282,192,265,223],
[264,262,243,197,259,233,219,0,216,236,230],
[305,260,237,255,234,203,309,285,0,340,273],
[261,250,197,243,222,194,236,265,161,0,248],
[284,240,229,160,251,232,278,271,228,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,236,292,248,216,260,245,319,256,251],
[233,0,215,259,215,225,236,212,261,226,247],
[265,286,0,276,284,233,235,295,304,274,285],
[209,242,225,0,227,201,278,247,288,245,231],
[253,286,217,274,0,253,240,230,294,260,264],
[285,276,268,300,248,0,286,296,317,285,274],
[241,265,266,223,261,215,0,257,269,252,247],
[256,289,206,254,271,205,244,0,294,264,259],
[182,240,197,213,207,184,232,207,0,223,210],
[245,275,227,256,241,216,249,237,278,0,245],
[250,254,216,270,237,227,254,242,291,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,244,259,269,262,250,262,246,252,229],
[261,0,254,266,270,267,249,257,263,262,256],
[257,247,0,246,259,261,263,254,264,269,218],
[242,235,255,0,243,238,258,261,265,251,215],
[232,231,242,258,0,239,260,267,238,244,246],
[239,234,240,263,262,0,245,248,230,247,239],
[251,252,238,243,241,256,0,265,263,256,231],
[239,244,247,240,234,253,236,0,253,246,239],
[255,238,237,236,263,271,238,248,0,271,265],
[249,239,232,250,257,254,245,255,230,0,232],
[272,245,283,286,255,262,270,262,236,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,230,220,242,229,235,229,210,221,221],
[280,0,299,279,270,262,248,283,286,251,287],
[271,202,0,252,234,242,234,252,243,254,254],
[281,222,249,0,254,258,242,241,241,252,267],
[259,231,267,247,0,235,239,242,249,222,272],
[272,239,259,243,266,0,228,245,259,253,272],
[266,253,267,259,262,273,0,243,249,249,269],
[272,218,249,260,259,256,258,0,270,245,267],
[291,215,258,260,252,242,252,231,0,223,264],
[280,250,247,249,279,248,252,256,278,0,288],
[280,214,247,234,229,229,232,234,237,213,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,337,285,234,200,297,343,270,305,354,217],
[164,0,276,132,203,163,304,207,127,80,126],
[216,225,0,171,189,247,261,160,230,238,225],
[267,369,330,0,218,195,351,256,226,265,286],
[301,298,312,283,0,299,287,275,205,298,240],
[204,338,254,306,202,0,339,264,228,332,219],
[158,197,240,150,214,162,0,211,210,195,251],
[231,294,341,245,226,237,290,0,163,247,265],
[196,374,271,275,296,273,291,338,0,264,305],
[147,421,263,236,203,169,306,254,237,0,250],
[284,375,276,215,261,282,250,236,196,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,206,228,266,263,293,240,329,262,293,235],
[295,0,234,256,250,286,292,325,243,294,296],
[273,267,0,259,245,244,263,321,227,281,224],
[235,245,242,0,268,265,273,308,219,238,234],
[238,251,256,233,0,254,266,332,227,276,215],
[208,215,257,236,247,0,261,266,200,264,255],
[261,209,238,228,235,240,0,319,258,229,221],
[172,176,180,193,169,235,182,0,145,161,181],
[239,258,274,282,274,301,243,356,0,266,259],
[208,207,220,263,225,237,272,340,235,0,216],
[266,205,277,267,286,246,280,320,242,285,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,283,262,273,250,254,260,263,259,268],
[256,0,261,256,234,271,252,238,273,263,257],
[218,240,0,226,236,238,216,231,239,250,275],
[239,245,275,0,246,252,228,225,256,261,255],
[228,267,265,255,0,261,242,250,260,265,264],
[251,230,263,249,240,0,241,239,248,250,250],
[247,249,285,273,259,260,0,242,272,260,279],
[241,263,270,276,251,262,259,0,269,285,276],
[238,228,262,245,241,253,229,232,0,234,262],
[242,238,251,240,236,251,241,216,267,0,255],
[233,244,226,246,237,251,222,225,239,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,249,254,247,261,255,264,257,257,256],
[254,0,253,257,260,256,254,272,236,262,243],
[252,248,0,247,243,267,248,255,241,256,249],
[247,244,254,0,242,270,273,263,250,260,246],
[254,241,258,259,0,267,258,279,247,259,259],
[240,245,234,231,234,0,239,250,238,246,245],
[246,247,253,228,243,262,0,262,249,242,249],
[237,229,246,238,222,251,239,0,233,252,232],
[244,265,260,251,254,263,252,268,0,261,260],
[244,239,245,241,242,255,259,249,240,0,237],
[245,258,252,255,242,256,252,269,241,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,251,244,215,225,221,249,207,208,255],
[261,0,284,237,241,240,228,246,228,255,262],
[250,217,0,245,233,235,245,246,241,253,266],
[257,264,256,0,256,251,232,266,246,224,271],
[286,260,268,245,0,267,249,248,251,252,278],
[276,261,266,250,234,0,225,272,231,224,259],
[280,273,256,269,252,276,0,304,275,234,301],
[252,255,255,235,253,229,197,0,244,219,238],
[294,273,260,255,250,270,226,257,0,226,288],
[293,246,248,277,249,277,267,282,275,0,297],
[246,239,235,230,223,242,200,263,213,204,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,187,199,197,239,227,216,228,226,238,216],
[314,0,250,242,250,250,287,288,273,268,259],
[302,251,0,209,273,278,295,298,248,249,257],
[304,259,292,0,285,287,307,283,281,254,248],
[262,251,228,216,0,229,282,265,251,257,229],
[274,251,223,214,272,0,259,259,276,279,243],
[285,214,206,194,219,242,0,251,245,252,224],
[273,213,203,218,236,242,250,0,259,265,240],
[275,228,253,220,250,225,256,242,0,244,213],
[263,233,252,247,244,222,249,236,257,0,239],
[285,242,244,253,272,258,277,261,288,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,250,292,269,285,245,302,240,240,314],
[258,0,246,280,272,251,273,287,249,246,308],
[251,255,0,244,281,259,249,267,258,256,293],
[209,221,257,0,282,255,244,266,254,226,279],
[232,229,220,219,0,247,208,275,206,232,259],
[216,250,242,246,254,0,238,283,241,258,292],
[256,228,252,257,293,263,0,278,264,255,289],
[199,214,234,235,226,218,223,0,254,213,253],
[261,252,243,247,295,260,237,247,0,269,288],
[261,255,245,275,269,243,246,288,232,0,298],
[187,193,208,222,242,209,212,248,213,203,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,238,243,238,254,253,249,248,254,232],
[257,0,248,245,249,269,257,266,247,277,250],
[263,253,0,244,240,253,260,251,252,255,244],
[258,256,257,0,248,269,265,258,249,245,239],
[263,252,261,253,0,267,261,275,253,250,253],
[247,232,248,232,234,0,242,252,237,253,222],
[248,244,241,236,240,259,0,240,236,261,240],
[252,235,250,243,226,249,261,0,242,244,241],
[253,254,249,252,248,264,265,259,0,261,241],
[247,224,246,256,251,248,240,257,240,0,240],
[269,251,257,262,248,279,261,260,260,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,278,290,252,337,316,292,284,303,384],
[266,0,387,280,236,398,178,379,305,414,392],
[223,114,0,209,193,229,229,262,231,316,355],
[211,221,292,0,166,288,91,309,243,279,364],
[249,265,308,335,0,344,298,342,351,414,408],
[164,103,272,213,157,0,173,292,173,243,269],
[185,323,272,410,203,328,0,270,278,353,429],
[209,122,239,192,159,209,231,0,165,229,265],
[217,196,270,258,150,328,223,336,0,292,401],
[198,87,185,222,87,258,148,272,209,0,358],
[117,109,146,137,93,232,72,236,100,143,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,242,292,269,227,317,201,248,268,302],
[247,0,225,266,219,216,249,232,208,261,203],
[259,276,0,329,234,201,308,262,260,284,303],
[209,235,172,0,227,134,344,197,153,222,235],
[232,282,267,274,0,228,272,269,163,320,240],
[274,285,300,367,273,0,312,322,223,322,264],
[184,252,193,157,229,189,0,220,229,170,213],
[300,269,239,304,232,179,281,0,128,257,287],
[253,293,241,348,338,278,272,373,0,371,228],
[233,240,217,279,181,179,331,244,130,0,315],
[199,298,198,266,261,237,288,214,273,186,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,246,220,235,233,242,232,246,237,229],
[254,0,242,232,257,250,238,264,230,229,227],
[255,259,0,244,232,255,260,270,244,258,265],
[281,269,257,0,249,257,272,266,284,262,243],
[266,244,269,252,0,269,283,266,264,253,239],
[268,251,246,244,232,0,259,255,238,248,225],
[259,263,241,229,218,242,0,244,257,252,237],
[269,237,231,235,235,246,257,0,240,245,233],
[255,271,257,217,237,263,244,261,0,248,230],
[264,272,243,239,248,253,249,256,253,0,237],
[272,274,236,258,262,276,264,268,271,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,239,230,237,209,184,222,276,231,245],
[280,0,262,244,255,211,267,299,321,240,288],
[262,239,0,266,217,241,241,226,272,251,261],
[271,257,235,0,246,238,206,247,261,255,279],
[264,246,284,255,0,219,257,210,284,275,286],
[292,290,260,263,282,0,244,290,314,292,299],
[317,234,260,295,244,257,0,258,291,277,274],
[279,202,275,254,291,211,243,0,273,294,294],
[225,180,229,240,217,187,210,228,0,242,228],
[270,261,250,246,226,209,224,207,259,0,265],
[256,213,240,222,215,202,227,207,273,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,315,216,161,285,262,265,331,106,263,197],
[186,0,274,238,219,257,129,333,162,249,180],
[285,227,0,212,225,278,299,260,152,132,109],
[340,263,289,0,356,259,279,319,188,260,283],
[216,282,276,145,0,264,143,274,161,149,179],
[239,244,223,242,237,0,108,276,147,190,199],
[236,372,202,222,358,393,0,332,220,193,126],
[170,168,241,182,227,225,169,0,33,77,95],
[395,339,349,313,340,354,281,468,0,247,302],
[238,252,369,241,352,311,308,424,254,0,294],
[304,321,392,218,322,302,375,406,199,207,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,251,259,248,254,264,256,255,267,258],
[245,0,250,265,248,246,259,265,259,266,263],
[250,251,0,255,245,252,252,259,237,259,253],
[242,236,246,0,256,240,257,256,233,247,236],
[253,253,256,245,0,255,260,249,237,253,249],
[247,255,249,261,246,0,280,263,246,251,258],
[237,242,249,244,241,221,0,257,230,233,257],
[245,236,242,245,252,238,244,0,237,234,243],
[246,242,264,268,264,255,271,264,0,260,268],
[234,235,242,254,248,250,268,267,241,0,255],
[243,238,248,265,252,243,244,258,233,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,244,248,262,241,251,261,285,273,271],
[232,0,247,261,260,290,245,251,264,247,241],
[257,254,0,243,249,253,243,236,281,259,270],
[253,240,258,0,249,266,256,242,271,266,255],
[239,241,252,252,0,264,246,251,276,251,257],
[260,211,248,235,237,0,222,246,246,262,242],
[250,256,258,245,255,279,0,257,270,281,266],
[240,250,265,259,250,255,244,0,292,251,281],
[216,237,220,230,225,255,231,209,0,238,236],
[228,254,242,235,250,239,220,250,263,0,270],
[230,260,231,246,244,259,235,220,265,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,273,263,253,242,272,250,223,247,260],
[256,0,245,268,243,254,284,240,253,263,250],
[228,256,0,256,220,227,237,229,226,211,225],
[238,233,245,0,230,235,232,225,244,230,255],
[248,258,281,271,0,271,266,254,256,260,278],
[259,247,274,266,230,0,268,252,243,262,251],
[229,217,264,269,235,233,0,227,230,236,272],
[251,261,272,276,247,249,274,0,261,256,276],
[278,248,275,257,245,258,271,240,0,279,255],
[254,238,290,271,241,239,265,245,222,0,271],
[241,251,276,246,223,250,229,225,246,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,256,251,266,244,255,246,255,261,267],
[249,0,241,221,266,257,240,264,254,241,259],
[245,260,0,233,270,235,246,253,274,260,263],
[250,280,268,0,269,256,247,262,269,269,261],
[235,235,231,232,0,232,233,250,231,252,251],
[257,244,266,245,269,0,251,253,264,249,254],
[246,261,255,254,268,250,0,265,259,280,265],
[255,237,248,239,251,248,236,0,258,250,245],
[246,247,227,232,270,237,242,243,0,223,278],
[240,260,241,232,249,252,221,251,278,0,267],
[234,242,238,240,250,247,236,256,223,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,240,248,240,251,257,244,270,246,286],
[234,0,232,243,220,239,242,226,248,233,264],
[261,269,0,271,264,250,263,263,279,248,276],
[253,258,230,0,241,249,228,234,254,233,272],
[261,281,237,260,0,240,239,251,241,229,261],
[250,262,251,252,261,0,243,253,260,252,267],
[244,259,238,273,262,258,0,239,249,248,275],
[257,275,238,267,250,248,262,0,279,258,282],
[231,253,222,247,260,241,252,222,0,229,261],
[255,268,253,268,272,249,253,243,272,0,286],
[215,237,225,229,240,234,226,219,240,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,257,246,265,261,274,267,258,254,267],
[249,0,249,246,244,249,255,242,231,225,263],
[244,252,0,242,249,246,274,249,244,246,265],
[255,255,259,0,263,248,258,259,247,251,262],
[236,257,252,238,0,257,258,255,252,253,273],
[240,252,255,253,244,0,264,246,235,245,253],
[227,246,227,243,243,237,0,235,230,237,264],
[234,259,252,242,246,255,266,0,252,251,257],
[243,270,257,254,249,266,271,249,0,257,246],
[247,276,255,250,248,256,264,250,244,0,262],
[234,238,236,239,228,248,237,244,255,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,238,236,223,236,239,225,233,244,197],
[265,0,234,272,236,249,261,286,258,276,239],
[263,267,0,286,243,267,240,261,265,255,228],
[265,229,215,0,214,230,231,242,233,235,228],
[278,265,258,287,0,266,239,266,263,290,259],
[265,252,234,271,235,0,226,261,251,250,249],
[262,240,261,270,262,275,0,270,255,267,237],
[276,215,240,259,235,240,231,0,224,247,221],
[268,243,236,268,238,250,246,277,0,258,209],
[257,225,246,266,211,251,234,254,243,0,238],
[304,262,273,273,242,252,264,280,292,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,268,249,244,240,252,237,271,241,239],
[245,0,262,240,255,268,266,248,265,239,267],
[233,239,0,242,235,235,243,235,262,239,236],
[252,261,259,0,242,260,242,252,271,255,258],
[257,246,266,259,0,260,243,249,271,235,244],
[261,233,266,241,241,0,246,237,262,233,236],
[249,235,258,259,258,255,0,244,256,224,239],
[264,253,266,249,252,264,257,0,260,262,265],
[230,236,239,230,230,239,245,241,0,233,238],
[260,262,262,246,266,268,277,239,268,0,242],
[262,234,265,243,257,265,262,236,263,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,233,275,264,182,283,300,252,149,342],
[234,0,182,243,178,270,238,199,249,236,278],
[268,319,0,218,211,219,246,293,334,219,272],
[226,258,283,0,251,229,308,287,226,258,378],
[237,323,290,250,0,313,233,310,341,245,298],
[319,231,282,272,188,0,263,297,304,197,359],
[218,263,255,193,268,238,0,280,282,260,326],
[201,302,208,214,191,204,221,0,290,232,276],
[249,252,167,275,160,197,219,211,0,204,317],
[352,265,282,243,256,304,241,269,297,0,342],
[159,223,229,123,203,142,175,225,184,159,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,292,250,255,226,263,250,202,298,236,256],
[209,0,232,231,216,219,266,196,201,213,221],
[251,269,0,259,265,226,270,247,254,257,230],
[246,270,242,0,237,221,252,218,252,213,210],
[275,285,236,264,0,220,266,238,254,240,253],
[238,282,275,280,281,0,270,223,247,247,258],
[251,235,231,249,235,231,0,211,226,216,228],
[299,305,254,283,263,278,290,0,285,221,250],
[203,300,247,249,247,254,275,216,0,236,227],
[265,288,244,288,261,254,285,280,265,0,298],
[245,280,271,291,248,243,273,251,274,203,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,248,281,251,255,246,243,244,253,257],
[243,0,247,264,253,239,232,230,246,251,259],
[253,254,0,272,261,262,251,251,241,259,256],
[220,237,229,0,239,231,230,224,243,251,231],
[250,248,240,262,0,244,250,241,248,257,263],
[246,262,239,270,257,0,237,233,256,265,253],
[255,269,250,271,251,264,0,250,246,266,247],
[258,271,250,277,260,268,251,0,249,259,261],
[257,255,260,258,253,245,255,252,0,253,260],
[248,250,242,250,244,236,235,242,248,0,251],
[244,242,245,270,238,248,254,240,241,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,246,239,238,242,255,242,239,232,245],
[265,0,250,267,245,260,243,238,259,254,251],
[255,251,0,259,262,250,228,228,238,248,266],
[262,234,242,0,244,251,237,234,246,244,257],
[263,256,239,257,0,246,246,261,251,239,259],
[259,241,251,250,255,0,257,243,244,254,244],
[246,258,273,264,255,244,0,242,250,253,256],
[259,263,273,267,240,258,259,0,248,242,277],
[262,242,263,255,250,257,251,253,0,244,262],
[269,247,253,257,262,247,248,259,257,0,261],
[256,250,235,244,242,257,245,224,239,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,298,290,273,248,267,312,276,240,274],
[224,0,277,245,239,237,280,269,248,251,286],
[203,224,0,213,222,232,252,270,235,216,257],
[211,256,288,0,225,241,258,256,253,237,253],
[228,262,279,276,0,245,283,281,260,254,280],
[253,264,269,260,256,0,260,276,244,231,279],
[234,221,249,243,218,241,0,257,239,213,238],
[189,232,231,245,220,225,244,0,223,221,237],
[225,253,266,248,241,257,262,278,0,229,273],
[261,250,285,264,247,270,288,280,272,0,267],
[227,215,244,248,221,222,263,264,228,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,257,280,265,252,251,258,254,244,275],
[252,0,250,271,257,238,237,250,254,239,264],
[244,251,0,262,258,252,239,246,254,243,264],
[221,230,239,0,252,233,218,239,243,226,246],
[236,244,243,249,0,246,241,244,254,241,268],
[249,263,249,268,255,0,256,261,266,242,275],
[250,264,262,283,260,245,0,265,251,261,282],
[243,251,255,262,257,240,236,0,257,235,259],
[247,247,247,258,247,235,250,244,0,246,270],
[257,262,258,275,260,259,240,266,255,0,266],
[226,237,237,255,233,226,219,242,231,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,253,256,249,266,255,268,252,243,269],
[251,0,241,235,242,248,240,270,245,238,268],
[248,260,0,250,248,260,266,256,259,247,274],
[245,266,251,0,250,254,260,264,247,252,269],
[252,259,253,251,0,249,247,261,245,243,264],
[235,253,241,247,252,0,261,257,252,239,280],
[246,261,235,241,254,240,0,265,243,248,268],
[233,231,245,237,240,244,236,0,238,251,255],
[249,256,242,254,256,249,258,263,0,244,274],
[258,263,254,249,258,262,253,250,257,0,263],
[232,233,227,232,237,221,233,246,227,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,242,253,275,250,228,237,223,257,250],
[272,0,278,295,293,269,251,267,268,272,248],
[259,223,0,251,313,230,254,234,253,225,252],
[248,206,250,0,251,234,250,216,240,262,231],
[226,208,188,250,0,221,210,210,219,225,203],
[251,232,271,267,280,0,216,231,254,268,239],
[273,250,247,251,291,285,0,267,272,262,255],
[264,234,267,285,291,270,234,0,261,247,241],
[278,233,248,261,282,247,229,240,0,247,249],
[244,229,276,239,276,233,239,254,254,0,222],
[251,253,249,270,298,262,246,260,252,279,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,314,246,250,251,269,271,255,265,248],
[248,0,306,239,254,259,262,260,229,250,253],
[187,195,0,198,207,177,206,229,217,230,204],
[255,262,303,0,278,248,279,266,262,252,268],
[251,247,294,223,0,255,276,252,264,243,248],
[250,242,324,253,246,0,284,258,262,294,270],
[232,239,295,222,225,217,0,280,219,241,261],
[230,241,272,235,249,243,221,0,229,244,236],
[246,272,284,239,237,239,282,272,0,258,242],
[236,251,271,249,258,207,260,257,243,0,252],
[253,248,297,233,253,231,240,265,259,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,193,210,263,273,253,228,282,205,180],
[228,0,203,219,281,250,226,234,295,236,211],
[308,298,0,288,286,307,301,259,283,241,275],
[291,282,213,0,292,278,296,273,269,235,252],
[238,220,215,209,0,277,242,257,256,232,241],
[228,251,194,223,224,0,255,219,259,237,196],
[248,275,200,205,259,246,0,241,254,217,226],
[273,267,242,228,244,282,260,0,278,225,230],
[219,206,218,232,245,242,247,223,0,198,207],
[296,265,260,266,269,264,284,276,303,0,239],
[321,290,226,249,260,305,275,271,294,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,249,255,229,251,241,228,234,248,233],
[272,0,243,254,264,252,235,249,263,262,276],
[252,258,0,255,231,247,184,235,236,266,234],
[246,247,246,0,222,262,217,230,233,269,262],
[272,237,270,279,0,284,255,246,274,292,299],
[250,249,254,239,217,0,217,253,251,251,275],
[260,266,317,284,246,284,0,263,277,279,274],
[273,252,266,271,255,248,238,0,270,272,272],
[267,238,265,268,227,250,224,231,0,265,258],
[253,239,235,232,209,250,222,229,236,0,251],
[268,225,267,239,202,226,227,229,243,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,256,248,255,300,235,254,274,251,236],
[232,0,238,206,221,217,224,197,236,210,198],
[245,263,0,223,261,245,242,230,256,225,240],
[253,295,278,0,260,279,270,229,253,251,247],
[246,280,240,241,0,231,227,228,221,220,237],
[201,284,256,222,270,0,232,244,216,241,238],
[266,277,259,231,274,269,0,214,264,236,264],
[247,304,271,272,273,257,287,0,245,237,234],
[227,265,245,248,280,285,237,256,0,260,256],
[250,291,276,250,281,260,265,264,241,0,245],
[265,303,261,254,264,263,237,267,245,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,273,244,263,264,252,253,254,262,271],
[229,0,234,233,242,251,237,219,238,239,229],
[228,267,0,234,227,257,220,209,229,234,240],
[257,268,267,0,263,285,253,249,244,264,261],
[238,259,274,238,0,267,236,252,232,274,261],
[237,250,244,216,234,0,235,239,235,256,250],
[249,264,281,248,265,266,0,251,256,259,280],
[248,282,292,252,249,262,250,0,268,270,285],
[247,263,272,257,269,266,245,233,0,271,269],
[239,262,267,237,227,245,242,231,230,0,247],
[230,272,261,240,240,251,221,216,232,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,274,238,285,248,233,302,229,262,202],
[228,0,216,287,218,213,239,228,233,275,274],
[227,285,0,283,267,246,332,272,289,319,270],
[263,214,218,0,221,209,281,232,225,274,217],
[216,283,234,280,0,246,278,279,264,273,241],
[253,288,255,292,255,0,281,280,221,293,262],
[268,262,169,220,223,220,0,270,256,260,216],
[199,273,229,269,222,221,231,0,249,269,190],
[272,268,212,276,237,280,245,252,0,254,230],
[239,226,182,227,228,208,241,232,247,0,188],
[299,227,231,284,260,239,285,311,271,313,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,238,246,232,257,248,250,232,256,254],
[255,0,238,249,260,258,255,263,245,270,263],
[263,263,0,269,250,263,283,274,240,269,270],
[255,252,232,0,242,265,253,264,247,247,249],
[269,241,251,259,0,268,263,271,253,271,261],
[244,243,238,236,233,0,265,270,239,264,243],
[253,246,218,248,238,236,0,246,224,254,231],
[251,238,227,237,230,231,255,0,231,275,244],
[269,256,261,254,248,262,277,270,0,274,248],
[245,231,232,254,230,237,247,226,227,0,231],
[247,238,231,252,240,258,270,257,253,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,246,275,256,226,280,224,253,249,264],
[267,0,245,251,250,229,270,237,256,255,237],
[255,256,0,259,256,231,274,235,253,253,267],
[226,250,242,0,252,225,263,231,225,234,251],
[245,251,245,249,0,216,267,226,251,254,253],
[275,272,270,276,285,0,290,247,278,284,266],
[221,231,227,238,234,211,0,223,229,215,232],
[277,264,266,270,275,254,278,0,267,249,265],
[248,245,248,276,250,223,272,234,0,255,248],
[252,246,248,267,247,217,286,252,246,0,255],
[237,264,234,250,248,235,269,236,253,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,240,240,262,257,239,265,254,258,259],
[256,0,254,237,267,261,241,285,270,271,255],
[261,247,0,236,272,256,248,254,256,272,258],
[261,264,265,0,264,260,248,278,257,275,265],
[239,234,229,237,0,239,223,246,249,252,227],
[244,240,245,241,262,0,242,252,261,274,244],
[262,260,253,253,278,259,0,271,259,259,249],
[236,216,247,223,255,249,230,0,247,254,240],
[247,231,245,244,252,240,242,254,0,263,249],
[243,230,229,226,249,227,242,247,238,0,231],
[242,246,243,236,274,257,252,261,252,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,245,232,248,253,247,246,237,245,247],
[254,0,265,249,262,249,253,245,252,252,255],
[256,236,0,243,244,250,246,241,235,235,237],
[269,252,258,0,257,259,241,255,258,252,253],
[253,239,257,244,0,250,258,256,242,240,250],
[248,252,251,242,251,0,241,257,238,243,261],
[254,248,255,260,243,260,0,242,265,245,253],
[255,256,260,246,245,244,259,0,254,250,246],
[264,249,266,243,259,263,236,247,0,246,244],
[256,249,266,249,261,258,256,251,255,0,263],
[254,246,264,248,251,240,248,255,257,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,298,267,283,286,280,280,261,282,249],
[231,0,282,285,262,228,256,301,272,261,271],
[203,219,0,235,262,214,227,227,215,232,227],
[234,216,266,0,215,256,256,259,241,273,250],
[218,239,239,286,0,221,271,245,220,265,251],
[215,273,287,245,280,0,265,260,245,258,273],
[221,245,274,245,230,236,0,290,237,281,258],
[221,200,274,242,256,241,211,0,243,229,221],
[240,229,286,260,281,256,264,258,0,253,252],
[219,240,269,228,236,243,220,272,248,0,247],
[252,230,274,251,250,228,243,280,249,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,242,222,256,225,248,270,254,252,245],
[262,0,264,246,237,237,244,271,252,247,250],
[259,237,0,231,256,235,246,256,245,247,235],
[279,255,270,0,238,252,252,257,246,255,261],
[245,264,245,263,0,245,227,277,251,270,251],
[276,264,266,249,256,0,257,265,274,269,266],
[253,257,255,249,274,244,0,262,275,275,273],
[231,230,245,244,224,236,239,0,245,243,248],
[247,249,256,255,250,227,226,256,0,246,253],
[249,254,254,246,231,232,226,258,255,0,251],
[256,251,266,240,250,235,228,253,248,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,195,216,246,215,249,229,252,191,193,274],
[306,0,272,289,269,290,272,287,246,265,288],
[285,229,0,280,257,267,304,309,221,291,271],
[255,212,221,0,228,228,227,211,233,236,261],
[286,232,244,273,0,316,254,258,251,266,314],
[252,211,234,273,185,0,233,230,212,240,262],
[272,229,197,274,247,268,0,273,223,225,274],
[249,214,192,290,243,271,228,0,235,216,256],
[310,255,280,268,250,289,278,266,0,250,295],
[308,236,210,265,235,261,276,285,251,0,286],
[227,213,230,240,187,239,227,245,206,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,239,253,266,231,300,255,280,278,221],
[269,0,236,278,280,238,301,251,277,301,233],
[262,265,0,292,298,246,309,281,298,285,265],
[248,223,209,0,260,223,269,258,279,252,223],
[235,221,203,241,0,218,267,245,270,248,193],
[270,263,255,278,283,0,283,270,328,295,233],
[201,200,192,232,234,218,0,238,271,264,226],
[246,250,220,243,256,231,263,0,264,254,242],
[221,224,203,222,231,173,230,237,0,214,192],
[223,200,216,249,253,206,237,247,287,0,218],
[280,268,236,278,308,268,275,259,309,283,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,250,264,245,255,233,232,258,229,254],
[264,0,259,262,245,259,251,258,259,240,246],
[251,242,0,262,254,252,247,252,262,238,251],
[237,239,239,0,239,246,251,232,253,234,246],
[256,256,247,262,0,256,251,256,279,262,271],
[246,242,249,255,245,0,244,246,264,239,249],
[268,250,254,250,250,257,0,254,270,249,257],
[269,243,249,269,245,255,247,0,246,258,267],
[243,242,239,248,222,237,231,255,0,230,242],
[272,261,263,267,239,262,252,243,271,0,253],
[247,255,250,255,230,252,244,234,259,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,255,232,224,226,237,227,267,215,234],
[278,0,234,235,238,226,244,234,259,231,236],
[246,267,0,220,226,248,249,246,275,234,261],
[269,266,281,0,255,237,273,291,265,246,229],
[277,263,275,246,0,235,257,291,287,264,273],
[275,275,253,264,266,0,281,262,269,230,252],
[264,257,252,228,244,220,0,243,265,238,247],
[274,267,255,210,210,239,258,0,268,225,236],
[234,242,226,236,214,232,236,233,0,223,219],
[286,270,267,255,237,271,263,276,278,0,262],
[267,265,240,272,228,249,254,265,282,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,223,231,254,236,272,260,266,242,221],
[228,0,220,191,179,204,215,196,246,233,209],
[278,281,0,218,211,218,242,218,211,263,223],
[270,310,283,0,261,237,257,252,285,276,253],
[247,322,290,240,0,235,251,239,282,268,239],
[265,297,283,264,266,0,256,266,294,301,246],
[229,286,259,244,250,245,0,267,277,308,250],
[241,305,283,249,262,235,234,0,297,270,241],
[235,255,290,216,219,207,224,204,0,254,235],
[259,268,238,225,233,200,193,231,247,0,244],
[280,292,278,248,262,255,251,260,266,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,243,250,264,242,259,266,211,240,257],
[259,0,244,220,249,222,243,269,237,241,246],
[258,257,0,208,273,254,231,229,218,203,229],
[251,281,293,0,273,282,253,274,246,238,255],
[237,252,228,228,0,217,221,215,191,243,240],
[259,279,247,219,284,0,234,269,254,249,248],
[242,258,270,248,280,267,0,239,245,237,244],
[235,232,272,227,286,232,262,0,242,253,219],
[290,264,283,255,310,247,256,259,0,253,247],
[261,260,298,263,258,252,264,248,248,0,235],
[244,255,272,246,261,253,257,282,254,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,249,270,256,258,253,258,253,238,256],
[238,0,246,251,238,242,239,242,239,232,249],
[252,255,0,278,245,244,238,256,246,237,242],
[231,250,223,0,233,229,237,244,237,232,233],
[245,263,256,268,0,250,245,256,243,244,259],
[243,259,257,272,251,0,238,264,251,249,263],
[248,262,263,264,256,263,0,270,251,238,249],
[243,259,245,257,245,237,231,0,241,236,248],
[248,262,255,264,258,250,250,260,0,256,254],
[263,269,264,269,257,252,263,265,245,0,273],
[245,252,259,268,242,238,252,253,247,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,254,230,256,237,244,249,259,254,233],
[260,0,263,252,274,262,241,242,266,261,242],
[247,238,0,223,253,227,214,239,266,245,225],
[271,249,278,0,274,265,250,251,264,262,255],
[245,227,248,227,0,263,225,252,263,226,229],
[264,239,274,236,238,0,239,243,272,266,253],
[257,260,287,251,276,262,0,260,269,269,246],
[252,259,262,250,249,258,241,0,262,257,255],
[242,235,235,237,238,229,232,239,0,236,230],
[247,240,256,239,275,235,232,244,265,0,227],
[268,259,276,246,272,248,255,246,271,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,228,260,264,237,309,289,228,295,214],
[258,0,233,269,243,268,295,266,242,279,191],
[273,268,0,293,244,262,289,246,289,279,260],
[241,232,208,0,245,269,301,258,261,280,215],
[237,258,257,256,0,334,284,279,288,295,257],
[264,233,239,232,167,0,257,256,231,227,178],
[192,206,212,200,217,244,0,200,227,233,194],
[212,235,255,243,222,245,301,0,229,235,195],
[273,259,212,240,213,270,274,272,0,266,198],
[206,222,222,221,206,274,268,266,235,0,199],
[287,310,241,286,244,323,307,306,303,302,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,238,263,238,250,244,265,251,246,244],
[236,0,255,265,248,231,242,264,229,244,224],
[263,246,0,241,242,240,233,260,247,252,237],
[238,236,260,0,251,241,231,263,238,236,230],
[263,253,259,250,0,244,247,257,252,240,250],
[251,270,261,260,257,0,260,264,250,267,236],
[257,259,268,270,254,241,0,267,266,255,229],
[236,237,241,238,244,237,234,0,234,224,234],
[250,272,254,263,249,251,235,267,0,247,251],
[255,257,249,265,261,234,246,277,254,0,246],
[257,277,264,271,251,265,272,267,250,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,248,265,249,283,274,253,235,255,270],
[254,0,241,268,249,257,263,271,239,266,247],
[253,260,0,252,272,257,256,238,257,263,241],
[236,233,249,0,221,254,249,239,229,245,236],
[252,252,229,280,0,265,270,251,236,245,252],
[218,244,244,247,236,0,229,255,207,221,221],
[227,238,245,252,231,272,0,261,244,255,239],
[248,230,263,262,250,246,240,0,242,242,255],
[266,262,244,272,265,294,257,259,0,272,253],
[246,235,238,256,256,280,246,259,229,0,259],
[231,254,260,265,249,280,262,246,248,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,213,258,235,197,263,224,200,221,170],
[236,0,216,276,220,184,252,285,247,255,221],
[288,285,0,240,289,222,321,271,275,294,205],
[243,225,261,0,255,261,293,274,254,242,233],
[266,281,212,246,0,248,341,284,253,245,221],
[304,317,279,240,253,0,316,263,269,279,247],
[238,249,180,208,160,185,0,247,181,227,212],
[277,216,230,227,217,238,254,0,232,244,190],
[301,254,226,247,248,232,320,269,0,282,258],
[280,246,207,259,256,222,274,257,219,0,195],
[331,280,296,268,280,254,289,311,243,306,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,266,270,258,233,238,262,274,244,264],
[243,0,275,261,271,251,260,270,280,265,255],
[235,226,0,247,260,225,221,237,258,235,235],
[231,240,254,0,252,246,233,265,268,241,258],
[243,230,241,249,0,237,234,256,261,237,256],
[268,250,276,255,264,0,231,260,270,269,249],
[263,241,280,268,267,270,0,275,282,252,275],
[239,231,264,236,245,241,226,0,262,246,253],
[227,221,243,233,240,231,219,239,0,226,247],
[257,236,266,260,264,232,249,255,275,0,245],
[237,246,266,243,245,252,226,248,254,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 501, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_11_501.csv", index=False, header=False)