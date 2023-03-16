
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,243,239,222,243,235,244,245],
[258,0,247,258,254,240,236,248],
[262,254,0,254,245,258,258,248],
[279,243,247,0,246,252,246,252],
[258,247,256,255,0,249,249,250],
[266,261,243,249,252,0,250,241],
[257,265,243,255,252,251,0,254],
[256,253,253,249,251,260,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,249,247,279,251,258,274],
[249,0,238,237,270,284,255,274],
[252,263,0,260,311,291,249,294],
[254,264,241,0,301,264,278,301],
[222,231,190,200,0,232,223,244],
[250,217,210,237,269,0,235,278],
[243,246,252,223,278,266,0,287],
[227,227,207,200,257,223,214,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,260,250,254,252,270,258],
[252,0,260,246,259,250,267,252],
[241,241,0,240,260,251,246,237],
[251,255,261,0,252,238,259,247],
[247,242,241,249,0,245,274,252],
[249,251,250,263,256,0,266,252],
[231,234,255,242,227,235,0,233],
[243,249,264,254,249,249,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,250,248,298,331,228,306],
[237,0,287,267,289,264,273,288],
[251,214,0,225,260,257,221,263],
[253,234,276,0,276,249,226,277],
[203,212,241,225,0,269,204,244],
[170,237,244,252,232,0,222,195],
[273,228,280,275,297,279,0,341],
[195,213,238,224,257,306,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,230,241,237,259,236,260],
[270,0,259,249,254,259,251,264],
[271,242,0,253,250,259,244,262],
[260,252,248,0,259,251,246,248],
[264,247,251,242,0,247,245,250],
[242,242,242,250,254,0,245,250],
[265,250,257,255,256,256,0,255],
[241,237,239,253,251,251,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,290,256,274,282,262,237],
[259,0,264,266,256,286,234,265],
[211,237,0,251,263,276,208,245],
[245,235,250,0,263,286,228,235],
[227,245,238,238,0,237,212,223],
[219,215,225,215,264,0,214,223],
[239,267,293,273,289,287,0,250],
[264,236,256,266,278,278,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,259,245,277,267,265,258],
[264,0,264,231,269,261,246,281],
[242,237,0,241,252,240,244,248],
[256,270,260,0,292,288,248,270],
[224,232,249,209,0,250,258,240],
[234,240,261,213,251,0,243,264],
[236,255,257,253,243,258,0,261],
[243,220,253,231,261,237,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,193,210,198,186,229,206],
[266,0,269,254,198,248,272,260],
[308,232,0,244,279,252,275,236],
[291,247,257,0,229,231,280,253],
[303,303,222,272,0,263,289,289],
[315,253,249,270,238,0,276,261],
[272,229,226,221,212,225,0,215],
[295,241,265,248,212,240,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,212,244,256,196,263,241,257],
[289,0,280,311,249,287,257,271],
[257,221,0,237,218,219,226,251],
[245,190,264,0,200,268,193,244],
[305,252,283,301,0,261,191,272],
[238,214,282,233,240,0,308,265],
[260,244,275,308,310,193,0,267],
[244,230,250,257,229,236,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,265,239,268,224,234,252],
[235,0,223,239,242,235,225,214],
[236,278,0,252,251,242,245,235],
[262,262,249,0,265,254,251,259],
[233,259,250,236,0,233,228,236],
[277,266,259,247,268,0,219,242],
[267,276,256,250,273,282,0,258],
[249,287,266,242,265,259,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,265,255,250,252,263,252],
[246,0,258,250,254,243,278,252],
[236,243,0,250,248,241,256,259],
[246,251,251,0,247,233,246,243],
[251,247,253,254,0,238,249,245],
[249,258,260,268,263,0,258,260],
[238,223,245,255,252,243,0,236],
[249,249,242,258,256,241,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,314,259,211,264,259,238],
[221,0,255,214,196,232,253,222],
[187,246,0,271,261,218,277,272],
[242,287,230,0,205,252,277,213],
[290,305,240,296,0,293,304,300],
[237,269,283,249,208,0,270,228],
[242,248,224,224,197,231,0,258],
[263,279,229,288,201,273,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,234,250,248,229,257,255],
[265,0,258,244,279,257,248,248],
[267,243,0,248,257,249,272,241],
[251,257,253,0,274,243,268,246],
[253,222,244,227,0,206,246,215],
[272,244,252,258,295,0,275,270],
[244,253,229,233,255,226,0,237],
[246,253,260,255,286,231,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,235,232,256,243,264,255],
[244,0,256,240,266,255,261,258],
[266,245,0,253,265,244,253,260],
[269,261,248,0,268,264,263,250],
[245,235,236,233,0,250,264,243],
[258,246,257,237,251,0,248,257],
[237,240,248,238,237,253,0,237],
[246,243,241,251,258,244,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,254,224,234,269,252,281],
[252,0,232,223,255,243,269,310],
[247,269,0,263,265,262,252,276],
[277,278,238,0,274,279,281,280],
[267,246,236,227,0,277,236,267],
[232,258,239,222,224,0,227,246],
[249,232,249,220,265,274,0,296],
[220,191,225,221,234,255,205,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,242,254,252,245,264,251],
[260,0,254,267,246,240,272,263],
[259,247,0,272,247,258,261,242],
[247,234,229,0,248,239,244,231],
[249,255,254,253,0,229,249,240],
[256,261,243,262,272,0,280,248],
[237,229,240,257,252,221,0,223],
[250,238,259,270,261,253,278,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,279,246,262,269,245,260,260],
[222,0,242,223,242,229,225,247],
[255,259,0,245,271,236,257,261],
[239,278,256,0,273,266,263,250],
[232,259,230,228,0,222,247,229],
[256,272,265,235,279,0,265,262],
[241,276,244,238,254,236,0,260],
[241,254,240,251,272,239,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,259,240,247,249,242,244],
[250,0,265,249,228,260,249,232],
[242,236,0,256,231,256,251,249],
[261,252,245,0,254,247,243,230],
[254,273,270,247,0,269,263,254],
[252,241,245,254,232,0,249,233],
[259,252,250,258,238,252,0,255],
[257,269,252,271,247,268,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,284,261,237,248,264,287],
[245,0,274,252,256,235,253,253],
[217,227,0,228,214,223,220,235],
[240,249,273,0,270,254,254,265],
[264,245,287,231,0,232,281,283],
[253,266,278,247,269,0,283,269],
[237,248,281,247,220,218,0,248],
[214,248,266,236,218,232,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,285,259,277,252,250,266,262],
[216,0,266,225,217,236,226,251],
[242,235,0,265,263,233,257,272],
[224,276,236,0,252,235,201,240],
[249,284,238,249,0,267,255,255],
[251,265,268,266,234,0,253,278],
[235,275,244,300,246,248,0,280],
[239,250,229,261,246,223,221,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,243,225,218,246,245,232],
[274,0,276,244,231,248,254,260],
[258,225,0,239,214,232,254,247],
[276,257,262,0,258,250,290,268],
[283,270,287,243,0,257,257,248],
[255,253,269,251,244,0,254,235],
[256,247,247,211,244,247,0,235],
[269,241,254,233,253,266,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,252,250,239,235,254,229],
[285,0,257,269,250,271,266,253],
[249,244,0,259,227,247,251,248],
[251,232,242,0,264,240,261,251],
[262,251,274,237,0,270,250,254],
[266,230,254,261,231,0,257,256],
[247,235,250,240,251,244,0,259],
[272,248,253,250,247,245,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,255,251,242,259,271,261],
[232,0,272,276,256,267,273,293],
[246,229,0,245,238,243,274,220],
[250,225,256,0,238,246,278,237],
[259,245,263,263,0,232,301,259],
[242,234,258,255,269,0,247,241],
[230,228,227,223,200,254,0,217],
[240,208,281,264,242,260,284,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,269,264,235,259,246,249],
[249,0,247,241,243,258,228,253],
[232,254,0,246,259,239,223,235],
[237,260,255,0,242,252,224,249],
[266,258,242,259,0,252,252,284],
[242,243,262,249,249,0,227,258],
[255,273,278,277,249,274,0,256],
[252,248,266,252,217,243,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,251,253,261,254,259,249],
[241,0,224,232,244,267,252,238],
[250,277,0,255,269,250,263,265],
[248,269,246,0,280,255,271,260],
[240,257,232,221,0,239,247,250],
[247,234,251,246,262,0,256,246],
[242,249,238,230,254,245,0,242],
[252,263,236,241,251,255,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,271,260,234,259,251,260],
[240,0,258,223,218,250,271,250],
[230,243,0,231,239,260,246,265],
[241,278,270,0,266,276,252,278],
[267,283,262,235,0,256,269,270],
[242,251,241,225,245,0,270,263],
[250,230,255,249,232,231,0,252],
[241,251,236,223,231,238,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,230,252,258,280,233,240],
[243,0,251,268,256,256,252,245],
[271,250,0,272,258,260,238,252],
[249,233,229,0,247,238,234,229],
[243,245,243,254,0,254,230,240],
[221,245,241,263,247,0,223,237],
[268,249,263,267,271,278,0,276],
[261,256,249,272,261,264,225,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,257,250,262,260,244,258],
[274,0,249,250,281,278,255,262],
[244,252,0,237,266,257,247,240],
[251,251,264,0,268,258,249,270],
[239,220,235,233,0,250,241,252],
[241,223,244,243,251,0,243,249],
[257,246,254,252,260,258,0,278],
[243,239,261,231,249,252,223,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,267,254,260,263,244,234],
[256,0,276,251,249,262,254,260],
[234,225,0,235,260,255,237,243],
[247,250,266,0,260,263,255,263],
[241,252,241,241,0,252,246,256],
[238,239,246,238,249,0,258,243],
[257,247,264,246,255,243,0,241],
[267,241,258,238,245,258,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,341,184,274,223,206,283],
[287,0,365,204,205,197,228,294],
[160,136,0,169,164,111,154,197],
[317,297,332,0,236,212,291,335],
[227,296,337,265,0,251,261,298],
[278,304,390,289,250,0,238,283],
[295,273,347,210,240,263,0,349],
[218,207,304,166,203,218,152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,260,234,255,223,253,229],
[253,0,274,254,270,259,254,245],
[241,227,0,241,255,248,256,246],
[267,247,260,0,253,249,270,233],
[246,231,246,248,0,236,257,238],
[278,242,253,252,265,0,247,263],
[248,247,245,231,244,254,0,253],
[272,256,255,268,263,238,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,249,245,250,256,267,241],
[241,0,238,242,242,246,248,230],
[252,263,0,246,246,246,256,241],
[256,259,255,0,242,246,245,227],
[251,259,255,259,0,234,245,248],
[245,255,255,255,267,0,253,247],
[234,253,245,256,256,248,0,257],
[260,271,260,274,253,254,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,258,200,229,280,288,200],
[228,0,223,239,271,289,224,234],
[243,278,0,259,282,305,291,258],
[301,262,242,0,259,286,239,196],
[272,230,219,242,0,296,290,212],
[221,212,196,215,205,0,228,181],
[213,277,210,262,211,273,0,197],
[301,267,243,305,289,320,304,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,271,261,252,248,254,238],
[255,0,273,280,250,251,264,248],
[230,228,0,256,241,230,242,223],
[240,221,245,0,231,252,242,234],
[249,251,260,270,0,257,266,248],
[253,250,271,249,244,0,254,254],
[247,237,259,259,235,247,0,241],
[263,253,278,267,253,247,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,242,251,247,251,254,238],
[254,0,241,247,232,240,262,228],
[259,260,0,239,238,244,246,245],
[250,254,262,0,257,271,267,254],
[254,269,263,244,0,274,271,260],
[250,261,257,230,227,0,259,243],
[247,239,255,234,230,242,0,241],
[263,273,256,247,241,258,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,274,255,232,249,264,241],
[253,0,276,265,254,260,250,248],
[227,225,0,252,239,234,233,235],
[246,236,249,0,229,231,227,228],
[269,247,262,272,0,263,240,255],
[252,241,267,270,238,0,235,233],
[237,251,268,274,261,266,0,244],
[260,253,266,273,246,268,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,230,230,250,230,227,243],
[251,0,241,253,268,244,276,281],
[271,260,0,243,280,254,246,281],
[271,248,258,0,289,263,252,283],
[251,233,221,212,0,222,235,246],
[271,257,247,238,279,0,268,276],
[274,225,255,249,266,233,0,261],
[258,220,220,218,255,225,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,272,245,261,261,252,252],
[233,0,247,229,249,251,247,246],
[229,254,0,242,240,223,245,244],
[256,272,259,0,260,266,254,249],
[240,252,261,241,0,261,252,237],
[240,250,278,235,240,0,261,248],
[249,254,256,247,249,240,0,245],
[249,255,257,252,264,253,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,228,239,232,250,261,245],
[276,0,255,230,257,264,264,255],
[273,246,0,227,259,257,253,270],
[262,271,274,0,253,233,247,270],
[269,244,242,248,0,271,247,255],
[251,237,244,268,230,0,264,279],
[240,237,248,254,254,237,0,257],
[256,246,231,231,246,222,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,245,258,236,246,253,251],
[262,0,243,268,255,253,263,265],
[256,258,0,245,227,236,255,237],
[243,233,256,0,254,240,256,251],
[265,246,274,247,0,247,262,259],
[255,248,265,261,254,0,276,272],
[248,238,246,245,239,225,0,242],
[250,236,264,250,242,229,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,321,252,342,248,299,305,294],
[180,0,253,302,292,272,338,284],
[249,248,0,290,241,285,274,316],
[159,199,211,0,201,279,264,243],
[253,209,260,300,0,256,269,301],
[202,229,216,222,245,0,298,207],
[196,163,227,237,232,203,0,215],
[207,217,185,258,200,294,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,252,296,286,236,247,251],
[239,0,232,276,289,239,266,252],
[249,269,0,284,300,253,276,255],
[205,225,217,0,257,203,227,219],
[215,212,201,244,0,215,251,236],
[265,262,248,298,286,0,261,256],
[254,235,225,274,250,240,0,239],
[250,249,246,282,265,245,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,238,247,235,239,250,257],
[237,0,229,256,243,243,247,255],
[263,272,0,241,248,256,256,258],
[254,245,260,0,253,235,260,245],
[266,258,253,248,0,254,249,277],
[262,258,245,266,247,0,247,265],
[251,254,245,241,252,254,0,250],
[244,246,243,256,224,236,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,247,262,254,285,258,257],
[248,0,233,262,229,264,227,237],
[254,268,0,282,253,264,240,238],
[239,239,219,0,247,253,244,245],
[247,272,248,254,0,266,246,244],
[216,237,237,248,235,0,254,236],
[243,274,261,257,255,247,0,249],
[244,264,263,256,257,265,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,294,321,274,222,277,304],
[253,0,303,307,241,248,294,275],
[207,198,0,242,219,213,221,148],
[180,194,259,0,229,222,178,230],
[227,260,282,272,0,298,276,279],
[279,253,288,279,203,0,280,305],
[224,207,280,323,225,221,0,257],
[197,226,353,271,222,196,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,288,288,249,293,227,236,290],
[213,0,222,205,184,189,209,245],
[213,279,0,211,183,212,233,250],
[252,296,290,0,258,262,268,250],
[208,317,318,243,0,245,291,267],
[274,312,289,239,256,0,291,317],
[265,292,268,233,210,210,0,238],
[211,256,251,251,234,184,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,243,245,253,257,245,242],
[252,0,251,250,257,266,262,261],
[258,250,0,254,256,265,249,251],
[256,251,247,0,258,259,254,240],
[248,244,245,243,0,265,257,238],
[244,235,236,242,236,0,247,229],
[256,239,252,247,244,254,0,252],
[259,240,250,261,263,272,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,241,199,236,245,233,231],
[254,0,223,236,245,232,246,227],
[260,278,0,240,241,271,233,245],
[302,265,261,0,236,247,257,262],
[265,256,260,265,0,240,252,232],
[256,269,230,254,261,0,235,248],
[268,255,268,244,249,266,0,251],
[270,274,256,239,269,253,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,299,269,294,242,289,204,343],
[202,0,267,198,210,264,192,241],
[232,234,0,263,197,272,203,303],
[207,303,238,0,209,251,232,252],
[259,291,304,292,0,287,226,308],
[212,237,229,250,214,0,258,274],
[297,309,298,269,275,243,0,258],
[158,260,198,249,193,227,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,274,258,247,227,265,252],
[266,0,266,259,290,234,280,264],
[227,235,0,227,236,198,245,218],
[243,242,274,0,283,254,277,241],
[254,211,265,218,0,232,243,213],
[274,267,303,247,269,0,276,252],
[236,221,256,224,258,225,0,226],
[249,237,283,260,288,249,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,234,234,241,242,256,232],
[261,0,240,234,252,250,255,237],
[267,261,0,246,260,261,256,256],
[267,267,255,0,266,256,270,235],
[260,249,241,235,0,256,269,235],
[259,251,240,245,245,0,268,251],
[245,246,245,231,232,233,0,226],
[269,264,245,266,266,250,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,185,200,239,196,243,276,194],
[316,0,242,289,251,293,313,240],
[301,259,0,264,266,333,298,219],
[262,212,237,0,230,251,281,208],
[305,250,235,271,0,294,328,258],
[258,208,168,250,207,0,257,200],
[225,188,203,220,173,244,0,201],
[307,261,282,293,243,301,300,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,258,271,243,248,261,254],
[244,0,253,249,229,234,236,263],
[243,248,0,256,242,228,227,242],
[230,252,245,0,227,227,224,242],
[258,272,259,274,0,246,241,250],
[253,267,273,274,255,0,247,259],
[240,265,274,277,260,254,0,251],
[247,238,259,259,251,242,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,272,284,275,268,269,282],
[254,0,282,266,275,290,266,250],
[229,219,0,276,243,233,245,254],
[217,235,225,0,209,238,215,224],
[226,226,258,292,0,266,265,247],
[233,211,268,263,235,0,245,252],
[232,235,256,286,236,256,0,260],
[219,251,247,277,254,249,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,256,266,258,274,265,260],
[252,0,265,240,258,275,289,255],
[245,236,0,251,239,272,265,242],
[235,261,250,0,264,264,265,239],
[243,243,262,237,0,262,250,246],
[227,226,229,237,239,0,258,237],
[236,212,236,236,251,243,0,227],
[241,246,259,262,255,264,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,320,235,382,273,324,269],
[258,0,215,196,266,177,266,246],
[181,286,0,166,311,283,212,170],
[266,305,335,0,427,316,245,301],
[119,235,190,74,0,201,142,216],
[228,324,218,185,300,0,281,265],
[177,235,289,256,359,220,0,291],
[232,255,331,200,285,236,210,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,233,262,266,256,271,267],
[243,0,241,243,272,248,253,248],
[268,260,0,237,255,249,261,263],
[239,258,264,0,266,258,251,253],
[235,229,246,235,0,234,247,233],
[245,253,252,243,267,0,267,264],
[230,248,240,250,254,234,0,242],
[234,253,238,248,268,237,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,247,219,233,252,245,263],
[248,0,249,257,236,275,248,250],
[254,252,0,223,251,251,261,255],
[282,244,278,0,228,254,265,249],
[268,265,250,273,0,249,257,272],
[249,226,250,247,252,0,230,254],
[256,253,240,236,244,271,0,241],
[238,251,246,252,229,247,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,249,246,242,229,236,254],
[257,0,260,250,231,241,224,262],
[252,241,0,235,236,252,244,264],
[255,251,266,0,237,238,236,257],
[259,270,265,264,0,249,246,270],
[272,260,249,263,252,0,262,275],
[265,277,257,265,255,239,0,275],
[247,239,237,244,231,226,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,213,206,254,208,203,204,233],
[288,0,244,279,241,256,264,229],
[295,257,0,250,319,337,340,263],
[247,222,251,0,272,257,278,192],
[293,260,182,229,0,307,262,220],
[298,245,164,244,194,0,214,202],
[297,237,161,223,239,287,0,110],
[268,272,238,309,281,299,391,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,249,277,257,280,247,275],
[275,0,231,229,262,284,225,281],
[252,270,0,225,276,301,246,292],
[224,272,276,0,267,294,260,300],
[244,239,225,234,0,257,223,253],
[221,217,200,207,244,0,187,236],
[254,276,255,241,278,314,0,281],
[226,220,209,201,248,265,220,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,280,272,246,265,253,269],
[252,0,280,253,239,233,233,266],
[221,221,0,227,223,237,248,239],
[229,248,274,0,242,249,240,252],
[255,262,278,259,0,255,243,277],
[236,268,264,252,246,0,247,249],
[248,268,253,261,258,254,0,254],
[232,235,262,249,224,252,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,233,244,222,262,217,245],
[274,0,253,243,229,306,239,243],
[268,248,0,265,266,276,250,249],
[257,258,236,0,241,262,238,254],
[279,272,235,260,0,292,254,269],
[239,195,225,239,209,0,218,232],
[284,262,251,263,247,283,0,270],
[256,258,252,247,232,269,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,191,226,204,236,209,231],
[252,0,230,194,213,238,213,221],
[310,271,0,263,240,251,254,257],
[275,307,238,0,258,289,264,272],
[297,288,261,243,0,298,280,266],
[265,263,250,212,203,0,254,219],
[292,288,247,237,221,247,0,265],
[270,280,244,229,235,282,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,264,279,238,230,271,230],
[228,0,266,243,231,254,227,259],
[237,235,0,235,247,250,224,216],
[222,258,266,0,251,247,245,235],
[263,270,254,250,0,268,285,247],
[271,247,251,254,233,0,254,257],
[230,274,277,256,216,247,0,231],
[271,242,285,266,254,244,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,247,243,252,280,250,245],
[263,0,252,262,251,251,241,262],
[254,249,0,255,229,235,257,249],
[258,239,246,0,241,281,236,256],
[249,250,272,260,0,276,252,266],
[221,250,266,220,225,0,238,254],
[251,260,244,265,249,263,0,281],
[256,239,252,245,235,247,220,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,243,263,221,270,243,250],
[260,0,245,320,245,247,263,254],
[258,256,0,298,244,263,253,251],
[238,181,203,0,194,197,199,211],
[280,256,257,307,0,235,237,275],
[231,254,238,304,266,0,244,254],
[258,238,248,302,264,257,0,286],
[251,247,250,290,226,247,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,289,248,255,272,272,297,278],
[212,0,249,226,219,226,246,257],
[253,252,0,229,248,253,283,256],
[246,275,272,0,262,287,280,264],
[229,282,253,239,0,260,270,280],
[229,275,248,214,241,0,247,235],
[204,255,218,221,231,254,0,253],
[223,244,245,237,221,266,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,208,233,249,247,239,222],
[247,0,226,221,249,243,232,229],
[293,275,0,245,289,254,277,288],
[268,280,256,0,268,249,249,239],
[252,252,212,233,0,226,260,221],
[254,258,247,252,275,0,248,202],
[262,269,224,252,241,253,0,219],
[279,272,213,262,280,299,282,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,212,280,266,312,272,216],
[253,0,206,237,225,272,272,221],
[289,295,0,310,281,347,306,240],
[221,264,191,0,266,265,293,189],
[235,276,220,235,0,235,280,261],
[189,229,154,236,266,0,209,177],
[229,229,195,208,221,292,0,189],
[285,280,261,312,240,324,312,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,247,259,243,252,245,229],
[260,0,258,261,247,261,251,238],
[254,243,0,239,252,254,224,225],
[242,240,262,0,235,249,255,233],
[258,254,249,266,0,267,243,252],
[249,240,247,252,234,0,232,232],
[256,250,277,246,258,269,0,246],
[272,263,276,268,249,269,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,260,245,248,259,239,239],
[251,0,252,253,254,246,238,248],
[241,249,0,251,242,233,237,225],
[256,248,250,0,271,235,256,252],
[253,247,259,230,0,249,258,263],
[242,255,268,266,252,0,263,264],
[262,263,264,245,243,238,0,246],
[262,253,276,249,238,237,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,216,261,130,91,328],
[456,0,152,322,367,303,152,434],
[455,349,0,298,237,242,179,304],
[285,179,203,0,373,264,203,395],
[240,134,264,128,0,219,264,326],
[371,198,259,237,282,0,152,434],
[410,349,322,298,237,349,0,304],
[173,67,197,106,175,67,197,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,321,261,293,302,232,223],
[264,0,298,270,252,275,286,239],
[180,203,0,209,224,223,182,245],
[240,231,292,0,263,232,201,248],
[208,249,277,238,0,285,247,216],
[199,226,278,269,216,0,249,232],
[269,215,319,300,254,252,0,275],
[278,262,256,253,285,269,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,258,254,267,249,246,255],
[237,0,224,232,253,245,233,243],
[243,277,0,245,256,244,255,255],
[247,269,256,0,257,271,260,260],
[234,248,245,244,0,246,241,245],
[252,256,257,230,255,0,243,250],
[255,268,246,241,260,258,0,249],
[246,258,246,241,256,251,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,268,267,256,288,239,248],
[247,0,240,270,242,250,223,265],
[233,261,0,295,266,295,269,254],
[234,231,206,0,254,250,233,208],
[245,259,235,247,0,237,248,241],
[213,251,206,251,264,0,276,233],
[262,278,232,268,253,225,0,277],
[253,236,247,293,260,268,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,305,222,344,216,255,248,191],
[196,0,285,209,153,240,217,159],
[279,216,0,254,184,241,171,111],
[157,292,247,0,192,197,200,228],
[285,348,317,309,0,238,251,204],
[246,261,260,304,263,0,234,251],
[253,284,330,301,250,267,0,202],
[310,342,390,273,297,250,299,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,252,270,247,242,266,288],
[244,0,255,322,268,272,337,296],
[249,246,0,293,249,284,314,257],
[231,179,208,0,224,242,314,236],
[254,233,252,277,0,259,262,256],
[259,229,217,259,242,0,289,274],
[235,164,187,187,239,212,0,238],
[213,205,244,265,245,227,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,290,233,223,158,283,315,298],
[211,0,189,211,224,211,327,276],
[268,312,0,285,188,302,329,249],
[278,290,216,0,253,283,330,247],
[343,277,313,248,0,299,326,313],
[218,290,199,218,202,0,233,227],
[186,174,172,171,175,268,0,176],
[203,225,252,254,188,274,325,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,287,243,265,297,230,272],
[234,0,254,220,228,232,248,266],
[214,247,0,245,212,237,221,234],
[258,281,256,0,240,249,227,255],
[236,273,289,261,0,263,259,259],
[204,269,264,252,238,0,233,254],
[271,253,280,274,242,268,0,272],
[229,235,267,246,242,247,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,265,257,251,240,231,252],
[242,0,248,234,197,205,252,241],
[236,253,0,240,241,220,252,240],
[244,267,261,0,245,252,253,204],
[250,304,260,256,0,241,276,237],
[261,296,281,249,260,0,278,248],
[270,249,249,248,225,223,0,227],
[249,260,261,297,264,253,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,257,214,228,285,163,229],
[280,0,138,156,194,136,194,185],
[244,363,0,222,236,313,270,302],
[287,345,279,0,173,309,282,242],
[273,307,265,328,0,287,230,275],
[216,365,188,192,214,0,214,234],
[338,307,231,219,271,287,0,242],
[272,316,199,259,226,267,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,235,244,247,232,238,249],
[263,0,251,259,269,244,246,259],
[266,250,0,242,265,251,243,253],
[257,242,259,0,258,245,229,263],
[254,232,236,243,0,234,230,243],
[269,257,250,256,267,0,258,273],
[263,255,258,272,271,243,0,265],
[252,242,248,238,258,228,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,260,232,241,244,234,249],
[265,0,263,237,253,285,259,252],
[241,238,0,240,256,240,242,225],
[269,264,261,0,247,265,275,249],
[260,248,245,254,0,256,255,242],
[257,216,261,236,245,0,277,256],
[267,242,259,226,246,224,0,224],
[252,249,276,252,259,245,277,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,212,226,251,255,246,245],
[268,0,264,218,250,300,256,280],
[289,237,0,215,218,246,253,237],
[275,283,286,0,258,267,247,235],
[250,251,283,243,0,287,256,252],
[246,201,255,234,214,0,232,253],
[255,245,248,254,245,269,0,231],
[256,221,264,266,249,248,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,233,206,220,230,220,235],
[240,0,267,222,236,254,252,265],
[268,234,0,224,210,243,234,245],
[295,279,277,0,247,278,269,270],
[281,265,291,254,0,277,248,264],
[271,247,258,223,224,0,248,230],
[281,249,267,232,253,253,0,272],
[266,236,256,231,237,271,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,177,229,255,329,279,272,202],
[324,0,317,250,284,374,317,347],
[272,184,0,255,319,282,352,319],
[246,251,246,0,319,296,212,269],
[172,217,182,182,0,344,307,290],
[222,127,219,205,157,0,205,180],
[229,184,149,289,194,296,0,217],
[299,154,182,232,211,321,284,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,276,254,262,259,251,260],
[260,0,251,253,232,224,248,236],
[225,250,0,242,254,249,230,254],
[247,248,259,0,267,266,250,280],
[239,269,247,234,0,245,245,245],
[242,277,252,235,256,0,242,247],
[250,253,271,251,256,259,0,261],
[241,265,247,221,256,254,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,243,264,252,256,249,263],
[277,0,248,262,247,265,270,270],
[258,253,0,267,258,249,258,262],
[237,239,234,0,215,214,228,233],
[249,254,243,286,0,267,264,243],
[245,236,252,287,234,0,244,261],
[252,231,243,273,237,257,0,248],
[238,231,239,268,258,240,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,221,236,241,246,231,238],
[256,0,282,271,245,255,264,235],
[280,219,0,245,269,225,276,256],
[265,230,256,0,254,247,258,261],
[260,256,232,247,0,233,224,246],
[255,246,276,254,268,0,278,249],
[270,237,225,243,277,223,0,243],
[263,266,245,240,255,252,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,253,267,228,224,227,257],
[266,0,254,267,236,240,255,257],
[248,247,0,255,261,224,253,250],
[234,234,246,0,233,242,216,222],
[273,265,240,268,0,258,250,260],
[277,261,277,259,243,0,258,242],
[274,246,248,285,251,243,0,232],
[244,244,251,279,241,259,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,269,255,274,255,243,253],
[238,0,236,245,254,259,252,240],
[232,265,0,257,274,262,261,247],
[246,256,244,0,243,266,253,258],
[227,247,227,258,0,238,238,231],
[246,242,239,235,263,0,265,245],
[258,249,240,248,263,236,0,253],
[248,261,254,243,270,256,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,238,273,277,277,264,268],
[251,0,229,242,248,245,226,257],
[263,272,0,263,261,262,219,245],
[228,259,238,0,260,263,243,246],
[224,253,240,241,0,255,260,243],
[224,256,239,238,246,0,242,232],
[237,275,282,258,241,259,0,261],
[233,244,256,255,258,269,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,254,234,187,220,268,225],
[258,0,261,258,217,273,315,260],
[247,240,0,215,244,259,274,260],
[267,243,286,0,242,259,315,233],
[314,284,257,259,0,298,306,242],
[281,228,242,242,203,0,273,221],
[233,186,227,186,195,228,0,204],
[276,241,241,268,259,280,297,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,262,226,240,263,270,259],
[237,0,241,217,226,249,244,241],
[239,260,0,242,225,237,267,231],
[275,284,259,0,257,267,279,248],
[261,275,276,244,0,252,285,258],
[238,252,264,234,249,0,255,247],
[231,257,234,222,216,246,0,248],
[242,260,270,253,243,254,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,236,257,259,252,260,267],
[238,0,228,231,263,256,242,242],
[265,273,0,247,271,270,244,276],
[244,270,254,0,262,267,247,256],
[242,238,230,239,0,256,244,252],
[249,245,231,234,245,0,246,251],
[241,259,257,254,257,255,0,254],
[234,259,225,245,249,250,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,312,268,214,278,238,260],
[276,0,285,252,186,237,217,250],
[189,216,0,204,213,213,221,212],
[233,249,297,0,254,238,248,276],
[287,315,288,247,0,245,220,262],
[223,264,288,263,256,0,297,269],
[263,284,280,253,281,204,0,223],
[241,251,289,225,239,232,278,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,269,236,242,252,254,250],
[259,0,264,239,253,255,244,274],
[232,237,0,224,241,244,232,242],
[265,262,277,0,269,271,245,269],
[259,248,260,232,0,247,256,277],
[249,246,257,230,254,0,256,262],
[247,257,269,256,245,245,0,266],
[251,227,259,232,224,239,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,229,262,276,254,242,244],
[230,0,209,229,252,247,248,221],
[272,292,0,278,268,266,248,256],
[239,272,223,0,272,244,230,256],
[225,249,233,229,0,222,196,239],
[247,254,235,257,279,0,239,252],
[259,253,253,271,305,262,0,247],
[257,280,245,245,262,249,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,260,238,248,232,232,247],
[240,0,234,233,234,230,220,247],
[241,267,0,246,259,251,243,253],
[263,268,255,0,245,259,252,245],
[253,267,242,256,0,240,239,231],
[269,271,250,242,261,0,246,249],
[269,281,258,249,262,255,0,257],
[254,254,248,256,270,252,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,241,240,251,253,232,252],
[258,0,240,245,259,260,222,258],
[260,261,0,264,258,254,235,256],
[261,256,237,0,250,267,256,259],
[250,242,243,251,0,256,236,246],
[248,241,247,234,245,0,234,244],
[269,279,266,245,265,267,0,273],
[249,243,245,242,255,257,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,253,240,248,247,246,262],
[234,0,241,234,240,230,242,244],
[248,260,0,253,262,249,245,266],
[261,267,248,0,260,244,266,256],
[253,261,239,241,0,254,244,267],
[254,271,252,257,247,0,263,259],
[255,259,256,235,257,238,0,272],
[239,257,235,245,234,242,229,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,246,262,225,284,333,227],
[274,0,227,250,203,170,250,224],
[255,274,0,245,279,301,359,255],
[239,251,256,0,225,317,389,279],
[276,298,222,276,0,201,373,314],
[217,331,200,184,300,0,294,299],
[168,251,142,112,128,207,0,206],
[274,277,246,222,187,202,295,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,237,258,261,267,243,272],
[250,0,253,259,249,273,245,258],
[264,248,0,266,247,269,244,277],
[243,242,235,0,259,265,235,260],
[240,252,254,242,0,272,256,258],
[234,228,232,236,229,0,226,253],
[258,256,257,266,245,275,0,280],
[229,243,224,241,243,248,221,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,236,232,256,250,252,250],
[223,0,207,216,218,230,231,220],
[265,294,0,276,256,233,232,241],
[269,285,225,0,261,219,250,255],
[245,283,245,240,0,239,251,238],
[251,271,268,282,262,0,248,255],
[249,270,269,251,250,253,0,233],
[251,281,260,246,263,246,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,186,267,223,237,225,234],
[279,0,247,297,275,283,275,251],
[315,254,0,288,264,282,248,288],
[234,204,213,0,207,247,175,232],
[278,226,237,294,0,259,237,271],
[264,218,219,254,242,0,230,254],
[276,226,253,326,264,271,0,273],
[267,250,213,269,230,247,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,224,237,230,222,240,222],
[274,0,251,253,265,242,253,255],
[277,250,0,260,254,264,254,260],
[264,248,241,0,259,245,246,246],
[271,236,247,242,0,232,253,254],
[279,259,237,256,269,0,257,266],
[261,248,247,255,248,244,0,249],
[279,246,241,255,247,235,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,291,201,142,384,396,273,213],
[210,0,201,239,317,323,244,213],
[300,300,0,202,359,384,173,274],
[359,262,299,0,371,396,267,236],
[117,184,142,130,0,213,92,163],
[105,178,117,105,288,0,202,201],
[228,257,328,234,409,299,0,299],
[288,288,227,265,338,300,202,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,251,228,268,284,253,237],
[230,0,228,273,256,245,249,236],
[250,273,0,242,292,283,268,295],
[273,228,259,0,297,304,269,261],
[233,245,209,204,0,225,227,230],
[217,256,218,197,276,0,275,227],
[248,252,233,232,274,226,0,252],
[264,265,206,240,271,274,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,225,268,230,247,236,237,225],
[276,0,275,255,264,256,257,237],
[233,226,0,205,239,243,212,228],
[271,246,296,0,253,250,263,251],
[254,237,262,248,0,233,244,230],
[265,245,258,251,268,0,250,239],
[264,244,289,238,257,251,0,252],
[276,264,273,250,271,262,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,274,258,234,245,255,250],
[269,0,258,267,261,250,277,272],
[227,243,0,229,235,230,237,244],
[243,234,272,0,264,258,271,261],
[267,240,266,237,0,248,249,245],
[256,251,271,243,253,0,272,239],
[246,224,264,230,252,229,0,246],
[251,229,257,240,256,262,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,241,239,210,254,247,221],
[274,0,235,238,234,260,255,241],
[260,266,0,243,247,247,265,249],
[262,263,258,0,268,266,261,243],
[291,267,254,233,0,252,270,240],
[247,241,254,235,249,0,247,236],
[254,246,236,240,231,254,0,256],
[280,260,252,258,261,265,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,248,250,251,242,243,265],
[247,0,243,247,242,240,231,272],
[253,258,0,237,234,236,232,248],
[251,254,264,0,243,239,243,249],
[250,259,267,258,0,252,251,266],
[259,261,265,262,249,0,260,260],
[258,270,269,258,250,241,0,274],
[236,229,253,252,235,241,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,267,291,247,233,284,241],
[240,0,261,273,216,231,264,223],
[234,240,0,254,226,253,214,245],
[210,228,247,0,203,220,222,200],
[254,285,275,298,0,264,268,230],
[268,270,248,281,237,0,255,259],
[217,237,287,279,233,246,0,238],
[260,278,256,301,271,242,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,252,236,246,235,233,252],
[256,0,248,238,236,237,246,253],
[249,253,0,239,240,236,232,258],
[265,263,262,0,256,247,256,249],
[255,265,261,245,0,256,251,248],
[266,264,265,254,245,0,256,260],
[268,255,269,245,250,245,0,267],
[249,248,243,252,253,241,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,259,272,249,270,282,251],
[243,0,248,275,250,230,251,253],
[242,253,0,253,265,252,265,236],
[229,226,248,0,262,249,262,237],
[252,251,236,239,0,230,246,257],
[231,271,249,252,271,0,279,260],
[219,250,236,239,255,222,0,223],
[250,248,265,264,244,241,278,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,232,301,260,251,217,276],
[261,0,259,286,283,245,286,250],
[269,242,0,283,265,235,272,281],
[200,215,218,0,254,233,222,202],
[241,218,236,247,0,237,229,243],
[250,256,266,268,264,0,239,273],
[284,215,229,279,272,262,0,180],
[225,251,220,299,258,228,321,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,245,242,257,247,228,237],
[252,0,240,243,252,261,257,237],
[256,261,0,239,268,270,249,242],
[259,258,262,0,264,260,247,264],
[244,249,233,237,0,245,243,231],
[254,240,231,241,256,0,227,236],
[273,244,252,254,258,274,0,237],
[264,264,259,237,270,265,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,255,237,268,273,254,251],
[232,0,212,205,223,237,234,225],
[246,289,0,247,268,252,273,276],
[264,296,254,0,278,248,271,259],
[233,278,233,223,0,248,252,259],
[228,264,249,253,253,0,253,246],
[247,267,228,230,249,248,0,264],
[250,276,225,242,242,255,237,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,249,279,253,250,246,256],
[251,0,259,269,252,250,243,270],
[252,242,0,254,248,243,262,255],
[222,232,247,0,235,243,228,257],
[248,249,253,266,0,255,235,256],
[251,251,258,258,246,0,236,268],
[255,258,239,273,266,265,0,267],
[245,231,246,244,245,233,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,242,262,261,252,251,275],
[254,0,256,268,259,247,247,270],
[259,245,0,266,253,256,247,257],
[239,233,235,0,249,234,241,261],
[240,242,248,252,0,238,245,271],
[249,254,245,267,263,0,248,269],
[250,254,254,260,256,253,0,277],
[226,231,244,240,230,232,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,255,268,252,244,251,264],
[269,0,262,245,272,265,274,274],
[246,239,0,257,263,259,247,254],
[233,256,244,0,243,257,268,260],
[249,229,238,258,0,257,262,257],
[257,236,242,244,244,0,264,249],
[250,227,254,233,239,237,0,242],
[237,227,247,241,244,252,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,238,264,252,258,254,255],
[253,0,254,269,248,260,254,252],
[263,247,0,248,238,249,238,229],
[237,232,253,0,239,258,239,249],
[249,253,263,262,0,260,254,263],
[243,241,252,243,241,0,250,257],
[247,247,263,262,247,251,0,255],
[246,249,272,252,238,244,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,262,266,244,259,261,243],
[252,0,256,270,243,261,266,238],
[239,245,0,274,252,252,258,258],
[235,231,227,0,234,244,237,235],
[257,258,249,267,0,251,257,248],
[242,240,249,257,250,0,255,232],
[240,235,243,264,244,246,0,235],
[258,263,243,266,253,269,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,249,274,246,256,244,286],
[260,0,242,275,249,261,246,259],
[252,259,0,267,243,247,268,263],
[227,226,234,0,243,259,216,260],
[255,252,258,258,0,251,244,272],
[245,240,254,242,250,0,246,276],
[257,255,233,285,257,255,0,275],
[215,242,238,241,229,225,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,264,241,239,281,255,225],
[238,0,263,265,218,250,222,245],
[237,238,0,244,225,257,233,226],
[260,236,257,0,252,264,238,246],
[262,283,276,249,0,263,240,232],
[220,251,244,237,238,0,253,257],
[246,279,268,263,261,248,0,242],
[276,256,275,255,269,244,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,165,311,174,238,158,216,227],
[336,0,285,202,260,66,125,113],
[190,216,0,169,270,220,312,232],
[327,299,332,0,427,274,250,254],
[263,241,231,74,0,160,121,132],
[343,435,281,227,341,0,313,255],
[285,376,189,251,380,188,0,299],
[274,388,269,247,369,246,202,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,327,285,255,226,334,223,273],
[174,0,284,226,252,258,261,259],
[216,217,0,218,300,295,234,278],
[246,275,283,0,246,258,239,255],
[275,249,201,255,0,270,252,304],
[167,243,206,243,231,0,265,300],
[278,240,267,262,249,236,0,359],
[228,242,223,246,197,201,142,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,245,231,228,234,250,237],
[266,0,258,260,256,242,233,252],
[256,243,0,240,257,248,246,245],
[270,241,261,0,260,243,245,261],
[273,245,244,241,0,243,241,233],
[267,259,253,258,258,0,247,266],
[251,268,255,256,260,254,0,244],
[264,249,256,240,268,235,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,247,246,240,264,248,236],
[225,0,248,225,223,269,225,222],
[254,253,0,226,251,279,237,218],
[255,276,275,0,248,280,255,252],
[261,278,250,253,0,271,267,251],
[237,232,222,221,230,0,240,244],
[253,276,264,246,234,261,0,240],
[265,279,283,249,250,257,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,222,231,241,223,221,213],
[264,0,255,244,266,235,249,253],
[279,246,0,244,249,236,258,253],
[270,257,257,0,266,271,252,250],
[260,235,252,235,0,267,238,247],
[278,266,265,230,234,0,265,237],
[280,252,243,249,263,236,0,269],
[288,248,248,251,254,264,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,291,292,278,241,230,266],
[253,0,246,253,261,244,259,260],
[210,255,0,269,256,231,264,232],
[209,248,232,0,232,224,244,237],
[223,240,245,269,0,200,242,263],
[260,257,270,277,301,0,260,246],
[271,242,237,257,259,241,0,285],
[235,241,269,264,238,255,216,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,246,260,257,274,251,258],
[245,0,256,277,261,258,263,246],
[255,245,0,260,254,237,255,241],
[241,224,241,0,225,252,245,263],
[244,240,247,276,0,251,247,276],
[227,243,264,249,250,0,259,265],
[250,238,246,256,254,242,0,235],
[243,255,260,238,225,236,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,265,255,236,244,233,273],
[254,0,239,238,251,237,235,243],
[236,262,0,232,233,229,219,246],
[246,263,269,0,286,269,267,235],
[265,250,268,215,0,246,229,229],
[257,264,272,232,255,0,248,263],
[268,266,282,234,272,253,0,233],
[228,258,255,266,272,238,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,263,246,247,266,264,269],
[237,0,241,248,234,247,247,253],
[238,260,0,252,240,256,240,227],
[255,253,249,0,231,252,248,248],
[254,267,261,270,0,259,269,249],
[235,254,245,249,242,0,251,245],
[237,254,261,253,232,250,0,249],
[232,248,274,253,252,256,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,268,248,253,246,231,274],
[272,0,264,235,230,249,249,244],
[233,237,0,226,226,229,227,249],
[253,266,275,0,258,243,250,280],
[248,271,275,243,0,245,258,265],
[255,252,272,258,256,0,229,245],
[270,252,274,251,243,272,0,247],
[227,257,252,221,236,256,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,274,247,264,257,269,263],
[217,0,248,207,242,219,257,241],
[227,253,0,226,253,222,252,241],
[254,294,275,0,272,243,280,251],
[237,259,248,229,0,221,263,245],
[244,282,279,258,280,0,280,248],
[232,244,249,221,238,221,0,228],
[238,260,260,250,256,253,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,299,322,221,270,267,335,278],
[202,0,313,260,310,180,306,266],
[179,188,0,187,219,201,213,235],
[280,241,314,0,317,261,307,249],
[231,191,282,184,0,243,274,247],
[234,321,300,240,258,0,281,297],
[166,195,288,194,227,220,0,270],
[223,235,266,252,254,204,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,258,232,234,240,232,244],
[267,0,264,252,251,257,239,258],
[243,237,0,225,241,246,246,240],
[269,249,276,0,247,252,266,278],
[267,250,260,254,0,243,271,256],
[261,244,255,249,258,0,235,250],
[269,262,255,235,230,266,0,258],
[257,243,261,223,245,251,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,250,241,259,248,254,250],
[248,0,241,248,265,230,253,253],
[251,260,0,258,262,242,252,248],
[260,253,243,0,279,250,262,244],
[242,236,239,222,0,226,249,236],
[253,271,259,251,275,0,264,250],
[247,248,249,239,252,237,0,249],
[251,248,253,257,265,251,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,287,258,284,252,225,252,261],
[214,0,213,258,234,194,235,267],
[243,288,0,267,277,245,255,254],
[217,243,234,0,215,206,196,219],
[249,267,224,286,0,253,261,248],
[276,307,256,295,248,0,243,275],
[249,266,246,305,240,258,0,265],
[240,234,247,282,253,226,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,264,234,245,257,253,238],
[261,0,275,242,260,262,258,248],
[237,226,0,226,231,232,251,234],
[267,259,275,0,247,243,241,252],
[256,241,270,254,0,249,254,250],
[244,239,269,258,252,0,261,251],
[248,243,250,260,247,240,0,235],
[263,253,267,249,251,250,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,209,241,234,268,230,282,283],
[292,0,298,253,297,225,289,289],
[260,203,0,211,279,212,268,228],
[267,248,290,0,282,267,295,264],
[233,204,222,219,0,227,269,227],
[271,276,289,234,274,0,289,266],
[219,212,233,206,232,212,0,221],
[218,212,273,237,274,235,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,180,224,421,279,344,284,368],
[321,0,313,336,338,188,418,448],
[277,188,0,367,249,224,230,373],
[80,165,134,0,329,224,230,373],
[222,163,252,172,0,222,349,294],
[157,313,277,277,279,0,284,359],
[217,83,271,271,152,217,0,271],
[133,53,128,128,207,142,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,182,286,329,172,347,216,227],
[319,0,238,275,276,355,259,292],
[215,263,0,230,236,361,227,261],
[172,226,271,0,169,265,259,228],
[329,225,265,332,0,346,291,225],
[154,146,140,236,155,0,178,222],
[285,242,274,242,210,323,0,313],
[274,209,240,273,276,279,188,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,311,271,307,246,237,280],
[224,0,268,246,287,206,254,251],
[190,233,0,253,276,251,205,240],
[230,255,248,0,250,227,243,281],
[194,214,225,251,0,217,222,210],
[255,295,250,274,284,0,251,268],
[264,247,296,258,279,250,0,297],
[221,250,261,220,291,233,204,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,255,241,242,258,233,247],
[245,0,255,258,242,243,255,247],
[246,246,0,249,246,253,252,249],
[260,243,252,0,257,242,260,237],
[259,259,255,244,0,244,260,240],
[243,258,248,259,257,0,248,254],
[268,246,249,241,241,253,0,244],
[254,254,252,264,261,247,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,256,289,232,238,245,226],
[285,0,257,274,254,242,295,261],
[245,244,0,271,219,244,234,214],
[212,227,230,0,197,234,220,224],
[269,247,282,304,0,276,263,278],
[263,259,257,267,225,0,261,240],
[256,206,267,281,238,240,0,229],
[275,240,287,277,223,261,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,242,244,242,255,235,261],
[251,0,254,245,254,247,242,234],
[259,247,0,239,266,261,243,228],
[257,256,262,0,268,253,249,242],
[259,247,235,233,0,260,234,248],
[246,254,240,248,241,0,224,237],
[266,259,258,252,267,277,0,245],
[240,267,273,259,253,264,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,277,243,254,274,257,278],
[278,0,267,243,257,250,246,246],
[224,234,0,213,244,277,264,251],
[258,258,288,0,286,245,297,267],
[247,244,257,215,0,283,292,272],
[227,251,224,256,218,0,254,245],
[244,255,237,204,209,247,0,221],
[223,255,250,234,229,256,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,258,267,255,250,243,247],
[264,0,262,267,245,255,252,252],
[243,239,0,240,234,247,234,237],
[234,234,261,0,251,241,246,255],
[246,256,267,250,0,246,242,264],
[251,246,254,260,255,0,246,256],
[258,249,267,255,259,255,0,238],
[254,249,264,246,237,245,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,285,197,295,237,181,269,235],
[216,0,209,231,188,173,269,208],
[304,292,0,272,291,269,265,244],
[206,270,229,0,222,173,284,285],
[264,313,210,279,0,241,225,295],
[320,328,232,328,260,0,225,327],
[232,232,236,217,276,276,0,246],
[266,293,257,216,206,174,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,243,247,252,252,252,250],
[253,0,261,231,256,244,225,238],
[258,240,0,238,235,242,235,244],
[254,270,263,0,273,255,259,250],
[249,245,266,228,0,235,236,245],
[249,257,259,246,266,0,241,240],
[249,276,266,242,265,260,0,256],
[251,263,257,251,256,261,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,230,260,243,259,229,261],
[267,0,232,256,266,266,259,267],
[271,269,0,274,275,286,250,264],
[241,245,227,0,260,248,242,247],
[258,235,226,241,0,264,250,255],
[242,235,215,253,237,0,237,252],
[272,242,251,259,251,264,0,252],
[240,234,237,254,246,249,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,249,251,238,243,253,252],
[249,0,254,254,259,246,253,246],
[252,247,0,266,232,241,253,241],
[250,247,235,0,244,239,244,236],
[263,242,269,257,0,243,246,255],
[258,255,260,262,258,0,254,242],
[248,248,248,257,255,247,0,254],
[249,255,260,265,246,259,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,262,268,243,235,252,245],
[238,0,236,253,243,244,244,245],
[239,265,0,236,234,254,245,255],
[233,248,265,0,253,243,234,247],
[258,258,267,248,0,252,247,248],
[266,257,247,258,249,0,254,236],
[249,257,256,267,254,247,0,269],
[256,256,246,254,253,265,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,199,285,315,290,248,332],
[231,0,256,287,304,301,263,309],
[302,245,0,278,303,249,166,292],
[216,214,223,0,304,265,288,243],
[186,197,198,197,0,190,208,255],
[211,200,252,236,311,0,259,264],
[253,238,335,213,293,242,0,257],
[169,192,209,258,246,237,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,251,237,240,246,246,249],
[254,0,259,250,243,245,236,260],
[250,242,0,250,231,242,242,244],
[264,251,251,0,251,234,246,244],
[261,258,270,250,0,246,255,266],
[255,256,259,267,255,0,249,253],
[255,265,259,255,246,252,0,251],
[252,241,257,257,235,248,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,257,240,242,245,243,244],
[249,0,250,228,243,244,240,256],
[244,251,0,230,240,241,260,251],
[261,273,271,0,261,269,262,250],
[259,258,261,240,0,253,247,250],
[256,257,260,232,248,0,248,257],
[258,261,241,239,254,253,0,261],
[257,245,250,251,251,244,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,245,251,244,252,227,247],
[249,0,255,253,256,263,243,266],
[256,246,0,255,242,241,241,244],
[250,248,246,0,246,251,245,252],
[257,245,259,255,0,255,251,262],
[249,238,260,250,246,0,246,244],
[274,258,260,256,250,255,0,243],
[254,235,257,249,239,257,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,240,254,231,250,245,254],
[236,0,234,236,237,237,242,233],
[261,267,0,244,260,250,256,265],
[247,265,257,0,267,252,279,261],
[270,264,241,234,0,259,269,269],
[251,264,251,249,242,0,251,246],
[256,259,245,222,232,250,0,239],
[247,268,236,240,232,255,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,237,236,235,269,255,196],
[247,0,247,273,240,287,272,272],
[264,254,0,241,237,261,255,240],
[265,228,260,0,219,260,255,249],
[266,261,264,282,0,262,311,219],
[232,214,240,241,239,0,252,196],
[246,229,246,246,190,249,0,215],
[305,229,261,252,282,305,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,255,251,270,272,272,248],
[235,0,227,246,235,233,249,241],
[246,274,0,248,258,243,269,260],
[250,255,253,0,243,252,266,254],
[231,266,243,258,0,234,253,251],
[229,268,258,249,267,0,267,249],
[229,252,232,235,248,234,0,226],
[253,260,241,247,250,252,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,303,266,248,273,268,282,301],
[198,0,234,251,254,228,265,293],
[235,267,0,240,232,226,260,300],
[253,250,261,0,263,236,284,257],
[228,247,269,238,0,245,277,300],
[233,273,275,265,256,0,281,293],
[219,236,241,217,224,220,0,287],
[200,208,201,244,201,208,214,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,234,271,249,248,236,251],
[270,0,245,268,267,264,259,256],
[267,256,0,273,241,270,242,239],
[230,233,228,0,245,239,238,239],
[252,234,260,256,0,250,261,250],
[253,237,231,262,251,0,260,237],
[265,242,259,263,240,241,0,250],
[250,245,262,262,251,264,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,229,241,257,242,258,251],
[258,0,186,268,251,242,254,252],
[272,315,0,281,270,249,270,295],
[260,233,220,0,248,260,265,266],
[244,250,231,253,0,227,242,263],
[259,259,252,241,274,0,257,242],
[243,247,231,236,259,244,0,246],
[250,249,206,235,238,259,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,264,247,269,241,271,238],
[254,0,276,269,262,241,275,252],
[237,225,0,233,251,232,258,239],
[254,232,268,0,262,247,267,239],
[232,239,250,239,0,252,259,242],
[260,260,269,254,249,0,249,250],
[230,226,243,234,242,252,0,233],
[263,249,262,262,259,251,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,236,240,217,253,231,232],
[279,0,259,247,255,263,234,270],
[265,242,0,239,227,241,231,232],
[261,254,262,0,257,266,239,280],
[284,246,274,244,0,273,257,273],
[248,238,260,235,228,0,238,255],
[270,267,270,262,244,263,0,256],
[269,231,269,221,228,246,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,245,270,251,256,240,258],
[244,0,237,250,250,247,233,249],
[256,264,0,271,259,262,236,250],
[231,251,230,0,241,234,231,225],
[250,251,242,260,0,234,245,252],
[245,254,239,267,267,0,263,254],
[261,268,265,270,256,238,0,250],
[243,252,251,276,249,247,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,231,243,241,233,235,256],
[259,0,234,248,259,237,238,266],
[270,267,0,258,261,245,263,261],
[258,253,243,0,267,243,261,264],
[260,242,240,234,0,227,246,252],
[268,264,256,258,274,0,249,281],
[266,263,238,240,255,252,0,256],
[245,235,240,237,249,220,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,260,242,248,244,241,261],
[246,0,263,245,273,239,246,256],
[241,238,0,242,242,248,217,236],
[259,256,259,0,263,247,236,247],
[253,228,259,238,0,244,240,236],
[257,262,253,254,257,0,246,246],
[260,255,284,265,261,255,0,241],
[240,245,265,254,265,255,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,241,261,273,271,295,258],
[247,0,268,266,240,261,315,273],
[260,233,0,253,244,267,265,243],
[240,235,248,0,241,287,256,247],
[228,261,257,260,0,280,307,286],
[230,240,234,214,221,0,273,229],
[206,186,236,245,194,228,0,233],
[243,228,258,254,215,272,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,262,247,259,246,247,257],
[241,0,232,256,256,248,247,267],
[239,269,0,275,248,257,232,242],
[254,245,226,0,274,242,266,256],
[242,245,253,227,0,250,248,233],
[255,253,244,259,251,0,253,244],
[254,254,269,235,253,248,0,253],
[244,234,259,245,268,257,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,282,245,202,287,207,258,228],
[219,0,256,227,275,224,245,257],
[256,245,0,222,280,269,232,265],
[299,274,279,0,297,251,248,246],
[214,226,221,204,0,207,254,197],
[294,277,232,250,294,0,279,227],
[243,256,269,253,247,222,0,245],
[273,244,236,255,304,274,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,299,299,310,223,310,338,245],
[202,0,54,184,169,184,158,43],
[202,447,0,130,371,184,371,332],
[191,317,371,0,284,501,284,245],
[278,332,130,217,0,217,256,76],
[191,317,317,0,284,0,284,245],
[163,343,130,217,245,217,0,245],
[256,458,169,256,425,256,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,237,250,242,238,283,258],
[250,0,263,234,240,244,228,254],
[264,238,0,248,257,249,253,249],
[251,267,253,0,257,239,236,267],
[259,261,244,244,0,259,270,254],
[263,257,252,262,242,0,269,266],
[218,273,248,265,231,232,0,234],
[243,247,252,234,247,235,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,249,248,240,238,255,235],
[254,0,248,248,256,265,249,249],
[252,253,0,239,231,259,257,249],
[253,253,262,0,249,242,257,263],
[261,245,270,252,0,264,270,240],
[263,236,242,259,237,0,256,256],
[246,252,244,244,231,245,0,228],
[266,252,252,238,261,245,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,237,241,228,258,242,225],
[267,0,250,263,250,288,239,257],
[264,251,0,195,238,265,258,227],
[260,238,306,0,264,274,246,250],
[273,251,263,237,0,281,243,254],
[243,213,236,227,220,0,206,218],
[259,262,243,255,258,295,0,299],
[276,244,274,251,247,283,202,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,239,261,264,255,257,255],
[233,0,242,253,254,274,258,251],
[262,259,0,280,236,258,282,251],
[240,248,221,0,245,259,285,245],
[237,247,265,256,0,253,247,256],
[246,227,243,242,248,0,274,271],
[244,243,219,216,254,227,0,250],
[246,250,250,256,245,230,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,251,240,261,266,237,262],
[250,0,235,243,246,284,235,244],
[250,266,0,259,257,250,231,261],
[261,258,242,0,249,282,241,251],
[240,255,244,252,0,258,269,239],
[235,217,251,219,243,0,217,211],
[264,266,270,260,232,284,0,243],
[239,257,240,250,262,290,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,230,214,190,251,233,231],
[266,0,298,270,248,278,286,225],
[271,203,0,215,215,254,207,206],
[287,231,286,0,248,305,303,219],
[311,253,286,253,0,308,248,271],
[250,223,247,196,193,0,251,247],
[268,215,294,198,253,250,0,207],
[270,276,295,282,230,254,294,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,226,236,243,253,263,257],
[250,0,252,256,252,236,241,239],
[275,249,0,237,264,252,288,241],
[265,245,264,0,287,255,270,287],
[258,249,237,214,0,241,271,231],
[248,265,249,246,260,0,276,279],
[238,260,213,231,230,225,0,259],
[244,262,260,214,270,222,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,259,255,249,250,260,258],
[253,0,244,259,249,253,243,240],
[242,257,0,255,236,243,243,252],
[246,242,246,0,241,254,249,268],
[252,252,265,260,0,246,256,248],
[251,248,258,247,255,0,246,244],
[241,258,258,252,245,255,0,263],
[243,261,249,233,253,257,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,183,252,247,206,263,231,216],
[318,0,254,295,299,288,244,284],
[249,247,0,254,239,287,249,248],
[254,206,247,0,256,293,261,225],
[295,202,262,245,0,261,247,289],
[238,213,214,208,240,0,218,205],
[270,257,252,240,254,283,0,251],
[285,217,253,276,212,296,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,275,245,256,237,283,282],
[241,0,259,247,233,259,244,249],
[226,242,0,271,239,242,255,243],
[256,254,230,0,233,243,255,258],
[245,268,262,268,0,271,257,257],
[264,242,259,258,230,0,263,250],
[218,257,246,246,244,238,0,250],
[219,252,258,243,244,251,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,244,252,238,251,254,254],
[236,0,234,253,259,251,242,247],
[257,267,0,272,261,250,284,265],
[249,248,229,0,268,247,242,245],
[263,242,240,233,0,246,251,230],
[250,250,251,254,255,0,252,249],
[247,259,217,259,250,249,0,242],
[247,254,236,256,271,252,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,234,227,252,245,257,237],
[265,0,248,253,228,280,274,248],
[267,253,0,233,251,260,252,246],
[274,248,268,0,250,272,270,247],
[249,273,250,251,0,260,239,264],
[256,221,241,229,241,0,274,232],
[244,227,249,231,262,227,0,226],
[264,253,255,254,237,269,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,257,252,258,235,260,246],
[237,0,248,232,250,238,262,253],
[244,253,0,245,269,246,248,240],
[249,269,256,0,274,261,263,246],
[243,251,232,227,0,249,242,237],
[266,263,255,240,252,0,269,235],
[241,239,253,238,259,232,0,245],
[255,248,261,255,264,266,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,293,284,259,271,273,262],
[252,0,281,265,270,264,279,246],
[208,220,0,241,222,245,254,206],
[217,236,260,0,236,244,262,226],
[242,231,279,265,0,253,258,215],
[230,237,256,257,248,0,270,227],
[228,222,247,239,243,231,0,240],
[239,255,295,275,286,274,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,253,227,284,249,330,257],
[287,0,221,272,292,233,282,239],
[248,280,0,267,310,296,317,287],
[274,229,234,0,239,272,269,219],
[217,209,191,262,0,217,226,225],
[252,268,205,229,284,0,292,249],
[171,219,184,232,275,209,0,219],
[244,262,214,282,276,252,282,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,241,255,213,258,249,238],
[277,0,271,249,260,269,282,293],
[260,230,0,254,276,276,292,265],
[246,252,247,0,257,268,252,278],
[288,241,225,244,0,253,256,285],
[243,232,225,233,248,0,249,264],
[252,219,209,249,245,252,0,261],
[263,208,236,223,216,237,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,202,235,235,237,215,252,218],
[299,0,253,246,287,263,255,253],
[266,248,0,263,269,228,250,258],
[266,255,238,0,280,237,276,264],
[264,214,232,221,0,240,222,216],
[286,238,273,264,261,0,277,262],
[249,246,251,225,279,224,0,253],
[283,248,243,237,285,239,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,224,238,241,206,219,213],
[269,0,268,271,245,232,215,255],
[277,233,0,255,211,235,216,231],
[263,230,246,0,214,232,217,251],
[260,256,290,287,0,271,252,232],
[295,269,266,269,230,0,240,241],
[282,286,285,284,249,261,0,275],
[288,246,270,250,269,260,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,259,239,258,259,250,257],
[245,0,256,250,261,246,251,242],
[242,245,0,228,266,241,241,256],
[262,251,273,0,243,248,256,266],
[243,240,235,258,0,256,242,241],
[242,255,260,253,245,0,245,250],
[251,250,260,245,259,256,0,252],
[244,259,245,235,260,251,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,243,258,251,241,250,265],
[241,0,233,243,221,237,237,251],
[258,268,0,250,239,250,251,248],
[243,258,251,0,234,255,254,266],
[250,280,262,267,0,261,272,257],
[260,264,251,246,240,0,240,263],
[251,264,250,247,229,261,0,243],
[236,250,253,235,244,238,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,231,259,247,267,250,243],
[243,0,261,251,235,249,234,251],
[270,240,0,275,246,257,229,255],
[242,250,226,0,249,255,235,250],
[254,266,255,252,0,257,250,247],
[234,252,244,246,244,0,239,260],
[251,267,272,266,251,262,0,233],
[258,250,246,251,254,241,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,235,266,247,245,261,276],
[226,0,223,236,247,252,244,257],
[266,278,0,275,275,243,268,275],
[235,265,226,0,236,243,247,258],
[254,254,226,265,0,223,264,252],
[256,249,258,258,278,0,268,268],
[240,257,233,254,237,233,0,257],
[225,244,226,243,249,233,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,266,248,262,266,256,260],
[247,0,279,248,245,248,258,263],
[235,222,0,219,229,236,247,206],
[253,253,282,0,250,292,265,266],
[239,256,272,251,0,232,243,255],
[235,253,265,209,269,0,242,251],
[245,243,254,236,258,259,0,265],
[241,238,295,235,246,250,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,275,257,260,280,228,282],
[252,0,238,242,272,261,230,251],
[226,263,0,247,250,231,251,264],
[244,259,254,0,266,251,247,252],
[241,229,251,235,0,253,254,236],
[221,240,270,250,248,0,225,229],
[273,271,250,254,247,276,0,260],
[219,250,237,249,265,272,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,241,251,237,253,257,252],
[257,0,250,266,261,256,241,253],
[260,251,0,239,241,243,230,228],
[250,235,262,0,252,249,242,257],
[264,240,260,249,0,266,258,263],
[248,245,258,252,235,0,233,251],
[244,260,271,259,243,268,0,278],
[249,248,273,244,238,250,223,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 501, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_8_501.csv", index=False, header=False)