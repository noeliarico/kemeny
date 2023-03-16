
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,253,264,254,251,240,247,247,264,251],
[247,0,258,228,234,243,237,259,258,255],
[236,242,0,223,247,235,216,225,248,244],
[246,272,277,0,250,259,251,261,274,251],
[249,266,253,250,0,246,257,261,266,252],
[260,257,265,241,254,0,246,255,254,255],
[253,263,284,249,243,254,0,249,249,266],
[253,241,275,239,239,245,251,0,252,261],
[236,242,252,226,234,246,251,248,0,242],
[249,245,256,249,248,245,234,239,258,0]])



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
result = np.append(np.array([10, 500, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,241,254,259,251,266,237,236,241],
[251,0,244,254,254,244,254,249,258,253],
[259,256,0,260,263,232,243,252,247,244],
[246,246,240,0,261,259,258,253,234,248],
[241,246,237,239,0,250,251,240,237,254],
[249,256,268,241,250,0,271,242,253,250],
[234,246,257,242,249,229,0,241,248,252],
[263,251,248,247,260,258,259,0,252,248],
[264,242,253,266,263,247,252,248,0,262],
[259,247,256,252,246,250,248,252,238,0]])



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
result = np.append(np.array([10, 500, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,267,240,213,270,258,260,253,267],
[243,0,235,233,214,252,257,273,256,238],
[233,265,0,224,221,241,234,227,230,236],
[260,267,276,0,241,277,256,253,247,264],
[287,286,279,259,0,254,250,282,261,267],
[230,248,259,223,246,0,258,248,237,254],
[242,243,266,244,250,242,0,255,257,266],
[240,227,273,247,218,252,245,0,228,239],
[247,244,270,253,239,263,243,272,0,270],
[233,262,264,236,233,246,234,261,230,0]])



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
result = np.append(np.array([10, 500, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,254,292,252,251,247,236,231,292],
[232,0,247,266,217,245,229,237,232,294],
[246,253,0,272,244,242,267,251,198,304],
[208,234,228,0,226,202,201,243,199,280],
[248,283,256,274,0,255,249,275,241,289],
[249,255,258,298,245,0,249,266,255,302],
[253,271,233,299,251,251,0,264,227,297],
[264,263,249,257,225,234,236,0,211,288],
[269,268,302,301,259,245,273,289,0,304],
[208,206,196,220,211,198,203,212,196,0]])



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
result = np.append(np.array([10, 500, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,261,275,260,258,286,237,252,259],
[223,0,256,259,215,225,250,251,239,244],
[239,244,0,288,258,251,252,272,274,251],
[225,241,212,0,238,228,242,238,260,242],
[240,285,242,262,0,260,270,265,252,241],
[242,275,249,272,240,0,265,248,279,249],
[214,250,248,258,230,235,0,248,250,238],
[263,249,228,262,235,252,252,0,270,245],
[248,261,226,240,248,221,250,230,0,241],
[241,256,249,258,259,251,262,255,259,0]])



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
result = np.append(np.array([10, 500, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,232,249,249,230,237,227,260,242],
[277,0,263,257,273,256,258,233,269,276],
[268,237,0,258,268,250,252,254,270,273],
[251,243,242,0,250,255,237,227,254,255],
[251,227,232,250,0,227,215,212,247,239],
[270,244,250,245,273,0,249,229,243,273],
[263,242,248,263,285,251,0,234,250,259],
[273,267,246,273,288,271,266,0,286,288],
[240,231,230,246,253,257,250,214,0,255],
[258,224,227,245,261,227,241,212,245,0]])



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
result = np.append(np.array([10, 500, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,279,240,252,222,232,251,267,257,257],
[221,0,262,237,231,216,258,224,251,243],
[260,238,0,252,254,250,252,261,276,258],
[248,263,248,0,257,235,280,285,272,277],
[278,269,246,243,0,255,277,274,256,254],
[268,284,250,265,245,0,269,262,259,265],
[249,242,248,220,223,231,0,269,240,249],
[233,276,239,215,226,238,231,0,237,266],
[243,249,224,228,244,241,260,263,0,245],
[243,257,242,223,246,235,251,234,255,0]])



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
result = np.append(np.array([10, 500, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,249,204,188,227,241,212,214,282],
[236,0,219,270,244,287,263,196,243,290],
[251,281,0,252,220,238,281,210,218,269],
[296,230,248,0,254,251,322,210,275,268],
[312,256,280,246,0,308,317,200,238,289],
[273,213,262,249,192,0,255,207,233,295],
[259,237,219,178,183,245,0,188,195,213],
[288,304,290,290,300,293,312,0,223,280],
[286,257,282,225,262,267,305,277,0,298],
[218,210,231,232,211,205,287,220,202,0]])



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
result = np.append(np.array([10, 500, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,274,254,259,244,256,264,256,262],
[245,0,239,258,250,229,233,252,244,250],
[226,261,0,249,257,239,241,248,252,257],
[246,242,251,0,227,237,246,245,257,256],
[241,250,243,273,0,242,244,240,234,247],
[256,271,261,263,258,0,237,277,268,266],
[244,267,259,254,256,263,0,265,246,263],
[236,248,252,255,260,223,235,0,242,247],
[244,256,248,243,266,232,254,258,0,241],
[238,250,243,244,253,234,237,253,259,0]])



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
result = np.append(np.array([10, 500, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,244,207,221,284,160,174,262,172],
[274,0,227,306,209,363,214,331,293,264],
[256,273,0,232,276,307,227,228,230,317],
[293,194,268,0,231,331,239,176,263,287],
[279,291,224,269,0,266,248,205,222,241],
[216,137,193,169,234,0,156,225,190,238],
[340,286,273,261,252,344,0,206,348,270],
[326,169,272,324,295,275,294,0,313,282],
[238,207,270,237,278,310,152,187,0,237],
[328,236,183,213,259,262,230,218,263,0]])



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
result = np.append(np.array([10, 500, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,337,337,493,244,337,330,251,330,251],
[163,0,256,407,163,256,493,170,163,414],
[163,244,0,407,407,414,244,407,407,407],
[7,93,93,0,7,93,93,7,93,251],
[256,337,93,493,0,256,337,170,500,414],
[163,244,86,407,244,0,244,163,407,407],
[170,7,256,407,163,256,0,170,170,414],
[249,330,93,493,330,337,330,0,493,500],
[170,337,93,407,0,93,330,7,0,251],
[249,86,93,249,86,93,86,0,249,0]])



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
result = np.append(np.array([10, 500, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,246,264,239,255,247,248,256,237],
[257,0,236,258,223,260,266,244,237,253],
[254,264,0,254,252,264,242,257,255,249],
[236,242,246,0,229,253,242,247,234,254],
[261,277,248,271,0,258,260,261,269,252],
[245,240,236,247,242,0,236,238,226,231],
[253,234,258,258,240,264,0,235,245,256],
[252,256,243,253,239,262,265,0,243,249],
[244,263,245,266,231,274,255,257,0,250],
[263,247,251,246,248,269,244,251,250,0]])



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
result = np.append(np.array([10, 500, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,265,262,266,268,249,259,260,263],
[250,0,277,261,274,260,253,260,259,250],
[235,223,0,257,245,248,226,246,252,249],
[238,239,243,0,250,247,239,255,249,254],
[234,226,255,250,0,241,249,254,245,249],
[232,240,252,253,259,0,243,252,254,252],
[251,247,274,261,251,257,0,255,258,256],
[241,240,254,245,246,248,245,0,265,230],
[240,241,248,251,255,246,242,235,0,257],
[237,250,251,246,251,248,244,270,243,0]])



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
result = np.append(np.array([10, 500, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,154,289,204,221,252,255,204,304,210],
[346,0,343,203,278,310,250,269,322,274],
[211,157,0,177,184,150,192,140,177,196],
[296,297,323,0,308,263,287,354,323,232],
[279,222,316,192,0,286,216,309,356,216],
[248,190,350,237,214,0,209,182,213,210],
[245,250,308,213,284,291,0,277,333,216],
[296,231,360,146,191,318,223,0,335,299],
[196,178,323,177,144,287,167,165,0,194],
[290,226,304,268,284,290,284,201,306,0]])



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
result = np.append(np.array([10, 500, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,210,245,217,203,228,256,229,215],
[282,0,236,291,262,248,270,295,245,247],
[290,264,0,299,250,242,252,302,266,258],
[255,209,201,0,215,231,216,271,230,227],
[283,238,250,285,0,236,264,281,250,258],
[297,252,258,269,264,0,241,308,246,283],
[272,230,248,284,236,259,0,302,241,241],
[244,205,198,229,219,192,198,0,221,226],
[271,255,234,270,250,254,259,279,0,258],
[285,253,242,273,242,217,259,274,242,0]])



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
result = np.append(np.array([10, 500, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,255,255,259,245,269,237,255,234],
[245,0,263,266,267,260,269,265,264,258],
[245,237,0,230,253,236,252,250,251,241],
[245,234,270,0,258,247,254,244,242,237],
[241,233,247,242,0,236,245,228,252,256],
[255,240,264,253,264,0,267,234,255,228],
[231,231,248,246,255,233,0,235,243,229],
[263,235,250,256,272,266,265,0,261,243],
[245,236,249,258,248,245,257,239,0,249],
[266,242,259,263,244,272,271,257,251,0]])



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
result = np.append(np.array([10, 500, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,266,278,266,295,265,267,240,234],
[250,0,290,284,265,270,240,255,248,247],
[234,210,0,257,269,283,231,230,216,234],
[222,216,243,0,257,284,250,246,204,222],
[234,235,231,243,0,250,249,229,256,211],
[205,230,217,216,250,0,221,247,219,235],
[235,260,269,250,251,279,0,251,223,253],
[233,245,270,254,271,253,249,0,245,225],
[260,252,284,296,244,281,277,255,0,273],
[266,253,266,278,289,265,247,275,227,0]])



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
result = np.append(np.array([10, 500, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,335,239,262,245,281,207,332,302,224],
[165,0,166,214,117,251,91,270,241,159],
[261,334,0,300,256,277,153,297,276,285],
[238,286,200,0,217,247,265,287,275,207],
[255,383,244,283,0,307,236,307,280,226],
[219,249,223,253,193,0,173,212,220,170],
[293,409,347,235,264,327,0,377,321,287],
[168,230,203,213,193,288,123,0,288,194],
[198,259,224,225,220,280,179,212,0,188],
[276,341,215,293,274,330,213,306,312,0]])



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
result = np.append(np.array([10, 500, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,252,257,242,248,247,246,260,272],
[269,0,265,269,260,260,263,239,240,251],
[248,235,0,260,248,228,235,238,221,242],
[243,231,240,0,257,237,248,229,218,228],
[258,240,252,243,0,245,246,241,229,249],
[252,240,272,263,255,0,241,255,251,255],
[253,237,265,252,254,259,0,228,232,251],
[254,261,262,271,259,245,272,0,263,263],
[240,260,279,282,271,249,268,237,0,247],
[228,249,258,272,251,245,249,237,253,0]])



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
result = np.append(np.array([10, 500, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,300,269,285,230,275,252,267,296],
[271,0,277,253,256,276,245,225,250,291],
[200,223,0,267,220,214,237,216,247,269],
[231,247,233,0,231,247,219,215,239,267],
[215,244,280,269,0,268,253,264,266,304],
[270,224,286,253,232,0,253,237,257,281],
[225,255,263,281,247,247,0,247,264,274],
[248,275,284,285,236,263,253,0,277,317],
[233,250,253,261,234,243,236,223,0,287],
[204,209,231,233,196,219,226,183,213,0]])



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
result = np.append(np.array([10, 500, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,250,263,244,247,239,234,257,258],
[272,0,251,254,246,259,266,251,279,267],
[250,249,0,256,237,232,235,239,243,246],
[237,246,244,0,221,237,234,225,258,235],
[256,254,263,279,0,260,258,243,268,252],
[253,241,268,263,240,0,265,247,256,242],
[261,234,265,266,242,235,0,221,250,244],
[266,249,261,275,257,253,279,0,276,260],
[243,221,257,242,232,244,250,224,0,239],
[242,233,254,265,248,258,256,240,261,0]])



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
result = np.append(np.array([10, 500, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,256,225,278,255,246,230,273,234],
[264,0,291,253,276,290,299,239,308,265],
[244,209,0,235,272,239,223,192,253,176],
[275,247,265,0,288,258,250,247,260,232],
[222,224,228,212,0,258,232,219,240,207],
[245,210,261,242,242,0,249,255,265,268],
[254,201,277,250,268,251,0,190,255,202],
[270,261,308,253,281,245,310,0,271,264],
[227,192,247,240,260,235,245,229,0,210],
[266,235,324,268,293,232,298,236,290,0]])



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
result = np.append(np.array([10, 500, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,261,258,246,272,277,270,250,287],
[244,0,237,248,255,255,237,255,217,249],
[239,263,0,241,241,286,259,256,216,263],
[242,252,259,0,255,271,260,269,269,278],
[254,245,259,245,0,258,252,257,231,247],
[228,245,214,229,242,0,227,220,201,252],
[223,263,241,240,248,273,0,279,242,259],
[230,245,244,231,243,280,221,0,221,228],
[250,283,284,231,269,299,258,279,0,281],
[213,251,237,222,253,248,241,272,219,0]])



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
result = np.append(np.array([10, 500, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,229,221,240,214,255,219,238,231],
[266,0,235,231,235,241,245,224,245,246],
[271,265,0,257,253,257,269,251,248,256],
[279,269,243,0,257,243,275,233,260,261],
[260,265,247,243,0,232,245,241,254,264],
[286,259,243,257,268,0,260,250,253,252],
[245,255,231,225,255,240,0,233,252,237],
[281,276,249,267,259,250,267,0,258,275],
[262,255,252,240,246,247,248,242,0,238],
[269,254,244,239,236,248,263,225,262,0]])



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
result = np.append(np.array([10, 500, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,258,256,258,256,268,253,258,248],
[228,0,238,253,243,286,246,272,252,213],
[242,262,0,224,242,273,246,271,237,258],
[244,247,276,0,241,252,288,248,239,224],
[242,257,258,259,0,273,253,264,234,224],
[244,214,227,248,227,0,234,244,198,205],
[232,254,254,212,247,266,0,263,247,223],
[247,228,229,252,236,256,237,0,209,208],
[242,248,263,261,266,302,253,291,0,238],
[252,287,242,276,276,295,277,292,262,0]])



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
result = np.append(np.array([10, 500, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,253,268,255,254,261,253,244,257],
[249,0,252,258,238,244,256,260,248,243],
[247,248,0,262,238,251,249,240,252,246],
[232,242,238,0,228,241,253,249,231,231],
[245,262,262,272,0,263,259,253,259,250],
[246,256,249,259,237,0,272,253,246,249],
[239,244,251,247,241,228,0,247,257,234],
[247,240,260,251,247,247,253,0,243,239],
[256,252,248,269,241,254,243,257,0,245],
[243,257,254,269,250,251,266,261,255,0]])



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
result = np.append(np.array([10, 500, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,206,238,237,253,250,216,220,225,246],
[294,0,273,245,301,260,241,242,291,293],
[262,227,0,258,262,232,238,195,244,270],
[263,255,242,0,283,241,254,263,248,299],
[247,199,238,217,0,204,238,197,197,261],
[250,240,268,259,296,0,258,228,254,260],
[284,259,262,246,262,242,0,281,264,297],
[280,258,305,237,303,272,219,0,272,292],
[275,209,256,252,303,246,236,228,0,277],
[254,207,230,201,239,240,203,208,223,0]])



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
result = np.append(np.array([10, 500, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,269,246,255,247,255,292,273,242],
[260,0,240,242,218,217,252,256,240,232],
[231,260,0,211,238,235,223,248,271,243],
[254,258,289,0,260,276,249,298,280,271],
[245,282,262,240,0,259,234,287,234,287],
[253,283,265,224,241,0,260,276,275,292],
[245,248,277,251,266,240,0,294,264,261],
[208,244,252,202,213,224,206,0,232,210],
[227,260,229,220,266,225,236,268,0,231],
[258,268,257,229,213,208,239,290,269,0]])



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
result = np.append(np.array([10, 500, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,259,235,247,260,236,252,232,251],
[258,0,253,246,241,239,240,250,240,259],
[241,247,0,252,241,237,244,236,234,262],
[265,254,248,0,247,242,243,243,243,246],
[253,259,259,253,0,247,251,255,242,265],
[240,261,263,258,253,0,254,245,254,265],
[264,260,256,257,249,246,0,250,253,255],
[248,250,264,257,245,255,250,0,233,247],
[268,260,266,257,258,246,247,267,0,271],
[249,241,238,254,235,235,245,253,229,0]])



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
result = np.append(np.array([10, 500, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,263,256,248,248,247,235,240,261],
[271,0,259,276,249,277,290,265,262,261],
[237,241,0,236,242,234,250,242,245,252],
[244,224,264,0,252,244,258,237,261,254],
[252,251,258,248,0,246,260,250,248,259],
[252,223,266,256,254,0,247,258,254,244],
[253,210,250,242,240,253,0,236,266,249],
[265,235,258,263,250,242,264,0,279,256],
[260,238,255,239,252,246,234,221,0,245],
[239,239,248,246,241,256,251,244,255,0]])



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
result = np.append(np.array([10, 500, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,249,242,254,251,252,250,243,237],
[254,0,228,238,250,242,230,253,238,250],
[251,272,0,247,262,261,254,268,257,250],
[258,262,253,0,249,257,248,261,246,264],
[246,250,238,251,0,256,248,257,248,241],
[249,258,239,243,244,0,222,248,233,245],
[248,270,246,252,252,278,0,249,243,253],
[250,247,232,239,243,252,251,0,248,255],
[257,262,243,254,252,267,257,252,0,269],
[263,250,250,236,259,255,247,245,231,0]])



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
result = np.append(np.array([10, 500, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,249,271,249,247,248,282,260,243],
[261,0,255,256,261,259,254,284,248,251],
[251,245,0,267,263,265,254,258,249,254],
[229,244,233,0,248,237,246,258,240,260],
[251,239,237,252,0,236,262,267,245,243],
[253,241,235,263,264,0,248,266,259,245],
[252,246,246,254,238,252,0,269,256,255],
[218,216,242,242,233,234,231,0,219,234],
[240,252,251,260,255,241,244,281,0,266],
[257,249,246,240,257,255,245,266,234,0]])



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
result = np.append(np.array([10, 500, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,269,291,278,283,267,272,289,305],
[255,0,267,267,237,268,277,262,251,288],
[231,233,0,233,265,241,262,244,249,275],
[209,233,267,0,247,263,249,252,226,256],
[222,263,235,253,0,274,233,248,230,251],
[217,232,259,237,226,0,237,238,224,250],
[233,223,238,251,267,263,0,237,251,258],
[228,238,256,248,252,262,263,0,258,278],
[211,249,251,274,270,276,249,242,0,275],
[195,212,225,244,249,250,242,222,225,0]])



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
result = np.append(np.array([10, 500, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,181,310,233,321,245,315,240,293],
[262,0,227,253,184,220,221,259,249,265],
[319,273,0,216,219,295,236,246,281,273],
[190,247,284,0,223,272,225,292,211,244],
[267,316,281,277,0,307,284,295,245,301],
[179,280,205,228,193,0,246,196,220,264],
[255,279,264,275,216,254,0,317,284,302],
[185,241,254,208,205,304,183,0,197,284],
[260,251,219,289,255,280,216,303,0,308],
[207,235,227,256,199,236,198,216,192,0]])



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
result = np.append(np.array([10, 500, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,256,251,239,264,244,250,252,207],
[244,0,259,236,227,280,242,269,259,241],
[244,241,0,245,234,248,230,232,242,244],
[249,264,255,0,239,243,256,257,274,244],
[261,273,266,261,0,287,283,265,290,250],
[236,220,252,257,213,0,255,213,250,226],
[256,258,270,244,217,245,0,258,267,231],
[250,231,268,243,235,287,242,0,288,264],
[248,241,258,226,210,250,233,212,0,219],
[293,259,256,256,250,274,269,236,281,0]])



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
result = np.append(np.array([10, 500, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,238,252,232,245,247,248,240,246],
[267,0,250,259,265,258,268,252,262,269],
[262,250,0,243,250,239,267,257,251,254],
[248,241,257,0,242,258,257,245,247,260],
[268,235,250,258,0,253,274,258,264,246],
[255,242,261,242,247,0,259,260,253,252],
[253,232,233,243,226,241,0,237,245,256],
[252,248,243,255,242,240,263,0,255,273],
[260,238,249,253,236,247,255,245,0,259],
[254,231,246,240,254,248,244,227,241,0]])



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
result = np.append(np.array([10, 500, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,260,290,259,252,255,279,235,252],
[247,0,254,296,240,264,268,285,243,250],
[240,246,0,269,281,250,251,247,258,251],
[210,204,231,0,233,200,217,249,210,220],
[241,260,219,267,0,213,234,221,228,236],
[248,236,250,300,287,0,247,249,261,238],
[245,232,249,283,266,253,0,243,225,257],
[221,215,253,251,279,251,257,0,266,258],
[265,257,242,290,272,239,275,234,0,259],
[248,250,249,280,264,262,243,242,241,0]])



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
result = np.append(np.array([10, 500, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,234,256,227,237,226,263,255,243],
[236,0,223,247,261,208,237,260,261,239],
[266,277,0,268,252,246,267,271,282,272],
[244,253,232,0,248,246,248,263,263,251],
[273,239,248,252,0,254,257,245,262,230],
[263,292,254,254,246,0,266,265,285,253],
[274,263,233,252,243,234,0,260,267,244],
[237,240,229,237,255,235,240,0,263,226],
[245,239,218,237,238,215,233,237,0,235],
[257,261,228,249,270,247,256,274,265,0]])



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
result = np.append(np.array([10, 500, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,269,253,255,279,263,242,272,252],
[251,0,246,257,270,280,272,240,273,241],
[231,254,0,231,252,277,249,234,248,234],
[247,243,269,0,241,272,257,269,263,239],
[245,230,248,259,0,294,265,237,265,239],
[221,220,223,228,206,0,230,203,232,191],
[237,228,251,243,235,270,0,244,258,233],
[258,260,266,231,263,297,256,0,274,241],
[228,227,252,237,235,268,242,226,0,239],
[248,259,266,261,261,309,267,259,261,0]])



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
result = np.append(np.array([10, 500, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,223,203,210,256,251,243,222,229],
[262,0,210,220,197,263,239,243,177,236],
[277,290,0,248,230,284,252,278,250,226],
[297,280,252,0,211,253,243,269,259,252],
[290,303,270,289,0,292,280,264,272,245],
[244,237,216,247,208,0,207,213,258,172],
[249,261,248,257,220,293,0,258,244,241],
[257,257,222,231,236,287,242,0,238,215],
[278,323,250,241,228,242,256,262,0,235],
[271,264,274,248,255,328,259,285,265,0]])



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
result = np.append(np.array([10, 500, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,252,235,241,227,222,247,241,227],
[264,0,266,255,276,264,253,266,238,249],
[248,234,0,258,269,237,252,258,230,250],
[265,245,242,0,258,248,239,267,229,246],
[259,224,231,242,0,226,232,234,221,221],
[273,236,263,252,274,0,246,257,248,243],
[278,247,248,261,268,254,0,273,245,246],
[253,234,242,233,266,243,227,0,227,244],
[259,262,270,271,279,252,255,273,0,246],
[273,251,250,254,279,257,254,256,254,0]])



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
result = np.append(np.array([10, 500, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,248,253,261,224,246,255,263,234],
[243,0,252,258,246,257,258,284,262,250],
[252,248,0,246,248,257,239,269,261,228],
[247,242,254,0,254,247,249,277,265,262],
[239,254,252,246,0,250,255,267,257,240],
[276,243,243,253,250,0,249,281,270,244],
[254,242,261,251,245,251,0,268,254,241],
[245,216,231,223,233,219,232,0,233,230],
[237,238,239,235,243,230,246,267,0,229],
[266,250,272,238,260,256,259,270,271,0]])



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
result = np.append(np.array([10, 500, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,276,267,274,244,238,284,282,282],
[230,0,198,256,240,231,235,253,246,237],
[224,302,0,266,262,281,240,266,272,256],
[233,244,234,0,259,229,264,276,245,229],
[226,260,238,241,0,247,288,274,291,266],
[256,269,219,271,253,0,261,261,255,237],
[262,265,260,236,212,239,0,273,301,258],
[216,247,234,224,226,239,227,0,250,252],
[218,254,228,255,209,245,199,250,0,230],
[218,263,244,271,234,263,242,248,270,0]])



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
result = np.append(np.array([10, 500, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,245,223,239,239,269,232,230,253],
[234,0,233,204,241,230,250,237,216,254],
[255,267,0,237,250,258,257,271,222,260],
[277,296,263,0,250,254,275,254,269,288],
[261,259,250,250,0,249,270,237,242,278],
[261,270,242,246,251,0,273,248,239,269],
[231,250,243,225,230,227,0,236,217,258],
[268,263,229,246,263,252,264,0,227,261],
[270,284,278,231,258,261,283,273,0,265],
[247,246,240,212,222,231,242,239,235,0]])



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
result = np.append(np.array([10, 500, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,282,240,261,256,233,235,254,262],
[261,0,284,257,259,274,261,266,283,238],
[218,216,0,233,242,222,197,223,234,196],
[260,243,267,0,242,232,229,216,225,217],
[239,241,258,258,0,238,221,238,234,214],
[244,226,278,268,262,0,267,254,269,255],
[267,239,303,271,279,233,0,240,258,249],
[265,234,277,284,262,246,260,0,260,267],
[246,217,266,275,266,231,242,240,0,272],
[238,262,304,283,286,245,251,233,228,0]])



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
result = np.append(np.array([10, 500, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,209,229,262,233,229,239,214,254,224],
[291,0,232,271,251,266,260,257,287,276],
[271,268,0,267,286,287,273,243,296,292],
[238,229,233,0,242,245,249,216,195,243],
[267,249,214,258,0,254,269,230,254,249],
[271,234,213,255,246,0,215,236,231,287],
[261,240,227,251,231,285,0,261,258,258],
[286,243,257,284,270,264,239,0,295,267],
[246,213,204,305,246,269,242,205,0,287],
[276,224,208,257,251,213,242,233,213,0]])



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
result = np.append(np.array([10, 500, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,325,230,281,298,375,214,284,308,230],
[175,0,208,245,257,251,198,250,207,245],
[270,292,0,268,269,259,209,250,323,291],
[219,255,232,0,308,279,257,255,294,288],
[202,243,231,192,0,264,222,245,230,242],
[125,249,241,221,236,0,176,209,224,234],
[286,302,291,243,278,324,0,246,307,308],
[216,250,250,245,255,291,254,0,302,287],
[192,293,177,206,270,276,193,198,0,243],
[270,255,209,212,258,266,192,213,257,0]])



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
result = np.append(np.array([10, 500, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,250,246,250,254,251,262,279,247],
[246,0,249,253,248,234,251,235,261,238],
[250,251,0,255,252,247,252,247,258,246],
[254,247,245,0,250,229,233,254,247,248],
[250,252,248,250,0,248,224,239,258,251],
[246,266,253,271,252,0,271,246,272,256],
[249,249,248,267,276,229,0,253,258,243],
[238,265,253,246,261,254,247,0,260,239],
[221,239,242,253,242,228,242,240,0,244],
[253,262,254,252,249,244,257,261,256,0]])



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
result = np.append(np.array([10, 500, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,253,247,251,238,230,224,231,239],
[263,0,264,267,272,247,244,249,259,260],
[247,236,0,251,251,244,228,254,251,240],
[253,233,249,0,248,248,230,245,257,246],
[249,228,249,252,0,243,231,249,244,238],
[262,253,256,252,257,0,241,244,255,236],
[270,256,272,270,269,259,0,260,262,250],
[276,251,246,255,251,256,240,0,259,248],
[269,241,249,243,256,245,238,241,0,238],
[261,240,260,254,262,264,250,252,262,0]])



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
result = np.append(np.array([10, 500, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,276,267,254,263,259,244,254,264],
[246,0,253,267,241,234,239,251,230,252],
[224,247,0,251,228,254,229,242,234,249],
[233,233,249,0,244,238,234,240,225,239],
[246,259,272,256,0,239,241,265,253,254],
[237,266,246,262,261,0,245,256,242,255],
[241,261,271,266,259,255,0,248,245,261],
[256,249,258,260,235,244,252,0,247,253],
[246,270,266,275,247,258,255,253,0,257],
[236,248,251,261,246,245,239,247,243,0]])



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
result = np.append(np.array([10, 500, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,247,243,247,247,232,242,259,255],
[231,0,250,246,236,251,234,257,259,254],
[253,250,0,241,253,237,251,282,256,267],
[257,254,259,0,241,245,237,268,257,255],
[253,264,247,259,0,244,239,267,258,257],
[253,249,263,255,256,0,241,249,248,241],
[268,266,249,263,261,259,0,262,259,252],
[258,243,218,232,233,251,238,0,243,244],
[241,241,244,243,242,252,241,257,0,247],
[245,246,233,245,243,259,248,256,253,0]])



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
result = np.append(np.array([10, 500, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,208,280,217,222,260,227,243,233,216],
[292,0,308,280,250,250,268,284,249,279],
[220,192,0,201,207,202,190,233,230,201],
[283,220,299,0,229,254,246,233,256,249],
[278,250,293,271,0,263,239,312,249,251],
[240,250,298,246,237,0,242,271,263,238],
[273,232,310,254,261,258,0,255,238,252],
[257,216,267,267,188,229,245,0,240,223],
[267,251,270,244,251,237,262,260,0,223],
[284,221,299,251,249,262,248,277,277,0]])



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
result = np.append(np.array([10, 500, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,248,264,249,251,256,238,266,281],
[247,0,242,267,239,261,236,236,234,259],
[252,258,0,276,254,252,246,246,255,275],
[236,233,224,0,236,241,233,233,231,245],
[251,261,246,264,0,250,250,249,240,259],
[249,239,248,259,250,0,243,252,234,252],
[244,264,254,267,250,257,0,242,251,269],
[262,264,254,267,251,248,258,0,269,255],
[234,266,245,269,260,266,249,231,0,277],
[219,241,225,255,241,248,231,245,223,0]])



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
result = np.append(np.array([10, 500, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,248,247,251,257,256,256,260,264],
[243,0,238,240,252,260,246,255,264,277],
[252,262,0,253,256,264,254,249,261,272],
[253,260,247,0,253,250,261,255,266,262],
[249,248,244,247,0,256,238,254,262,257],
[243,240,236,250,244,0,249,241,256,273],
[244,254,246,239,262,251,0,235,259,264],
[244,245,251,245,246,259,265,0,265,267],
[240,236,239,234,238,244,241,235,0,245],
[236,223,228,238,243,227,236,233,255,0]])



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
result = np.append(np.array([10, 500, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,149,172,149,219,204,204,204,219,219],
[351,0,262,71,253,211,335,216,381,226],
[328,238,0,238,253,204,365,365,253,253],
[351,429,262,0,223,429,429,317,351,317],
[281,247,247,277,0,284,247,302,299,354],
[296,289,296,71,216,0,223,344,326,351],
[296,165,135,71,253,277,0,381,326,354],
[296,284,135,183,198,156,119,0,333,299],
[281,119,247,149,201,174,174,167,0,62],
[281,274,247,183,146,149,146,201,438,0]])



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
result = np.append(np.array([10, 500, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,246,280,237,273,263,262,302,275],
[250,0,250,265,247,266,247,247,279,260],
[254,250,0,276,257,278,252,249,275,255],
[220,235,224,0,225,259,246,249,263,251],
[263,253,243,275,0,276,273,263,290,256],
[227,234,222,241,224,0,234,235,243,231],
[237,253,248,254,227,266,0,247,267,252],
[238,253,251,251,237,265,253,0,268,239],
[198,221,225,237,210,257,233,232,0,229],
[225,240,245,249,244,269,248,261,271,0]])



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
result = np.append(np.array([10, 500, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,244,226,234,262,243,252,264,252],
[260,0,243,237,243,259,249,247,256,255],
[256,257,0,256,248,258,253,260,265,285],
[274,263,244,0,258,260,214,249,252,252],
[266,257,252,242,0,263,256,271,261,252],
[238,241,242,240,237,0,230,244,251,248],
[257,251,247,286,244,270,0,260,258,262],
[248,253,240,251,229,256,240,0,248,262],
[236,244,235,248,239,249,242,252,0,236],
[248,245,215,248,248,252,238,238,264,0]])



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
result = np.append(np.array([10, 500, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,259,287,248,270,276,280,260,256],
[250,0,261,253,258,264,288,272,257,248],
[241,239,0,249,241,238,254,245,258,242],
[213,247,251,0,238,259,259,247,245,236],
[252,242,259,262,0,251,270,269,241,243],
[230,236,262,241,249,0,260,259,246,243],
[224,212,246,241,230,240,0,250,247,240],
[220,228,255,253,231,241,250,0,231,244],
[240,243,242,255,259,254,253,269,0,237],
[244,252,258,264,257,257,260,256,263,0]])



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
result = np.append(np.array([10, 500, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,231,259,237,258,259,227,229,230],
[259,0,252,249,252,242,253,245,243,289],
[269,248,0,232,268,269,302,215,261,282],
[241,251,268,0,248,249,259,203,220,272],
[263,248,232,252,0,258,273,240,270,267],
[242,258,231,251,242,0,272,223,219,280],
[241,247,198,241,227,228,0,205,224,231],
[273,255,285,297,260,277,295,0,247,279],
[271,257,239,280,230,281,276,253,0,304],
[270,211,218,228,233,220,269,221,196,0]])



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
result = np.append(np.array([10, 500, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,272,256,250,249,250,253,273,262],
[235,0,255,256,254,249,244,240,257,251],
[228,245,0,255,249,251,236,236,263,252],
[244,244,245,0,239,266,235,237,252,256],
[250,246,251,261,0,265,240,230,274,254],
[251,251,249,234,235,0,237,224,251,253],
[250,256,264,265,260,263,0,258,266,263],
[247,260,264,263,270,276,242,0,266,263],
[227,243,237,248,226,249,234,234,0,249],
[238,249,248,244,246,247,237,237,251,0]])



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
result = np.append(np.array([10, 500, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,204,219,250,254,233,240,231,264],
[281,0,281,270,245,291,269,258,254,318],
[296,219,0,240,240,234,250,235,240,267],
[281,230,260,0,244,250,250,247,246,262],
[250,255,260,256,0,273,245,232,256,296],
[246,209,266,250,227,0,242,215,241,241],
[267,231,250,250,255,258,0,261,237,259],
[260,242,265,253,268,285,239,0,235,302],
[269,246,260,254,244,259,263,265,0,271],
[236,182,233,238,204,259,241,198,229,0]])



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
result = np.append(np.array([10, 500, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,259,278,255,243,264,250,255,280],
[233,0,251,254,250,251,275,252,258,274],
[241,249,0,241,256,269,280,252,260,283],
[222,246,259,0,249,234,263,231,248,263],
[245,250,244,251,0,239,269,234,268,259],
[257,249,231,266,261,0,282,253,268,267],
[236,225,220,237,231,218,0,223,241,253],
[250,248,248,269,266,247,277,0,263,272],
[245,242,240,252,232,232,259,237,0,288],
[220,226,217,237,241,233,247,228,212,0]])



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
result = np.append(np.array([10, 500, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,237,239,228,249,242,243,225,230],
[254,0,234,237,244,266,238,222,213,219],
[263,266,0,247,250,270,218,267,254,258],
[261,263,253,0,252,273,231,267,233,242],
[272,256,250,248,0,286,253,265,242,252],
[251,234,230,227,214,0,224,249,234,239],
[258,262,282,269,247,276,0,280,265,259],
[257,278,233,233,235,251,220,0,256,222],
[275,287,246,267,258,266,235,244,0,249],
[270,281,242,258,248,261,241,278,251,0]])



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
result = np.append(np.array([10, 500, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,237,227,256,260,233,251,245,246],
[255,0,268,238,265,277,255,268,251,240],
[263,232,0,239,274,285,252,258,246,261],
[273,262,261,0,296,261,247,276,270,268],
[244,235,226,204,0,252,232,247,245,238],
[240,223,215,239,248,0,232,240,242,259],
[267,245,248,253,268,268,0,261,244,241],
[249,232,242,224,253,260,239,0,238,243],
[255,249,254,230,255,258,256,262,0,238],
[254,260,239,232,262,241,259,257,262,0]])



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
result = np.append(np.array([10, 500, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,260,262,260,253,253,253,243,261],
[246,0,238,251,246,244,257,256,235,253],
[240,262,0,266,243,250,277,247,244,273],
[238,249,234,0,247,233,269,236,231,262],
[240,254,257,253,0,238,255,247,244,247],
[247,256,250,267,262,0,275,251,251,262],
[247,243,223,231,245,225,0,234,228,236],
[247,244,253,264,253,249,266,0,238,258],
[257,265,256,269,256,249,272,262,0,257],
[239,247,227,238,253,238,264,242,243,0]])



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
result = np.append(np.array([10, 500, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,269,254,249,251,268,224,256,255],
[256,0,266,261,253,266,242,243,259,255],
[231,234,0,254,250,251,250,250,252,246],
[246,239,246,0,234,259,246,238,255,245],
[251,247,250,266,0,259,240,241,257,253],
[249,234,249,241,241,0,249,238,264,258],
[232,258,250,254,260,251,0,240,255,249],
[276,257,250,262,259,262,260,0,261,258],
[244,241,248,245,243,236,245,239,0,258],
[245,245,254,255,247,242,251,242,242,0]])



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
result = np.append(np.array([10, 500, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,219,268,224,204,249,276,178,295],
[279,0,240,253,270,259,278,279,243,306],
[281,260,0,234,257,229,215,304,204,326],
[232,247,266,0,210,254,250,251,209,311],
[276,230,243,290,0,253,248,304,244,302],
[296,241,271,246,247,0,264,258,273,305],
[251,222,285,250,252,236,0,210,212,283],
[224,221,196,249,196,242,290,0,220,247],
[322,257,296,291,256,227,288,280,0,333],
[205,194,174,189,198,195,217,253,167,0]])



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
result = np.append(np.array([10, 500, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,241,238,255,239,243,226,228,233],
[245,0,262,253,253,260,251,252,246,248],
[259,238,0,261,254,250,265,239,228,232],
[262,247,239,0,253,245,244,232,236,242],
[245,247,246,247,0,247,256,230,238,232],
[261,240,250,255,253,0,238,251,245,234],
[257,249,235,256,244,262,0,243,243,238],
[274,248,261,268,270,249,257,0,242,252],
[272,254,272,264,262,255,257,258,0,249],
[267,252,268,258,268,266,262,248,251,0]])



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
result = np.append(np.array([10, 500, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,254,217,246,223,261,239,238,242],
[260,0,259,237,260,242,263,238,256,239],
[246,241,0,233,261,242,274,238,244,233],
[283,263,267,0,275,255,280,266,250,246],
[254,240,239,225,0,215,248,236,237,235],
[277,258,258,245,285,0,277,261,266,259],
[239,237,226,220,252,223,0,232,234,231],
[261,262,262,234,264,239,268,0,253,243],
[262,244,256,250,263,234,266,247,0,256],
[258,261,267,254,265,241,269,257,244,0]])



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
result = np.append(np.array([10, 500, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,251,241,269,237,243,273,254,240],
[255,0,269,256,255,239,244,249,267,239],
[249,231,0,255,247,247,251,253,251,243],
[259,244,245,0,254,234,252,254,257,252],
[231,245,253,246,0,234,232,247,243,229],
[263,261,253,266,266,0,243,271,259,252],
[257,256,249,248,268,257,0,261,252,253],
[227,251,247,246,253,229,239,0,246,262],
[246,233,249,243,257,241,248,254,0,246],
[260,261,257,248,271,248,247,238,254,0]])



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
result = np.append(np.array([10, 500, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,294,245,336,253,267,250,334,232,295],
[206,0,299,289,320,223,299,337,237,316],
[255,201,0,313,242,239,296,338,261,295],
[164,211,187,0,222,205,250,244,180,274],
[247,180,258,278,0,272,257,271,173,264],
[233,277,261,295,228,0,267,271,219,273],
[250,201,204,250,243,233,0,251,216,224],
[166,163,162,256,229,229,249,0,181,231],
[268,263,239,320,327,281,284,319,0,334],
[205,184,205,226,236,227,276,269,166,0]])



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
result = np.append(np.array([10, 500, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,241,235,274,235,287,240,219,199],
[268,0,238,208,242,228,259,247,253,216],
[259,262,0,231,266,226,293,257,231,247],
[265,292,269,0,281,270,321,300,231,251],
[226,258,234,219,0,223,273,241,228,228],
[265,272,274,230,277,0,302,257,235,252],
[213,241,207,179,227,198,0,237,198,222],
[260,253,243,200,259,243,263,0,214,229],
[281,247,269,269,272,265,302,286,0,255],
[301,284,253,249,272,248,278,271,245,0]])



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
result = np.append(np.array([10, 500, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,278,257,253,247,263,251,247,275],
[223,0,220,233,234,224,256,250,198,259],
[222,280,0,255,256,238,268,250,225,253],
[243,267,245,0,251,240,265,264,239,262],
[247,266,244,249,0,220,265,246,235,266],
[253,276,262,260,280,0,273,248,252,253],
[237,244,232,235,235,227,0,237,219,266],
[249,250,250,236,254,252,263,0,247,276],
[253,302,275,261,265,248,281,253,0,278],
[225,241,247,238,234,247,234,224,222,0]])



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
result = np.append(np.array([10, 500, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,240,217,213,206,239,214,213,212],
[281,0,254,236,239,263,245,230,269,229],
[260,246,0,243,245,246,247,227,244,244],
[283,264,257,0,250,259,263,256,270,258],
[287,261,255,250,0,248,259,254,245,218],
[294,237,254,241,252,0,247,232,263,233],
[261,255,253,237,241,253,0,232,236,250],
[286,270,273,244,246,268,268,0,244,255],
[287,231,256,230,255,237,264,256,0,240],
[288,271,256,242,282,267,250,245,260,0]])



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
result = np.append(np.array([10, 500, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,301,260,248,308,283,235,298,291,265],
[199,0,261,238,279,248,220,238,230,227],
[240,239,0,215,288,273,235,236,257,240],
[252,262,285,0,294,246,247,256,257,237],
[192,221,212,206,0,230,184,200,235,194],
[217,252,227,254,270,0,247,225,244,235],
[265,280,265,253,316,253,0,266,281,234],
[202,262,264,244,300,275,234,0,251,247],
[209,270,243,243,265,256,219,249,0,247],
[235,273,260,263,306,265,266,253,253,0]])



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
result = np.append(np.array([10, 500, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,280,248,255,266,264,256,245,264],
[236,0,286,249,254,260,254,268,249,265],
[220,214,0,219,233,239,227,226,212,235],
[252,251,281,0,255,267,250,259,249,251],
[245,246,267,245,0,263,253,262,245,245],
[234,240,261,233,237,0,238,262,236,232],
[236,246,273,250,247,262,0,269,259,267],
[244,232,274,241,238,238,231,0,229,250],
[255,251,288,251,255,264,241,271,0,255],
[236,235,265,249,255,268,233,250,245,0]])



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
result = np.append(np.array([10, 500, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,245,253,281,249,290,280,244,257],
[264,0,224,193,212,298,255,251,250,245],
[255,276,0,262,229,244,321,318,269,227],
[247,307,238,0,293,256,348,294,278,230],
[219,288,271,207,0,227,290,288,249,207],
[251,202,256,244,273,0,276,285,246,241],
[210,245,179,152,210,224,0,191,223,227],
[220,249,182,206,212,215,309,0,261,230],
[256,250,231,222,251,254,277,239,0,248],
[243,255,273,270,293,259,273,270,252,0]])



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
result = np.append(np.array([10, 500, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,249,240,256,252,275,241,253,249],
[234,0,224,228,230,211,250,225,212,250],
[251,276,0,235,255,241,255,248,238,247],
[260,272,265,0,253,257,285,249,257,273],
[244,270,245,247,0,224,241,219,231,248],
[248,289,259,243,276,0,267,256,251,255],
[225,250,245,215,259,233,0,221,233,255],
[259,275,252,251,281,244,279,0,253,268],
[247,288,262,243,269,249,267,247,0,263],
[251,250,253,227,252,245,245,232,237,0]])



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
result = np.append(np.array([10, 500, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,287,264,261,273,238,247,259,264,265],
[213,0,232,224,227,232,234,232,238,227],
[236,268,0,241,241,227,246,231,263,248],
[239,276,259,0,245,239,253,249,248,250],
[227,273,259,255,0,242,260,256,245,240],
[262,268,273,261,258,0,251,238,280,251],
[253,266,254,247,240,249,0,259,270,252],
[241,268,269,251,244,262,241,0,259,240],
[236,262,237,252,255,220,230,241,0,236],
[235,273,252,250,260,249,248,260,264,0]])



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
result = np.append(np.array([10, 500, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,241,268,266,254,256,278,227,239],
[242,0,242,247,274,237,235,267,250,233],
[259,258,0,258,263,246,230,265,244,232],
[232,253,242,0,252,233,201,265,241,228],
[234,226,237,248,0,230,220,263,226,226],
[246,263,254,267,270,0,249,274,256,249],
[244,265,270,299,280,251,0,270,252,252],
[222,233,235,235,237,226,230,0,218,218],
[273,250,256,259,274,244,248,282,0,235],
[261,267,268,272,274,251,248,282,265,0]])



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
result = np.append(np.array([10, 500, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,256,264,242,261,264,251,234,240],
[256,0,241,267,220,257,251,268,236,225],
[244,259,0,251,218,256,276,270,232,252],
[236,233,249,0,231,262,264,242,232,235],
[258,280,282,269,0,287,276,265,250,267],
[239,243,244,238,213,0,240,232,220,222],
[236,249,224,236,224,260,0,229,234,226],
[249,232,230,258,235,268,271,0,230,228],
[266,264,268,268,250,280,266,270,0,248],
[260,275,248,265,233,278,274,272,252,0]])



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
result = np.append(np.array([10, 500, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,313,172,259,319,290,105,235,196,365],
[187,0,215,319,205,248,93,290,299,266],
[328,285,0,198,231,386,291,290,377,404],
[241,181,302,0,202,248,148,365,353,320],
[181,295,269,298,0,218,148,332,344,404],
[210,252,114,252,282,0,144,228,222,310],
[395,407,209,352,352,356,0,323,344,344],
[265,210,210,135,168,272,177,0,377,404],
[304,201,123,147,156,278,156,123,0,320],
[135,234,96,180,96,190,156,96,180,0]])



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
result = np.append(np.array([10, 500, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,265,251,230,245,253,277,270,230],
[237,0,243,266,230,241,245,232,251,245],
[235,257,0,259,229,247,253,214,242,229],
[249,234,241,0,192,220,248,231,254,271],
[270,270,271,308,0,253,261,244,273,257],
[255,259,253,280,247,0,251,246,262,257],
[247,255,247,252,239,249,0,222,238,254],
[223,268,286,269,256,254,278,0,272,234],
[230,249,258,246,227,238,262,228,0,225],
[270,255,271,229,243,243,246,266,275,0]])



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
result = np.append(np.array([10, 500, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,244,228,219,256,238,236,241,242],
[254,0,246,225,251,258,240,260,271,229],
[256,254,0,244,255,265,255,271,255,249],
[272,275,256,0,255,269,261,270,260,250],
[281,249,245,245,0,260,266,250,254,249],
[244,242,235,231,240,0,231,245,247,228],
[262,260,245,239,234,269,0,254,258,238],
[264,240,229,230,250,255,246,0,269,236],
[259,229,245,240,246,253,242,231,0,224],
[258,271,251,250,251,272,262,264,276,0]])



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
result = np.append(np.array([10, 500, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,232,266,262,245,305,250,304,218],
[267,0,294,335,267,249,318,243,295,265],
[268,206,0,304,301,253,302,196,299,213],
[234,165,196,0,195,219,294,209,248,205],
[238,233,199,305,0,213,231,195,267,264],
[255,251,247,281,287,0,334,255,336,277],
[195,182,198,206,269,166,0,196,244,231],
[250,257,304,291,305,245,304,0,300,283],
[196,205,201,252,233,164,256,200,0,205],
[282,235,287,295,236,223,269,217,295,0]])



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
result = np.append(np.array([10, 500, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,216,233,208,254,254,206,199,266],
[259,0,258,218,246,248,280,246,256,263],
[284,242,0,232,230,322,263,225,232,241],
[267,282,268,0,224,276,271,223,274,263],
[292,254,270,276,0,298,272,269,242,300],
[246,252,178,224,202,0,258,198,229,220],
[246,220,237,229,228,242,0,216,206,214],
[294,254,275,277,231,302,284,0,249,249],
[301,244,268,226,258,271,294,251,0,238],
[234,237,259,237,200,280,286,251,262,0]])



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
result = np.append(np.array([10, 500, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,272,245,225,221,207,288,248,250],
[281,0,287,251,266,270,264,318,249,246],
[228,213,0,260,228,229,235,268,220,197],
[255,249,240,0,233,226,252,299,252,239],
[275,234,272,267,0,244,215,249,270,257],
[279,230,271,274,256,0,235,302,284,246],
[293,236,265,248,285,265,0,323,287,234],
[212,182,232,201,251,198,177,0,232,189],
[252,251,280,248,230,216,213,268,0,216],
[250,254,303,261,243,254,266,311,284,0]])



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
result = np.append(np.array([10, 500, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,256,272,242,278,258,266,240,261],
[252,0,242,247,245,254,258,274,225,255],
[244,258,0,249,235,270,265,240,256,285],
[228,253,251,0,247,207,241,252,262,246],
[258,255,265,253,0,250,277,263,261,260],
[222,246,230,293,250,0,264,264,263,277],
[242,242,235,259,223,236,0,241,234,257],
[234,226,260,248,237,236,259,0,231,261],
[260,275,244,238,239,237,266,269,0,260],
[239,245,215,254,240,223,243,239,240,0]])



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
result = np.append(np.array([10, 500, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,198,227,266,271,290,253,220,238],
[256,0,213,230,211,196,205,255,174,320],
[302,287,0,282,253,385,341,245,250,288],
[273,270,218,0,222,300,289,288,181,234],
[234,289,247,278,0,260,241,193,182,291],
[229,304,115,200,240,0,231,253,142,243],
[210,295,159,211,259,269,0,258,168,232],
[247,245,255,212,307,247,242,0,201,282],
[280,326,250,319,318,358,332,299,0,310],
[262,180,212,266,209,257,268,218,190,0]])



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
result = np.append(np.array([10, 500, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,216,230,275,245,181,208,190,259],
[264,0,258,244,270,270,224,249,232,212],
[284,242,0,221,287,277,238,278,257,258],
[270,256,279,0,292,271,264,255,217,260],
[225,230,213,208,0,227,212,233,172,221],
[255,230,223,229,273,0,217,229,195,252],
[319,276,262,236,288,283,0,294,205,273],
[292,251,222,245,267,271,206,0,227,260],
[310,268,243,283,328,305,295,273,0,263],
[241,288,242,240,279,248,227,240,237,0]])



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
result = np.append(np.array([10, 500, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,266,258,271,245,271,251,253,242],
[266,0,260,249,249,231,282,268,258,250],
[234,240,0,280,265,245,243,236,243,225],
[242,251,220,0,271,242,265,241,250,238],
[229,251,235,229,0,231,270,232,211,235],
[255,269,255,258,269,0,268,261,235,264],
[229,218,257,235,230,232,0,242,217,244],
[249,232,264,259,268,239,258,0,242,248],
[247,242,257,250,289,265,283,258,0,236],
[258,250,275,262,265,236,256,252,264,0]])



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
result = np.append(np.array([10, 500, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,289,289,267,256,285,249,267,286],
[236,0,285,256,246,246,251,267,278,274],
[211,215,0,244,238,203,247,230,249,247],
[211,244,256,0,228,234,250,233,257,258],
[233,254,262,272,0,252,264,243,244,279],
[244,254,297,266,248,0,258,246,250,280],
[215,249,253,250,236,242,0,250,253,254],
[251,233,270,267,257,254,250,0,263,254],
[233,222,251,243,256,250,247,237,0,255],
[214,226,253,242,221,220,246,246,245,0]])



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
result = np.append(np.array([10, 500, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,213,239,223,215,201,237,238,262],
[250,0,286,281,286,262,280,273,244,271],
[287,214,0,280,273,252,267,290,293,285],
[261,219,220,0,210,218,213,279,227,224],
[277,214,227,290,0,245,234,264,298,195],
[285,238,248,282,255,0,213,294,252,273],
[299,220,233,287,266,287,0,294,216,303],
[263,227,210,221,236,206,206,0,248,281],
[262,256,207,273,202,248,284,252,0,278],
[238,229,215,276,305,227,197,219,222,0]])



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
result = np.append(np.array([10, 500, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,247,275,273,244,283,296,288,275],
[261,0,250,264,274,247,263,268,258,266],
[253,250,0,278,266,261,288,290,282,268],
[225,236,222,0,271,242,256,262,248,266],
[227,226,234,229,0,254,252,264,243,269],
[256,253,239,258,246,0,267,265,262,270],
[217,237,212,244,248,233,0,261,270,262],
[204,232,210,238,236,235,239,0,258,245],
[212,242,218,252,257,238,230,242,0,258],
[225,234,232,234,231,230,238,255,242,0]])



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
result = np.append(np.array([10, 500, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,170,241,188,227,281,180,166,236],
[276,0,232,260,244,237,270,238,225,348],
[330,268,0,287,253,261,287,226,227,258],
[259,240,213,0,230,189,263,186,204,272],
[312,256,247,270,0,217,291,236,251,311],
[273,263,239,311,283,0,231,216,232,294],
[219,230,213,237,209,269,0,261,220,229],
[320,262,274,314,264,284,239,0,255,266],
[334,275,273,296,249,268,280,245,0,314],
[264,152,242,228,189,206,271,234,186,0]])



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
result = np.append(np.array([10, 500, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,260,242,236,240,249,254,256,258],
[275,0,291,266,256,254,260,275,248,252],
[240,209,0,225,216,236,246,250,251,241],
[258,234,275,0,252,231,269,253,256,252],
[264,244,284,248,0,244,254,285,257,260],
[260,246,264,269,256,0,281,272,265,272],
[251,240,254,231,246,219,0,257,265,250],
[246,225,250,247,215,228,243,0,251,243],
[244,252,249,244,243,235,235,249,0,259],
[242,248,259,248,240,228,250,257,241,0]])



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
result = np.append(np.array([10, 500, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,310,288,287,238,253,254,283,308,220],
[190,0,258,189,173,222,245,252,260,126],
[212,242,0,224,176,211,227,213,284,170],
[213,311,276,0,224,232,236,270,218,242],
[262,327,324,276,0,280,314,281,301,239],
[247,278,289,268,220,0,238,239,312,261],
[246,255,273,264,186,262,0,255,249,180],
[217,248,287,230,219,261,245,0,224,205],
[192,240,216,282,199,188,251,276,0,172],
[280,374,330,258,261,239,320,295,328,0]])



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
result = np.append(np.array([10, 500, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,234,313,227,293,288,278,291,261],
[226,0,277,296,266,223,264,269,240,276],
[266,223,0,272,250,239,229,206,261,233],
[187,204,228,0,203,205,227,180,222,192],
[273,234,250,297,0,323,261,265,278,271],
[207,277,261,295,177,0,255,265,267,269],
[212,236,271,273,239,245,0,238,255,273],
[222,231,294,320,235,235,262,0,259,286],
[209,260,239,278,222,233,245,241,0,231],
[239,224,267,308,229,231,227,214,269,0]])



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
result = np.append(np.array([10, 500, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,262,280,254,254,234,253,219,251],
[264,0,266,275,272,247,245,254,271,276],
[238,234,0,261,261,255,226,262,242,279],
[220,225,239,0,247,237,222,253,222,241],
[246,228,239,253,0,249,214,261,253,258],
[246,253,245,263,251,0,231,245,227,264],
[266,255,274,278,286,269,0,270,250,272],
[247,246,238,247,239,255,230,0,235,258],
[281,229,258,278,247,273,250,265,0,278],
[249,224,221,259,242,236,228,242,222,0]])



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
result = np.append(np.array([10, 500, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,246,261,233,234,236,241,249,257],
[250,0,242,234,220,240,225,244,238,249],
[254,258,0,255,234,257,242,253,239,255],
[239,266,245,0,241,238,254,264,247,255],
[267,280,266,259,0,248,255,287,253,263],
[266,260,243,262,252,0,262,274,260,257],
[264,275,258,246,245,238,0,270,258,274],
[259,256,247,236,213,226,230,0,237,245],
[251,262,261,253,247,240,242,263,0,256],
[243,251,245,245,237,243,226,255,244,0]])



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
result = np.append(np.array([10, 500, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,246,253,276,262,253,256,251,261],
[238,0,229,236,248,268,236,240,241,235],
[254,271,0,249,278,276,270,259,263,261],
[247,264,251,0,277,274,261,258,259,250],
[224,252,222,223,0,246,233,243,241,229],
[238,232,224,226,254,0,241,225,229,223],
[247,264,230,239,267,259,0,259,247,249],
[244,260,241,242,257,275,241,0,250,246],
[249,259,237,241,259,271,253,250,0,248],
[239,265,239,250,271,277,251,254,252,0]])



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
result = np.append(np.array([10, 500, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,267,264,244,286,266,283,276,271],
[229,0,281,262,250,253,257,261,282,242],
[233,219,0,215,233,260,243,241,260,244],
[236,238,285,0,251,256,244,269,252,274],
[256,250,267,249,0,257,245,247,238,225],
[214,247,240,244,243,0,240,230,265,235],
[234,243,257,256,255,260,0,228,245,263],
[217,239,259,231,253,270,272,0,246,299],
[224,218,240,248,262,235,255,254,0,246],
[229,258,256,226,275,265,237,201,254,0]])



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
result = np.append(np.array([10, 500, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,248,230,242,244,240,257,240,270],
[267,0,259,257,245,241,258,265,252,274],
[252,241,0,251,252,252,267,249,253,287],
[270,243,249,0,255,249,266,243,263,286],
[258,255,248,245,0,245,260,254,242,267],
[256,259,248,251,255,0,259,259,246,289],
[260,242,233,234,240,241,0,259,236,268],
[243,235,251,257,246,241,241,0,251,275],
[260,248,247,237,258,254,264,249,0,265],
[230,226,213,214,233,211,232,225,235,0]])



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
result = np.append(np.array([10, 500, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,262,271,245,266,248,255,280,281],
[231,0,242,264,218,241,242,232,263,257],
[238,258,0,261,252,248,243,240,266,256],
[229,236,239,0,234,234,232,236,280,262],
[255,282,248,266,0,279,262,270,271,274],
[234,259,252,266,221,0,235,231,260,242],
[252,258,257,268,238,265,0,262,291,265],
[245,268,260,264,230,269,238,0,299,263],
[220,237,234,220,229,240,209,201,0,243],
[219,243,244,238,226,258,235,237,257,0]])



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
result = np.append(np.array([10, 500, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,322,271,301,346,391,321,232,307,309],
[178,0,198,298,236,236,238,272,221,344],
[229,302,0,252,289,248,292,285,244,299],
[199,202,248,0,277,302,242,185,225,223],
[154,264,211,223,0,291,225,193,251,216],
[109,264,252,198,209,0,264,183,138,220],
[179,262,208,258,275,236,0,227,217,302],
[268,228,215,315,307,317,273,0,200,254],
[193,279,256,275,249,362,283,300,0,285],
[191,156,201,277,284,280,198,246,215,0]])



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
result = np.append(np.array([10, 500, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,324,258,249,288,291,277,292,286],
[230,0,261,261,241,247,262,248,270,249],
[176,239,0,211,222,204,218,230,251,247],
[242,239,289,0,245,267,242,278,263,269],
[251,259,278,255,0,261,263,238,299,261],
[212,253,296,233,239,0,242,271,293,251],
[209,238,282,258,237,258,0,244,271,237],
[223,252,270,222,262,229,256,0,270,239],
[208,230,249,237,201,207,229,230,0,210],
[214,251,253,231,239,249,263,261,290,0]])



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
result = np.append(np.array([10, 500, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,238,234,219,243,236,252,267,239],
[249,0,253,259,219,250,258,262,249,248],
[262,247,0,262,244,235,236,281,259,234],
[266,241,238,0,227,243,227,258,246,233],
[281,281,256,273,0,278,247,273,279,278],
[257,250,265,257,222,0,234,261,251,259],
[264,242,264,273,253,266,0,276,270,256],
[248,238,219,242,227,239,224,0,248,237],
[233,251,241,254,221,249,230,252,0,230],
[261,252,266,267,222,241,244,263,270,0]])



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
result = np.append(np.array([10, 500, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,236,230,244,212,233,242,247,261],
[254,0,263,252,251,252,241,269,269,285],
[264,237,0,223,260,230,232,241,260,278],
[270,248,277,0,248,245,254,272,247,275],
[256,249,240,252,0,225,207,227,270,286],
[288,248,270,255,275,0,258,251,255,273],
[267,259,268,246,293,242,0,255,292,304],
[258,231,259,228,273,249,245,0,243,251],
[253,231,240,253,230,245,208,257,0,248],
[239,215,222,225,214,227,196,249,252,0]])



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
result = np.append(np.array([10, 500, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,208,229,237,220,223,225,206,226,239],
[292,0,264,268,234,295,261,250,288,248],
[271,236,0,262,239,264,261,243,240,249],
[263,232,238,0,217,277,251,244,239,253],
[280,266,261,283,0,261,282,235,295,232],
[277,205,236,223,239,0,245,199,221,220],
[275,239,239,249,218,255,0,205,256,243],
[294,250,257,256,265,301,295,0,284,259],
[274,212,260,261,205,279,244,216,0,229],
[261,252,251,247,268,280,257,241,271,0]])



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
result = np.append(np.array([10, 500, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,229,244,226,226,243,249,231,238],
[251,0,233,249,236,246,240,236,251,251],
[271,267,0,270,258,267,262,250,247,262],
[256,251,230,0,234,251,255,248,224,251],
[274,264,242,266,0,247,256,258,239,258],
[274,254,233,249,253,0,273,252,243,261],
[257,260,238,245,244,227,0,230,237,259],
[251,264,250,252,242,248,270,0,236,250],
[269,249,253,276,261,257,263,264,0,279],
[262,249,238,249,242,239,241,250,221,0]])



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
result = np.append(np.array([10, 500, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,299,292,268,273,249,312,253,256,287],
[201,0,269,224,251,273,268,236,196,239],
[208,231,0,249,220,263,278,261,238,268],
[232,276,251,0,248,237,310,261,240,274],
[227,249,280,252,0,244,263,264,244,250],
[251,227,237,263,256,0,305,270,238,255],
[188,232,222,190,237,195,0,205,215,253],
[247,264,239,239,236,230,295,0,224,287],
[244,304,262,260,256,262,285,276,0,280],
[213,261,232,226,250,245,247,213,220,0]])



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
result = np.append(np.array([10, 500, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,243,255,252,234,245,242,253,242],
[269,0,240,261,256,258,252,251,253,254],
[257,260,0,239,270,266,257,245,242,271],
[245,239,261,0,241,255,267,258,245,262],
[248,244,230,259,0,257,240,246,270,247],
[266,242,234,245,243,0,240,237,255,264],
[255,248,243,233,260,260,0,244,273,257],
[258,249,255,242,254,263,256,0,260,252],
[247,247,258,255,230,245,227,240,0,252],
[258,246,229,238,253,236,243,248,248,0]])



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
result = np.append(np.array([10, 500, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,258,257,227,260,257,249,238,232],
[243,0,244,216,243,247,256,250,230,230],
[242,256,0,232,241,235,242,254,248,236],
[243,284,268,0,255,269,265,272,246,227],
[273,257,259,245,0,258,254,259,251,251],
[240,253,265,231,242,0,239,228,247,218],
[243,244,258,235,246,261,0,255,263,233],
[251,250,246,228,241,272,245,0,247,235],
[262,270,252,254,249,253,237,253,0,219],
[268,270,264,273,249,282,267,265,281,0]])



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
result = np.append(np.array([10, 500, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,224,276,225,252,222,248,251,277],
[254,0,227,238,242,248,237,251,270,248],
[276,273,0,292,277,244,257,258,278,278],
[224,262,208,0,241,241,245,234,260,242],
[275,258,223,259,0,237,240,260,257,239],
[248,252,256,259,263,0,224,251,275,253],
[278,263,243,255,260,276,0,267,275,271],
[252,249,242,266,240,249,233,0,282,254],
[249,230,222,240,243,225,225,218,0,248],
[223,252,222,258,261,247,229,246,252,0]])



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
result = np.append(np.array([10, 500, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,210,238,241,261,239,228,232,247],
[261,0,273,297,252,278,250,272,247,271],
[290,227,0,274,264,269,259,259,234,239],
[262,203,226,0,236,254,220,254,256,231],
[259,248,236,264,0,262,239,259,261,258],
[239,222,231,246,238,0,218,255,224,238],
[261,250,241,280,261,282,0,236,266,265],
[272,228,241,246,241,245,264,0,237,219],
[268,253,266,244,239,276,234,263,0,272],
[253,229,261,269,242,262,235,281,228,0]])



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
result = np.append(np.array([10, 500, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,249,254,249,262,246,265,278,252],
[224,0,224,239,241,262,248,241,250,241],
[251,276,0,247,259,264,262,255,270,252],
[246,261,253,0,244,263,269,244,261,265],
[251,259,241,256,0,264,252,260,255,278],
[238,238,236,237,236,0,246,241,244,241],
[254,252,238,231,248,254,0,242,246,259],
[235,259,245,256,240,259,258,0,260,242],
[222,250,230,239,245,256,254,240,0,233],
[248,259,248,235,222,259,241,258,267,0]])



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
result = np.append(np.array([10, 500, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,245,263,241,228,237,245,238,239],
[257,0,261,255,239,257,229,245,232,248],
[255,239,0,272,250,255,253,238,255,261],
[237,245,228,0,250,244,224,253,244,246],
[259,261,250,250,0,250,268,242,255,255],
[272,243,245,256,250,0,226,210,236,260],
[263,271,247,276,232,274,0,258,260,262],
[255,255,262,247,258,290,242,0,247,263],
[262,268,245,256,245,264,240,253,0,265],
[261,252,239,254,245,240,238,237,235,0]])



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
result = np.append(np.array([10, 500, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,236,250,261,246,262,250,251,254],
[254,0,226,214,225,244,253,240,238,253],
[264,274,0,271,247,244,263,295,271,277],
[250,286,229,0,241,259,247,272,244,234],
[239,275,253,259,0,227,242,268,257,247],
[254,256,256,241,273,0,274,259,274,254],
[238,247,237,253,258,226,0,267,250,244],
[250,260,205,228,232,241,233,0,244,263],
[249,262,229,256,243,226,250,256,0,254],
[246,247,223,266,253,246,256,237,246,0]])



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
result = np.append(np.array([10, 500, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,254,203,267,213,265,250,256,262],
[264,0,281,252,270,251,272,241,253,292],
[246,219,0,218,257,243,287,248,216,258],
[297,248,282,0,281,276,300,282,264,272],
[233,230,243,219,0,247,238,226,256,261],
[287,249,257,224,253,0,264,263,242,242],
[235,228,213,200,262,236,0,250,246,263],
[250,259,252,218,274,237,250,0,260,253],
[244,247,284,236,244,258,254,240,0,276],
[238,208,242,228,239,258,237,247,224,0]])



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
result = np.append(np.array([10, 500, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,271,254,235,271,253,247,258,241],
[252,0,245,250,256,263,258,278,270,233],
[229,255,0,226,223,245,244,247,239,237],
[246,250,274,0,229,264,247,246,249,237],
[265,244,277,271,0,277,251,268,238,259],
[229,237,255,236,223,0,230,249,226,228],
[247,242,256,253,249,270,0,270,267,247],
[253,222,253,254,232,251,230,0,253,242],
[242,230,261,251,262,274,233,247,0,250],
[259,267,263,263,241,272,253,258,250,0]])



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
result = np.append(np.array([10, 500, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,219,264,245,248,248,230,243,251],
[270,0,251,258,253,249,253,241,264,249],
[281,249,0,281,256,265,254,256,266,249],
[236,242,219,0,233,239,239,235,245,227],
[255,247,244,267,0,240,257,246,267,252],
[252,251,235,261,260,0,260,224,249,249],
[252,247,246,261,243,240,0,238,253,269],
[270,259,244,265,254,276,262,0,253,257],
[257,236,234,255,233,251,247,247,0,240],
[249,251,251,273,248,251,231,243,260,0]])



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
result = np.append(np.array([10, 500, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,252,272,272,244,272,228,250,259],
[274,0,260,275,275,250,268,256,268,286],
[248,240,0,253,277,254,248,251,242,263],
[228,225,247,0,238,251,260,224,252,249],
[228,225,223,262,0,232,246,239,245,260],
[256,250,246,249,268,0,269,245,253,264],
[228,232,252,240,254,231,0,240,253,264],
[272,244,249,276,261,255,260,0,260,252],
[250,232,258,248,255,247,247,240,0,266],
[241,214,237,251,240,236,236,248,234,0]])



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
result = np.append(np.array([10, 500, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,256,213,231,263,225,236,237,217],
[280,0,270,245,269,237,267,306,242,250],
[244,230,0,255,262,235,262,280,225,196],
[287,255,245,0,286,244,269,274,235,220],
[269,231,238,214,0,229,266,251,202,222],
[237,263,265,256,271,0,233,276,260,254],
[275,233,238,231,234,267,0,264,272,218],
[264,194,220,226,249,224,236,0,227,218],
[263,258,275,265,298,240,228,273,0,253],
[283,250,304,280,278,246,282,282,247,0]])



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
result = np.append(np.array([10, 500, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,235,213,188,197,176,224,231,219],
[276,0,287,294,247,257,225,272,293,238],
[265,213,0,197,222,226,201,270,243,265],
[287,206,303,0,257,238,202,240,282,267],
[312,253,278,243,0,226,232,267,263,238],
[303,243,274,262,274,0,253,270,299,298],
[324,275,299,298,268,247,0,271,302,251],
[276,228,230,260,233,230,229,0,296,204],
[269,207,257,218,237,201,198,204,0,207],
[281,262,235,233,262,202,249,296,293,0]])



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
result = np.append(np.array([10, 500, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,209,214,255,212,194,206,231,240],
[274,0,282,252,297,260,221,247,254,275],
[291,218,0,265,275,269,271,252,245,267],
[286,248,235,0,285,270,243,237,245,284],
[245,203,225,215,0,215,180,228,211,228],
[288,240,231,230,285,0,221,245,240,270],
[306,279,229,257,320,279,0,268,280,277],
[294,253,248,263,272,255,232,0,258,258],
[269,246,255,255,289,260,220,242,0,281],
[260,225,233,216,272,230,223,242,219,0]])



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
result = np.append(np.array([10, 500, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,249,252,224,253,238,256,253,232],
[259,0,253,259,248,268,244,246,247,269],
[251,247,0,275,256,270,276,263,236,241],
[248,241,225,0,228,254,246,256,228,233],
[276,252,244,272,0,277,266,259,254,233],
[247,232,230,246,223,0,242,232,225,232],
[262,256,224,254,234,258,0,249,232,254],
[244,254,237,244,241,268,251,0,262,263],
[247,253,264,272,246,275,268,238,0,251],
[268,231,259,267,267,268,246,237,249,0]])



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
result = np.append(np.array([10, 500, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,239,246,228,289,244,196,219,292],
[216,0,220,238,198,258,230,186,189,253],
[261,280,0,214,267,273,297,238,253,330],
[254,262,286,0,262,326,250,242,272,326],
[272,302,233,238,0,293,219,270,220,252],
[211,242,227,174,207,0,208,194,172,235],
[256,270,203,250,281,292,0,222,244,276],
[304,314,262,258,230,306,278,0,258,286],
[281,311,247,228,280,328,256,242,0,287],
[208,247,170,174,248,265,224,214,213,0]])



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
result = np.append(np.array([10, 500, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,281,227,218,269,244,243,225,231,250],
[219,0,255,233,245,222,243,250,234,246],
[273,245,0,243,264,261,257,270,257,259],
[282,267,257,0,245,252,248,251,244,276],
[231,255,236,255,0,226,248,251,221,233],
[256,278,239,248,274,0,266,268,246,252],
[257,257,243,252,252,234,0,239,231,252],
[275,250,230,249,249,232,261,0,226,274],
[269,266,243,256,279,254,269,274,0,254],
[250,254,241,224,267,248,248,226,246,0]])



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
result = np.append(np.array([10, 500, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,229,248,255,271,243,239,229,249],
[252,0,264,272,280,271,242,277,211,240],
[271,236,0,256,249,277,251,260,241,236],
[252,228,244,0,265,271,257,263,234,222],
[245,220,251,235,0,240,257,244,245,240],
[229,229,223,229,260,0,243,260,238,220],
[257,258,249,243,243,257,0,261,257,250],
[261,223,240,237,256,240,239,0,246,250],
[271,289,259,266,255,262,243,254,0,263],
[251,260,264,278,260,280,250,250,237,0]])



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
result = np.append(np.array([10, 500, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,263,264,260,247,249,255,246,245],
[251,0,255,257,249,245,266,269,254,274],
[237,245,0,243,232,234,248,234,255,229],
[236,243,257,0,227,240,240,240,245,235],
[240,251,268,273,0,238,257,261,234,234],
[253,255,266,260,262,0,258,261,235,245],
[251,234,252,260,243,242,0,264,230,227],
[245,231,266,260,239,239,236,0,243,232],
[254,246,245,255,266,265,270,257,0,251],
[255,226,271,265,266,255,273,268,249,0]])



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
result = np.append(np.array([10, 500, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,159,226,150,219,262,177,227,160],
[263,0,151,150,187,104,234,166,212,163],
[341,349,0,235,239,233,250,269,285,272],
[274,350,265,0,245,298,192,263,275,255],
[350,313,261,255,0,191,308,248,233,230],
[281,396,267,202,309,0,276,326,284,228],
[238,266,250,308,192,224,0,204,200,248],
[323,334,231,237,252,174,296,0,240,279],
[273,288,215,225,267,216,300,260,0,156],
[340,337,228,245,270,272,252,221,344,0]])



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
result = np.append(np.array([10, 500, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,234,250,247,261,255,254,249,280],
[233,0,257,239,247,269,211,254,231,262],
[266,243,0,256,272,266,247,255,255,273],
[250,261,244,0,258,229,240,245,269,288],
[253,253,228,242,0,251,243,245,236,267],
[239,231,234,271,249,0,237,249,226,274],
[245,289,253,260,257,263,0,243,261,283],
[246,246,245,255,255,251,257,0,258,259],
[251,269,245,231,264,274,239,242,0,290],
[220,238,227,212,233,226,217,241,210,0]])



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
result = np.append(np.array([10, 500, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,246,256,255,271,255,247,257,257],
[246,0,234,243,249,263,261,232,242,251],
[254,266,0,257,248,281,255,254,248,272],
[244,257,243,0,250,252,244,250,254,260],
[245,251,252,250,0,268,266,235,239,241],
[229,237,219,248,232,0,239,228,230,239],
[245,239,245,256,234,261,0,250,243,252],
[253,268,246,250,265,272,250,0,240,254],
[243,258,252,246,261,270,257,260,0,261],
[243,249,228,240,259,261,248,246,239,0]])



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
result = np.append(np.array([10, 500, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,205,223,242,253,253,206,236,239,237],
[295,0,253,264,271,295,247,292,257,283],
[277,247,0,282,287,294,260,274,273,281],
[258,236,218,0,251,267,193,252,275,261],
[247,229,213,249,0,266,231,247,266,266],
[247,205,206,233,234,0,181,215,251,217],
[294,253,240,307,269,319,0,289,324,284],
[264,208,226,248,253,285,211,0,274,247],
[261,243,227,225,234,249,176,226,0,251],
[263,217,219,239,234,283,216,253,249,0]])



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
result = np.append(np.array([10, 500, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,313,273,232,236,241,264,241,294],
[246,0,230,267,254,200,256,223,242,252],
[187,270,0,275,236,248,204,212,253,283],
[227,233,225,0,193,186,206,190,235,247],
[268,246,264,307,0,246,243,230,269,253],
[264,300,252,314,254,0,272,282,233,290],
[259,244,296,294,257,228,0,252,270,292],
[236,277,288,310,270,218,248,0,249,298],
[259,258,247,265,231,267,230,251,0,274],
[206,248,217,253,247,210,208,202,226,0]])



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
result = np.append(np.array([10, 500, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,281,264,246,200,270,251,257,259,277],
[219,0,250,217,254,259,246,234,242,264],
[236,250,0,230,224,266,253,247,244,272],
[254,283,270,0,275,254,269,248,279,293],
[300,246,276,225,0,252,232,255,243,287],
[230,241,234,246,248,0,232,238,232,271],
[249,254,247,231,268,268,0,255,241,244],
[243,266,253,252,245,262,245,0,288,283],
[241,258,256,221,257,268,259,212,0,278],
[223,236,228,207,213,229,256,217,222,0]])



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
result = np.append(np.array([10, 500, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,304,255,270,221,254,275,272,228,262],
[196,0,218,219,192,222,239,227,199,205],
[245,282,0,228,257,242,279,266,241,256],
[230,281,272,0,229,248,262,246,241,258],
[279,308,243,271,0,264,279,272,251,238],
[246,278,258,252,236,0,252,277,251,252],
[225,261,221,238,221,248,0,235,222,244],
[228,273,234,254,228,223,265,0,232,252],
[272,301,259,259,249,249,278,268,0,250],
[238,295,244,242,262,248,256,248,250,0]])



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
result = np.append(np.array([10, 500, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,272,248,256,210,205,216,264,232],
[252,0,290,301,281,209,250,251,272,331],
[228,210,0,311,258,192,213,243,227,283],
[252,199,189,0,217,182,183,215,180,267],
[244,219,242,283,0,223,246,197,213,287],
[290,291,308,318,277,0,192,285,231,306],
[295,250,287,317,254,308,0,299,270,286],
[284,249,257,285,303,215,201,0,313,290],
[236,228,273,320,287,269,230,187,0,231],
[268,169,217,233,213,194,214,210,269,0]])



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
result = np.append(np.array([10, 500, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,311,262,296,283,218,279,256,264],
[234,0,295,253,279,312,240,249,255,258],
[189,205,0,214,217,236,223,238,221,213],
[238,247,286,0,299,319,269,257,243,247],
[204,221,283,201,0,220,192,249,236,283],
[217,188,264,181,280,0,210,228,188,196],
[282,260,277,231,308,290,0,247,232,268],
[221,251,262,243,251,272,253,0,225,238],
[244,245,279,257,264,312,268,275,0,264],
[236,242,287,253,217,304,232,262,236,0]])



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
result = np.append(np.array([10, 500, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,306,253,234,235,235,242,244,243,260],
[194,0,234,215,201,205,200,211,218,183],
[247,266,0,260,243,236,236,274,264,210],
[266,285,240,0,247,228,241,253,247,213],
[265,299,257,253,0,257,260,282,271,237],
[265,295,264,272,243,0,243,262,239,220],
[258,300,264,259,240,257,0,267,261,196],
[256,289,226,247,218,238,233,0,210,225],
[257,282,236,253,229,261,239,290,0,225],
[240,317,290,287,263,280,304,275,275,0]])



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
result = np.append(np.array([10, 500, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,296,258,274,274,273,244,271,271,255],
[204,0,212,219,236,243,232,245,211,236],
[242,288,0,268,278,264,251,270,270,261],
[226,281,232,0,249,232,239,251,241,234],
[226,264,222,251,0,248,235,247,243,252],
[227,257,236,268,252,0,212,271,234,246],
[256,268,249,261,265,288,0,253,246,248],
[229,255,230,249,253,229,247,0,248,246],
[229,289,230,259,257,266,254,252,0,247],
[245,264,239,266,248,254,252,254,253,0]])



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
result = np.append(np.array([10, 500, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,243,248,246,244,239,257,254,275],
[246,0,247,226,261,233,231,257,235,244],
[257,253,0,244,242,237,244,267,228,260],
[252,274,256,0,257,242,244,253,259,253],
[254,239,258,243,0,235,244,262,235,261],
[256,267,263,258,265,0,260,269,243,269],
[261,269,256,256,256,240,0,272,261,261],
[243,243,233,247,238,231,228,0,229,242],
[246,265,272,241,265,257,239,271,0,277],
[225,256,240,247,239,231,239,258,223,0]])



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
result = np.append(np.array([10, 500, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,251,254,262,255,234,262,249,256],
[237,0,226,239,245,221,214,244,223,229],
[249,274,0,263,245,247,221,264,251,273],
[246,261,237,0,237,232,219,247,223,227],
[238,255,255,263,0,245,233,261,244,246],
[245,279,253,268,255,0,222,252,251,243],
[266,286,279,281,267,278,0,290,248,269],
[238,256,236,253,239,248,210,0,236,241],
[251,277,249,277,256,249,252,264,0,244],
[244,271,227,273,254,257,231,259,256,0]])



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
result = np.append(np.array([10, 500, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,235,247,238,237,253,237,243,258],
[257,0,239,235,217,230,252,243,248,248],
[265,261,0,251,234,245,249,245,249,253],
[253,265,249,0,236,254,250,242,250,248],
[262,283,266,264,0,246,258,259,269,271],
[263,270,255,246,254,0,253,253,250,273],
[247,248,251,250,242,247,0,250,248,262],
[263,257,255,258,241,247,250,0,250,252],
[257,252,251,250,231,250,252,250,0,257],
[242,252,247,252,229,227,238,248,243,0]])



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
result = np.append(np.array([10, 500, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,259,236,248,257,244,249,265,235],
[237,0,251,252,246,272,242,261,262,244],
[241,249,0,250,228,257,238,252,247,264],
[264,248,250,0,241,265,254,250,251,238],
[252,254,272,259,0,273,242,254,242,261],
[243,228,243,235,227,0,234,252,236,230],
[256,258,262,246,258,266,0,262,240,257],
[251,239,248,250,246,248,238,0,265,244],
[235,238,253,249,258,264,260,235,0,247],
[265,256,236,262,239,270,243,256,253,0]])



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
result = np.append(np.array([10, 500, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,255,233,258,275,295,276,248,287],
[242,0,260,246,257,261,263,274,262,278],
[245,240,0,257,279,271,261,267,251,286],
[267,254,243,0,260,280,257,289,258,274],
[242,243,221,240,0,251,242,297,245,253],
[225,239,229,220,249,0,229,255,228,245],
[205,237,239,243,258,271,0,259,228,260],
[224,226,233,211,203,245,241,0,240,228],
[252,238,249,242,255,272,272,260,0,265],
[213,222,214,226,247,255,240,272,235,0]])



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
result = np.append(np.array([10, 500, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,263,251,257,257,250,264,265,251],
[233,0,252,253,250,235,238,264,273,245],
[237,248,0,244,259,225,231,257,269,248],
[249,247,256,0,264,250,241,257,269,240],
[243,250,241,236,0,237,256,266,260,248],
[243,265,275,250,263,0,257,250,287,252],
[250,262,269,259,244,243,0,270,283,250],
[236,236,243,243,234,250,230,0,273,238],
[235,227,231,231,240,213,217,227,0,229],
[249,255,252,260,252,248,250,262,271,0]])



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
result = np.append(np.array([10, 500, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,254,263,249,263,243,234,261,241],
[273,0,254,254,281,266,258,243,267,233],
[246,246,0,246,278,270,251,264,269,250],
[237,246,254,0,250,235,230,241,263,255],
[251,219,222,250,0,254,229,242,255,258],
[237,234,230,265,246,0,237,239,267,249],
[257,242,249,270,271,263,0,255,273,247],
[266,257,236,259,258,261,245,0,259,252],
[239,233,231,237,245,233,227,241,0,235],
[259,267,250,245,242,251,253,248,265,0]])



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
result = np.append(np.array([10, 500, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,272,263,260,269,268,258,241,247],
[226,0,243,251,253,242,254,244,244,227],
[228,257,0,251,224,251,253,246,227,250],
[237,249,249,0,235,248,284,243,226,248],
[240,247,276,265,0,274,280,244,254,243],
[231,258,249,252,226,0,263,229,247,255],
[232,246,247,216,220,237,0,226,218,245],
[242,256,254,257,256,271,274,0,238,241],
[259,256,273,274,246,253,282,262,0,253],
[253,273,250,252,257,245,255,259,247,0]])



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
result = np.append(np.array([10, 500, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,244,243,231,249,251,246,240,257],
[259,0,249,266,257,266,266,256,272,275],
[256,251,0,258,254,237,267,244,258,257],
[257,234,242,0,242,243,248,249,240,253],
[269,243,246,258,0,259,261,262,274,262],
[251,234,263,257,241,0,268,242,240,236],
[249,234,233,252,239,232,0,243,246,262],
[254,244,256,251,238,258,257,0,259,259],
[260,228,242,260,226,260,254,241,0,248],
[243,225,243,247,238,264,238,241,252,0]])



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
result = np.append(np.array([10, 500, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,228,275,226,240,219,238,271,236],
[261,0,268,293,248,261,265,271,283,271],
[272,232,0,263,256,258,242,243,264,233],
[225,207,237,0,233,242,235,255,264,215],
[274,252,244,267,0,272,237,270,280,232],
[260,239,242,258,228,0,225,231,271,231],
[281,235,258,265,263,275,0,266,286,252],
[262,229,257,245,230,269,234,0,278,253],
[229,217,236,236,220,229,214,222,0,204],
[264,229,267,285,268,269,248,247,296,0]])



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
result = np.append(np.array([10, 500, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,289,293,333,283,246,302,248,309,316],
[211,0,260,220,189,223,246,198,230,247],
[207,240,0,265,206,195,282,239,257,219],
[167,280,235,0,208,191,226,181,257,223],
[217,311,294,292,0,258,274,215,293,290],
[254,277,305,309,242,0,310,258,329,270],
[198,254,218,274,226,190,0,184,207,229],
[252,302,261,319,285,242,316,0,316,284],
[191,270,243,243,207,171,293,184,0,273],
[184,253,281,277,210,230,271,216,227,0]])



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
result = np.append(np.array([10, 500, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,236,325,322,273,217,225,300,257],
[286,0,226,326,314,285,214,261,272,287],
[264,274,0,287,327,248,237,234,262,270],
[175,174,213,0,232,173,202,184,196,239],
[178,186,173,268,0,207,164,190,264,196],
[227,215,252,327,293,0,230,235,272,246],
[283,286,263,298,336,270,0,245,301,266],
[275,239,266,316,310,265,255,0,295,266],
[200,228,238,304,236,228,199,205,0,229],
[243,213,230,261,304,254,234,234,271,0]])



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
result = np.append(np.array([10, 500, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,246,222,192,235,252,231,209,222],
[252,0,251,258,240,236,253,240,245,239],
[254,249,0,257,249,268,258,254,242,245],
[278,242,243,0,231,247,295,281,240,243],
[308,260,251,269,0,226,282,277,248,270],
[265,264,232,253,274,0,265,241,228,236],
[248,247,242,205,218,235,0,249,234,244],
[269,260,246,219,223,259,251,0,236,255],
[291,255,258,260,252,272,266,264,0,244],
[278,261,255,257,230,264,256,245,256,0]])



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
result = np.append(np.array([10, 500, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,266,242,248,232,245,242,251,254],
[268,0,253,242,273,238,246,253,243,262],
[234,247,0,250,258,234,251,251,247,263],
[258,258,250,0,262,237,254,245,261,259],
[252,227,242,238,0,251,257,249,244,245],
[268,262,266,263,249,0,258,253,249,269],
[255,254,249,246,243,242,0,257,253,263],
[258,247,249,255,251,247,243,0,258,269],
[249,257,253,239,256,251,247,242,0,260],
[246,238,237,241,255,231,237,231,240,0]])



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
result = np.append(np.array([10, 500, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,249,405,279,146,177,375,424,378],
[243,0,194,416,243,224,192,293,340,294],
[251,306,0,222,355,123,74,249,405,195],
[95,84,278,0,179,76,103,179,301,148],
[221,257,145,321,0,173,93,221,375,294],
[354,276,377,424,327,0,177,305,424,298],
[323,308,426,397,407,323,0,377,358,247],
[125,207,251,321,279,195,123,0,405,294],
[76,160,95,199,125,76,142,95,0,125],
[122,206,305,352,206,202,253,206,375,0]])



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
result = np.append(np.array([10, 500, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,246,252,263,255,248,260,255,242],
[244,0,235,240,247,241,249,251,236,225],
[254,265,0,253,275,255,271,266,248,260],
[248,260,247,0,261,264,271,249,245,243],
[237,253,225,239,0,241,260,252,246,240],
[245,259,245,236,259,0,251,249,250,245],
[252,251,229,229,240,249,0,264,239,234],
[240,249,234,251,248,251,236,0,239,249],
[245,264,252,255,254,250,261,261,0,255],
[258,275,240,257,260,255,266,251,245,0]])



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
result = np.append(np.array([10, 500, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,251,246,295,254,253,204,242,231],
[232,0,165,223,221,198,194,255,201,172],
[249,335,0,297,294,273,219,289,276,237],
[254,277,203,0,290,218,214,275,286,228],
[205,279,206,210,0,201,208,209,230,231],
[246,302,227,282,299,0,217,261,241,195],
[247,306,281,286,292,283,0,292,307,253],
[296,245,211,225,291,239,208,0,217,229],
[258,299,224,214,270,259,193,283,0,204],
[269,328,263,272,269,305,247,271,296,0]])



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
result = np.append(np.array([10, 500, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,230,239,238,257,258,244,259,274],
[247,0,245,249,232,243,249,246,247,268],
[270,255,0,257,245,279,268,262,254,275],
[261,251,243,0,258,259,257,266,253,275],
[262,268,255,242,0,256,261,269,253,276],
[243,257,221,241,244,0,251,254,238,271],
[242,251,232,243,239,249,0,254,252,284],
[256,254,238,234,231,246,246,0,245,270],
[241,253,246,247,247,262,248,255,0,274],
[226,232,225,225,224,229,216,230,226,0]])



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
result = np.append(np.array([10, 500, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,243,233,207,236,230,256,236,211],
[251,0,239,233,238,235,238,228,233,220],
[257,261,0,242,244,238,241,249,246,217],
[267,267,258,0,239,242,252,246,247,268],
[293,262,256,261,0,237,261,253,281,233],
[264,265,262,258,263,0,258,248,227,242],
[270,262,259,248,239,242,0,244,233,245],
[244,272,251,254,247,252,256,0,220,244],
[264,267,254,253,219,273,267,280,0,251],
[289,280,283,232,267,258,255,256,249,0]])



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
result = np.append(np.array([10, 500, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,255,248,245,242,244,256,245,246],
[264,0,256,245,236,245,258,265,265,247],
[245,244,0,227,227,226,238,244,231,237],
[252,255,273,0,252,248,240,251,264,263],
[255,264,273,248,0,260,258,256,271,260],
[258,255,274,252,240,0,255,248,274,263],
[256,242,262,260,242,245,0,239,252,255],
[244,235,256,249,244,252,261,0,271,262],
[255,235,269,236,229,226,248,229,0,244],
[254,253,263,237,240,237,245,238,256,0]])



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
result = np.append(np.array([10, 500, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,190,239,248,189,224,251,270,227],
[242,0,212,183,214,180,209,216,261,187],
[310,288,0,280,306,259,230,258,321,263],
[261,317,220,0,265,234,231,296,357,258],
[252,286,194,235,0,246,221,236,248,220],
[311,320,241,266,254,0,269,237,320,228],
[276,291,270,269,279,231,0,236,322,253],
[249,284,242,204,264,263,264,0,292,286],
[230,239,179,143,252,180,178,208,0,176],
[273,313,237,242,280,272,247,214,324,0]])



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
result = np.append(np.array([10, 500, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,296,228,287,279,278,277,280,234],
[224,0,288,209,277,257,246,218,273,249],
[204,212,0,210,264,251,236,216,205,223],
[272,291,290,0,274,298,238,261,269,231],
[213,223,236,226,0,229,217,258,215,225],
[221,243,249,202,271,0,224,209,275,233],
[222,254,264,262,283,276,0,255,288,282],
[223,282,284,239,242,291,245,0,310,239],
[220,227,295,231,285,225,212,190,0,243],
[266,251,277,269,275,267,218,261,257,0]])



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
result = np.append(np.array([10, 500, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,235,235,245,240,236,250,231,266],
[242,0,256,240,250,241,234,257,238,244],
[265,244,0,223,241,259,227,251,237,258],
[265,260,277,0,265,250,248,253,254,261],
[255,250,259,235,0,256,268,268,247,261],
[260,259,241,250,244,0,226,246,234,239],
[264,266,273,252,232,274,0,270,239,281],
[250,243,249,247,232,254,230,0,234,253],
[269,262,263,246,253,266,261,266,0,273],
[234,256,242,239,239,261,219,247,227,0]])



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
result = np.append(np.array([10, 500, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,281,235,249,225,280,191,186,263,227],
[219,0,172,253,150,230,179,132,173,196],
[265,328,0,212,197,229,216,255,255,330],
[251,247,288,0,205,287,256,153,242,275],
[275,350,303,295,0,280,255,211,307,329],
[220,270,271,213,220,0,205,171,276,282],
[309,321,284,244,245,295,0,194,303,360],
[314,368,245,347,289,329,306,0,277,273],
[237,327,245,258,193,224,197,223,0,279],
[273,304,170,225,171,218,140,227,221,0]])



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
result = np.append(np.array([10, 500, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,247,258,246,254,240,261,252,265],
[248,0,253,237,241,274,239,271,270,267],
[253,247,0,261,237,252,222,258,263,252],
[242,263,239,0,243,250,258,244,271,244],
[254,259,263,257,0,262,237,253,251,259],
[246,226,248,250,238,0,214,235,241,252],
[260,261,278,242,263,286,0,251,258,256],
[239,229,242,256,247,265,249,0,262,256],
[248,230,237,229,249,259,242,238,0,243],
[235,233,248,256,241,248,244,244,257,0]])



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
result = np.append(np.array([10, 500, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,232,238,234,244,219,229,262,232],
[267,0,245,248,219,244,240,238,257,266],
[268,255,0,238,239,261,237,257,245,249],
[262,252,262,0,259,280,243,253,276,260],
[266,281,261,241,0,272,256,265,273,257],
[256,256,239,220,228,0,217,255,256,241],
[281,260,263,257,244,283,0,277,291,265],
[271,262,243,247,235,245,223,0,250,258],
[238,243,255,224,227,244,209,250,0,244],
[268,234,251,240,243,259,235,242,256,0]])



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
result = np.append(np.array([10, 500, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,259,242,270,268,257,259,268,274],
[273,0,251,231,245,245,273,254,238,255],
[241,249,0,254,250,258,266,249,244,251],
[258,269,246,0,256,252,281,263,253,263],
[230,255,250,244,0,246,242,252,227,237],
[232,255,242,248,254,0,261,219,224,244],
[243,227,234,219,258,239,0,237,244,222],
[241,246,251,237,248,281,263,0,253,250],
[232,262,256,247,273,276,256,247,0,257],
[226,245,249,237,263,256,278,250,243,0]])



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
result = np.append(np.array([10, 500, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,247,242,234,252,274,233,247,235],
[267,0,254,250,257,267,260,252,258,263],
[253,246,0,274,264,261,274,259,256,280],
[258,250,226,0,234,255,249,246,233,249],
[266,243,236,266,0,247,241,254,248,260],
[248,233,239,245,253,0,241,255,246,251],
[226,240,226,251,259,259,0,220,220,222],
[267,248,241,254,246,245,280,0,232,268],
[253,242,244,267,252,254,280,268,0,261],
[265,237,220,251,240,249,278,232,239,0]])



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
result = np.append(np.array([10, 500, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,231,252,245,228,237,247,234,248],
[272,0,244,257,248,275,263,266,253,250],
[269,256,0,259,248,279,286,259,244,277],
[248,243,241,0,257,251,273,269,242,262],
[255,252,252,243,0,239,259,242,234,245],
[272,225,221,249,261,0,246,260,253,236],
[263,237,214,227,241,254,0,262,246,253],
[253,234,241,231,258,240,238,0,254,250],
[266,247,256,258,266,247,254,246,0,244],
[252,250,223,238,255,264,247,250,256,0]])



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
result = np.append(np.array([10, 500, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,244,272,269,254,249,263,276,256],
[241,0,243,267,249,244,243,242,273,263],
[256,257,0,249,230,229,247,242,250,264],
[228,233,251,0,224,245,232,233,246,262],
[231,251,270,276,0,258,251,248,251,267],
[246,256,271,255,242,0,255,249,273,267],
[251,257,253,268,249,245,0,223,262,283],
[237,258,258,267,252,251,277,0,251,261],
[224,227,250,254,249,227,238,249,0,261],
[244,237,236,238,233,233,217,239,239,0]])



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
result = np.append(np.array([10, 500, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,227,241,239,245,261,221,220,230],
[247,0,244,244,257,239,271,238,238,246],
[273,256,0,258,258,249,274,257,249,261],
[259,256,242,0,247,258,252,254,254,239],
[261,243,242,253,0,246,243,235,228,237],
[255,261,251,242,254,0,254,231,249,228],
[239,229,226,248,257,246,0,243,240,244],
[279,262,243,246,265,269,257,0,255,261],
[280,262,251,246,272,251,260,245,0,242],
[270,254,239,261,263,272,256,239,258,0]])



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
result = np.append(np.array([10, 500, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,281,250,261,261,247,247,269,250],
[222,0,276,226,265,252,244,235,259,265],
[219,224,0,216,245,242,241,222,243,232],
[250,274,284,0,269,274,256,250,264,270],
[239,235,255,231,0,229,246,233,259,240],
[239,248,258,226,271,0,263,233,257,244],
[253,256,259,244,254,237,0,226,252,266],
[253,265,278,250,267,267,274,0,275,266],
[231,241,257,236,241,243,248,225,0,242],
[250,235,268,230,260,256,234,234,258,0]])



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
result = np.append(np.array([10, 500, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,229,263,234,256,240,237,242,266],
[276,0,245,267,255,257,254,259,246,260],
[271,255,0,279,252,270,256,247,253,282],
[237,233,221,0,232,227,229,234,250,253],
[266,245,248,268,0,266,238,241,252,282],
[244,243,230,273,234,0,236,239,237,264],
[260,246,244,271,262,264,0,263,255,272],
[263,241,253,266,259,261,237,0,247,278],
[258,254,247,250,248,263,245,253,0,262],
[234,240,218,247,218,236,228,222,238,0]])



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
result = np.append(np.array([10, 500, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,231,245,243,242,252,227,242,260],
[255,0,232,234,233,258,224,236,252,213],
[269,268,0,238,267,273,264,259,226,241],
[255,266,262,0,270,263,288,226,235,251],
[257,267,233,230,0,217,207,236,219,223],
[258,242,227,237,283,0,240,216,238,256],
[248,276,236,212,293,260,0,214,243,250],
[273,264,241,274,264,284,286,0,257,269],
[258,248,274,265,281,262,257,243,0,251],
[240,287,259,249,277,244,250,231,249,0]])



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
result = np.append(np.array([10, 500, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,276,265,254,248,255,257,254,261],
[220,0,255,258,235,237,232,253,238,252],
[224,245,0,237,238,230,220,230,216,233],
[235,242,263,0,238,249,230,241,242,243],
[246,265,262,262,0,242,253,261,263,282],
[252,263,270,251,258,0,257,241,245,262],
[245,268,280,270,247,243,0,260,250,271],
[243,247,270,259,239,259,240,0,235,257],
[246,262,284,258,237,255,250,265,0,251],
[239,248,267,257,218,238,229,243,249,0]])



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
result = np.append(np.array([10, 500, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,265,243,274,263,252,273,241,265],
[258,0,255,254,257,253,263,272,248,259],
[235,245,0,238,248,255,258,247,239,265],
[257,246,262,0,263,244,273,252,260,277],
[226,243,252,237,0,249,226,255,258,243],
[237,247,245,256,251,0,251,246,240,265],
[248,237,242,227,274,249,0,271,256,276],
[227,228,253,248,245,254,229,0,236,267],
[259,252,261,240,242,260,244,264,0,240],
[235,241,235,223,257,235,224,233,260,0]])



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
result = np.append(np.array([10, 500, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,255,236,256,251,210,227,256,255],
[265,0,227,242,274,287,240,273,251,229],
[245,273,0,254,242,262,250,224,226,234],
[264,258,246,0,223,285,239,213,240,212],
[244,226,258,277,0,258,249,236,229,216],
[249,213,238,215,242,0,205,205,201,212],
[290,260,250,261,251,295,0,259,232,229],
[273,227,276,287,264,295,241,0,240,263],
[244,249,274,260,271,299,268,260,0,226],
[245,271,266,288,284,288,271,237,274,0]])



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
result = np.append(np.array([10, 500, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,249,259,280,258,288,272,270,260],
[238,0,249,258,259,242,261,254,270,245],
[251,251,0,249,261,244,270,265,265,264],
[241,242,251,0,254,255,274,269,254,236],
[220,241,239,246,0,234,270,233,250,240],
[242,258,256,245,266,0,273,261,272,251],
[212,239,230,226,230,227,0,223,259,233],
[228,246,235,231,267,239,277,0,259,241],
[230,230,235,246,250,228,241,241,0,239],
[240,255,236,264,260,249,267,259,261,0]])



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
result = np.append(np.array([10, 500, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,274,269,267,271,255,231,275,244],
[237,0,261,240,237,232,247,232,237,224],
[226,239,0,244,242,236,242,249,256,218],
[231,260,256,0,253,246,234,265,259,237],
[233,263,258,247,0,252,258,247,264,226],
[229,268,264,254,248,0,249,241,260,251],
[245,253,258,266,242,251,0,245,263,233],
[269,268,251,235,253,259,255,0,248,245],
[225,263,244,241,236,240,237,252,0,238],
[256,276,282,263,274,249,267,255,262,0]])



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
result = np.append(np.array([10, 500, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,250,242,255,247,225,260,234,244],
[247,0,250,235,236,244,243,259,258,252],
[250,250,0,238,241,244,250,259,246,234],
[258,265,262,0,239,255,265,257,245,258],
[245,264,259,261,0,248,234,265,246,244],
[253,256,256,245,252,0,244,266,240,240],
[275,257,250,235,266,256,0,272,234,252],
[240,241,241,243,235,234,228,0,229,256],
[266,242,254,255,254,260,266,271,0,255],
[256,248,266,242,256,260,248,244,245,0]])



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
result = np.append(np.array([10, 500, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,263,240,272,254,268,245,256,260],
[241,0,241,231,270,230,296,259,253,241],
[237,259,0,240,248,249,251,253,242,250],
[260,269,260,0,249,249,284,259,282,249],
[228,230,252,251,0,212,248,260,236,228],
[246,270,251,251,288,0,255,283,268,229],
[232,204,249,216,252,245,0,221,209,238],
[255,241,247,241,240,217,279,0,241,250],
[244,247,258,218,264,232,291,259,0,241],
[240,259,250,251,272,271,262,250,259,0]])



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
result = np.append(np.array([10, 500, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,240,253,239,282,267,257,243,269],
[246,0,236,230,229,252,243,229,237,259],
[260,264,0,253,251,268,265,243,246,266],
[247,270,247,0,256,248,262,259,262,273],
[261,271,249,244,0,270,254,255,254,260],
[218,248,232,252,230,0,244,226,234,242],
[233,257,235,238,246,256,0,239,242,262],
[243,271,257,241,245,274,261,0,246,282],
[257,263,254,238,246,266,258,254,0,276],
[231,241,234,227,240,258,238,218,224,0]])



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
result = np.append(np.array([10, 500, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,190,218,194,192,259,226,203,202,153],
[310,0,295,273,236,290,266,253,242,253],
[282,205,0,279,243,220,300,240,266,243],
[306,227,221,0,246,269,278,232,232,222],
[308,264,257,254,0,272,324,223,287,248],
[241,210,280,231,228,0,264,226,252,262],
[274,234,200,222,176,236,0,203,231,165],
[297,247,260,268,277,274,297,0,285,235],
[298,258,234,268,213,248,269,215,0,222],
[347,247,257,278,252,238,335,265,278,0]])



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
result = np.append(np.array([10, 500, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,237,214,253,239,246,260,278,243],
[254,0,225,210,221,259,254,269,275,221],
[263,275,0,250,251,266,270,305,298,256],
[286,290,250,0,265,279,276,309,287,241],
[247,279,249,235,0,246,250,278,264,258],
[261,241,234,221,254,0,233,289,273,249],
[254,246,230,224,250,267,0,292,253,247],
[240,231,195,191,222,211,208,0,219,231],
[222,225,202,213,236,227,247,281,0,219],
[257,279,244,259,242,251,253,269,281,0]])



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
result = np.append(np.array([10, 500, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,255,270,262,266,259,244,263,251],
[253,0,251,251,244,240,246,244,243,239],
[245,249,0,255,244,242,254,249,252,251],
[230,249,245,0,241,229,243,248,248,228],
[238,256,256,259,0,246,249,254,247,244],
[234,260,258,271,254,0,247,254,261,260],
[241,254,246,257,251,253,0,255,264,245],
[256,256,251,252,246,246,245,0,261,240],
[237,257,248,252,253,239,236,239,0,251],
[249,261,249,272,256,240,255,260,249,0]])



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
result = np.append(np.array([10, 500, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,241,241,245,252,249,230,242,242],
[245,0,241,236,241,244,255,235,237,250],
[259,259,0,247,252,253,273,242,251,262],
[259,264,253,0,261,255,255,245,256,253],
[255,259,248,239,0,254,258,256,242,252],
[248,256,247,245,246,0,245,251,257,253],
[251,245,227,245,242,255,0,239,248,235],
[270,265,258,255,244,249,261,0,248,248],
[258,263,249,244,258,243,252,252,0,245],
[258,250,238,247,248,247,265,252,255,0]])



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
result = np.append(np.array([10, 500, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,292,231,234,247,247,247,274,235,245],
[208,0,249,232,230,239,210,249,220,242],
[269,251,0,226,244,253,246,292,260,240],
[266,268,274,0,278,253,251,283,241,244],
[253,270,256,222,0,249,263,279,227,269],
[253,261,247,247,251,0,272,259,247,215],
[253,290,254,249,237,228,0,309,246,250],
[226,251,208,217,221,241,191,0,215,198],
[265,280,240,259,273,253,254,285,0,220],
[255,258,260,256,231,285,250,302,280,0]])



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
result = np.append(np.array([10, 500, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,291,281,257,268,262,229,273,268],
[245,0,270,296,232,230,222,242,276,228],
[209,230,0,267,227,250,256,256,228,219],
[219,204,233,0,273,226,210,202,219,242],
[243,268,273,227,0,182,209,230,226,225],
[232,270,250,274,318,0,242,238,295,277],
[238,278,244,290,291,258,0,264,261,270],
[271,258,244,298,270,262,236,0,266,279],
[227,224,272,281,274,205,239,234,0,291],
[232,272,281,258,275,223,230,221,209,0]])



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
result = np.append(np.array([10, 500, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,241,251,257,260,244,243,257,254],
[243,0,252,241,245,246,242,241,256,257],
[259,248,0,263,250,272,248,250,255,249],
[249,259,237,0,252,237,236,249,239,257],
[243,255,250,248,0,250,252,248,237,254],
[240,254,228,263,250,0,232,245,239,246],
[256,258,252,264,248,268,0,266,246,264],
[257,259,250,251,252,255,234,0,252,268],
[243,244,245,261,263,261,254,248,0,252],
[246,243,251,243,246,254,236,232,248,0]])



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
result = np.append(np.array([10, 500, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,256,249,263,234,231,237,229,251],
[233,0,259,254,272,226,235,237,249,277],
[244,241,0,263,274,221,243,229,244,249],
[251,246,237,0,265,224,231,238,227,260],
[237,228,226,235,0,216,242,212,237,251],
[266,274,279,276,284,0,258,246,255,279],
[269,265,257,269,258,242,0,254,256,276],
[263,263,271,262,288,254,246,0,256,275],
[271,251,256,273,263,245,244,244,0,258],
[249,223,251,240,249,221,224,225,242,0]])



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
result = np.append(np.array([10, 500, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,275,268,265,242,241,258,250,249],
[231,0,263,241,255,245,243,240,241,228],
[225,237,0,246,261,217,225,255,257,251],
[232,259,254,0,265,227,234,245,227,242],
[235,245,239,235,0,213,233,227,250,240],
[258,255,283,273,287,0,242,263,256,264],
[259,257,275,266,267,258,0,272,256,238],
[242,260,245,255,273,237,228,0,249,239],
[250,259,243,273,250,244,244,251,0,245],
[251,272,249,258,260,236,262,261,255,0]])



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
result = np.append(np.array([10, 500, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,253,264,258,249,253,256,251,246],
[259,0,254,267,250,257,249,238,251,249],
[247,246,0,261,261,248,267,255,248,253],
[236,233,239,0,251,239,243,239,241,234],
[242,250,239,249,0,242,243,231,240,247],
[251,243,252,261,258,0,249,255,251,235],
[247,251,233,257,257,251,0,242,246,239],
[244,262,245,261,269,245,258,0,251,264],
[249,249,252,259,260,249,254,249,0,247],
[254,251,247,266,253,265,261,236,253,0]])



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
result = np.append(np.array([10, 500, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,260,230,243,265,284,259,263,254],
[258,0,259,241,235,247,268,242,258,230],
[240,241,0,238,241,245,272,240,250,251],
[270,259,262,0,261,250,272,248,250,254],
[257,265,259,239,0,255,275,276,264,250],
[235,253,255,250,245,0,273,263,250,243],
[216,232,228,228,225,227,0,252,238,219],
[241,258,260,252,224,237,248,0,244,230],
[237,242,250,250,236,250,262,256,0,234],
[246,270,249,246,250,257,281,270,266,0]])



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
result = np.append(np.array([10, 500, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,257,246,247,263,266,249,266,275],
[239,0,238,248,255,257,280,251,267,277],
[243,262,0,244,251,263,265,247,254,294],
[254,252,256,0,267,248,270,243,265,274],
[253,245,249,233,0,236,253,228,278,264],
[237,243,237,252,264,0,261,243,256,257],
[234,220,235,230,247,239,0,219,231,263],
[251,249,253,257,272,257,281,0,270,280],
[234,233,246,235,222,244,269,230,0,259],
[225,223,206,226,236,243,237,220,241,0]])



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
result = np.append(np.array([10, 500, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,229,329,274,271,295,258,278,279],
[253,0,245,241,245,228,231,251,257,228],
[271,255,0,277,288,256,252,227,307,257],
[171,259,223,0,219,232,257,256,251,256],
[226,255,212,281,0,263,254,245,239,274],
[229,272,244,268,237,0,294,240,264,227],
[205,269,248,243,246,206,0,240,228,280],
[242,249,273,244,255,260,260,0,268,262],
[222,243,193,249,261,236,272,232,0,228],
[221,272,243,244,226,273,220,238,272,0]])



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
result = np.append(np.array([10, 500, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,230,222,228,224,254,185,224,277],
[226,0,250,251,271,261,273,236,252,245],
[270,250,0,214,274,246,245,258,270,326],
[278,249,286,0,248,249,275,213,193,332],
[272,229,226,252,0,212,214,198,212,293],
[276,239,254,251,288,0,282,193,301,314],
[246,227,255,225,286,218,0,178,202,283],
[315,264,242,287,302,307,322,0,245,330],
[276,248,230,307,288,199,298,255,0,311],
[223,255,174,168,207,186,217,170,189,0]])



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
result = np.append(np.array([10, 500, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,259,247,261,258,247,255,238,248],
[228,0,235,235,266,259,248,245,237,244],
[241,265,0,248,277,269,248,266,254,238],
[253,265,252,0,268,280,259,257,233,240],
[239,234,223,232,0,258,246,237,230,230],
[242,241,231,220,242,0,254,238,223,233],
[253,252,252,241,254,246,0,259,255,248],
[245,255,234,243,263,262,241,0,250,239],
[262,263,246,267,270,277,245,250,0,260],
[252,256,262,260,270,267,252,261,240,0]])



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
result = np.append(np.array([10, 500, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,282,268,271,211,252,235,275,240],
[277,0,278,261,262,254,273,230,278,264],
[218,222,0,257,272,257,267,195,265,230],
[232,239,243,0,231,212,262,244,271,265],
[229,238,228,269,0,224,274,239,240,278],
[289,246,243,288,276,0,293,250,254,296],
[248,227,233,238,226,207,0,235,207,203],
[265,270,305,256,261,250,265,0,255,217],
[225,222,235,229,260,246,293,245,0,210],
[260,236,270,235,222,204,297,283,290,0]])



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
result = np.append(np.array([10, 500, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,242,253,233,250,246,236,239,268],
[259,0,233,241,245,251,250,248,249,263],
[258,267,0,252,246,253,253,236,263,274],
[247,259,248,0,235,256,259,241,248,254],
[267,255,254,265,0,257,236,248,254,259],
[250,249,247,244,243,0,246,251,242,264],
[254,250,247,241,264,254,0,257,256,274],
[264,252,264,259,252,249,243,0,247,278],
[261,251,237,252,246,258,244,253,0,261],
[232,237,226,246,241,236,226,222,239,0]])



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
result = np.append(np.array([10, 500, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_10_500.csv", index=False, header=False)