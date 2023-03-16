
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,272,249,241,238,244,269,251,261],
[229,0,231,250,238,242,251,258,227],
[252,270,0,280,249,260,267,287,257],
[260,251,221,0,236,261,265,247,242],
[263,263,252,265,0,248,276,266,255],
[257,259,241,240,253,0,263,256,245],
[232,250,234,236,225,238,0,245,232],
[250,243,214,254,235,245,256,0,228],
[240,274,244,259,246,256,269,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,260,268,270,253,275,262,249],
[234,0,245,256,241,227,244,255,232],
[241,256,0,261,251,235,254,256,235],
[233,245,240,0,244,245,237,249,237],
[231,260,250,257,0,244,249,249,241],
[248,274,266,256,257,0,251,272,247],
[226,257,247,264,252,250,0,246,252],
[239,246,245,252,252,229,255,0,228],
[252,269,266,264,260,254,249,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,248,260,266,253,262,266,256],
[243,0,248,264,254,249,261,265,251],
[253,253,0,268,263,250,258,270,255],
[241,237,233,0,257,241,263,261,227],
[235,247,238,244,0,234,259,259,238],
[248,252,251,260,267,0,260,277,267],
[239,240,243,238,242,241,0,244,233],
[235,236,231,240,242,224,257,0,236],
[245,250,246,274,263,234,268,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,257,252,263,260,266,245,253],
[247,0,228,247,237,251,251,232,243],
[244,273,0,246,237,265,263,254,256],
[249,254,255,0,254,262,240,242,244],
[238,264,264,247,0,250,255,237,248],
[241,250,236,239,251,0,260,241,260],
[235,250,238,261,246,241,0,242,262],
[256,269,247,259,264,260,259,0,267],
[248,258,245,257,253,241,239,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,241,241,224,246,209,231,224],
[255,0,260,247,242,241,245,256,214],
[260,241,0,234,239,236,214,235,254],
[260,254,267,0,249,292,223,244,225],
[277,259,262,252,0,252,234,240,231],
[255,260,265,209,249,0,232,247,221],
[292,256,287,278,267,269,0,261,247],
[270,245,266,257,261,254,240,0,261],
[277,287,247,276,270,280,254,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,264,229,246,297,295,256,254],
[254,0,225,211,244,288,267,264,249],
[237,276,0,201,244,263,275,255,262],
[272,290,300,0,292,305,301,290,249],
[255,257,257,209,0,263,267,245,259],
[204,213,238,196,238,0,235,202,232],
[206,234,226,200,234,266,0,220,212],
[245,237,246,211,256,299,281,0,239],
[247,252,239,252,242,269,289,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,254,246,266,289,283,267,265],
[245,0,270,263,268,254,282,292,276],
[247,231,0,249,253,247,280,276,225],
[255,238,252,0,271,276,262,274,246],
[235,233,248,230,0,253,273,251,256],
[212,247,254,225,248,0,257,253,237],
[218,219,221,239,228,244,0,257,238],
[234,209,225,227,250,248,244,0,223],
[236,225,276,255,245,264,263,278,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,242,251,231,237,236,186,259],
[248,0,239,238,225,264,240,238,247],
[259,262,0,269,232,243,255,256,283],
[250,263,232,0,235,227,261,183,258],
[270,276,269,266,0,251,255,228,303],
[264,237,258,274,250,0,263,241,273],
[265,261,246,240,246,238,0,222,255],
[315,263,245,318,273,260,279,0,305],
[242,254,218,243,198,228,246,196,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,249,267,280,254,286,277,281],
[240,0,249,267,237,255,287,264,248],
[252,252,0,272,227,245,273,267,276],
[234,234,229,0,251,230,267,247,248],
[221,264,274,250,0,259,280,268,298],
[247,246,256,271,242,0,292,264,260],
[215,214,228,234,221,209,0,212,238],
[224,237,234,254,233,237,289,0,274],
[220,253,225,253,203,241,263,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,241,298,264,284,260,269,268],
[248,0,233,282,244,269,247,276,245],
[260,268,0,294,249,283,255,291,259],
[203,219,207,0,216,240,229,238,244],
[237,257,252,285,0,277,267,281,255],
[217,232,218,261,224,0,226,257,229],
[241,254,246,272,234,275,0,290,262],
[232,225,210,263,220,244,211,0,235],
[233,256,242,257,246,272,239,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,278,254,268,274,261,247,276],
[229,0,237,241,254,244,239,238,239],
[223,264,0,231,233,246,231,258,258],
[247,260,270,0,252,256,238,263,259],
[233,247,268,249,0,236,228,234,249],
[227,257,255,245,265,0,226,261,239],
[240,262,270,263,273,275,0,259,280],
[254,263,243,238,267,240,242,0,252],
[225,262,243,242,252,262,221,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,219,247,242,238,242,234,229],
[255,0,237,265,240,240,253,244,252],
[282,264,0,259,252,260,246,255,240],
[254,236,242,0,238,241,266,242,226],
[259,261,249,263,0,249,277,244,252],
[263,261,241,260,252,0,258,247,225],
[259,248,255,235,224,243,0,232,223],
[267,257,246,259,257,254,269,0,232],
[272,249,261,275,249,276,278,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,233,226,227,260,253,248,216],
[260,0,251,256,251,265,278,263,237],
[268,250,0,244,231,250,244,248,250],
[275,245,257,0,243,258,261,268,243],
[274,250,270,258,0,267,253,264,254],
[241,236,251,243,234,0,252,247,228],
[248,223,257,240,248,249,0,238,233],
[253,238,253,233,237,254,263,0,240],
[285,264,251,258,247,273,268,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,205,251,206,228,225,271,293,212],
[296,0,234,231,290,262,263,317,273],
[250,267,0,257,326,249,281,300,254],
[295,270,244,0,258,208,274,280,246],
[273,211,175,243,0,235,235,287,228],
[276,239,252,293,266,0,277,293,280],
[230,238,220,227,266,224,0,295,270],
[208,184,201,221,214,208,206,0,211],
[289,228,247,255,273,221,231,290,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,310,294,299,269,260,246,307,303],
[191,0,277,277,212,206,239,227,227],
[207,224,0,310,229,217,230,246,233],
[202,224,191,0,181,205,207,263,169],
[232,289,272,320,0,222,246,257,249],
[241,295,284,296,279,0,257,309,209],
[255,262,271,294,255,244,0,236,295],
[194,274,255,238,244,192,265,0,247],
[198,274,268,332,252,292,206,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,249,256,240,248,252,253,263],
[247,0,257,248,236,256,249,250,263],
[252,244,0,226,251,235,257,244,283],
[245,253,275,0,235,254,245,267,279],
[261,265,250,266,0,253,255,243,268],
[253,245,266,247,248,0,256,243,266],
[249,252,244,256,246,245,0,244,264],
[248,251,257,234,258,258,257,0,256],
[238,238,218,222,233,235,237,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,295,247,215,277,272,250,237,265],
[206,0,246,237,214,196,207,211,235],
[254,255,0,247,240,242,239,271,239],
[286,264,254,0,267,247,264,282,219],
[224,287,261,234,0,207,183,198,264],
[229,305,259,254,294,0,251,200,304],
[251,294,262,237,318,250,0,246,285],
[264,290,230,219,303,301,255,0,264],
[236,266,262,282,237,197,216,237,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,249,253,263,255,250,251,244],
[237,0,240,252,249,252,249,252,243],
[252,261,0,266,242,252,269,249,247],
[248,249,235,0,252,252,243,265,243],
[238,252,259,249,0,261,253,250,256],
[246,249,249,249,240,0,246,261,241],
[251,252,232,258,248,255,0,252,243],
[250,249,252,236,251,240,249,0,247],
[257,258,254,258,245,260,258,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,391,288,254,356,288,103,172,110],
[110,0,193,254,254,110,110,172,110],
[213,308,0,315,315,212,69,213,151],
[247,247,186,0,247,103,103,247,254],
[145,247,186,254,0,288,103,62,90],
[213,391,289,398,213,0,69,213,213],
[398,391,432,398,398,432,0,213,234],
[329,329,288,254,439,288,288,0,192],
[391,391,350,247,411,288,267,309,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,225,270,228,231,214,229,235],
[285,0,269,278,249,250,251,273,252],
[276,232,0,269,230,264,225,268,246],
[231,223,232,0,223,244,219,240,255],
[273,252,271,278,0,269,245,264,248],
[270,251,237,257,232,0,240,236,232],
[287,250,276,282,256,261,0,276,279],
[272,228,233,261,237,265,225,0,271],
[266,249,255,246,253,269,222,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,298,257,267,274,228,241,292],
[228,0,249,237,241,240,233,242,262],
[203,252,0,244,217,268,214,235,243],
[244,264,257,0,255,271,209,265,246],
[234,260,284,246,0,292,249,276,275],
[227,261,233,230,209,0,227,227,251],
[273,268,287,292,252,274,0,238,268],
[260,259,266,236,225,274,263,0,246],
[209,239,258,255,226,250,233,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,265,337,247,284,340,209,284],
[279,0,214,260,260,235,334,259,258],
[236,287,0,278,216,229,322,237,209],
[164,241,223,0,206,238,242,162,198],
[254,241,285,295,0,244,304,237,188],
[217,266,272,263,257,0,316,248,173],
[161,167,179,259,197,185,0,176,138],
[292,242,264,339,264,253,325,0,204],
[217,243,292,303,313,328,363,297,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,262,259,252,243,245,262,269],
[257,0,246,231,242,254,238,252,265],
[239,255,0,244,254,253,234,252,260],
[242,270,257,0,258,268,255,266,277],
[249,259,247,243,0,235,229,254,256],
[258,247,248,233,266,0,244,243,279],
[256,263,267,246,272,257,0,260,265],
[239,249,249,235,247,258,241,0,245],
[232,236,241,224,245,222,236,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,326,234,296,270,286,272,257],
[229,0,261,241,312,276,255,291,252],
[175,240,0,225,262,230,209,248,236],
[267,260,276,0,266,222,259,271,275],
[205,189,239,235,0,209,191,247,221],
[231,225,271,279,292,0,294,306,295],
[215,246,292,242,310,207,0,273,265],
[229,210,253,230,254,195,228,0,254],
[244,249,265,226,280,206,236,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,252,244,236,248,247,212,229],
[284,0,257,254,272,279,234,256,229],
[249,244,0,259,270,272,245,241,241],
[257,247,242,0,259,278,281,254,247],
[265,229,231,242,0,260,238,230,245],
[253,222,229,223,241,0,281,248,219],
[254,267,256,220,263,220,0,261,238],
[289,245,260,247,271,253,240,0,256],
[272,272,260,254,256,282,263,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,397,190,429,212,332,190,346],
[228,0,359,242,311,336,346,242,228],
[104,142,0,72,194,94,142,190,156],
[311,259,429,0,311,316,142,426,311],
[72,190,307,190,0,284,294,190,294],
[289,165,407,185,217,0,214,384,289],
[169,155,359,359,207,287,0,359,345],
[311,259,311,75,311,117,142,0,311],
[155,273,345,190,207,212,156,190,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,243,246,270,251,247,262,242],
[254,0,220,246,279,260,259,239,240],
[258,281,0,278,240,272,262,218,254],
[255,255,223,0,265,264,225,233,228],
[231,222,261,236,0,245,251,205,234],
[250,241,229,237,256,0,252,204,247],
[254,242,239,276,250,249,0,244,263],
[239,262,283,268,296,297,257,0,286],
[259,261,247,273,267,254,238,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,248,255,247,241,243,236,249],
[255,0,265,266,274,258,262,244,251],
[253,236,0,233,254,236,254,252,246],
[246,235,268,0,254,239,249,246,248],
[254,227,247,247,0,245,245,244,228],
[260,243,265,262,256,0,246,252,248],
[258,239,247,252,256,255,0,259,248],
[265,257,249,255,257,249,242,0,245],
[252,250,255,253,273,253,253,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,285,294,291,246,246,279,291],
[226,0,295,257,249,257,209,291,290],
[216,206,0,241,219,233,216,237,271],
[207,244,260,0,214,216,189,250,253],
[210,252,282,287,0,246,241,279,255],
[255,244,268,285,255,0,255,249,289],
[255,292,285,312,260,246,0,288,291],
[222,210,264,251,222,252,213,0,250],
[210,211,230,248,246,212,210,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,305,259,247,251,270,249,277,269],
[196,0,228,208,254,247,212,233,249],
[242,273,0,222,226,222,270,255,260],
[254,293,279,0,235,242,240,249,260],
[250,247,275,266,0,267,246,263,291],
[231,254,279,259,234,0,238,235,285],
[252,289,231,261,255,263,0,256,291],
[224,268,246,252,238,266,245,0,269],
[232,252,241,241,210,216,210,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,241,255,240,221,215,235,267],
[268,0,240,279,251,244,224,233,259],
[260,261,0,243,242,257,210,234,261],
[246,222,258,0,233,221,220,204,213],
[261,250,259,268,0,237,230,223,260],
[280,257,244,280,264,0,261,262,281],
[286,277,291,281,271,240,0,247,281],
[266,268,267,297,278,239,254,0,277],
[234,242,240,288,241,220,220,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,267,248,237,233,231,241,250],
[259,0,274,288,252,270,260,248,252],
[234,227,0,244,240,224,249,246,258],
[253,213,257,0,213,246,231,212,236],
[264,249,261,288,0,276,262,253,255],
[268,231,277,255,225,0,238,248,268],
[270,241,252,270,239,263,0,245,261],
[260,253,255,289,248,253,256,0,255],
[251,249,243,265,246,233,240,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,273,239,223,263,206,252,260],
[268,0,295,233,256,278,255,277,268],
[228,206,0,230,206,243,219,229,237],
[262,268,271,0,242,302,229,273,265],
[278,245,295,259,0,297,242,276,278],
[238,223,258,199,204,0,228,248,246],
[295,246,282,272,259,273,0,273,277],
[249,224,272,228,225,253,228,0,237],
[241,233,264,236,223,255,224,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,245,224,251,249,247,221,255],
[273,0,264,250,245,234,256,247,267],
[256,237,0,228,243,230,261,249,264],
[277,251,273,0,270,220,268,267,284],
[250,256,258,231,0,233,261,254,270],
[252,267,271,281,268,0,286,233,274],
[254,245,240,233,240,215,0,237,232],
[280,254,252,234,247,268,264,0,280],
[246,234,237,217,231,227,269,221,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,253,229,250,232,237,258,256],
[253,0,246,237,230,236,230,257,242],
[248,255,0,239,249,231,243,257,248],
[272,264,262,0,251,244,245,269,258],
[251,271,252,250,0,234,239,255,249],
[269,265,270,257,267,0,258,265,248],
[264,271,258,256,262,243,0,278,256],
[243,244,244,232,246,236,223,0,229],
[245,259,253,243,252,253,245,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,263,252,253,246,263,267,258],
[237,0,269,265,264,259,254,260,253],
[238,232,0,264,222,232,268,227,232],
[249,236,237,0,232,250,252,248,250],
[248,237,279,269,0,255,274,263,264],
[255,242,269,251,246,0,279,248,272],
[238,247,233,249,227,222,0,254,245],
[234,241,274,253,238,253,247,0,233],
[243,248,269,251,237,229,256,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,234,237,232,249,226,229,237],
[255,0,258,257,262,255,241,263,262],
[267,243,0,272,251,263,252,243,246],
[264,244,229,0,235,271,237,225,262],
[269,239,250,266,0,279,262,258,265],
[252,246,238,230,222,0,249,233,245],
[275,260,249,264,239,252,0,239,262],
[272,238,258,276,243,268,262,0,260],
[264,239,255,239,236,256,239,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,231,255,227,250,256,227,244],
[226,0,234,236,256,243,251,232,237],
[270,267,0,249,263,243,256,260,247],
[246,265,252,0,254,249,256,265,277],
[274,245,238,247,0,232,251,239,242],
[251,258,258,252,269,0,244,253,264],
[245,250,245,245,250,257,0,236,239],
[274,269,241,236,262,248,265,0,266],
[257,264,254,224,259,237,262,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,250,235,238,248,258,237,248],
[249,0,244,226,242,240,247,242,243],
[251,257,0,242,241,252,259,241,261],
[266,275,259,0,252,258,270,238,251],
[263,259,260,249,0,253,247,246,248],
[253,261,249,243,248,0,279,244,251],
[243,254,242,231,254,222,0,253,245],
[264,259,260,263,255,257,248,0,253],
[253,258,240,250,253,250,256,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,257,280,268,285,282,248,237],
[250,0,261,248,242,297,276,274,246],
[244,240,0,221,228,268,253,224,207],
[221,253,280,0,262,268,263,253,214],
[233,259,273,239,0,277,256,262,254],
[216,204,233,233,224,0,241,275,222],
[219,225,248,238,245,260,0,223,251],
[253,227,277,248,239,226,278,0,226],
[264,255,294,287,247,279,250,275,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,262,252,259,275,243,253,249],
[254,0,227,247,269,251,238,229,254],
[239,274,0,258,273,278,252,249,257],
[249,254,243,0,272,250,249,262,262],
[242,232,228,229,0,264,242,215,243],
[226,250,223,251,237,0,241,221,245],
[258,263,249,252,259,260,0,251,261],
[248,272,252,239,286,280,250,0,245],
[252,247,244,239,258,256,240,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,225,245,236,257,251,231,249],
[269,0,248,250,241,264,250,245,261],
[276,253,0,266,254,268,258,249,277],
[256,251,235,0,252,266,253,244,261],
[265,260,247,249,0,252,247,262,264],
[244,237,233,235,249,0,266,234,254],
[250,251,243,248,254,235,0,243,253],
[270,256,252,257,239,267,258,0,266],
[252,240,224,240,237,247,248,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,137,184,223,117,221,194,273],
[271,0,192,245,257,223,271,192,276],
[364,309,0,299,275,253,241,288,275],
[317,256,202,0,279,232,266,230,157],
[278,244,226,222,0,230,211,270,290],
[384,278,248,269,271,0,247,251,349],
[280,230,260,235,290,254,0,210,251],
[307,309,213,271,231,250,291,0,304],
[228,225,226,344,211,152,250,197,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,255,246,246,260,243,244,257],
[260,0,254,265,251,276,261,245,233],
[246,247,0,248,242,257,268,232,233],
[255,236,253,0,231,273,253,227,224],
[255,250,259,270,0,282,268,250,245],
[241,225,244,228,219,0,247,218,217],
[258,240,233,248,233,254,0,221,227],
[257,256,269,274,251,283,280,0,249],
[244,268,268,277,256,284,274,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,259,246,258,267,240,257,253],
[241,0,257,252,271,251,251,253,252],
[242,244,0,249,249,247,233,246,250],
[255,249,252,0,265,269,242,245,249],
[243,230,252,236,0,248,239,254,239],
[234,250,254,232,253,0,245,252,243],
[261,250,268,259,262,256,0,268,252],
[244,248,255,256,247,249,233,0,242],
[248,249,251,252,262,258,249,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,193,274,231,237,229,238,241],
[243,0,201,246,230,220,239,248,218],
[308,300,0,296,246,268,306,277,268],
[227,255,205,0,250,219,237,217,206],
[270,271,255,251,0,216,267,251,223],
[264,281,233,282,285,0,293,246,256],
[272,262,195,264,234,208,0,246,213],
[263,253,224,284,250,255,255,0,241],
[260,283,233,295,278,245,288,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,258,261,277,253,257,286,257],
[259,0,269,271,275,252,262,276,233],
[243,232,0,265,273,257,235,260,230],
[240,230,236,0,230,249,245,270,234],
[224,226,228,271,0,239,253,262,218],
[248,249,244,252,262,0,247,265,241],
[244,239,266,256,248,254,0,282,239],
[215,225,241,231,239,236,219,0,215],
[244,268,271,267,283,260,262,286,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,245,259,272,259,269,267,257],
[260,0,239,255,246,238,263,260,265],
[256,262,0,268,270,276,274,284,243],
[242,246,233,0,258,234,252,256,263],
[229,255,231,243,0,237,260,254,253],
[242,263,225,267,264,0,273,270,258],
[232,238,227,249,241,228,0,252,241],
[234,241,217,245,247,231,249,0,247],
[244,236,258,238,248,243,260,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,255,249,264,276,254,265,257],
[247,0,234,252,255,283,254,263,248],
[246,267,0,256,263,281,231,249,265],
[252,249,245,0,260,285,249,261,255],
[237,246,238,241,0,265,239,244,248],
[225,218,220,216,236,0,224,217,223],
[247,247,270,252,262,277,0,266,256],
[236,238,252,240,257,284,235,0,249],
[244,253,236,246,253,278,245,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,237,258,256,252,252,240,258],
[267,0,251,267,280,249,258,265,268],
[264,250,0,255,265,263,250,247,256],
[243,234,246,0,264,242,250,238,234],
[245,221,236,237,0,246,247,244,240],
[249,252,238,259,255,0,256,242,252],
[249,243,251,251,254,245,0,249,254],
[261,236,254,263,257,259,252,0,266],
[243,233,245,267,261,249,247,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,259,251,250,249,245,252,249],
[245,0,252,248,246,238,253,244,248],
[242,249,0,252,264,239,246,250,249],
[250,253,249,0,250,248,262,253,244],
[251,255,237,251,0,250,245,240,245],
[252,263,262,253,251,0,252,241,252],
[256,248,255,239,256,249,0,238,255],
[249,257,251,248,261,260,263,0,247],
[252,253,252,257,256,249,246,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,224,271,288,273,315,228,255],
[270,0,262,202,263,272,353,258,205],
[277,239,0,255,312,273,335,313,263],
[230,299,246,0,293,253,272,266,186],
[213,238,189,208,0,247,261,210,234],
[228,229,228,248,254,0,331,197,139],
[186,148,166,229,240,170,0,207,202],
[273,243,188,235,291,304,294,0,341],
[246,296,238,315,267,362,299,160,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,262,236,244,267,257,271,249],
[245,0,255,245,244,250,237,257,252],
[239,246,0,220,233,245,241,252,240],
[265,256,281,0,246,268,244,269,264],
[257,257,268,255,0,273,236,266,258],
[234,251,256,233,228,0,240,252,245],
[244,264,260,257,265,261,0,267,249],
[230,244,249,232,235,249,234,0,235],
[252,249,261,237,243,256,252,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,235,256,262,278,229,269,239],
[257,0,266,288,265,273,241,261,247],
[266,235,0,258,270,265,255,254,253],
[245,213,243,0,250,249,236,255,254],
[239,236,231,251,0,254,228,242,238],
[223,228,236,252,247,0,236,225,234],
[272,260,246,265,273,265,0,279,261],
[232,240,247,246,259,276,222,0,234],
[262,254,248,247,263,267,240,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,256,265,255,286,257,241,261],
[237,0,258,255,250,269,254,244,262],
[245,243,0,261,260,267,249,259,242],
[236,246,240,0,251,252,247,242,250],
[246,251,241,250,0,264,250,246,248],
[215,232,234,249,237,0,259,238,225],
[244,247,252,254,251,242,0,238,236],
[260,257,242,259,255,263,263,0,269],
[240,239,259,251,253,276,265,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,229,259,233,251,237,265,252],
[243,0,235,244,239,247,244,260,258],
[272,266,0,266,260,250,258,271,270],
[242,257,235,0,234,235,260,250,267],
[268,262,241,267,0,257,258,264,261],
[250,254,251,266,244,0,248,270,264],
[264,257,243,241,243,253,0,255,251],
[236,241,230,251,237,231,246,0,243],
[249,243,231,234,240,237,250,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,242,255,285,251,281,263,244],
[249,0,248,257,239,238,238,240,236],
[259,253,0,265,255,257,263,259,249],
[246,244,236,0,236,246,240,247,241],
[216,262,246,265,0,236,253,252,245],
[250,263,244,255,265,0,261,273,245],
[220,263,238,261,248,240,0,253,263],
[238,261,242,254,249,228,248,0,257],
[257,265,252,260,256,256,238,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,249,259,244,294,254,258,275],
[249,0,261,250,282,314,264,251,281],
[252,240,0,264,239,298,286,265,276],
[242,251,237,0,257,276,259,226,262],
[257,219,262,244,0,275,241,218,259],
[207,187,203,225,226,0,255,184,220],
[247,237,215,242,260,246,0,222,253],
[243,250,236,275,283,317,279,0,283],
[226,220,225,239,242,281,248,218,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,207,191,222,223,259,217,194,220],
[294,0,219,260,241,291,256,241,187],
[310,282,0,270,306,268,265,239,221],
[279,241,231,0,264,252,266,237,275],
[278,260,195,237,0,169,217,210,210],
[242,210,233,249,332,0,288,232,234],
[284,245,236,235,284,213,0,195,233],
[307,260,262,264,291,269,306,0,236],
[281,314,280,226,291,267,268,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,260,235,260,257,249,255,253],
[250,0,246,227,267,260,232,242,259],
[241,255,0,255,273,257,257,252,269],
[266,274,246,0,282,265,250,254,260],
[241,234,228,219,0,242,237,245,243],
[244,241,244,236,259,0,239,247,262],
[252,269,244,251,264,262,0,257,261],
[246,259,249,247,256,254,244,0,273],
[248,242,232,241,258,239,240,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,273,253,249,236,254,252,248],
[260,0,280,249,273,266,280,251,248],
[228,221,0,253,244,260,239,234,222],
[248,252,248,0,256,263,265,260,270],
[252,228,257,245,0,251,251,234,236],
[265,235,241,238,250,0,244,243,232],
[247,221,262,236,250,257,0,253,242],
[249,250,267,241,267,258,248,0,244],
[253,253,279,231,265,269,259,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,258,235,288,256,226,241,251],
[254,0,241,240,286,249,253,251,244],
[243,260,0,236,286,268,236,265,247],
[266,261,265,0,299,259,251,252,238],
[213,215,215,202,0,218,217,231,248],
[245,252,233,242,283,0,233,248,253],
[275,248,265,250,284,268,0,274,262],
[260,250,236,249,270,253,227,0,228],
[250,257,254,263,253,248,239,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,237,241,219,218,232,236,201],
[263,0,237,263,255,276,197,232,221],
[264,264,0,285,260,276,241,295,253],
[260,238,216,0,246,236,213,258,228],
[282,246,241,255,0,266,234,223,246],
[283,225,225,265,235,0,245,248,224],
[269,304,260,288,267,256,0,250,261],
[265,269,206,243,278,253,251,0,238],
[300,280,248,273,255,277,240,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,219,257,244,227,253,209,209],
[275,0,224,250,253,256,263,246,241],
[282,277,0,290,287,244,286,265,259],
[244,251,211,0,247,223,242,248,236],
[257,248,214,254,0,233,272,224,225],
[274,245,257,278,268,0,276,258,253],
[248,238,215,259,229,225,0,238,228],
[292,255,236,253,277,243,263,0,228],
[292,260,242,265,276,248,273,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,247,259,252,241,229,258,257],
[237,0,241,251,259,240,242,255,254],
[254,260,0,241,253,237,246,256,260],
[242,250,260,0,268,227,253,232,240],
[249,242,248,233,0,239,232,230,259],
[260,261,264,274,262,0,243,263,264],
[272,259,255,248,269,258,0,261,271],
[243,246,245,269,271,238,240,0,244],
[244,247,241,261,242,237,230,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,262,269,248,244,255,254,256],
[258,0,244,282,254,236,254,227,259],
[239,257,0,245,257,256,288,265,253],
[232,219,256,0,251,224,232,244,230],
[253,247,244,250,0,232,254,231,240],
[257,265,245,277,269,0,264,266,262],
[246,247,213,269,247,237,0,258,235],
[247,274,236,257,270,235,243,0,249],
[245,242,248,271,261,239,266,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,252,251,233,247,253,249,224],
[254,0,267,250,239,249,245,236,229],
[249,234,0,234,221,229,229,235,227],
[250,251,267,0,251,249,234,257,223],
[268,262,280,250,0,257,265,250,254],
[254,252,272,252,244,0,254,241,250],
[248,256,272,267,236,247,0,256,240],
[252,265,266,244,251,260,245,0,235],
[277,272,274,278,247,251,261,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,258,260,250,230,243,223,248],
[248,0,242,256,237,225,242,255,231],
[243,259,0,277,230,227,238,237,219],
[241,245,224,0,246,216,234,217,224],
[251,264,271,255,0,236,247,241,257],
[271,276,274,285,265,0,260,238,247],
[258,259,263,267,254,241,0,231,238],
[278,246,264,284,260,263,270,0,274],
[253,270,282,277,244,254,263,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,244,251,234,259,275,234,266],
[256,0,249,251,242,285,255,259,239],
[257,252,0,275,251,273,248,263,250],
[250,250,226,0,204,240,247,235,242],
[267,259,250,297,0,289,278,256,284],
[242,216,228,261,212,0,224,207,257],
[226,246,253,254,223,277,0,231,252],
[267,242,238,266,245,294,270,0,254],
[235,262,251,259,217,244,249,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,239,297,275,253,262,247,293],
[245,0,252,281,268,235,292,251,251],
[262,249,0,282,267,232,280,248,252],
[204,220,219,0,245,206,246,224,249],
[226,233,234,256,0,218,290,230,285],
[248,266,269,295,283,0,301,227,243],
[239,209,221,255,211,200,0,195,242],
[254,250,253,277,271,274,306,0,274],
[208,250,249,252,216,258,259,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,225,228,209,219,227,220,233],
[223,0,193,204,197,214,214,215,222],
[276,308,0,228,255,227,244,218,217],
[273,297,273,0,262,256,281,258,250],
[292,304,246,239,0,246,267,225,260],
[282,287,274,245,255,0,234,205,264],
[274,287,257,220,234,267,0,255,270],
[281,286,283,243,276,296,246,0,256],
[268,279,284,251,241,237,231,245,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,243,238,235,227,237,251,233],
[275,0,254,254,261,259,253,264,246],
[258,247,0,254,261,239,226,249,243],
[263,247,247,0,258,254,247,252,246],
[266,240,240,243,0,257,243,252,233],
[274,242,262,247,244,0,249,263,250],
[264,248,275,254,258,252,0,264,254],
[250,237,252,249,249,238,237,0,242],
[268,255,258,255,268,251,247,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,266,245,239,278,244,224,213],
[224,0,241,224,235,246,229,232,189],
[235,260,0,249,247,282,249,226,248],
[256,277,252,0,231,287,235,244,243],
[262,266,254,270,0,283,239,244,255],
[223,255,219,214,218,0,189,189,156],
[257,272,252,266,262,312,0,272,230],
[277,269,275,257,257,312,229,0,236],
[288,312,253,258,246,345,271,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,210,221,238,228,261,195,219,228],
[291,0,259,248,237,273,238,288,268],
[280,242,0,248,242,262,198,241,260],
[263,253,253,0,277,283,251,236,279],
[273,264,259,224,0,229,231,260,253],
[240,228,239,218,272,0,220,246,224],
[306,263,303,250,270,281,0,281,304],
[282,213,260,265,241,255,220,0,250],
[273,233,241,222,248,277,197,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,203,187,268,219,208,209,209],
[265,0,243,253,262,248,242,213,250],
[298,258,0,247,281,288,284,254,287],
[314,248,254,0,302,273,260,218,227],
[233,239,220,199,0,260,265,207,236],
[282,253,213,228,241,0,251,213,243],
[293,259,217,241,236,250,0,219,242],
[292,288,247,283,294,288,282,0,260],
[292,251,214,274,265,258,259,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,266,260,265,252,264,277,249,270],
[235,0,236,224,241,237,249,219,220],
[241,265,0,273,254,255,257,225,245],
[236,277,228,0,249,275,273,259,238],
[249,260,247,252,0,274,262,223,259],
[237,264,246,226,227,0,262,235,241],
[224,252,244,228,239,239,0,226,240],
[252,282,276,242,278,266,275,0,253],
[231,281,256,263,242,260,261,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,260,243,252,264,278,255,254],
[233,0,241,256,248,265,258,268,267],
[241,260,0,267,240,298,281,273,270],
[258,245,234,0,232,280,268,258,278],
[249,253,261,269,0,286,311,287,281],
[237,236,203,221,215,0,225,250,227],
[223,243,220,233,190,276,0,244,245],
[246,233,228,243,214,251,257,0,246],
[247,234,231,223,220,274,256,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,255,241,209,229,271,248,308],
[259,0,259,249,251,243,270,239,262],
[246,242,0,215,212,211,241,206,281],
[260,252,286,0,232,228,258,227,263],
[292,250,289,269,0,304,304,240,276],
[272,258,290,273,197,0,280,255,281],
[230,231,260,243,197,221,0,236,247],
[253,262,295,274,261,246,265,0,269],
[193,239,220,238,225,220,254,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,186,160,182,206,220,213,200,199],
[315,0,233,244,244,248,305,288,288],
[341,268,0,280,237,270,287,276,279],
[319,257,221,0,275,243,279,298,261],
[295,257,264,226,0,270,268,300,271],
[281,253,231,258,231,0,297,285,251],
[288,196,214,222,233,204,0,224,212],
[301,213,225,203,201,216,277,0,252],
[302,213,222,240,230,250,289,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,298,281,302,305,242,261,320],
[228,0,262,260,246,289,220,259,275],
[203,239,0,219,242,266,221,279,274],
[220,241,282,0,231,261,305,319,307],
[199,255,259,270,0,320,243,336,328],
[196,212,235,240,181,0,190,267,279],
[259,281,280,196,258,311,0,340,394],
[240,242,222,182,165,234,161,0,286],
[181,226,227,194,173,222,107,215,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,248,249,213,240,235,230,239],
[268,0,271,287,274,253,242,240,258],
[253,230,0,247,233,222,239,238,248],
[252,214,254,0,255,239,235,233,249],
[288,227,268,246,0,234,239,256,255],
[261,248,279,262,267,0,252,240,272],
[266,259,262,266,262,249,0,240,256],
[271,261,263,268,245,261,261,0,265],
[262,243,253,252,246,229,245,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,270,242,258,260,243,243,244],
[248,0,260,247,271,267,237,249,244],
[231,241,0,247,255,236,242,234,246],
[259,254,254,0,267,264,251,263,242],
[243,230,246,234,0,224,231,236,222],
[241,234,265,237,277,0,259,227,249],
[258,264,259,250,270,242,0,240,255],
[258,252,267,238,265,274,261,0,253],
[257,257,255,259,279,252,246,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,275,249,300,261,274,285,270],
[227,0,246,196,278,220,313,289,257],
[226,255,0,241,259,192,247,238,275],
[252,305,260,0,258,214,274,270,287],
[201,223,242,243,0,226,264,249,243],
[240,281,309,287,275,0,282,266,245],
[227,188,254,227,237,219,0,217,220],
[216,212,263,231,252,235,284,0,260],
[231,244,226,214,258,256,281,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,261,253,235,219,254,227,251],
[239,0,250,252,241,240,244,258,279],
[240,251,0,267,255,222,249,252,260],
[248,249,234,0,246,226,252,222,243],
[266,260,246,255,0,240,266,242,255],
[282,261,279,275,261,0,272,246,271],
[247,257,252,249,235,229,0,236,242],
[274,243,249,279,259,255,265,0,273],
[250,222,241,258,246,230,259,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,233,260,235,265,266,238,242],
[255,0,252,249,222,278,260,229,237],
[268,249,0,272,227,292,273,259,231],
[241,252,229,0,247,244,277,249,234],
[266,279,274,254,0,264,290,259,243],
[236,223,209,257,237,0,256,247,254],
[235,241,228,224,211,245,0,224,228],
[263,272,242,252,242,254,277,0,235],
[259,264,270,267,258,247,273,266,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,249,244,243,240,235,265,246],
[259,0,258,266,253,258,236,255,251],
[252,243,0,258,242,244,249,256,251],
[257,235,243,0,250,260,235,256,231],
[258,248,259,251,0,246,257,268,265],
[261,243,257,241,255,0,250,255,229],
[266,265,252,266,244,251,0,258,234],
[236,246,245,245,233,246,243,0,228],
[255,250,250,270,236,272,267,273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,255,264,253,254,245,252,259],
[233,0,234,256,259,248,252,242,240],
[246,267,0,255,248,258,261,246,255],
[237,245,246,0,245,258,257,252,242],
[248,242,253,256,0,240,250,261,252],
[247,253,243,243,261,0,245,244,241],
[256,249,240,244,251,256,0,257,244],
[249,259,255,249,240,257,244,0,247],
[242,261,246,259,249,260,257,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,243,242,237,226,257,246,249],
[264,0,252,247,249,271,259,244,247],
[258,249,0,271,261,265,273,256,237],
[259,254,230,0,263,262,255,241,252],
[264,252,240,238,0,271,250,248,237],
[275,230,236,239,230,0,245,243,235],
[244,242,228,246,251,256,0,242,238],
[255,257,245,260,253,258,259,0,243],
[252,254,264,249,264,266,263,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,241,228,240,243,235,252,239],
[262,0,231,246,248,238,256,245,250],
[260,270,0,248,254,239,240,241,259],
[273,255,253,0,265,250,271,267,246],
[261,253,247,236,0,252,255,265,260],
[258,263,262,251,249,0,247,259,250],
[266,245,261,230,246,254,0,256,243],
[249,256,260,234,236,242,245,0,236],
[262,251,242,255,241,251,258,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,185,243,245,258,356,244,212,282],
[316,0,304,298,198,256,316,313,323],
[258,197,0,185,237,254,194,247,290],
[256,203,316,0,217,237,214,227,304],
[243,303,264,284,0,279,265,236,311],
[145,245,247,264,222,0,203,246,288],
[257,185,307,287,236,298,0,234,317],
[289,188,254,274,265,255,267,0,330],
[219,178,211,197,190,213,184,171,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,249,247,251,239,228,225,252],
[247,0,255,226,242,234,261,227,262],
[252,246,0,240,246,256,260,228,283],
[254,275,261,0,236,262,253,246,284],
[250,259,255,265,0,251,265,262,259],
[262,267,245,239,250,0,227,237,245],
[273,240,241,248,236,274,0,244,264],
[276,274,273,255,239,264,257,0,271],
[249,239,218,217,242,256,237,230,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,232,219,227,198,260,259,231],
[281,0,250,267,262,238,269,276,257],
[269,251,0,267,266,245,291,256,269],
[282,234,234,0,268,234,254,275,239],
[274,239,235,233,0,259,262,276,260],
[303,263,256,267,242,0,297,268,274],
[241,232,210,247,239,204,0,229,257],
[242,225,245,226,225,233,272,0,257],
[270,244,232,262,241,227,244,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,248,257,234,245,241,252,246],
[255,0,261,263,240,248,250,264,269],
[253,240,0,264,244,260,252,258,261],
[244,238,237,0,237,238,219,251,246],
[267,261,257,264,0,251,247,260,248],
[256,253,241,263,250,0,242,252,260],
[260,251,249,282,254,259,0,262,256],
[249,237,243,250,241,249,239,0,261],
[255,232,240,255,253,241,245,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,255,263,256,263,257,241,253],
[248,0,246,269,257,263,242,246,254],
[246,255,0,269,258,251,246,253,245],
[238,232,232,0,242,230,249,236,248],
[245,244,243,259,0,259,250,237,249],
[238,238,250,271,242,0,248,242,247],
[244,259,255,252,251,253,0,249,249],
[260,255,248,265,264,259,252,0,254],
[248,247,256,253,252,254,252,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,215,238,218,253,226,251,224,223],
[286,0,255,236,278,258,265,284,241],
[263,246,0,231,290,278,287,247,258],
[283,265,270,0,319,261,270,241,245],
[248,223,211,182,0,227,257,236,221],
[275,243,223,240,274,0,219,239,236],
[250,236,214,231,244,282,0,245,247],
[277,217,254,260,265,262,256,0,250],
[278,260,243,256,280,265,254,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,249,232,239,207,235,257,230],
[258,0,262,254,259,249,268,271,267],
[252,239,0,239,249,240,242,270,249],
[269,247,262,0,251,257,256,282,266],
[262,242,252,250,0,232,266,269,250],
[294,252,261,244,269,0,276,267,272],
[266,233,259,245,235,225,0,253,246],
[244,230,231,219,232,234,248,0,252],
[271,234,252,235,251,229,255,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,261,284,243,276,265,265,262],
[229,0,250,269,258,248,246,233,236],
[240,251,0,267,257,252,268,251,260],
[217,232,234,0,235,258,247,228,225],
[258,243,244,266,0,256,275,238,251],
[225,253,249,243,245,0,268,252,239],
[236,255,233,254,226,233,0,249,230],
[236,268,250,273,263,249,252,0,238],
[239,265,241,276,250,262,271,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,264,255,253,250,303,244,257],
[229,0,262,222,224,238,272,231,232],
[237,239,0,245,211,223,275,206,226],
[246,279,256,0,266,260,280,259,252],
[248,277,290,235,0,250,291,265,259],
[251,263,278,241,251,0,266,251,244],
[198,229,226,221,210,235,0,234,230],
[257,270,295,242,236,250,267,0,287],
[244,269,275,249,242,257,271,214,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,318,199,215,225,252,252,239],
[255,0,325,241,271,254,267,282,263],
[183,176,0,269,208,220,227,229,256],
[302,260,232,0,261,239,214,298,267],
[286,230,293,240,0,264,255,225,276],
[276,247,281,262,237,0,271,203,282],
[249,234,274,287,246,230,0,286,270],
[249,219,272,203,276,298,215,0,274],
[262,238,245,234,225,219,231,227,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,242,257,242,232,271,255,237],
[246,0,220,242,224,208,246,237,223],
[259,281,0,243,277,239,283,263,262],
[244,259,258,0,234,245,273,244,256],
[259,277,224,267,0,249,283,248,244],
[269,293,262,256,252,0,285,249,258],
[230,255,218,228,218,216,0,233,213],
[246,264,238,257,253,252,268,0,248],
[264,278,239,245,257,243,288,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,239,240,256,253,243,259,246],
[259,0,254,252,259,277,256,265,246],
[262,247,0,250,253,264,260,279,256],
[261,249,251,0,265,266,260,276,252],
[245,242,248,236,0,264,258,268,240],
[248,224,237,235,237,0,251,253,221],
[258,245,241,241,243,250,0,250,251],
[242,236,222,225,233,248,251,0,237],
[255,255,245,249,261,280,250,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,268,249,259,274,242,267,264],
[256,0,261,246,228,270,261,238,245],
[233,240,0,222,238,242,267,256,237],
[252,255,279,0,250,259,255,275,250],
[242,273,263,251,0,257,235,257,237],
[227,231,259,242,244,0,243,257,242],
[259,240,234,246,266,258,0,257,258],
[234,263,245,226,244,244,244,0,257],
[237,256,264,251,264,259,243,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,220,228,247,259,210,263,241],
[265,0,250,235,236,272,257,268,238],
[281,251,0,262,243,256,243,247,260],
[273,266,239,0,239,275,228,272,251],
[254,265,258,262,0,268,243,279,290],
[242,229,245,226,233,0,214,248,263],
[291,244,258,273,258,287,0,298,285],
[238,233,254,229,222,253,203,0,265],
[260,263,241,250,211,238,216,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,226,229,227,244,244,268,288],
[264,0,254,264,264,206,306,230,269],
[275,247,0,274,228,255,276,258,286],
[272,237,227,0,199,239,270,270,286],
[274,237,273,302,0,256,284,260,283],
[257,295,246,262,245,0,264,269,292],
[257,195,225,231,217,237,0,221,234],
[233,271,243,231,241,232,280,0,282],
[213,232,215,215,218,209,267,219,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,252,239,255,246,210,239,207],
[284,0,242,258,281,261,262,269,251],
[249,259,0,248,267,235,241,254,228],
[262,243,253,0,245,247,223,239,224],
[246,220,234,256,0,226,231,236,208],
[255,240,266,254,275,0,233,240,228],
[291,239,260,278,270,268,0,242,217],
[262,232,247,262,265,261,259,0,242],
[294,250,273,277,293,273,284,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,279,267,361,250,338,329,284],
[234,0,273,245,342,241,393,328,247],
[222,228,0,254,335,316,326,306,321],
[234,256,247,0,300,236,315,313,317],
[140,159,166,201,0,166,271,279,233],
[251,260,185,265,335,0,337,321,309],
[163,108,175,186,230,164,0,227,208],
[172,173,195,188,222,180,274,0,266],
[217,254,180,184,268,192,293,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,243,259,283,294,288,297,253],
[238,0,208,250,266,301,280,272,249],
[258,293,0,244,297,264,286,282,285],
[242,251,257,0,293,292,261,296,270],
[218,235,204,208,0,267,248,261,235],
[207,200,237,209,234,0,256,244,244],
[213,221,215,240,253,245,0,277,235],
[204,229,219,205,240,257,224,0,233],
[248,252,216,231,266,257,266,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,246,246,233,211,288,244,219],
[245,0,221,252,269,259,252,292,206],
[255,280,0,247,276,231,263,245,249],
[255,249,254,0,255,221,267,267,224],
[268,232,225,246,0,211,240,212,264],
[290,242,270,280,290,0,318,290,237],
[213,249,238,234,261,183,0,242,234],
[257,209,256,234,289,211,259,0,261],
[282,295,252,277,237,264,267,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,240,255,232,226,248,232,257],
[254,0,243,256,235,231,261,238,265],
[261,258,0,259,232,242,266,251,268],
[246,245,242,0,223,202,243,233,252],
[269,266,269,278,0,255,279,249,267],
[275,270,259,299,246,0,277,270,283],
[253,240,235,258,222,224,0,253,247],
[269,263,250,268,252,231,248,0,263],
[244,236,233,249,234,218,254,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,271,252,275,275,258,281,273],
[253,0,276,224,263,242,252,247,246],
[230,225,0,214,262,245,233,244,234],
[249,277,287,0,281,250,255,288,250],
[226,238,239,220,0,229,241,234,240],
[226,259,256,251,272,0,248,251,255],
[243,249,268,246,260,253,0,258,257],
[220,254,257,213,267,250,243,0,260],
[228,255,267,251,261,246,244,241,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,250,243,245,240,244,251,255],
[250,0,253,243,245,249,245,241,256],
[251,248,0,240,244,242,237,244,248],
[258,258,261,0,259,244,259,245,266],
[256,256,257,242,0,262,246,232,254],
[261,252,259,257,239,0,255,241,251],
[257,256,264,242,255,246,0,248,264],
[250,260,257,256,269,260,253,0,267],
[246,245,253,235,247,250,237,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,240,226,236,217,238,257,238],
[274,0,270,258,269,252,248,286,277],
[261,231,0,237,262,224,237,256,259],
[275,243,264,0,255,234,259,282,268],
[265,232,239,246,0,229,237,259,256],
[284,249,277,267,272,0,267,284,270],
[263,253,264,242,264,234,0,275,257],
[244,215,245,219,242,217,226,0,240],
[263,224,242,233,245,231,244,261,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,313,261,300,285,348,280,238,304],
[188,0,139,136,255,218,131,92,200],
[240,362,0,342,294,328,261,267,205],
[201,365,159,0,365,289,284,265,241],
[216,246,207,136,0,328,179,154,229],
[153,283,173,212,173,0,196,172,178],
[221,370,240,217,322,305,0,201,212],
[263,409,234,236,347,329,300,0,289],
[197,301,296,260,272,323,289,212,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,299,258,276,258,266,253,288],
[265,0,259,247,249,237,256,235,257],
[202,242,0,244,235,226,242,202,262],
[243,254,257,0,245,230,254,234,283],
[225,252,266,256,0,251,245,227,270],
[243,264,275,271,250,0,252,274,264],
[235,245,259,247,256,249,0,236,274],
[248,266,299,267,274,227,265,0,275],
[213,244,239,218,231,237,227,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,234,252,224,237,220,228,240],
[250,0,253,281,255,249,232,245,245],
[267,248,0,279,280,233,245,226,263],
[249,220,222,0,232,235,234,229,249],
[277,246,221,269,0,250,252,235,248],
[264,252,268,266,251,0,248,239,269],
[281,269,256,267,249,253,0,251,265],
[273,256,275,272,266,262,250,0,254],
[261,256,238,252,253,232,236,247,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,272,275,235,242,252,264,239],
[239,0,262,286,252,257,254,273,263],
[229,239,0,231,224,244,224,244,233],
[226,215,270,0,223,240,250,233,217],
[266,249,277,278,0,292,257,263,258],
[259,244,257,261,209,0,230,264,246],
[249,247,277,251,244,271,0,278,251],
[237,228,257,268,238,237,223,0,244],
[262,238,268,284,243,255,250,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,244,238,252,246,275,261,251],
[248,0,230,246,252,241,250,256,242],
[257,271,0,234,246,254,261,241,253],
[263,255,267,0,247,252,275,271,262],
[249,249,255,254,0,249,263,259,255],
[255,260,247,249,252,0,279,256,267],
[226,251,240,226,238,222,0,242,230],
[240,245,260,230,242,245,259,0,234],
[250,259,248,239,246,234,271,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,237,254,263,243,297,259,262],
[258,0,257,275,247,256,259,276,272],
[264,244,0,277,236,239,265,271,255],
[247,226,224,0,240,225,248,264,245],
[238,254,265,261,0,254,270,254,268],
[258,245,262,276,247,0,277,256,257],
[204,242,236,253,231,224,0,250,232],
[242,225,230,237,247,245,251,0,251],
[239,229,246,256,233,244,269,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,136,248,204,260,218,244,226,158],
[365,0,237,281,309,318,237,257,300],
[253,264,0,301,309,249,281,281,312],
[297,220,200,0,251,328,260,291,288],
[241,192,192,250,0,259,237,244,157],
[283,183,252,173,242,0,311,167,280],
[257,264,220,241,264,190,0,261,230],
[275,244,220,210,257,334,240,0,233],
[343,201,189,213,344,221,271,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,309,313,256,266,256,269,226,275],
[192,0,257,220,197,199,201,226,257],
[188,244,0,235,203,191,215,225,206],
[245,281,266,0,257,205,256,248,205],
[235,304,298,244,0,268,238,278,273],
[245,302,310,296,233,0,258,226,287],
[232,300,286,245,263,243,0,225,237],
[275,275,276,253,223,275,276,0,310],
[226,244,295,296,228,214,264,191,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,246,226,232,239,238,229,249],
[250,0,258,255,240,252,242,255,258],
[255,243,0,236,246,245,230,231,261],
[275,246,265,0,252,257,250,253,250],
[269,261,255,249,0,263,251,260,260],
[262,249,256,244,238,0,249,234,246],
[263,259,271,251,250,252,0,249,259],
[272,246,270,248,241,267,252,0,267],
[252,243,240,251,241,255,242,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,441,400,293,219,245,239,292],
[282,0,393,400,346,288,299,219,276],
[60,108,0,230,182,156,129,181,113],
[101,101,271,0,245,197,101,165,79],
[208,155,319,256,0,278,187,183,191],
[282,213,345,304,223,0,262,182,281],
[256,202,372,400,314,239,0,273,251],
[262,282,320,336,318,319,228,0,208],
[209,225,388,422,310,220,250,293,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,269,225,262,246,243,259,228],
[230,0,242,215,264,234,231,270,256],
[232,259,0,251,255,253,252,277,247],
[276,286,250,0,270,267,267,276,251],
[239,237,246,231,0,246,238,273,204],
[255,267,248,234,255,0,256,302,229],
[258,270,249,234,263,245,0,307,251],
[242,231,224,225,228,199,194,0,212],
[273,245,254,250,297,272,250,289,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,255,244,269,262,280,265,262],
[252,0,248,254,266,259,269,263,250],
[246,253,0,250,253,255,262,258,249],
[257,247,251,0,254,249,240,261,240],
[232,235,248,247,0,246,241,232,250],
[239,242,246,252,255,0,262,244,244],
[221,232,239,261,260,239,0,248,234],
[236,238,243,240,269,257,253,0,246],
[239,251,252,261,251,257,267,255,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,249,244,249,259,255,250,253],
[262,0,268,268,254,251,262,255,248],
[252,233,0,261,261,250,239,260,240],
[257,233,240,0,244,255,245,245,236],
[252,247,240,257,0,248,260,251,242],
[242,250,251,246,253,0,247,260,250],
[246,239,262,256,241,254,0,259,252],
[251,246,241,256,250,241,242,0,232],
[248,253,261,265,259,251,249,269,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,266,251,254,246,248,253,231],
[252,0,256,237,256,253,257,253,244],
[235,245,0,218,244,240,254,246,244],
[250,264,283,0,265,259,270,269,253],
[247,245,257,236,0,241,270,245,242],
[255,248,261,242,260,0,271,240,251],
[253,244,247,231,231,230,0,245,233],
[248,248,255,232,256,261,256,0,251],
[270,257,257,248,259,250,268,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,257,259,282,249,262,276,260],
[257,0,261,277,280,243,256,260,258],
[244,240,0,247,275,271,241,263,258],
[242,224,254,0,279,265,254,262,249],
[219,221,226,222,0,229,236,248,226],
[252,258,230,236,272,0,265,263,259],
[239,245,260,247,265,236,0,250,242],
[225,241,238,239,253,238,251,0,239],
[241,243,243,252,275,242,259,262,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,251,245,240,259,258,257,269],
[263,0,242,249,234,260,255,271,274],
[250,259,0,271,252,262,262,272,281],
[256,252,230,0,247,252,254,256,264],
[261,267,249,254,0,264,259,262,280],
[242,241,239,249,237,0,266,251,273],
[243,246,239,247,242,235,0,246,240],
[244,230,229,245,239,250,255,0,275],
[232,227,220,237,221,228,261,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,249,258,274,239,265,233,244],
[242,0,244,268,228,241,259,250,209],
[252,257,0,240,241,245,248,238,227],
[243,233,261,0,212,226,236,250,225],
[227,273,260,289,0,240,251,283,239],
[262,260,256,275,261,0,215,273,225],
[236,242,253,265,250,286,0,262,258],
[268,251,263,251,218,228,239,0,221],
[257,292,274,276,262,276,243,280,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,247,257,219,242,220,251,245],
[246,0,254,233,214,201,221,232,234],
[254,247,0,270,242,244,256,271,300],
[244,268,231,0,247,215,234,253,250],
[282,287,259,254,0,230,260,278,263],
[259,300,257,286,271,0,244,253,266],
[281,280,245,267,241,257,0,274,254],
[250,269,230,248,223,248,227,0,247],
[256,267,201,251,238,235,247,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,253,257,256,258,246,231,241],
[261,0,240,250,249,265,242,232,265],
[248,261,0,254,261,258,260,240,254],
[244,251,247,0,251,248,255,253,246],
[245,252,240,250,0,234,254,249,244],
[243,236,243,253,267,0,256,251,262],
[255,259,241,246,247,245,0,261,258],
[270,269,261,248,252,250,240,0,275],
[260,236,247,255,257,239,243,226,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,226,251,225,258,265,217,242,240],
[275,0,264,258,275,281,248,274,257],
[250,237,0,252,272,281,225,242,229],
[276,243,249,0,276,297,239,248,254],
[243,226,229,225,0,249,223,198,199],
[236,220,220,204,252,0,217,243,198],
[284,253,276,262,278,284,0,253,250],
[259,227,259,253,303,258,248,0,255],
[261,244,272,247,302,303,251,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,263,228,278,276,282,276,252],
[227,0,218,260,285,304,266,249,220],
[238,283,0,259,332,247,289,241,254],
[273,241,242,0,275,273,269,234,251],
[223,216,169,226,0,240,214,198,233],
[225,197,254,228,261,0,284,215,206],
[219,235,212,232,287,217,0,199,217],
[225,252,260,267,303,286,302,0,245],
[249,281,247,250,268,295,284,256,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,267,246,251,254,250,246,263],
[236,0,252,230,248,242,232,238,264],
[234,249,0,234,243,238,239,247,251],
[255,271,267,0,254,258,254,233,257],
[250,253,258,247,0,242,253,234,259],
[247,259,263,243,259,0,248,253,272],
[251,269,262,247,248,253,0,249,248],
[255,263,254,268,267,248,252,0,273],
[238,237,250,244,242,229,253,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,253,259,264,274,242,229,246],
[260,0,250,277,260,237,245,246,236],
[248,251,0,267,263,230,250,268,216],
[242,224,234,0,240,214,238,242,228],
[237,241,238,261,0,241,233,235,222],
[227,264,271,287,260,0,230,245,255],
[259,256,251,263,268,271,0,252,240],
[272,255,233,259,266,256,249,0,249],
[255,265,285,273,279,246,261,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,225,283,276,292,300,264,260],
[252,0,254,262,261,279,282,265,203],
[276,247,0,274,250,301,285,280,244],
[218,239,227,0,234,251,260,225,218],
[225,240,251,267,0,278,280,259,221],
[209,222,200,250,223,0,267,246,207],
[201,219,216,241,221,234,0,231,238],
[237,236,221,276,242,255,270,0,216],
[241,298,257,283,280,294,263,285,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,257,213,241,229,240,205,206],
[264,0,270,247,231,253,208,258,257],
[244,231,0,250,238,247,222,223,236],
[288,254,251,0,255,242,273,247,243],
[260,270,263,246,0,267,265,241,221],
[272,248,254,259,234,0,250,227,226],
[261,293,279,228,236,251,0,255,257],
[296,243,278,254,260,274,246,0,267],
[295,244,265,258,280,275,244,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,263,267,259,258,241,248,258],
[254,0,243,259,235,253,241,244,246],
[238,258,0,260,241,254,243,235,249],
[234,242,241,0,237,235,239,237,238],
[242,266,260,264,0,256,249,255,264],
[243,248,247,266,245,0,242,250,263],
[260,260,258,262,252,259,0,247,263],
[253,257,266,264,246,251,254,0,267],
[243,255,252,263,237,238,238,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,211,212,194,225,217,264,186,215],
[290,0,245,279,270,261,266,250,253],
[289,256,0,250,260,311,268,289,231],
[307,222,251,0,266,293,244,257,210],
[276,231,241,235,0,255,236,227,239],
[284,240,190,208,246,0,246,162,213],
[237,235,233,257,265,255,0,215,231],
[315,251,212,244,274,339,286,0,253],
[286,248,270,291,262,288,270,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,248,260,231,264,269,253,245],
[240,0,239,235,218,258,248,237,237],
[253,262,0,244,242,254,259,232,261],
[241,266,257,0,257,275,249,244,244],
[270,283,259,244,0,263,263,247,253],
[237,243,247,226,238,0,244,244,254],
[232,253,242,252,238,257,0,242,239],
[248,264,269,257,254,257,259,0,243],
[256,264,240,257,248,247,262,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,289,250,229,245,266,275,240,275],
[212,0,271,232,265,226,287,239,270],
[251,230,0,273,246,252,305,214,278],
[272,269,228,0,258,248,276,258,289],
[256,236,255,243,0,277,312,252,272],
[235,275,249,253,224,0,267,185,252],
[226,214,196,225,189,234,0,217,244],
[261,262,287,243,249,316,284,0,273],
[226,231,223,212,229,249,257,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,248,250,251,244,236,245,249],
[255,0,265,249,257,264,248,264,250],
[253,236,0,236,224,243,233,258,233],
[251,252,265,0,247,265,254,262,259],
[250,244,277,254,0,260,245,257,248],
[257,237,258,236,241,0,221,265,263],
[265,253,268,247,256,280,0,258,248],
[256,237,243,239,244,236,243,0,241],
[252,251,268,242,253,238,253,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,273,252,227,295,261,271,255],
[251,0,314,259,233,273,250,264,288],
[228,187,0,214,199,248,231,210,229],
[249,242,287,0,247,325,290,285,266],
[274,268,302,254,0,311,243,285,278],
[206,228,253,176,190,0,234,205,233],
[240,251,270,211,258,267,0,273,245],
[230,237,291,216,216,296,228,0,249],
[246,213,272,235,223,268,256,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,241,253,247,247,237,257,247],
[285,0,247,246,243,252,240,236,276],
[260,254,0,257,255,277,240,254,267],
[248,255,244,0,259,260,235,232,273],
[254,258,246,242,0,269,252,249,252],
[254,249,224,241,232,0,248,251,249],
[264,261,261,266,249,253,0,247,267],
[244,265,247,269,252,250,254,0,267],
[254,225,234,228,249,252,234,234,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,240,251,253,261,259,257,252],
[262,0,248,258,268,260,268,261,264],
[261,253,0,271,255,260,262,262,249],
[250,243,230,0,251,256,243,252,256],
[248,233,246,250,0,259,243,254,233],
[240,241,241,245,242,0,244,248,239],
[242,233,239,258,258,257,0,247,244],
[244,240,239,249,247,253,254,0,238],
[249,237,252,245,268,262,257,263,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,220,225,196,262,202,230,258,265],
[281,0,256,247,294,239,283,282,292],
[276,245,0,224,280,241,268,248,289],
[305,254,277,0,273,273,229,277,282],
[239,207,221,228,0,206,247,228,260],
[299,262,260,228,295,0,256,297,325],
[271,218,233,272,254,245,0,259,263],
[243,219,253,224,273,204,242,0,257],
[236,209,212,219,241,176,238,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,309,331,309,277,306,272,328,238],
[192,0,329,259,261,271,236,249,213],
[170,172,0,171,174,231,193,241,165],
[192,242,330,0,254,323,245,317,250],
[224,240,327,247,0,311,318,317,282],
[195,230,270,178,190,0,272,272,222],
[229,265,308,256,183,229,0,279,241],
[173,252,260,184,184,229,222,0,202],
[263,288,336,251,219,279,260,299,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,255,221,221,268,221,256,231],
[280,0,257,205,215,239,199,253,274],
[246,244,0,204,212,260,202,252,263],
[280,296,297,0,246,301,260,261,327],
[280,286,289,255,0,295,204,274,262],
[233,262,241,200,206,0,182,246,227],
[280,302,299,241,297,319,0,279,300],
[245,248,249,240,227,255,222,0,265],
[270,227,238,174,239,274,201,236,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,232,249,252,244,250,234,238],
[255,0,245,236,236,255,257,229,247],
[269,256,0,256,283,270,268,262,247],
[252,265,245,0,258,256,252,258,248],
[249,265,218,243,0,236,254,255,240],
[257,246,231,245,265,0,259,227,249],
[251,244,233,249,247,242,0,258,237],
[267,272,239,243,246,274,243,0,262],
[263,254,254,253,261,252,264,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,241,237,230,249,222,226,247],
[265,0,254,266,245,269,251,243,247],
[260,247,0,248,242,265,230,250,263],
[264,235,253,0,245,261,232,256,258],
[271,256,259,256,0,268,246,256,261],
[252,232,236,240,233,0,230,239,243],
[279,250,271,269,255,271,0,260,266],
[275,258,251,245,245,262,241,0,252],
[254,254,238,243,240,258,235,249,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,249,254,256,252,274,244,256],
[253,0,239,261,250,243,247,258,262],
[252,262,0,264,266,242,257,233,273],
[247,240,237,0,236,237,238,248,241],
[245,251,235,265,0,239,232,256,272],
[249,258,259,264,262,0,230,237,258],
[227,254,244,263,269,271,0,270,268],
[257,243,268,253,245,264,231,0,277],
[245,239,228,260,229,243,233,224,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,266,274,274,277,297,244,274],
[247,0,278,286,270,288,274,266,287],
[235,223,0,246,207,237,257,226,246],
[227,215,255,0,217,226,232,220,232],
[227,231,294,284,0,257,270,231,281],
[224,213,264,275,244,0,250,242,248],
[204,227,244,269,231,251,0,219,256],
[257,235,275,281,270,259,282,0,283],
[227,214,255,269,220,253,245,218,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,235,247,239,268,230,249,231],
[262,0,254,271,250,264,221,253,241],
[266,247,0,256,236,266,235,242,247],
[254,230,245,0,260,274,226,237,257],
[262,251,265,241,0,277,221,275,231],
[233,237,235,227,224,0,226,241,232],
[271,280,266,275,280,275,0,275,245],
[252,248,259,264,226,260,226,0,237],
[270,260,254,244,270,269,256,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,257,257,237,284,292,283,260],
[229,0,255,282,258,281,267,272,282],
[244,246,0,283,261,250,267,232,230],
[244,219,218,0,237,238,243,201,230],
[264,243,240,264,0,249,284,239,272],
[217,220,251,263,252,0,257,246,269],
[209,234,234,258,217,244,0,225,248],
[218,229,269,300,262,255,276,0,291],
[241,219,271,271,229,232,253,210,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,262,270,247,249,259,247,259],
[242,0,268,252,241,247,255,251,240],
[239,233,0,229,223,239,245,259,219],
[231,249,272,0,239,239,249,248,232],
[254,260,278,262,0,247,264,255,237],
[252,254,262,262,254,0,244,242,247],
[242,246,256,252,237,257,0,259,242],
[254,250,242,253,246,259,242,0,244],
[242,261,282,269,264,254,259,257,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,193,295,253,241,254,333,268,272],
[308,0,336,275,225,280,294,250,214],
[206,165,0,209,210,198,294,249,187],
[248,226,292,0,187,245,321,291,216],
[260,276,291,314,0,284,321,224,295],
[247,221,303,256,217,0,266,270,268],
[168,207,207,180,180,235,0,261,245],
[233,251,252,210,277,231,240,0,210],
[229,287,314,285,206,233,256,291,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,244,226,272,234,266,237,265],
[242,0,213,210,234,271,255,242,282],
[257,288,0,246,288,230,263,254,299],
[275,291,255,0,273,304,311,246,322],
[229,267,213,228,0,234,261,254,268],
[267,230,271,197,267,0,276,239,305],
[235,246,238,190,240,225,0,235,278],
[264,259,247,255,247,262,266,0,285],
[236,219,202,179,233,196,223,216,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,244,240,238,262,235,280,252],
[260,0,247,239,238,252,224,272,241],
[257,254,0,255,237,263,238,254,256],
[261,262,246,0,252,266,241,261,246],
[263,263,264,249,0,266,262,265,269],
[239,249,238,235,235,0,246,257,231],
[266,277,263,260,239,255,0,274,240],
[221,229,247,240,236,244,227,0,247],
[249,260,245,255,232,270,261,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,242,259,251,267,247,257,233],
[256,0,225,253,248,241,249,245,238],
[259,276,0,266,252,274,237,248,241],
[242,248,235,0,244,245,247,238,251],
[250,253,249,257,0,254,236,235,245],
[234,260,227,256,247,0,239,243,239],
[254,252,264,254,265,262,0,241,246],
[244,256,253,263,266,258,260,0,266],
[268,263,260,250,256,262,255,235,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,241,236,250,247,259,256,253],
[256,0,247,254,250,248,258,281,266],
[260,254,0,249,251,259,280,273,264],
[265,247,252,0,256,271,259,275,256],
[251,251,250,245,0,261,259,268,263],
[254,253,242,230,240,0,250,259,250],
[242,243,221,242,242,251,0,269,251],
[245,220,228,226,233,242,232,0,234],
[248,235,237,245,238,251,250,267,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,256,245,245,228,246,258,242],
[254,0,255,243,242,238,262,276,272],
[245,246,0,262,224,233,249,248,238],
[256,258,239,0,251,255,242,235,250],
[256,259,277,250,0,259,270,249,257],
[273,263,268,246,242,0,255,254,274],
[255,239,252,259,231,246,0,238,243],
[243,225,253,266,252,247,263,0,270],
[259,229,263,251,244,227,258,231,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,255,281,256,255,266,277,237],
[247,0,244,276,255,248,258,262,242],
[246,257,0,271,233,248,266,276,258],
[220,225,230,0,247,234,239,260,244],
[245,246,268,254,0,249,260,265,254],
[246,253,253,267,252,0,283,271,260],
[235,243,235,262,241,218,0,264,236],
[224,239,225,241,236,230,237,0,242],
[264,259,243,257,247,241,265,259,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,218,241,232,296,232,383,255,218],
[283,0,91,307,225,357,447,305,178],
[260,410,0,339,221,424,358,337,311],
[269,194,162,0,217,349,338,226,166],
[205,276,280,284,0,300,374,290,274],
[269,144,77,152,201,0,385,172,126],
[118,54,143,163,127,116,0,191,66],
[246,196,164,275,211,329,310,0,263],
[283,323,190,335,227,375,435,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,275,260,238,265,265,246,269,235],
[226,0,205,242,234,251,233,254,234],
[241,296,0,244,255,265,255,255,243],
[263,259,257,0,220,257,259,267,259],
[236,267,246,281,0,277,260,272,236],
[236,250,236,244,224,0,238,258,237],
[255,268,246,242,241,263,0,258,227],
[232,247,246,234,229,243,243,0,229],
[266,267,258,242,265,264,274,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,233,217,241,221,244,252,233],
[285,0,237,198,224,249,220,223,216],
[268,264,0,247,222,244,247,251,252],
[284,303,254,0,257,215,293,309,278],
[260,277,279,244,0,228,264,241,223],
[280,252,257,286,273,0,249,225,225],
[257,281,254,208,237,252,0,264,248],
[249,278,250,192,260,276,237,0,227],
[268,285,249,223,278,276,253,274,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,270,290,262,263,286,264,255],
[253,0,274,285,245,238,264,263,250],
[231,227,0,250,243,232,231,266,248],
[211,216,251,0,237,204,238,240,218],
[239,256,258,264,0,254,265,273,266],
[238,263,269,297,247,0,259,271,276],
[215,237,270,263,236,242,0,261,256],
[237,238,235,261,228,230,240,0,222],
[246,251,253,283,235,225,245,279,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,254,254,253,241,249,260,252],
[258,0,242,253,242,249,247,253,262],
[247,259,0,248,278,252,259,279,239],
[247,248,253,0,257,255,240,266,244],
[248,259,223,244,0,240,231,255,240],
[260,252,249,246,261,0,245,262,272],
[252,254,242,261,270,256,0,271,258],
[241,248,222,235,246,239,230,0,231],
[249,239,262,257,261,229,243,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,254,257,271,270,267,271,245],
[250,0,267,250,270,271,262,264,253],
[247,234,0,248,261,273,250,259,238],
[244,251,253,0,262,266,245,239,235],
[230,231,240,239,0,262,250,245,232],
[231,230,228,235,239,0,241,232,225],
[234,239,251,256,251,260,0,239,243],
[230,237,242,262,256,269,262,0,236],
[256,248,263,266,269,276,258,265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,226,226,233,239,217,221,255],
[285,0,261,275,258,256,216,250,264],
[275,240,0,258,269,269,264,247,267],
[275,226,243,0,233,252,216,243,262],
[268,243,232,268,0,259,252,243,269],
[262,245,232,249,242,0,229,260,270],
[284,285,237,285,249,272,0,264,266],
[280,251,254,258,258,241,237,0,263],
[246,237,234,239,232,231,235,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,253,241,248,248,261,231,268],
[257,0,262,239,249,253,258,249,265],
[248,239,0,235,268,232,256,227,255],
[260,262,266,0,257,244,261,259,263],
[253,252,233,244,0,248,231,242,249],
[253,248,269,257,253,0,248,240,266],
[240,243,245,240,270,253,0,230,262],
[270,252,274,242,259,261,271,0,263],
[233,236,246,238,252,235,239,238,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,242,252,238,239,241,260,241],
[244,0,232,228,241,241,220,241,217],
[259,269,0,241,256,265,241,249,232],
[249,273,260,0,254,260,236,224,254],
[263,260,245,247,0,258,244,214,250],
[262,260,236,241,243,0,229,244,245],
[260,281,260,265,257,272,0,230,245],
[241,260,252,277,287,257,271,0,257],
[260,284,269,247,251,256,256,244,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,240,241,249,235,246,272,258],
[232,0,255,234,261,229,255,253,231],
[261,246,0,237,276,251,249,257,243],
[260,267,264,0,257,247,263,271,243],
[252,240,225,244,0,249,257,237,222],
[266,272,250,254,252,0,255,268,233],
[255,246,252,238,244,246,0,252,236],
[229,248,244,230,264,233,249,0,249],
[243,270,258,258,279,268,265,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,249,206,219,307,262,266,242],
[282,0,277,267,225,293,299,337,250],
[252,224,0,226,213,233,273,249,257],
[295,234,275,0,250,271,252,243,287],
[282,276,288,251,0,306,222,257,237],
[194,208,268,230,195,0,226,265,201],
[239,202,228,249,279,275,0,276,246],
[235,164,252,258,244,236,225,0,203],
[259,251,244,214,264,300,255,298,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,337,221,307,268,272,258,283],
[236,0,295,231,286,288,242,231,241],
[164,206,0,231,189,239,191,177,226],
[280,270,270,0,265,294,190,225,223],
[194,215,312,236,0,260,231,287,208],
[233,213,262,207,241,0,196,270,223],
[229,259,310,311,270,305,0,313,307],
[243,270,324,276,214,231,188,0,229],
[218,260,275,278,293,278,194,272,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,175,219,200,254,247,242,262,227],
[326,0,279,234,314,329,271,306,257],
[282,222,0,202,254,264,257,291,229],
[301,267,299,0,301,345,311,289,231],
[247,187,247,200,0,283,264,259,233],
[254,172,237,156,218,0,259,217,195],
[259,230,244,190,237,242,0,213,226],
[239,195,210,212,242,284,288,0,208],
[274,244,272,270,268,306,275,293,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,236,243,241,241,252,248,242],
[256,0,232,232,247,246,263,271,244],
[265,269,0,240,255,266,266,258,260],
[258,269,261,0,266,245,267,269,254],
[260,254,246,235,0,246,254,261,268],
[260,255,235,256,255,0,267,266,255],
[249,238,235,234,247,234,0,250,252],
[253,230,243,232,240,235,251,0,233],
[259,257,241,247,233,246,249,268,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,254,267,272,257,266,250,256],
[245,0,239,239,236,237,240,218,242],
[247,262,0,245,254,243,255,254,255],
[234,262,256,0,246,251,253,231,229],
[229,265,247,255,0,247,253,243,251],
[244,264,258,250,254,0,264,256,258],
[235,261,246,248,248,237,0,236,253],
[251,283,247,270,258,245,265,0,261],
[245,259,246,272,250,243,248,240,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,260,273,241,243,256,259,258],
[260,0,255,258,263,255,276,248,259],
[241,246,0,273,251,244,263,262,249],
[228,243,228,0,228,246,267,262,250],
[260,238,250,273,0,243,258,262,270],
[258,246,257,255,258,0,279,269,249],
[245,225,238,234,243,222,0,245,250],
[242,253,239,239,239,232,256,0,247],
[243,242,252,251,231,252,251,254,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,224,264,251,237,249,264,257,266],
[277,0,244,259,225,264,247,270,272],
[237,257,0,240,231,242,255,228,232],
[250,242,261,0,216,241,269,257,253],
[264,276,270,285,0,269,280,266,236],
[252,237,259,260,232,0,240,262,251],
[237,254,246,232,221,261,0,250,216],
[244,231,273,244,235,239,251,0,248],
[235,229,269,248,265,250,285,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,235,253,256,248,276,235,259],
[248,0,245,249,248,247,239,232,237],
[266,256,0,253,257,257,248,258,269],
[248,252,248,0,260,256,275,256,269],
[245,253,244,241,0,262,255,259,244],
[253,254,244,245,239,0,255,256,250],
[225,262,253,226,246,246,0,249,268],
[266,269,243,245,242,245,252,0,255],
[242,264,232,232,257,251,233,246,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,246,229,228,243,242,279,236],
[256,0,260,252,257,242,259,259,233],
[255,241,0,243,224,228,255,263,215],
[272,249,258,0,254,254,252,267,238],
[273,244,277,247,0,265,260,258,260],
[258,259,273,247,236,0,233,275,216],
[259,242,246,249,241,268,0,273,243],
[222,242,238,234,243,226,228,0,237],
[265,268,286,263,241,285,258,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,230,265,252,245,249,280,259],
[233,0,245,266,283,267,240,259,258],
[271,256,0,274,278,235,260,268,269],
[236,235,227,0,261,234,251,252,235],
[249,218,223,240,0,246,240,249,250],
[256,234,266,267,255,0,274,259,249],
[252,261,241,250,261,227,0,244,243],
[221,242,233,249,252,242,257,0,258],
[242,243,232,266,251,252,258,243,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,244,226,233,261,225,256,257],
[229,0,222,220,196,223,211,218,215],
[257,279,0,239,253,257,246,266,249],
[275,281,262,0,245,244,255,237,258],
[268,305,248,256,0,236,262,251,252],
[240,278,244,257,265,0,248,268,268],
[276,290,255,246,239,253,0,276,251],
[245,283,235,264,250,233,225,0,231],
[244,286,252,243,249,233,250,270,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,245,228,249,240,251,284,258],
[245,0,254,237,243,243,252,245,249],
[256,247,0,237,265,236,248,248,256],
[273,264,264,0,250,263,274,269,281],
[252,258,236,251,0,251,259,273,261],
[261,258,265,238,250,0,252,258,255],
[250,249,253,227,242,249,0,260,254],
[217,256,253,232,228,243,241,0,262],
[243,252,245,220,240,246,247,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,230,247,231,238,248,239,233],
[256,0,249,254,248,245,281,245,257],
[271,252,0,261,236,251,255,250,244],
[254,247,240,0,231,263,259,232,244],
[270,253,265,270,0,253,265,252,243],
[263,256,250,238,248,0,262,249,257],
[253,220,246,242,236,239,0,225,231],
[262,256,251,269,249,252,276,0,259],
[268,244,257,257,258,244,270,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,245,233,230,240,249,252,243],
[246,0,267,287,290,268,271,304,273],
[256,234,0,287,264,264,213,268,231],
[268,214,214,0,262,232,246,260,220],
[271,211,237,239,0,224,245,288,191],
[261,233,237,269,277,0,236,286,217],
[252,230,288,255,256,265,0,287,223],
[249,197,233,241,213,215,214,0,205],
[258,228,270,281,310,284,278,296,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,251,232,242,249,252,258,254],
[254,0,241,236,237,231,227,244,242],
[250,260,0,238,234,228,260,234,240],
[269,265,263,0,242,268,263,264,269],
[259,264,267,259,0,247,264,267,257],
[252,270,273,233,254,0,278,250,259],
[249,274,241,238,237,223,0,240,229],
[243,257,267,237,234,251,261,0,249],
[247,259,261,232,244,242,272,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,242,249,241,249,256,247,254],
[258,0,248,262,264,240,269,264,275],
[259,253,0,268,266,254,252,247,271],
[252,239,233,0,272,251,262,245,258],
[260,237,235,229,0,225,243,225,267],
[252,261,247,250,276,0,259,261,252],
[245,232,249,239,258,242,0,228,249],
[254,237,254,256,276,240,273,0,273],
[247,226,230,243,234,249,252,228,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,278,264,303,241,284,255,245],
[241,0,271,291,265,238,258,249,237],
[223,230,0,271,250,221,249,227,234],
[237,210,230,0,239,246,238,246,226],
[198,236,251,262,0,229,240,226,253],
[260,263,280,255,272,0,268,256,246],
[217,243,252,263,261,233,0,237,236],
[246,252,274,255,275,245,264,0,253],
[256,264,267,275,248,255,265,248,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,254,251,281,260,252,258,266],
[254,0,282,268,291,242,263,273,266],
[247,219,0,246,251,243,226,238,258],
[250,233,255,0,273,239,257,251,256],
[220,210,250,228,0,219,238,254,248],
[241,259,258,262,282,0,257,263,277],
[249,238,275,244,263,244,0,254,256],
[243,228,263,250,247,238,247,0,248],
[235,235,243,245,253,224,245,253,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,257,247,246,219,243,251,263],
[274,0,281,273,244,239,255,264,244],
[244,220,0,243,232,231,233,233,249],
[254,228,258,0,237,235,248,240,251],
[255,257,269,264,0,251,241,259,266],
[282,262,270,266,250,0,261,236,245],
[258,246,268,253,260,240,0,251,250],
[250,237,268,261,242,265,250,0,259],
[238,257,252,250,235,256,251,242,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,261,264,260,244,233,261,260],
[242,0,259,265,264,262,252,272,256],
[240,242,0,241,251,240,241,253,243],
[237,236,260,0,250,256,240,255,254],
[241,237,250,251,0,257,233,245,243],
[257,239,261,245,244,0,236,267,252],
[268,249,260,261,268,265,0,269,256],
[240,229,248,246,256,234,232,0,250],
[241,245,258,247,258,249,245,251,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,283,233,271,203,217,259,257,249],
[218,0,248,259,224,226,237,222,241],
[268,253,0,297,237,226,265,250,235],
[230,242,204,0,246,225,245,244,230],
[298,277,264,255,0,259,270,271,245],
[284,275,275,276,242,0,295,288,300],
[242,264,236,256,231,206,0,235,212],
[244,279,251,257,230,213,266,0,251],
[252,260,266,271,256,201,289,250,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,268,267,257,252,269,262,256],
[251,0,262,247,240,259,234,271,249],
[233,239,0,254,252,253,239,243,251],
[234,254,247,0,244,250,249,253,251],
[244,261,249,257,0,240,255,248,251],
[249,242,248,251,261,0,247,255,266],
[232,267,262,252,246,254,0,257,241],
[239,230,258,248,253,246,244,0,262],
[245,252,250,250,250,235,260,239,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,257,249,260,252,251,261,260],
[240,0,248,252,253,263,241,250,257],
[244,253,0,240,251,251,237,244,255],
[252,249,261,0,275,256,252,262,272],
[241,248,250,226,0,249,234,245,248],
[249,238,250,245,252,0,231,261,242],
[250,260,264,249,267,270,0,276,278],
[240,251,257,239,256,240,225,0,241],
[241,244,246,229,253,259,223,260,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,239,252,275,229,197,233,222],
[270,0,266,258,286,249,243,235,247],
[262,235,0,205,269,228,253,231,219],
[249,243,296,0,259,257,226,246,228],
[226,215,232,242,0,215,244,214,228],
[272,252,273,244,286,0,234,249,271],
[304,258,248,275,257,267,0,260,251],
[268,266,270,255,287,252,241,0,269],
[279,254,282,273,273,230,250,232,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,245,249,250,246,236,245,242],
[255,0,244,245,248,249,238,237,234],
[256,257,0,243,257,256,238,241,258],
[252,256,258,0,259,246,238,234,265],
[251,253,244,242,0,235,231,237,240],
[255,252,245,255,266,0,250,252,254],
[265,263,263,263,270,251,0,248,258],
[256,264,260,267,264,249,253,0,243],
[259,267,243,236,261,247,243,258,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,282,272,260,251,263,252,249],
[241,0,262,288,248,247,262,265,250],
[219,239,0,241,223,237,217,235,224],
[229,213,260,0,238,233,244,242,247],
[241,253,278,263,0,249,259,239,232],
[250,254,264,268,252,0,237,239,242],
[238,239,284,257,242,264,0,245,253],
[249,236,266,259,262,262,256,0,237],
[252,251,277,254,269,259,248,264,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,258,279,268,252,262,264,211],
[217,0,232,237,236,226,224,250,199],
[243,269,0,282,252,233,252,266,249],
[222,264,219,0,225,245,233,234,208],
[233,265,249,276,0,234,229,251,205],
[249,275,268,256,267,0,276,259,254],
[239,277,249,268,272,225,0,228,216],
[237,251,235,267,250,242,273,0,230],
[290,302,252,293,296,247,285,271,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,255,255,259,246,248,265,252],
[244,0,253,249,255,252,250,237,230],
[246,248,0,255,249,259,258,251,236],
[246,252,246,0,257,255,254,252,239],
[242,246,252,244,0,226,247,245,226],
[255,249,242,246,275,0,251,246,219],
[253,251,243,247,254,250,0,265,239],
[236,264,250,249,256,255,236,0,249],
[249,271,265,262,275,282,262,252,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 501, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_9_501.csv", index=False, header=False)