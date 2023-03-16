
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,253,265,254,251,241,247,248,265,251],
[248,0,259,228,234,244,237,260,259,256],
[236,242,0,223,247,236,216,226,249,244],
[247,273,278,0,251,260,252,262,275,252],
[250,267,254,250,0,247,257,262,267,253],
[260,257,265,241,254,0,246,256,255,255],
[254,264,285,249,244,255,0,250,250,267],
[253,241,275,239,239,245,251,0,252,261],
[236,242,252,226,234,246,251,249,0,242],
[250,245,257,249,248,246,234,240,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,242,237,250,242,255,217,228,235],
[262,0,268,251,264,257,257,243,265,236],
[259,233,0,248,245,227,235,230,225,232],
[264,250,253,0,265,261,260,256,245,251],
[251,237,256,236,0,267,252,245,249,262],
[259,244,274,240,234,0,265,238,258,245],
[246,244,266,241,249,236,0,245,249,240],
[284,258,271,245,256,263,256,0,256,231],
[273,236,276,256,252,243,252,245,0,255],
[266,265,269,250,239,256,261,270,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,259,248,244,231,215,234,232,239],
[276,0,275,264,264,252,258,248,253,255],
[242,226,0,248,232,217,222,250,232,229],
[253,237,253,0,241,236,222,249,252,246],
[257,237,269,260,0,243,232,229,256,220],
[270,249,284,265,258,0,240,258,258,255],
[286,243,279,279,269,261,0,260,261,258],
[267,253,251,252,272,243,241,0,254,251],
[269,248,269,249,245,243,240,247,0,254],
[262,246,272,255,281,246,243,250,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,268,223,234,299,220,238,248,234],
[249,0,230,223,207,250,250,230,218,255],
[233,271,0,193,227,258,239,231,238,238],
[278,278,308,0,251,301,249,296,252,283],
[267,294,274,250,0,311,232,303,225,279],
[202,251,243,200,190,0,183,209,202,205],
[281,251,262,252,269,318,0,277,230,253],
[263,271,270,205,198,292,224,0,240,267],
[253,283,263,249,276,299,271,261,0,278],
[267,246,263,218,222,296,248,234,223,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,285,264,283,259,296,271,240,252],
[252,0,259,247,257,261,244,243,264,236],
[216,242,0,239,264,254,224,229,238,242],
[237,254,262,0,291,269,273,268,273,251],
[218,244,237,210,0,240,231,223,228,216],
[242,240,247,232,261,0,259,236,242,223],
[205,257,277,228,270,242,0,252,253,239],
[230,258,272,233,278,265,249,0,267,254],
[261,237,263,228,273,259,248,234,0,248],
[249,265,259,250,285,278,262,247,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,230,241,257,251,238,229,257,239],
[269,0,237,260,255,251,253,249,262,261],
[271,264,0,254,269,264,245,255,266,246],
[260,241,247,0,250,255,264,246,258,250],
[244,246,232,251,0,250,255,246,254,243],
[250,250,237,246,251,0,244,244,257,249],
[263,248,256,237,246,257,0,256,253,243],
[272,252,246,255,255,257,245,0,256,236],
[244,239,235,243,247,244,248,245,0,246],
[262,240,255,251,258,252,258,265,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,252,244,237,244,247,243,244,256],
[252,0,248,245,254,235,247,240,258,269],
[249,253,0,252,248,244,254,255,248,265],
[257,256,249,0,250,253,249,261,258,265],
[264,247,253,251,0,242,252,251,250,253],
[257,266,257,248,259,0,264,269,262,254],
[254,254,247,252,249,237,0,264,248,266],
[258,261,246,240,250,232,237,0,242,249],
[257,243,253,243,251,239,253,259,0,239],
[245,232,236,236,248,247,235,252,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,253,274,260,250,268,239,252,278],
[244,0,244,243,264,228,232,237,235,247],
[248,257,0,257,261,243,257,232,247,279],
[227,258,244,0,245,255,257,241,245,271],
[241,237,240,256,0,237,231,251,229,256],
[251,273,258,246,264,0,268,245,277,281],
[233,269,244,244,270,233,0,247,253,273],
[262,264,269,260,250,256,254,0,238,263],
[249,266,254,256,272,224,248,263,0,260],
[223,254,222,230,245,220,228,238,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,249,243,249,262,238,210,232,249],
[266,0,261,252,241,251,228,246,239,251],
[252,240,0,258,241,262,256,252,238,240],
[258,249,243,0,249,250,256,237,254,260],
[252,260,260,252,0,261,261,239,240,240],
[239,250,239,251,240,0,249,219,257,253],
[263,273,245,245,240,252,0,230,247,245],
[291,255,249,264,262,282,271,0,265,261],
[269,262,263,247,261,244,254,236,0,262],
[252,250,261,241,261,248,256,240,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,236,257,256,247,249,240,264,253],
[269,0,261,255,265,265,266,244,276,264],
[265,240,0,257,274,261,259,255,280,267],
[244,246,244,0,261,265,255,235,263,256],
[245,236,227,240,0,236,238,223,253,235],
[254,236,240,236,265,0,251,234,245,258],
[252,235,242,246,263,250,0,236,251,242],
[261,257,246,266,278,267,265,0,281,274],
[237,225,221,238,248,256,250,220,0,246],
[248,237,234,245,266,243,259,227,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,255,292,224,262,263,257,266,257],
[252,0,205,257,267,214,294,266,285,244],
[246,296,0,261,264,229,262,175,282,278],
[209,244,240,0,250,214,258,240,271,259],
[277,234,237,251,0,253,295,261,323,278],
[239,287,272,287,248,0,270,241,261,295],
[238,207,239,243,206,231,0,246,247,229],
[244,235,326,261,240,260,255,0,294,280],
[235,216,219,230,178,240,254,207,0,251],
[244,257,223,242,223,206,272,221,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,247,250,242,228,254,253,201,244],
[272,0,243,263,243,241,273,264,233,270],
[254,258,0,244,228,221,248,253,230,278],
[251,238,257,0,242,243,246,256,238,251],
[259,258,273,259,0,247,250,288,255,262],
[273,260,280,258,254,0,268,274,246,265],
[247,228,253,255,251,233,0,262,242,261],
[248,237,248,245,213,227,239,0,221,257],
[300,268,271,263,246,255,259,280,0,271],
[257,231,223,250,239,236,240,244,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,246,249,256,256,240,242,229,246],
[271,0,261,279,266,267,261,251,248,266],
[255,240,0,260,265,261,247,251,251,250],
[252,222,241,0,246,249,235,231,219,251],
[245,235,236,255,0,249,235,238,227,233],
[245,234,240,252,252,0,235,241,214,244],
[261,240,254,266,266,266,0,247,238,261],
[259,250,250,270,263,260,254,0,231,243],
[272,253,250,282,274,287,263,270,0,259],
[255,235,251,250,268,257,240,258,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,267,293,260,242,257,300,274,255],
[227,0,241,233,240,245,252,279,226,248],
[234,260,0,249,239,246,229,259,244,224],
[208,268,252,0,242,258,250,279,243,227],
[241,261,262,259,0,228,258,288,268,230],
[259,256,255,243,273,0,251,268,248,247],
[244,249,272,251,243,250,0,244,271,259],
[201,222,242,222,213,233,257,0,228,222],
[227,275,257,258,233,253,230,273,0,248],
[246,253,277,274,271,254,242,279,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,261,237,259,251,257,280,264,286],
[229,0,251,224,239,242,246,264,246,277],
[240,250,0,235,251,238,242,265,239,261],
[264,277,266,0,245,248,248,300,251,266],
[242,262,250,256,0,244,249,264,233,249],
[250,259,263,253,257,0,240,285,247,277],
[244,255,259,253,252,261,0,280,233,270],
[221,237,236,201,237,216,221,0,214,247],
[237,255,262,250,268,254,268,287,0,281],
[215,224,240,235,252,224,231,254,220,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,271,253,255,271,276,235,263,265],
[225,0,245,240,252,235,260,232,243,250],
[230,256,0,253,253,240,242,238,256,260],
[248,261,248,0,269,253,252,251,258,264],
[246,249,248,232,0,243,266,227,225,252],
[230,266,261,248,258,0,252,251,263,250],
[225,241,259,249,235,249,0,236,246,255],
[266,269,263,250,274,250,265,0,286,255],
[238,258,245,243,276,238,255,215,0,255],
[236,251,241,237,249,251,246,246,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,248,273,256,236,269,251,274,231],
[234,0,259,261,269,236,242,265,256,250],
[253,242,0,269,268,241,266,265,273,232],
[228,240,232,0,238,221,260,245,251,227],
[245,232,233,263,0,224,263,253,273,241],
[265,265,260,280,277,0,264,250,276,253],
[232,259,235,241,238,237,0,242,226,232],
[250,236,236,256,248,251,259,0,264,244],
[227,245,228,250,228,225,275,237,0,260],
[270,251,269,274,260,248,269,257,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,300,262,289,249,271,224,292,270],
[224,0,288,266,311,230,259,323,263,277],
[201,213,0,206,260,198,205,244,246,194],
[239,235,295,0,305,228,236,229,239,232],
[212,190,241,196,0,207,198,226,270,243],
[252,271,303,273,294,0,240,282,286,227],
[230,242,296,265,303,261,0,269,249,247],
[277,178,257,272,275,219,232,0,228,217],
[209,238,255,262,231,215,252,273,0,221],
[231,224,307,269,258,274,254,284,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,249,263,254,252,246,254,249,237],
[250,0,267,267,269,262,241,250,272,251],
[252,234,0,250,264,253,255,251,254,255],
[238,234,251,0,257,257,249,233,229,243],
[247,232,237,244,0,240,235,225,254,246],
[249,239,248,244,261,0,244,235,256,240],
[255,260,246,252,266,257,0,247,259,259],
[247,251,250,268,276,266,254,0,267,253],
[252,229,247,272,247,245,242,234,0,247],
[264,250,246,258,255,261,242,248,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,303,215,276,312,234,230,192,227,235],
[198,0,206,168,205,202,200,154,209,171],
[286,295,0,232,288,200,273,202,281,228],
[225,333,269,0,316,208,278,234,260,225],
[189,296,213,185,0,176,215,161,167,176],
[267,299,301,293,325,0,273,252,215,256],
[271,301,228,223,286,228,0,204,191,207],
[309,347,299,267,340,249,297,0,256,220],
[274,292,220,241,334,286,310,245,0,252],
[266,330,273,276,325,245,294,281,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,278,252,246,253,264,269,292,265],
[258,0,296,247,268,233,293,271,302,276],
[223,205,0,225,240,204,214,252,246,233],
[249,254,276,0,275,241,260,278,282,257],
[255,233,261,226,0,261,226,256,252,228],
[248,268,297,260,240,0,263,274,278,263],
[237,208,287,241,275,238,0,234,259,254],
[232,230,249,223,245,227,267,0,227,228],
[209,199,255,219,249,223,242,274,0,245],
[236,225,268,244,273,238,247,273,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,329,270,319,319,242,321,300,292,284],
[172,0,221,206,259,241,245,250,250,221],
[231,280,0,258,328,270,259,237,238,190],
[182,295,243,0,236,320,261,235,241,289],
[182,242,173,265,0,275,222,242,271,249],
[259,260,231,181,226,0,227,201,235,214],
[180,256,242,240,279,274,0,223,181,181],
[201,251,264,266,259,300,278,0,213,186],
[209,251,263,260,230,266,320,288,0,229],
[217,280,311,212,252,287,320,315,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,248,245,259,219,265,246,250,232],
[245,0,227,218,239,226,241,216,224,223],
[253,274,0,248,264,254,279,251,241,237],
[256,283,253,0,258,250,264,246,260,248],
[242,262,237,243,0,230,249,245,233,244],
[282,275,247,251,271,0,261,264,251,249],
[236,260,222,237,252,240,0,238,244,225],
[255,285,250,255,256,237,263,0,234,257],
[251,277,260,241,268,250,257,267,0,247],
[269,278,264,253,257,252,276,244,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,261,254,265,242,260,237,261,252],
[229,0,235,248,260,253,246,236,247,245],
[240,266,0,247,261,246,241,276,247,255],
[247,253,254,0,259,238,258,238,245,237],
[236,241,240,242,0,232,242,243,244,245],
[259,248,255,263,269,0,247,244,250,249],
[241,255,260,243,259,254,0,257,253,245],
[264,265,225,263,258,257,244,0,251,242],
[240,254,254,256,257,251,248,250,0,241],
[249,256,246,264,256,252,256,259,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,242,261,246,254,259,230,255,228],
[249,0,265,271,260,262,245,257,260,250],
[259,236,0,259,239,259,253,236,248,241],
[240,230,242,0,239,256,239,245,237,234],
[255,241,262,262,0,270,248,231,259,259],
[247,239,242,245,231,0,260,216,249,231],
[242,256,248,262,253,241,0,242,241,249],
[271,244,265,256,270,285,259,0,248,269],
[246,241,253,264,242,252,260,253,0,248],
[273,251,260,267,242,270,252,232,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,269,267,267,245,257,265,273,260],
[251,0,254,250,235,238,261,273,269,248],
[232,247,0,264,244,248,258,241,276,263],
[234,251,237,0,233,244,241,247,239,239],
[234,266,257,268,0,262,266,261,272,249],
[256,263,253,257,239,0,272,261,263,250],
[244,240,243,260,235,229,0,257,277,241],
[236,228,260,254,240,240,244,0,251,231],
[228,232,225,262,229,238,224,250,0,239],
[241,253,238,262,252,251,260,270,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,260,249,249,258,247,261,251,254],
[263,0,268,265,257,242,260,243,246,241],
[241,233,0,244,248,235,244,252,242,239],
[252,236,257,0,243,240,239,255,231,246],
[252,244,253,258,0,253,253,269,248,258],
[243,259,266,261,248,0,263,268,254,268],
[254,241,257,262,248,238,0,256,253,251],
[240,258,249,246,232,233,245,0,248,246],
[250,255,259,270,253,247,248,253,0,259],
[247,260,262,255,243,233,250,255,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,294,260,249,255,216,262,220,252],
[247,0,293,234,237,245,223,284,227,265],
[207,208,0,244,192,192,198,246,198,258],
[241,267,257,0,229,232,213,264,238,261],
[252,264,309,272,0,261,252,313,250,293],
[246,256,309,269,240,0,235,286,247,255],
[285,278,303,288,249,266,0,303,269,293],
[239,217,255,237,188,215,198,0,176,228],
[281,274,303,263,251,254,232,325,0,312],
[249,236,243,240,208,246,208,273,189,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,257,261,257,255,244,273,268,247],
[254,0,244,247,263,250,245,272,256,247],
[244,257,0,256,267,263,237,258,256,256],
[240,254,245,0,262,247,253,265,255,270],
[244,238,234,239,0,237,244,271,252,241],
[246,251,238,254,264,0,239,263,266,247],
[257,256,264,248,257,262,0,266,269,270],
[228,229,243,236,230,238,235,0,247,243],
[233,245,245,246,249,235,232,254,0,258],
[254,254,245,231,260,254,231,258,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,252,261,253,258,253,258,292,295],
[278,0,265,254,239,263,264,253,270,299],
[249,236,0,235,253,243,259,236,255,270],
[240,247,266,0,267,264,253,253,230,268],
[248,262,248,234,0,264,247,239,252,269],
[243,238,258,237,237,0,243,246,235,269],
[248,237,242,248,254,258,0,236,257,256],
[243,248,265,248,262,255,265,0,246,294],
[209,231,246,271,249,266,244,255,0,291],
[206,202,231,233,232,232,245,207,210,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,213,230,252,221,238,218,261,238,234],
[288,0,256,257,277,301,250,256,284,262],
[271,245,0,236,262,264,242,273,240,237],
[249,244,265,0,249,262,229,253,229,245],
[280,224,239,252,0,259,253,274,235,223],
[263,200,237,239,242,0,243,263,240,243],
[283,251,259,272,248,258,0,261,259,247],
[240,245,228,248,227,238,240,0,255,232],
[263,217,261,272,266,261,242,246,0,255],
[267,239,264,256,278,258,254,269,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,294,303,274,264,245,286,268,255],
[224,0,244,275,242,246,246,280,241,241],
[207,257,0,263,267,233,238,236,254,227],
[198,226,238,0,228,219,224,250,221,222],
[227,259,234,273,0,215,225,231,222,221],
[237,255,268,282,286,0,241,258,260,237],
[256,255,263,277,276,260,0,274,249,260],
[215,221,265,251,270,243,227,0,255,250],
[233,260,247,280,279,241,252,246,0,263],
[246,260,274,279,280,264,241,251,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,257,280,244,261,254,264,270,268],
[229,0,247,260,262,241,230,242,265,246],
[244,254,0,259,248,251,244,244,245,250],
[221,241,242,0,244,246,241,239,247,255],
[257,239,253,257,0,264,241,247,268,241],
[240,260,250,255,237,0,249,236,268,248],
[247,271,257,260,260,252,0,250,274,260],
[237,259,257,262,254,265,251,0,269,239],
[231,236,256,254,233,233,227,232,0,240],
[233,255,251,246,260,253,241,262,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,273,251,265,256,275,222,300,222],
[252,0,221,216,279,241,293,221,282,260],
[228,280,0,187,208,272,241,238,219,208],
[250,285,314,0,290,330,298,269,248,266],
[236,222,293,211,0,274,237,247,278,223],
[245,260,229,171,227,0,288,218,214,165],
[226,208,260,203,264,213,0,287,247,279],
[279,280,263,232,254,283,214,0,221,181],
[201,219,282,253,223,287,254,280,0,252],
[279,241,293,235,278,336,222,320,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,275,200,243,229,188,250,236,240],
[249,0,262,227,274,238,221,272,214,222],
[226,239,0,246,274,231,236,257,242,256],
[301,274,255,0,275,257,246,282,253,252],
[258,227,227,226,0,220,207,232,220,209],
[272,263,270,244,281,0,225,266,248,255],
[313,280,265,255,294,276,0,291,254,248],
[251,229,244,219,269,235,210,0,226,241],
[265,287,259,248,281,253,247,275,0,253],
[261,279,245,249,292,246,253,260,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,208,254,252,241,251,254,213,187],
[254,0,230,262,258,272,252,238,216,239],
[293,271,0,262,261,257,302,301,199,236],
[247,239,239,0,250,213,233,293,216,217],
[249,243,240,251,0,223,215,238,216,192],
[260,229,244,288,278,0,264,254,208,232],
[250,249,199,268,286,237,0,266,232,215],
[247,263,200,208,263,247,235,0,201,252],
[288,285,302,285,285,293,269,300,0,247],
[314,262,265,284,309,269,286,249,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,255,258,263,245,248,241,255,250],
[231,0,241,246,236,232,253,239,242,238],
[246,260,0,259,267,251,250,259,246,250],
[243,255,242,0,255,233,253,242,248,232],
[238,265,234,246,0,239,245,238,242,246],
[256,269,250,268,262,0,263,268,251,263],
[253,248,251,248,256,238,0,242,241,247],
[260,262,242,259,263,233,259,0,242,256],
[246,259,255,253,259,250,260,259,0,238],
[251,263,251,269,255,238,254,245,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,203,261,226,207,220,211,224,212,216],
[298,0,278,254,256,264,229,242,251,269],
[240,223,0,227,231,205,187,231,234,218],
[275,247,274,0,207,244,205,258,261,265],
[294,245,270,294,0,261,218,256,250,271],
[281,237,296,257,240,0,226,243,277,266],
[290,272,314,296,283,275,0,306,239,288],
[277,259,270,243,245,258,195,0,231,238],
[289,250,267,240,251,224,262,270,0,263],
[285,232,283,236,230,235,213,263,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,252,261,258,248,256,224,238,253],
[255,0,240,264,277,242,250,245,251,259],
[249,261,0,265,272,256,248,253,252,251],
[240,237,236,0,257,242,255,237,232,246],
[243,224,229,244,0,233,234,240,237,231],
[253,259,245,259,268,0,241,246,257,249],
[245,251,253,246,267,260,0,245,251,256],
[277,256,248,264,261,255,256,0,270,268],
[263,250,249,269,264,244,250,231,0,256],
[248,242,250,255,270,252,245,233,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,269,267,242,240,256,256,271,262],
[237,0,246,260,219,253,243,243,248,250],
[232,255,0,236,234,231,242,238,254,232],
[234,241,265,0,241,242,249,247,247,257],
[259,282,267,260,0,259,240,265,282,260],
[261,248,270,259,242,0,263,259,269,270],
[245,258,259,252,261,238,0,262,259,259],
[245,258,263,254,236,242,239,0,267,248],
[230,253,247,254,219,232,242,234,0,247],
[239,251,269,244,241,231,242,253,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,251,262,246,256,249,257,243,253],
[265,0,268,238,251,248,251,269,269,256],
[250,233,0,252,246,250,239,253,266,254],
[239,263,249,0,260,255,247,268,273,261],
[255,250,255,241,0,236,245,273,276,260],
[245,253,251,246,265,0,243,247,267,248],
[252,250,262,254,256,258,0,269,253,257],
[244,232,248,233,228,254,232,0,249,243],
[258,232,235,228,225,234,248,252,0,247],
[248,245,247,240,241,253,244,258,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,239,289,292,259,321,281,334,251],
[257,0,243,286,287,186,309,277,326,270],
[262,258,0,249,298,274,270,273,306,270],
[212,215,252,0,221,227,263,219,264,247],
[209,214,203,280,0,246,298,271,315,249],
[242,315,227,274,255,0,312,282,336,297],
[180,192,231,238,203,189,0,224,276,201],
[220,224,228,282,230,219,277,0,271,214],
[167,175,195,237,186,165,225,230,0,188],
[250,231,231,254,252,204,300,287,313,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,234,239,234,253,223,230,248,256],
[269,0,275,253,269,256,237,243,267,274],
[267,226,0,224,218,249,205,228,243,256],
[262,248,277,0,217,258,227,255,252,265],
[267,232,283,284,0,262,259,249,265,292],
[248,245,252,243,239,0,233,230,246,247],
[278,264,296,274,242,268,0,256,269,273],
[271,258,273,246,252,271,245,0,269,275],
[253,234,258,249,236,255,232,232,0,265],
[245,227,245,236,209,254,228,226,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,255,251,260,241,262,252,275,255],
[223,0,242,240,237,246,248,253,253,244],
[246,259,0,244,263,234,266,280,261,271],
[250,261,257,0,255,251,263,271,275,253],
[241,264,238,246,0,245,255,255,257,257],
[260,255,267,250,256,0,263,251,260,242],
[239,253,235,238,246,238,0,254,254,243],
[249,248,221,230,246,250,247,0,249,245],
[226,248,240,226,244,241,247,252,0,230],
[246,257,230,248,244,259,258,256,271,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,253,261,276,250,252,251,260,273],
[240,0,242,255,254,246,233,247,238,245],
[248,259,0,257,266,239,252,247,260,277],
[240,246,244,0,251,239,248,245,233,248],
[225,247,235,250,0,241,238,239,229,242],
[251,255,262,262,260,0,252,267,242,258],
[249,268,249,253,263,249,0,255,241,257],
[250,254,254,256,262,234,246,0,246,253],
[241,263,241,268,272,259,260,255,0,277],
[228,256,224,253,259,243,244,248,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,237,236,245,236,243,235,264,249],
[270,0,246,239,255,258,265,267,274,247],
[264,255,0,262,243,236,263,261,265,244],
[265,262,239,0,228,242,250,229,277,249],
[256,246,258,273,0,232,254,255,266,244],
[265,243,265,259,269,0,252,275,287,261],
[258,236,238,251,247,249,0,254,268,241],
[266,234,240,272,246,226,247,0,279,264],
[237,227,236,224,235,214,233,222,0,234],
[252,254,257,252,257,240,260,237,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,247,246,242,260,251,258,262,254],
[262,0,247,252,258,258,259,249,250,265],
[254,254,0,266,250,253,263,256,265,272],
[255,249,235,0,242,248,234,239,252,243],
[259,243,251,259,0,249,249,260,258,247],
[241,243,248,253,252,0,249,249,258,264],
[250,242,238,267,252,252,0,237,247,249],
[243,252,245,262,241,252,264,0,250,267],
[239,251,236,249,243,243,254,251,0,244],
[247,236,229,258,254,237,252,234,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,195,238,228,234,243,237,239,227],
[266,0,258,264,253,254,270,273,245,263],
[306,243,0,274,262,253,275,241,255,256],
[263,237,227,0,237,248,265,257,239,239],
[273,248,239,264,0,235,285,262,265,256],
[267,247,248,253,266,0,269,264,271,265],
[258,231,226,236,216,232,0,239,234,217],
[264,228,260,244,239,237,262,0,249,257],
[262,256,246,262,236,230,267,252,0,243],
[274,238,245,262,245,236,284,244,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,286,247,226,277,194,237,233,325],
[278,0,228,262,276,216,214,280,261,332],
[215,273,0,270,266,263,277,318,284,325],
[254,239,231,0,276,235,245,238,261,276],
[275,225,235,225,0,245,263,274,267,306],
[224,285,238,266,256,0,269,320,282,297],
[307,287,224,256,238,232,0,268,253,294],
[264,221,183,263,227,181,233,0,229,291],
[268,240,217,240,234,219,248,272,0,265],
[176,169,176,225,195,204,207,210,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,292,278,273,251,261,223,237,294,265],
[209,0,230,280,188,235,244,215,246,209],
[223,271,0,280,208,271,218,236,289,249],
[228,221,221,0,210,249,225,206,275,257],
[250,313,293,291,0,284,269,250,296,249],
[240,266,230,252,217,0,234,199,272,231],
[278,257,283,276,232,267,0,266,294,267],
[264,286,265,295,251,302,235,0,291,275],
[207,255,212,226,205,229,207,210,0,235],
[236,292,252,244,252,270,234,226,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,252,270,262,259,257,253,257,283],
[253,0,253,246,246,252,238,245,252,268],
[249,248,0,257,255,250,241,255,253,263],
[231,255,244,0,256,242,241,243,243,263],
[239,255,246,245,0,250,255,256,260,273],
[242,249,251,259,251,0,243,252,263,246],
[244,263,260,260,246,258,0,248,260,278],
[248,256,246,258,245,249,253,0,259,265],
[244,249,248,258,241,238,241,242,0,256],
[218,233,238,238,228,255,223,236,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,266,235,227,230,264,231,282,230],
[250,0,232,229,220,213,233,215,256,264],
[235,269,0,212,221,217,223,206,247,255],
[266,272,289,0,262,240,268,251,290,259],
[274,281,280,239,0,267,254,263,277,267],
[271,288,284,261,234,0,250,237,279,265],
[237,268,278,233,247,251,0,242,260,271],
[270,286,295,250,238,264,259,0,270,272],
[219,245,254,211,224,222,241,231,0,243],
[271,237,246,242,234,236,230,229,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,246,246,239,246,218,243,248,245],
[262,0,255,260,260,252,277,248,273,265],
[255,246,0,259,247,257,267,262,253,252],
[255,241,242,0,227,245,250,234,264,249],
[262,241,254,274,0,286,255,268,259,241],
[255,249,244,256,215,0,269,260,256,252],
[283,224,234,251,246,232,0,247,259,253],
[258,253,239,267,233,241,254,0,261,248],
[253,228,248,237,242,245,242,240,0,240],
[256,236,249,252,260,249,248,253,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,253,250,261,261,260,279,231,258],
[233,0,245,217,231,239,246,229,221,234],
[248,256,0,241,241,236,256,251,226,232],
[251,284,260,0,268,246,277,247,237,245],
[240,270,260,233,0,255,260,264,242,228],
[240,262,265,255,246,0,255,263,253,246],
[241,255,245,224,241,246,0,249,233,237],
[222,272,250,254,237,238,252,0,233,239],
[270,280,275,264,259,248,268,268,0,255],
[243,267,269,256,273,255,264,262,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,256,257,246,254,257,250,242,243],
[243,0,245,240,244,260,260,231,238,245],
[245,256,0,237,252,274,250,253,252,260],
[244,261,264,0,253,272,264,261,257,267],
[255,257,249,248,0,267,259,242,261,254],
[247,241,227,229,234,0,244,243,240,247],
[244,241,251,237,242,257,0,254,251,238],
[251,270,248,240,259,258,247,0,256,253],
[259,263,249,244,240,261,250,245,0,265],
[258,256,241,234,247,254,263,248,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,248,231,253,243,241,247,230,239],
[262,0,261,253,267,242,254,240,244,244],
[253,240,0,251,233,235,250,229,230,256],
[270,248,250,0,255,242,277,262,242,266],
[248,234,268,246,0,250,254,244,255,248],
[258,259,266,259,251,0,272,252,243,259],
[260,247,251,224,247,229,0,246,229,238],
[254,261,272,239,257,249,255,0,238,256],
[271,257,271,259,246,258,272,263,0,256],
[262,257,245,235,253,242,263,245,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,245,249,211,246,242,243,266,229],
[260,0,226,235,214,273,222,218,225,211],
[256,275,0,245,245,285,260,236,247,267],
[252,266,256,0,270,273,227,252,234,241],
[290,287,256,231,0,295,225,244,234,252],
[255,228,216,228,206,0,213,229,266,240],
[259,279,241,274,276,288,0,232,252,287],
[258,283,265,249,257,272,269,0,302,242],
[235,276,254,267,267,235,249,199,0,220],
[272,290,234,260,249,261,214,259,281,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,179,179,144,215,157,165,245,180],
[270,0,251,203,221,192,211,226,253,197],
[322,250,0,259,295,290,233,279,348,239],
[322,298,242,0,224,254,263,275,247,243],
[357,280,206,277,0,287,248,205,273,233],
[286,309,211,247,214,0,214,247,281,241],
[344,290,268,238,253,287,0,249,328,232],
[336,275,222,226,296,254,252,0,280,267],
[256,248,153,254,228,220,173,221,0,175],
[321,304,262,258,268,260,269,234,326,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,281,222,162,251,240,219,307,219,242],
[220,0,328,310,292,196,312,312,272,254],
[279,173,0,231,273,185,339,261,234,236],
[339,191,270,0,299,217,294,301,222,288],
[250,209,228,202,0,254,297,333,243,239],
[261,305,316,284,247,0,283,293,327,242],
[282,189,162,207,204,218,0,297,185,270],
[194,189,240,200,168,208,204,0,221,261],
[282,229,267,279,258,174,316,280,0,261],
[259,247,265,213,262,259,231,240,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,272,259,262,261,267,240,262,251],
[255,0,251,257,255,256,252,244,253,246],
[229,250,0,258,254,241,258,248,260,253],
[242,244,243,0,227,253,237,237,238,238],
[239,246,247,274,0,252,240,237,258,241],
[240,245,260,248,249,0,257,244,254,255],
[234,249,243,264,261,244,0,242,256,257],
[261,257,253,264,264,257,259,0,265,246],
[239,248,241,263,243,247,245,236,0,255],
[250,255,248,263,260,246,244,255,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,247,225,256,250,261,243,263,252],
[239,0,242,246,247,243,246,253,276,246],
[254,259,0,227,253,238,232,259,259,238],
[276,255,274,0,265,238,242,266,284,271],
[245,254,248,236,0,232,244,249,265,239],
[251,258,263,263,269,0,249,275,273,255],
[240,255,269,259,257,252,0,272,256,262],
[258,248,242,235,252,226,229,0,259,246],
[238,225,242,217,236,228,245,242,0,232],
[249,255,263,230,262,246,239,255,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,244,273,252,232,237,266,246,254],
[278,0,260,268,256,272,236,237,276,242],
[257,241,0,283,230,237,233,226,244,226],
[228,233,218,0,280,233,231,244,244,239],
[249,245,271,221,0,234,226,247,222,248],
[269,229,264,268,267,0,250,258,256,262],
[264,265,268,270,275,251,0,281,276,234],
[235,264,275,257,254,243,220,0,230,241],
[255,225,257,257,279,245,225,271,0,243],
[247,259,275,262,253,239,267,260,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,242,233,250,251,272,242,250,261],
[258,0,245,244,256,261,249,242,253,253],
[259,256,0,251,265,264,279,252,249,257],
[268,257,250,0,266,266,262,245,250,250],
[251,245,236,235,0,238,248,246,251,242],
[250,240,237,235,263,0,257,262,252,250],
[229,252,222,239,253,244,0,249,244,251],
[259,259,249,256,255,239,252,0,253,245],
[251,248,252,251,250,249,257,248,0,242],
[240,248,244,251,259,251,250,256,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,270,270,262,273,279,259,250,261],
[226,0,222,227,216,215,251,232,189,243],
[231,279,0,258,251,244,290,234,239,253],
[231,274,243,0,269,248,287,257,262,253],
[239,285,250,232,0,229,291,236,270,271],
[228,286,257,253,272,0,293,233,264,236],
[222,250,211,214,210,208,0,228,205,240],
[242,269,267,244,265,268,273,0,265,275],
[251,312,262,239,231,237,296,236,0,268],
[240,258,248,248,230,265,261,226,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,260,252,243,274,233,259,248,267],
[234,0,270,259,244,258,257,262,220,254],
[241,231,0,237,262,246,228,238,227,223],
[249,242,264,0,233,240,228,250,229,237],
[258,257,239,268,0,250,238,246,230,242],
[227,243,255,261,251,0,246,264,232,244],
[268,244,273,273,263,255,0,260,251,257],
[242,239,263,251,255,237,241,0,227,247],
[253,281,274,272,271,269,250,274,0,266],
[234,247,278,264,259,257,244,254,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,264,285,253,261,281,233,260,293],
[251,0,250,238,214,273,260,248,236,266],
[237,251,0,272,208,249,270,257,256,251],
[216,263,229,0,242,228,313,247,228,254],
[248,287,293,259,0,265,291,273,265,294],
[240,228,252,273,236,0,268,284,243,278],
[220,241,231,188,210,233,0,212,241,279],
[268,253,244,254,228,217,289,0,255,266],
[241,265,245,273,236,258,260,246,0,288],
[208,235,250,247,207,223,222,235,213,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,241,249,253,253,254,254,240,230],
[271,0,265,252,254,259,246,265,263,258],
[260,236,0,252,224,252,254,274,248,238],
[252,249,249,0,244,259,248,254,252,256],
[248,247,277,257,0,265,250,271,240,242],
[248,242,249,242,236,0,249,262,251,245],
[247,255,247,253,251,252,0,249,259,257],
[247,236,227,247,230,239,252,0,246,240],
[261,238,253,249,261,250,242,255,0,239],
[271,243,263,245,259,256,244,261,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,244,254,220,260,272,248,264,259],
[253,0,271,263,254,286,259,290,260,230],
[257,230,0,262,225,264,234,263,249,226],
[247,238,239,0,233,229,247,245,262,238],
[281,247,276,268,0,265,271,246,244,241],
[241,215,237,272,236,0,248,263,245,241],
[229,242,267,254,230,253,0,255,226,254],
[253,211,238,256,255,238,246,0,261,225],
[237,241,252,239,257,256,275,240,0,232],
[242,271,275,263,260,260,247,276,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,289,247,272,249,260,256,275,256,269],
[212,0,233,231,242,265,229,260,243,226],
[254,268,0,285,272,262,274,293,240,263],
[229,270,216,0,215,249,246,260,243,234],
[252,259,229,286,0,237,257,263,248,246],
[241,236,239,252,264,0,249,271,239,247],
[245,272,227,255,244,252,0,295,246,236],
[226,241,208,241,238,230,206,0,228,221],
[245,258,261,258,253,262,255,273,0,239],
[232,275,238,267,255,254,265,280,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,257,246,250,242,245,245,274,265],
[231,0,258,243,236,242,242,236,266,231],
[244,243,0,257,237,259,249,235,269,248],
[255,258,244,0,242,255,239,248,297,255],
[251,265,264,259,0,260,251,224,273,247],
[259,259,242,246,241,0,238,230,259,254],
[256,259,252,262,250,263,0,257,275,255],
[256,265,266,253,277,271,244,0,284,276],
[227,235,232,204,228,242,226,217,0,218],
[236,270,253,246,254,247,246,225,283,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,308,248,250,294,278,275,223,268],
[233,0,312,178,223,264,300,270,239,193],
[193,189,0,204,198,261,222,212,210,208],
[253,323,297,0,232,267,322,276,273,265],
[251,278,303,269,0,291,269,285,242,213],
[207,237,240,234,210,0,257,234,211,262],
[223,201,279,179,232,244,0,227,225,235],
[226,231,289,225,216,267,274,0,217,206],
[278,262,291,228,259,290,276,284,0,259],
[233,308,293,236,288,239,266,295,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,238,265,259,259,251,271,256,251],
[246,0,245,244,258,244,251,259,243,259],
[263,256,0,257,247,252,251,244,261,273],
[236,257,244,0,239,231,235,242,253,238],
[242,243,254,262,0,237,251,244,253,247],
[242,257,249,270,264,0,242,247,268,253],
[250,250,250,266,250,259,0,237,244,247],
[230,242,257,259,257,254,264,0,260,257],
[245,258,240,248,248,233,257,241,0,246],
[250,242,228,263,254,248,254,244,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,293,266,270,271,255,249,256,272],
[230,0,241,233,247,220,237,230,228,227],
[208,260,0,238,231,228,243,249,227,241],
[235,268,263,0,229,228,255,226,238,239],
[231,254,270,272,0,273,250,258,228,268],
[230,281,273,273,228,0,246,256,225,236],
[246,264,258,246,251,255,0,248,205,227],
[252,271,252,275,243,245,253,0,223,248],
[245,273,274,263,273,276,296,278,0,290],
[229,274,260,262,233,265,274,253,211,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,297,287,269,258,274,272,233,273],
[245,0,299,288,251,270,262,279,265,280],
[204,202,0,260,233,219,247,216,233,240],
[214,213,241,0,214,234,241,250,234,243],
[232,250,268,287,0,252,253,278,246,267],
[243,231,282,267,249,0,249,251,240,265],
[227,239,254,260,248,252,0,262,248,267],
[229,222,285,251,223,250,239,0,251,238],
[268,236,268,267,255,261,253,250,0,266],
[228,221,261,258,234,236,234,263,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,254,284,274,252,272,277,279,273],
[261,0,278,266,264,244,259,270,255,277],
[247,223,0,269,258,246,273,281,268,257],
[217,235,232,0,281,235,244,271,257,268],
[227,237,243,220,0,240,235,265,256,262],
[249,257,255,266,261,0,268,268,268,273],
[229,242,228,257,266,233,0,267,269,269],
[224,231,220,230,236,233,234,0,266,242],
[222,246,233,244,245,233,232,235,0,260],
[228,224,244,233,239,228,232,259,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,248,256,245,238,262,252,231,268],
[254,0,236,246,242,230,253,255,207,233],
[253,265,0,269,260,256,273,260,244,238],
[245,255,232,0,241,224,259,258,229,244],
[256,259,241,260,0,239,247,263,235,250],
[263,271,245,277,262,0,270,282,256,258],
[239,248,228,242,254,231,0,261,232,247],
[249,246,241,243,238,219,240,0,234,251],
[270,294,257,272,266,245,269,267,0,261],
[233,268,263,257,251,243,254,250,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,200,247,252,257,224,250,226,228,276],
[301,0,259,256,268,254,266,247,271,290],
[254,242,0,275,283,256,251,228,225,278],
[249,245,226,0,250,239,248,241,216,247],
[244,233,218,251,0,226,236,251,243,249],
[277,247,245,262,275,0,261,258,259,305],
[251,235,250,253,265,240,0,238,247,274],
[275,254,273,260,250,243,263,0,269,279],
[273,230,276,285,258,242,254,232,0,266],
[225,211,223,254,252,196,227,222,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,275,240,214,255,229,214,217,239],
[259,0,290,258,253,242,220,222,239,247],
[226,211,0,199,221,264,199,227,220,228],
[261,243,302,0,232,263,237,223,229,237],
[287,248,280,269,0,278,250,241,231,245],
[246,259,237,238,223,0,202,219,191,221],
[272,281,302,264,251,299,0,243,271,254],
[287,279,274,278,260,282,258,0,260,239],
[284,262,281,272,270,310,230,241,0,266],
[262,254,273,264,256,280,247,262,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,244,253,248,225,233,251,258,263],
[241,0,232,248,222,231,234,245,242,258],
[257,269,0,263,245,271,241,249,250,280],
[248,253,238,0,233,230,250,249,262,252],
[253,279,256,268,0,246,230,272,258,265],
[276,270,230,271,255,0,254,260,266,280],
[268,267,260,251,271,247,0,268,276,279],
[250,256,252,252,229,241,233,0,254,266],
[243,259,251,239,243,235,225,247,0,251],
[238,243,221,249,236,221,222,235,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,231,255,264,260,260,238,241,255],
[244,0,229,249,267,264,238,236,242,235],
[270,272,0,249,269,271,270,253,236,242],
[246,252,252,0,273,270,258,238,236,244],
[237,234,232,228,0,239,243,244,224,221],
[241,237,230,231,262,0,242,233,214,223],
[241,263,231,243,258,259,0,246,229,272],
[263,265,248,263,257,268,255,0,253,262],
[260,259,265,265,277,287,272,248,0,268],
[246,266,259,257,280,278,229,239,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,255,255,248,249,244,263,237,248],
[263,0,262,255,244,245,245,256,239,232],
[246,239,0,248,231,235,232,255,238,232],
[246,246,253,0,244,236,244,250,243,250],
[253,257,270,257,0,251,254,263,252,249],
[252,256,266,265,250,0,253,274,260,252],
[257,256,269,257,247,248,0,253,254,247],
[238,245,246,251,238,227,248,0,239,247],
[264,262,263,258,249,241,247,262,0,240],
[253,269,269,251,252,249,254,254,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,179,216,355,248,207,150,170,306],
[274,0,263,194,319,263,204,250,193,368],
[322,238,0,341,420,213,238,283,293,289],
[285,307,160,0,382,199,209,211,257,244],
[146,182,81,119,0,109,146,150,156,123],
[253,238,288,302,392,0,288,207,293,309],
[294,297,263,292,355,213,0,199,305,320],
[351,251,218,290,351,294,302,0,221,319],
[331,308,208,244,345,208,196,280,0,429],
[195,133,212,257,378,192,181,182,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,220,251,243,242,237,278,268,253],
[249,0,274,247,281,264,249,263,245,264],
[281,227,0,224,263,256,253,265,240,255],
[250,254,277,0,270,259,265,280,257,233],
[258,220,238,231,0,244,238,249,245,245],
[259,237,245,242,257,0,223,246,242,241],
[264,252,248,236,263,278,0,258,226,265],
[223,238,236,221,252,255,243,0,252,257],
[233,256,261,244,256,259,275,249,0,251],
[248,237,246,268,256,260,236,244,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,264,214,276,237,261,244,231,267],
[247,0,235,235,246,206,253,244,229,243],
[237,266,0,240,256,236,249,230,240,250],
[287,266,261,0,289,238,264,267,252,267],
[225,255,245,212,0,203,260,215,207,241],
[264,295,265,263,298,0,274,273,250,263],
[240,248,252,237,241,227,0,236,228,236],
[257,257,271,234,286,228,265,0,239,251],
[270,272,261,249,294,251,273,262,0,247],
[234,258,251,234,260,238,265,250,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,208,262,282,330,207,321,262,249],
[236,0,243,216,254,306,234,210,213,149],
[293,258,0,234,308,274,227,300,256,252],
[239,285,267,0,259,279,302,312,325,221],
[219,247,193,242,0,270,221,290,306,158],
[171,195,227,222,231,0,244,280,266,177],
[294,267,274,199,280,257,0,331,211,169],
[180,291,201,189,211,221,170,0,221,144],
[239,288,245,176,195,235,290,280,0,257],
[252,352,249,280,343,324,332,357,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,243,253,226,229,238,233,271,269],
[266,0,274,262,246,250,256,249,289,282],
[258,227,0,263,240,243,236,245,272,273],
[248,239,238,0,229,224,236,248,265,259],
[275,255,261,272,0,270,249,281,289,285],
[272,251,258,277,231,0,228,267,265,250],
[263,245,265,265,252,273,0,270,301,276],
[268,252,256,253,220,234,231,0,269,263],
[230,212,229,236,212,236,200,232,0,232],
[232,219,228,242,216,251,225,238,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,247,265,245,244,251,254,255,250],
[260,0,253,265,258,263,248,271,257,266],
[254,248,0,239,243,258,246,253,254,237],
[236,236,262,0,240,249,253,265,247,241],
[256,243,258,261,0,266,246,263,264,251],
[257,238,243,252,235,0,241,250,246,237],
[250,253,255,248,255,260,0,269,254,255],
[247,230,248,236,238,251,232,0,226,232],
[246,244,247,254,237,255,247,275,0,244],
[251,235,264,260,250,264,246,269,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,242,254,232,234,246,245,235,232],
[243,0,227,231,239,234,229,222,247,246],
[259,274,0,264,266,261,250,237,250,253],
[247,270,237,0,251,253,257,248,237,249],
[269,262,235,250,0,246,255,250,247,244],
[267,267,240,248,255,0,266,258,245,255],
[255,272,251,244,246,235,0,243,252,262],
[256,279,264,253,251,243,258,0,237,254],
[266,254,251,264,254,256,249,264,0,267],
[269,255,248,252,257,246,239,247,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,231,267,270,205,243,226,240,244],
[274,0,227,239,267,222,234,242,239,257],
[270,274,0,239,284,255,245,265,255,295],
[234,262,262,0,272,245,264,260,251,269],
[231,234,217,229,0,222,225,233,265,248],
[296,279,246,256,279,0,259,254,258,293],
[258,267,256,237,276,242,0,257,280,282],
[275,259,236,241,268,247,244,0,277,250],
[261,262,246,250,236,243,221,224,0,253],
[257,244,206,232,253,208,219,251,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,235,263,242,263,236,243,255,260],
[250,0,241,256,251,256,245,253,261,249],
[266,260,0,260,273,259,260,248,266,270],
[238,245,241,0,245,272,257,250,259,242],
[259,250,228,256,0,250,241,250,251,233],
[238,245,242,229,251,0,225,244,247,254],
[265,256,241,244,260,276,0,258,266,262],
[258,248,253,251,251,257,243,0,271,255],
[246,240,235,242,250,254,235,230,0,253],
[241,252,231,259,268,247,239,246,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,254,223,267,242,260,241,256,262],
[224,0,231,188,241,238,242,249,258,262],
[247,270,0,214,254,234,262,249,254,263],
[278,313,287,0,282,287,307,310,245,282],
[234,260,247,219,0,252,228,218,229,266],
[259,263,267,214,249,0,246,265,252,237],
[241,259,239,194,273,255,0,247,232,262],
[260,252,252,191,283,236,254,0,252,259],
[245,243,247,256,272,249,269,249,0,267],
[239,239,238,219,235,264,239,242,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,253,264,256,252,259,245,251,242],
[261,0,257,274,257,279,268,260,256,246],
[248,244,0,257,255,272,252,241,273,261],
[237,227,244,0,265,268,251,246,254,245],
[245,244,246,236,0,269,275,235,252,255],
[249,222,229,233,232,0,234,208,235,244],
[242,233,249,250,226,267,0,247,255,244],
[256,241,260,255,266,293,254,0,255,259],
[250,245,228,247,249,266,246,246,0,260],
[259,255,240,256,246,257,257,242,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,272,252,313,219,272,256,239,247],
[248,0,269,260,275,236,265,248,246,228],
[229,232,0,236,274,214,248,237,210,213],
[249,241,265,0,285,250,234,255,227,233],
[188,226,227,216,0,199,227,206,209,230],
[282,265,287,251,302,0,271,272,242,244],
[229,236,253,267,274,230,0,227,265,266],
[245,253,264,246,295,229,274,0,266,249],
[262,255,291,274,292,259,236,235,0,237],
[254,273,288,268,271,257,235,252,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,241,262,262,259,255,263,259,276],
[241,0,230,238,243,232,258,251,251,254],
[260,271,0,262,273,249,246,268,262,267],
[239,263,239,0,239,255,264,243,255,268],
[239,258,228,262,0,233,253,256,258,269],
[242,269,252,246,268,0,263,247,252,265],
[246,243,255,237,248,238,0,247,247,269],
[238,250,233,258,245,254,254,0,245,263],
[242,250,239,246,243,249,254,256,0,254],
[225,247,234,233,232,236,232,238,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,273,258,242,268,253,234,251,246],
[263,0,266,255,261,256,264,257,262,223],
[228,235,0,212,244,247,231,229,230,233],
[243,246,289,0,240,269,253,236,251,228],
[259,240,257,261,0,261,234,245,218,236],
[233,245,254,232,240,0,249,247,237,244],
[248,237,270,248,267,252,0,278,260,249],
[267,244,272,265,256,254,223,0,259,253],
[250,239,271,250,283,264,241,242,0,243],
[255,278,268,273,265,257,252,248,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,289,264,260,234,254,251,229,278],
[245,0,313,268,252,257,267,248,292,227],
[212,188,0,187,210,212,214,230,201,239],
[237,233,314,0,271,258,265,275,269,278],
[241,249,291,230,0,201,221,244,255,224],
[267,244,289,243,300,0,259,236,284,256],
[247,234,287,236,280,242,0,226,278,276],
[250,253,271,226,257,265,275,0,265,251],
[272,209,300,232,246,217,223,236,0,243],
[223,274,262,223,277,245,225,250,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,242,223,233,252,202,235,236,234],
[279,0,252,266,273,272,248,286,251,257],
[259,249,0,245,275,279,248,305,249,236],
[278,235,256,0,286,262,248,259,244,236],
[268,228,226,215,0,242,234,238,212,225],
[249,229,222,239,259,0,225,261,254,247],
[299,253,253,253,267,276,0,269,277,247],
[266,215,196,242,263,240,232,0,236,247],
[265,250,252,257,289,247,224,265,0,247],
[267,244,265,265,276,254,254,254,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,220,216,240,217,214,217,217,237],
[263,0,246,247,270,247,228,239,242,264],
[281,255,0,272,259,266,252,229,245,270],
[285,254,229,0,245,270,244,257,241,264],
[261,231,242,256,0,262,239,226,244,253],
[284,254,235,231,239,0,235,228,240,242],
[287,273,249,257,262,266,0,253,257,279],
[284,262,272,244,275,273,248,0,268,288],
[284,259,256,260,257,261,244,233,0,263],
[264,237,231,237,248,259,222,213,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,218,248,230,245,249,263,243,228],
[260,0,240,260,261,254,241,270,235,265],
[283,261,0,260,275,255,276,278,245,274],
[253,241,241,0,245,249,257,270,218,239],
[271,240,226,256,0,264,263,263,254,225],
[256,247,246,252,237,0,258,262,235,255],
[252,260,225,244,238,243,0,244,230,237],
[238,231,223,231,238,239,257,0,250,237],
[258,266,256,283,247,266,271,251,0,264],
[273,236,227,262,276,246,264,264,237,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,231,240,253,251,243,233,254,249],
[247,0,264,256,266,259,267,250,267,250],
[270,237,0,260,271,257,269,257,273,259],
[261,245,241,0,252,259,254,247,271,243],
[248,235,230,249,0,252,249,252,262,226],
[250,242,244,242,249,0,247,254,265,242],
[258,234,232,247,252,254,0,244,267,230],
[268,251,244,254,249,247,257,0,263,249],
[247,234,228,230,239,236,234,238,0,225],
[252,251,242,258,275,259,271,252,276,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,236,201,229,234,234,225,244,242],
[287,0,261,221,234,271,259,249,242,232],
[265,240,0,238,261,269,256,234,241,224],
[300,280,263,0,245,269,263,271,228,257],
[272,267,240,256,0,231,275,257,239,224],
[267,230,232,232,270,0,263,251,212,239],
[267,242,245,238,226,238,0,257,233,219],
[276,252,267,230,244,250,244,0,239,219],
[257,259,260,273,262,289,268,262,0,235],
[259,269,277,244,277,262,282,282,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,249,231,268,226,273,263,263,199],
[232,0,198,225,260,235,276,263,282,214],
[252,303,0,272,184,227,269,212,227,237],
[270,276,229,0,204,236,230,260,258,217],
[233,241,317,297,0,252,315,254,279,243],
[275,266,274,265,249,0,280,230,214,255],
[228,225,232,271,186,221,0,253,218,198],
[238,238,289,241,247,271,248,0,291,251],
[238,219,274,243,222,287,283,210,0,267],
[302,287,264,284,258,246,303,250,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,211,256,177,221,213,149,151,158,258],
[290,0,290,270,297,163,258,198,230,335],
[245,211,0,177,207,144,142,186,168,203],
[324,231,324,0,307,289,316,281,243,286],
[280,204,294,194,0,175,194,206,237,301],
[288,338,357,212,326,0,284,279,283,263],
[352,243,359,185,307,217,0,209,215,278],
[350,303,315,220,295,222,292,0,304,300],
[343,271,333,258,264,218,286,197,0,287],
[243,166,298,215,200,238,223,201,214,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,253,237,253,247,250,272,253,244],
[254,0,258,260,244,248,237,245,264,237],
[248,243,0,258,255,241,243,262,254,244],
[264,241,243,0,257,254,243,246,262,243],
[248,257,246,244,0,246,242,260,253,239],
[254,253,260,247,255,0,262,261,261,238],
[251,264,258,258,259,239,0,272,274,255],
[229,256,239,255,241,240,229,0,246,239],
[248,237,247,239,248,240,227,255,0,227],
[257,264,257,258,262,263,246,262,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,222,258,252,275,253,248,262,271],
[238,0,265,232,241,262,226,271,249,257],
[279,236,0,245,264,234,248,245,246,245],
[243,269,256,0,224,237,220,265,249,268],
[249,260,237,277,0,251,249,279,239,264],
[226,239,267,264,250,0,261,270,273,265],
[248,275,253,281,252,240,0,271,239,297],
[253,230,256,236,222,231,230,0,249,238],
[239,252,255,252,262,228,262,252,0,276],
[230,244,256,233,237,236,204,263,225,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,254,249,242,245,256,251,247,258],
[249,0,268,260,251,259,241,270,248,262],
[247,233,0,265,243,245,240,263,248,262],
[252,241,236,0,240,246,247,251,260,250],
[259,250,258,261,0,235,250,251,248,253],
[256,242,256,255,266,0,249,257,251,255],
[245,260,261,254,251,252,0,254,254,263],
[250,231,238,250,250,244,247,0,254,253],
[254,253,253,241,253,250,247,247,0,258],
[243,239,239,251,248,246,238,248,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,199,248,268,282,263,271,260,263],
[275,0,202,270,255,278,246,252,246,250],
[302,299,0,307,272,340,254,309,233,313],
[253,231,194,0,235,235,186,259,236,251],
[233,246,229,266,0,276,225,211,200,272],
[219,223,161,266,225,0,225,229,183,238],
[238,255,247,315,276,276,0,266,236,297],
[230,249,192,242,290,272,235,0,233,245],
[241,255,268,265,301,318,265,268,0,285],
[238,251,188,250,229,263,204,256,216,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,291,302,308,274,273,258,218,253,323],
[210,0,226,271,223,228,270,196,261,281],
[199,275,0,269,243,244,244,220,235,299],
[193,230,232,0,242,209,226,262,259,297],
[227,278,258,259,0,243,263,213,227,263],
[228,273,257,292,258,0,267,261,281,296],
[243,231,257,275,238,234,0,251,282,287],
[283,305,281,239,288,240,250,0,256,297],
[248,240,266,242,274,220,219,245,0,297],
[178,220,202,204,238,205,214,204,204,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,230,241,249,244,228,221,240,238],
[268,0,245,256,257,305,249,250,256,239],
[271,256,0,251,258,276,281,259,252,247],
[260,245,250,0,279,268,233,266,288,252],
[252,244,243,222,0,271,238,229,254,225],
[257,196,225,233,230,0,209,192,211,206],
[273,252,220,268,263,292,0,251,283,244],
[280,251,242,235,272,309,250,0,262,234],
[261,245,249,213,247,290,218,239,0,237],
[263,262,254,249,276,295,257,267,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,282,263,251,245,271,266,281,285,272],
[219,0,243,218,255,248,259,228,251,232],
[238,258,0,213,238,242,252,243,257,264],
[250,283,288,0,277,248,290,247,303,276],
[256,246,263,224,0,223,240,255,254,261],
[230,253,259,253,278,0,277,254,262,267],
[235,242,249,211,261,224,0,251,238,250],
[220,273,258,254,246,247,250,0,275,277],
[216,250,244,198,247,239,263,226,0,254],
[229,269,237,225,240,234,251,224,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,303,298,247,290,245,250,266,262,269],
[198,0,260,232,254,244,246,213,227,230],
[203,241,0,226,231,220,248,245,217,212],
[254,269,275,0,266,246,245,272,250,258],
[211,247,270,235,0,212,236,249,245,254],
[256,257,281,255,289,0,264,268,256,249],
[251,255,253,256,265,237,0,254,231,224],
[235,288,256,229,252,233,247,0,247,235],
[239,274,284,251,256,245,270,254,0,268],
[232,271,289,243,247,252,277,266,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,298,247,256,242,258,262,259,264,257],
[203,0,215,217,223,230,237,234,208,215],
[254,286,0,257,249,260,260,273,268,250],
[245,284,244,0,257,228,252,250,242,226],
[259,278,252,244,0,260,269,255,261,247],
[243,271,241,273,241,0,234,265,245,243],
[239,264,241,249,232,267,0,247,226,224],
[242,267,228,251,246,236,254,0,236,242],
[237,293,233,259,240,256,275,265,0,242],
[244,286,251,275,254,258,277,259,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,196,227,285,206,212,206,294,196,198],
[305,0,278,249,195,297,232,235,210,295],
[274,223,0,203,205,239,266,258,241,216],
[216,252,298,0,164,195,182,145,176,233],
[295,306,296,337,0,220,220,295,212,286],
[289,204,262,306,281,0,186,320,181,276],
[295,269,235,319,281,315,0,318,306,253],
[207,266,243,356,206,181,183,0,168,260],
[305,291,260,325,289,320,195,333,0,260],
[303,206,285,268,215,225,248,241,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,238,221,177,192,244,257,241,237],
[254,0,246,210,283,222,257,256,261,214],
[263,255,0,223,220,204,258,298,236,238],
[280,291,278,0,258,280,286,273,311,217],
[324,218,281,243,0,205,336,283,237,238],
[309,279,297,221,296,0,294,242,222,259],
[257,244,243,215,165,207,0,288,231,184],
[244,245,203,228,218,259,213,0,198,196],
[260,240,265,190,264,279,270,303,0,278],
[264,287,263,284,263,242,317,305,223,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,259,244,256,241,282,258,252,260],
[254,0,275,231,234,270,280,278,215,252],
[242,226,0,205,263,236,236,249,227,235],
[257,270,296,0,293,293,276,287,285,231],
[245,267,238,208,0,237,256,266,264,267],
[260,231,265,208,264,0,240,266,221,257],
[219,221,265,225,245,261,0,270,227,248],
[243,223,252,214,235,235,231,0,244,221],
[249,286,274,216,237,280,274,257,0,236],
[241,249,266,270,234,244,253,280,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,249,220,232,248,226,267,251,234],
[246,0,253,237,267,255,240,264,258,245],
[252,248,0,253,245,252,239,254,255,259],
[281,264,248,0,257,290,254,266,247,245],
[269,234,256,244,0,235,236,260,246,273],
[253,246,249,211,266,0,226,246,248,236],
[275,261,262,247,265,275,0,260,240,251],
[234,237,247,235,241,255,241,0,261,237],
[250,243,246,254,255,253,261,240,0,247],
[267,256,242,256,228,265,250,264,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,276,238,253,264,251,263,275,255],
[251,0,283,245,267,266,261,245,273,252],
[225,218,0,226,242,244,243,240,249,238],
[263,256,275,0,253,244,248,249,270,259],
[248,234,259,248,0,265,239,237,262,259],
[237,235,257,257,236,0,254,243,262,251],
[250,240,258,253,262,247,0,245,262,254],
[238,256,261,252,264,258,256,0,268,266],
[226,228,252,231,239,239,239,233,0,241],
[246,249,263,242,242,250,247,235,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,266,263,260,256,243,255,243,256],
[234,0,247,252,260,240,248,248,247,242],
[235,254,0,240,239,240,240,256,232,243],
[238,249,261,0,240,247,262,249,237,247],
[241,241,262,261,0,266,250,255,256,245],
[245,261,261,254,235,0,259,244,241,263],
[258,253,261,239,251,242,0,249,239,259],
[246,253,245,252,246,257,252,0,241,250],
[258,254,269,264,245,260,262,260,0,255],
[245,259,258,254,256,238,242,251,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,251,236,249,270,271,275,232,254],
[251,0,259,275,264,260,258,272,242,254],
[250,242,0,268,262,260,259,248,238,232],
[265,226,233,0,250,238,259,252,225,250],
[252,237,239,251,0,255,276,261,241,240],
[231,241,241,263,246,0,274,265,236,225],
[230,243,242,242,225,227,0,253,236,239],
[226,229,253,249,240,236,248,0,223,231],
[269,259,263,276,260,265,265,278,0,250],
[247,247,269,251,261,276,262,270,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,258,267,237,263,260,278,258,277],
[231,0,241,268,247,249,259,257,260,280],
[243,260,0,237,251,241,266,265,246,274],
[234,233,264,0,231,238,253,262,235,258],
[264,254,250,270,0,259,266,285,287,269],
[238,252,260,263,242,0,277,250,252,275],
[241,242,235,248,235,224,0,251,258,243],
[223,244,236,239,216,251,250,0,250,258],
[243,241,255,266,214,249,243,251,0,248],
[224,221,227,243,232,226,258,243,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,240,221,178,209,260,201,203,205],
[275,0,287,258,227,226,265,228,221,230],
[261,214,0,232,233,247,254,240,225,227],
[280,243,269,0,224,214,317,260,244,244],
[323,274,268,277,0,202,319,275,252,275],
[292,275,254,287,299,0,315,275,249,273],
[241,236,247,184,182,186,0,221,215,205],
[300,273,261,241,226,226,280,0,257,245],
[298,280,276,257,249,252,286,244,0,242],
[296,271,274,257,226,228,296,256,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,261,237,238,226,224,242,245,252],
[268,0,242,236,264,234,233,250,233,252],
[240,259,0,246,249,232,243,256,253,268],
[264,265,255,0,257,244,242,257,264,266],
[263,237,252,244,0,247,252,250,247,258],
[275,267,269,257,254,0,253,274,249,280],
[277,268,258,259,249,248,0,263,267,284],
[259,251,245,244,251,227,238,0,247,272],
[256,268,248,237,254,252,234,254,0,268],
[249,249,233,235,243,221,217,229,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,360,294,394,335,227,266,312,386,368],
[141,0,200,291,244,211,220,155,258,269],
[207,301,0,290,278,227,206,201,312,248],
[107,210,211,0,216,193,167,166,233,224],
[166,257,223,285,0,156,257,195,237,258],
[274,290,274,308,345,0,245,222,305,256],
[235,281,295,334,244,256,0,251,295,297],
[189,346,300,335,306,279,250,0,394,365],
[115,243,189,268,264,196,206,107,0,199],
[133,232,253,277,243,245,204,136,302,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,258,264,282,273,281,266,284,244],
[240,0,249,235,269,247,259,256,259,235],
[243,252,0,257,275,239,278,273,255,260],
[237,266,244,0,263,260,284,244,256,234],
[219,232,226,238,0,230,273,239,246,237],
[228,254,262,241,271,0,265,251,257,246],
[220,242,223,217,228,236,0,246,247,238],
[235,245,228,257,262,250,255,0,268,260],
[217,242,246,245,255,244,254,233,0,240],
[257,266,241,267,264,255,263,241,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,249,251,256,243,258,236,254,242],
[244,0,240,250,236,239,232,242,248,248],
[252,261,0,236,255,260,261,239,258,251],
[250,251,265,0,246,244,246,250,252,246],
[245,265,246,255,0,271,266,251,242,257],
[258,262,241,257,230,0,279,265,266,264],
[243,269,240,255,235,222,0,248,249,256],
[265,259,262,251,250,236,253,0,243,244],
[247,253,243,249,259,235,252,258,0,254],
[259,253,250,255,244,237,245,257,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,230,249,266,258,270,253,281,224],
[246,0,203,250,226,254,251,240,269,214],
[271,298,0,273,255,288,301,255,293,233],
[252,251,228,0,238,246,253,251,273,232],
[235,275,246,263,0,282,285,267,281,242],
[243,247,213,255,219,0,271,246,272,213],
[231,250,200,248,216,230,0,239,237,253],
[248,261,246,250,234,255,262,0,260,233],
[220,232,208,228,220,229,264,241,0,213],
[277,287,268,269,259,288,248,268,288,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,254,221,212,225,224,212,239,258],
[279,0,293,266,233,270,222,248,256,285],
[247,208,0,212,206,218,218,222,227,229],
[280,235,289,0,254,277,257,265,275,280],
[289,268,295,247,0,291,267,245,268,275],
[276,231,283,224,210,0,220,233,259,256],
[277,279,283,244,234,281,0,243,263,282],
[289,253,279,236,256,268,258,0,268,273],
[262,245,274,226,233,242,238,233,0,254],
[243,216,272,221,226,245,219,228,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,199,246,214,240,232,281,249,248,213],
[302,0,257,225,260,231,304,277,254,245],
[255,244,0,218,221,221,245,246,236,203],
[287,276,283,0,263,262,313,297,265,245],
[261,241,280,238,0,244,271,258,220,226],
[269,270,280,239,257,0,278,258,259,255],
[220,197,256,188,230,223,0,220,228,202],
[252,224,255,204,243,243,281,0,238,242],
[253,247,265,236,281,242,273,263,0,250],
[288,256,298,256,275,246,299,259,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,226,258,246,261,268,232,254,262],
[247,0,226,255,245,249,258,229,238,255],
[275,275,0,287,262,272,288,249,275,278],
[243,246,214,0,224,245,253,230,234,248],
[255,256,239,277,0,243,262,255,258,260],
[240,252,229,256,258,0,246,237,244,238],
[233,243,213,248,239,255,0,215,244,226],
[269,272,252,271,246,264,286,0,254,272],
[247,263,226,267,243,257,257,247,0,267],
[239,246,223,253,241,263,275,229,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,247,266,244,229,251,244,237,256],
[254,0,260,266,249,251,254,240,244,246],
[254,241,0,269,237,262,266,251,260,258],
[235,235,232,0,237,240,255,236,240,250],
[257,252,264,264,0,242,274,239,269,267],
[272,250,239,261,259,0,253,253,257,256],
[250,247,235,246,227,248,0,237,250,248],
[257,261,250,265,262,248,264,0,265,264],
[264,257,241,261,232,244,251,236,0,257],
[245,255,243,251,234,245,253,237,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,230,262,258,247,224,247,252,249],
[258,0,237,274,250,244,246,238,239,252],
[271,264,0,253,242,241,249,239,243,266],
[239,227,248,0,229,243,225,237,243,256],
[243,251,259,272,0,258,241,233,234,269],
[254,257,260,258,243,0,242,252,243,261],
[277,255,252,276,260,259,0,230,241,290],
[254,263,262,264,268,249,271,0,253,269],
[249,262,258,258,267,258,260,248,0,279],
[252,249,235,245,232,240,211,232,222,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,221,212,223,222,267,241,212,229],
[254,0,234,237,233,248,270,246,254,245],
[280,267,0,256,243,246,282,285,258,267],
[289,264,245,0,258,252,259,284,257,267],
[278,268,258,243,0,261,269,288,234,260],
[279,253,255,249,240,0,270,285,262,253],
[234,231,219,242,232,231,0,254,245,252],
[260,255,216,217,213,216,247,0,231,257],
[289,247,243,244,267,239,256,270,0,249],
[272,256,234,234,241,248,249,244,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,241,249,243,257,274,219,239,254],
[248,0,267,251,268,253,289,255,261,245],
[260,234,0,267,269,249,272,249,274,252],
[252,250,234,0,245,252,268,221,252,246],
[258,233,232,256,0,258,273,232,251,240],
[244,248,252,249,243,0,275,218,253,240],
[227,212,229,233,228,226,0,239,232,233],
[282,246,252,280,269,283,262,0,261,265],
[262,240,227,249,250,248,269,240,0,227],
[247,256,249,255,261,261,268,236,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,271,240,234,242,239,245,256,253],
[236,0,264,230,253,245,241,222,257,257],
[230,237,0,222,237,240,228,219,233,235],
[261,271,279,0,249,262,237,241,251,256],
[267,248,264,252,0,243,242,252,277,247],
[259,256,261,239,258,0,255,243,260,246],
[262,260,273,264,259,246,0,246,246,271],
[256,279,282,260,249,258,255,0,277,263],
[245,244,268,250,224,241,255,224,0,236],
[248,244,266,245,254,255,230,238,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,259,248,265,263,238,255,267,277],
[246,0,248,230,270,241,237,241,264,254],
[242,253,0,238,235,235,240,243,239,252],
[253,271,263,0,257,254,240,253,290,262],
[236,231,266,244,0,244,226,241,259,257],
[238,260,266,247,257,0,256,255,243,260],
[263,264,261,261,275,245,0,264,264,270],
[246,260,258,248,260,246,237,0,247,241],
[234,237,262,211,242,258,237,254,0,257],
[224,247,249,239,244,241,231,260,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,194,209,266,207,218,225,231,213],
[261,0,214,236,265,218,218,204,272,271],
[307,287,0,301,301,292,273,250,260,287],
[292,265,200,0,242,253,232,225,234,236],
[235,236,200,259,0,204,205,205,274,246],
[294,283,209,248,297,0,213,252,309,235],
[283,283,228,269,296,288,0,317,287,285],
[276,297,251,276,296,249,184,0,288,279],
[270,229,241,267,227,192,214,213,0,238],
[288,230,214,265,255,266,216,222,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,257,259,255,253,261,257,229,236],
[283,0,272,282,262,250,269,308,256,275],
[244,229,0,238,245,239,277,262,258,252],
[242,219,263,0,265,248,255,262,255,256],
[246,239,256,236,0,258,288,262,249,255],
[248,251,262,253,243,0,274,262,256,266],
[240,232,224,246,213,227,0,276,220,241],
[244,193,239,239,239,239,225,0,235,254],
[272,245,243,246,252,245,281,266,0,264],
[265,226,249,245,246,235,260,247,237,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,251,249,265,273,255,247,250,249],
[242,0,240,233,232,242,242,235,226,230],
[250,261,0,254,266,271,268,243,253,257],
[252,268,247,0,265,261,280,247,256,268],
[236,269,235,236,0,263,233,233,232,236],
[228,259,230,240,238,0,242,213,225,242],
[246,259,233,221,268,259,0,240,248,255],
[254,266,258,254,268,288,261,0,250,259],
[251,275,248,245,269,276,253,251,0,241],
[252,271,244,233,265,259,246,242,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,233,246,229,273,259,256,234,256],
[255,0,237,231,233,255,246,235,243,256],
[268,264,0,259,257,268,264,249,254,267],
[255,270,242,0,258,253,262,263,259,274],
[272,268,244,243,0,273,260,260,257,259],
[228,246,233,248,228,0,239,233,242,240],
[242,255,237,239,241,262,0,246,242,253],
[245,266,252,238,241,268,255,0,250,280],
[267,258,247,242,244,259,259,251,0,266],
[245,245,234,227,242,261,248,221,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,254,226,257,264,252,229,242,228],
[263,0,251,233,240,253,254,263,236,253],
[247,250,0,237,258,254,252,252,251,252],
[275,268,264,0,253,271,274,248,264,259],
[244,261,243,248,0,261,258,242,260,253],
[237,248,247,230,240,0,246,234,244,244],
[249,247,249,227,243,255,0,240,258,242],
[272,238,249,253,259,267,261,0,254,255],
[259,265,250,237,241,257,243,247,0,248],
[273,248,249,242,248,257,259,246,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,219,239,228,239,249,222,230,204],
[272,0,244,263,248,281,259,242,253,254],
[282,257,0,248,237,261,250,229,222,216],
[262,238,253,0,235,255,284,246,229,210],
[273,253,264,266,0,271,275,247,261,236],
[262,220,240,246,230,0,273,227,231,247],
[252,242,251,217,226,228,0,219,224,219],
[279,259,272,255,254,274,282,0,268,243],
[271,248,279,272,240,270,277,233,0,240],
[297,247,285,291,265,254,282,258,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,234,261,276,257,270,263,266,270],
[252,0,253,270,274,242,271,261,273,269],
[267,248,0,274,277,256,278,264,278,269],
[240,231,227,0,250,227,254,248,239,250],
[225,227,224,251,0,253,233,230,234,252],
[244,259,245,274,248,0,247,258,264,265],
[231,230,223,247,268,254,0,252,254,250],
[238,240,237,253,271,243,249,0,265,270],
[235,228,223,262,267,237,247,236,0,256],
[231,232,232,251,249,236,251,231,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,249,231,266,259,258,262,286,256],
[230,0,215,207,226,250,240,241,259,222],
[252,286,0,247,250,275,248,274,303,247],
[270,294,254,0,275,275,286,288,293,240],
[235,275,251,226,0,254,250,252,265,263],
[242,251,226,226,247,0,219,261,254,247],
[243,261,253,215,251,282,0,289,259,260],
[239,260,227,213,249,240,212,0,249,251],
[215,242,198,208,236,247,242,252,0,230],
[245,279,254,261,238,254,241,250,271,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,236,251,242,240,253,237,254,252],
[257,0,249,257,247,266,281,260,258,268],
[265,252,0,251,248,258,255,244,256,249],
[250,244,250,0,258,273,258,271,241,273],
[259,254,253,243,0,286,267,278,254,278],
[261,235,243,228,215,0,250,253,226,270],
[248,220,246,243,234,251,0,256,231,253],
[264,241,257,230,223,248,245,0,233,261],
[247,243,245,260,247,275,270,268,0,261],
[249,233,252,228,223,231,248,240,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,275,247,237,260,254,264,247,264],
[252,0,268,265,256,244,264,263,261,252],
[226,233,0,252,222,245,241,246,249,233],
[254,236,249,0,234,255,269,268,266,257],
[264,245,279,267,0,265,264,256,258,266],
[241,257,256,246,236,0,234,255,242,251],
[247,237,260,232,237,267,0,276,247,242],
[237,238,255,233,245,246,225,0,236,233],
[254,240,252,235,243,259,254,265,0,261],
[237,249,268,244,235,250,259,268,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,241,257,228,262,257,233,223,231],
[247,0,243,256,226,266,246,223,227,216],
[260,258,0,256,229,252,242,215,254,231],
[244,245,245,0,235,264,243,235,232,238],
[273,275,272,266,0,277,267,242,263,251],
[239,235,249,237,224,0,246,225,232,231],
[244,255,259,258,234,255,0,239,236,249],
[268,278,286,266,259,276,262,0,260,247],
[278,274,247,269,238,269,265,241,0,249],
[270,285,270,263,250,270,252,254,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,248,259,268,283,259,253,286,245],
[251,0,238,237,241,239,254,255,245,238],
[253,263,0,254,267,250,268,256,269,272],
[242,264,247,0,257,246,265,272,273,246],
[233,260,234,244,0,245,255,257,242,248],
[218,262,251,255,256,0,260,261,259,255],
[242,247,233,236,246,241,0,256,277,247],
[248,246,245,229,244,240,245,0,267,242],
[215,256,232,228,259,242,224,234,0,250],
[256,263,229,255,253,246,254,259,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,290,248,290,240,257,279,295,278,257],
[211,0,201,253,210,210,227,228,228,215],
[253,300,0,278,265,233,268,261,271,269],
[211,248,223,0,200,202,228,209,249,201],
[261,291,236,301,0,243,260,261,277,249],
[244,291,268,299,258,0,286,256,284,286],
[222,274,233,273,241,215,0,238,262,254],
[206,273,240,292,240,245,263,0,248,217],
[223,273,230,252,224,217,239,253,0,253],
[244,286,232,300,252,215,247,284,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,187,251,253,151,226,253,212,191,304],
[314,0,236,276,230,213,355,217,184,272],
[250,265,0,292,225,281,308,325,262,245],
[248,225,209,0,245,214,257,266,248,256],
[350,271,276,256,0,224,324,308,240,282],
[275,288,220,287,277,0,357,368,239,346],
[248,146,193,244,177,144,0,161,157,154],
[289,284,176,235,193,133,340,0,231,304],
[310,317,239,253,261,262,344,270,0,282],
[197,229,256,245,219,155,347,197,219,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,259,246,251,264,260,230,266,247],
[256,0,257,278,223,238,261,261,288,225],
[242,244,0,269,248,287,267,260,269,249],
[255,223,232,0,238,231,228,227,249,228],
[250,278,253,263,0,225,249,238,238,219],
[237,263,214,270,276,0,244,238,259,265],
[241,240,234,273,252,257,0,263,275,260],
[271,240,241,274,263,263,238,0,253,260],
[235,213,232,252,263,242,226,248,0,240],
[254,276,252,273,282,236,241,241,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,246,244,269,235,228,250,248,241],
[257,0,263,252,258,248,239,256,240,245],
[255,238,0,254,265,239,241,264,243,241],
[257,249,247,0,272,242,236,261,238,247],
[232,243,236,229,0,229,219,249,238,236],
[266,253,262,259,272,0,253,250,244,252],
[273,262,260,265,282,248,0,268,256,273],
[251,245,237,240,252,251,233,0,248,232],
[253,261,258,263,263,257,245,253,0,241],
[260,256,260,254,265,249,228,269,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,215,236,253,258,258,243,239,246,229],
[286,0,276,280,255,285,254,240,255,254],
[265,225,0,253,238,231,245,224,227,255],
[248,221,248,0,247,224,233,226,233,226],
[243,246,263,254,0,257,249,218,241,239],
[243,216,270,277,244,0,233,255,241,229],
[258,247,256,268,252,268,0,238,234,244],
[262,261,277,275,283,246,263,0,251,260],
[255,246,274,268,260,260,267,250,0,240],
[272,247,246,275,262,272,257,241,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,253,252,264,228,247,247,242,272],
[276,0,272,269,278,240,266,285,266,257],
[248,229,0,259,252,243,255,231,250,264],
[249,232,242,0,241,237,260,241,252,248],
[237,223,249,260,0,249,230,252,252,240],
[273,261,258,264,252,0,262,277,248,272],
[254,235,246,241,271,239,0,264,268,259],
[254,216,270,260,249,224,237,0,252,250],
[259,235,251,249,249,253,233,249,0,251],
[229,244,237,253,261,229,242,251,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,243,238,220,234,254,241,248,230],
[267,0,258,251,265,266,270,250,274,258],
[258,243,0,228,239,253,263,240,269,252],
[263,250,273,0,260,237,259,226,284,259],
[281,236,262,241,0,235,265,228,260,252],
[267,235,248,264,266,0,276,238,267,236],
[247,231,238,242,236,225,0,214,248,230],
[260,251,261,275,273,263,287,0,278,245],
[253,227,232,217,241,234,253,223,0,222],
[271,243,249,242,249,265,271,256,279,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,266,248,262,268,280,260,250,249],
[235,0,242,243,281,275,263,255,236,242],
[235,259,0,251,268,264,249,252,250,240],
[253,258,250,0,268,261,266,239,235,250],
[239,220,233,233,0,245,261,243,239,238],
[233,226,237,240,256,0,271,243,250,241],
[221,238,252,235,240,230,0,255,252,247],
[241,246,249,262,258,258,246,0,254,248],
[251,265,251,266,262,251,249,247,0,256],
[252,259,261,251,263,260,254,253,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,249,257,239,260,241,236,242,284],
[231,0,262,247,240,237,259,234,251,266],
[252,239,0,248,250,270,254,265,256,245],
[244,254,253,0,252,272,265,270,230,261],
[262,261,251,249,0,236,274,232,250,243],
[241,264,231,229,265,0,250,246,233,274],
[260,242,247,236,227,251,0,243,225,276],
[265,267,236,231,269,255,258,0,253,266],
[259,250,245,271,251,268,276,248,0,283],
[217,235,256,240,258,227,225,235,218,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,130,130,78,269,139,78,208,0,0],
[371,0,263,247,269,247,217,371,263,139],
[371,238,0,108,269,247,108,238,0,108],
[423,254,393,0,269,263,139,393,263,263],
[232,232,232,232,0,371,232,232,202,232],
[362,254,254,238,130,0,208,332,254,254],
[423,284,393,362,269,293,0,362,124,284],
[293,130,263,108,269,169,139,0,0,0],
[501,238,501,238,299,247,377,501,0,238],
[501,362,393,238,269,247,217,501,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,245,245,286,250,280,261,272,249],
[224,0,225,235,255,223,268,229,255,236],
[256,276,0,255,274,288,297,237,288,256],
[256,266,246,0,277,277,270,235,278,247],
[215,246,227,224,0,242,245,217,249,244],
[251,278,213,224,259,0,253,240,250,238],
[221,233,204,231,256,248,0,218,216,236],
[240,272,264,266,284,261,283,0,261,260],
[229,246,213,223,252,251,285,240,0,226],
[252,265,245,254,257,263,265,241,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,249,274,291,248,251,276,229,276],
[261,0,233,286,278,235,208,257,210,263],
[252,268,0,276,290,242,245,238,223,221],
[227,215,225,0,256,219,214,241,218,211],
[210,223,211,245,0,251,230,234,243,221],
[253,266,259,282,250,0,259,278,239,258],
[250,293,256,287,271,242,0,261,239,239],
[225,244,263,260,267,223,240,0,251,266],
[272,291,278,283,258,262,262,250,0,274],
[225,238,280,290,280,243,262,235,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,199,259,297,246,232,200,247,316],
[251,0,240,285,266,285,218,256,254,281],
[302,261,0,250,276,275,224,236,251,263],
[242,216,251,0,242,278,212,181,202,287],
[204,235,225,259,0,225,166,211,162,232],
[255,216,226,223,276,0,225,231,217,267],
[269,283,277,289,335,276,0,242,248,284],
[301,245,265,320,290,270,259,0,273,326],
[254,247,250,299,339,284,253,228,0,227],
[185,220,238,214,269,234,217,175,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,216,231,232,233,222,243,245,243],
[257,0,255,232,263,228,246,254,247,244],
[285,246,0,257,270,250,254,268,263,277],
[270,269,244,0,259,240,242,260,240,242],
[269,238,231,242,0,243,232,239,231,248],
[268,273,251,261,258,0,282,260,256,249],
[279,255,247,259,269,219,0,254,263,254],
[258,247,233,241,262,241,247,0,263,235],
[256,254,238,261,270,245,238,238,0,234],
[258,257,224,259,253,252,247,266,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,234,235,239,236,225,233,232,242],
[275,0,248,264,252,266,254,269,266,266],
[267,253,0,251,261,247,248,264,260,267],
[266,237,250,0,256,243,244,245,246,252],
[262,249,240,245,0,257,245,253,256,254],
[265,235,254,258,244,0,258,248,241,244],
[276,247,253,257,256,243,0,261,258,252],
[268,232,237,256,248,253,240,0,239,249],
[269,235,241,255,245,260,243,262,0,248],
[259,235,234,249,247,257,249,252,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,258,247,233,242,255,250,282,267],
[231,0,247,251,232,242,244,239,255,240],
[243,254,0,268,221,252,245,246,267,247],
[254,250,233,0,225,236,242,245,284,255],
[268,269,280,276,0,236,265,256,286,268],
[259,259,249,265,265,0,243,263,272,255],
[246,257,256,259,236,258,0,251,283,267],
[251,262,255,256,245,238,250,0,270,246],
[219,246,234,217,215,229,218,231,0,241],
[234,261,254,246,233,246,234,255,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,257,247,253,248,259,252,247,248],
[270,0,262,257,273,256,269,249,258,260],
[244,239,0,246,263,266,250,257,247,237],
[254,244,255,0,244,266,268,258,243,247],
[248,228,238,257,0,241,240,243,245,251],
[253,245,235,235,260,0,244,257,247,240],
[242,232,251,233,261,257,0,254,239,238],
[249,252,244,243,258,244,247,0,247,247],
[254,243,254,258,256,254,262,254,0,241],
[253,241,264,254,250,261,263,254,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,241,225,233,252,244,245,265,240],
[273,0,266,251,241,247,256,278,282,265],
[260,235,0,253,248,252,266,271,260,247],
[276,250,248,0,253,265,272,272,283,260],
[268,260,253,248,0,257,258,270,269,256],
[249,254,249,236,244,0,266,270,269,233],
[257,245,235,229,243,235,0,264,266,245],
[256,223,230,229,231,231,237,0,238,237],
[236,219,241,218,232,232,235,263,0,225],
[261,236,254,241,245,268,256,264,276,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,243,237,250,238,243,243,232,229],
[251,0,236,242,242,230,250,244,241,247],
[258,265,0,245,264,245,256,247,244,244],
[264,259,256,0,252,245,258,244,261,242],
[251,259,237,249,0,250,261,241,234,242],
[263,271,256,256,251,0,251,261,249,248],
[258,251,245,243,240,250,0,247,233,262],
[258,257,254,257,260,240,254,0,253,265],
[269,260,257,240,267,252,268,248,0,258],
[272,254,257,259,259,253,239,236,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,242,242,225,270,232,220,248,237],
[274,0,283,248,252,289,284,250,271,268],
[259,218,0,227,211,240,247,226,246,244],
[259,253,274,0,243,276,241,243,276,254],
[276,249,290,258,0,297,266,275,260,241],
[231,212,261,225,204,0,228,246,230,253],
[269,217,254,260,235,273,0,244,230,256],
[281,251,275,258,226,255,257,0,241,260],
[253,230,255,225,241,271,271,260,0,261],
[264,233,257,247,260,248,245,241,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,239,263,248,259,247,200,258,254],
[235,0,260,285,271,249,249,214,251,249],
[262,241,0,257,261,223,214,223,233,222],
[238,216,244,0,230,188,199,197,230,220],
[253,230,240,271,0,220,212,205,230,234],
[242,252,278,313,281,0,238,216,256,237],
[254,252,287,302,289,263,0,229,236,268],
[301,287,278,304,296,285,272,0,261,246],
[243,250,268,271,271,245,265,240,0,255],
[247,252,279,281,267,264,233,255,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,239,258,252,258,240,271,269,237],
[252,0,269,245,258,260,244,248,274,266],
[262,232,0,228,239,254,234,244,269,227],
[243,256,273,0,268,262,244,249,267,252],
[249,243,262,233,0,236,239,258,245,243],
[243,241,247,239,265,0,231,239,271,255],
[261,257,267,257,262,270,0,273,283,241],
[230,253,257,252,243,262,228,0,240,219],
[232,227,232,234,256,230,218,261,0,215],
[264,235,274,249,258,246,260,282,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,243,248,244,235,239,254,226,255],
[247,0,235,246,224,245,232,228,235,226],
[258,266,0,249,250,251,258,247,237,253],
[253,255,252,0,245,247,262,247,228,238],
[257,277,251,256,0,258,258,269,259,246],
[266,256,250,254,243,0,255,265,244,241],
[262,269,243,239,243,246,0,245,236,247],
[247,273,254,254,232,236,256,0,236,250],
[275,266,264,273,242,257,265,265,0,268],
[246,275,248,263,255,260,254,251,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,303,266,272,217,274,222,202,304,295],
[198,0,209,212,187,268,216,214,299,238],
[235,292,0,260,260,302,277,237,285,270],
[229,289,241,0,240,304,249,241,320,265],
[284,314,241,261,0,332,279,253,336,261],
[227,233,199,197,169,0,197,165,204,218],
[279,285,224,252,222,304,0,212,287,252],
[299,287,264,260,248,336,289,0,322,280],
[197,202,216,181,165,297,214,179,0,212],
[206,263,231,236,240,283,249,221,289,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,279,217,299,288,207,275,252,244],
[240,0,216,231,245,239,188,240,211,228],
[222,285,0,244,306,290,218,273,233,272],
[284,270,257,0,281,290,199,280,239,262],
[202,256,195,220,0,232,205,295,237,238],
[213,262,211,211,269,0,185,240,227,203],
[294,313,283,302,296,316,0,307,245,288],
[226,261,228,221,206,261,194,0,238,220],
[249,290,268,262,264,274,256,263,0,281],
[257,273,229,239,263,298,213,281,220,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,294,260,238,252,246,279,245,250],
[267,0,259,245,260,274,296,283,265,283],
[207,242,0,234,219,274,251,267,230,226],
[241,256,267,0,243,290,262,253,230,242],
[263,241,282,258,0,239,289,248,271,293],
[249,227,227,211,262,0,266,210,237,234],
[255,205,250,239,212,235,0,278,242,242],
[222,218,234,248,253,291,223,0,245,243],
[256,236,271,271,230,264,259,256,0,234],
[251,218,275,259,208,267,259,258,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,254,249,256,254,243,252,268,223],
[251,0,265,235,240,257,256,271,268,232],
[247,236,0,259,227,244,254,254,244,224],
[252,266,242,0,219,260,243,249,256,258],
[245,261,274,282,0,267,251,244,287,236],
[247,244,257,241,234,0,228,245,252,250],
[258,245,247,258,250,273,0,259,270,249],
[249,230,247,252,257,256,242,0,266,253],
[233,233,257,245,214,249,231,235,0,218],
[278,269,277,243,265,251,252,248,283,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,200,225,233,195,261,301,136,367],
[255,0,185,322,340,265,288,241,263,345],
[301,316,0,346,348,254,224,269,196,387],
[276,179,155,0,254,241,212,220,166,307],
[268,161,153,247,0,224,190,272,249,235],
[306,236,247,260,277,0,246,289,159,264],
[240,213,277,289,311,255,0,216,223,320],
[200,260,232,281,229,212,285,0,141,332],
[365,238,305,335,252,342,278,360,0,331],
[134,156,114,194,266,237,181,169,170,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,260,240,256,246,267,252,253,287],
[238,0,248,251,260,247,266,257,253,280],
[241,253,0,240,240,252,267,223,237,272],
[261,250,261,0,245,240,281,248,262,272],
[245,241,261,256,0,247,281,253,264,272],
[255,254,249,261,254,0,267,255,265,268],
[234,235,234,220,220,234,0,216,236,246],
[249,244,278,253,248,246,285,0,268,271],
[248,248,264,239,237,236,265,233,0,278],
[214,221,229,229,229,233,255,230,223,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,254,242,244,258,243,287,250,260],
[238,0,197,228,205,261,243,223,213,209],
[247,304,0,264,294,292,251,265,241,247],
[259,273,237,0,287,296,255,255,263,244],
[257,296,207,214,0,272,267,274,233,216],
[243,240,209,205,229,0,225,278,214,227],
[258,258,250,246,234,276,0,286,257,231],
[214,278,236,246,227,223,215,0,228,233],
[251,288,260,238,268,287,244,273,0,229],
[241,292,254,257,285,274,270,268,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,269,258,255,249,266,248,238,248],
[263,0,260,267,273,270,290,273,251,249],
[232,241,0,254,265,257,258,249,240,259],
[243,234,247,0,266,234,249,254,228,248],
[246,228,236,235,0,238,265,249,233,226],
[252,231,244,267,263,0,270,276,236,240],
[235,211,243,252,236,231,0,249,234,235],
[253,228,252,247,252,225,252,0,217,247],
[263,250,261,273,268,265,267,284,0,268],
[253,252,242,253,275,261,266,254,233,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,262,267,266,267,252,302,267,230],
[226,0,253,214,230,220,221,281,235,213],
[239,248,0,252,256,244,245,295,247,226],
[234,287,249,0,258,248,241,301,236,258],
[235,271,245,243,0,265,237,290,261,233],
[234,281,257,253,236,0,238,281,251,241],
[249,280,256,260,264,263,0,294,245,232],
[199,220,206,200,211,220,207,0,203,208],
[234,266,254,265,240,250,256,298,0,237],
[271,288,275,243,268,260,269,293,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,239,259,254,249,273,270,255,290],
[236,0,196,221,245,242,258,241,174,306],
[262,305,0,247,298,304,325,282,290,346],
[242,280,254,0,263,272,274,275,255,254],
[247,256,203,238,0,240,283,271,183,244],
[252,259,197,229,261,0,261,272,243,236],
[228,243,176,227,218,240,0,265,165,302],
[231,260,219,226,230,229,236,0,214,269],
[246,327,211,246,318,258,336,287,0,354],
[211,195,155,247,257,265,199,232,147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,219,204,252,248,214,167,229,191],
[281,0,249,262,256,295,259,242,270,250],
[282,252,0,226,266,237,260,248,282,242],
[297,239,275,0,274,279,257,256,232,261],
[249,245,235,227,0,235,225,205,235,233],
[253,206,264,222,266,0,272,241,216,217],
[287,242,241,244,276,229,0,246,240,235],
[334,259,253,245,296,260,255,0,231,272],
[272,231,219,269,266,285,261,270,0,228],
[310,251,259,240,268,284,266,229,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,233,246,266,272,237,249,249,257],
[233,0,235,253,243,269,259,243,250,251],
[268,266,0,273,285,295,264,246,281,247],
[255,248,228,0,256,293,236,242,278,240],
[235,258,216,245,0,276,240,236,245,251],
[229,232,206,208,225,0,215,219,226,231],
[264,242,237,265,261,286,0,246,261,265],
[252,258,255,259,265,282,255,0,252,250],
[252,251,220,223,256,275,240,249,0,242],
[244,250,254,261,250,270,236,251,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,252,249,246,248,241,251,240,271],
[247,0,245,250,249,243,237,254,251,255],
[249,256,0,237,257,246,233,252,246,250],
[252,251,264,0,273,243,236,246,251,261],
[255,252,244,228,0,250,230,243,236,251],
[253,258,255,258,251,0,252,250,257,256],
[260,264,268,265,271,249,0,257,245,263],
[250,247,249,255,258,251,244,0,246,251],
[261,250,255,250,265,244,256,255,0,266],
[230,246,251,240,250,245,238,250,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,213,196,203,240,232,214,232,218],
[287,0,252,219,230,229,238,219,243,234],
[288,249,0,269,288,260,289,236,334,352],
[305,282,232,0,256,259,289,258,296,301],
[298,271,213,245,0,254,255,235,252,263],
[261,272,241,242,247,0,252,227,245,295],
[269,263,212,212,246,249,0,245,243,286],
[287,282,265,243,266,274,256,0,267,272],
[269,258,167,205,249,256,258,234,0,243],
[283,267,149,200,238,206,215,229,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,264,284,242,268,257,250,268,238],
[233,0,234,251,248,250,245,239,241,235],
[237,267,0,278,245,268,268,247,255,242],
[217,250,223,0,236,252,257,241,262,240],
[259,253,256,265,0,279,277,255,265,237],
[233,251,233,249,222,0,261,260,263,245],
[244,256,233,244,224,240,0,239,249,236],
[251,262,254,260,246,241,262,0,260,248],
[233,260,246,239,236,238,252,241,0,251],
[263,266,259,261,264,256,265,253,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,248,270,269,256,251,256,255,250],
[259,0,235,276,264,274,249,259,251,240],
[253,266,0,263,260,267,248,289,258,256],
[231,225,238,0,271,238,225,262,230,238],
[232,237,241,230,0,245,218,274,234,253],
[245,227,234,263,256,0,223,279,238,246],
[250,252,253,276,283,278,0,264,264,260],
[245,242,212,239,227,222,237,0,224,218],
[246,250,243,271,267,263,237,277,0,252],
[251,261,245,263,248,255,241,283,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,254,254,253,259,262,230,245,274],
[236,0,254,234,253,245,256,252,253,266],
[247,247,0,247,235,242,248,251,240,259],
[247,267,254,0,260,264,267,256,255,264],
[248,248,266,241,0,257,263,259,258,274],
[242,256,259,237,244,0,256,248,246,260],
[239,245,253,234,238,245,0,243,242,265],
[271,249,250,245,242,253,258,0,247,261],
[256,248,261,246,243,255,259,254,0,262],
[227,235,242,237,227,241,236,240,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,245,222,218,226,253,244,225,238],
[283,0,239,212,263,252,256,263,240,275],
[256,262,0,250,246,256,269,237,280,260],
[279,289,251,0,259,239,272,273,259,295],
[283,238,255,242,0,235,268,271,251,259],
[275,249,245,262,266,0,260,288,252,283],
[248,245,232,229,233,241,0,242,223,242],
[257,238,264,228,230,213,259,0,246,253],
[276,261,221,242,250,249,278,255,0,272],
[263,226,241,206,242,218,259,248,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,253,269,198,229,228,230,215,212],
[275,0,287,288,233,242,255,256,201,262],
[248,214,0,262,214,206,243,176,178,242],
[232,213,239,0,228,221,291,255,229,223],
[303,268,287,273,0,223,298,206,251,227],
[272,259,295,280,278,0,278,234,227,275],
[273,246,258,210,203,223,0,218,185,219],
[271,245,325,246,295,267,283,0,218,258],
[286,300,323,272,250,274,316,283,0,291],
[289,239,259,278,274,226,282,243,210,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,273,263,248,247,252,265,273,255],
[242,0,256,240,248,252,247,282,274,234],
[228,245,0,251,243,231,249,277,272,245],
[238,261,250,0,246,248,264,257,272,250],
[253,253,258,255,0,264,241,275,270,259],
[254,249,270,253,237,0,238,274,278,241],
[249,254,252,237,260,263,0,265,277,258],
[236,219,224,244,226,227,236,0,257,223],
[228,227,229,229,231,223,224,244,0,227],
[246,267,256,251,242,260,243,278,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,318,256,290,262,268,299,218,307,303],
[183,0,187,226,234,262,214,217,297,248],
[245,314,0,370,287,313,251,273,299,306],
[211,275,131,0,212,194,234,221,248,265],
[239,267,214,289,0,215,197,222,238,218],
[233,239,188,307,286,0,217,272,253,305],
[202,287,250,267,304,284,0,217,210,314],
[283,284,228,280,279,229,284,0,289,270],
[194,204,202,253,263,248,291,212,0,273],
[198,253,195,236,283,196,187,231,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,216,216,234,236,225,219,240,249],
[275,0,219,259,249,271,283,287,267,265],
[285,282,0,262,241,306,305,263,254,278],
[285,242,239,0,226,271,273,229,258,255],
[267,252,260,275,0,256,300,250,236,249],
[265,230,195,230,245,0,275,205,236,262],
[276,218,196,228,201,226,0,200,203,239],
[282,214,238,272,251,296,301,0,246,284],
[261,234,247,243,265,265,298,255,0,266],
[252,236,223,246,252,239,262,217,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,232,252,249,245,258,242,255,254],
[259,0,260,264,251,254,273,245,270,269],
[269,241,0,257,249,250,275,245,251,247],
[249,237,244,0,241,247,265,252,270,247],
[252,250,252,260,0,261,261,253,248,260],
[256,247,251,254,240,0,253,240,254,243],
[243,228,226,236,240,248,0,234,241,241],
[259,256,256,249,248,261,267,0,278,258],
[246,231,250,231,253,247,260,223,0,252],
[247,232,254,254,241,258,260,243,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,265,241,254,258,263,243,248,245],
[264,0,254,247,261,268,267,262,265,254],
[236,247,0,237,243,243,258,238,251,249],
[260,254,264,0,258,259,258,260,261,246],
[247,240,258,243,0,254,262,249,251,251],
[243,233,258,242,247,0,253,246,259,249],
[238,234,243,243,239,248,0,243,248,247],
[258,239,263,241,252,255,258,0,264,253],
[253,236,250,240,250,242,253,237,0,239],
[256,247,252,255,250,252,254,248,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,233,237,277,245,254,253,251,222],
[237,0,209,229,252,237,228,240,237,229],
[268,292,0,270,279,269,246,280,257,255],
[264,272,231,0,264,257,249,254,251,264],
[224,249,222,237,0,243,246,266,250,228],
[256,264,232,244,258,0,239,254,255,237],
[247,273,255,252,255,262,0,261,260,257],
[248,261,221,247,235,247,240,0,241,233],
[250,264,244,250,251,246,241,260,0,254],
[279,272,246,237,273,264,244,268,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,215,249,265,225,252,239,229,269],
[236,0,211,219,222,244,237,220,235,234],
[286,290,0,283,252,252,283,236,276,270],
[252,282,218,0,266,244,260,230,265,242],
[236,279,249,235,0,234,255,228,250,261],
[276,257,249,257,267,0,268,201,254,274],
[249,264,218,241,246,233,0,216,237,253],
[262,281,265,271,273,300,285,0,240,283],
[272,266,225,236,251,247,264,261,0,240],
[232,267,231,259,240,227,248,218,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,226,260,258,259,237,255,267,235],
[257,0,243,271,268,261,231,284,223,244],
[275,258,0,248,251,255,253,251,249,247],
[241,230,253,0,261,271,253,277,234,254],
[243,233,250,240,0,244,238,247,240,242],
[242,240,246,230,257,0,231,261,264,246],
[264,270,248,248,263,270,0,270,262,246],
[246,217,250,224,254,240,231,0,231,226],
[234,278,252,267,261,237,239,270,0,249],
[266,257,254,247,259,255,255,275,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,269,233,282,268,259,247,277,284],
[247,0,238,220,248,228,217,221,252,226],
[232,263,0,241,244,257,235,260,257,255],
[268,281,260,0,282,257,263,233,281,277],
[219,253,257,219,0,234,221,241,242,242],
[233,273,244,244,267,0,251,233,267,241],
[242,284,266,238,280,250,0,221,267,273],
[254,280,241,268,260,268,280,0,271,266],
[224,249,244,220,259,234,234,230,0,230],
[217,275,246,224,259,260,228,235,271,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,252,240,250,251,251,250,263,258],
[271,0,250,249,258,254,263,271,253,271],
[249,251,0,254,252,246,251,251,265,262],
[261,252,247,0,248,241,241,258,258,258],
[251,243,249,253,0,251,254,262,256,279],
[250,247,255,260,250,0,262,259,257,259],
[250,238,250,260,247,239,0,262,254,273],
[251,230,250,243,239,242,239,0,239,260],
[238,248,236,243,245,244,247,262,0,255],
[243,230,239,243,222,242,228,241,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,287,245,260,241,236,234,252,299,321],
[214,0,173,244,237,237,174,212,215,294],
[256,328,0,298,323,281,321,248,327,332],
[241,257,203,0,254,224,267,245,334,294],
[260,264,178,247,0,248,251,213,260,324],
[265,264,220,277,253,0,289,243,261,292],
[267,327,180,234,250,212,0,261,275,293],
[249,289,253,256,288,258,240,0,305,325],
[202,286,174,167,241,240,226,196,0,266],
[180,207,169,207,177,209,208,176,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 501, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_501.csv", index=False, header=False)