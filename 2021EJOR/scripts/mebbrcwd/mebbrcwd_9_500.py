
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,271,248,240,237,243,268,250,260],
[229,0,230,249,237,241,250,257,226],
[252,270,0,280,249,259,267,286,257],
[260,251,220,0,235,260,264,246,241],
[263,263,251,265,0,247,275,265,254],
[257,259,241,240,253,0,263,255,245],
[232,250,233,236,225,237,0,244,231],
[250,243,214,254,235,245,256,0,228],
[240,274,243,259,246,255,269,272,0]])



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
result = np.append(np.array([9, 500, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,255,271,270,248,276,257,251],
[228,0,242,253,238,224,243,249,225],
[245,258,0,265,259,223,252,266,229],
[229,247,235,0,232,235,229,249,238],
[230,262,241,268,0,233,242,243,232],
[252,276,277,265,267,0,253,276,249],
[224,257,248,271,258,247,0,246,257],
[243,251,234,251,257,224,254,0,222],
[249,275,271,262,268,251,243,278,0]])



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
result = np.append(np.array([9, 500, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,256,266,241,248,263,267,253],
[242,0,227,241,250,230,238,251,235],
[244,273,0,265,248,257,265,268,259],
[234,259,235,0,249,252,251,248,236],
[259,250,252,251,0,244,256,265,246],
[252,270,243,248,256,0,255,257,254],
[237,262,235,249,244,245,0,255,259],
[233,249,232,252,235,243,245,0,245],
[247,265,241,264,254,246,241,255,0]])



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
result = np.append(np.array([9, 500, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,253,230,246,242,262,238,255],
[250,0,252,242,267,230,251,235,237],
[247,248,0,246,283,241,265,265,246],
[270,258,254,0,270,232,256,245,234],
[254,233,217,230,0,228,240,223,232],
[258,270,259,268,272,0,245,243,243],
[238,249,235,244,260,255,0,229,251],
[262,265,235,255,277,257,271,0,276],
[245,263,254,266,268,257,249,224,0]])



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
result = np.append(np.array([9, 500, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,316,285,319,281,234,339,307],
[261,0,198,193,240,198,191,239,229],
[184,302,0,250,224,181,220,276,316],
[215,307,250,0,296,212,264,271,218],
[181,260,276,204,0,250,220,299,292],
[219,302,319,288,250,0,196,370,340],
[266,309,280,236,280,304,0,337,278],
[161,261,224,229,201,130,163,0,167],
[193,271,184,282,208,160,222,333,0]])



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
result = np.append(np.array([9, 500, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,243,254,247,245,267,243,251],
[253,0,231,235,231,244,253,242,246],
[257,269,0,241,264,260,274,258,267],
[246,265,259,0,246,255,270,253,239],
[253,269,236,254,0,240,251,245,247],
[255,256,240,245,260,0,256,238,250],
[233,247,226,230,249,244,0,248,248],
[257,258,242,247,255,262,252,0,237],
[249,254,233,261,253,250,252,263,0]])



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
result = np.append(np.array([9, 500, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,217,252,225,232,201,243,215],
[274,0,225,238,234,253,208,268,200],
[283,275,0,306,261,253,200,241,232],
[248,262,194,0,212,222,193,226,230],
[275,266,239,288,0,248,252,292,245],
[268,247,247,278,252,0,227,240,239],
[299,292,300,307,248,273,0,300,253],
[257,232,259,274,208,260,200,0,218],
[285,300,268,270,255,261,247,282,0]])



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
result = np.append(np.array([9, 500, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,247,263,250,250,255,254,251],
[241,0,233,253,235,246,260,252,244],
[253,267,0,270,251,257,249,266,259],
[237,247,230,0,237,240,245,244,257],
[250,265,249,263,0,249,245,258,246],
[250,254,243,260,251,0,242,253,239],
[245,240,251,255,255,258,0,265,249],
[246,248,234,256,242,247,235,0,246],
[249,256,241,243,254,261,251,254,0]])



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
result = np.append(np.array([9, 500, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,236,243,241,231,244,240,246],
[254,0,251,249,263,259,256,270,262],
[264,249,0,261,253,259,243,274,256],
[257,251,239,0,235,236,250,233,228],
[259,237,247,265,0,233,258,261,264],
[269,241,241,264,267,0,244,251,252],
[256,244,257,250,242,256,0,243,232],
[260,230,226,267,239,249,257,0,255],
[254,238,244,272,236,248,268,245,0]])



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
result = np.append(np.array([9, 500, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,254,262,247,262,253,254,253],
[247,0,244,236,236,268,259,252,236],
[246,256,0,242,237,263,255,244,220],
[238,264,258,0,252,278,250,258,246],
[253,264,263,248,0,263,240,275,247],
[238,232,237,222,237,0,238,247,230],
[247,241,245,250,260,262,0,239,231],
[246,248,256,242,225,253,261,0,218],
[247,264,280,254,253,270,269,282,0]])



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
result = np.append(np.array([9, 500, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,196,287,238,293,259,300,270,369],
[304,0,278,283,318,203,273,251,317],
[213,222,0,152,179,195,218,265,236],
[262,217,348,0,281,273,294,288,344],
[207,182,321,219,0,225,233,187,305],
[241,297,305,227,275,0,284,262,296],
[200,227,282,206,267,216,0,254,244],
[230,249,235,212,313,238,246,0,344],
[131,183,264,156,195,204,256,156,0]])



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
result = np.append(np.array([9, 500, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,201,230,221,268,267,241,233,246],
[299,0,217,261,264,266,247,269,240],
[270,283,0,278,307,258,275,261,248],
[279,239,222,0,236,243,249,261,242],
[232,236,193,264,0,228,236,224,226],
[233,234,242,257,272,0,228,226,232],
[259,253,225,251,264,272,0,240,225],
[267,231,239,239,276,274,260,0,251],
[254,260,252,258,274,268,275,249,0]])



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
result = np.append(np.array([9, 500, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,241,237,250,250,243,248,242],
[249,0,253,258,224,243,242,242,248],
[259,247,0,264,261,259,246,266,252],
[263,242,236,0,259,264,263,250,258],
[250,276,239,241,0,273,235,258,249],
[250,257,241,236,227,0,252,245,248],
[257,258,254,237,265,248,0,255,232],
[252,258,234,250,242,255,245,0,250],
[258,252,248,242,251,252,268,250,0]])



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
result = np.append(np.array([9, 500, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,208,231,255,203,173,266,214,196],
[292,0,272,301,306,244,305,288,276],
[269,228,0,252,304,246,294,285,223],
[245,199,248,0,288,250,275,306,266],
[297,194,196,212,0,227,249,239,173],
[327,256,254,250,273,0,288,262,282],
[234,195,206,225,251,212,0,252,205],
[286,212,215,194,261,238,248,0,235],
[304,224,277,234,327,218,295,265,0]])



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
result = np.append(np.array([9, 500, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,247,263,270,261,287,256,276],
[246,0,246,256,250,260,263,263,255],
[253,254,0,264,262,249,268,268,266],
[237,244,236,0,250,234,254,263,254],
[230,250,238,250,0,212,239,252,260],
[239,240,251,266,288,0,274,275,257],
[213,237,232,246,261,226,0,245,232],
[244,237,232,237,248,225,255,0,246],
[224,245,234,246,240,243,268,254,0]])



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
result = np.append(np.array([9, 500, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,246,247,254,272,226,209,252],
[235,0,242,228,240,258,210,232,254],
[254,258,0,230,239,252,224,245,248],
[253,272,270,0,245,246,227,242,251],
[246,260,261,255,0,255,236,238,256],
[228,242,248,254,245,0,226,252,240],
[274,290,276,273,264,274,0,249,267],
[291,268,255,258,262,248,251,0,265],
[248,246,252,249,244,260,233,235,0]])



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
result = np.append(np.array([9, 500, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,195,214,159,206,194,159,149,173],
[305,0,279,240,227,246,243,294,245],
[286,221,0,226,231,236,235,272,205],
[341,260,274,0,254,244,283,221,254],
[294,273,269,246,0,241,281,238,249],
[306,254,264,256,259,0,265,236,251],
[341,257,265,217,219,235,0,225,210],
[351,206,228,279,262,264,275,0,208],
[327,255,295,246,251,249,290,292,0]])



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
result = np.append(np.array([9, 500, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,264,239,260,252,242,257,257],
[239,0,248,234,252,230,234,220,244],
[236,252,0,223,251,215,250,240,262],
[261,266,277,0,264,249,265,255,280],
[240,248,249,236,0,234,235,235,250],
[248,270,285,251,266,0,258,253,277],
[258,266,250,235,265,242,0,241,249],
[243,280,260,245,265,247,259,0,256],
[243,256,238,220,250,223,251,244,0]])



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
result = np.append(np.array([9, 500, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,231,241,244,249,241,252,241],
[250,0,235,264,259,251,263,250,245],
[269,265,0,272,246,260,265,264,259],
[259,236,228,0,216,242,247,244,240],
[256,241,254,284,0,250,246,273,243],
[251,249,240,258,250,0,235,252,231],
[259,237,235,253,254,265,0,240,228],
[248,250,236,256,227,248,260,0,235],
[259,255,241,260,257,269,272,265,0]])



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
result = np.append(np.array([9, 500, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,252,266,260,268,271,271,236],
[262,0,257,249,235,285,258,246,229],
[248,243,0,230,266,255,279,244,256],
[234,251,270,0,268,277,266,270,250],
[240,265,234,232,0,257,273,246,237],
[232,215,245,223,243,0,237,196,209],
[229,242,221,234,227,263,0,212,226],
[229,254,256,230,254,304,288,0,250],
[264,271,244,250,263,291,274,250,0]])



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
result = np.append(np.array([9, 500, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,243,239,215,284,231,241,285],
[245,0,259,208,255,254,274,251,287],
[257,241,0,259,256,289,284,192,223],
[261,292,241,0,252,278,266,200,276],
[285,245,244,248,0,303,299,218,327],
[216,246,211,222,197,0,282,211,306],
[269,226,216,234,201,218,0,203,286],
[259,249,308,300,282,289,297,0,302],
[215,213,277,224,173,194,214,198,0]])



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
result = np.append(np.array([9, 500, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,231,236,261,227,252,255,253],
[247,0,249,260,272,234,253,264,237],
[269,251,0,252,272,249,246,251,251],
[264,240,248,0,264,229,247,249,238],
[239,228,228,236,0,224,220,238,230],
[273,266,251,271,276,0,246,250,259],
[248,247,254,253,280,254,0,254,234],
[245,236,249,251,262,250,246,0,252],
[247,263,249,262,270,241,266,248,0]])



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
result = np.append(np.array([9, 500, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,249,248,244,259,244,247,249],
[249,0,255,240,257,274,250,260,257],
[251,245,0,240,247,257,255,249,246],
[252,260,260,0,249,259,234,271,262],
[256,243,253,251,0,256,237,270,266],
[241,226,243,241,244,0,238,264,239],
[256,250,245,266,263,262,0,258,262],
[253,240,251,229,230,236,242,0,253],
[251,243,254,238,234,261,238,247,0]])



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
result = np.append(np.array([9, 500, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,244,273,272,258,265,253,232],
[241,0,247,275,248,248,260,262,244],
[256,253,0,280,225,247,273,252,238],
[227,225,220,0,233,239,249,252,220],
[228,252,275,267,0,261,266,259,267],
[242,252,253,261,239,0,246,263,247],
[235,240,227,251,234,254,0,234,242],
[247,238,248,248,241,237,266,0,256],
[268,256,262,280,233,253,258,244,0]])



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
result = np.append(np.array([9, 500, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,231,235,315,140,264,148,181],
[233,0,281,277,164,305,412,224,255],
[269,219,0,319,333,333,273,207,253],
[265,223,181,0,254,223,273,271,223],
[185,336,167,246,0,257,307,226,224],
[360,195,167,277,243,0,200,224,215],
[236,88,227,227,193,300,0,174,334],
[352,276,293,229,274,276,326,0,277],
[319,245,247,277,276,285,166,223,0]])



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
result = np.append(np.array([9, 500, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,259,243,264,250,238,252,238],
[253,0,197,235,217,247,207,219,200],
[241,303,0,258,261,260,255,246,234],
[257,265,242,0,290,283,246,272,241],
[236,283,239,210,0,246,237,239,215],
[250,253,240,217,254,0,215,234,233],
[262,293,245,254,263,285,0,255,265],
[248,281,254,228,261,266,245,0,243],
[262,300,266,259,285,267,235,257,0]])



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
result = np.append(np.array([9, 500, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,236,211,244,247,216,254,233],
[253,0,225,235,255,264,246,231,256],
[264,275,0,241,233,248,236,249,227],
[289,265,259,0,267,254,244,265,238],
[256,245,267,233,0,263,238,266,253],
[253,236,252,246,237,0,245,251,242],
[284,254,264,256,262,255,0,273,250],
[246,269,251,235,234,249,227,0,240],
[267,244,273,262,247,258,250,260,0]])



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
result = np.append(np.array([9, 500, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,253,261,269,280,262,241,287],
[234,0,234,227,221,229,243,237,264],
[247,266,0,238,242,221,254,245,256],
[239,273,262,0,255,252,270,267,264],
[231,279,258,245,0,260,258,235,258],
[220,271,279,248,240,0,247,247,246],
[238,257,246,230,242,253,0,244,245],
[259,263,255,233,265,253,256,0,258],
[213,236,244,236,242,254,255,242,0]])



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
result = np.append(np.array([9, 500, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,270,250,268,265,261,277,269],
[249,0,263,237,256,264,267,242,279],
[230,237,0,219,249,257,243,232,262],
[250,263,281,0,275,286,256,275,290],
[232,244,251,225,0,258,247,231,255],
[235,236,243,214,242,0,249,245,243],
[239,233,257,244,253,251,0,250,251],
[223,258,268,225,269,255,250,0,252],
[231,221,238,210,245,257,249,248,0]])



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
result = np.append(np.array([9, 500, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,234,252,239,216,212,234,219],
[253,0,228,236,235,212,244,229,214],
[266,272,0,257,245,217,243,241,230],
[248,264,243,0,243,253,240,224,235],
[261,265,255,257,0,251,262,233,240],
[284,288,283,247,249,0,258,237,226],
[288,256,257,260,238,242,0,240,251],
[266,271,259,276,267,263,260,0,249],
[281,286,270,265,260,274,249,251,0]])



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
result = np.append(np.array([9, 500, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,163,216,178,210,246,220,264,192],
[337,0,298,226,267,289,279,288,236],
[284,202,0,183,196,233,237,272,197],
[322,274,317,0,247,252,267,299,243],
[290,233,304,253,0,273,261,341,198],
[254,211,267,248,227,0,206,325,236],
[280,221,263,233,239,294,0,299,275],
[236,212,228,201,159,175,201,0,238],
[308,264,303,257,302,264,225,262,0]])



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
result = np.append(np.array([9, 500, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,242,268,262,249,245,281,272],
[249,0,263,269,246,258,247,282,244],
[258,237,0,287,239,273,253,270,265],
[232,231,213,0,225,234,212,246,238],
[238,254,261,275,0,267,248,275,259],
[251,242,227,266,233,0,251,261,241],
[255,253,247,288,252,249,0,277,288],
[219,218,230,254,225,239,223,0,265],
[228,256,235,262,241,259,212,235,0]])



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
result = np.append(np.array([9, 500, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,275,256,252,270,239,254,256],
[239,0,249,225,196,243,221,210,225],
[225,251,0,236,222,243,234,209,221],
[244,275,264,0,258,295,270,235,247],
[248,304,278,242,0,257,263,257,295],
[230,257,257,205,243,0,220,212,241],
[261,279,266,230,237,280,0,238,241],
[246,290,291,265,243,288,262,0,263],
[244,275,279,253,205,259,259,237,0]])



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
result = np.append(np.array([9, 500, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,268,260,250,256,257,249,248],
[242,0,264,262,237,251,245,242,245],
[232,236,0,238,234,226,228,241,245],
[240,238,262,0,236,234,252,252,250],
[250,263,266,264,0,240,246,252,259],
[244,249,274,266,260,0,261,254,241],
[243,255,272,248,254,239,0,264,261],
[251,258,259,248,248,246,236,0,241],
[252,255,255,250,241,259,239,259,0]])



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
result = np.append(np.array([9, 500, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,280,253,260,258,239,253,261],
[246,0,242,239,244,250,243,247,263],
[220,258,0,240,253,253,237,246,239],
[247,261,260,0,260,264,243,259,262],
[240,256,247,240,0,250,243,250,253],
[242,250,247,236,250,0,246,237,262],
[261,257,263,257,257,254,0,247,247],
[247,253,254,241,250,263,253,0,237],
[239,237,261,238,247,238,253,263,0]])



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
result = np.append(np.array([9, 500, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,272,256,268,245,258,242,276],
[244,0,244,240,274,239,250,236,261],
[228,256,0,253,267,242,246,251,259],
[244,260,247,0,274,235,253,236,243],
[232,226,233,226,0,241,239,217,262],
[255,261,258,265,259,0,262,237,281],
[242,250,254,247,261,238,0,220,241],
[258,264,249,264,283,263,280,0,265],
[224,239,241,257,238,219,259,235,0]])



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
result = np.append(np.array([9, 500, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,211,262,258,217,226,256,221,258],
[289,0,261,265,262,265,236,252,246],
[238,239,0,243,244,248,207,232,267],
[242,235,257,0,253,223,243,234,269],
[283,238,256,247,0,267,209,220,268],
[274,235,252,277,233,0,279,280,267],
[244,264,293,257,291,221,0,269,264],
[279,248,268,266,280,220,231,0,274],
[242,254,233,231,232,233,236,226,0]])



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
result = np.append(np.array([9, 500, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,245,260,282,257,261,260,252],
[245,0,237,252,261,251,257,257,257],
[255,263,0,266,271,247,249,243,266],
[240,248,234,0,256,238,241,243,258],
[218,239,229,244,0,245,246,231,242],
[243,249,253,262,255,0,244,236,280],
[239,243,251,259,254,256,0,248,266],
[240,243,257,257,269,264,252,0,264],
[248,243,234,242,258,220,234,236,0]])



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
result = np.append(np.array([9, 500, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,244,263,249,246,249,236,244],
[258,0,263,277,277,262,259,248,253],
[256,237,0,238,251,242,250,252,241],
[237,223,262,0,249,235,243,241,245],
[251,223,249,251,0,252,239,240,224],
[254,238,258,265,248,0,241,250,244],
[251,241,250,257,261,259,0,250,251],
[264,252,248,259,260,250,250,0,249],
[256,247,259,255,276,256,249,251,0]])



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
result = np.append(np.array([9, 500, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,269,272,262,246,257,263,269],
[237,0,267,237,251,244,224,266,254],
[231,233,0,233,233,253,247,248,255],
[228,263,267,0,237,226,239,246,252],
[238,249,267,263,0,252,254,258,250],
[254,256,247,274,248,0,260,250,272],
[243,276,253,261,246,240,0,252,279],
[237,234,252,254,242,250,248,0,252],
[231,246,245,248,250,228,221,248,0]])



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
result = np.append(np.array([9, 500, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,241,279,232,270,271,223,300],
[229,0,232,221,182,207,181,181,245],
[259,268,0,235,268,245,193,212,267],
[221,279,265,0,276,238,248,230,240],
[268,318,232,224,0,250,269,254,301],
[230,293,255,262,250,0,283,231,268],
[229,319,307,252,231,217,0,221,264],
[277,319,288,270,246,269,279,0,318],
[200,255,233,260,199,232,236,182,0]])



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
result = np.append(np.array([9, 500, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,275,262,275,270,256,260,260],
[270,0,286,263,293,264,270,249,285],
[225,214,0,228,264,244,235,220,252],
[238,237,272,0,258,249,249,260,278],
[225,207,236,242,0,251,241,215,239],
[230,236,256,251,249,0,244,253,245],
[244,230,265,251,259,256,0,242,272],
[240,251,280,240,285,247,258,0,261],
[240,215,248,222,261,255,228,239,0]])



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
result = np.append(np.array([9, 500, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,244,251,258,250,246,265,262],
[236,0,248,271,260,252,247,253,240],
[256,252,0,248,255,245,259,255,274],
[249,229,252,0,237,238,239,246,268],
[242,240,245,263,0,253,244,240,252],
[250,248,255,262,247,0,241,242,272],
[254,253,241,261,256,259,0,251,258],
[235,247,245,254,260,258,249,0,248],
[238,260,226,232,248,228,242,252,0]])



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
result = np.append(np.array([9, 500, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,234,184,234,229,223,203,219],
[269,0,243,260,252,252,239,213,246],
[266,257,0,233,252,228,217,263,272],
[316,240,267,0,246,266,262,236,237],
[266,248,248,254,0,241,236,248,254],
[271,248,272,234,259,0,263,259,264],
[277,261,283,238,264,237,0,248,242],
[297,287,237,264,252,241,252,0,236],
[281,254,228,263,246,236,258,264,0]])



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
result = np.append(np.array([9, 500, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,233,221,226,258,227,260,226],
[267,0,252,271,282,243,254,304,248],
[267,248,0,255,273,226,240,291,242],
[279,229,245,0,254,230,244,254,228],
[274,218,227,246,0,241,242,261,255],
[242,257,274,270,259,0,239,270,265],
[273,246,260,256,258,261,0,293,246],
[240,196,209,246,239,230,207,0,212],
[274,252,258,272,245,235,254,288,0]])



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
result = np.append(np.array([9, 500, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,273,222,215,243,213,202,229],
[277,0,291,224,256,263,287,250,267],
[227,209,0,227,220,218,247,210,209],
[278,276,273,0,241,271,235,233,241],
[285,244,280,259,0,309,267,253,283],
[257,237,282,229,191,0,251,214,216],
[287,213,253,265,233,249,0,236,241],
[298,250,290,267,247,286,264,0,252],
[271,233,291,259,217,284,259,248,0]])



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
result = np.append(np.array([9, 500, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,249,259,256,246,246,227,251],
[250,0,273,273,267,256,251,252,260],
[251,227,0,254,258,234,239,249,255],
[241,227,246,0,268,228,250,247,258],
[244,233,242,232,0,231,233,235,244],
[254,244,266,272,269,0,247,242,255],
[254,249,261,250,267,253,0,247,263],
[273,248,251,253,265,258,253,0,256],
[249,240,245,242,256,245,237,244,0]])



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
result = np.append(np.array([9, 500, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,210,231,207,200,169,196,212,279],
[290,0,247,240,193,175,241,227,314],
[269,253,0,244,225,154,228,215,231],
[293,260,256,0,280,179,227,249,265],
[300,307,275,220,0,253,262,270,270],
[331,325,346,321,247,0,338,297,310],
[304,259,272,273,238,162,0,268,282],
[288,273,285,251,230,203,232,0,234],
[221,186,269,235,230,190,218,266,0]])



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
result = np.append(np.array([9, 500, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,255,264,255,258,270,275,239],
[243,0,252,267,247,255,257,269,232],
[245,248,0,257,238,253,260,255,237],
[236,233,243,0,227,246,243,252,236],
[245,253,262,273,0,259,271,272,256],
[242,245,247,254,241,0,261,247,251],
[230,243,240,257,229,239,0,251,242],
[225,231,245,248,228,253,249,0,212],
[261,268,263,264,244,249,258,288,0]])



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
result = np.append(np.array([9, 500, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,246,257,272,276,230,269,251],
[259,0,240,273,286,265,227,271,259],
[254,260,0,291,261,290,236,244,268],
[243,227,209,0,239,262,221,220,236],
[228,214,239,261,0,250,221,238,248],
[224,235,210,238,250,0,237,232,244],
[270,273,264,279,279,263,0,244,283],
[231,229,256,280,262,268,256,0,268],
[249,241,232,264,252,256,217,232,0]])



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
result = np.append(np.array([9, 500, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,269,246,242,238,266,259,230],
[225,0,233,217,253,218,252,227,218],
[231,267,0,235,253,233,243,236,246],
[254,283,265,0,271,245,267,244,254],
[258,247,247,229,0,214,246,247,215],
[262,282,267,255,286,0,276,283,248],
[234,248,257,233,254,224,0,261,238],
[241,273,264,256,253,217,239,0,228],
[270,282,254,246,285,252,262,272,0]])



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
result = np.append(np.array([9, 500, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,231,264,247,262,249,239,249],
[260,0,253,275,259,263,250,263,243],
[269,247,0,268,253,249,262,239,247],
[236,225,232,0,239,235,252,235,244],
[253,241,247,261,0,248,267,238,239],
[238,237,251,265,252,0,248,253,247],
[251,250,238,248,233,252,0,229,247],
[261,237,261,265,262,247,271,0,264],
[251,257,253,256,261,253,253,236,0]])



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
result = np.append(np.array([9, 500, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,334,284,300,245,373,307,379,368],
[166,0,200,216,266,262,203,308,369],
[216,300,0,309,252,212,198,227,337],
[200,284,191,0,238,227,236,242,297],
[255,234,248,262,0,220,213,255,312],
[127,238,288,273,280,0,267,258,394],
[193,297,302,264,287,233,0,275,317],
[121,192,273,258,245,242,225,0,269],
[132,131,163,203,188,106,183,231,0]])



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
result = np.append(np.array([9, 500, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,239,239,252,253,262,249,269],
[250,0,230,256,241,236,255,267,246],
[261,270,0,274,259,263,263,236,291],
[261,244,226,0,241,257,263,273,255],
[248,259,241,259,0,244,264,267,264],
[247,264,237,243,256,0,291,267,272],
[238,245,237,237,236,209,0,253,242],
[251,233,264,227,233,233,247,0,252],
[231,254,209,245,236,228,258,248,0]])



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
result = np.append(np.array([9, 500, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,244,278,248,252,269,268,271],
[249,0,254,248,251,252,244,225,266],
[256,246,0,265,253,247,242,249,261],
[222,252,235,0,254,256,251,231,262],
[252,249,247,246,0,246,239,255,264],
[248,248,253,244,254,0,235,251,225],
[231,256,258,249,261,265,0,242,259],
[232,275,251,269,245,249,258,0,262],
[229,234,239,238,236,275,241,238,0]])



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
result = np.append(np.array([9, 500, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,212,263,270,265,298,299,266],
[223,0,228,235,178,240,270,201,252],
[288,272,0,283,226,274,288,233,294],
[237,265,217,0,214,213,292,170,227],
[230,322,274,286,0,326,310,251,274],
[235,260,226,287,174,0,305,244,287],
[202,230,212,208,190,195,0,174,209],
[201,299,267,330,249,256,326,0,294],
[234,248,206,273,226,213,291,206,0]])



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
result = np.append(np.array([9, 500, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,219,284,265,269,261,259,234],
[277,0,250,292,237,316,300,351,217],
[281,250,0,289,247,305,295,291,271],
[216,208,211,0,223,249,200,261,201],
[235,263,253,277,0,332,261,321,264],
[231,184,195,251,168,0,218,252,190],
[239,200,205,300,239,282,0,284,240],
[241,149,209,239,179,248,216,0,234],
[266,283,229,299,236,310,260,266,0]])



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
result = np.append(np.array([9, 500, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,270,242,263,156,207,248,253],
[272,0,239,253,276,282,271,274,302],
[230,261,0,245,246,262,236,249,293],
[258,247,255,0,254,198,227,236,282],
[237,224,254,246,0,186,203,237,228],
[344,218,238,302,314,0,245,256,357],
[293,229,264,273,297,255,0,280,288],
[252,226,251,264,263,244,220,0,256],
[247,198,207,218,272,143,212,244,0]])



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
result = np.append(np.array([9, 500, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,263,247,260,256,242,248,253],
[251,0,250,255,264,251,252,251,257],
[237,250,0,250,246,252,233,235,258],
[253,245,250,0,250,252,247,242,255],
[240,236,254,250,0,247,255,255,248],
[244,249,248,248,253,0,252,248,249],
[258,248,267,253,245,248,0,261,250],
[252,249,265,258,245,252,239,0,251],
[247,243,242,245,252,251,250,249,0]])



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
result = np.append(np.array([9, 500, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,246,260,279,279,282,287,276],
[240,0,247,258,239,257,260,260,274],
[254,253,0,274,259,285,266,279,236],
[240,242,226,0,234,245,245,253,252],
[221,261,241,266,0,261,270,260,269],
[221,243,215,255,239,0,245,265,239],
[218,240,234,255,230,255,0,261,252],
[213,240,221,247,240,235,239,0,260],
[224,226,264,248,231,261,248,240,0]])



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
result = np.append(np.array([9, 500, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,293,265,276,249,186,260,218],
[263,0,261,288,300,215,223,257,236],
[207,239,0,246,239,230,211,237,220],
[235,212,254,0,267,227,210,230,211],
[224,200,261,233,0,209,196,259,201],
[251,285,270,273,291,0,227,273,266],
[314,277,289,290,304,273,0,291,226],
[240,243,263,270,241,227,209,0,227],
[282,264,280,289,299,234,274,273,0]])



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
result = np.append(np.array([9, 500, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,334,238,267,234,334,248,317,375],
[166,0,130,265,199,255,138,171,313],
[262,370,0,312,240,287,138,218,264],
[233,235,188,0,196,279,230,227,341],
[266,301,260,304,0,324,209,250,280],
[166,245,213,221,176,0,124,172,234],
[252,362,362,270,291,376,0,193,350],
[183,329,282,273,250,328,307,0,305],
[125,187,236,159,220,266,150,195,0]])



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
result = np.append(np.array([9, 500, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,221,270,226,265,230,266,237],
[248,0,270,281,212,203,252,249,276],
[279,230,0,219,238,283,246,223,273],
[230,219,281,0,250,210,248,312,281],
[274,288,262,250,0,260,239,256,229],
[235,297,217,290,240,0,278,302,299],
[270,248,254,252,261,222,0,242,293],
[234,251,277,188,244,198,258,0,288],
[263,224,227,219,271,201,207,212,0]])



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
result = np.append(np.array([9, 500, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,232,253,251,229,245,246,218],
[264,0,256,270,243,242,240,250,258],
[268,244,0,261,255,266,244,258,237],
[247,230,239,0,238,239,245,237,245],
[249,257,245,262,0,259,265,258,238],
[271,258,234,261,241,0,253,257,241],
[255,260,256,255,235,247,0,250,249],
[254,250,242,263,242,243,250,0,238],
[282,242,263,255,262,259,251,262,0]])



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
result = np.append(np.array([9, 500, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,247,228,241,226,231,219,235],
[258,0,238,221,228,224,253,250,248],
[253,262,0,231,253,257,251,258,248],
[272,279,269,0,237,249,268,266,256],
[259,272,247,263,0,244,270,243,247],
[274,276,243,251,256,0,286,250,248],
[269,247,249,232,230,214,0,251,256],
[281,250,242,234,257,250,249,0,243],
[265,252,252,244,253,252,244,257,0]])



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
result = np.append(np.array([9, 500, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,245,241,264,264,251,266,249],
[246,0,245,245,230,241,243,238,246],
[255,255,0,257,244,266,237,257,253],
[259,255,243,0,231,263,251,274,252],
[236,270,256,269,0,274,262,266,256],
[236,259,234,237,226,0,242,231,219],
[249,257,263,249,238,258,0,249,259],
[234,262,243,226,234,269,251,0,244],
[251,254,247,248,244,281,241,256,0]])



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
result = np.append(np.array([9, 500, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,242,263,259,255,260,256,255],
[251,0,239,258,269,260,253,259,271],
[258,261,0,269,276,275,239,255,272],
[237,242,231,0,267,262,256,263,260],
[241,231,224,233,0,242,229,250,251],
[245,240,225,238,258,0,255,241,238],
[240,247,261,244,271,245,0,265,266],
[244,241,245,237,250,259,235,0,246],
[245,229,228,240,249,262,234,254,0]])



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
result = np.append(np.array([9, 500, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,243,246,272,216,238,220,212],
[262,0,254,250,283,222,271,256,272],
[257,246,0,234,298,219,267,224,245],
[254,250,266,0,272,219,272,251,214],
[228,217,202,228,0,190,227,192,235],
[284,278,281,281,310,0,274,250,255],
[262,229,233,228,273,226,0,210,233],
[280,244,276,249,308,250,290,0,255],
[288,228,255,286,265,245,267,245,0]])



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
result = np.append(np.array([9, 500, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,296,268,242,223,260,307,249,263],
[204,0,237,254,179,260,314,219,248],
[232,263,0,221,232,254,272,227,217],
[258,246,279,0,232,259,288,264,225],
[277,321,268,268,0,278,298,257,250],
[240,240,246,241,222,0,264,249,193],
[193,186,228,212,202,236,0,227,219],
[251,281,273,236,243,251,273,0,235],
[237,252,283,275,250,307,281,265,0]])



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
result = np.append(np.array([9, 500, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,254,238,241,271,242,273,250],
[242,0,250,249,240,268,234,256,251],
[246,250,0,226,234,254,241,266,244],
[262,251,274,0,239,275,246,268,257],
[259,260,266,261,0,268,241,277,254],
[229,232,246,225,232,0,233,246,229],
[258,266,259,254,259,267,0,267,244],
[227,244,234,232,223,254,233,0,236],
[250,249,256,243,246,271,256,264,0]])



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
result = np.append(np.array([9, 500, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,236,250,249,269,255,249,243],
[246,0,255,250,267,287,248,250,269],
[264,245,0,260,272,273,252,272,262],
[250,250,240,0,258,262,245,280,249],
[251,233,228,242,0,278,238,259,241],
[231,213,227,238,222,0,249,246,215],
[245,252,248,255,262,251,0,255,248],
[251,250,228,220,241,254,245,0,235],
[257,231,238,251,259,285,252,265,0]])



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
result = np.append(np.array([9, 500, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,222,260,248,262,245,257,236],
[252,0,244,261,263,273,263,242,256],
[278,256,0,283,251,273,249,260,248],
[240,239,217,0,257,267,221,238,240],
[252,237,249,243,0,267,260,250,256],
[238,227,227,233,233,0,239,244,221],
[255,237,251,279,240,261,0,254,252],
[243,258,240,262,250,256,246,0,250],
[264,244,252,260,244,279,248,250,0]])



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
result = np.append(np.array([9, 500, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,260,254,239,252,243,269,255],
[252,0,265,247,251,255,258,254,252],
[240,235,0,244,236,245,239,251,241],
[246,253,256,0,241,250,260,249,267],
[261,249,264,259,0,256,255,256,260],
[248,245,255,250,244,0,242,250,257],
[257,242,261,240,245,258,0,238,254],
[231,246,249,251,244,250,262,0,249],
[245,248,259,233,240,243,246,251,0]])



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
result = np.append(np.array([9, 500, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,248,258,253,267,268,258,261],
[250,0,252,250,249,270,259,249,256],
[252,248,0,250,241,268,274,248,253],
[242,250,250,0,243,264,254,242,246],
[247,251,259,257,0,261,256,236,254],
[233,230,232,236,239,0,259,235,238],
[232,241,226,246,244,241,0,229,255],
[242,251,252,258,264,265,271,0,266],
[239,244,247,254,246,262,245,234,0]])



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
result = np.append(np.array([9, 500, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,260,224,265,253,278,266,270],
[264,0,238,219,259,254,248,247,276],
[240,262,0,256,271,255,259,266,273],
[276,281,244,0,279,263,254,252,251],
[235,241,229,221,0,244,247,267,240],
[247,246,245,237,256,0,235,256,270],
[222,252,241,246,253,265,0,255,237],
[234,253,234,248,233,244,245,0,261],
[230,224,227,249,260,230,263,239,0]])



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
result = np.append(np.array([9, 500, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,175,393,311,486,257,175,311],
[271,0,257,393,257,364,257,350,189],
[325,243,0,325,404,418,175,268,325],
[107,107,175,0,93,107,93,93,14],
[189,243,96,407,0,418,189,268,325],
[14,136,82,393,82,0,175,0,325],
[243,243,325,407,311,325,0,311,150],
[325,150,232,407,232,500,189,0,325],
[189,311,175,486,175,175,350,175,0]])



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
result = np.append(np.array([9, 500, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,304,286,274,253,259,269,251,250],
[196,0,264,270,206,217,210,238,202],
[214,236,0,246,225,210,220,214,236],
[226,230,254,0,208,245,212,220,203],
[247,294,275,292,0,264,263,295,246],
[241,283,290,255,236,0,236,227,223],
[231,290,280,288,237,264,0,236,233],
[249,262,286,280,205,273,264,0,215],
[250,298,264,297,254,277,267,285,0]])



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
result = np.append(np.array([9, 500, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,241,233,259,248,247,246,263],
[258,0,239,268,256,263,251,244,267],
[259,261,0,252,272,271,259,251,250],
[267,232,248,0,279,255,239,238,253],
[241,244,228,221,0,242,224,235,250],
[252,237,229,245,258,0,220,218,254],
[253,249,241,261,276,280,0,234,251],
[254,256,249,262,265,282,266,0,252],
[237,233,250,247,250,246,249,248,0]])



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
result = np.append(np.array([9, 500, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,234,248,241,259,246,261,255],
[234,0,237,224,250,244,228,225,247],
[266,263,0,241,239,268,251,244,245],
[252,276,259,0,251,263,247,258,266],
[259,250,261,249,0,250,250,237,260],
[241,256,232,237,250,0,231,240,244],
[254,272,249,253,250,269,0,247,272],
[239,275,256,242,263,260,253,0,239],
[245,253,255,234,240,256,228,261,0]])



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
result = np.append(np.array([9, 500, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,263,258,257,246,261,240,257],
[250,0,237,263,262,247,269,262,266],
[237,263,0,264,269,250,258,257,251],
[242,237,236,0,264,231,253,234,245],
[243,238,231,236,0,228,254,243,253],
[254,253,250,269,272,0,268,248,259],
[239,231,242,247,246,232,0,226,251],
[260,238,243,266,257,252,274,0,244],
[243,234,249,255,247,241,249,256,0]])



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
result = np.append(np.array([9, 500, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,235,223,254,229,236,226,236],
[280,0,263,239,279,232,239,246,247],
[265,237,0,238,262,251,248,240,249],
[277,261,262,0,278,257,250,254,241],
[246,221,238,222,0,236,238,247,229],
[271,268,249,243,264,0,243,244,266],
[264,261,252,250,262,257,0,241,227],
[274,254,260,246,253,256,259,0,259],
[264,253,251,259,271,234,273,241,0]])



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
result = np.append(np.array([9, 500, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,247,247,242,258,263,253,256],
[253,0,253,247,248,270,254,259,247],
[253,247,0,251,254,270,246,259,262],
[253,253,249,0,257,264,254,259,269],
[258,252,246,243,0,266,251,253,269],
[242,230,230,236,234,0,241,242,250],
[237,246,254,246,249,259,0,252,251],
[247,241,241,241,247,258,248,0,257],
[244,253,238,231,231,250,249,243,0]])



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
result = np.append(np.array([9, 500, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,243,245,245,245,252,263,242],
[253,0,252,242,241,247,253,255,222],
[257,248,0,250,244,256,252,255,245],
[255,258,250,0,239,228,257,263,241],
[255,259,256,261,0,254,257,276,250],
[255,253,244,272,246,0,250,260,241],
[248,247,248,243,243,250,0,266,243],
[237,245,245,237,224,240,234,0,224],
[258,278,255,259,250,259,257,276,0]])



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
result = np.append(np.array([9, 500, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,255,248,244,264,254,254,232],
[227,0,239,239,227,236,237,240,224],
[245,261,0,235,239,240,232,231,217],
[252,261,265,0,247,259,253,250,235],
[256,273,261,253,0,250,253,257,255],
[236,264,260,241,250,0,256,246,238],
[246,263,268,247,247,244,0,247,244],
[246,260,269,250,243,254,253,0,225],
[268,276,283,265,245,262,256,275,0]])



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
result = np.append(np.array([9, 500, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,235,274,317,268,259,292,244],
[226,0,223,257,271,255,255,276,257],
[265,277,0,295,278,250,284,295,249],
[226,243,205,0,280,244,251,281,299],
[183,229,222,220,0,245,215,261,234],
[232,245,250,256,255,0,253,308,221],
[241,245,216,249,285,247,0,289,250],
[208,224,205,219,239,192,211,0,219],
[256,243,251,201,266,279,250,281,0]])



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
result = np.append(np.array([9, 500, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,235,242,231,226,237,252,224],
[273,0,247,268,245,251,249,266,236],
[265,253,0,252,256,243,232,239,239],
[258,232,248,0,250,251,255,245,239],
[269,255,244,250,0,270,257,262,239],
[274,249,257,249,230,0,244,263,239],
[263,251,268,245,243,256,0,265,255],
[248,234,261,255,238,237,235,0,233],
[276,264,261,261,261,261,245,267,0]])



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
result = np.append(np.array([9, 500, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,237,258,245,263,235,245,243],
[251,0,256,256,246,262,246,253,256],
[263,244,0,254,250,263,233,256,263],
[242,244,246,0,249,265,250,239,253],
[255,254,250,251,0,255,232,260,260],
[237,238,237,235,245,0,232,247,232],
[265,254,267,250,268,268,0,272,257],
[255,247,244,261,240,253,228,0,247],
[257,244,237,247,240,268,243,253,0]])



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
result = np.append(np.array([9, 500, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,283,262,239,240,256,276,286,232],
[217,0,224,243,240,244,216,253,237],
[238,276,0,256,235,261,225,280,261],
[261,257,244,0,257,261,240,279,236],
[260,260,265,243,0,262,243,288,253],
[244,256,239,239,238,0,213,273,208],
[224,284,275,260,257,287,0,305,273],
[214,247,220,221,212,227,195,0,234],
[268,263,239,264,247,292,227,266,0]])



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
result = np.append(np.array([9, 500, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,269,256,253,278,278,262,230],
[249,0,256,251,269,257,267,268,248],
[231,244,0,255,239,265,270,265,252],
[244,249,245,0,241,264,256,256,254],
[247,231,261,259,0,283,279,265,247],
[222,243,235,236,217,0,237,251,222],
[222,233,230,244,221,263,0,260,236],
[238,232,235,244,235,249,240,0,229],
[270,252,248,246,253,278,264,271,0]])



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
result = np.append(np.array([9, 500, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,267,244,258,255,244,256,242],
[241,0,258,252,258,254,247,262,241],
[233,242,0,238,243,240,233,251,246],
[256,248,262,0,257,252,255,278,252],
[242,242,257,243,0,233,242,253,229],
[245,246,260,248,267,0,247,246,245],
[256,253,267,245,258,253,0,260,242],
[244,238,249,222,247,254,240,0,235],
[258,259,254,248,271,255,258,265,0]])



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
result = np.append(np.array([9, 500, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,247,259,249,251,250,238,239],
[231,0,254,240,223,266,239,257,236],
[253,246,0,249,233,262,236,246,238],
[241,260,251,0,258,260,257,259,259],
[251,277,267,242,0,266,263,258,242],
[249,234,238,240,234,0,234,254,247],
[250,261,264,243,237,266,0,255,247],
[262,243,254,241,242,246,245,0,239],
[261,264,262,241,258,253,253,261,0]])



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
result = np.append(np.array([9, 500, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,256,259,243,255,248,273,250],
[256,0,259,242,257,257,256,289,273],
[244,241,0,249,245,254,256,239,240],
[241,258,251,0,262,250,236,266,256],
[257,243,255,238,0,271,271,293,264],
[245,243,246,250,229,0,247,261,237],
[252,244,244,264,229,253,0,263,226],
[227,211,261,234,207,239,237,0,220],
[250,227,260,244,236,263,274,280,0]])



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
result = np.append(np.array([9, 500, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,253,240,252,249,244,298,271],
[226,0,230,265,261,268,278,269,277],
[247,270,0,256,247,289,269,277,257],
[260,235,244,0,228,278,239,265,234],
[248,239,253,272,0,267,236,264,262],
[251,232,211,222,233,0,226,248,267],
[256,222,231,261,264,274,0,298,261],
[202,231,223,235,236,252,202,0,251],
[229,223,243,266,238,233,239,249,0]])



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
result = np.append(np.array([9, 500, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,252,273,242,234,272,233,248],
[239,0,247,258,234,261,260,248,255],
[248,253,0,283,273,249,271,267,288],
[227,242,217,0,227,245,252,232,222],
[258,266,227,273,0,261,255,236,273],
[266,239,251,255,239,0,277,234,268],
[228,240,229,248,245,223,0,246,248],
[267,252,233,268,264,266,254,0,285],
[252,245,212,278,227,232,252,215,0]])



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
result = np.append(np.array([9, 500, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,261,272,242,275,278,277,277],
[233,0,230,240,210,248,204,246,242],
[239,270,0,268,251,269,260,256,244],
[228,260,232,0,246,275,250,241,252],
[258,290,249,254,0,285,266,278,275],
[225,252,231,225,215,0,231,229,225],
[222,296,240,250,234,269,0,231,246],
[223,254,244,259,222,271,269,0,224],
[223,258,256,248,225,275,254,276,0]])



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
result = np.append(np.array([9, 500, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,246,215,237,198,256,241,283],
[269,0,254,237,269,256,263,249,276],
[254,246,0,249,258,226,251,259,264],
[285,263,251,0,263,263,245,242,295],
[263,231,242,237,0,243,216,252,277],
[302,244,274,237,257,0,273,275,294],
[244,237,249,255,284,227,0,255,271],
[259,251,241,258,248,225,245,0,263],
[217,224,236,205,223,206,229,237,0]])



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
result = np.append(np.array([9, 500, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,251,258,249,245,258,261,247],
[264,0,267,278,248,263,276,249,237],
[249,233,0,286,247,281,289,261,220],
[242,222,214,0,206,256,263,255,207],
[251,252,253,294,0,301,280,261,237],
[255,237,219,244,199,0,244,232,170],
[242,224,211,237,220,256,0,258,228],
[239,251,239,245,239,268,242,0,254],
[253,263,280,293,263,330,272,246,0]])



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
result = np.append(np.array([9, 500, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,220,230,237,227,219,239,213],
[259,0,241,224,246,232,246,247,223],
[280,259,0,249,275,251,241,290,241],
[270,276,251,0,251,246,268,269,220],
[263,254,225,249,0,237,244,249,247],
[273,268,249,254,263,0,272,248,261],
[281,254,259,232,256,228,0,285,222],
[261,253,210,231,251,252,215,0,197],
[287,277,259,280,253,239,278,303,0]])



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
result = np.append(np.array([9, 500, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,237,230,256,249,210,265,231],
[259,0,234,244,238,243,232,241,239],
[263,266,0,250,260,245,226,256,244],
[270,256,250,0,257,253,258,277,254],
[244,262,240,243,0,263,226,267,255],
[251,257,255,247,237,0,221,275,236],
[290,268,274,242,274,279,0,281,242],
[235,259,244,223,233,225,219,0,215],
[269,261,256,246,245,264,258,285,0]])



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
result = np.append(np.array([9, 500, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,230,239,251,232,248,236,268],
[264,0,252,250,255,243,263,248,261],
[270,248,0,231,249,230,273,248,269],
[261,250,269,0,252,250,274,253,291],
[249,245,251,248,0,258,259,241,269],
[268,257,270,250,242,0,264,261,286],
[252,237,227,226,241,236,0,239,271],
[264,252,252,247,259,239,261,0,273],
[232,239,231,209,231,214,229,227,0]])



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
result = np.append(np.array([9, 500, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,232,237,215,249,245,237,223],
[276,0,250,262,241,265,251,261,257],
[268,250,0,253,237,256,262,269,240],
[263,238,247,0,209,236,225,251,226],
[285,259,263,291,0,261,266,274,246],
[251,235,244,264,239,0,245,251,230],
[255,249,238,275,234,255,0,255,249],
[263,239,231,249,226,249,245,0,230],
[277,243,260,274,254,270,251,270,0]])



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
result = np.append(np.array([9, 500, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,238,262,249,212,232,233,245],
[224,0,237,229,230,198,225,230,254],
[262,263,0,265,282,215,253,262,278],
[238,271,235,0,272,213,241,239,256],
[251,270,218,228,0,214,247,238,281],
[288,302,285,287,286,0,239,261,302],
[268,275,247,259,253,261,0,260,259],
[267,270,238,261,262,239,240,0,265],
[255,246,222,244,219,198,241,235,0]])



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
result = np.append(np.array([9, 500, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,265,262,247,251,292,269,230],
[223,0,182,193,202,201,243,221,252],
[235,318,0,259,264,245,284,293,291],
[238,307,241,0,290,235,280,262,320],
[253,298,236,210,0,205,273,266,260],
[249,299,255,265,295,0,306,284,272],
[208,257,216,220,227,194,0,225,245],
[231,279,207,238,234,216,275,0,290],
[270,248,209,180,240,228,255,210,0]])



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
result = np.append(np.array([9, 500, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,257,231,263,258,252,260,226],
[233,0,259,245,231,265,232,238,220],
[243,241,0,232,248,253,224,252,213],
[269,255,268,0,252,258,234,252,243],
[237,269,252,248,0,257,254,243,253],
[242,235,247,242,243,0,226,234,222],
[248,268,276,266,246,274,0,266,228],
[240,262,248,248,257,266,234,0,223],
[274,280,287,257,247,278,272,277,0]])



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
result = np.append(np.array([9, 500, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,233,228,230,227,248,225,232],
[265,0,267,253,252,224,246,243,276],
[267,233,0,243,241,223,245,252,243],
[272,247,257,0,234,241,266,264,267],
[270,248,259,266,0,255,259,267,256],
[273,276,277,259,245,0,271,278,276],
[252,254,255,234,241,229,0,242,273],
[275,257,248,236,233,222,258,0,268],
[268,224,257,233,244,224,227,232,0]])



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
result = np.append(np.array([9, 500, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,263,263,275,257,257,223,241],
[243,0,263,268,264,253,264,247,250],
[237,237,0,275,268,254,260,244,259],
[237,232,225,0,238,222,233,224,227],
[225,236,232,262,0,246,249,226,231],
[243,247,246,278,254,0,262,254,257],
[243,236,240,267,251,238,0,225,241],
[277,253,256,276,274,246,275,0,243],
[259,250,241,273,269,243,259,257,0]])



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
result = np.append(np.array([9, 500, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,229,248,217,248,236,252,235],
[263,0,251,242,219,253,248,268,270],
[271,249,0,260,240,270,260,268,267],
[252,258,240,0,241,268,216,258,252],
[283,281,260,259,0,265,248,271,255],
[252,247,230,232,235,0,225,238,239],
[264,252,240,284,252,275,0,274,241],
[248,232,232,242,229,262,226,0,263],
[265,230,233,248,245,261,259,237,0]])



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
result = np.append(np.array([9, 500, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,236,218,254,244,225,222,226],
[274,0,248,255,277,268,270,265,253],
[264,252,0,249,273,274,246,255,234],
[282,245,251,0,280,275,270,265,257],
[246,223,227,220,0,249,238,233,222],
[256,232,226,225,251,0,248,241,229],
[275,230,254,230,262,252,0,241,239],
[278,235,245,235,267,259,259,0,248],
[274,247,266,243,278,271,261,252,0]])



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
result = np.append(np.array([9, 500, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,252,256,259,269,251,246,246],
[258,0,242,271,256,268,243,239,248],
[248,258,0,254,261,243,235,253,235],
[244,229,246,0,244,239,234,242,247],
[241,244,239,256,0,248,236,238,255],
[231,232,257,261,252,0,241,240,245],
[249,257,265,266,264,259,0,265,244],
[254,261,247,258,262,260,235,0,256],
[254,252,265,253,245,255,256,244,0]])



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
result = np.append(np.array([9, 500, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,291,261,268,274,258,272,247,292],
[209,0,241,258,238,240,265,256,268],
[239,259,0,245,254,243,250,249,264],
[232,242,255,0,259,232,279,224,264],
[226,262,246,241,0,249,267,250,271],
[242,260,257,268,251,0,267,254,256],
[228,235,250,221,233,233,0,253,241],
[253,244,251,276,250,246,247,0,237],
[208,232,236,236,229,244,259,263,0]])



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
result = np.append(np.array([9, 500, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,313,315,338,280,224,335,276],
[261,0,248,294,242,207,221,294,252],
[187,252,0,318,287,239,262,303,285],
[185,206,182,0,213,199,122,231,219],
[162,258,213,287,0,189,181,263,248],
[220,293,261,301,311,0,199,257,226],
[276,279,238,378,319,301,0,302,274],
[165,206,197,269,237,243,198,0,193],
[224,248,215,281,252,274,226,307,0]])



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
result = np.append(np.array([9, 500, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,240,241,253,273,244,268,256],
[240,0,253,225,255,240,266,276,243],
[260,247,0,255,247,221,247,261,250],
[259,275,245,0,299,270,247,296,255],
[247,245,253,201,0,253,254,281,215],
[227,260,279,230,247,0,240,299,239],
[256,234,253,253,246,260,0,251,230],
[232,224,239,204,219,201,249,0,185],
[244,257,250,245,285,261,270,315,0]])



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
result = np.append(np.array([9, 500, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,288,272,277,284,255,239,323,277],
[212,0,279,240,257,251,249,275,223],
[228,221,0,282,212,278,221,251,237],
[223,260,218,0,175,234,223,261,252],
[216,243,288,325,0,287,278,321,311],
[245,249,222,266,213,0,236,288,276],
[261,251,279,277,222,264,0,299,271],
[177,225,249,239,179,212,201,0,227],
[223,277,263,248,189,224,229,273,0]])



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
result = np.append(np.array([9, 500, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,243,245,237,209,237,251,239],
[267,0,259,264,243,253,251,253,267],
[257,241,0,263,253,247,239,266,263],
[255,236,237,0,243,248,242,275,260],
[263,257,247,257,0,222,226,267,243],
[291,247,253,252,278,0,254,268,276],
[263,249,261,258,274,246,0,267,253],
[249,247,234,225,233,232,233,0,242],
[261,233,237,240,257,224,247,258,0]])



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
result = np.append(np.array([9, 500, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,245,237,234,236,234,239,237],
[252,0,254,258,256,232,257,240,243],
[255,246,0,245,254,245,254,257,249],
[263,242,255,0,261,257,242,264,267],
[266,244,246,239,0,229,247,244,236],
[264,268,255,243,271,0,249,260,259],
[266,243,246,258,253,251,0,245,252],
[261,260,243,236,256,240,255,0,245],
[263,257,251,233,264,241,248,255,0]])



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
result = np.append(np.array([9, 500, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,238,252,235,236,264,229,238],
[249,0,228,245,222,220,248,227,215],
[262,272,0,261,275,244,281,269,248],
[248,255,239,0,231,244,274,239,257],
[265,278,225,269,0,260,274,248,249],
[264,280,256,256,240,0,273,235,247],
[236,252,219,226,226,227,0,219,213],
[271,273,231,261,252,265,281,0,255],
[262,285,252,243,251,253,287,245,0]])



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
result = np.append(np.array([9, 500, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,261,251,253,260,253,268,252],
[260,0,265,259,243,271,259,264,247],
[239,235,0,239,238,247,265,257,242],
[249,241,261,0,247,239,246,273,239],
[247,257,262,253,0,256,239,262,234],
[240,229,253,261,244,0,249,262,226],
[247,241,235,254,261,251,0,260,243],
[232,236,243,227,238,238,240,0,240],
[248,253,258,261,266,274,257,260,0]])



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
result = np.append(np.array([9, 500, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,224,261,253,283,232,263,264],
[244,0,264,254,249,272,271,279,246],
[276,236,0,264,227,249,237,260,247],
[239,246,236,0,246,260,229,264,237],
[247,251,273,254,0,250,239,286,277],
[217,228,251,240,250,0,222,249,255],
[268,229,263,271,261,278,0,291,269],
[237,221,240,236,214,251,209,0,255],
[236,254,253,263,223,245,231,245,0]])



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
result = np.append(np.array([9, 500, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,243,229,232,265,234,244,221],
[260,0,217,247,266,235,222,225,224],
[257,283,0,260,289,288,266,262,247],
[271,253,240,0,242,255,257,254,272],
[268,234,211,258,0,218,259,261,232],
[235,265,212,245,282,0,237,238,212],
[266,278,234,243,241,263,0,257,220],
[256,275,238,246,239,262,243,0,238],
[279,276,253,228,268,288,280,262,0]])



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
result = np.append(np.array([9, 500, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,278,267,266,264,256,248,275],
[255,0,269,263,250,270,247,253,261],
[222,231,0,227,239,248,234,243,246],
[233,237,273,0,246,257,235,250,249],
[234,250,261,254,0,253,238,237,263],
[236,230,252,243,247,0,233,255,251],
[244,253,266,265,262,267,0,263,270],
[252,247,257,250,263,245,237,0,255],
[225,239,254,251,237,249,230,245,0]])



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
result = np.append(np.array([9, 500, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,228,229,252,213,246,216,241],
[282,0,246,273,285,254,281,261,241],
[272,254,0,253,269,260,271,236,257],
[271,227,247,0,254,238,272,260,249],
[248,215,231,246,0,215,241,219,246],
[287,246,240,262,285,0,283,258,267],
[254,219,229,228,259,217,0,225,222],
[284,239,264,240,281,242,275,0,256],
[259,259,243,251,254,233,278,244,0]])



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
result = np.append(np.array([9, 500, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,307,305,319,244,228,236,243,286],
[193,0,268,218,224,221,229,247,211],
[195,232,0,235,178,226,210,242,191],
[181,282,265,0,218,188,251,236,246],
[256,276,322,282,0,237,273,279,261],
[272,279,274,312,263,0,267,254,238],
[264,271,290,249,227,233,0,299,256],
[257,253,258,264,221,246,201,0,253],
[214,289,309,254,239,262,244,247,0]])



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
result = np.append(np.array([9, 500, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,254,238,255,270,247,252,272],
[239,0,267,223,252,247,261,237,271],
[246,233,0,226,246,243,256,242,246],
[262,277,274,0,260,259,271,274,248],
[245,248,254,240,0,259,264,249,260],
[230,253,257,241,241,0,250,250,249],
[253,239,244,229,236,250,0,243,262],
[248,263,258,226,251,250,257,0,258],
[228,229,254,252,240,251,238,242,0]])



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
result = np.append(np.array([9, 500, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,267,233,243,235,252,254,252],
[252,0,261,251,254,249,257,249,268],
[233,239,0,238,254,237,232,236,252],
[267,249,262,0,266,246,260,241,277],
[257,246,246,234,0,249,252,236,254],
[265,251,263,254,251,0,267,240,266],
[248,243,268,240,248,233,0,241,257],
[246,251,264,259,264,260,259,0,273],
[248,232,248,223,246,234,243,227,0]])



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
result = np.append(np.array([9, 500, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,211,217,226,203,240,236,219],
[256,0,255,254,239,259,243,267,264],
[289,245,0,211,230,263,235,235,250],
[283,246,289,0,256,244,274,263,280],
[274,261,270,244,0,260,237,235,272],
[297,241,237,256,240,0,241,246,225],
[260,257,265,226,263,259,0,255,234],
[264,233,265,237,265,254,245,0,242],
[281,236,250,220,228,275,266,258,0]])



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
result = np.append(np.array([9, 500, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,183,196,219,189,104,196,191],
[276,0,370,234,304,351,200,228,274],
[317,130,0,243,399,338,317,197,337],
[304,266,257,0,257,267,248,315,248],
[281,196,101,243,0,215,69,101,253],
[311,149,162,233,285,0,186,169,378],
[396,300,183,252,431,314,0,208,293],
[304,272,303,185,399,331,292,0,343],
[309,226,163,252,247,122,207,157,0]])



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
result = np.append(np.array([9, 500, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,324,311,191,210,290,260,197,273],
[176,0,225,191,197,192,205,164,258],
[189,275,0,136,211,288,244,223,217],
[309,309,364,0,243,307,279,273,328],
[290,303,289,257,0,231,225,214,273],
[210,308,212,193,269,0,274,223,292],
[240,295,256,221,275,226,0,243,261],
[303,336,277,227,286,277,257,0,307],
[227,242,283,172,227,208,239,193,0]])



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
result = np.append(np.array([9, 500, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,236,264,278,237,275,259,254],
[252,0,246,267,244,263,254,261,274],
[264,254,0,279,243,241,262,261,241],
[236,233,221,0,237,221,234,247,236],
[222,256,257,263,0,248,259,232,240],
[263,237,259,279,252,0,263,240,247],
[225,246,238,266,241,237,0,242,231],
[241,239,239,253,268,260,258,0,267],
[246,226,259,264,260,253,269,233,0]])



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
result = np.append(np.array([9, 500, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,231,224,199,211,226,213,235],
[280,0,241,241,251,222,254,293,219],
[269,259,0,261,236,225,228,270,251],
[276,259,239,0,223,225,227,279,233],
[301,249,264,277,0,228,259,280,244],
[289,278,275,275,272,0,274,281,247],
[274,246,272,273,241,226,0,276,229],
[287,207,230,221,220,219,224,0,215],
[265,281,249,267,256,253,271,285,0]])



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
result = np.append(np.array([9, 500, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,238,242,237,245,242,232,237],
[266,0,248,254,247,252,252,246,250],
[262,252,0,259,244,248,257,249,263],
[258,246,241,0,251,240,248,252,260],
[263,253,256,249,0,252,269,265,263],
[255,248,252,260,248,0,270,251,253],
[258,248,243,252,231,230,0,245,243],
[268,254,251,248,235,249,255,0,254],
[263,250,237,240,237,247,257,246,0]])



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
result = np.append(np.array([9, 500, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,256,238,243,226,234,239,270],
[247,0,269,266,230,253,217,248,263],
[244,231,0,244,239,235,207,225,257],
[262,234,256,0,244,255,243,230,250],
[257,270,261,256,0,267,237,265,282],
[274,247,265,245,233,0,251,213,271],
[266,283,293,257,263,249,0,259,277],
[261,252,275,270,235,287,241,0,281],
[230,237,243,250,218,229,223,219,0]])



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
result = np.append(np.array([9, 500, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,266,252,243,260,257,251,270],
[255,0,262,260,252,250,258,269,267],
[234,238,0,215,225,235,234,236,251],
[248,240,285,0,253,262,245,277,243],
[257,248,275,247,0,249,247,268,254],
[240,250,265,238,251,0,256,253,239],
[243,242,266,255,253,244,0,256,243],
[249,231,264,223,232,247,244,0,265],
[230,233,249,257,246,261,257,235,0]])



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
result = np.append(np.array([9, 500, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,255,245,239,220,250,241,254],
[284,0,270,279,255,259,256,249,265],
[245,230,0,259,242,216,222,237,258],
[255,221,241,0,228,238,236,233,228],
[261,245,258,272,0,231,270,245,264],
[280,241,284,262,269,0,253,261,265],
[250,244,278,264,230,247,0,236,277],
[259,251,263,267,255,239,264,0,264],
[246,235,242,272,236,235,223,236,0]])



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
result = np.append(np.array([9, 500, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,224,238,260,277,241,254,254],
[268,0,248,270,249,262,250,254,219],
[276,252,0,278,278,303,255,291,234],
[262,230,222,0,260,276,244,258,239],
[240,251,222,240,0,278,251,270,229],
[223,238,197,224,222,0,235,248,203],
[259,250,245,256,249,265,0,264,228],
[246,246,209,242,230,252,236,0,203],
[246,281,266,261,271,297,272,297,0]])



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
result = np.append(np.array([9, 500, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,221,235,272,243,244,251,252],
[249,0,243,232,279,239,239,280,210],
[279,257,0,249,284,253,249,285,240],
[265,268,251,0,286,245,239,261,262],
[228,221,216,214,0,221,202,237,227],
[257,261,247,255,279,0,266,261,227],
[256,261,251,261,298,234,0,265,231],
[249,220,215,239,263,239,235,0,221],
[248,290,260,238,273,273,269,279,0]])



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
result = np.append(np.array([9, 500, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,254,256,280,266,252,241,231],
[277,0,248,251,261,262,266,250,248],
[246,252,0,243,244,266,262,249,247],
[244,249,257,0,273,250,258,250,244],
[220,239,256,227,0,253,253,255,240],
[234,238,234,250,247,0,259,256,275],
[248,234,238,242,247,241,0,230,232],
[259,250,251,250,245,244,270,0,234],
[269,252,253,256,260,225,268,266,0]])



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
result = np.append(np.array([9, 500, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,241,268,239,232,270,257,219],
[264,0,251,265,249,258,256,267,240],
[259,249,0,229,251,215,279,246,251],
[232,235,271,0,247,247,285,269,233],
[261,251,249,253,0,238,283,268,255],
[268,242,285,253,262,0,306,249,233],
[230,244,221,215,217,194,0,256,226],
[243,233,254,231,232,251,244,0,244],
[281,260,249,267,245,267,274,256,0]])



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
result = np.append(np.array([9, 500, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,282,234,229,250,238,266,265],
[220,0,240,242,239,220,235,239,250],
[218,260,0,214,231,224,219,213,271],
[266,258,286,0,240,258,251,248,292],
[271,261,269,260,0,244,226,247,283],
[250,280,276,242,256,0,242,231,283],
[262,265,281,249,274,258,0,231,258],
[234,261,287,252,253,269,269,0,261],
[235,250,229,208,217,217,242,239,0]])



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
result = np.append(np.array([9, 500, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,255,276,258,254,256,247,261],
[240,0,250,254,230,246,243,238,244],
[245,250,0,265,242,265,254,252,261],
[224,246,235,0,224,228,242,244,239],
[242,270,258,276,0,252,261,265,256],
[246,254,235,272,248,0,241,248,252],
[244,257,246,258,239,259,0,256,241],
[253,262,248,256,235,252,244,0,268],
[239,256,239,261,244,248,259,232,0]])



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
result = np.append(np.array([9, 500, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,268,272,245,257,233,245,247],
[257,0,279,260,249,269,252,256,262],
[232,221,0,252,239,244,231,251,252],
[228,240,248,0,235,245,255,253,237],
[255,251,261,265,0,236,251,261,256],
[243,231,256,255,264,0,248,248,252],
[267,248,269,245,249,252,0,268,257],
[255,244,249,247,239,252,232,0,264],
[253,238,248,263,244,248,243,236,0]])



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
result = np.append(np.array([9, 500, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,259,249,255,259,243,236,240],
[252,0,257,258,262,254,264,252,243],
[241,243,0,249,255,253,245,226,224],
[251,242,251,0,274,265,257,235,247],
[245,238,245,226,0,241,248,208,229],
[241,246,247,235,259,0,247,249,224],
[257,236,255,243,252,253,0,223,230],
[264,248,274,265,292,251,277,0,257],
[260,257,276,253,271,276,270,243,0]])



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
result = np.append(np.array([9, 500, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,251,255,260,246,251,251,256],
[233,0,254,237,248,237,229,231,256],
[249,246,0,245,259,236,251,249,261],
[245,263,255,0,269,251,250,232,261],
[240,252,241,231,0,236,238,233,259],
[254,263,264,249,264,0,275,251,273],
[249,271,249,250,262,225,0,235,261],
[249,269,251,268,267,249,265,0,263],
[244,244,239,239,241,227,239,237,0]])



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
result = np.append(np.array([9, 500, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,256,249,274,274,260,272,275],
[229,0,260,245,275,275,276,284,256],
[244,240,0,245,256,249,263,261,242],
[251,255,255,0,256,275,244,270,232],
[226,225,244,244,0,247,243,240,211],
[226,225,251,225,253,0,254,267,241],
[240,224,237,256,257,246,0,265,238],
[228,216,239,230,260,233,235,0,234],
[225,244,258,268,289,259,262,266,0]])



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
result = np.append(np.array([9, 500, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,286,215,286,269,251,202,279],
[269,0,261,250,342,254,281,224,284],
[214,239,0,224,287,223,247,224,229],
[285,250,276,0,326,288,301,264,331],
[214,158,213,174,0,214,214,199,236],
[231,246,277,212,286,0,297,218,275],
[249,219,253,199,286,203,0,203,232],
[298,276,276,236,301,282,297,0,321],
[221,216,271,169,264,225,268,179,0]])



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
result = np.append(np.array([9, 500, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,267,248,259,284,287,222,255],
[232,0,253,245,254,274,259,254,244],
[233,247,0,241,215,284,269,231,224],
[252,255,259,0,232,262,276,236,242],
[241,246,285,268,0,273,297,248,239],
[216,226,216,238,227,0,258,226,220],
[213,241,231,224,203,242,0,235,245],
[278,246,269,264,252,274,265,0,256],
[245,256,276,258,261,280,255,244,0]])



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
result = np.append(np.array([9, 500, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,266,244,230,235,245,232,238],
[245,0,337,305,230,279,210,270,266],
[234,163,0,225,226,194,214,195,241],
[256,195,275,0,280,223,231,204,202],
[270,270,274,220,0,204,242,255,229],
[265,221,306,277,296,0,262,264,264],
[255,290,286,269,258,238,0,279,248],
[268,230,305,296,245,236,221,0,245],
[262,234,259,298,271,236,252,255,0]])



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
result = np.append(np.array([9, 500, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,256,254,254,237,244,233,251],
[271,0,248,268,275,256,246,260,257],
[244,252,0,271,265,255,241,253,263],
[246,232,229,0,244,233,238,257,235],
[246,225,235,256,0,234,246,240,262],
[263,244,245,267,266,0,251,234,267],
[256,254,259,262,254,249,0,248,265],
[267,240,247,243,260,266,252,0,257],
[249,243,237,265,238,233,235,243,0]])



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
result = np.append(np.array([9, 500, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,243,256,240,255,274,245,241],
[226,0,225,228,225,245,258,233,224],
[257,275,0,254,250,262,258,226,250],
[244,272,246,0,257,274,257,235,233],
[260,275,250,243,0,255,280,257,259],
[245,255,238,226,245,0,244,235,240],
[226,242,242,243,220,256,0,243,218],
[255,267,274,265,243,265,257,0,244],
[259,276,250,267,241,260,282,256,0]])



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
result = np.append(np.array([9, 500, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,245,265,248,262,243,260,259],
[255,0,250,261,250,271,250,265,270],
[255,250,0,264,239,259,249,250,251],
[235,239,236,0,244,249,240,243,243],
[252,250,261,256,0,265,249,247,242],
[238,229,241,251,235,0,250,245,228],
[257,250,251,260,251,250,0,236,251],
[240,235,250,257,253,255,264,0,244],
[241,230,249,257,258,272,249,256,0]])



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
result = np.append(np.array([9, 500, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,230,276,217,240,241,226,235],
[254,0,215,243,256,236,217,242,264],
[270,285,0,267,257,268,247,274,272],
[224,257,233,0,253,257,238,235,245],
[283,244,243,247,0,274,254,239,247],
[260,264,232,243,226,0,265,219,261],
[259,283,253,262,246,235,0,250,274],
[274,258,226,265,261,281,250,0,254],
[265,236,228,255,253,239,226,246,0]])



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
result = np.append(np.array([9, 500, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,232,237,257,242,259,254,238],
[253,0,252,259,263,247,263,263,260],
[268,248,0,262,261,255,257,249,265],
[263,241,238,0,270,269,245,259,259],
[243,237,239,230,0,233,244,243,252],
[258,253,245,231,267,0,262,265,258],
[241,237,243,255,256,238,0,256,247],
[246,237,251,241,257,235,244,0,238],
[262,240,235,241,248,242,253,262,0]])



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
result = np.append(np.array([9, 500, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,250,245,225,237,266,256,239],
[250,0,243,230,221,249,265,251,234],
[250,257,0,263,263,256,306,251,226],
[255,270,237,0,248,256,254,274,234],
[275,279,237,252,0,262,279,279,254],
[263,251,244,244,238,0,266,258,231],
[234,235,194,246,221,234,0,241,200],
[244,249,249,226,221,242,259,0,215],
[261,266,274,266,246,269,300,285,0]])



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
result = np.append(np.array([9, 500, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,246,254,247,267,261,267,257],
[252,0,258,227,237,252,222,236,249],
[254,242,0,241,257,261,243,259,256],
[246,273,259,0,239,279,258,259,260],
[253,263,243,261,0,268,248,260,256],
[233,248,239,221,232,0,220,235,239],
[239,278,257,242,252,280,0,264,257],
[233,264,241,241,240,265,236,0,249],
[243,251,244,240,244,261,243,251,0]])



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
result = np.append(np.array([9, 500, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,208,376,192,165,146,173,164,128],
[292,0,284,46,54,116,140,35,107],
[124,216,0,129,30,154,83,53,83],
[308,454,371,0,285,189,291,221,208],
[335,446,470,215,0,333,316,275,150],
[354,384,346,311,167,0,149,159,184],
[327,360,417,209,184,351,0,268,111],
[336,465,447,279,225,341,232,0,295],
[372,393,417,292,350,316,389,205,0]])



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
result = np.append(np.array([9, 500, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,253,258,252,249,281,251,261],
[239,0,256,264,250,238,261,258,249],
[247,244,0,258,249,232,234,235,247],
[242,236,242,0,248,238,254,255,242],
[248,250,251,252,0,240,235,243,243],
[251,262,268,262,260,0,248,245,255],
[219,239,266,246,265,252,0,245,267],
[249,242,265,245,257,255,255,0,252],
[239,251,253,258,257,245,233,248,0]])



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
result = np.append(np.array([9, 500, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,262,252,253,237,279,275,278],
[236,0,260,252,247,258,255,255,257],
[238,240,0,233,244,243,261,242,244],
[248,248,267,0,254,257,261,251,243],
[247,253,256,246,0,242,255,260,261],
[263,242,257,243,258,0,256,254,250],
[221,245,239,239,245,244,0,247,255],
[225,245,258,249,240,246,253,0,232],
[222,243,256,257,239,250,245,268,0]])



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
result = np.append(np.array([9, 500, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,244,256,239,245,256,235,250],
[241,0,252,245,237,243,236,228,237],
[256,248,0,238,231,252,246,251,241],
[244,255,262,0,231,250,250,243,233],
[261,263,269,269,0,260,266,251,240],
[255,257,248,250,240,0,243,229,248],
[244,264,254,250,234,257,0,248,239],
[265,272,249,257,249,271,252,0,261],
[250,263,259,267,260,252,261,239,0]])



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
result = np.append(np.array([9, 500, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,265,243,259,244,252,272,259],
[262,0,250,245,263,252,263,263,262],
[235,250,0,246,255,243,260,265,250],
[257,255,254,0,265,242,270,261,257],
[241,237,245,235,0,236,260,258,246],
[256,248,257,258,264,0,279,278,276],
[248,237,240,230,240,221,0,261,249],
[228,237,235,239,242,222,239,0,244],
[241,238,250,243,254,224,251,256,0]])



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
result = np.append(np.array([9, 500, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,252,242,275,238,252,263,258],
[250,0,247,269,262,273,252,286,248],
[248,253,0,259,234,256,237,255,257],
[258,231,241,0,254,273,235,265,263],
[225,238,266,246,0,250,244,269,253],
[262,227,244,227,250,0,250,260,255],
[248,248,263,265,256,250,0,260,283],
[237,214,245,235,231,240,240,0,227],
[242,252,243,237,247,245,217,273,0]])



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
result = np.append(np.array([9, 500, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,254,250,249,236,253,251,251],
[255,0,259,247,257,256,261,270,243],
[246,241,0,233,248,241,247,246,230],
[250,253,267,0,252,261,254,280,247],
[251,243,252,248,0,248,255,248,239],
[264,244,259,239,252,0,246,251,247],
[247,239,253,246,245,254,0,250,242],
[249,230,254,220,252,249,250,0,236],
[249,257,270,253,261,253,258,264,0]])



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
result = np.append(np.array([9, 500, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,259,249,249,267,260,268,268],
[234,0,239,258,237,262,254,264,258],
[241,261,0,254,252,257,263,248,279],
[251,242,246,0,240,256,229,257,261],
[251,263,248,260,0,260,267,258,257],
[233,238,243,244,240,0,242,257,248],
[240,246,237,271,233,258,0,263,261],
[232,236,252,243,242,243,237,0,253],
[232,242,221,239,243,252,239,247,0]])



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
result = np.append(np.array([9, 500, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,225,256,251,237,248,277,286],
[267,0,247,226,256,243,253,274,266],
[275,253,0,272,235,247,282,277,263],
[244,274,228,0,265,263,272,266,271],
[249,244,265,235,0,240,290,294,315],
[263,257,253,237,260,0,280,265,262],
[252,247,218,228,210,220,0,239,233],
[223,226,223,234,206,235,261,0,287],
[214,234,237,229,185,238,267,213,0]])



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
result = np.append(np.array([9, 500, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,258,281,235,352,288,269,270],
[275,0,195,247,270,274,282,239,281],
[242,305,0,313,280,320,347,262,263],
[219,253,187,0,222,257,311,228,216],
[265,230,220,278,0,246,287,260,246],
[148,226,180,243,254,0,272,216,204],
[212,218,153,189,213,228,0,210,200],
[231,261,238,272,240,284,290,0,204],
[230,219,237,284,254,296,300,296,0]])



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
result = np.append(np.array([9, 500, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,229,244,239,252,239,257,255],
[240,0,232,241,252,227,249,250,245],
[271,268,0,256,236,271,252,268,254],
[256,259,244,0,252,260,247,262,262],
[261,248,264,248,0,250,248,257,260],
[248,273,229,240,250,0,242,254,245],
[261,251,248,253,252,258,0,255,258],
[243,250,232,238,243,246,245,0,271],
[245,255,246,238,240,255,242,229,0]])



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
result = np.append(np.array([9, 500, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,297,276,260,294,241,260,265,269],
[203,0,204,238,213,189,217,254,232],
[224,296,0,236,264,253,265,240,280],
[240,262,264,0,255,241,200,260,267],
[206,287,236,245,0,237,254,250,281],
[259,311,247,259,263,0,251,273,291],
[240,283,235,300,246,249,0,274,258],
[235,246,260,240,250,227,226,0,259],
[231,268,220,233,219,209,242,241,0]])



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
result = np.append(np.array([9, 500, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,211,226,241,254,219,233,258],
[236,0,204,240,238,257,231,237,234],
[289,296,0,263,257,275,261,247,284],
[274,260,237,0,254,279,246,255,275],
[259,262,243,246,0,257,231,231,228],
[246,243,225,221,243,0,237,225,255],
[281,269,239,254,269,263,0,246,243],
[267,263,253,245,269,275,254,0,273],
[242,266,216,225,272,245,257,227,0]])



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
result = np.append(np.array([9, 500, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,253,264,239,238,251,255,255],
[252,0,259,264,237,247,247,267,275],
[247,241,0,267,233,246,257,249,258],
[236,236,233,0,238,235,229,229,239],
[261,263,267,262,0,260,270,248,266],
[262,253,254,265,240,0,246,242,272],
[249,253,243,271,230,254,0,242,255],
[245,233,251,271,252,258,258,0,270],
[245,225,242,261,234,228,245,230,0]])



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
result = np.append(np.array([9, 500, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,236,278,249,249,254,266,238],
[267,0,243,281,263,264,269,272,260],
[264,257,0,274,243,263,268,276,267],
[222,219,226,0,244,239,240,251,249],
[251,237,257,256,0,259,263,260,256],
[251,236,237,261,241,0,261,260,255],
[246,231,232,260,237,239,0,259,249],
[234,228,224,249,240,240,241,0,246],
[262,240,233,251,244,245,251,254,0]])



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
result = np.append(np.array([9, 500, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,259,246,242,253,246,245,248],
[239,0,251,244,234,240,253,248,234],
[241,249,0,241,241,235,247,243,213],
[254,256,259,0,241,234,241,234,223],
[258,266,259,259,0,242,252,256,244],
[247,260,265,266,258,0,258,252,252],
[254,247,253,259,248,242,0,243,240],
[255,252,257,266,244,248,257,0,255],
[252,266,287,277,256,248,260,245,0]])



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
result = np.append(np.array([9, 500, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,250,234,241,247,227,243,261],
[257,0,254,243,255,244,246,245,267],
[250,246,0,235,299,251,280,241,269],
[266,257,265,0,258,253,279,247,265],
[259,245,201,242,0,206,280,226,253],
[253,256,249,247,294,0,271,253,276],
[273,254,220,221,220,229,0,236,244],
[257,255,259,253,274,247,264,0,266],
[239,233,231,235,247,224,256,234,0]])



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
result = np.append(np.array([9, 500, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,285,237,251,295,280,285,305,264],
[215,0,177,200,225,169,212,221,283],
[263,323,0,270,250,234,278,260,313],
[249,300,230,0,280,219,282,325,328],
[205,275,250,220,0,217,253,245,318],
[220,331,266,281,283,0,247,309,334],
[215,288,222,218,247,253,0,257,235],
[195,279,240,175,255,191,243,0,281],
[236,217,187,172,182,166,265,219,0]])



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
result = np.append(np.array([9, 500, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,234,252,259,237,253,247,262],
[238,0,257,259,247,247,258,244,263],
[266,243,0,260,256,256,253,237,256],
[248,241,240,0,261,247,245,241,244],
[241,253,244,239,0,239,249,233,244],
[263,253,244,253,261,0,251,257,259],
[247,242,247,255,251,249,0,231,262],
[253,256,263,259,267,243,269,0,261],
[238,237,244,256,256,241,238,239,0]])



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
result = np.append(np.array([9, 500, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,271,247,216,240,235,245,262],
[251,0,296,261,254,246,252,248,276],
[229,204,0,229,210,244,217,218,236],
[253,239,271,0,250,232,229,230,265],
[284,246,290,250,0,237,248,269,268],
[260,254,256,268,263,0,250,272,280],
[265,248,283,271,252,250,0,258,263],
[255,252,282,270,231,228,242,0,267],
[238,224,264,235,232,220,237,233,0]])



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
result = np.append(np.array([9, 500, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,279,254,235,270,273,253,248],
[262,0,279,255,239,261,253,256,256],
[221,221,0,233,233,253,269,236,217],
[246,245,267,0,245,268,269,276,227],
[265,261,267,255,0,254,257,259,241],
[230,239,247,232,246,0,263,239,248],
[227,247,231,231,243,237,0,257,230],
[247,244,264,224,241,261,243,0,224],
[252,244,283,273,259,252,270,276,0]])



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
result = np.append(np.array([9, 500, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,288,295,308,344,262,284,247,277],
[212,0,242,191,287,168,237,205,172],
[205,258,0,244,291,265,264,251,263],
[192,309,256,0,281,217,257,184,248],
[156,213,209,219,0,174,222,179,194],
[238,332,235,283,326,0,329,227,266],
[216,263,236,243,278,171,0,182,240],
[253,295,249,316,321,273,318,0,252],
[223,328,237,252,306,234,260,248,0]])



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
result = np.append(np.array([9, 500, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,289,241,266,305,253,290,243],
[233,0,272,219,257,273,255,292,263],
[211,228,0,200,248,276,227,292,243],
[259,281,300,0,308,282,239,279,247],
[234,243,252,192,0,260,206,255,228],
[195,227,224,218,240,0,241,245,209],
[247,245,273,261,294,259,0,265,246],
[210,208,208,221,245,255,235,0,216],
[257,237,257,253,272,291,254,284,0]])



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
result = np.append(np.array([9, 500, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,226,225,232,238,216,220,255],
[284,0,261,274,257,255,215,249,264],
[274,239,0,257,268,268,263,246,266],
[275,226,243,0,232,251,216,243,262],
[268,243,232,268,0,259,252,243,269],
[262,245,232,249,241,0,229,260,270],
[284,285,237,284,248,271,0,264,266],
[280,251,254,257,257,240,236,0,263],
[245,236,234,238,231,230,234,237,0]])



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
result = np.append(np.array([9, 500, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,254,240,248,249,259,230,268],
[256,0,262,238,249,252,257,248,264],
[246,238,0,233,267,232,254,226,254],
[260,262,267,0,257,245,259,259,262],
[252,251,233,243,0,248,230,241,248],
[251,248,268,255,252,0,246,238,265],
[241,243,246,241,270,254,0,231,262],
[270,252,274,241,259,262,269,0,262],
[232,236,246,238,252,235,238,238,0]])



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
result = np.append(np.array([9, 500, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,245,248,223,246,253,254,229],
[252,0,228,236,216,237,231,210,222],
[255,272,0,250,234,257,229,219,247],
[252,264,250,0,211,228,247,211,253],
[277,284,266,289,0,293,260,237,280],
[254,263,243,272,207,0,234,235,232],
[247,269,271,253,240,266,0,228,243],
[246,290,281,289,263,265,272,0,271],
[271,278,253,247,220,268,257,229,0]])



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
result = np.append(np.array([9, 500, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,259,242,259,262,272,265,254],
[249,0,231,219,269,254,270,268,222],
[241,269,0,247,258,268,281,263,229],
[258,281,253,0,272,264,290,297,241],
[241,231,242,228,0,251,269,271,250],
[238,246,232,236,249,0,283,266,230],
[228,230,219,210,231,217,0,242,231],
[235,232,237,203,229,234,258,0,227],
[246,278,271,259,250,270,269,273,0]])



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
result = np.append(np.array([9, 500, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,230,248,225,245,228,211,258],
[256,0,255,248,233,256,243,243,257],
[270,245,0,249,253,270,255,256,285],
[252,252,251,0,259,262,247,242,264],
[275,267,247,241,0,259,252,247,273],
[255,244,230,238,241,0,228,240,252],
[272,257,245,253,248,272,0,251,292],
[289,257,244,258,253,260,249,0,259],
[242,243,215,236,227,248,208,241,0]])



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
result = np.append(np.array([9, 500, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,263,261,244,254,236,260,241],
[260,0,242,259,227,230,217,236,252],
[237,258,0,254,236,251,233,237,210],
[239,241,246,0,219,227,199,232,235],
[256,273,264,281,0,281,246,258,235],
[246,270,249,273,219,0,216,247,261],
[264,283,267,301,254,284,0,263,245],
[240,264,263,268,242,253,237,0,256],
[259,248,290,265,265,239,255,244,0]])



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
result = np.append(np.array([9, 500, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,234,255,248,239,244,252,260],
[251,0,232,268,257,259,244,264,259],
[266,268,0,272,277,246,264,260,261],
[245,232,228,0,241,242,248,259,254],
[252,243,223,259,0,238,253,252,241],
[261,241,254,258,262,0,271,268,264],
[256,256,236,252,247,229,0,271,258],
[248,236,240,241,248,232,229,0,241],
[240,241,239,246,259,236,242,259,0]])



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
result = np.append(np.array([9, 500, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,273,251,258,265,272,270,246],
[244,0,256,244,234,247,249,253,226],
[227,244,0,230,235,239,241,240,222],
[249,256,270,0,244,245,242,253,246],
[242,266,265,256,0,271,253,258,232],
[235,253,261,255,229,0,249,257,250],
[228,251,259,258,247,251,0,274,245],
[230,247,260,247,242,243,226,0,224],
[254,274,278,254,268,250,255,276,0]])



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
result = np.append(np.array([9, 500, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,233,246,246,244,263,242,254],
[258,0,263,254,262,247,262,250,260],
[267,237,0,243,254,241,252,257,266],
[254,246,257,0,259,240,271,274,263],
[254,238,246,241,0,251,254,259,257],
[256,253,259,260,249,0,269,266,259],
[237,238,248,229,246,231,0,255,260],
[258,250,243,226,241,234,245,0,248],
[246,240,234,237,243,241,240,252,0]])



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
result = np.append(np.array([9, 500, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,199,213,242,218,257,253,306],
[277,0,240,201,232,206,229,232,273],
[301,260,0,258,251,278,254,234,317],
[287,299,242,0,296,295,255,264,320],
[258,268,249,204,0,228,212,240,298],
[282,294,222,205,272,0,251,262,311],
[243,271,246,245,288,249,0,250,285],
[247,268,266,236,260,238,250,0,307],
[194,227,183,180,202,189,215,193,0]])



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
result = np.append(np.array([9, 500, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,204,242,259,214,201,221,251,236],
[296,0,252,240,224,234,254,244,267],
[258,248,0,283,256,186,248,235,228],
[241,260,217,0,233,208,247,249,245],
[286,276,244,267,0,292,261,270,257],
[299,266,314,292,208,0,281,248,286],
[279,246,252,253,239,219,0,243,252],
[249,256,265,251,230,252,257,0,239],
[264,233,272,255,243,214,248,261,0]])



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
result = np.append(np.array([9, 500, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,233,247,241,246,251,238,249],
[244,0,242,234,243,244,266,240,256],
[267,258,0,260,249,257,253,250,249],
[253,266,240,0,250,264,262,243,259],
[259,257,251,250,0,248,255,247,234],
[254,256,243,236,252,0,251,240,264],
[249,234,247,238,245,249,0,231,241],
[262,260,250,257,253,260,269,0,259],
[251,244,251,241,266,236,259,241,0]])



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
result = np.append(np.array([9, 500, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,218,261,252,228,220,220,281],
[267,0,270,287,270,250,254,287,269],
[282,230,0,266,245,218,272,231,260],
[239,213,234,0,244,227,244,235,265],
[248,230,255,256,0,223,255,248,262],
[272,250,282,273,277,0,273,274,284],
[280,246,228,256,245,227,0,227,275],
[280,213,269,265,252,226,273,0,253],
[219,231,240,235,238,216,225,247,0]])



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
result = np.append(np.array([9, 500, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,262,239,234,245,250,256,255],
[278,0,268,253,262,240,284,279,244],
[238,232,0,268,248,232,242,216,243],
[261,247,232,0,266,245,252,253,256],
[266,238,252,234,0,235,248,223,275],
[255,260,268,255,265,0,260,271,244],
[250,216,258,248,252,240,0,236,244],
[244,221,284,247,277,229,264,0,271],
[245,256,257,244,225,256,256,229,0]])



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
result = np.append(np.array([9, 500, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,276,269,297,250,275,261,245],
[236,0,272,281,281,244,228,238,251],
[224,228,0,248,236,217,221,208,217],
[231,219,252,0,231,236,220,230,220],
[203,219,264,269,0,217,220,206,238],
[250,256,283,264,283,0,246,256,251],
[225,272,279,280,280,254,0,258,240],
[239,262,292,270,294,244,242,0,259],
[255,249,283,280,262,249,260,241,0]])



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
result = np.append(np.array([9, 500, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,261,262,281,253,288,267,284],
[251,0,276,271,287,241,276,279,267],
[239,224,0,258,251,253,253,241,281],
[238,229,242,0,266,234,261,239,260],
[219,213,249,234,0,247,253,256,273],
[247,259,247,266,253,0,266,259,279],
[212,224,247,239,247,234,0,252,249],
[233,221,259,261,244,241,248,0,269],
[216,233,219,240,227,221,251,231,0]])



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
result = np.append(np.array([9, 500, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,239,241,195,206,272,220,240],
[283,0,300,279,246,270,295,247,272],
[261,200,0,274,235,206,251,246,246],
[259,221,226,0,234,234,287,221,260],
[305,254,265,266,0,237,263,243,246],
[294,230,294,266,263,0,315,250,291],
[228,205,249,213,237,185,0,192,222],
[280,253,254,279,257,250,308,0,265],
[260,228,254,240,254,209,278,235,0]])



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
result = np.append(np.array([9, 500, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,233,228,251,225,258,256,234],
[255,0,247,247,232,243,243,258,234],
[267,253,0,253,266,249,258,264,239],
[272,253,247,0,266,250,255,261,242],
[249,268,234,234,0,234,251,252,238],
[275,257,251,250,266,0,248,258,264],
[242,257,242,245,249,252,0,249,237],
[244,242,236,239,248,242,251,0,240],
[266,266,261,258,262,236,263,260,0]])



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
result = np.append(np.array([9, 500, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,200,337,276,317,260,324,346,314],
[300,0,293,238,324,335,313,354,330],
[163,207,0,257,208,243,272,349,293],
[224,262,243,0,237,309,227,275,266],
[183,176,292,263,0,241,200,299,311],
[240,165,257,191,259,0,215,313,278],
[176,187,228,273,300,285,0,296,292],
[154,146,151,225,201,187,204,0,236],
[186,170,207,234,189,222,208,264,0]])



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
result = np.append(np.array([9, 500, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,224,237,231,229,256,231,270],
[268,0,236,260,273,254,259,270,271],
[276,264,0,244,251,243,268,259,266],
[263,240,256,0,256,254,290,272,276],
[269,227,249,244,0,232,257,263,264],
[271,246,257,246,268,0,278,254,243],
[244,241,232,210,243,222,0,256,256],
[269,230,241,228,237,246,244,0,253],
[230,229,234,224,236,257,244,247,0]])



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
result = np.append(np.array([9, 500, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,245,264,260,257,264,242,247],
[245,0,223,234,246,232,253,249,241],
[255,277,0,266,269,245,271,258,238],
[236,266,234,0,254,235,262,257,254],
[240,254,231,246,0,240,257,256,231],
[243,268,255,265,260,0,261,266,250],
[236,247,229,238,243,239,0,247,236],
[258,251,242,243,244,234,253,0,246],
[253,259,262,246,269,250,264,254,0]])



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
result = np.append(np.array([9, 500, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,201,223,216,213,231,218,242,197],
[299,0,263,251,241,266,246,276,251],
[277,237,0,253,223,273,267,264,229],
[284,249,247,0,238,235,243,246,225],
[287,259,277,262,0,247,282,271,256],
[269,234,227,265,253,0,276,277,254],
[282,254,233,257,218,224,0,243,232],
[258,224,236,254,229,223,257,0,239],
[303,249,271,275,244,246,268,261,0]])



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
result = np.append(np.array([9, 500, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,230,237,250,223,241,255,253],
[271,0,259,259,267,253,256,252,249],
[270,241,0,258,257,254,267,265,252],
[263,241,242,0,251,240,255,248,241],
[250,233,243,249,0,221,255,248,241],
[277,247,246,260,279,0,269,260,252],
[259,244,233,245,245,231,0,258,243],
[245,248,235,252,252,240,242,0,249],
[247,251,248,259,259,248,257,251,0]])



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
result = np.append(np.array([9, 500, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,273,266,265,242,300,245,258],
[241,0,234,278,296,221,294,271,271],
[227,266,0,260,270,244,296,256,264],
[234,222,240,0,277,253,282,245,265],
[235,204,230,223,0,210,262,230,218],
[258,279,256,247,290,0,292,269,256],
[200,206,204,218,238,208,0,237,240],
[255,229,244,255,270,231,263,0,286],
[242,229,236,235,282,244,260,214,0]])



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
result = np.append(np.array([9, 500, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_9_500.csv", index=False, header=False)