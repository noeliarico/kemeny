
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,267,271,264,267,237,240,246,248,251,250],
[233,0,250,243,235,235,243,250,241,234,231],
[229,250,0,237,236,229,236,216,235,241,226],
[236,257,263,0,268,257,245,260,263,256,263],
[233,265,264,232,0,220,241,250,236,252,231],
[263,265,271,243,280,0,254,257,264,269,251],
[260,257,264,255,259,246,0,249,255,253,250],
[254,250,284,240,250,243,251,0,255,250,248],
[252,259,265,237,264,236,245,245,0,252,241],
[249,266,259,244,248,231,247,250,248,0,252],
[250,269,274,237,269,249,250,252,259,248,0]])



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
result = np.append(np.array([11, 500, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,240,252,253,256,238,256,264,265,237],
[238,0,238,251,239,253,239,239,253,257,198],
[260,262,0,258,249,244,260,240,256,300,236],
[248,249,242,0,253,240,235,256,259,257,234],
[247,261,251,247,0,263,253,243,241,251,219],
[244,247,256,260,237,0,252,261,280,271,251],
[262,261,240,265,247,248,0,247,263,261,241],
[244,261,260,244,257,239,253,0,257,265,234],
[236,247,244,241,259,220,237,243,0,249,241],
[235,243,200,243,249,229,239,235,251,0,223],
[263,302,264,266,281,249,259,266,259,277,0]])



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
result = np.append(np.array([11, 500, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,383,257,382,283,335,405,317,354,245,271],
[117,0,136,290,147,143,192,163,222,242,173],
[243,364,0,218,241,297,279,281,310,261,359],
[118,210,282,0,214,198,150,179,284,213,250],
[217,353,259,286,0,278,324,277,317,302,228],
[165,357,203,302,222,0,215,203,269,272,270],
[95,308,221,350,176,285,0,263,230,233,359],
[183,337,219,321,223,297,237,0,236,216,299],
[146,278,190,216,183,231,270,264,0,192,203],
[255,258,239,287,198,228,267,284,308,0,258],
[229,327,141,250,272,230,141,201,297,242,0]])



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
result = np.append(np.array([11, 500, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,237,226,258,254,267,257,229,205,264],
[255,0,215,279,226,280,288,263,249,254,263],
[263,285,0,277,243,273,273,255,261,244,234],
[274,221,223,0,261,265,241,263,272,232,216],
[242,274,257,239,0,276,261,240,282,214,266],
[246,220,227,235,224,0,276,247,253,215,236],
[233,212,227,259,239,224,0,242,274,219,219],
[243,237,245,237,260,253,258,0,294,227,230],
[271,251,239,228,218,247,226,206,0,223,224],
[295,246,256,268,286,285,281,273,277,0,248],
[236,237,266,284,234,264,281,270,276,252,0]])



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
result = np.append(np.array([11, 500, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,302,234,219,286,233,253,253,271,238,261],
[198,0,218,221,251,219,184,243,212,192,206],
[266,282,0,241,229,240,167,256,212,240,264],
[281,279,259,0,257,218,267,282,242,265,255],
[214,249,271,243,0,232,195,277,266,242,245],
[267,281,260,282,268,0,161,310,242,221,275],
[247,316,333,233,305,339,0,321,304,303,251],
[247,257,244,218,223,190,179,0,203,248,268],
[229,288,288,258,234,258,196,297,0,236,273],
[262,308,260,235,258,279,197,252,264,0,245],
[239,294,236,245,255,225,249,232,227,255,0]])



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
result = np.append(np.array([11, 500, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,252,237,220,260,259,233,243,229,255],
[264,0,243,258,246,263,287,237,258,255,265],
[248,257,0,268,269,237,256,223,261,298,273],
[263,242,232,0,202,236,262,235,237,239,231],
[280,254,231,298,0,273,296,257,289,257,251],
[240,237,263,264,227,0,249,234,244,230,234],
[241,213,244,238,204,251,0,220,260,236,246],
[267,263,277,265,243,266,280,0,268,260,242],
[257,242,239,263,211,256,240,232,0,224,230],
[271,245,202,261,243,270,264,240,276,0,261],
[245,235,227,269,249,266,254,258,270,239,0]])



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
result = np.append(np.array([11, 500, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,256,254,239,241,291,257,258,275,234],
[279,0,259,270,242,234,268,246,271,248,241],
[244,241,0,259,241,239,269,249,259,265,215],
[246,230,241,0,238,252,271,246,252,256,251],
[261,258,259,262,0,257,286,261,244,273,254],
[259,266,261,248,243,0,267,247,281,277,243],
[209,232,231,229,214,233,0,205,259,240,205],
[243,254,251,254,239,253,295,0,259,280,219],
[242,229,241,248,256,219,241,241,0,248,234],
[225,252,235,244,227,223,260,220,252,0,221],
[266,259,285,249,246,257,295,281,266,279,0]])



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
result = np.append(np.array([11, 500, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,215,204,242,223,231,238,233,240,216],
[282,0,252,239,262,269,268,278,242,279,259],
[285,248,0,273,275,267,271,281,253,279,265],
[296,261,227,0,225,263,252,252,235,253,234],
[258,238,225,275,0,246,261,271,217,267,276],
[277,231,233,237,254,0,224,281,239,293,232],
[269,232,229,248,239,276,0,261,213,253,235],
[262,222,219,248,229,219,239,0,188,262,222],
[267,258,247,265,283,261,287,312,0,271,280],
[260,221,221,247,233,207,247,238,229,0,226],
[284,241,235,266,224,268,265,278,220,274,0]])



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
result = np.append(np.array([11, 500, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,247,201,238,260,238,198,224,249,234],
[262,0,249,217,236,254,244,242,233,242,230],
[253,251,0,219,267,276,238,249,230,252,234],
[299,283,281,0,277,301,304,269,283,250,251],
[262,264,233,223,0,267,241,226,236,230,215],
[240,246,224,199,233,0,254,203,223,215,208],
[262,256,262,196,259,246,0,232,249,242,199],
[302,258,251,231,274,297,268,0,256,239,255],
[276,267,270,217,264,277,251,244,0,240,219],
[251,258,248,250,270,285,258,261,260,0,255],
[266,270,266,249,285,292,301,245,281,245,0]])



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
result = np.append(np.array([11, 500, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,244,258,245,250,248,233,255,249,248],
[249,0,234,232,239,254,243,227,245,248,248],
[256,266,0,248,264,252,258,249,271,269,268],
[242,268,252,0,256,254,238,244,262,251,268],
[255,261,236,244,0,261,231,241,252,261,247],
[250,246,248,246,239,0,239,238,255,256,246],
[252,257,242,262,269,261,0,260,268,253,265],
[267,273,251,256,259,262,240,0,261,251,267],
[245,255,229,238,248,245,232,239,0,248,250],
[251,252,231,249,239,244,247,249,252,0,249],
[252,252,232,232,253,254,235,233,250,251,0]])



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
result = np.append(np.array([11, 500, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,323,289,249,232,240,265,324,300,261],
[222,0,290,246,266,241,219,185,272,201,261],
[177,210,0,245,252,191,204,242,246,239,149],
[211,254,255,0,255,273,212,283,260,286,276],
[251,234,248,245,0,193,243,252,298,229,222],
[268,259,309,227,307,0,238,292,304,225,301],
[260,281,296,288,257,262,0,254,316,262,225],
[235,315,258,217,248,208,246,0,230,255,203],
[176,228,254,240,202,196,184,270,0,264,238],
[200,299,261,214,271,275,238,245,236,0,234],
[239,239,351,224,278,199,275,297,262,266,0]])



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
result = np.append(np.array([11, 500, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,252,260,250,239,265,254,253,254,260],
[265,0,245,252,264,242,256,258,270,251,251],
[248,255,0,277,264,257,259,230,265,245,245],
[240,248,223,0,269,268,258,254,271,220,248],
[250,236,236,231,0,248,257,262,243,245,233],
[261,258,243,232,252,0,254,254,238,242,244],
[235,244,241,242,243,246,0,226,257,244,239],
[246,242,270,246,238,246,274,0,250,258,258],
[247,230,235,229,257,262,243,250,0,233,238],
[246,249,255,280,255,258,256,242,267,0,244],
[240,249,255,252,267,256,261,242,262,256,0]])



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
result = np.append(np.array([11, 500, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,248,221,255,292,309,225,310,294,238],
[271,0,209,249,332,358,266,194,271,296,233],
[252,291,0,242,224,301,193,192,226,273,152],
[279,251,258,0,266,230,294,255,281,223,250],
[245,168,276,234,0,331,287,218,247,213,216],
[208,142,199,270,169,0,196,220,262,197,179],
[191,234,307,206,213,304,0,245,243,251,257],
[275,306,308,245,282,280,255,0,271,312,231],
[190,229,274,219,253,238,257,229,0,291,242],
[206,204,227,277,287,303,249,188,209,0,202],
[262,267,348,250,284,321,243,269,258,298,0]])



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
result = np.append(np.array([11, 500, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,309,293,241,277,248,283,235,338,300],
[216,0,280,283,279,271,229,228,276,320,253],
[191,220,0,268,230,250,209,240,245,304,263],
[207,217,232,0,235,246,233,213,232,271,270],
[259,221,270,265,0,250,200,249,233,304,238],
[223,229,250,254,250,0,231,243,224,276,277],
[252,271,291,267,300,269,0,240,266,298,280],
[217,272,260,287,251,257,260,0,249,296,267],
[265,224,255,268,267,276,234,251,0,273,272],
[162,180,196,229,196,224,202,204,227,0,220],
[200,247,237,230,262,223,220,233,228,280,0]])



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
result = np.append(np.array([11, 500, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,229,221,226,233,293,218,271,252,176],
[260,0,241,254,288,270,295,259,296,275,222],
[271,259,0,295,286,248,312,282,290,280,254],
[279,246,205,0,269,257,266,235,313,329,231],
[274,212,214,231,0,296,297,259,301,316,271],
[267,230,252,243,204,0,295,270,263,251,220],
[207,205,188,234,203,205,0,227,240,208,151],
[282,241,218,265,241,230,273,0,308,253,236],
[229,204,210,187,199,237,260,192,0,274,209],
[248,225,220,171,184,249,292,247,226,0,199],
[324,278,246,269,229,280,349,264,291,301,0]])



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
result = np.append(np.array([11, 500, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,234,253,246,230,223,226,235,236,220],
[265,0,235,280,248,247,237,220,237,228,245],
[266,265,0,266,255,242,247,270,262,268,248],
[247,220,234,0,237,236,248,241,223,258,242],
[254,252,245,263,0,244,261,256,232,268,249],
[270,253,258,264,256,0,274,246,250,260,235],
[277,263,253,252,239,226,0,239,240,275,217],
[274,280,230,259,244,254,261,0,242,262,227],
[265,263,238,277,268,250,260,258,0,260,273],
[264,272,232,242,232,240,225,238,240,0,238],
[280,255,252,258,251,265,283,273,227,262,0]])



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
result = np.append(np.array([11, 500, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,242,239,241,263,235,234,237,251,237],
[259,0,246,231,238,258,226,253,223,261,235],
[258,254,0,236,237,254,228,247,222,266,237],
[261,269,264,0,243,264,209,248,238,263,251],
[259,262,263,257,0,264,246,226,248,269,244],
[237,242,246,236,236,0,223,230,228,256,238],
[265,274,272,291,254,277,0,249,258,277,269],
[266,247,253,252,274,270,251,0,253,258,241],
[263,277,278,262,252,272,242,247,0,279,248],
[249,239,234,237,231,244,223,242,221,0,229],
[263,265,263,249,256,262,231,259,252,271,0]])



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
result = np.append(np.array([11, 500, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,279,242,277,251,272,257,263,265,291],
[237,0,269,233,250,248,247,249,256,259,270],
[221,231,0,230,236,236,244,205,232,230,252],
[258,267,270,0,256,241,281,237,264,242,273],
[223,250,264,244,0,246,256,242,257,242,267],
[249,252,264,259,254,0,270,259,259,239,249],
[228,253,256,219,244,230,0,240,255,229,256],
[243,251,295,263,258,241,260,0,256,252,290],
[237,244,268,236,243,241,245,244,0,230,246],
[235,241,270,258,258,261,271,248,270,0,267],
[209,230,248,227,233,251,244,210,254,233,0]])



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
result = np.append(np.array([11, 500, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,248,247,230,238,265,248,230,283,250],
[263,0,254,266,249,268,270,265,248,281,255],
[252,246,0,259,253,259,261,245,245,295,255],
[253,234,241,0,230,261,277,268,246,274,255],
[270,251,247,270,0,255,286,269,274,288,271],
[262,232,241,239,245,0,265,260,235,280,256],
[235,230,239,223,214,235,0,229,237,263,221],
[252,235,255,232,231,240,271,0,239,264,257],
[270,252,255,254,226,265,263,261,0,296,244],
[217,219,205,226,212,220,237,236,204,0,213],
[250,245,245,245,229,244,279,243,256,287,0]])



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
result = np.append(np.array([11, 500, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,251,246,237,245,255,246,255,256,258],
[274,0,264,255,255,256,247,258,253,265,265],
[249,236,0,248,243,249,253,253,250,255,258],
[254,245,252,0,248,248,260,256,251,264,261],
[263,245,257,252,0,250,263,255,272,268,259],
[255,244,251,252,250,0,249,253,251,249,246],
[245,253,247,240,237,251,0,253,249,259,257],
[254,242,247,244,245,247,247,0,262,263,263],
[245,247,250,249,228,249,251,238,0,246,240],
[244,235,245,236,232,251,241,237,254,0,235],
[242,235,242,239,241,254,243,237,260,265,0]])



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
result = np.append(np.array([11, 500, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,245,253,246,235,218,255,232,243,232],
[276,0,267,250,261,247,250,266,267,260,254],
[255,233,0,224,238,208,201,248,223,249,226],
[247,250,276,0,250,231,235,255,252,258,251],
[254,239,262,250,0,231,225,252,253,259,245],
[265,253,292,269,269,0,243,267,243,264,247],
[282,250,299,265,275,257,0,277,277,288,256],
[245,234,252,245,248,233,223,0,232,242,247],
[268,233,277,248,247,257,223,268,0,275,251],
[257,240,251,242,241,236,212,258,225,0,252],
[268,246,274,249,255,253,244,253,249,248,0]])



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
result = np.append(np.array([11, 500, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,232,258,254,302,302,291,289,282,249],
[244,0,247,233,206,289,263,267,281,286,242],
[268,253,0,243,198,254,275,243,238,278,274],
[242,267,257,0,224,255,246,267,256,242,252],
[246,294,302,276,0,279,302,282,262,250,270],
[198,211,246,245,221,0,242,258,258,233,234],
[198,237,225,254,198,258,0,267,252,246,217],
[209,233,257,233,218,242,233,0,232,226,230],
[211,219,262,244,238,242,248,268,0,239,211],
[218,214,222,258,250,267,254,274,261,0,275],
[251,258,226,248,230,266,283,270,289,225,0]])



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
result = np.append(np.array([11, 500, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,272,257,267,232,244,231,238,235,238],
[244,0,233,248,256,225,260,233,246,226,230],
[228,267,0,267,251,219,252,226,228,224,236],
[243,252,233,0,243,234,248,232,224,233,235],
[233,244,249,257,0,229,243,215,220,222,243],
[268,275,281,266,271,0,250,237,262,265,259],
[256,240,248,252,257,250,0,229,226,236,234],
[269,267,274,268,285,263,271,0,256,234,266],
[262,254,272,276,280,238,274,244,0,276,261],
[265,274,276,267,278,235,264,266,224,0,238],
[262,270,264,265,257,241,266,234,239,262,0]])



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
result = np.append(np.array([11, 500, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,240,232,248,238,230,240,251,225,270],
[262,0,228,269,246,243,244,219,257,256,259],
[260,272,0,255,252,248,242,235,246,249,268],
[268,231,245,0,232,233,228,232,247,237,262],
[252,254,248,268,0,243,248,232,240,244,271],
[262,257,252,267,257,0,250,239,263,253,264],
[270,256,258,272,252,250,0,257,278,270,274],
[260,281,265,268,268,261,243,0,248,253,274],
[249,243,254,253,260,237,222,252,0,253,268],
[275,244,251,263,256,247,230,247,247,0,260],
[230,241,232,238,229,236,226,226,232,240,0]])



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
result = np.append(np.array([11, 500, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,244,244,250,246,211,270,248,235,232],
[263,0,259,236,271,258,237,251,249,233,254],
[256,241,0,240,263,252,208,238,245,239,260],
[256,264,260,0,266,259,243,263,286,254,263],
[250,229,237,234,0,251,233,228,248,227,231],
[254,242,248,241,249,0,250,231,246,249,245],
[289,263,292,257,267,250,0,249,278,247,246],
[230,249,262,237,272,269,251,0,262,260,250],
[252,251,255,214,252,254,222,238,0,249,244],
[265,267,261,246,273,251,253,240,251,0,242],
[268,246,240,237,269,255,254,250,256,258,0]])



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
result = np.append(np.array([11, 500, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,250,270,274,270,250,279,256,235,258],
[233,0,232,223,242,240,227,262,243,240,239],
[250,268,0,249,265,256,260,268,260,246,240],
[230,277,251,0,258,266,244,270,238,226,245],
[226,258,235,242,0,256,227,253,236,249,230],
[230,260,244,234,244,0,241,263,239,225,226],
[250,273,240,256,273,259,0,269,259,251,258],
[221,238,232,230,247,237,231,0,233,242,217],
[244,257,240,262,264,261,241,267,0,240,233],
[265,260,254,274,251,275,249,258,260,0,239],
[242,261,260,255,270,274,242,283,267,261,0]])



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
result = np.append(np.array([11, 500, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,230,264,261,247,256,219,245,263,275],
[246,0,227,255,252,259,246,251,233,245,254],
[270,273,0,265,282,259,253,245,256,270,284],
[236,245,235,0,255,256,264,237,239,253,241],
[239,248,218,245,0,237,250,232,207,239,243],
[253,241,241,244,263,0,252,245,246,260,262],
[244,254,247,236,250,248,0,244,212,241,238],
[281,249,255,263,268,255,256,0,251,269,269],
[255,267,244,261,293,254,288,249,0,255,272],
[237,255,230,247,261,240,259,231,245,0,237],
[225,246,216,259,257,238,262,231,228,263,0]])



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
result = np.append(np.array([11, 500, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,268,249,273,273,242,235,242,258,251],
[261,0,239,263,264,271,293,240,274,259,258],
[232,261,0,260,283,264,244,228,242,235,265],
[251,237,240,0,278,260,252,234,251,274,245],
[227,236,217,222,0,256,245,231,234,229,228],
[227,229,236,240,244,0,236,225,230,256,234],
[258,207,256,248,255,264,0,227,244,244,252],
[265,260,272,266,269,275,273,0,250,263,272],
[258,226,258,249,266,270,256,250,0,261,254],
[242,241,265,226,271,244,256,237,239,0,240],
[249,242,235,255,272,266,248,228,246,260,0]])



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
result = np.append(np.array([11, 500, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,253,245,255,257,223,253,242,247,231],
[262,0,244,255,238,277,252,248,249,259,235],
[247,256,0,239,246,265,247,248,244,267,239],
[255,245,261,0,251,267,235,252,263,261,218],
[245,262,254,249,0,250,244,245,241,252,240],
[243,223,235,233,250,0,250,251,218,254,224],
[277,248,253,265,256,250,0,263,253,283,253],
[247,252,252,248,255,249,237,0,236,252,233],
[258,251,256,237,259,282,247,264,0,263,250],
[253,241,233,239,248,246,217,248,237,0,221],
[269,265,261,282,260,276,247,267,250,279,0]])



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
result = np.append(np.array([11, 500, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,232,276,251,246,254,251,251,255,260],
[257,0,266,278,273,264,272,258,257,243,264],
[268,234,0,271,255,254,285,250,239,246,248],
[224,222,229,0,227,230,248,236,229,228,219],
[249,227,245,273,0,231,261,249,249,241,235],
[254,236,246,270,269,0,269,254,246,251,233],
[246,228,215,252,239,231,0,236,216,254,239],
[249,242,250,264,251,246,264,0,271,250,221],
[249,243,261,271,251,254,284,229,0,260,239],
[245,257,254,272,259,249,246,250,240,0,264],
[240,236,252,281,265,267,261,279,261,236,0]])



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
result = np.append(np.array([11, 500, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,265,277,256,252,256,268,236,243,254],
[256,0,260,273,267,264,273,260,251,243,260],
[235,240,0,239,237,236,214,241,242,216,241],
[223,227,261,0,256,237,262,249,240,234,258],
[244,233,263,244,0,245,254,271,231,248,264],
[248,236,264,263,255,0,261,250,229,250,264],
[244,227,286,238,246,239,0,262,231,241,239],
[232,240,259,251,229,250,238,0,224,226,242],
[264,249,258,260,269,271,269,276,0,255,275],
[257,257,284,266,252,250,259,274,245,0,266],
[246,240,259,242,236,236,261,258,225,234,0]])



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
result = np.append(np.array([11, 500, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,257,261,245,263,250,267,247,222,230],
[228,0,235,249,238,239,230,252,243,225,238],
[243,265,0,251,226,252,241,257,262,233,224],
[239,251,249,0,235,241,234,255,215,231,233],
[255,262,274,265,0,272,256,276,249,232,255],
[237,261,248,259,228,0,240,262,239,221,236],
[250,270,259,266,244,260,0,271,253,235,230],
[233,248,243,245,224,238,229,0,243,206,219],
[253,257,238,285,251,261,247,257,0,255,241],
[278,275,267,269,268,279,265,294,245,0,268],
[270,262,276,267,245,264,270,281,259,232,0]])



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
result = np.append(np.array([11, 500, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,212,190,232,235,252,280,213,204,215,239],
[288,0,258,263,242,245,281,203,241,218,252],
[310,242,0,272,263,267,276,242,225,244,279],
[268,237,228,0,232,255,278,244,246,250,282],
[265,258,237,268,0,223,221,205,234,272,269],
[248,255,233,245,277,0,293,273,259,226,220],
[220,219,224,222,279,207,0,221,187,211,235],
[287,297,258,256,295,227,279,0,214,254,263],
[296,259,275,254,266,241,313,286,0,274,281],
[285,282,256,250,228,274,289,246,226,0,285],
[261,248,221,218,231,280,265,237,219,215,0]])



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
result = np.append(np.array([11, 500, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,288,287,239,238,241,243,259,213,242],
[224,0,258,282,231,231,274,274,265,233,248],
[212,242,0,280,238,226,222,256,250,234,222],
[213,218,220,0,208,231,202,222,241,211,214],
[261,269,262,292,0,241,270,290,269,254,262],
[262,269,274,269,259,0,243,255,281,249,233],
[259,226,278,298,230,257,0,281,257,227,260],
[257,226,244,278,210,245,219,0,246,250,229],
[241,235,250,259,231,219,243,254,0,227,243],
[287,267,266,289,246,251,273,250,273,0,306],
[258,252,278,286,238,267,240,271,257,194,0]])



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
result = np.append(np.array([11, 500, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,254,260,256,234,245,252,251,249,252],
[248,0,264,248,247,256,243,253,248,249,256],
[246,236,0,255,236,235,239,248,251,248,242],
[240,252,245,0,254,240,243,246,236,256,244],
[244,253,264,246,0,247,259,256,242,241,248],
[266,244,265,260,253,0,259,257,261,257,251],
[255,257,261,257,241,241,0,242,250,245,242],
[248,247,252,254,244,243,258,0,236,255,247],
[249,252,249,264,258,239,250,264,0,257,257],
[251,251,252,244,259,243,255,245,243,0,262],
[248,244,258,256,252,249,258,253,243,238,0]])



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
result = np.append(np.array([11, 500, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,353,276,356,265,319,200,332,289,310,256],
[147,0,185,268,113,218,160,227,180,205,121],
[224,315,0,350,167,309,257,274,215,269,213],
[144,232,150,0,180,225,218,179,130,293,158],
[235,387,333,320,0,339,232,321,253,305,258],
[181,282,191,275,161,0,191,233,186,154,107],
[300,340,243,282,268,309,0,269,230,273,238],
[168,273,226,321,179,267,231,0,175,213,211],
[211,320,285,370,247,314,270,325,0,263,219],
[190,295,231,207,195,346,227,287,237,0,166],
[244,379,287,342,242,393,262,289,281,334,0]])



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
result = np.append(np.array([11, 500, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,267,274,272,276,265,262,243,248,282],
[248,0,271,242,250,283,267,269,256,236,254],
[233,229,0,221,253,258,257,251,231,233,221],
[226,258,279,0,254,273,246,256,257,236,243],
[228,250,247,246,0,263,252,242,250,229,239],
[224,217,242,227,237,0,240,236,228,226,227],
[235,233,243,254,248,260,0,230,246,243,243],
[238,231,249,244,258,264,270,0,234,242,251],
[257,244,269,243,250,272,254,266,0,256,256],
[252,264,267,264,271,274,257,258,244,0,259],
[218,246,279,257,261,273,257,249,244,241,0]])



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
result = np.append(np.array([11, 500, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,234,249,247,228,233,279,220,233,217],
[251,0,265,235,236,249,272,242,241,221,252],
[266,235,0,259,236,251,233,273,234,254,243],
[251,265,241,0,221,249,249,253,245,231,241],
[253,264,264,279,0,243,274,289,263,244,267],
[272,251,249,251,257,0,273,282,236,246,257],
[267,228,267,251,226,227,0,268,233,224,236],
[221,258,227,247,211,218,232,0,257,230,225],
[280,259,266,255,237,264,267,243,0,253,244],
[267,279,246,269,256,254,276,270,247,0,248],
[283,248,257,259,233,243,264,275,256,252,0]])



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
result = np.append(np.array([11, 500, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,258,264,261,244,248,264,254,270,255],
[259,0,246,254,252,264,274,264,264,276,241],
[242,254,0,258,272,275,256,277,263,268,261],
[236,246,242,0,248,246,253,259,249,264,249],
[239,248,228,252,0,249,231,272,250,258,235],
[256,236,225,254,251,0,256,260,241,270,238],
[252,226,244,247,269,244,0,274,250,256,247],
[236,236,223,241,228,240,226,0,229,256,229],
[246,236,237,251,250,259,250,271,0,266,251],
[230,224,232,236,242,230,244,244,234,0,224],
[245,259,239,251,265,262,253,271,249,276,0]])



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
result = np.append(np.array([11, 500, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,229,206,268,254,223,280,297,229,245,310],
[271,0,231,225,184,199,207,235,224,192,266],
[294,269,0,261,225,257,260,281,265,245,282],
[232,275,239,0,242,248,217,227,201,207,250],
[246,316,275,258,0,255,284,309,245,261,276],
[277,301,243,252,245,0,265,285,266,244,240],
[220,293,240,283,216,235,0,264,258,220,227],
[203,265,219,273,191,215,236,0,223,228,260],
[271,276,235,299,255,234,242,277,0,228,253],
[255,308,255,293,239,256,280,272,272,0,250],
[190,234,218,250,224,260,273,240,247,250,0]])



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
result = np.append(np.array([11, 500, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,283,268,310,197,220,168,261,178,210,259],
[217,0,331,240,237,281,280,282,214,238,249],
[232,169,0,284,164,195,212,219,153,212,214],
[190,260,216,0,240,245,240,260,195,202,238],
[303,263,336,260,0,220,219,267,252,226,227],
[280,219,305,255,280,0,246,178,238,227,211],
[332,220,288,260,281,254,0,209,207,271,231],
[239,218,281,240,233,322,291,0,240,192,261],
[322,286,347,305,248,262,293,260,0,288,249],
[290,262,288,298,274,273,229,308,212,0,268],
[241,251,286,262,273,289,269,239,251,232,0]])



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
result = np.append(np.array([11, 500, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,276,265,270,255,257,255,271,264,250],
[239,0,260,260,264,262,265,249,276,261,254],
[224,240,0,245,251,246,242,235,253,232,236],
[235,240,255,0,253,241,243,238,264,244,231],
[230,236,249,247,0,231,227,233,250,234,251],
[245,238,254,259,269,0,253,271,276,240,256],
[243,235,258,257,273,247,0,238,276,250,252],
[245,251,265,262,267,229,262,0,270,253,252],
[229,224,247,236,250,224,224,230,0,221,243],
[236,239,268,256,266,260,250,247,279,0,257],
[250,246,264,269,249,244,248,248,257,243,0]])



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
result = np.append(np.array([11, 500, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,200,77,292,279,200,292,399,169,279,63],
[300,0,314,272,363,194,300,314,300,486,300],
[423,186,0,335,322,380,428,336,365,380,380],
[208,228,165,0,228,165,165,165,271,394,208],
[221,137,178,272,0,195,286,243,149,437,221],
[300,306,120,335,305,0,365,213,149,486,270],
[208,200,72,335,214,135,0,213,164,394,178],
[101,186,164,335,257,287,287,0,270,380,164],
[331,200,135,229,351,351,336,230,0,394,178],
[221,14,120,106,63,14,106,120,106,0,207],
[437,200,120,292,279,230,322,336,322,293,0]])



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
result = np.append(np.array([11, 500, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,260,257,263,249,265,259,279,267,258],
[245,0,286,253,239,257,250,231,258,271,255],
[240,214,0,241,249,233,264,238,239,260,244],
[243,247,259,0,251,241,248,244,241,254,250],
[237,261,251,249,0,228,244,228,249,249,240],
[251,243,267,259,272,0,258,250,253,262,252],
[235,250,236,252,256,242,0,239,242,258,256],
[241,269,262,256,272,250,261,0,260,264,264],
[221,242,261,259,251,247,258,240,0,247,244],
[233,229,240,246,251,238,242,236,253,0,249],
[242,245,256,250,260,248,244,236,256,251,0]])



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
result = np.append(np.array([11, 500, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,243,236,237,250,265,252,243,251,243],
[246,0,237,245,227,262,285,226,221,256,232],
[257,263,0,224,228,252,269,229,251,239,249],
[264,255,276,0,250,263,304,283,266,264,246],
[263,273,272,250,0,269,294,264,247,263,250],
[250,238,248,237,231,0,278,259,235,244,243],
[235,215,231,196,206,222,0,233,227,227,211],
[248,274,271,217,236,241,267,0,242,270,248],
[257,279,249,234,253,265,273,258,0,267,261],
[249,244,261,236,237,256,273,230,233,0,250],
[257,268,251,254,250,257,289,252,239,250,0]])



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
result = np.append(np.array([11, 500, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,271,245,267,259,259,266,264,237,241],
[268,0,257,258,262,261,264,269,255,252,242],
[229,243,0,246,257,273,257,264,251,239,238],
[255,242,254,0,269,268,255,263,258,235,244],
[233,238,243,231,0,260,245,241,250,228,244],
[241,239,227,232,240,0,247,253,238,236,250],
[241,236,243,245,255,253,0,242,257,243,243],
[234,231,236,237,259,247,258,0,253,221,236],
[236,245,249,242,250,262,243,247,0,246,240],
[263,248,261,265,272,264,257,279,254,0,252],
[259,258,262,256,256,250,257,264,260,248,0]])



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
result = np.append(np.array([11, 500, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,247,234,229,240,236,259,237,255,251],
[263,0,253,250,252,246,255,260,254,257,261],
[253,247,0,235,240,240,241,246,258,253,257],
[266,250,265,0,248,259,264,256,254,262,275],
[271,248,260,252,0,255,251,266,249,260,266],
[260,254,260,241,245,0,252,272,253,261,260],
[264,245,259,236,249,248,0,268,244,257,268],
[241,240,254,244,234,228,232,0,249,253,268],
[263,246,242,246,251,247,256,251,0,261,255],
[245,243,247,238,240,239,243,247,239,0,251],
[249,239,243,225,234,240,232,232,245,249,0]])



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
result = np.append(np.array([11, 500, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,313,362,358,231,156,297,231,170,310,205],
[187,0,356,264,144,196,210,223,193,224,64],
[138,144,0,145,182,137,123,234,157,160,88],
[142,236,355,0,280,141,173,226,210,320,256],
[269,356,318,220,0,157,274,294,228,304,279],
[344,304,363,359,343,0,323,344,216,382,267],
[203,290,377,327,226,177,0,244,184,281,239],
[269,277,266,274,206,156,256,0,210,260,200],
[330,307,343,290,272,284,316,290,0,296,209],
[190,276,340,180,196,118,219,240,204,0,161],
[295,436,412,244,221,233,261,300,291,339,0]])



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
result = np.append(np.array([11, 500, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,257,222,228,246,233,216,228,239,212],
[251,0,234,214,252,232,238,218,248,220,224],
[243,266,0,233,228,230,230,235,247,223,231],
[278,286,267,0,253,265,259,256,268,254,244],
[272,248,272,247,0,260,258,246,256,250,230],
[254,268,270,235,240,0,250,220,254,233,235],
[267,262,270,241,242,250,0,244,263,254,241],
[284,282,265,244,254,280,256,0,267,249,251],
[272,252,253,232,244,246,237,233,0,231,234],
[261,280,277,246,250,267,246,251,269,0,243],
[288,276,269,256,270,265,259,249,266,257,0]])



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
result = np.append(np.array([11, 500, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,228,259,247,234,241,237,244,237,261],
[260,0,274,248,273,252,247,268,262,233,264],
[272,226,0,253,255,254,253,260,262,237,272],
[241,252,247,0,250,246,232,245,248,233,261],
[253,227,245,250,0,252,236,238,262,239,252],
[266,248,246,254,248,0,256,265,261,249,257],
[259,253,247,268,264,244,0,255,268,243,274],
[263,232,240,255,262,235,245,0,254,262,261],
[256,238,238,252,238,239,232,246,0,238,243],
[263,267,263,267,261,251,257,238,262,0,262],
[239,236,228,239,248,243,226,239,257,238,0]])



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
result = np.append(np.array([11, 500, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,254,260,257,260,244,254,263,277,258],
[267,0,270,265,255,244,253,239,253,261,241],
[246,230,0,252,254,252,246,248,252,250,245],
[240,235,248,0,243,238,223,227,248,261,241],
[243,245,246,257,0,244,239,246,256,258,236],
[240,256,248,262,256,0,250,243,261,259,243],
[256,247,254,277,261,250,0,250,259,257,254],
[246,261,252,273,254,257,250,0,269,261,243],
[237,247,248,252,244,239,241,231,0,248,244],
[223,239,250,239,242,241,243,239,252,0,243],
[242,259,255,259,264,257,246,257,256,257,0]])



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
result = np.append(np.array([11, 500, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,232,220,222,221,211,226,238,253,226],
[274,0,260,247,234,249,244,251,239,276,272],
[268,240,0,245,239,244,241,251,263,260,263],
[280,253,255,0,267,259,244,280,258,281,273],
[278,266,261,233,0,278,262,274,262,281,275],
[279,251,256,241,222,0,256,262,237,275,257],
[289,256,259,256,238,244,0,265,245,278,259],
[274,249,249,220,226,238,235,0,259,285,253],
[262,261,237,242,238,263,255,241,0,288,263],
[247,224,240,219,219,225,222,215,212,0,237],
[274,228,237,227,225,243,241,247,237,263,0]])



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
result = np.append(np.array([11, 500, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,251,260,263,229,250,288,260,251,256],
[243,0,260,281,260,246,301,300,305,262,299],
[249,240,0,290,218,242,247,244,251,245,230],
[240,219,210,0,219,222,237,256,216,225,246],
[237,240,282,281,0,249,283,263,294,271,267],
[271,254,258,278,251,0,274,287,253,246,254],
[250,199,253,263,217,226,0,271,265,260,257],
[212,200,256,244,237,213,229,0,269,200,224],
[240,195,249,284,206,247,235,231,0,222,280],
[249,238,255,275,229,254,240,300,278,0,253],
[244,201,270,254,233,246,243,276,220,247,0]])



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
result = np.append(np.array([11, 500, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,261,246,257,249,238,230,253,260,251],
[246,0,251,252,246,228,225,239,245,250,247],
[239,249,0,245,247,250,252,235,242,259,235],
[254,248,255,0,264,233,231,260,248,258,253],
[243,254,253,236,0,239,235,240,243,257,248],
[251,272,250,267,261,0,241,240,255,260,261],
[262,275,248,269,265,259,0,258,253,271,261],
[270,261,265,240,260,260,242,0,260,263,265],
[247,255,258,252,257,245,247,240,0,252,250],
[240,250,241,242,243,240,229,237,248,0,233],
[249,253,265,247,252,239,239,235,250,267,0]])



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
result = np.append(np.array([11, 500, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,251,253,266,258,251,264,267,243,275],
[245,0,247,248,222,250,239,241,243,257,257],
[249,253,0,256,243,253,242,252,247,250,251],
[247,252,244,0,228,262,240,235,258,239,249],
[234,278,257,272,0,267,263,255,263,255,267],
[242,250,247,238,233,0,257,229,255,244,262],
[249,261,258,260,237,243,0,249,259,244,251],
[236,259,248,265,245,271,251,0,250,255,256],
[233,257,253,242,237,245,241,250,0,243,248],
[257,243,250,261,245,256,256,245,257,0,258],
[225,243,249,251,233,238,249,244,252,242,0]])



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
result = np.append(np.array([11, 500, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,259,226,248,252,246,253,239,274,245],
[249,0,247,252,250,244,240,246,247,261,253],
[241,253,0,234,247,228,245,250,245,262,254],
[274,248,266,0,248,237,252,271,267,277,261],
[252,250,253,252,0,248,251,261,252,275,257],
[248,256,272,263,252,0,249,264,263,279,257],
[254,260,255,248,249,251,0,259,254,265,261],
[247,254,250,229,239,236,241,0,226,262,248],
[261,253,255,233,248,237,246,274,0,269,243],
[226,239,238,223,225,221,235,238,231,0,243],
[255,247,246,239,243,243,239,252,257,257,0]])



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
result = np.append(np.array([11, 500, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,264,256,259,259,255,246,252,263,260],
[250,0,235,226,240,245,261,242,240,244,246],
[236,265,0,242,263,245,275,245,250,259,263],
[244,274,258,0,261,274,269,249,258,259,276],
[241,260,237,239,0,243,249,235,260,244,249],
[241,255,255,226,257,0,265,233,259,256,261],
[245,239,225,231,251,235,0,238,243,232,257],
[254,258,255,251,265,267,262,0,262,246,266],
[248,260,250,242,240,241,257,238,0,265,252],
[237,256,241,241,256,244,268,254,235,0,257],
[240,254,237,224,251,239,243,234,248,243,0]])



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
result = np.append(np.array([11, 500, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,258,257,249,246,257,269,270,255,260],
[226,0,235,253,219,221,246,259,256,239,242],
[242,265,0,266,251,269,259,274,269,237,265],
[243,247,234,0,222,247,247,257,258,249,242],
[251,281,249,278,0,254,260,289,269,267,264],
[254,279,231,253,246,0,265,278,254,251,269],
[243,254,241,253,240,235,0,267,264,242,260],
[231,241,226,243,211,222,233,0,246,240,236],
[230,244,231,242,231,246,236,254,0,246,244],
[245,261,263,251,233,249,258,260,254,0,252],
[240,258,235,258,236,231,240,264,256,248,0]])



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
result = np.append(np.array([11, 500, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,247,237,249,271,240,265,236,246,236],
[262,0,261,275,260,256,255,266,263,239,254],
[253,239,0,231,216,234,242,255,236,224,237],
[263,225,269,0,234,251,251,254,249,235,262],
[251,240,284,266,0,248,242,250,253,251,259],
[229,244,266,249,252,0,258,274,253,225,235],
[260,245,258,249,258,242,0,261,260,233,238],
[235,234,245,246,250,226,239,0,216,210,253],
[264,237,264,251,247,247,240,284,0,238,244],
[254,261,276,265,249,275,267,290,262,0,266],
[264,246,263,238,241,265,262,247,256,234,0]])



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
result = np.append(np.array([11, 500, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,201,259,294,267,277,272,249,249,210,324],
[299,0,208,279,298,361,254,296,333,232,297],
[241,292,0,227,266,284,238,254,205,251,191],
[206,221,273,0,231,310,243,177,186,141,267],
[233,202,234,269,0,291,198,195,191,220,201],
[223,139,216,190,209,0,162,156,176,108,237],
[228,246,262,257,302,338,0,223,163,222,261],
[251,204,246,323,305,344,277,0,248,205,319],
[251,167,295,314,309,324,337,252,0,240,257],
[290,268,249,359,280,392,278,295,260,0,306],
[176,203,309,233,299,263,239,181,243,194,0]])



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
result = np.append(np.array([11, 500, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,272,260,255,237,242,250,254,243,256],
[243,0,280,259,247,234,249,230,264,250,245],
[228,220,0,263,237,230,237,226,241,240,237],
[240,241,237,0,247,221,243,241,252,243,243],
[245,253,263,253,0,227,250,241,263,245,242],
[263,266,270,279,273,0,271,243,254,251,235],
[258,251,263,257,250,229,0,237,263,244,246],
[250,270,274,259,259,257,263,0,263,248,253],
[246,236,259,248,237,246,237,237,0,233,235],
[257,250,260,257,255,249,256,252,267,0,250],
[244,255,263,257,258,265,254,247,265,250,0]])



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
result = np.append(np.array([11, 500, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,250,257,264,243,257,258,271,262,251],
[268,0,264,254,274,250,257,255,277,270,252],
[250,236,0,248,247,250,265,252,261,250,261],
[243,246,252,0,264,239,243,233,261,237,242],
[236,226,253,236,0,219,247,232,262,228,245],
[257,250,250,261,281,0,260,240,257,253,248],
[243,243,235,257,253,240,0,231,251,249,243],
[242,245,248,267,268,260,269,0,263,247,243],
[229,223,239,239,238,243,249,237,0,241,251],
[238,230,250,263,272,247,251,253,259,0,248],
[249,248,239,258,255,252,257,257,249,252,0]])



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
result = np.append(np.array([11, 500, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,215,213,220,286,206,239,302,288,300],
[265,0,226,224,304,265,240,228,325,325,325],
[285,274,0,248,278,305,255,253,303,323,344],
[287,276,252,0,253,275,238,277,295,268,274],
[280,196,222,247,0,222,215,212,295,296,280],
[214,235,195,225,278,0,199,223,298,292,266],
[294,260,245,262,285,301,0,238,344,299,326],
[261,272,247,223,288,277,262,0,337,256,264],
[198,175,197,205,205,202,156,163,0,225,242],
[212,175,177,232,204,208,201,244,275,0,291],
[200,175,156,226,220,234,174,236,258,209,0]])



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
result = np.append(np.array([11, 500, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,254,250,245,246,241,243,238,245,249],
[251,0,242,260,254,264,236,252,257,251,238],
[246,258,0,241,252,264,240,249,240,260,263],
[250,240,259,0,245,257,253,250,234,259,261],
[255,246,248,255,0,254,231,246,241,257,251],
[254,236,236,243,246,0,223,247,240,225,240],
[259,264,260,247,269,277,0,250,249,253,254],
[257,248,251,250,254,253,250,0,260,273,242],
[262,243,260,266,259,260,251,240,0,240,251],
[255,249,240,241,243,275,247,227,260,0,259],
[251,262,237,239,249,260,246,258,249,241,0]])



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
result = np.append(np.array([11, 500, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,247,245,257,260,242,266,233,240,255],
[249,0,234,229,231,270,225,242,233,222,250],
[253,266,0,251,257,280,254,261,263,249,274],
[255,271,249,0,257,263,263,256,266,240,280],
[243,269,243,243,0,251,227,253,251,235,252],
[240,230,220,237,249,0,229,248,235,249,239],
[258,275,246,237,273,271,0,282,279,255,272],
[234,258,239,244,247,252,218,0,242,234,250],
[267,267,237,234,249,265,221,258,0,233,240],
[260,278,251,260,265,251,245,266,267,0,260],
[245,250,226,220,248,261,228,250,260,240,0]])



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
result = np.append(np.array([11, 500, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,257,264,212,200,243,242,235,229,266],
[259,0,225,297,229,265,249,259,249,276,252],
[243,275,0,289,218,272,296,297,254,292,274],
[236,203,211,0,187,208,211,223,201,252,245],
[288,271,282,313,0,241,255,280,287,286,292],
[300,235,228,292,259,0,212,246,249,276,238],
[257,251,204,289,245,288,0,255,263,275,275],
[258,241,203,277,220,254,245,0,235,268,249],
[265,251,246,299,213,251,237,265,0,275,253],
[271,224,208,248,214,224,225,232,225,0,240],
[234,248,226,255,208,262,225,251,247,260,0]])



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
result = np.append(np.array([11, 500, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,266,240,254,264,265,256,265,253,269],
[235,0,257,226,249,243,254,249,250,248,255],
[234,243,0,230,248,230,261,237,251,245,257],
[260,274,270,0,259,248,278,257,269,259,259],
[246,251,252,241,0,260,247,241,262,258,259],
[236,257,270,252,240,0,261,247,257,255,264],
[235,246,239,222,253,239,0,233,237,235,244],
[244,251,263,243,259,253,267,0,252,252,254],
[235,250,249,231,238,243,263,248,0,240,258],
[247,252,255,241,242,245,265,248,260,0,255],
[231,245,243,241,241,236,256,246,242,245,0]])



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
result = np.append(np.array([11, 500, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,252,245,255,219,233,237,229,234,231],
[281,0,258,275,237,255,255,261,270,285,227],
[248,242,0,278,253,236,250,280,263,265,232],
[255,225,222,0,230,207,197,236,206,218,207],
[245,263,247,270,0,216,262,268,237,264,250],
[281,245,264,293,284,0,278,260,268,268,240],
[267,245,250,303,238,222,0,273,262,306,251],
[263,239,220,264,232,240,227,0,233,237,213],
[271,230,237,294,263,232,238,267,0,243,252],
[266,215,235,282,236,232,194,263,257,0,248],
[269,273,268,293,250,260,249,287,248,252,0]])



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
result = np.append(np.array([11, 500, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,216,229,261,258,203,220,225,248,244],
[259,0,249,266,240,242,257,245,241,256,233],
[284,251,0,258,278,273,231,235,239,284,263],
[271,234,242,0,248,244,251,255,251,279,241],
[239,260,222,252,0,241,215,233,254,256,246],
[242,258,227,256,259,0,217,255,246,262,226],
[297,243,269,249,285,283,0,280,272,255,238],
[280,255,265,245,267,245,220,0,261,279,229],
[275,259,261,249,246,254,228,239,0,271,245],
[252,244,216,221,244,238,245,221,229,0,246],
[256,267,237,259,254,274,262,271,255,254,0]])



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
result = np.append(np.array([11, 500, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,214,240,242,219,220,230,221,223,227,232],
[286,0,255,267,252,251,251,247,257,240,262],
[260,245,0,255,246,221,259,234,242,230,241],
[258,233,245,0,253,214,239,240,252,222,238],
[281,248,254,247,0,249,245,247,235,245,255],
[280,249,279,286,251,0,264,257,254,248,234],
[270,249,241,261,255,236,0,237,251,242,244],
[279,253,266,260,253,243,263,0,274,256,262],
[277,243,258,248,265,246,249,226,0,252,239],
[273,260,270,278,255,252,258,244,248,0,263],
[268,238,259,262,245,266,256,238,261,237,0]])



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
result = np.append(np.array([11, 500, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,248,256,251,229,237,264,227,233,263],
[261,0,241,249,275,270,235,264,253,230,278],
[252,259,0,237,222,236,216,257,228,230,271],
[244,251,263,0,247,268,259,275,265,244,255],
[249,225,278,253,0,256,236,260,243,225,267],
[271,230,264,232,244,0,247,272,246,222,258],
[263,265,284,241,264,253,0,282,254,270,250],
[236,236,243,225,240,228,218,0,223,224,262],
[273,247,272,235,257,254,246,277,0,254,269],
[267,270,270,256,275,278,230,276,246,0,252],
[237,222,229,245,233,242,250,238,231,248,0]])



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
result = np.append(np.array([11, 500, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,245,273,264,269,247,264,249,251,255],
[240,0,237,245,255,243,236,245,232,245,230],
[255,263,0,253,257,251,250,269,246,245,251],
[227,255,247,0,242,236,226,254,233,239,229],
[236,245,243,258,0,241,241,243,229,239,237],
[231,257,249,264,259,0,234,248,250,248,237],
[253,264,250,274,259,266,0,265,250,244,242],
[236,255,231,246,257,252,235,0,241,234,256],
[251,268,254,267,271,250,250,259,0,251,242],
[249,255,255,261,261,252,256,266,249,0,250],
[245,270,249,271,263,263,258,244,258,250,0]])



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
result = np.append(np.array([11, 500, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,255,256,257,240,266,256,275,258,264],
[240,0,246,247,240,254,258,255,259,233,254],
[245,254,0,286,251,255,268,253,268,256,276],
[244,253,214,0,234,246,244,249,250,223,259],
[243,260,249,266,0,252,266,255,279,238,266],
[260,246,245,254,248,0,255,246,256,242,251],
[234,242,232,256,234,245,0,245,251,233,257],
[244,245,247,251,245,254,255,0,256,236,247],
[225,241,232,250,221,244,249,244,0,249,251],
[242,267,244,277,262,258,267,264,251,0,242],
[236,246,224,241,234,249,243,253,249,258,0]])



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
result = np.append(np.array([11, 500, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,253,244,279,283,246,229,252,248,277],
[222,0,244,241,260,254,237,212,239,224,272],
[247,256,0,251,256,256,226,208,242,225,240],
[256,259,249,0,266,253,254,249,254,244,263],
[221,240,244,234,0,245,229,217,219,248,269],
[217,246,244,247,255,0,213,228,223,232,266],
[254,263,274,246,271,287,0,255,258,255,271],
[271,288,292,251,283,272,245,0,284,259,284],
[248,261,258,246,281,277,242,216,0,253,271],
[252,276,275,256,252,268,245,241,247,0,284],
[223,228,260,237,231,234,229,216,229,216,0]])



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
result = np.append(np.array([11, 500, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,257,263,242,261,253,254,258,260,249],
[245,0,252,270,243,255,252,245,259,244,258],
[243,248,0,263,257,265,266,245,251,266,252],
[237,230,237,0,229,246,247,230,251,246,248],
[258,257,243,271,0,262,262,239,261,246,255],
[239,245,235,254,238,0,249,245,243,237,245],
[247,248,234,253,238,251,0,246,248,256,260],
[246,255,255,270,261,255,254,0,256,245,237],
[242,241,249,249,239,257,252,244,0,242,251],
[240,256,234,254,254,263,244,255,258,0,245],
[251,242,248,252,245,255,240,263,249,255,0]])



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
result = np.append(np.array([11, 500, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,235,302,244,276,269,269,274,265,284],
[243,0,251,270,258,280,249,268,261,272,284],
[265,249,0,282,256,281,256,275,269,281,300],
[198,230,218,0,245,231,232,249,238,255,279],
[256,242,244,255,0,264,234,281,275,272,265],
[224,220,219,269,236,0,229,265,251,243,255],
[231,251,244,268,266,271,0,248,270,266,269],
[231,232,225,251,219,235,252,0,250,262,270],
[226,239,231,262,225,249,230,250,0,249,267],
[235,228,219,245,228,257,234,238,251,0,245],
[216,216,200,221,235,245,231,230,233,255,0]])



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
result = np.append(np.array([11, 500, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,261,260,246,236,249,265,256,257,262],
[251,0,267,244,238,251,237,253,234,251,278],
[239,233,0,247,242,244,235,247,238,224,252],
[240,256,253,0,238,236,234,248,234,238,269],
[254,262,258,262,0,255,253,256,242,247,271],
[264,249,256,264,245,0,241,277,267,261,268],
[251,263,265,266,247,259,0,264,255,260,273],
[235,247,253,252,244,223,236,0,241,234,255],
[244,266,262,266,258,233,245,259,0,252,256],
[243,249,276,262,253,239,240,266,248,0,282],
[238,222,248,231,229,232,227,245,244,218,0]])



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
result = np.append(np.array([11, 500, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,258,257,230,256,233,239,250,257,234],
[279,0,267,269,263,270,261,237,254,274,276],
[242,233,0,250,253,261,211,236,250,257,258],
[243,231,250,0,257,240,237,238,235,281,263],
[270,237,247,243,0,262,231,254,258,264,266],
[244,230,239,260,238,0,234,249,233,277,278],
[267,239,289,263,269,266,0,253,252,284,273],
[261,263,264,262,246,251,247,0,252,256,266],
[250,246,250,265,242,267,248,248,0,261,274],
[243,226,243,219,236,223,216,244,239,0,248],
[266,224,242,237,234,222,227,234,226,252,0]])



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
result = np.append(np.array([11, 500, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,253,220,230,238,232,243,246,243,220],
[281,0,266,233,239,254,244,253,274,269,226],
[247,234,0,207,246,254,223,222,252,258,212],
[280,267,293,0,265,304,248,273,282,287,248],
[270,261,254,235,0,244,250,244,263,255,257],
[262,246,246,196,256,0,225,232,249,244,226],
[268,256,277,252,250,275,0,253,279,278,239],
[257,247,278,227,256,268,247,0,272,261,230],
[254,226,248,218,237,251,221,228,0,256,197],
[257,231,242,213,245,256,222,239,244,0,223],
[280,274,288,252,243,274,261,270,303,277,0]])



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
result = np.append(np.array([11, 500, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,294,259,252,282,265,260,238,235,254,275],
[206,0,245,261,250,218,243,222,259,227,244],
[241,255,0,263,283,242,262,240,288,273,271],
[248,239,237,0,259,265,263,234,248,256,276],
[218,250,217,241,0,258,277,244,236,244,257],
[235,282,258,235,242,0,269,264,238,273,246],
[240,257,238,237,223,231,0,224,243,250,231],
[262,278,260,266,256,236,276,0,277,260,247],
[265,241,212,252,264,262,257,223,0,262,257],
[246,273,227,244,256,227,250,240,238,0,246],
[225,256,229,224,243,254,269,253,243,254,0]])



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
result = np.append(np.array([11, 500, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,230,242,226,243,241,235,222,243,253],
[268,0,268,259,253,263,243,258,260,255,267],
[270,232,0,265,238,239,247,236,250,261,264],
[258,241,235,0,232,251,246,243,238,247,248],
[274,247,262,268,0,266,234,252,253,273,266],
[257,237,261,249,234,0,241,243,243,248,254],
[259,257,253,254,266,259,0,249,256,267,255],
[265,242,264,257,248,257,251,0,252,267,259],
[278,240,250,262,247,257,244,248,0,263,259],
[257,245,239,253,227,252,233,233,237,0,265],
[247,233,236,252,234,246,245,241,241,235,0]])



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
result = np.append(np.array([11, 500, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,500,247,500,462,247,462,462,462,247],
[38,0,38,0,38,285,247,253,215,215,38],
[0,462,0,0,462,462,247,462,462,462,0],
[253,500,500,0,500,500,247,500,462,500,253],
[0,462,38,0,0,462,247,215,215,215,0],
[38,215,38,0,38,0,247,253,215,215,38],
[253,253,253,253,253,253,0,253,215,253,253],
[38,247,38,0,285,247,247,0,215,215,0],
[38,285,38,38,285,285,285,285,0,253,38],
[38,285,38,0,285,285,247,285,247,0,38],
[253,462,500,247,500,462,247,500,462,462,0]])



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
result = np.append(np.array([11, 500, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,279,242,257,273,271,267,249,238,231],
[229,0,223,238,210,248,230,238,213,203,225],
[221,277,0,233,233,253,248,239,240,220,232],
[258,262,267,0,258,244,267,253,255,257,224],
[243,290,267,242,0,286,251,246,249,217,244],
[227,252,247,256,214,0,245,222,236,214,204],
[229,270,252,233,249,255,0,250,247,210,236],
[233,262,261,247,254,278,250,0,251,226,246],
[251,287,260,245,251,264,253,249,0,249,245],
[262,297,280,243,283,286,290,274,251,0,278],
[269,275,268,276,256,296,264,254,255,222,0]])



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
result = np.append(np.array([11, 500, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,279,277,257,276,285,249,254,246,261,260],
[221,0,247,234,241,241,258,248,215,230,238],
[223,253,0,243,251,239,244,249,213,253,246],
[243,266,257,0,265,259,231,254,240,250,266],
[224,259,249,235,0,246,240,254,240,253,240],
[215,259,261,241,254,0,238,234,250,261,245],
[251,242,256,269,260,262,0,280,244,266,259],
[246,252,251,246,246,266,220,0,215,259,260],
[254,285,287,260,260,250,256,285,0,266,279],
[239,270,247,250,247,239,234,241,234,0,250],
[240,262,254,234,260,255,241,240,221,250,0]])



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
result = np.append(np.array([11, 500, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,211,230,267,201,214,240,203,233,230,215],
[289,0,257,279,216,242,238,236,221,212,260],
[270,243,0,260,223,194,203,230,228,199,255],
[233,221,240,0,189,200,232,195,214,199,214],
[299,284,277,311,0,238,275,262,244,234,234],
[286,258,306,300,262,0,295,254,260,221,258],
[260,262,297,268,225,205,0,233,216,202,257],
[297,264,270,305,238,246,267,0,264,234,274],
[267,279,272,286,256,240,284,236,0,261,255],
[270,288,301,301,266,279,298,266,239,0,244],
[285,240,245,286,266,242,243,226,245,256,0]])



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
result = np.append(np.array([11, 500, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,248,233,228,234,267,226,235,226,257],
[279,0,253,249,228,242,259,251,252,227,283],
[252,247,0,255,226,243,262,240,232,240,267],
[267,251,245,0,235,240,255,260,243,242,251],
[272,272,274,265,0,248,268,275,247,254,256],
[266,258,257,260,252,0,269,255,257,238,264],
[233,241,238,245,232,231,0,228,227,238,250],
[274,249,260,240,225,245,272,0,235,234,256],
[265,248,268,257,253,243,273,265,0,240,262],
[274,273,260,258,246,262,262,266,260,0,256],
[243,217,233,249,244,236,250,244,238,244,0]])



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
result = np.append(np.array([11, 500, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,248,234,249,256,236,236,256,256,253],
[256,0,261,255,245,240,258,256,261,270,254],
[252,239,0,246,239,252,247,238,249,255,251],
[266,245,254,0,253,251,235,248,251,255,250],
[251,255,261,247,0,240,248,239,262,258,258],
[244,260,248,249,260,0,238,242,247,244,261],
[264,242,253,265,252,262,0,251,257,265,252],
[264,244,262,252,261,258,249,0,269,263,271],
[244,239,251,249,238,253,243,231,0,257,237],
[244,230,245,245,242,256,235,237,243,0,256],
[247,246,249,250,242,239,248,229,263,244,0]])



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
result = np.append(np.array([11, 500, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,288,224,282,185,239,224,208,225,252],
[233,0,250,177,284,216,231,188,235,189,246],
[212,250,0,201,261,182,260,184,207,188,209],
[276,323,299,0,262,235,261,232,263,246,296],
[218,216,239,238,0,228,255,216,263,192,236],
[315,284,318,265,272,0,270,277,245,238,265],
[261,269,240,239,245,230,0,194,256,234,248],
[276,312,316,268,284,223,306,0,288,233,262],
[292,265,293,237,237,255,244,212,0,254,275],
[275,311,312,254,308,262,266,267,246,0,322],
[248,254,291,204,264,235,252,238,225,178,0]])



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
result = np.append(np.array([11, 500, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,245,240,242,259,243,259,248,246,235],
[263,0,244,264,252,243,247,259,263,249,246],
[255,256,0,258,251,273,257,260,254,247,240],
[260,236,242,0,247,255,243,274,257,264,236],
[258,248,249,253,0,249,243,257,247,238,255],
[241,257,227,245,251,0,240,255,235,237,240],
[257,253,243,257,257,260,0,264,256,266,251],
[241,241,240,226,243,245,236,0,246,252,236],
[252,237,246,243,253,265,244,254,0,239,243],
[254,251,253,236,262,263,234,248,261,0,242],
[265,254,260,264,245,260,249,264,257,258,0]])



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
result = np.append(np.array([11, 500, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,290,212,258,233,268,260,238,271,254],
[246,0,272,162,264,247,242,307,245,272,335],
[210,228,0,220,192,190,152,217,224,277,228],
[288,338,280,0,356,246,278,317,279,385,367],
[242,236,308,144,0,186,155,248,244,259,271],
[267,253,310,254,314,0,207,297,247,329,246],
[232,258,348,222,345,293,0,327,195,313,361],
[240,193,283,183,252,203,173,0,183,281,251],
[262,255,276,221,256,253,305,317,0,278,387],
[229,228,223,115,241,171,187,219,222,0,271],
[246,165,272,133,229,254,139,249,113,229,0]])



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
result = np.append(np.array([11, 500, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,269,244,267,294,251,272,276,282,268],
[242,0,254,250,250,273,241,263,247,255,245],
[231,246,0,230,242,274,248,267,246,256,271],
[256,250,270,0,253,273,242,249,260,269,273],
[233,250,258,247,0,271,240,258,252,250,264],
[206,227,226,227,229,0,210,248,234,250,242],
[249,259,252,258,260,290,0,271,263,258,272],
[228,237,233,251,242,252,229,0,243,246,254],
[224,253,254,240,248,266,237,257,0,247,256],
[218,245,244,231,250,250,242,254,253,0,268],
[232,255,229,227,236,258,228,246,244,232,0]])



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
result = np.append(np.array([11, 500, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,265,238,262,231,224,261,271,255,278],
[254,0,253,229,273,254,253,278,293,251,287],
[235,247,0,260,257,229,248,248,224,255,260],
[262,271,240,0,220,248,237,274,251,260,281],
[238,227,243,280,0,252,243,249,289,280,290],
[269,246,271,252,248,0,258,256,302,273,283],
[276,247,252,263,257,242,0,285,300,272,282],
[239,222,252,226,251,244,215,0,249,254,260],
[229,207,276,249,211,198,200,251,0,227,219],
[245,249,245,240,220,227,228,246,273,0,268],
[222,213,240,219,210,217,218,240,281,232,0]])



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
result = np.append(np.array([11, 500, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,291,253,246,239,251,244,264,245,264],
[246,0,296,274,249,249,253,243,265,257,280],
[209,204,0,220,212,228,224,229,222,214,244],
[247,226,280,0,253,222,253,260,238,237,238],
[254,251,288,247,0,247,273,244,250,273,261],
[261,251,272,278,253,0,261,243,257,257,257],
[249,247,276,247,227,239,0,248,251,247,260],
[256,257,271,240,256,257,252,0,252,233,272],
[236,235,278,262,250,243,249,248,0,268,270],
[255,243,286,263,227,243,253,267,232,0,251],
[236,220,256,262,239,243,240,228,230,249,0]])



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
result = np.append(np.array([11, 500, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,240,260,237,271,258,251,230,241,265],
[264,0,217,252,223,259,244,243,262,257,243],
[260,283,0,279,273,248,267,278,295,247,258],
[240,248,221,0,220,244,245,227,254,249,261],
[263,277,227,280,0,262,262,238,290,269,273],
[229,241,252,256,238,0,273,226,260,224,246],
[242,256,233,255,238,227,0,234,259,260,262],
[249,257,222,273,262,274,266,0,280,240,283],
[270,238,205,246,210,240,241,220,0,252,257],
[259,243,253,251,231,276,240,260,248,0,287],
[235,257,242,239,227,254,238,217,243,213,0]])



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
result = np.append(np.array([11, 500, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,237,233,247,239,243,231,246,262,256],
[254,0,237,255,256,252,259,251,260,273,243],
[263,263,0,247,264,259,254,267,247,267,256],
[267,245,253,0,247,261,255,257,259,263,252],
[253,244,236,253,0,253,241,251,250,278,256],
[261,248,241,239,247,0,254,261,259,261,247],
[257,241,246,245,259,246,0,240,251,250,253],
[269,249,233,243,249,239,260,0,245,250,260],
[254,240,253,241,250,241,249,255,0,253,250],
[238,227,233,237,222,239,250,250,247,0,249],
[244,257,244,248,244,253,247,240,250,251,0]])



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
result = np.append(np.array([11, 500, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,267,247,247,255,251,261,251,260,255],
[252,0,246,258,258,238,255,256,248,257,245],
[233,254,0,240,259,228,239,249,250,239,241],
[253,242,260,0,250,237,229,245,258,242,241],
[253,242,241,250,0,240,241,255,246,255,237],
[245,262,272,263,260,0,248,267,273,270,269],
[249,245,261,271,259,252,0,257,252,268,253],
[239,244,251,255,245,233,243,0,252,262,258],
[249,252,250,242,254,227,248,248,0,247,252],
[240,243,261,258,245,230,232,238,253,0,236],
[245,255,259,259,263,231,247,242,248,264,0]])



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
result = np.append(np.array([11, 500, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,255,250,264,243,242,249,257,279,261],
[223,0,241,228,259,211,222,218,239,256,237],
[245,259,0,242,262,240,245,239,248,261,236],
[250,272,258,0,269,249,245,226,264,270,250],
[236,241,238,231,0,229,245,236,233,258,228],
[257,289,260,251,271,0,268,248,271,277,254],
[258,278,255,255,255,232,0,232,259,266,240],
[251,282,261,274,264,252,268,0,257,290,244],
[243,261,252,236,267,229,241,243,0,272,249],
[221,244,239,230,242,223,234,210,228,0,218],
[239,263,264,250,272,246,260,256,251,282,0]])



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
result = np.append(np.array([11, 500, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,255,244,255,240,234,277,231,229,244],
[255,0,238,252,246,233,238,240,228,236,220],
[245,262,0,250,282,231,255,272,233,245,235],
[256,248,250,0,268,264,261,274,235,238,230],
[245,254,218,232,0,221,251,239,237,247,218],
[260,267,269,236,279,0,250,270,266,244,257],
[266,262,245,239,249,250,0,253,232,258,229],
[223,260,228,226,261,230,247,0,245,230,237],
[269,272,267,265,263,234,268,255,0,253,246],
[271,264,255,262,253,256,242,270,247,0,252],
[256,280,265,270,282,243,271,263,254,248,0]])



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
result = np.append(np.array([11, 500, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,228,232,287,252,244,254,251,264,249],
[247,0,243,238,275,253,256,256,253,263,245],
[272,257,0,251,275,264,254,261,251,259,250],
[268,262,249,0,265,258,261,277,267,261,257],
[213,225,225,235,0,235,241,230,237,241,223],
[248,247,236,242,265,0,235,256,248,254,244],
[256,244,246,239,259,265,0,251,252,248,253],
[246,244,239,223,270,244,249,0,260,244,252],
[249,247,249,233,263,252,248,240,0,248,239],
[236,237,241,239,259,246,252,256,252,0,239],
[251,255,250,243,277,256,247,248,261,261,0]])



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
result = np.append(np.array([11, 500, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,310,228,232,259,270,263,253,265,285,255],
[190,0,238,190,183,233,232,221,266,240,188],
[272,262,0,249,241,252,267,223,280,271,245],
[268,310,251,0,273,294,272,250,294,243,270],
[241,317,259,227,0,287,267,215,284,266,265],
[230,267,248,206,213,0,270,197,267,273,214],
[237,268,233,228,233,230,0,190,303,239,232],
[247,279,277,250,285,303,310,0,326,272,238],
[235,234,220,206,216,233,197,174,0,224,237],
[215,260,229,257,234,227,261,228,276,0,226],
[245,312,255,230,235,286,268,262,263,274,0]])



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
result = np.append(np.array([11, 500, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,186,199,188,211,215,224,238,209,195],
[262,0,196,156,241,263,249,236,226,253,226],
[314,304,0,287,247,240,303,288,252,321,277],
[301,344,213,0,273,290,333,303,250,327,332],
[312,259,253,227,0,232,244,305,289,230,257],
[289,237,260,210,268,0,257,294,264,229,288],
[285,251,197,167,256,243,0,241,235,222,263],
[276,264,212,197,195,206,259,0,193,252,231],
[262,274,248,250,211,236,265,307,0,250,233],
[291,247,179,173,270,271,278,248,250,0,253],
[305,274,223,168,243,212,237,269,267,247,0]])



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
result = np.append(np.array([11, 500, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,228,217,226,223,238,247,221,262,245],
[248,0,231,236,246,257,251,238,231,242,246],
[272,269,0,258,247,251,268,262,263,271,232],
[283,264,242,0,258,245,269,258,244,263,254],
[274,254,253,242,0,251,258,247,239,267,253],
[277,243,249,255,249,0,255,250,256,255,262],
[262,249,232,231,242,245,0,249,240,234,262],
[253,262,238,242,253,250,251,0,258,264,248],
[279,269,237,256,261,244,260,242,0,278,249],
[238,258,229,237,233,245,266,236,222,0,246],
[255,254,268,246,247,238,238,252,251,254,0]])



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
result = np.append(np.array([11, 500, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,213,249,253,246,204,209,184,204,216,234],
[287,0,271,260,269,202,236,214,214,276,256],
[251,229,0,281,239,216,236,216,222,238,241],
[247,240,219,0,249,245,241,239,246,254,240],
[254,231,261,251,0,240,225,196,204,229,215],
[296,298,284,255,260,0,245,260,254,282,252],
[291,264,264,259,275,255,0,197,254,264,252],
[316,286,284,261,304,240,303,0,237,281,268],
[296,286,278,254,296,246,246,263,0,294,280],
[284,224,262,246,271,218,236,219,206,0,247],
[266,244,259,260,285,248,248,232,220,253,0]])



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
result = np.append(np.array([11, 500, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,240,233,260,256,242,229,246,231,244],
[255,0,225,249,271,259,248,228,231,233,237],
[260,275,0,270,271,277,254,247,233,247,244],
[267,251,230,0,267,252,257,230,227,226,240],
[240,229,229,233,0,246,243,211,222,235,221],
[244,241,223,248,254,0,249,222,226,233,249],
[258,252,246,243,257,251,0,228,255,234,231],
[271,272,253,270,289,278,272,0,250,260,260],
[254,269,267,273,278,274,245,250,0,246,251],
[269,267,253,274,265,267,266,240,254,0,260],
[256,263,256,260,279,251,269,240,249,240,0]])



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
result = np.append(np.array([11, 500, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,212,188,247,209,268,112,304,177,253,202],
[288,0,295,247,267,277,190,333,281,301,191],
[312,205,0,240,245,307,199,293,241,269,238],
[253,253,260,0,262,278,213,271,218,244,159],
[291,233,255,238,0,277,180,326,244,226,204],
[232,223,193,222,223,0,142,236,196,188,181],
[388,310,301,287,320,358,0,323,296,319,212],
[196,167,207,229,174,264,177,0,210,197,169],
[323,219,259,282,256,304,204,290,0,310,253],
[247,199,231,256,274,312,181,303,190,0,218],
[298,309,262,341,296,319,288,331,247,282,0]])



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
result = np.append(np.array([11, 500, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,239,229,242,266,262,253,270,242,260],
[243,0,245,239,254,276,251,257,249,260,251],
[261,255,0,229,251,261,247,253,244,261,256],
[271,261,271,0,259,290,275,244,252,270,277],
[258,246,249,241,0,264,259,264,252,254,260],
[234,224,239,210,236,0,251,245,210,255,243],
[238,249,253,225,241,249,0,232,246,250,258],
[247,243,247,256,236,255,268,0,255,259,259],
[230,251,256,248,248,290,254,245,0,249,261],
[258,240,239,230,246,245,250,241,251,0,273],
[240,249,244,223,240,257,242,241,239,227,0]])



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
result = np.append(np.array([11, 500, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,242,263,271,215,241,244,284,244,263],
[251,0,259,288,258,226,233,250,263,235,268],
[258,241,0,285,258,237,242,236,275,240,261],
[237,212,215,0,250,201,216,217,236,210,203],
[229,242,242,250,0,230,242,224,240,228,238],
[285,274,263,299,270,0,250,244,291,258,267],
[259,267,258,284,258,250,0,241,262,253,267],
[256,250,264,283,276,256,259,0,285,276,280],
[216,237,225,264,260,209,238,215,0,231,254],
[256,265,260,290,272,242,247,224,269,0,267],
[237,232,239,297,262,233,233,220,246,233,0]])



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
result = np.append(np.array([11, 500, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,262,231,234,234,252,242,231,240,228],
[282,0,247,251,249,265,266,261,250,257,249],
[238,253,0,250,240,247,243,242,232,241,244],
[269,249,250,0,238,259,253,266,230,252,258],
[266,251,260,262,0,265,273,261,240,255,263],
[266,235,253,241,235,0,272,258,245,247,250],
[248,234,257,247,227,228,0,255,217,235,235],
[258,239,258,234,239,242,245,0,230,246,226],
[269,250,268,270,260,255,283,270,0,268,259],
[260,243,259,248,245,253,265,254,232,0,246],
[272,251,256,242,237,250,265,274,241,254,0]])



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
result = np.append(np.array([11, 500, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,252,272,288,273,283,290,255,230,279],
[228,0,227,255,248,269,247,291,245,250,243],
[248,273,0,255,271,275,281,279,249,282,261],
[228,245,245,0,248,267,265,264,246,241,247],
[212,252,229,252,0,230,257,273,226,225,218],
[227,231,225,233,270,0,258,244,232,258,228],
[217,253,219,235,243,242,0,262,220,262,226],
[210,209,221,236,227,256,238,0,207,216,240],
[245,255,251,254,274,268,280,293,0,267,263],
[270,250,218,259,275,242,238,284,233,0,251],
[221,257,239,253,282,272,274,260,237,249,0]])



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
result = np.append(np.array([11, 500, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,248,254,239,279,238,255,264,270,279],
[269,0,262,266,285,248,256,268,289,262,288],
[252,238,0,249,270,254,261,229,269,272,276],
[246,234,251,0,255,267,265,259,253,277,287],
[261,215,230,245,0,240,254,260,245,267,264],
[221,252,246,233,260,0,256,229,255,267,278],
[262,244,239,235,246,244,0,267,262,260,290],
[245,232,271,241,240,271,233,0,252,244,289],
[236,211,231,247,255,245,238,248,0,255,256],
[230,238,228,223,233,233,240,256,245,0,254],
[221,212,224,213,236,222,210,211,244,246,0]])



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
result = np.append(np.array([11, 500, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,240,289,286,317,263,243,235,267,273],
[261,0,294,286,290,331,299,279,278,246,319],
[260,206,0,265,247,282,292,275,296,252,284],
[211,214,235,0,257,314,308,221,234,187,271],
[214,210,253,243,0,322,302,270,219,233,271],
[183,169,218,186,178,0,247,224,199,198,238],
[237,201,208,192,198,253,0,249,207,186,272],
[257,221,225,279,230,276,251,0,253,225,283],
[265,222,204,266,281,301,293,247,0,198,285],
[233,254,248,313,267,302,314,275,302,0,265],
[227,181,216,229,229,262,228,217,215,235,0]])



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
result = np.append(np.array([11, 500, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,255,285,239,241,253,236,248,279,275],
[246,0,260,256,260,255,255,249,276,262,251],
[245,240,0,257,211,198,219,238,222,216,237],
[215,244,243,0,234,185,222,221,252,236,235],
[261,240,289,266,0,242,274,252,245,271,252],
[259,245,302,315,258,0,252,292,258,269,285],
[247,245,281,278,226,248,0,229,256,251,281],
[264,251,262,279,248,208,271,0,258,261,248],
[252,224,278,248,255,242,244,242,0,261,281],
[221,238,284,264,229,231,249,239,239,0,273],
[225,249,263,265,248,215,219,252,219,227,0]])



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
result = np.append(np.array([11, 500, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,203,162,322,312,237,157,166,312,213],
[235,0,132,171,239,214,126,201,140,198,151],
[297,368,0,187,346,459,200,301,362,361,352],
[338,329,313,0,317,337,247,336,312,403,325],
[178,261,154,183,0,261,171,170,191,240,239],
[188,286,41,163,239,0,128,157,193,312,238],
[263,374,300,253,329,372,0,280,245,351,341],
[343,299,199,164,330,343,220,0,221,258,291],
[334,360,138,188,309,307,255,279,0,353,195],
[188,302,139,97,260,188,149,242,147,0,200],
[287,349,148,175,261,262,159,209,305,300,0]])



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
result = np.append(np.array([11, 500, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,250,232,256,252,256,255,229,255,251],
[257,0,246,249,267,230,249,248,231,241,240],
[250,254,0,256,272,265,265,259,250,249,251],
[268,251,244,0,253,266,260,279,252,258,281],
[244,233,228,247,0,239,252,228,223,230,253],
[248,270,235,234,261,0,273,245,244,243,250],
[244,251,235,240,248,227,0,239,230,230,265],
[245,252,241,221,272,255,261,0,234,245,249],
[271,269,250,248,277,256,270,266,0,247,271],
[245,259,251,242,270,257,270,255,253,0,262],
[249,260,249,219,247,250,235,251,229,238,0]])



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
result = np.append(np.array([11, 500, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,230,214,250,242,241,237,230,226,233],
[257,0,266,258,237,256,251,257,247,231,242],
[270,234,0,247,252,253,279,264,259,232,248],
[286,242,253,0,267,256,266,278,244,243,264],
[250,263,248,233,0,260,255,253,255,242,242],
[258,244,247,244,240,0,249,258,242,251,266],
[259,249,221,234,245,251,0,257,236,236,234],
[263,243,236,222,247,242,243,0,232,252,243],
[270,253,241,256,245,258,264,268,0,243,266],
[274,269,268,257,258,249,264,248,257,0,239],
[267,258,252,236,258,234,266,257,234,261,0]])



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
result = np.append(np.array([11, 500, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,246,220,258,247,226,240,236,239,271],
[255,0,287,248,258,241,244,247,259,277,298],
[254,213,0,248,233,251,230,236,249,256,244],
[280,252,252,0,262,262,255,235,255,270,271],
[242,242,267,238,0,247,227,225,240,248,270],
[253,259,249,238,253,0,234,228,229,233,265],
[274,256,270,245,273,266,0,260,274,250,288],
[260,253,264,265,275,272,240,0,248,259,263],
[264,241,251,245,260,271,226,252,0,251,247],
[261,223,244,230,252,267,250,241,249,0,262],
[229,202,256,229,230,235,212,237,253,238,0]])



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
result = np.append(np.array([11, 500, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,250,257,233,236,237,241,256,250,236],
[247,0,249,268,236,245,231,244,274,238,224],
[250,251,0,251,224,243,233,250,260,234,221],
[243,232,249,0,247,251,234,238,256,246,230],
[267,264,276,253,0,264,225,236,271,249,230],
[264,255,257,249,236,0,224,248,262,246,244],
[263,269,267,266,275,276,0,256,277,248,252],
[259,256,250,262,264,252,244,0,270,250,234],
[244,226,240,244,229,238,223,230,0,243,231],
[250,262,266,254,251,254,252,250,257,0,249],
[264,276,279,270,270,256,248,266,269,251,0]])



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
result = np.append(np.array([11, 500, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,255,261,247,245,252,257,267,254,271],
[235,0,256,246,231,249,239,230,250,244,248],
[245,244,0,248,226,250,224,240,232,234,258],
[239,254,252,0,243,252,237,251,252,258,257],
[253,269,274,257,0,268,243,263,260,247,267],
[255,251,250,248,232,0,232,247,244,236,264],
[248,261,276,263,257,268,0,259,261,258,277],
[243,270,260,249,237,253,241,0,253,252,264],
[233,250,268,248,240,256,239,247,0,253,259],
[246,256,266,242,253,264,242,248,247,0,256],
[229,252,242,243,233,236,223,236,241,244,0]])



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
result = np.append(np.array([11, 500, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,253,246,240,264,235,251,260,249,249],
[230,0,236,226,214,250,227,235,253,236,234],
[247,264,0,238,230,269,231,230,254,249,255],
[254,274,262,0,254,263,245,241,265,251,257],
[260,286,270,246,0,267,258,264,282,257,255],
[236,250,231,237,233,0,230,239,259,228,243],
[265,273,269,255,242,270,0,271,267,247,252],
[249,265,270,259,236,261,229,0,267,257,248],
[240,247,246,235,218,241,233,233,0,246,240],
[251,264,251,249,243,272,253,243,254,0,247],
[251,266,245,243,245,257,248,252,260,253,0]])



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
result = np.append(np.array([11, 500, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,234,247,239,248,234,247,252,240,249],
[238,0,246,251,224,245,214,254,257,222,245],
[266,254,0,257,253,244,228,252,266,227,260],
[253,249,243,0,229,240,220,244,225,220,248],
[261,276,247,271,0,250,242,252,254,257,258],
[252,255,256,260,250,0,239,245,255,234,248],
[266,286,272,280,258,261,0,264,269,246,288],
[253,246,248,256,248,255,236,0,250,241,259],
[248,243,234,275,246,245,231,250,0,219,260],
[260,278,273,280,243,266,254,259,281,0,270],
[251,255,240,252,242,252,212,241,240,230,0]])



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
result = np.append(np.array([11, 500, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,239,251,241,236,253,248,238,248,253],
[259,0,234,253,255,241,248,251,238,242,260],
[261,266,0,257,255,249,250,256,230,243,255],
[249,247,243,0,243,242,248,247,250,242,251],
[259,245,245,257,0,262,245,257,238,257,258],
[264,259,251,258,238,0,231,231,239,234,266],
[247,252,250,252,255,269,0,251,258,248,272],
[252,249,244,253,243,269,249,0,243,239,249],
[262,262,270,250,262,261,242,257,0,260,264],
[252,258,257,258,243,266,252,261,240,0,253],
[247,240,245,249,242,234,228,251,236,247,0]])



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
result = np.append(np.array([11, 500, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,273,278,275,264,300,244,272,268,225],
[247,0,249,231,242,232,272,250,235,236,205],
[227,251,0,268,235,244,281,224,246,239,228],
[222,269,232,0,228,236,299,244,244,237,214],
[225,258,265,272,0,222,278,229,265,237,226],
[236,268,256,264,278,0,276,236,252,267,240],
[200,228,219,201,222,224,0,186,228,196,205],
[256,250,276,256,271,264,314,0,271,244,252],
[228,265,254,256,235,248,272,229,0,238,225],
[232,264,261,263,263,233,304,256,262,0,229],
[275,295,272,286,274,260,295,248,275,271,0]])



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
result = np.append(np.array([11, 500, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,241,224,246,258,210,256,230,202,229],
[273,0,227,227,240,244,223,253,243,253,241],
[259,273,0,239,240,238,263,215,251,226,206],
[276,273,261,0,291,243,241,237,233,254,233],
[254,260,260,209,0,272,234,240,265,250,205],
[242,256,262,257,228,0,216,229,214,223,197],
[290,277,237,259,266,284,0,266,225,281,236],
[244,247,285,263,260,271,234,0,224,249,246],
[270,257,249,267,235,286,275,276,0,237,257],
[298,247,274,246,250,277,219,251,263,0,230],
[271,259,294,267,295,303,264,254,243,270,0]])



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
result = np.append(np.array([11, 500, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,269,268,272,259,251,247,275,239,250],
[241,0,232,236,239,258,253,260,266,253,255],
[231,268,0,269,278,255,240,293,240,260,256],
[232,264,231,0,261,254,231,256,249,277,259],
[228,261,222,239,0,248,205,240,270,255,253],
[241,242,245,246,252,0,243,237,245,261,242],
[249,247,260,269,295,257,0,292,274,254,270],
[253,240,207,244,260,263,208,0,238,250,241],
[225,234,260,251,230,255,226,262,0,226,251],
[261,247,240,223,245,239,246,250,274,0,233],
[250,245,244,241,247,258,230,259,249,267,0]])



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
result = np.append(np.array([11, 500, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,247,267,241,272,253,254,246,260,244],
[246,0,254,244,230,260,251,259,237,241,239],
[253,246,0,268,233,252,238,258,243,245,236],
[233,256,232,0,247,257,245,263,246,239,234],
[259,270,267,253,0,281,246,262,271,264,262],
[228,240,248,243,219,0,249,243,237,237,237],
[247,249,262,255,254,251,0,264,245,250,241],
[246,241,242,237,238,257,236,0,234,242,240],
[254,263,257,254,229,263,255,266,0,241,250],
[240,259,255,261,236,263,250,258,259,0,249],
[256,261,264,266,238,263,259,260,250,251,0]])



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
result = np.append(np.array([11, 500, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,253,215,222,215,275,227,240,242,224],
[244,0,260,231,225,249,263,256,274,248,257],
[247,240,0,246,244,229,234,233,248,251,235],
[285,269,254,0,253,269,248,243,247,264,266],
[278,275,256,247,0,247,232,251,236,248,249],
[285,251,271,231,253,0,251,221,249,246,255],
[225,237,266,252,268,249,0,209,232,243,251],
[273,244,267,257,249,279,291,0,264,256,258],
[260,226,252,253,264,251,268,236,0,240,260],
[258,252,249,236,252,254,257,244,260,0,250],
[276,243,265,234,251,245,249,242,240,250,0]])



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
result = np.append(np.array([11, 500, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,251,260,237,253,214,224,249,239,229],
[254,0,212,249,249,244,240,251,247,235,255],
[249,288,0,284,276,273,259,271,252,258,253],
[240,251,216,0,257,254,232,242,255,259,259],
[263,251,224,243,0,222,223,229,246,258,250],
[247,256,227,246,278,0,242,244,248,233,240],
[286,260,241,268,277,258,0,251,252,231,253],
[276,249,229,258,271,256,249,0,250,253,248],
[251,253,248,245,254,252,248,250,0,213,268],
[261,265,242,241,242,267,269,247,287,0,276],
[271,245,247,241,250,260,247,252,232,224,0]])



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
result = np.append(np.array([11, 500, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,238,283,326,280,275,339,216,214,274],
[256,0,253,307,250,225,274,255,218,205,285],
[262,247,0,266,234,239,267,261,242,204,223],
[217,193,234,0,274,187,268,258,209,181,243],
[174,250,266,226,0,198,231,213,161,168,233],
[220,275,261,313,302,0,264,247,223,194,315],
[225,226,233,232,269,236,0,292,231,219,276],
[161,245,239,242,287,253,208,0,193,183,210],
[284,282,258,291,339,277,269,307,0,268,227],
[286,295,296,319,332,306,281,317,232,0,274],
[226,215,277,257,267,185,224,290,273,226,0]])



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
result = np.append(np.array([11, 500, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,195,250,231,240,270,231,232,267,238,257],
[305,0,305,228,251,266,255,288,263,269,285],
[250,195,0,241,233,274,233,246,269,246,248],
[269,272,259,0,269,267,225,258,252,268,279],
[260,249,267,231,0,289,226,245,255,265,223],
[230,234,226,233,211,0,225,243,259,252,216],
[269,245,267,275,274,275,0,271,271,247,270],
[268,212,254,242,255,257,229,0,237,237,239],
[233,237,231,248,245,241,229,263,0,255,269],
[262,231,254,232,235,248,253,263,245,0,254],
[243,215,252,221,277,284,230,261,231,246,0]])



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
result = np.append(np.array([11, 500, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,268,280,255,241,269,261,258,271,256],
[220,0,268,278,238,252,275,237,264,261,263],
[232,232,0,225,232,256,264,228,251,244,253],
[220,222,275,0,235,237,265,217,246,216,241],
[245,262,268,265,0,280,270,259,258,261,265],
[259,248,244,263,220,0,240,232,231,222,251],
[231,225,236,235,230,260,0,212,207,223,218],
[239,263,272,283,241,268,288,0,273,264,266],
[242,236,249,254,242,269,293,227,0,246,255],
[229,239,256,284,239,278,277,236,254,0,257],
[244,237,247,259,235,249,282,234,245,243,0]])



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
result = np.append(np.array([11, 500, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,265,245,232,240,247,221,251,275,258],
[247,0,259,234,235,270,247,257,261,281,265],
[235,241,0,223,209,243,233,211,262,242,244],
[255,266,277,0,247,269,248,245,265,260,265],
[268,265,291,253,0,256,273,239,293,292,288],
[260,230,257,231,244,0,250,228,268,256,267],
[253,253,267,252,227,250,0,232,261,294,268],
[279,243,289,255,261,272,268,0,282,271,288],
[249,239,238,235,207,232,239,218,0,233,240],
[225,219,258,240,208,244,206,229,267,0,254],
[242,235,256,235,212,233,232,212,260,246,0]])



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
result = np.append(np.array([11, 500, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,266,303,297,232,239,236,251,254,271],
[284,0,245,284,285,270,236,278,275,278,300],
[234,255,0,301,249,219,242,266,237,269,260],
[197,216,199,0,240,222,239,207,243,241,245],
[203,215,251,260,0,234,230,209,238,232,268],
[268,230,281,278,266,0,258,241,270,263,265],
[261,264,258,261,270,242,0,230,231,279,285],
[264,222,234,293,291,259,270,0,283,292,299],
[249,225,263,257,262,230,269,217,0,257,274],
[246,222,231,259,268,237,221,208,243,0,239],
[229,200,240,255,232,235,215,201,226,261,0]])



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
result = np.append(np.array([11, 500, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,259,264,253,260,267,244,254,278,260],
[255,0,271,242,264,272,261,250,248,286,248],
[241,229,0,256,253,235,243,253,248,266,233],
[236,258,244,0,250,268,257,256,264,245,252],
[247,236,247,250,0,260,239,244,242,270,256],
[240,228,265,232,240,0,263,240,254,256,239],
[233,239,257,243,261,237,0,219,255,248,237],
[256,250,247,244,256,260,281,0,242,264,243],
[246,252,252,236,258,246,245,258,0,264,252],
[222,214,234,255,230,244,252,236,236,0,232],
[240,252,267,248,244,261,263,257,248,268,0]])



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
result = np.append(np.array([11, 500, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,290,278,236,221,270,239,174,247,179,278],
[210,0,312,273,242,303,284,356,229,255,313],
[222,188,0,258,217,298,218,184,208,256,235],
[264,227,242,0,280,336,318,265,290,204,269],
[279,258,283,220,0,302,248,263,219,290,273],
[230,197,202,164,198,0,216,167,189,218,187],
[261,216,282,182,252,284,0,248,174,213,283],
[326,144,316,235,237,333,252,0,226,231,232],
[253,271,292,210,281,311,326,274,0,251,296],
[321,245,244,296,210,282,287,269,249,0,261],
[222,187,265,231,227,313,217,268,204,239,0]])



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
result = np.append(np.array([11, 500, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,281,250,230,219,226,257,277,262,231],
[253,0,244,241,246,229,228,247,233,264,234],
[219,256,0,252,280,234,246,271,237,264,220],
[250,259,248,0,269,258,240,243,280,261,252],
[270,254,220,231,0,218,259,219,262,245,211],
[281,271,266,242,282,0,268,249,308,272,225],
[274,272,254,260,241,232,0,254,285,257,264],
[243,253,229,257,281,251,246,0,254,267,232],
[223,267,263,220,238,192,215,246,0,243,212],
[238,236,236,239,255,228,243,233,257,0,234],
[269,266,280,248,289,275,236,268,288,266,0]])



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
result = np.append(np.array([11, 500, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,260,263,262,252,258,240,254,237,270],
[227,0,232,241,262,250,247,264,231,208,257],
[240,268,0,214,253,210,241,266,256,207,250],
[237,259,286,0,261,275,274,298,305,265,291],
[238,238,247,239,0,241,241,273,263,231,262],
[248,250,290,225,259,0,282,257,299,281,285],
[242,253,259,226,259,218,0,249,279,232,269],
[260,236,234,202,227,243,251,0,252,228,240],
[246,269,244,195,237,201,221,248,0,219,280],
[263,292,293,235,269,219,268,272,281,0,302],
[230,243,250,209,238,215,231,260,220,198,0]])



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
result = np.append(np.array([11, 500, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,271,231,258,218,256,238,249,246,228],
[250,0,247,205,256,218,232,238,254,250,247],
[229,253,0,219,250,201,221,243,257,218,251],
[269,295,281,0,249,251,261,268,280,266,279],
[242,244,250,251,0,211,236,224,249,227,259],
[282,282,299,249,289,0,265,285,282,277,279],
[244,268,279,239,264,235,0,260,262,234,254],
[262,262,257,232,276,215,240,0,271,243,278],
[251,246,243,220,251,218,238,229,0,224,265],
[254,250,282,234,273,223,266,257,276,0,259],
[272,253,249,221,241,221,246,222,235,241,0]])



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
result = np.append(np.array([11, 500, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,269,246,196,280,279,221,277,257,259],
[256,0,260,279,256,249,243,274,289,248,280],
[231,240,0,252,181,244,251,220,242,231,217],
[254,221,248,0,233,286,237,264,250,241,245],
[304,244,319,267,0,287,279,289,282,277,261],
[220,251,256,214,213,0,270,267,288,252,243],
[221,257,249,263,221,230,0,253,271,267,213],
[279,226,280,236,211,233,247,0,249,260,263],
[223,211,258,250,218,212,229,251,0,213,238],
[243,252,269,259,223,248,233,240,287,0,259],
[241,220,283,255,239,257,287,237,262,241,0]])



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
result = np.append(np.array([11, 500, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,238,281,276,264,267,253,252,250,272],
[226,0,230,259,234,242,242,247,227,242,263],
[262,270,0,285,261,272,263,249,264,258,262],
[219,241,215,0,224,241,246,236,240,226,254],
[224,266,239,276,0,265,255,248,249,239,263],
[236,258,228,259,235,0,242,229,238,233,244],
[233,258,237,254,245,258,0,230,246,237,253],
[247,253,251,264,252,271,270,0,257,257,261],
[248,273,236,260,251,262,254,243,0,255,255],
[250,258,242,274,261,267,263,243,245,0,267],
[228,237,238,246,237,256,247,239,245,233,0]])



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
result = np.append(np.array([11, 500, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,221,220,222,234,225,199,196,225,203],
[254,0,222,245,259,246,254,228,244,259,245],
[279,278,0,245,252,258,255,226,238,272,255],
[280,255,255,0,241,265,259,258,258,256,273],
[278,241,248,259,0,253,263,247,254,281,242],
[266,254,242,235,247,0,245,240,233,269,238],
[275,246,245,241,237,255,0,243,224,253,238],
[301,272,274,242,253,260,257,0,252,246,241],
[304,256,262,242,246,267,276,248,0,290,257],
[275,241,228,244,219,231,247,254,210,0,227],
[297,255,245,227,258,262,262,259,243,273,0]])



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
result = np.append(np.array([11, 500, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,254,261,237,252,251,242,296,234,248],
[220,0,249,262,239,244,243,234,258,214,242],
[246,251,0,249,257,240,245,283,269,239,253],
[239,238,251,0,218,222,247,245,267,246,226],
[263,261,243,282,0,277,252,255,287,257,233],
[248,256,260,278,223,0,288,267,281,246,233],
[249,257,255,253,248,212,0,234,279,234,213],
[258,266,217,255,245,233,266,0,297,261,245],
[204,242,231,233,213,219,221,203,0,212,205],
[266,286,261,254,243,254,266,239,288,0,264],
[252,258,247,274,267,267,287,255,295,236,0]])



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
result = np.append(np.array([11, 500, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,251,228,276,253,258,264,248,257,257],
[257,0,225,261,271,240,221,268,277,261,259],
[249,275,0,254,251,258,292,270,258,286,234],
[272,239,246,0,258,248,298,296,269,261,240],
[224,229,249,242,0,250,277,285,249,277,262],
[247,260,242,252,250,0,257,246,251,252,250],
[242,279,208,202,223,243,0,266,294,254,241],
[236,232,230,204,215,254,234,0,267,241,244],
[252,223,242,231,251,249,206,233,0,270,286],
[243,239,214,239,223,248,246,259,230,0,226],
[243,241,266,260,238,250,259,256,214,274,0]])



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
result = np.append(np.array([11, 500, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,232,248,253,243,249,253,239,237,235],
[257,0,261,262,267,256,248,260,273,247,261],
[268,239,0,254,256,257,253,259,258,253,248],
[252,238,246,0,243,230,245,243,242,248,244],
[247,233,244,257,0,237,240,253,243,232,254],
[257,244,243,270,263,0,241,255,248,251,258],
[251,252,247,255,260,259,0,248,244,252,256],
[247,240,241,257,247,245,252,0,254,244,258],
[261,227,242,258,257,252,256,246,0,248,252],
[263,253,247,252,268,249,248,256,252,0,254],
[265,239,252,256,246,242,244,242,248,246,0]])



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
result = np.append(np.array([11, 500, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,257,255,256,259,253,253,240,261,252],
[265,0,249,251,239,261,253,236,247,258,248],
[243,251,0,248,250,259,241,244,239,257,252],
[245,249,252,0,239,256,252,234,244,256,251],
[244,261,250,261,0,261,253,255,251,256,248],
[241,239,241,244,239,0,240,233,236,242,234],
[247,247,259,248,247,260,0,240,259,247,255],
[247,264,256,266,245,267,260,0,260,269,253],
[260,253,261,256,249,264,241,240,0,259,259],
[239,242,243,244,244,258,253,231,241,0,239],
[248,252,248,249,252,266,245,247,241,261,0]])



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
result = np.append(np.array([11, 500, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,257,258,246,240,241,239,231,236,237],
[249,0,262,249,261,247,244,245,236,259,247],
[243,238,0,237,247,226,239,234,226,228,250],
[242,251,263,0,258,249,263,239,242,252,261],
[254,239,253,242,0,247,242,227,222,244,233],
[260,253,274,251,253,0,244,256,242,250,242],
[259,256,261,237,258,256,0,242,242,261,256],
[261,255,266,261,273,244,258,0,242,259,253],
[269,264,274,258,278,258,258,258,0,253,237],
[264,241,272,248,256,250,239,241,247,0,232],
[263,253,250,239,267,258,244,247,263,268,0]])



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
result = np.append(np.array([11, 500, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,198,208,207,197,213,228,229,211,217,212],
[302,0,274,258,234,265,288,247,229,244,256],
[292,226,0,234,260,268,260,255,220,227,250],
[293,242,266,0,232,284,268,235,252,212,231],
[303,266,240,268,0,227,307,271,245,242,267],
[287,235,232,216,273,0,256,251,225,259,246],
[272,212,240,232,193,244,0,251,242,251,235],
[271,253,245,265,229,249,249,0,267,258,256],
[289,271,280,248,255,275,258,233,0,269,242],
[283,256,273,288,258,241,249,242,231,0,270],
[288,244,250,269,233,254,265,244,258,230,0]])



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
result = np.append(np.array([11, 500, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,251,251,254,267,251,257,267,262,232],
[247,0,258,251,254,265,248,261,248,264,255],
[249,242,0,239,233,240,245,244,252,245,243],
[249,249,261,0,258,269,265,257,249,242,232],
[246,246,267,242,0,259,245,275,259,245,253],
[233,235,260,231,241,0,237,247,243,246,236],
[249,252,255,235,255,263,0,254,250,273,245],
[243,239,256,243,225,253,246,0,248,238,231],
[233,252,248,251,241,257,250,252,0,252,239],
[238,236,255,258,255,254,227,262,248,0,238],
[268,245,257,268,247,264,255,269,261,262,0]])



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
result = np.append(np.array([11, 500, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,266,230,244,239,249,230,256,246,258],
[244,0,270,250,251,256,251,257,252,249,247],
[234,230,0,243,228,244,249,253,252,257,257],
[270,250,257,0,235,236,260,247,268,250,262],
[256,249,272,265,0,265,268,261,261,260,251],
[261,244,256,264,235,0,257,254,245,259,255],
[251,249,251,240,232,243,0,236,254,260,260],
[270,243,247,253,239,246,264,0,235,252,252],
[244,248,248,232,239,255,246,265,0,251,244],
[254,251,243,250,240,241,240,248,249,0,253],
[242,253,243,238,249,245,240,248,256,247,0]])



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
result = np.append(np.array([11, 500, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,295,229,259,236,238,255,249,282,221,221],
[205,0,221,210,239,203,219,230,245,211,231],
[271,279,0,254,268,257,239,232,266,172,221],
[241,290,246,0,228,226,239,230,258,226,226],
[264,261,232,272,0,246,274,219,275,230,205],
[262,297,243,274,254,0,290,269,281,210,253],
[245,281,261,261,226,210,0,255,250,253,204],
[251,270,268,270,281,231,245,0,288,250,232],
[218,255,234,242,225,219,250,212,0,236,244],
[279,289,328,274,270,290,247,250,264,0,261],
[279,269,279,274,295,247,296,268,256,239,0]])



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
result = np.append(np.array([11, 500, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,230,277,238,201,261,271,205,248,243],
[246,0,246,282,284,238,224,279,260,278,284],
[270,254,0,274,301,233,239,297,229,271,238],
[223,218,226,0,212,190,221,252,180,248,231],
[262,216,199,288,0,182,204,260,198,257,233],
[299,262,267,310,318,0,300,285,242,317,275],
[239,276,261,279,296,200,0,254,215,239,242],
[229,221,203,248,240,215,246,0,218,244,218],
[295,240,271,320,302,258,285,282,0,286,294],
[252,222,229,252,243,183,261,256,214,0,279],
[257,216,262,269,267,225,258,282,206,221,0]])



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
result = np.append(np.array([11, 500, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,219,231,242,242,230,227,245,234,242],
[269,0,254,265,272,290,273,247,274,261,261],
[281,246,0,262,270,247,281,274,264,251,267],
[269,235,238,0,260,270,263,254,258,244,247],
[258,228,230,240,0,260,237,240,298,232,247],
[258,210,253,230,240,0,250,240,242,233,216],
[270,227,219,237,263,250,0,219,253,243,269],
[273,253,226,246,260,260,281,0,274,262,255],
[255,226,236,242,202,258,247,226,0,247,242],
[266,239,249,256,268,267,257,238,253,0,257],
[258,239,233,253,253,284,231,245,258,243,0]])



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
result = np.append(np.array([11, 500, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,261,289,254,269,282,269,252,257,233],
[259,0,269,291,264,270,269,266,258,253,243],
[239,231,0,282,259,254,282,279,264,258,239],
[211,209,218,0,221,227,256,257,243,252,227],
[246,236,241,279,0,254,289,266,281,257,254],
[231,230,246,273,246,0,282,276,253,248,230],
[218,231,218,244,211,218,0,269,239,216,218],
[231,234,221,243,234,224,231,0,245,248,227],
[248,242,236,257,219,247,261,255,0,233,224],
[243,247,242,248,243,252,284,252,267,0,244],
[267,257,261,273,246,270,282,273,276,256,0]])



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
result = np.append(np.array([11, 500, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,248,249,257,257,254,258,248,243,267],
[242,0,246,255,249,267,249,250,245,250,250],
[252,254,0,270,247,266,251,244,249,250,255],
[251,245,230,0,249,260,239,254,250,258,255],
[243,251,253,251,0,265,246,256,256,239,257],
[243,233,234,240,235,0,237,239,228,229,238],
[246,251,249,261,254,263,0,259,254,263,249],
[242,250,256,246,244,261,241,0,244,243,257],
[252,255,251,250,244,272,246,256,0,233,245],
[257,250,250,242,261,271,237,257,267,0,248],
[233,250,245,245,243,262,251,243,255,252,0]])



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
result = np.append(np.array([11, 500, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,246,254,265,246,235,235,253,249,268],
[248,0,255,229,255,230,245,252,235,241,241],
[254,245,0,254,263,245,246,243,262,256,259],
[246,271,246,0,266,256,249,238,264,251,276],
[235,245,237,234,0,225,235,225,239,243,237],
[254,270,255,244,275,0,242,247,252,263,257],
[265,255,254,251,265,258,0,238,257,257,246],
[265,248,257,262,275,253,262,0,267,250,261],
[247,265,238,236,261,248,243,233,0,245,252],
[251,259,244,249,257,237,243,250,255,0,263],
[232,259,241,224,263,243,254,239,248,237,0]])



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
result = np.append(np.array([11, 500, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,252,243,264,258,276,261,256,277,263],
[245,0,246,239,241,242,246,254,251,255,251],
[248,254,0,230,242,245,238,241,240,251,256],
[257,261,270,0,261,255,275,271,248,262,274],
[236,259,258,239,0,249,278,250,250,262,254],
[242,258,255,245,251,0,259,262,237,243,259],
[224,254,262,225,222,241,0,255,218,223,255],
[239,246,259,229,250,238,245,0,243,244,264],
[244,249,260,252,250,263,282,257,0,252,269],
[223,245,249,238,238,257,277,256,248,0,266],
[237,249,244,226,246,241,245,236,231,234,0]])



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
result = np.append(np.array([11, 500, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,254,257,253,248,259,249,278,260,273],
[235,0,262,261,256,274,268,261,261,249,251],
[246,238,0,254,257,241,254,244,264,247,259],
[243,239,246,0,247,253,247,242,260,236,240],
[247,244,243,253,0,262,256,248,258,240,262],
[252,226,259,247,238,0,255,253,252,240,261],
[241,232,246,253,244,245,0,257,251,252,264],
[251,239,256,258,252,247,243,0,266,229,259],
[222,239,236,240,242,248,249,234,0,234,240],
[240,251,253,264,260,260,248,271,266,0,277],
[227,249,241,260,238,239,236,241,260,223,0]])



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
result = np.append(np.array([11, 500, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,249,228,230,250,217,233,231,221,271],
[246,0,231,237,253,260,241,242,254,240,266],
[251,269,0,249,244,270,247,248,259,239,276],
[272,263,251,0,263,263,276,257,257,249,263],
[270,247,256,237,0,249,251,223,233,237,261],
[250,240,230,237,251,0,240,243,248,254,262],
[283,259,253,224,249,260,0,269,253,239,274],
[267,258,252,243,277,257,231,0,259,259,281],
[269,246,241,243,267,252,247,241,0,238,258],
[279,260,261,251,263,246,261,241,262,0,284],
[229,234,224,237,239,238,226,219,242,216,0]])



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
result = np.append(np.array([11, 500, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,240,238,219,222,208,197,233,197,255],
[265,0,301,251,238,248,244,257,253,274,266],
[260,199,0,209,227,230,214,181,235,212,236],
[262,249,291,0,231,218,234,240,239,235,251],
[281,262,273,269,0,257,244,236,242,234,269],
[278,252,270,282,243,0,244,220,226,263,251],
[292,256,286,266,256,256,0,235,226,238,270],
[303,243,319,260,264,280,265,0,272,258,269],
[267,247,265,261,258,274,274,228,0,231,277],
[303,226,288,265,266,237,262,242,269,0,254],
[245,234,264,249,231,249,230,231,223,246,0]])



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
result = np.append(np.array([11, 500, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,244,254,269,256,269,239,278,233,283],
[220,0,235,239,238,230,247,208,247,202,251],
[256,265,0,279,269,269,265,257,278,233,268],
[246,261,221,0,259,254,233,235,255,223,254],
[231,262,231,241,0,237,238,215,235,206,240],
[244,270,231,246,263,0,247,245,253,233,261],
[231,253,235,267,262,253,0,219,252,228,262],
[261,292,243,265,285,255,281,0,295,254,287],
[222,253,222,245,265,247,248,205,0,210,249],
[267,298,267,277,294,267,272,246,290,0,287],
[217,249,232,246,260,239,238,213,251,213,0]])



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
result = np.append(np.array([11, 500, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,244,263,251,261,251,258,251,251,246],
[242,0,242,239,240,257,255,244,233,229,232],
[256,258,0,259,246,257,263,247,250,255,250],
[237,261,241,0,243,249,245,253,246,237,239],
[249,260,254,257,0,276,262,266,255,253,260],
[239,243,243,251,224,0,252,238,235,235,240],
[249,245,237,255,238,248,0,243,243,239,247],
[242,256,253,247,234,262,257,0,246,253,242],
[249,267,250,254,245,265,257,254,0,261,239],
[249,271,245,263,247,265,261,247,239,0,257],
[254,268,250,261,240,260,253,258,261,243,0]])



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
result = np.append(np.array([11, 500, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,235,232,250,244,255,253,242,214,221],
[266,0,203,245,248,231,258,262,253,237,222],
[265,297,0,283,268,247,273,277,262,259,254],
[268,255,217,0,233,222,251,241,238,214,228],
[250,252,232,267,0,255,247,247,237,229,232],
[256,269,253,278,245,0,267,260,267,224,251],
[245,242,227,249,253,233,0,262,245,222,218],
[247,238,223,259,253,240,238,0,236,214,213],
[258,247,238,262,263,233,255,264,0,235,237],
[286,263,241,286,271,276,278,286,265,0,269],
[279,278,246,272,268,249,282,287,263,231,0]])



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
result = np.append(np.array([11, 500, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,265,265,249,241,257,252,270,254,257],
[242,0,256,246,249,255,263,248,261,251,259],
[235,244,0,246,243,241,243,233,266,248,238],
[235,254,254,0,249,251,242,243,262,260,244],
[251,251,257,251,0,249,244,247,269,249,251],
[259,245,259,249,251,0,236,245,277,246,250],
[243,237,257,258,256,264,0,243,269,246,240],
[248,252,267,257,253,255,257,0,270,264,265],
[230,239,234,238,231,223,231,230,0,235,236],
[246,249,252,240,251,254,254,236,265,0,241],
[243,241,262,256,249,250,260,235,264,259,0]])



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
result = np.append(np.array([11, 500, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,281,235,236,253,261,239,274,234,226],
[263,0,288,252,248,265,261,269,289,255,250],
[219,212,0,216,230,230,210,238,236,231,219],
[265,248,284,0,244,259,247,263,269,253,230],
[264,252,270,256,0,258,239,254,298,263,243],
[247,235,270,241,242,0,244,232,267,259,225],
[239,239,290,253,261,256,0,255,270,267,242],
[261,231,262,237,246,268,245,0,287,249,244],
[226,211,264,231,202,233,230,213,0,212,210],
[266,245,269,247,237,241,233,251,288,0,224],
[274,250,281,270,257,275,258,256,290,276,0]])



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
result = np.append(np.array([11, 500, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,252,268,249,248,250,276,265,246,272],
[236,0,246,246,258,236,236,249,262,242,255],
[248,254,0,242,251,226,251,275,252,233,267],
[232,254,258,0,267,251,264,271,274,258,271],
[251,242,249,233,0,244,258,276,273,251,276],
[252,264,274,249,256,0,259,277,248,252,254],
[250,264,249,236,242,241,0,266,269,253,261],
[224,251,225,229,224,223,234,0,244,246,253],
[235,238,248,226,227,252,231,256,0,237,254],
[254,258,267,242,249,248,247,254,263,0,277],
[228,245,233,229,224,246,239,247,246,223,0]])



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
result = np.append(np.array([11, 500, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,267,233,279,230,260,233,260,254,225],
[266,0,290,254,302,242,280,244,267,264,251],
[233,210,0,204,250,245,247,243,233,249,250],
[267,246,296,0,262,269,273,227,253,249,250],
[221,198,250,238,0,224,244,244,264,224,230],
[270,258,255,231,276,0,284,253,256,279,278],
[240,220,253,227,256,216,0,239,263,246,250],
[267,256,257,273,256,247,261,0,266,253,243],
[240,233,267,247,236,244,237,234,0,239,245],
[246,236,251,251,276,221,254,247,261,0,245],
[275,249,250,250,270,222,250,257,255,255,0]])



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
result = np.append(np.array([11, 500, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,242,249,256,248,262,255,249,250,244],
[242,0,256,254,261,255,254,256,269,258,255],
[258,244,0,255,273,247,243,251,279,262,256],
[251,246,245,0,287,249,253,262,261,268,260],
[244,239,227,213,0,239,231,250,241,251,245],
[252,245,253,251,261,0,255,246,266,254,244],
[238,246,257,247,269,245,0,240,260,243,242],
[245,244,249,238,250,254,260,0,276,252,245],
[251,231,221,239,259,234,240,224,0,256,229],
[250,242,238,232,249,246,257,248,244,0,231],
[256,245,244,240,255,256,258,255,271,269,0]])



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
result = np.append(np.array([11, 500, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,252,281,247,258,253,243,254,253,263],
[238,0,246,262,245,241,247,228,237,246,257],
[248,254,0,271,256,262,262,245,244,255,232],
[219,238,229,0,240,230,256,219,244,237,222],
[253,255,244,260,0,239,256,241,250,245,258],
[242,259,238,270,261,0,252,231,249,258,259],
[247,253,238,244,244,248,0,236,242,241,238],
[257,272,255,281,259,269,264,0,251,244,253],
[246,263,256,256,250,251,258,249,0,239,246],
[247,254,245,263,255,242,259,256,261,0,269],
[237,243,268,278,242,241,262,247,254,231,0]])



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
result = np.append(np.array([11, 500, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,297,309,298,285,250,244,320,310,274],
[264,0,325,303,296,298,234,192,339,318,276],
[203,175,0,246,234,206,189,185,268,271,207],
[191,197,254,0,213,270,237,244,286,265,229],
[202,204,266,287,0,219,188,256,288,312,225],
[215,202,294,230,281,0,246,199,268,258,224],
[250,266,311,263,312,254,0,217,276,317,243],
[256,308,315,256,244,301,283,0,314,336,257],
[180,161,232,214,212,232,224,186,0,266,241],
[190,182,229,235,188,242,183,164,234,0,234],
[226,224,293,271,275,276,257,243,259,266,0]])



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
result = np.append(np.array([11, 500, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,234,235,252,260,259,254,230,223,251],
[246,0,247,247,245,266,243,234,242,239,256],
[266,253,0,247,266,269,230,251,230,252,268],
[265,253,253,0,260,273,246,261,240,239,262],
[248,255,234,240,0,261,238,249,232,220,261],
[240,234,231,227,239,0,244,241,209,245,229],
[241,257,270,254,262,256,0,249,237,253,261],
[246,266,249,239,251,259,251,0,236,243,261],
[270,258,270,260,268,291,263,264,0,248,261],
[277,261,248,261,280,255,247,257,252,0,259],
[249,244,232,238,239,271,239,239,239,241,0]])



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
result = np.append(np.array([11, 500, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,223,260,219,219,285,238,275,220,235],
[276,0,235,285,238,251,230,235,222,258,262],
[277,265,0,307,252,279,285,218,296,261,284],
[240,215,193,0,210,260,264,195,257,225,228],
[281,262,248,290,0,236,287,272,248,281,272],
[281,249,221,240,264,0,283,214,238,251,286],
[215,270,215,236,213,217,0,220,264,244,206],
[262,265,282,305,228,286,280,0,252,228,332],
[225,278,204,243,252,262,236,248,0,255,284],
[280,242,239,275,219,249,256,272,245,0,283],
[265,238,216,272,228,214,294,168,216,217,0]])



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
result = np.append(np.array([11, 500, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,192,241,148,178,217,150,212,218,186],
[247,0,239,308,230,275,205,247,323,283,224],
[308,261,0,286,244,229,200,206,254,262,334],
[259,192,214,0,195,186,122,140,174,224,193],
[352,270,256,305,0,262,278,335,298,238,293],
[322,225,271,314,238,0,186,224,263,222,245],
[283,295,300,378,222,314,0,256,304,259,289],
[350,253,294,360,165,276,244,0,242,226,228],
[288,177,246,326,202,237,196,258,0,195,242],
[282,217,238,276,262,278,241,274,305,0,213],
[314,276,166,307,207,255,211,272,258,287,0]])



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
result = np.append(np.array([11, 500, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,265,271,258,254,256,247,238,251,270],
[252,0,269,284,270,253,248,253,251,246,261],
[235,231,0,260,259,260,235,247,250,242,254],
[229,216,240,0,238,240,214,229,229,227,239],
[242,230,241,262,0,255,248,250,253,262,261],
[246,247,240,260,245,0,255,246,264,235,272],
[244,252,265,286,252,245,0,241,236,258,277],
[253,247,253,271,250,254,259,0,264,230,269],
[262,249,250,271,247,236,264,236,0,255,264],
[249,254,258,273,238,265,242,270,245,0,269],
[230,239,246,261,239,228,223,231,236,231,0]])



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
result = np.append(np.array([11, 500, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,248,251,247,262,252,260,241,235,251],
[255,0,243,248,232,244,248,270,239,245,262],
[252,257,0,267,242,262,259,268,262,257,247],
[249,252,233,0,238,257,247,261,239,256,249],
[253,268,258,262,0,259,260,262,251,243,252],
[238,256,238,243,241,0,264,255,246,249,261],
[248,252,241,253,240,236,0,262,237,241,261],
[240,230,232,239,238,245,238,0,237,255,254],
[259,261,238,261,249,254,263,263,0,254,262],
[265,255,243,244,257,251,259,245,246,0,251],
[249,238,253,251,248,239,239,246,238,249,0]])



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
result = np.append(np.array([11, 500, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,246,282,291,268,263,256,246,266,284],
[237,0,251,281,251,256,261,236,264,282,256],
[254,249,0,244,252,206,266,226,243,287,246],
[218,219,256,0,262,249,258,221,259,267,238],
[209,249,248,238,0,187,215,192,216,253,230],
[232,244,294,251,313,0,310,291,279,288,286],
[237,239,234,242,285,190,0,273,216,279,279],
[244,264,274,279,308,209,227,0,249,296,238],
[254,236,257,241,284,221,284,251,0,282,282],
[234,218,213,233,247,212,221,204,218,0,213],
[216,244,254,262,270,214,221,262,218,287,0]])



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
result = np.append(np.array([11, 500, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,225,257,226,244,248,219,247,239,261],
[279,0,228,250,262,264,254,252,275,231,283],
[275,272,0,285,253,267,240,223,246,256,293],
[243,250,215,0,232,232,267,246,229,255,295],
[274,238,247,268,0,273,244,251,264,257,304],
[256,236,233,268,227,0,241,220,262,247,291],
[252,246,260,233,256,259,0,242,242,263,295],
[281,248,277,254,249,280,258,0,277,250,309],
[253,225,254,271,236,238,258,223,0,240,281],
[261,269,244,245,243,253,237,250,260,0,290],
[239,217,207,205,196,209,205,191,219,210,0]])



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
result = np.append(np.array([11, 500, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,261,254,246,270,233,246,262,239,256],
[241,0,240,224,232,228,250,244,257,229,238],
[239,260,0,238,241,244,265,244,279,239,245],
[246,276,262,0,248,248,259,251,264,251,258],
[254,268,259,252,0,243,262,246,285,239,271],
[230,272,256,252,257,0,251,264,250,253,265],
[267,250,235,241,238,249,0,246,262,246,255],
[254,256,256,249,254,236,254,0,258,254,249],
[238,243,221,236,215,250,238,242,0,221,251],
[261,271,261,249,261,247,254,246,279,0,254],
[244,262,255,242,229,235,245,251,249,246,0]])



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
result = np.append(np.array([11, 500, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,251,249,252,247,245,250,251,252,251],
[252,0,251,256,256,252,237,245,244,247,237],
[249,249,0,248,237,258,232,233,243,244,242],
[251,244,252,0,262,269,248,244,253,257,244],
[248,244,263,238,0,253,239,254,235,252,241],
[253,248,242,231,247,0,249,249,243,262,244],
[255,263,268,252,261,251,0,266,247,254,262],
[250,255,267,256,246,251,234,0,247,257,257],
[249,256,257,247,265,257,253,253,0,257,251],
[248,253,256,243,248,238,246,243,243,0,239],
[249,263,258,256,259,256,238,243,249,261,0]])



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
result = np.append(np.array([11, 500, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,250,277,235,255,249,270,244,253,262],
[267,0,249,249,244,251,243,276,250,285,251],
[250,251,0,269,231,230,261,281,230,262,249],
[223,251,231,0,232,236,232,249,239,230,232],
[265,256,269,268,0,242,255,282,254,264,256],
[245,249,270,264,258,0,254,281,273,276,237],
[251,257,239,268,245,246,0,277,228,259,243],
[230,224,219,251,218,219,223,0,229,262,233],
[256,250,270,261,246,227,272,271,0,277,238],
[247,215,238,270,236,224,241,238,223,0,211],
[238,249,251,268,244,263,257,267,262,289,0]])



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
result = np.append(np.array([11, 500, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,253,256,248,259,283,245,235,245,274],
[256,0,279,256,277,278,271,273,254,243,278],
[247,221,0,241,249,259,244,247,247,244,253],
[244,244,259,0,247,259,255,277,248,242,248],
[252,223,251,253,0,265,272,248,247,257,257],
[241,222,241,241,235,0,270,266,247,258,268],
[217,229,256,245,228,230,0,232,234,248,229],
[255,227,253,223,252,234,268,0,241,255,251],
[265,246,253,252,253,253,266,259,0,236,258],
[255,257,256,258,243,242,252,245,264,0,266],
[226,222,247,252,243,232,271,249,242,234,0]])



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
result = np.append(np.array([11, 500, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,248,273,282,268,248,285,261,246,251],
[236,0,245,236,242,233,222,273,233,236,231],
[252,255,0,263,273,244,245,271,244,252,240],
[227,264,237,0,261,246,238,270,238,241,244],
[218,258,227,239,0,226,210,247,240,241,215],
[232,267,256,254,274,0,252,277,261,252,231],
[252,278,255,262,290,248,0,274,251,245,236],
[215,227,229,230,253,223,226,0,238,221,221],
[239,267,256,262,260,239,249,262,0,247,265],
[254,264,248,259,259,248,255,279,253,0,236],
[249,269,260,256,285,269,264,279,235,264,0]])



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
result = np.append(np.array([11, 500, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,253,241,289,257,227,249,241,250,243],
[245,0,248,226,246,212,220,238,217,226,241],
[247,252,0,212,258,215,239,251,240,225,218],
[259,274,288,0,246,244,246,240,263,262,269],
[211,254,242,254,0,231,239,249,259,247,278],
[243,288,285,256,269,0,239,251,277,254,263],
[273,280,261,254,261,261,0,246,256,249,259],
[251,262,249,260,251,249,254,0,248,240,240],
[259,283,260,237,241,223,244,252,0,265,276],
[250,274,275,238,253,246,251,260,235,0,253],
[257,259,282,231,222,237,241,260,224,247,0]])



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
result = np.append(np.array([11, 500, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,236,236,240,242,238,234,231,236,244],
[266,0,260,261,268,261,261,243,269,256,263],
[264,240,0,266,248,257,254,233,244,237,251],
[264,239,234,0,257,260,245,246,256,245,240],
[260,232,252,243,0,258,258,244,250,239,249],
[258,239,243,240,242,0,252,256,232,241,253],
[262,239,246,255,242,248,0,233,260,239,253],
[266,257,267,254,256,244,267,0,263,260,252],
[269,231,256,244,250,268,240,237,0,249,245],
[264,244,263,255,261,259,261,240,251,0,263],
[256,237,249,260,251,247,247,248,255,237,0]])



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
result = np.append(np.array([11, 500, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,269,214,255,264,261,253,265,241,255],
[269,0,258,253,259,270,286,282,257,243,277],
[231,242,0,235,236,267,257,269,268,246,272],
[286,247,265,0,251,262,281,267,269,246,260],
[245,241,264,249,0,258,289,295,258,228,253],
[236,230,233,238,242,0,263,247,209,238,217],
[239,214,243,219,211,237,0,250,254,225,247],
[247,218,231,233,205,253,250,0,251,233,252],
[235,243,232,231,242,291,246,249,0,252,254],
[259,257,254,254,272,262,275,267,248,0,247],
[245,223,228,240,247,283,253,248,246,253,0]])



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
result = np.append(np.array([11, 500, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,257,245,254,240,247,242,252,245,255],
[252,0,268,263,260,244,266,264,258,241,275],
[243,232,0,249,250,246,241,242,236,251,246],
[255,237,251,0,242,243,258,253,254,244,248],
[246,240,250,258,0,233,256,247,247,242,255],
[260,256,254,257,267,0,257,260,265,250,260],
[253,234,259,242,244,243,0,247,255,246,258],
[258,236,258,247,253,240,253,0,267,231,259],
[248,242,264,246,253,235,245,233,0,233,241],
[255,259,249,256,258,250,254,269,267,0,249],
[245,225,254,252,245,240,242,241,259,251,0]])



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
result = np.append(np.array([11, 500, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,252,231,247,260,276,248,280,258,251],
[251,0,257,263,267,260,242,255,278,270,257],
[248,243,0,242,290,260,259,245,291,238,238],
[269,237,258,0,277,240,251,207,295,265,260],
[253,233,210,223,0,228,241,226,261,252,244],
[240,240,240,260,272,0,227,268,288,268,242],
[224,258,241,249,259,273,0,251,299,245,263],
[252,245,255,293,274,232,249,0,278,250,268],
[220,222,209,205,239,212,201,222,0,212,214],
[242,230,262,235,248,232,255,250,288,0,255],
[249,243,262,240,256,258,237,232,286,245,0]])



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
result = np.append(np.array([11, 500, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,215,216,234,224,244,239,252,261,216,247],
[285,0,282,262,248,255,269,267,282,244,283],
[284,218,0,249,242,244,242,281,256,259,273],
[266,238,251,0,229,237,248,241,267,229,278],
[276,252,258,271,0,264,224,288,267,261,274],
[256,245,256,263,236,0,236,256,270,238,284],
[261,231,258,252,276,264,0,268,296,269,283],
[248,233,219,259,212,244,232,0,246,225,242],
[239,218,244,233,233,230,204,254,0,217,246],
[284,256,241,271,239,262,231,275,283,0,264],
[253,217,227,222,226,216,217,258,254,236,0]])



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
result = np.append(np.array([11, 500, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,240,237,240,235,258,254,252,246,249],
[254,0,249,263,256,248,249,249,250,257,236],
[260,251,0,262,264,245,277,271,267,263,253],
[263,237,238,0,242,238,268,258,260,249,242],
[260,244,236,258,0,256,252,263,270,258,245],
[265,252,255,262,244,0,266,256,270,262,255],
[242,251,223,232,248,234,0,256,266,260,248],
[246,251,229,242,237,244,244,0,253,243,248],
[248,250,233,240,230,230,234,247,0,247,240],
[254,243,237,251,242,238,240,257,253,0,259],
[251,264,247,258,255,245,252,252,260,241,0]])



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
result = np.append(np.array([11, 500, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,244,234,231,228,270,239,261,247,249],
[263,0,253,255,247,258,293,251,280,245,270],
[256,247,0,251,251,234,273,243,272,242,246],
[266,245,249,0,245,257,268,244,258,235,247],
[269,253,249,255,0,271,278,257,253,249,246],
[272,242,266,243,229,0,266,252,257,243,242],
[230,207,227,232,222,234,0,230,238,226,224],
[261,249,257,256,243,248,270,0,258,253,269],
[239,220,228,242,247,243,262,242,0,236,238],
[253,255,258,265,251,257,274,247,264,0,251],
[251,230,254,253,254,258,276,231,262,249,0]])



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
result = np.append(np.array([11, 500, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,287,226,241,249,246,232,248,254,262,235],
[213,0,223,237,204,214,249,246,209,219,218],
[274,277,0,285,257,273,254,277,267,276,240],
[259,263,215,0,245,273,269,261,237,260,233],
[251,296,243,255,0,260,248,277,268,254,250],
[254,286,227,227,240,0,254,258,227,258,216],
[268,251,246,231,252,246,0,258,253,265,223],
[252,254,223,239,223,242,242,0,223,243,213],
[246,291,233,263,232,273,247,277,0,259,210],
[238,281,224,240,246,242,235,257,241,0,224],
[265,282,260,267,250,284,277,287,290,276,0]])



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
result = np.append(np.array([11, 500, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,241,264,254,246,217,240,249,244,239],
[261,0,260,262,259,258,242,259,245,258,243],
[259,240,0,260,242,255,236,238,246,245,248],
[236,238,240,0,257,235,239,240,236,248,236],
[246,241,258,243,0,255,242,240,246,253,246],
[254,242,245,265,245,0,250,243,251,243,247],
[283,258,264,261,258,250,0,264,252,252,241],
[260,241,262,260,260,257,236,0,242,245,255],
[251,255,254,264,254,249,248,258,0,249,261],
[256,242,255,252,247,257,248,255,251,0,240],
[261,257,252,264,254,253,259,245,239,260,0]])



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
result = np.append(np.array([11, 500, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,249,244,253,266,253,265,251,260,258],
[244,0,260,256,265,264,272,281,253,258,256],
[251,240,0,264,267,276,257,271,247,269,267],
[256,244,236,0,254,264,257,268,239,255,249],
[247,235,233,246,0,261,251,260,250,252,242],
[234,236,224,236,239,0,245,248,221,236,236],
[247,228,243,243,249,255,0,261,236,260,254],
[235,219,229,232,240,252,239,0,229,249,238],
[249,247,253,261,250,279,264,271,0,260,256],
[240,242,231,245,248,264,240,251,240,0,252],
[242,244,233,251,258,264,246,262,244,248,0]])



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
result = np.append(np.array([11, 500, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,215,247,251,236,220,247,221,229,236,236],
[285,0,266,259,252,248,254,255,253,238,253],
[253,234,0,255,253,253,269,254,261,237,252],
[249,241,245,0,268,212,237,260,241,232,233],
[264,248,247,232,0,240,245,253,233,232,222],
[280,252,247,288,260,0,267,253,262,255,242],
[253,246,231,263,255,233,0,242,269,245,243],
[279,245,246,240,247,247,258,0,245,252,251],
[271,247,239,259,267,238,231,255,0,219,237],
[264,262,263,268,268,245,255,248,281,0,246],
[264,247,248,267,278,258,257,249,263,254,0]])



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
result = np.append(np.array([11, 500, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,281,258,245,267,295,250,276,296,277],
[226,0,258,242,225,232,251,217,248,257,213],
[219,242,0,232,197,242,237,204,222,257,242],
[242,258,268,0,236,241,267,226,226,269,244],
[255,275,303,264,0,278,295,238,283,296,262],
[233,268,258,259,222,0,264,239,269,297,242],
[205,249,263,233,205,236,0,227,249,280,226],
[250,283,296,274,262,261,273,0,283,292,277],
[224,252,278,274,217,231,251,217,0,260,246],
[204,243,243,231,204,203,220,208,240,0,215],
[223,287,258,256,238,258,274,223,254,285,0]])



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
result = np.append(np.array([11, 500, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,202,202,247,304,227,127,248,266,363,186],
[298,0,265,347,242,175,62,350,326,462,247],
[298,235,0,347,264,296,161,298,235,283,299],
[253,153,153,0,318,312,201,199,115,300,136],
[196,258,236,182,0,273,62,183,200,297,121],
[273,325,204,188,227,0,265,189,189,325,188],
[373,438,339,299,438,235,0,302,300,425,299],
[252,150,202,301,317,311,198,0,179,362,199],
[234,174,265,385,300,311,200,321,0,287,249],
[137,38,217,200,203,175,75,138,213,0,200],
[314,253,201,364,379,312,201,301,251,300,0]])



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
result = np.append(np.array([11, 500, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,237,231,248,226,235,234,244,246,263],
[280,0,263,249,257,250,248,257,265,262,284],
[263,237,0,251,249,240,230,236,279,256,260],
[269,251,249,0,260,255,246,250,260,248,273],
[252,243,251,240,0,256,228,240,270,257,242],
[274,250,260,245,244,0,250,252,248,263,266],
[265,252,270,254,272,250,0,244,278,266,280],
[266,243,264,250,260,248,256,0,272,234,275],
[256,235,221,240,230,252,222,228,0,255,276],
[254,238,244,252,243,237,234,266,245,0,266],
[237,216,240,227,258,234,220,225,224,234,0]])



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
result = np.append(np.array([11, 500, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,308,270,287,246,323,303,278,287,218,249],
[192,0,118,295,176,239,219,283,297,244,222],
[230,382,0,360,274,295,328,333,312,331,326],
[213,205,140,0,167,222,229,284,182,205,172],
[254,324,226,333,0,286,228,312,314,329,321],
[177,261,205,278,214,0,247,245,229,215,212],
[197,281,172,271,272,253,0,364,292,274,276],
[222,217,167,216,188,255,136,0,185,245,174],
[213,203,188,318,186,271,208,315,0,223,209],
[282,256,169,295,171,285,226,255,277,0,221],
[251,278,174,328,179,288,224,326,291,279,0]])



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
result = np.append(np.array([11, 500, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,260,231,202,231,282,200,231,231,229],
[277,0,312,279,300,331,352,246,331,243,304],
[240,188,0,274,273,276,266,205,334,229,229],
[269,221,226,0,270,301,257,225,262,250,216],
[298,200,227,230,0,241,242,209,297,245,224],
[269,169,224,199,259,0,293,227,284,189,267],
[218,148,234,243,258,207,0,229,298,216,167],
[300,254,295,275,291,273,271,0,312,280,236],
[269,169,166,238,203,216,202,188,0,214,187],
[269,257,271,250,255,311,284,220,286,0,251],
[271,196,271,284,276,233,333,264,313,249,0]])



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
result = np.append(np.array([11, 500, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,234,285,263,254,240,228,238,233,266],
[231,0,196,222,248,214,206,191,225,239,220],
[266,304,0,281,284,240,264,244,238,237,243],
[215,278,219,0,228,229,246,235,226,243,235],
[237,252,216,272,0,247,234,184,232,253,239],
[246,286,260,271,253,0,220,231,254,251,260],
[260,294,236,254,266,280,0,248,252,259,236],
[272,309,256,265,316,269,252,0,285,249,254],
[262,275,262,274,268,246,248,215,0,254,256],
[267,261,263,257,247,249,241,251,246,0,234],
[234,280,257,265,261,240,264,246,244,266,0]])



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
result = np.append(np.array([11, 500, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,254,258,238,266,244,234,226,229,250],
[258,0,274,250,233,256,250,244,253,233,264],
[246,226,0,253,236,242,237,235,240,214,227],
[242,250,247,0,221,240,235,238,224,234,247],
[262,267,264,279,0,270,252,263,234,231,252],
[234,244,258,260,230,0,223,230,236,221,242],
[256,250,263,265,248,277,0,243,241,235,246],
[266,256,265,262,237,270,257,0,262,243,256],
[274,247,260,276,266,264,259,238,0,251,264],
[271,267,286,266,269,279,265,257,249,0,284],
[250,236,273,253,248,258,254,244,236,216,0]])



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
result = np.append(np.array([11, 500, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,274,253,271,268,268,282,255,287,267],
[252,0,243,238,280,258,260,256,237,258,252],
[226,257,0,255,276,238,253,268,250,268,263],
[247,262,245,0,287,258,273,263,235,267,268],
[229,220,224,213,0,239,239,245,212,251,243],
[232,242,262,242,261,0,264,242,236,270,251],
[232,240,247,227,261,236,0,253,239,261,249],
[218,244,232,237,255,258,247,0,231,262,243],
[245,263,250,265,288,264,261,269,0,261,248],
[213,242,232,233,249,230,239,238,239,0,235],
[233,248,237,232,257,249,251,257,252,265,0]])



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
result = np.append(np.array([11, 500, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_11_500.csv", index=False, header=False)