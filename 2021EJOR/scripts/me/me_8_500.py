
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,242,239,221,242,234,243,244],
[258,0,247,258,254,240,235,247],
[261,253,0,253,244,257,257,247],
[279,242,247,0,245,252,245,251],
[258,246,256,255,0,249,248,249],
[266,260,243,248,251,0,249,240],
[257,265,243,255,252,251,0,253],
[256,253,253,249,251,260,247,0]])



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
result = np.append(np.array([8, 500, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,250,278,254,263,286,293],
[238,0,227,231,236,237,227,254],
[250,273,0,239,247,246,251,260],
[222,269,261,0,222,240,256,259],
[246,264,253,278,0,251,293,263],
[237,263,254,260,249,0,256,274],
[214,273,249,244,207,244,0,232],
[207,246,240,241,237,226,268,0]])



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
result = np.append(np.array([8, 500, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,218,204,228,217,250,249],
[264,0,265,257,261,240,309,218],
[282,235,0,248,279,259,259,253],
[296,243,252,0,285,261,282,245],
[272,239,221,215,0,229,303,239],
[283,260,241,239,271,0,273,252],
[250,191,241,218,197,227,0,215],
[251,282,247,255,261,248,285,0]])



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
result = np.append(np.array([8, 500, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,268,252,227,271,269,256],
[239,0,249,240,192,283,260,241],
[232,251,0,250,262,280,278,238],
[248,260,250,0,216,231,216,268],
[273,308,238,284,0,289,249,302],
[229,217,220,269,211,0,274,246],
[231,240,222,284,251,226,0,254],
[244,259,262,232,198,254,246,0]])



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
result = np.append(np.array([8, 500, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,230,247,240,238,269,261,244],
[270,0,265,251,247,253,266,260],
[253,235,0,231,254,251,247,257],
[260,249,269,0,264,257,280,271],
[262,253,246,236,0,240,254,242],
[231,247,249,243,260,0,247,256],
[239,234,253,220,246,253,0,256],
[256,240,243,229,258,244,244,0]])



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
result = np.append(np.array([8, 500, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,201,217,285,273,238,216,261],
[299,0,285,276,270,254,213,290],
[283,215,0,250,210,209,215,239],
[215,224,250,0,222,233,186,233],
[227,230,290,278,0,250,286,282],
[262,246,291,267,250,0,229,293],
[284,287,285,314,214,271,0,304],
[239,210,261,267,218,207,196,0]])



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
result = np.append(np.array([8, 500, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,216,236,260,292,241,309,234],
[284,0,257,266,228,260,261,281],
[264,243,0,251,300,242,280,286],
[240,234,249,0,260,306,292,301],
[208,272,200,240,0,241,261,267],
[259,240,258,194,259,0,276,275],
[191,239,220,208,239,224,0,260],
[266,219,214,199,233,225,240,0]])



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
result = np.append(np.array([8, 500, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,245,233,240,250,236,252],
[247,0,258,251,216,277,248,251],
[255,242,0,244,241,255,231,252],
[267,249,256,0,244,257,244,234],
[260,284,259,256,0,278,230,270],
[250,223,245,243,222,0,256,235],
[264,252,269,256,270,244,0,248],
[248,249,248,266,230,265,252,0]])



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
result = np.append(np.array([8, 500, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,245,263,252,243,243,242],
[265,0,252,247,231,241,301,281],
[255,248,0,255,271,263,278,293],
[237,253,245,0,249,238,274,264],
[248,269,229,251,0,269,280,235],
[257,259,237,262,231,0,256,266],
[257,199,222,226,220,244,0,276],
[258,219,207,236,265,234,224,0]])



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
result = np.append(np.array([8, 500, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,217,243,234,242,251,254],
[252,0,241,238,252,254,251,255],
[283,259,0,253,264,252,248,265],
[257,262,247,0,266,264,260,254],
[266,248,236,234,0,250,254,263],
[258,246,248,236,250,0,254,262],
[249,249,252,240,246,246,0,254],
[246,245,235,246,237,238,246,0]])



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
result = np.append(np.array([8, 500, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,252,270,250,253,267,255],
[254,0,245,263,239,245,263,250],
[248,255,0,276,254,260,262,235],
[230,237,224,0,244,236,244,220],
[250,261,246,256,0,239,250,239],
[247,255,240,264,261,0,267,241],
[233,237,238,256,250,233,0,225],
[245,250,265,280,261,259,275,0]])



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
result = np.append(np.array([8, 500, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,262,248,255,258,254,251],
[238,0,256,249,234,244,240,232],
[238,244,0,244,224,247,244,246],
[252,251,256,0,256,247,242,251],
[245,266,276,244,0,258,250,253],
[242,256,253,253,242,0,254,239],
[246,260,256,258,250,246,0,256],
[249,268,254,249,247,261,244,0]])



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
result = np.append(np.array([8, 500, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,241,235,235,228,251,249],
[272,0,263,276,257,267,250,264],
[259,237,0,264,239,256,225,235],
[265,224,236,0,223,236,217,255],
[265,243,261,277,0,256,241,247],
[272,233,244,264,244,0,250,267],
[249,250,275,283,259,250,0,238],
[251,236,265,245,253,233,262,0]])



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
result = np.append(np.array([8, 500, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,265,249,268,263,274,279],
[249,0,252,252,243,247,295,278],
[235,248,0,276,247,257,292,271],
[251,248,224,0,243,255,261,259],
[232,257,253,257,0,250,239,261],
[237,253,243,245,250,0,274,261],
[226,205,208,239,261,226,0,250],
[221,222,229,241,239,239,250,0]])



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
result = np.append(np.array([8, 500, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,266,258,252,245,262,268],
[250,0,260,260,247,254,248,251],
[234,240,0,259,236,234,245,240],
[242,240,241,0,251,238,235,251],
[248,253,264,249,0,244,261,265],
[255,246,266,262,256,0,252,261],
[238,252,255,265,239,248,0,255],
[232,249,260,249,235,239,245,0]])



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
result = np.append(np.array([8, 500, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,238,235,240,238,235,228],
[266,0,269,249,225,243,254,237],
[262,231,0,233,223,241,239,245],
[265,251,267,0,259,260,253,243],
[260,275,277,241,0,241,249,249],
[262,257,259,240,259,0,230,242],
[265,246,261,247,251,270,0,255],
[272,263,255,257,251,258,245,0]])



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
result = np.append(np.array([8, 500, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,306,173,279,307,306,257,280],
[194,0,204,247,310,291,249,217],
[327,296,0,351,392,309,281,228],
[221,253,149,0,364,254,195,299],
[193,190,108,136,0,189,156,206],
[194,209,191,246,311,0,301,321],
[243,251,219,305,344,199,0,266],
[220,283,272,201,294,179,234,0]])



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
result = np.append(np.array([8, 500, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,260,248,251,266,255,251],
[241,0,223,249,237,237,248,253],
[240,277,0,261,255,248,250,263],
[252,251,239,0,260,247,247,262],
[249,263,245,240,0,255,248,260],
[234,263,252,253,245,0,248,259],
[245,252,250,253,252,252,0,258],
[249,247,237,238,240,241,242,0]])



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
result = np.append(np.array([8, 500, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,251,274,262,251,277,242],
[250,0,262,253,236,261,275,243],
[249,238,0,258,237,249,268,255],
[226,247,242,0,253,253,270,259],
[238,264,263,247,0,262,264,257],
[249,239,251,247,238,0,277,257],
[223,225,232,230,236,223,0,263],
[258,257,245,241,243,243,237,0]])



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
result = np.append(np.array([8, 500, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,280,339,246,286,290,287,286],
[220,0,295,302,266,297,232,254],
[161,205,0,245,197,237,285,235],
[254,198,255,0,240,268,208,252],
[214,234,303,260,0,305,252,260],
[210,203,263,232,195,0,199,204],
[213,268,215,292,248,301,0,206],
[214,246,265,248,240,296,294,0]])



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
result = np.append(np.array([8, 500, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,269,267,252,247,252,241],
[233,0,240,229,221,226,243,244],
[231,260,0,239,236,238,242,244],
[233,271,261,0,247,237,250,246],
[248,279,264,253,0,252,250,256],
[253,274,262,263,248,0,254,247],
[248,257,258,250,250,246,0,246],
[259,256,256,254,244,253,254,0]])



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
result = np.append(np.array([8, 500, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,199,250,315,218,251,219,244],
[301,0,236,306,266,265,250,286],
[250,264,0,274,264,271,242,301],
[185,194,226,0,207,218,219,241],
[282,234,236,293,0,284,266,285],
[249,235,229,282,216,0,266,253],
[281,250,258,281,234,234,0,239],
[256,214,199,259,215,247,261,0]])



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
result = np.append(np.array([8, 500, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,273,235,258,270,254,266],
[248,0,223,252,233,258,266,248],
[227,277,0,214,249,260,244,279],
[265,248,286,0,227,282,232,282],
[242,267,251,273,0,265,253,238],
[230,242,240,218,235,0,236,232],
[246,234,256,268,247,264,0,238],
[234,252,221,218,262,268,262,0]])



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
result = np.append(np.array([8, 500, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,242,250,262,257,261,261],
[249,0,239,270,246,232,242,255],
[258,261,0,257,249,270,267,269],
[250,230,243,0,251,250,241,257],
[238,254,251,249,0,250,249,248],
[243,268,230,250,250,0,258,252],
[239,258,233,259,251,242,0,250],
[239,245,231,243,252,248,250,0]])



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
result = np.append(np.array([8, 500, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,215,216,193,244,231,232,272],
[285,0,261,282,280,246,250,245],
[284,239,0,259,272,282,267,262],
[307,218,241,0,263,273,235,283],
[256,220,228,237,0,219,217,250],
[269,254,218,227,281,0,204,257],
[268,250,233,265,283,296,0,239],
[228,255,238,217,250,243,261,0]])



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
result = np.append(np.array([8, 500, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,272,287,294,247,264,240,246],
[228,0,228,247,227,216,203,229],
[213,272,0,225,188,216,210,203],
[206,253,275,0,222,213,205,219],
[253,273,312,278,0,272,245,280],
[236,284,284,287,228,0,292,259],
[260,297,290,295,255,208,0,258],
[254,271,297,281,220,241,242,0]])



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
result = np.append(np.array([8, 500, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,299,277,233,278,162,222,264],
[201,0,209,221,181,228,266,199],
[223,291,0,213,270,238,258,248],
[267,279,287,0,259,246,184,237],
[222,319,230,241,0,250,200,255],
[338,272,262,254,250,0,335,247],
[278,234,242,316,300,165,0,243],
[236,301,252,263,245,253,257,0]])



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
result = np.append(np.array([8, 500, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,244,263,250,248,254,253,235],
[256,0,256,240,256,260,266,248],
[237,244,0,236,236,236,244,230],
[250,260,264,0,260,268,262,256],
[252,244,264,240,0,248,250,233],
[246,240,264,232,252,0,254,239],
[247,234,256,238,250,246,0,241],
[265,252,270,244,267,261,259,0]])



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
result = np.append(np.array([8, 500, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,258,236,260,257,236,277],
[243,0,228,243,236,247,237,238],
[242,272,0,239,253,257,261,268],
[264,257,261,0,264,265,250,261],
[240,264,247,236,0,252,231,254],
[243,253,243,235,248,0,251,255],
[264,263,239,250,269,249,0,266],
[223,262,232,239,246,245,234,0]])



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
result = np.append(np.array([8, 500, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,244,254,258,240,254,249],
[251,0,255,245,256,256,239,255],
[256,245,0,245,269,266,241,260],
[246,255,255,0,262,255,264,272],
[242,244,231,238,0,236,248,255],
[260,244,234,245,264,0,257,244],
[246,261,259,236,252,243,0,257],
[251,245,240,228,245,256,243,0]])



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
result = np.append(np.array([8, 500, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,250,247,247,243,276,232],
[244,0,249,233,241,241,262,224],
[250,251,0,246,254,261,282,239],
[253,267,254,0,286,249,280,240],
[253,259,246,214,0,248,256,251],
[257,259,239,251,252,0,270,237],
[224,238,218,220,244,230,0,223],
[268,276,261,260,249,263,277,0]])



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
result = np.append(np.array([8, 500, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,273,277,265,254,226,267,258],
[227,0,275,262,282,230,248,240],
[223,225,0,232,261,206,270,235],
[235,238,268,0,217,214,219,231],
[246,218,239,283,0,232,249,208],
[274,270,294,286,268,0,284,248],
[233,252,230,281,251,216,0,211],
[242,260,265,269,292,252,289,0]])



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
result = np.append(np.array([8, 500, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,283,231,270,237,266,261,232],
[217,0,211,244,250,230,233,236],
[269,289,0,281,240,266,253,257],
[230,256,219,0,224,220,244,217],
[263,250,260,276,0,254,254,245],
[234,270,234,280,246,0,241,260],
[239,267,247,256,246,259,0,226],
[268,264,243,283,255,240,274,0]])



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
result = np.append(np.array([8, 500, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,235,245,232,226,243,253],
[264,0,242,247,228,243,257,264],
[265,258,0,269,248,244,253,255],
[255,253,231,0,223,237,242,250],
[268,272,252,277,0,250,252,264],
[274,257,256,263,250,0,253,273],
[257,243,247,258,248,247,0,261],
[247,236,245,250,236,227,239,0]])



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
result = np.append(np.array([8, 500, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,263,260,252,253,245,239],
[254,0,252,254,246,257,239,238],
[237,248,0,260,249,254,264,266],
[240,246,240,0,236,247,254,243],
[248,254,251,264,0,267,240,250],
[247,243,246,253,233,0,244,239],
[255,261,236,246,260,256,0,236],
[261,262,234,257,250,261,264,0]])



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
result = np.append(np.array([8, 500, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,254,223,210,259,259,240],
[241,0,221,201,245,262,218,235],
[246,279,0,266,266,273,280,297],
[277,299,234,0,253,264,255,251],
[290,255,234,247,0,245,272,260],
[241,238,227,236,255,0,242,233],
[241,282,220,245,228,258,0,253],
[260,265,203,249,240,267,247,0]])



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
result = np.append(np.array([8, 500, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,246,255,244,211,240,236],
[247,0,257,254,265,241,219,261],
[254,243,0,260,224,220,222,224],
[245,246,240,0,248,225,212,236],
[256,235,276,252,0,259,247,276],
[289,259,280,275,241,0,246,259],
[260,281,278,288,253,254,0,247],
[264,239,276,264,224,241,253,0]])



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
result = np.append(np.array([8, 500, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,236,289,269,236,290,252],
[223,0,247,265,179,290,214,226],
[264,253,0,277,243,241,268,226],
[211,235,223,0,282,225,260,223],
[231,321,257,218,0,217,298,242],
[264,210,259,275,283,0,277,272],
[210,286,232,240,202,223,0,267],
[248,274,274,277,258,228,233,0]])



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
result = np.append(np.array([8, 500, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,262,267,260,254,256,250],
[244,0,248,262,246,227,248,245],
[238,252,0,258,247,248,245,238],
[233,238,242,0,239,215,239,237],
[240,254,253,261,0,240,248,230],
[246,273,252,285,260,0,245,251],
[244,252,255,261,252,255,0,251],
[250,255,262,263,270,249,249,0]])



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
result = np.append(np.array([8, 500, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,257,270,213,247,246,226],
[257,0,244,279,248,244,270,252],
[243,256,0,273,269,241,251,248],
[230,221,227,0,218,221,225,210],
[287,252,231,282,0,222,255,234],
[253,256,259,279,278,0,262,246],
[254,230,249,275,245,238,0,238],
[274,248,252,290,266,254,262,0]])



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
result = np.append(np.array([8, 500, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,231,265,254,254,233,245],
[259,0,244,247,256,239,253,247],
[269,256,0,267,253,240,250,237],
[235,253,233,0,264,263,255,246],
[246,244,247,236,0,245,216,241],
[246,261,260,237,255,0,256,244],
[267,247,250,245,284,244,0,261],
[255,253,263,254,259,256,239,0]])



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
result = np.append(np.array([8, 500, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,272,252,253,252,274,254],
[251,0,265,249,250,243,245,243],
[228,235,0,225,248,228,235,231],
[248,251,275,0,243,254,244,244],
[247,250,252,257,0,257,252,245],
[248,257,272,246,243,0,257,254],
[226,255,265,256,248,243,0,241],
[246,257,269,256,255,246,259,0]])



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
result = np.append(np.array([8, 500, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,235,230,228,249,250,249],
[260,0,240,267,243,252,264,248],
[265,260,0,269,256,250,263,255],
[270,233,231,0,239,245,247,249],
[272,257,244,261,0,259,274,270],
[251,248,250,255,241,0,256,242],
[250,236,237,253,226,244,0,230],
[251,252,245,251,230,258,270,0]])



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
result = np.append(np.array([8, 500, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,265,237,258,271,251,267],
[244,0,253,232,250,237,242,245],
[235,247,0,228,241,250,240,242],
[263,268,272,0,240,252,262,278],
[242,250,259,260,0,257,251,234],
[229,263,250,248,243,0,254,262],
[249,258,260,238,249,246,0,258],
[233,255,258,222,266,238,242,0]])



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
result = np.append(np.array([8, 500, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,223,256,221,203,246,261,221],
[277,0,270,228,217,234,204,242],
[244,230,0,227,203,224,202,208],
[279,272,273,0,231,248,240,216],
[297,283,297,269,0,268,232,251],
[254,266,276,252,232,0,225,256],
[239,296,298,260,268,275,0,258],
[279,258,292,284,249,244,242,0]])



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
result = np.append(np.array([8, 500, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,241,259,244,240,241,248],
[235,0,231,250,230,229,232,255],
[259,269,0,256,257,256,249,248],
[241,250,244,0,261,229,240,256],
[256,270,243,239,0,244,236,272],
[260,271,244,271,256,0,256,265],
[259,268,251,260,264,244,0,259],
[252,245,252,244,228,235,241,0]])



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
result = np.append(np.array([8, 500, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,297,233,273,233,286,275,255],
[203,0,216,245,210,230,241,217],
[267,284,0,299,223,277,250,273],
[227,255,201,0,200,230,237,218],
[267,290,277,300,0,280,280,235],
[214,270,223,270,220,0,252,246],
[225,259,250,263,220,248,0,233],
[245,283,227,282,265,254,267,0]])



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
result = np.append(np.array([8, 500, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,285,221,208,229,220,224,259],
[215,0,225,278,239,234,243,208],
[279,275,0,261,223,260,266,280],
[292,222,239,0,257,214,248,218],
[271,261,277,243,0,285,251,262],
[280,266,240,286,215,0,270,244],
[276,257,234,252,249,230,0,262],
[241,292,220,282,238,256,238,0]])



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
result = np.append(np.array([8, 500, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,247,252,248,281,272,254],
[240,0,243,251,247,260,264,233],
[253,257,0,266,247,284,267,246],
[248,249,234,0,253,268,263,258],
[252,253,253,247,0,265,262,239],
[219,240,216,232,235,0,252,223],
[228,236,233,237,238,248,0,230],
[246,267,254,242,261,277,270,0]])



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
result = np.append(np.array([8, 500, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,238,246,251,251,240,266],
[231,0,250,229,235,237,248,252],
[262,250,0,261,252,246,236,256],
[254,271,239,0,269,282,255,262],
[249,265,248,231,0,256,253,256],
[249,263,254,218,244,0,239,271],
[260,252,264,245,247,261,0,280],
[234,248,244,238,244,229,220,0]])



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
result = np.append(np.array([8, 500, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,248,240,266,250,232,247],
[260,0,260,237,251,252,269,250],
[252,240,0,240,255,235,247,246],
[260,263,260,0,259,267,258,244],
[234,249,245,241,0,249,235,244],
[250,248,265,233,251,0,237,250],
[268,231,253,242,265,263,0,256],
[253,250,254,256,256,250,244,0]])



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
result = np.append(np.array([8, 500, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,315,347,279,289,259,310,242],
[185,0,277,162,203,221,251,185],
[153,223,0,172,181,228,229,209],
[221,338,328,0,282,256,303,240],
[211,297,319,218,0,303,335,274],
[241,279,272,244,197,0,267,184],
[190,249,271,197,165,233,0,217],
[258,315,291,260,226,316,283,0]])



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
result = np.append(np.array([8, 500, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,261,244,242,264,250,254,249],
[239,0,222,245,238,241,246,239],
[256,278,0,250,264,254,263,245],
[258,255,250,0,264,246,263,233],
[236,262,236,236,0,237,249,224],
[250,259,246,254,263,0,274,254],
[246,254,237,237,251,226,0,224],
[251,261,255,267,276,246,276,0]])



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
result = np.append(np.array([8, 500, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,248,198,208,171,225,196],
[272,0,264,234,241,247,258,279],
[252,236,0,219,293,280,236,311],
[302,266,281,0,289,247,262,323],
[292,259,207,211,0,222,178,243],
[329,253,220,253,278,0,219,256],
[275,242,264,238,322,281,0,314],
[304,221,189,177,257,244,186,0]])



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
result = np.append(np.array([8, 500, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,260,262,247,244,251,257],
[235,0,250,273,247,243,240,237],
[240,250,0,250,236,247,236,245],
[238,227,250,0,243,229,236,225],
[253,253,264,257,0,242,246,269],
[256,257,253,271,258,0,250,248],
[249,260,264,264,254,250,0,247],
[243,263,255,275,231,252,253,0]])



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
result = np.append(np.array([8, 500, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,243,253,266,252,248,232],
[231,0,246,248,258,265,239,232],
[257,254,0,259,255,248,262,260],
[247,252,241,0,246,258,260,241],
[234,242,245,254,0,250,250,249],
[248,235,252,242,250,0,257,256],
[252,261,238,240,250,243,0,258],
[268,268,240,259,251,244,242,0]])



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
result = np.append(np.array([8, 500, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,254,242,243,244,262,258],
[251,0,259,257,242,257,262,260],
[246,241,0,250,244,250,250,262],
[258,243,250,0,248,255,249,264],
[257,258,256,252,0,271,241,254],
[256,243,250,245,229,0,238,248],
[238,238,250,251,259,262,0,256],
[242,240,238,236,246,252,244,0]])



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
result = np.append(np.array([8, 500, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,265,246,241,247,257,248],
[257,0,248,258,248,253,262,242],
[235,252,0,236,212,241,247,228],
[254,242,264,0,240,237,243,248],
[259,252,288,260,0,241,249,248],
[253,247,259,263,259,0,256,249],
[243,238,253,257,251,244,0,252],
[252,258,272,252,252,251,248,0]])



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
result = np.append(np.array([8, 500, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,236,221,244,234,247,260,255],
[264,0,250,264,254,267,273,269],
[279,250,0,268,264,262,269,277],
[256,236,232,0,252,251,265,247],
[266,246,236,248,0,266,270,256],
[253,233,238,249,234,0,259,254],
[240,227,231,235,230,241,0,246],
[245,231,223,253,244,246,254,0]])



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
result = np.append(np.array([8, 500, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,282,278,328,208,267,206,241],
[218,0,232,291,187,233,223,284],
[222,268,0,266,229,239,162,207],
[172,209,234,0,203,200,137,206],
[292,313,271,297,0,233,267,281],
[233,267,261,300,267,0,216,300],
[294,277,338,363,233,284,0,275],
[259,216,293,294,219,200,225,0]])



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
result = np.append(np.array([8, 500, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,260,241,253,237,268,241],
[237,0,253,214,224,240,232,245],
[240,247,0,222,219,228,222,243],
[259,286,278,0,240,245,262,267],
[247,276,281,260,0,249,250,256],
[263,260,272,255,251,0,247,236],
[232,268,278,238,250,253,0,240],
[259,255,257,233,244,264,260,0]])



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
result = np.append(np.array([8, 500, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,236,235,255,231,244,228],
[247,0,228,244,241,251,270,253],
[264,272,0,247,274,253,264,264],
[265,256,253,0,257,250,248,272],
[245,259,226,243,0,247,234,245],
[269,249,247,250,253,0,244,245],
[256,230,236,252,266,256,0,251],
[272,247,236,228,255,255,249,0]])



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
result = np.append(np.array([8, 500, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,217,233,235,227,233,264],
[266,0,255,266,258,249,248,277],
[283,245,0,262,233,235,221,279],
[267,234,238,0,262,249,250,286],
[265,242,267,238,0,246,225,261],
[273,251,265,251,254,0,237,288],
[267,252,279,250,275,263,0,273],
[236,223,221,214,239,212,227,0]])



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
result = np.append(np.array([8, 500, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,254,260,238,261,270,263],
[236,0,267,254,236,262,269,250],
[246,233,0,232,240,252,259,253],
[240,246,268,0,236,260,263,249],
[262,264,260,264,0,242,261,259],
[239,238,248,240,258,0,256,253],
[230,231,241,237,239,244,0,241],
[237,250,247,251,241,247,259,0]])



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
result = np.append(np.array([8, 500, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,249,252,253,252,252,260],
[252,0,250,238,247,250,239,248],
[251,250,0,231,238,259,256,265],
[248,262,269,0,245,266,271,278],
[247,253,262,255,0,259,251,270],
[248,250,241,234,241,0,251,264],
[248,261,244,229,249,249,0,253],
[240,252,235,222,230,236,247,0]])



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
result = np.append(np.array([8, 500, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,278,254,309,246,243,318,230],
[222,0,244,191,262,264,275,205],
[246,256,0,230,234,270,276,221],
[191,309,270,0,266,257,325,216],
[254,238,266,234,0,259,313,214],
[257,236,230,243,241,0,206,275],
[182,225,224,175,187,294,0,148],
[270,295,279,284,286,225,352,0]])



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
result = np.append(np.array([8, 500, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,259,251,261,248,261,242],
[249,0,239,252,254,241,264,267],
[241,261,0,246,253,266,246,253],
[249,248,254,0,248,250,254,255],
[239,246,247,252,0,247,251,251],
[252,259,234,250,253,0,266,235],
[239,236,254,246,249,234,0,238],
[258,233,247,245,249,265,262,0]])



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
result = np.append(np.array([8, 500, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,285,289,264,267,276,258],
[250,0,258,283,254,244,272,253],
[215,242,0,262,228,237,256,214],
[211,217,238,0,217,272,245,251],
[236,246,272,283,0,264,260,259],
[233,256,263,228,236,0,249,259],
[224,228,244,255,240,251,0,256],
[242,247,286,249,241,241,244,0]])



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
result = np.append(np.array([8, 500, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,220,243,222,233,233,260],
[257,0,241,249,246,238,252,258],
[280,259,0,234,248,246,247,259],
[257,251,266,0,251,238,245,251],
[278,254,252,249,0,253,250,249],
[267,262,254,262,247,0,254,268],
[267,248,253,255,250,246,0,261],
[240,242,241,249,251,232,239,0]])



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
result = np.append(np.array([8, 500, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,243,293,254,242,305,255],
[236,0,267,302,238,191,301,275],
[257,233,0,296,278,233,232,268],
[207,198,204,0,195,161,242,199],
[246,262,222,305,0,260,248,237],
[258,309,267,339,240,0,267,301],
[195,199,268,258,252,233,0,250],
[245,225,232,301,263,199,250,0]])



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
result = np.append(np.array([8, 500, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,259,245,234,245,238,251],
[254,0,262,241,239,244,242,266],
[241,238,0,247,232,239,241,227],
[255,259,253,0,228,245,234,246],
[266,261,268,272,0,262,260,250],
[255,256,261,255,238,0,239,237],
[262,258,259,266,240,261,0,249],
[249,234,273,254,250,263,251,0]])



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
result = np.append(np.array([8, 500, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,248,257,272,265,227,253],
[245,0,275,250,252,269,261,244],
[252,225,0,252,249,257,248,295],
[243,250,248,0,259,228,246,248],
[228,248,251,241,0,246,244,255],
[235,231,243,272,254,0,262,265],
[273,239,252,254,256,238,0,256],
[247,256,205,252,245,235,244,0]])



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
result = np.append(np.array([8, 500, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,282,249,291,264,274,247,272],
[218,0,225,239,234,240,213,223],
[251,275,0,291,255,244,250,270],
[209,261,209,0,214,208,208,235],
[236,266,245,286,0,253,236,251],
[226,260,256,292,247,0,227,268],
[253,287,250,292,264,273,0,273],
[228,277,230,265,249,232,227,0]])



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
result = np.append(np.array([8, 500, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,266,242,242,262,244,251],
[241,0,262,233,240,241,254,241],
[234,238,0,235,239,246,251,230],
[258,267,265,0,241,260,246,237],
[258,260,261,259,0,249,264,242],
[238,259,254,240,251,0,248,236],
[256,246,249,254,236,252,0,241],
[249,259,270,263,258,264,259,0]])



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
result = np.append(np.array([8, 500, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,251,253,263,255,253,268],
[250,0,254,236,261,250,245,252],
[249,246,0,241,248,249,247,252],
[247,264,259,0,261,249,252,256],
[237,239,252,239,0,240,252,245],
[245,250,251,251,260,0,253,263],
[247,255,253,248,248,247,0,255],
[232,248,248,244,255,237,245,0]])



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
result = np.append(np.array([8, 500, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,229,246,254,271,241,256],
[224,0,237,228,236,252,245,234],
[271,263,0,257,244,272,276,253],
[254,272,243,0,246,257,260,275],
[246,264,256,254,0,248,250,245],
[229,248,228,243,252,0,252,225],
[259,255,224,240,250,248,0,248],
[244,266,247,225,255,275,252,0]])



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
result = np.append(np.array([8, 500, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,247,253,266,259,259,238],
[249,0,254,247,249,243,264,241],
[253,246,0,241,248,242,249,252],
[247,253,259,0,247,255,262,264],
[234,251,252,253,0,229,236,248],
[241,257,258,245,271,0,272,255],
[241,236,251,238,264,228,0,256],
[262,259,248,236,252,245,244,0]])



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
result = np.append(np.array([8, 500, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,254,261,271,260,255,274],
[265,0,269,267,265,259,266,247],
[246,231,0,250,261,259,246,246],
[239,233,250,0,247,238,241,249],
[229,235,239,253,0,231,265,231],
[240,241,241,262,269,0,248,269],
[245,234,254,259,235,252,0,265],
[226,253,254,251,269,231,235,0]])



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
result = np.append(np.array([8, 500, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,244,265,243,271,255,256],
[232,0,242,235,230,268,239,243],
[256,258,0,245,262,261,228,254],
[235,265,255,0,254,260,253,257],
[257,270,238,246,0,267,258,259],
[229,232,239,240,233,0,213,230],
[245,261,272,247,242,287,0,253],
[244,257,246,243,241,270,247,0]])



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
result = np.append(np.array([8, 500, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,241,267,257,267,251,254],
[253,0,254,246,260,268,256,255],
[259,246,0,256,249,264,261,253],
[233,254,244,0,242,271,250,245],
[243,240,251,258,0,254,259,259],
[233,232,236,229,246,0,239,250],
[249,244,239,250,241,261,0,238],
[246,245,247,255,241,250,262,0]])



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
result = np.append(np.array([8, 500, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,248,254,252,255,248,242],
[258,0,264,262,234,248,250,245],
[252,236,0,262,231,250,227,228],
[246,238,238,0,237,232,249,249],
[248,266,269,263,0,253,277,268],
[245,252,250,268,247,0,263,256],
[252,250,273,251,223,237,0,251],
[258,255,272,251,232,244,249,0]])



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
result = np.append(np.array([8, 500, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,267,251,247,264,256,263],
[243,0,251,260,252,263,227,241],
[233,249,0,268,263,277,240,259],
[249,240,232,0,261,242,228,249],
[253,248,237,239,0,267,230,248],
[236,237,223,258,233,0,243,239],
[244,273,260,272,270,257,0,266],
[237,259,241,251,252,261,234,0]])



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
result = np.append(np.array([8, 500, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,228,218,240,233,216,214],
[273,0,252,244,240,229,244,245],
[272,248,0,240,236,225,242,215],
[282,256,260,0,242,243,241,227],
[260,260,264,258,0,262,244,258],
[267,271,275,257,238,0,233,254],
[284,256,258,259,256,267,0,247],
[286,255,285,273,242,246,253,0]])



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
result = np.append(np.array([8, 500, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,265,234,260,261,234,255],
[262,0,273,241,261,248,251,254],
[235,227,0,226,255,237,242,258],
[266,259,274,0,270,249,247,255],
[240,239,245,230,0,245,249,265],
[239,252,263,251,255,0,251,268],
[266,249,258,253,251,249,0,257],
[245,246,242,245,235,232,243,0]])



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
result = np.append(np.array([8, 500, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,266,233,251,242,234,245],
[243,0,258,238,251,243,247,250],
[234,242,0,238,260,240,239,246],
[267,262,262,0,265,253,255,249],
[249,249,240,235,0,238,240,241],
[258,257,260,247,262,0,247,251],
[266,253,261,245,260,253,0,260],
[255,250,254,251,259,249,240,0]])



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
result = np.append(np.array([8, 500, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,263,261,255,270,270,276],
[251,0,256,269,264,276,249,276],
[237,244,0,251,240,249,254,253],
[239,231,249,0,241,260,239,261],
[245,236,260,259,0,258,255,252],
[230,224,251,240,242,0,238,248],
[230,251,246,261,245,262,0,257],
[224,224,247,239,248,252,243,0]])



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
result = np.append(np.array([8, 500, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,246,237,247,247,235,253],
[247,0,268,236,252,239,246,268],
[254,232,0,250,258,245,256,256],
[263,264,250,0,285,252,259,258],
[253,248,242,215,0,248,237,256],
[253,261,255,248,252,0,240,275],
[265,254,244,241,263,260,0,261],
[247,232,244,242,244,225,239,0]])



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
result = np.append(np.array([8, 500, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,245,258,231,269,254,257],
[248,0,238,250,244,242,249,241],
[255,262,0,243,256,258,243,253],
[242,250,257,0,248,258,248,241],
[269,256,244,252,0,264,245,233],
[231,258,242,242,236,0,240,241],
[246,251,257,252,255,260,0,246],
[243,259,247,259,267,259,254,0]])



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
result = np.append(np.array([8, 500, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,251,253,252,234,248,250],
[245,0,281,267,265,269,254,233],
[249,219,0,253,248,244,248,224],
[247,233,247,0,249,247,235,231],
[248,235,252,251,0,233,241,254],
[266,231,256,253,267,0,247,245],
[252,246,252,265,259,253,0,241],
[250,267,276,269,246,255,259,0]])



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
result = np.append(np.array([8, 500, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,212,172,284,291,256,249],
[257,0,240,213,285,330,225,315],
[288,260,0,279,233,357,256,201],
[328,287,221,0,289,378,290,284],
[216,215,267,211,0,252,250,248],
[209,170,143,122,248,0,243,181],
[244,275,244,210,250,257,0,241],
[251,185,299,216,252,319,259,0]])



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
result = np.append(np.array([8, 500, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,247,274,258,255,253,258],
[223,0,240,226,216,223,228,232],
[253,260,0,240,243,257,259,241],
[226,274,260,0,242,237,260,243],
[242,284,257,258,0,262,263,246],
[245,277,243,263,238,0,251,248],
[247,272,241,240,237,249,0,240],
[242,268,259,257,254,252,260,0]])



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
result = np.append(np.array([8, 500, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,240,249,209,215,237,235,214],
[260,0,263,256,250,268,252,247],
[251,237,0,256,233,246,234,249],
[291,244,244,0,253,261,255,256],
[285,250,267,247,0,243,254,243],
[263,232,254,239,257,0,238,220],
[265,248,266,245,246,262,0,263],
[286,253,251,244,257,280,237,0]])



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
result = np.append(np.array([8, 500, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,245,238,253,240,224,234],
[265,0,264,264,258,249,257,253],
[255,236,0,238,258,261,247,245],
[262,236,262,0,267,248,252,263],
[247,242,242,233,0,242,254,234],
[260,251,239,252,258,0,247,236],
[276,243,253,248,246,253,0,254],
[266,247,255,237,266,264,246,0]])



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
result = np.append(np.array([8, 500, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,257,273,233,221,249,238],
[250,0,267,266,241,224,238,223],
[243,233,0,254,252,226,250,228],
[227,234,246,0,212,204,241,221],
[267,259,248,288,0,240,290,258],
[279,276,274,296,260,0,276,248],
[251,262,250,259,210,224,0,224],
[262,277,272,279,242,252,276,0]])



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
result = np.append(np.array([8, 500, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,250,273,259,254,253,243],
[255,0,243,255,243,250,254,249],
[250,257,0,265,251,245,227,247],
[227,245,235,0,236,226,229,242],
[241,257,249,264,0,255,240,250],
[246,250,255,274,245,0,243,248],
[247,246,273,271,260,257,0,246],
[257,251,253,258,250,252,254,0]])



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
result = np.append(np.array([8, 500, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,242,256,271,269,268,232],
[259,0,271,268,279,272,284,226],
[258,229,0,260,265,243,263,251],
[244,232,240,0,268,250,247,230],
[229,221,235,232,0,238,245,221],
[231,228,257,250,262,0,282,247],
[232,216,237,253,255,218,0,216],
[268,274,249,270,279,253,284,0]])



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
result = np.append(np.array([8, 500, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,254,243,203,261,230,206],
[243,0,231,235,197,237,219,210],
[246,269,0,229,268,296,277,250],
[257,265,271,0,229,281,256,245],
[297,303,232,271,0,309,282,239],
[239,263,204,219,191,0,221,183],
[270,281,223,244,218,279,0,238],
[294,290,250,255,261,317,262,0]])



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
result = np.append(np.array([8, 500, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,226,5,221,203,5,0],
[426,0,226,424,221,424,226,421],
[274,274,0,203,419,203,74,200],
[495,76,297,0,221,421,295,297],
[279,279,81,279,0,205,81,274],
[297,76,297,79,295,0,74,297],
[495,274,426,205,419,426,0,421],
[500,79,300,203,226,203,79,0]])



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
result = np.append(np.array([8, 500, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,250,237,243,241,240,255],
[257,0,255,243,242,245,236,268],
[250,245,0,242,240,237,244,246],
[263,257,258,0,230,240,236,239],
[257,258,260,270,0,253,250,262],
[259,255,263,260,247,0,248,248],
[260,264,256,264,250,252,0,255],
[245,232,254,261,238,252,245,0]])



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
result = np.append(np.array([8, 500, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,256,247,247,290,261,230],
[254,0,248,263,255,256,269,264],
[244,252,0,268,236,247,272,266],
[253,237,232,0,246,255,227,224],
[253,245,264,254,0,247,248,256],
[210,244,253,245,253,0,263,218],
[239,231,228,273,252,237,0,237],
[270,236,234,276,244,282,263,0]])



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
result = np.append(np.array([8, 500, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,268,254,257,268,251,265],
[251,0,235,233,270,246,270,262],
[232,265,0,244,246,260,241,250],
[246,267,256,0,264,268,252,265],
[243,230,254,236,0,260,261,271],
[232,254,240,232,240,0,276,253],
[249,230,259,248,239,224,0,283],
[235,238,250,235,229,247,217,0]])



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
result = np.append(np.array([8, 500, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,259,275,251,237,264,231,272],
[241,0,279,264,266,225,225,254],
[225,221,0,229,269,210,181,274],
[249,236,271,0,234,200,189,270],
[263,234,231,266,0,229,216,265],
[236,275,290,300,271,0,262,273],
[269,275,319,311,284,238,0,307],
[228,246,226,230,235,227,193,0]])



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
result = np.append(np.array([8, 500, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,244,257,263,257,261,250],
[232,0,232,265,250,241,232,254],
[256,268,0,258,257,242,258,258],
[243,235,242,0,234,231,221,243],
[237,250,243,266,0,242,236,238],
[243,259,258,269,258,0,245,254],
[239,268,242,279,264,255,0,274],
[250,246,242,257,262,246,226,0]])



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
result = np.append(np.array([8, 500, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,293,254,267,271,306,156,279],
[207,0,226,222,245,254,182,247],
[246,274,0,243,187,274,203,279],
[233,278,257,0,226,266,251,312],
[229,255,313,274,0,272,173,246],
[194,246,226,234,228,0,176,257],
[344,318,297,249,327,324,0,294],
[221,253,221,188,254,243,206,0]])



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
result = np.append(np.array([8, 500, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,294,257,258,278,286,263],
[267,0,279,234,215,286,254,249],
[206,221,0,197,208,246,263,220],
[243,266,303,0,261,295,307,278],
[242,285,292,239,0,300,282,280],
[222,214,254,205,200,0,254,220],
[214,246,237,193,218,246,0,202],
[237,251,280,222,220,280,298,0]])



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
result = np.append(np.array([8, 500, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,284,268,264,253,260,272,250],
[216,0,255,261,226,266,252,242],
[232,245,0,249,228,245,237,244],
[236,239,251,0,234,230,250,265],
[247,274,272,266,0,227,256,256],
[240,234,255,270,273,0,266,255],
[228,248,263,250,244,234,0,247],
[250,258,256,235,244,245,253,0]])



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
result = np.append(np.array([8, 500, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,227,247,253,268,241,235,247],
[273,0,270,255,257,259,240,259],
[253,230,0,263,261,269,253,264],
[247,245,237,0,264,244,247,253],
[232,243,239,236,0,260,233,229],
[259,241,231,256,240,0,230,251],
[265,260,247,253,267,270,0,264],
[253,241,236,247,271,249,236,0]])



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
result = np.append(np.array([8, 500, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,235,230,242,257,256,230],
[259,0,230,235,244,225,258,219],
[265,270,0,239,244,250,268,259],
[270,265,261,0,252,248,265,238],
[258,256,256,248,0,259,260,251],
[243,275,250,252,241,0,250,247],
[244,242,232,235,240,250,0,231],
[270,281,241,262,249,253,269,0]])



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
result = np.append(np.array([8, 500, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,252,246,302,234,259,245],
[247,0,254,257,316,269,270,261],
[248,246,0,264,309,272,292,286],
[254,243,236,0,291,240,271,241],
[198,184,191,209,0,218,203,199],
[266,231,228,260,282,0,236,236],
[241,230,208,229,297,264,0,216],
[255,239,214,259,301,264,284,0]])



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
result = np.append(np.array([8, 500, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,232,237,245,239,237,233,266],
[268,0,258,262,255,240,241,270],
[263,242,0,262,242,252,247,270],
[255,238,238,0,248,237,246,274],
[261,245,258,252,0,238,251,276],
[263,260,248,263,262,0,253,278],
[267,259,253,254,249,247,0,277],
[234,230,230,226,224,222,223,0]])



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
result = np.append(np.array([8, 500, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,267,243,237,252,274,259],
[265,0,257,245,265,261,291,253],
[233,243,0,237,249,254,270,231],
[257,255,263,0,248,258,287,258],
[263,235,251,252,0,250,278,261],
[248,239,246,242,250,0,278,241],
[226,209,230,213,222,222,0,218],
[241,247,269,242,239,259,282,0]])



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
result = np.append(np.array([8, 500, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,262,254,249,259,257,256],
[261,0,245,247,268,232,279,255],
[238,255,0,256,253,245,270,264],
[246,253,244,0,270,256,267,255],
[251,232,247,230,0,238,249,248],
[241,268,255,244,262,0,254,252],
[243,221,230,233,251,246,0,238],
[244,245,236,245,252,248,262,0]])



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
result = np.append(np.array([8, 500, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,249,253,247,275,253,274],
[250,0,239,216,233,230,211,262],
[251,261,0,239,240,238,232,256],
[247,284,261,0,266,274,233,270],
[253,267,260,234,0,269,241,239],
[225,270,262,226,231,0,210,250],
[247,289,268,267,259,290,0,266],
[226,238,244,230,261,250,234,0]])



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
result = np.append(np.array([8, 500, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,256,232,240,262,235,248],
[242,0,241,241,227,243,237,242],
[244,259,0,255,234,261,235,250],
[268,259,245,0,247,261,251,266],
[260,273,266,253,0,265,232,253],
[238,257,239,239,235,0,246,258],
[265,263,265,249,268,254,0,252],
[252,258,250,234,247,242,248,0]])



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
result = np.append(np.array([8, 500, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,222,269,276,269,287,247],
[262,0,175,195,218,316,214,223],
[278,325,0,234,373,277,279,318],
[231,305,266,0,327,333,297,282],
[224,282,127,173,0,251,256,175],
[231,184,223,167,249,0,253,216],
[213,286,221,203,244,247,0,299],
[253,277,182,218,325,284,201,0]])



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
result = np.append(np.array([8, 500, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,246,256,263,273,252,240],
[244,0,256,248,244,272,240,234],
[254,244,0,233,244,263,230,229],
[244,252,267,0,253,269,251,239],
[237,256,256,247,0,275,248,234],
[227,228,237,231,225,0,249,222],
[248,260,270,249,252,251,0,252],
[260,266,271,261,266,278,248,0]])



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
result = np.append(np.array([8, 500, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,232,250,280,253,242,226],
[257,0,233,237,273,243,237,231],
[268,267,0,252,271,237,247,232],
[250,263,248,0,265,260,271,263],
[220,227,229,235,0,232,222,209],
[247,257,263,240,268,0,250,253],
[258,263,253,229,278,250,0,269],
[274,269,268,237,291,247,231,0]])



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
result = np.append(np.array([8, 500, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,246,253,271,268,261,257],
[245,0,244,230,275,242,277,240],
[254,256,0,243,253,226,258,215],
[247,270,257,0,257,255,263,264],
[229,225,247,243,0,223,222,247],
[232,258,274,245,277,0,243,249],
[239,223,242,237,278,257,0,241],
[243,260,285,236,253,251,259,0]])



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
result = np.append(np.array([8, 500, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,270,256,232,261,268,269],
[254,0,260,265,257,231,265,271],
[230,240,0,240,244,238,250,279],
[244,235,260,0,242,245,264,264],
[268,243,256,258,0,263,250,274],
[239,269,262,255,237,0,263,276],
[232,235,250,236,250,237,0,253],
[231,229,221,236,226,224,247,0]])



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
result = np.append(np.array([8, 500, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,245,287,258,266,277,334],
[272,0,239,307,280,295,311,302],
[255,261,0,257,248,255,310,318],
[213,193,243,0,198,220,227,249],
[242,220,252,302,0,228,272,312],
[234,205,245,280,272,0,353,307],
[223,189,190,273,228,147,0,266],
[166,198,182,251,188,193,234,0]])



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
result = np.append(np.array([8, 500, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,277,233,275,264,283,258,263],
[223,0,241,265,256,290,210,245],
[267,259,0,260,249,326,226,249],
[225,235,240,0,249,253,214,219],
[236,244,251,251,0,247,213,243],
[217,210,174,247,253,0,218,211],
[242,290,274,286,287,282,0,268],
[237,255,251,281,257,289,232,0]])



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
result = np.append(np.array([8, 500, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,248,252,255,243,273,239],
[243,0,235,262,240,241,262,238],
[252,265,0,270,252,250,273,252],
[248,238,230,0,243,240,251,242],
[245,260,248,257,0,246,258,229],
[257,259,250,260,254,0,256,226],
[227,238,227,249,242,244,0,246],
[261,262,248,258,271,274,254,0]])



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
result = np.append(np.array([8, 500, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,238,213,262,215,228,213,223],
[262,0,219,264,240,250,244,225],
[287,281,0,231,230,241,221,210],
[238,236,269,0,218,203,238,237],
[285,260,270,282,0,219,278,227],
[272,250,259,297,281,0,232,266],
[287,256,279,262,222,268,0,237],
[277,275,290,263,273,234,263,0]])



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
result = np.append(np.array([8, 500, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,250,255,244,252,255,257],
[240,0,254,246,247,247,257,247],
[250,246,0,249,252,251,269,260],
[245,254,251,0,253,247,250,260],
[256,253,248,247,0,255,257,261],
[248,253,249,253,245,0,262,251],
[245,243,231,250,243,238,0,238],
[243,253,240,240,239,249,262,0]])



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
result = np.append(np.array([8, 500, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,251,240,253,232,260,287,273],
[249,0,250,280,264,255,292,248],
[260,250,0,278,270,268,279,299],
[247,220,222,0,244,209,255,236],
[268,236,230,256,0,244,276,263],
[240,245,232,291,256,0,277,253],
[213,208,221,245,224,223,0,220],
[227,252,201,264,237,247,280,0]])



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
result = np.append(np.array([8, 500, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,228,235,218,227,198,215,284],
[272,0,217,222,210,216,196,299],
[265,283,0,252,259,171,243,262],
[282,278,248,0,272,237,270,287],
[273,290,241,228,0,222,241,267],
[302,284,329,263,278,0,234,298],
[285,304,257,230,259,266,0,269],
[216,201,238,213,233,202,231,0]])



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
result = np.append(np.array([8, 500, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,271,250,283,259,257,253,263],
[229,0,265,264,249,241,238,240],
[250,235,0,265,233,245,209,236],
[217,236,235,0,235,210,213,237],
[241,251,267,265,0,252,236,264],
[243,259,255,290,248,0,246,264],
[247,262,291,287,264,254,0,276],
[237,260,264,263,236,236,224,0]])



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
result = np.append(np.array([8, 500, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,276,264,238,252,233,255,258],
[224,0,242,224,226,218,252,245],
[236,258,0,206,233,227,263,240],
[262,276,294,0,259,232,271,251],
[248,274,267,241,0,218,277,258],
[267,282,273,268,282,0,260,238],
[245,248,237,229,223,240,0,218],
[242,255,260,249,242,262,282,0]])



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
result = np.append(np.array([8, 500, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,282,253,278,263,267,260],
[252,0,259,248,252,254,254,258],
[218,241,0,228,245,239,249,230],
[247,252,272,0,256,248,265,261],
[222,248,255,244,0,252,260,242],
[237,246,261,252,248,0,249,255],
[233,246,251,235,240,251,0,261],
[240,242,270,239,258,245,239,0]])



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
result = np.append(np.array([8, 500, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,262,260,265,248,258,260,272],
[238,0,241,261,241,251,249,253],
[240,259,0,270,244,245,238,250],
[235,239,230,0,234,245,235,247],
[252,259,256,266,0,254,249,262],
[242,249,255,255,246,0,249,254],
[240,251,262,265,251,251,0,280],
[228,247,250,253,238,246,220,0]])



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
result = np.append(np.array([8, 500, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,245,261,267,244,268,254],
[258,0,250,269,279,260,259,275],
[255,250,0,271,270,253,268,259],
[239,231,229,0,249,236,240,249],
[233,221,230,251,0,236,249,238],
[256,240,247,264,264,0,263,266],
[232,241,232,260,251,237,0,233],
[246,225,241,251,262,234,267,0]])



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
result = np.append(np.array([8, 500, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,311,357,201,357,342,258,357],
[189,0,255,99,255,342,0,255],
[143,245,0,344,398,401,59,314],
[299,401,156,0,246,342,215,314],
[143,245,102,254,0,342,53,410],
[158,158,99,158,158,0,158,158],
[242,500,441,285,447,342,0,447],
[143,245,186,186,90,342,53,0]])



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
result = np.append(np.array([8, 500, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,242,228,213,223,213,229],
[265,0,264,321,245,269,287,267],
[258,236,0,292,260,263,258,268],
[272,179,208,0,206,208,193,218],
[287,255,240,294,0,255,293,247],
[277,231,237,292,245,0,253,253],
[287,213,242,307,207,247,0,251],
[271,233,232,282,253,247,249,0]])



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
result = np.append(np.array([8, 500, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,231,225,256,233,259,240,242],
[269,0,255,250,251,271,250,255],
[275,245,0,257,259,271,238,235],
[244,250,243,0,241,246,254,225],
[267,249,241,259,0,282,255,248],
[241,229,229,254,218,0,242,231],
[260,250,262,246,245,258,0,257],
[258,245,265,275,252,269,243,0]])



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
result = np.append(np.array([8, 500, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,217,293,242,271,286,305,230],
[283,0,315,269,243,257,282,248],
[207,185,0,247,272,255,265,197],
[258,231,253,0,270,221,281,260],
[229,257,228,230,0,320,204,249],
[214,243,245,279,180,0,266,193],
[195,218,235,219,296,234,0,171],
[270,252,303,240,251,307,329,0]])



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
result = np.append(np.array([8, 500, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,264,265,243,250,231,230],
[266,0,251,246,262,230,227,227],
[236,249,0,254,213,253,236,219],
[235,254,246,0,227,228,235,234],
[257,238,287,273,0,234,250,238],
[250,270,247,272,266,0,258,262],
[269,273,264,265,250,242,0,221],
[270,273,281,266,262,238,279,0]])



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
result = np.append(np.array([8, 500, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,243,230,227,223,246,239],
[242,0,232,229,240,236,242,253],
[257,268,0,248,256,266,264,282],
[270,271,252,0,296,248,268,285],
[273,260,244,204,0,225,242,257],
[277,264,234,252,275,0,227,258],
[254,258,236,232,258,273,0,259],
[261,247,218,215,243,242,241,0]])



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
result = np.append(np.array([8, 500, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,276,275,239,271,247,261],
[255,0,253,257,237,245,220,246],
[224,247,0,272,209,208,224,210],
[225,243,228,0,209,219,196,227],
[261,263,291,291,0,239,249,246],
[229,255,292,281,261,0,257,239],
[253,280,276,304,251,243,0,262],
[239,254,290,273,254,261,238,0]])



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
result = np.append(np.array([8, 500, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,229,212,312,228,195,213],
[246,0,199,262,249,278,222,213],
[271,301,0,249,310,270,297,276],
[288,238,251,0,283,216,234,218],
[188,251,190,217,0,253,191,178],
[272,222,230,284,247,0,221,218],
[305,278,203,266,309,279,0,237],
[287,287,224,282,322,282,263,0]])



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
result = np.append(np.array([8, 500, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,267,263,228,182,260,271],
[257,0,260,254,253,224,283,243],
[233,240,0,247,261,226,239,237],
[237,246,253,0,263,250,253,233],
[272,247,239,237,0,223,258,255],
[318,276,274,250,277,0,272,252],
[240,217,261,247,242,228,0,241],
[229,257,263,267,245,248,259,0]])



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
result = np.append(np.array([8, 500, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,267,244,261,243,248,252,243],
[233,0,205,269,216,236,237,229],
[256,295,0,253,239,264,246,246],
[239,231,247,0,239,246,219,246],
[257,284,261,261,0,259,232,242],
[252,264,236,254,241,0,231,241],
[248,263,254,281,268,269,0,273],
[257,271,254,254,258,259,227,0]])



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
result = np.append(np.array([8, 500, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,254,230,264,264,240,251],
[251,0,260,248,262,256,258,270],
[246,240,0,232,232,230,231,240],
[270,252,268,0,283,275,244,273],
[236,238,268,217,0,238,214,227],
[236,244,270,225,262,0,246,265],
[260,242,269,256,286,254,0,278],
[249,230,260,227,273,235,222,0]])



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
result = np.append(np.array([8, 500, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,231,227,234,219,252,248],
[259,0,242,249,242,228,254,260],
[269,258,0,250,267,243,250,261],
[273,251,250,0,253,252,248,251],
[266,258,233,247,0,248,255,275],
[281,272,257,248,252,0,274,258],
[248,246,250,252,245,226,0,254],
[252,240,239,249,225,242,246,0]])



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
result = np.append(np.array([8, 500, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,267,231,250,282,264,252],
[243,0,203,222,250,214,215,199],
[233,297,0,258,262,299,220,240],
[269,278,242,0,258,277,275,259],
[250,250,238,242,0,279,237,248],
[218,286,201,223,221,0,210,189],
[236,285,280,225,263,290,0,285],
[248,301,260,241,252,311,215,0]])



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
result = np.append(np.array([8, 500, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,235,241,233,235,226,262,259],
[265,0,247,245,260,251,276,270],
[259,253,0,244,247,258,269,276],
[267,255,256,0,259,242,279,273],
[265,240,253,241,0,251,258,253],
[274,249,242,258,249,0,263,257],
[238,224,231,221,242,237,0,250],
[241,230,224,227,247,243,250,0]])



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
result = np.append(np.array([8, 500, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,234,245,249,240,241,254,255],
[266,0,251,240,273,250,268,269],
[255,249,0,242,254,233,264,263],
[251,260,258,0,248,240,242,247],
[260,227,246,252,0,230,239,252],
[259,250,267,260,270,0,261,249],
[246,232,236,258,261,239,0,265],
[245,231,237,253,248,251,235,0]])



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
result = np.append(np.array([8, 500, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,250,252,270,234,241,263],
[235,0,265,262,286,270,274,248],
[250,235,0,266,245,256,248,235],
[248,238,234,0,255,260,237,226],
[230,214,255,245,0,234,254,272],
[266,230,244,240,266,0,268,244],
[259,226,252,263,246,232,0,214],
[237,252,265,274,228,256,286,0]])



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
result = np.append(np.array([8, 500, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,265,268,273,251,231,243,249],
[235,0,256,262,248,251,234,262],
[232,244,0,250,234,255,244,267],
[227,238,250,0,254,239,258,257],
[249,252,266,246,0,239,245,241],
[269,249,245,261,261,0,249,253],
[257,266,256,242,255,251,0,239],
[251,238,233,243,259,247,261,0]])



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
result = np.append(np.array([8, 500, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,226,284,233,253,204,229],
[259,0,260,340,259,243,213,218],
[274,240,0,259,261,289,235,235],
[216,160,241,0,229,192,221,206],
[267,241,239,271,0,253,214,233],
[247,257,211,308,247,0,253,230],
[296,287,265,279,286,247,0,268],
[271,282,265,294,267,270,232,0]])



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
result = np.append(np.array([8, 500, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,255,249,271,274,292,278],
[248,0,257,252,258,281,284,286],
[245,243,0,278,271,244,233,300],
[251,248,222,0,300,271,213,261],
[229,242,229,200,0,250,234,270],
[226,219,256,229,250,0,278,290],
[208,216,267,287,266,222,0,243],
[222,214,200,239,230,210,257,0]])



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
result = np.append(np.array([8, 500, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,233,252,247,245,242,261,259],
[267,0,264,252,235,255,272,277],
[248,236,0,249,251,232,244,262],
[253,248,251,0,247,248,273,264],
[255,265,249,253,0,257,255,263],
[258,245,268,252,243,0,256,266],
[239,228,256,227,245,244,0,253],
[241,223,238,236,237,234,247,0]])



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
result = np.append(np.array([8, 500, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,246,241,258,252,244,242,279],
[254,0,251,251,263,255,252,250],
[259,249,0,258,270,243,231,246],
[242,249,242,0,244,230,254,244],
[248,237,230,256,0,248,240,252],
[256,245,257,270,252,0,251,253],
[258,248,269,246,260,249,0,251],
[221,250,254,256,248,247,249,0]])



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
result = np.append(np.array([8, 500, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,256,295,278,314,267,253],
[251,0,226,275,228,275,260,225],
[244,274,0,301,252,278,265,249],
[205,225,199,0,234,264,266,201],
[222,272,248,266,0,285,256,222],
[186,225,222,236,215,0,234,179],
[233,240,235,234,244,266,0,217],
[247,275,251,299,278,321,283,0]])



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
result = np.append(np.array([8, 500, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,205,199,233,241,193,229,227],
[295,0,244,312,286,240,280,228],
[301,256,0,278,230,233,239,258],
[267,188,222,0,218,233,213,241],
[259,214,270,282,0,252,235,227],
[307,260,267,267,248,0,227,241],
[271,220,261,287,265,273,0,256],
[273,272,242,259,273,259,244,0]])



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
result = np.append(np.array([8, 500, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,194,199,220,228,227,198,242],
[306,0,246,247,253,266,271,282],
[301,254,0,294,236,284,244,277],
[280,253,206,0,226,251,224,254],
[272,247,264,274,0,242,277,282],
[273,234,216,249,258,0,222,266],
[302,229,256,276,223,278,0,287],
[258,218,223,246,218,234,213,0]])



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
result = np.append(np.array([8, 500, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,246,236,269,247,253,256],
[250,0,235,245,272,245,257,247],
[254,265,0,242,272,247,258,249],
[264,255,258,0,276,257,240,255],
[231,228,228,224,0,242,229,235],
[253,255,253,243,258,0,251,239],
[247,243,242,260,271,249,0,253],
[244,253,251,245,265,261,247,0]])



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
result = np.append(np.array([8, 500, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,245,254,257,242,239,244],
[244,0,239,239,265,234,247,231],
[255,261,0,250,281,245,245,242],
[246,261,250,0,269,257,261,254],
[243,235,219,231,0,228,224,233],
[258,266,255,243,272,0,250,243],
[261,253,255,239,276,250,0,254],
[256,269,258,246,267,257,246,0]])



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
result = np.append(np.array([8, 500, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,241,233,233,250,237,276,247],
[259,0,274,251,262,253,259,243],
[267,226,0,221,280,258,237,259],
[267,249,279,0,267,263,286,264],
[250,238,220,233,0,222,229,249],
[263,247,242,237,278,0,240,247],
[224,241,263,214,271,260,0,236],
[253,257,241,236,251,253,264,0]])



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
result = np.append(np.array([8, 500, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,255,259,246,257,241,231,249],
[245,0,250,226,249,251,233,246],
[241,250,0,226,248,241,234,237],
[254,274,274,0,262,256,249,258],
[243,251,252,238,0,244,239,241],
[259,249,259,244,256,0,256,254],
[269,267,266,251,261,244,0,252],
[251,254,263,242,259,246,248,0]])



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
result = np.append(np.array([8, 500, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,246,255,237,258,242,254],
[248,0,248,247,260,242,245,256],
[254,252,0,252,241,256,242,254],
[245,253,248,0,243,246,241,263],
[263,240,259,257,0,255,258,260],
[242,258,244,254,245,0,245,262],
[258,255,258,259,242,255,0,257],
[246,244,246,237,240,238,243,0]])



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
result = np.append(np.array([8, 500, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,268,249,240,268,262,280],
[263,0,252,230,266,251,264,253],
[232,248,0,249,243,277,255,235],
[251,270,251,0,239,258,245,258],
[260,234,257,261,0,260,256,257],
[232,249,223,242,240,0,247,241],
[238,236,245,255,244,253,0,247],
[220,247,265,242,243,259,253,0]])



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
result = np.append(np.array([8, 500, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,243,250,236,256,254,243,243],
[257,0,233,247,262,257,253,254],
[250,267,0,266,248,253,250,239],
[264,253,234,0,266,255,259,260],
[244,238,252,234,0,259,247,244],
[246,243,247,245,241,0,254,245],
[257,247,250,241,253,246,0,240],
[257,246,261,240,256,255,260,0]])



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
result = np.append(np.array([8, 500, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,242,259,259,234,248,237,250],
[258,0,260,244,245,264,264,251],
[241,240,0,260,250,234,236,245],
[241,256,240,0,237,236,232,239],
[266,255,250,263,0,250,265,255],
[252,236,266,264,250,0,241,247],
[263,236,264,268,235,259,0,248],
[250,249,255,261,245,253,252,0]])



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
result = np.append(np.array([8, 500, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,268,262,253,266,248,282,255],
[232,0,235,238,263,240,266,252],
[238,265,0,264,282,253,280,229],
[247,262,236,0,271,260,284,243],
[234,237,218,229,0,230,246,232],
[252,260,247,240,270,0,275,246],
[218,234,220,216,254,225,0,230],
[245,248,271,257,268,254,270,0]])



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
result = np.append(np.array([8, 500, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,254,174,293,209,277,256],
[237,0,250,211,317,162,264,242],
[246,250,0,201,253,248,276,278],
[326,289,299,0,323,244,229,276],
[207,183,247,177,0,127,245,181],
[291,338,252,256,373,0,287,237],
[223,236,224,271,255,213,0,221],
[244,258,222,224,319,263,279,0]])



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
result = np.append(np.array([8, 500, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,286,305,355,315,251,267,219],
[214,0,274,274,315,244,264,282],
[195,226,0,249,301,209,250,252],
[145,226,251,0,249,180,231,228],
[185,185,199,251,0,162,223,214],
[249,256,291,320,338,0,296,305],
[233,236,250,269,277,204,0,279],
[281,218,248,272,286,195,221,0]])



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
result = np.append(np.array([8, 500, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,243,263,275,252,262,271],
[253,0,256,222,255,229,264,275],
[257,244,0,229,271,245,229,254],
[237,278,271,0,268,271,262,282],
[225,245,229,232,0,220,233,222],
[248,271,255,229,280,0,276,246],
[238,236,271,238,267,224,0,236],
[229,225,246,218,278,254,264,0]])



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
result = np.append(np.array([8, 500, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,239,250,227,237,247,242,239],
[261,0,252,238,255,257,239,245],
[250,248,0,224,237,249,244,235],
[273,262,276,0,249,254,250,259],
[263,245,263,251,0,266,258,252],
[253,243,251,246,234,0,246,259],
[258,261,256,250,242,254,0,240],
[261,255,265,241,248,241,260,0]])



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
result = np.append(np.array([8, 500, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,254,245,246,251,258,260,242],
[246,0,233,255,241,241,251,249],
[255,267,0,263,254,248,260,241],
[254,245,237,0,235,238,239,244],
[249,259,246,265,0,264,259,252],
[242,259,252,262,236,0,257,234],
[240,249,240,261,241,243,0,236],
[258,251,259,256,248,266,264,0]])



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
result = np.append(np.array([8, 500, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,269,248,280,260,252,240,287],
[231,0,244,270,262,263,263,258],
[252,256,0,302,236,244,261,265],
[220,230,198,0,235,230,255,240],
[240,238,264,265,0,237,251,268],
[248,237,256,270,263,0,274,272],
[260,237,239,245,249,226,0,270],
[213,242,235,260,232,228,230,0]])



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
result = np.append(np.array([8, 500, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,256,239,250,245,232,255,263],
[244,0,244,263,235,247,239,255],
[261,256,0,244,262,254,253,267],
[250,237,256,0,241,252,246,268],
[255,265,238,259,0,247,257,265],
[268,253,246,248,253,0,238,266],
[245,261,247,254,243,262,0,266],
[237,245,233,232,235,234,234,0]])



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
result = np.append(np.array([8, 500, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,228,210,220,241,238,233],
[278,0,265,251,248,262,269,265],
[272,235,0,248,224,247,263,254],
[290,249,252,0,258,266,281,269],
[280,252,276,242,0,266,263,272],
[259,238,253,234,234,0,245,257],
[262,231,237,219,237,255,0,257],
[267,235,246,231,228,243,243,0]])



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
result = np.append(np.array([8, 500, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,248,241,234,248,269,261],
[240,0,235,240,237,249,247,253],
[252,265,0,255,244,256,261,275],
[259,260,245,0,252,281,266,271],
[266,263,256,248,0,263,260,274],
[252,251,244,219,237,0,230,246],
[231,253,239,234,240,270,0,260],
[239,247,225,229,226,254,240,0]])



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
result = np.append(np.array([8, 500, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,248,250,257,244,251,254,254],
[252,0,248,271,263,261,247,258],
[250,252,0,263,256,266,269,258],
[243,229,237,0,246,251,242,245],
[256,237,244,254,0,249,242,230],
[249,239,234,249,251,0,245,241],
[246,253,231,258,258,255,0,235],
[246,242,242,255,270,259,265,0]])



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
result = np.append(np.array([8, 500, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,274,278,237,251,260,249,263],
[226,0,240,225,245,254,242,210],
[222,260,0,227,234,252,241,229],
[263,275,273,0,247,261,297,266],
[249,255,266,253,0,256,262,232],
[240,246,248,239,244,0,246,242],
[251,258,259,203,238,254,0,252],
[237,290,271,234,268,258,248,0]])



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
result = np.append(np.array([8, 500, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,230,261,273,273,246,261],
[242,0,252,270,275,269,234,248],
[270,248,0,276,280,276,250,279],
[239,230,224,0,264,294,243,255],
[227,225,220,236,0,249,228,239],
[227,231,224,206,251,0,234,236],
[254,266,250,257,272,266,0,239],
[239,252,221,245,261,264,261,0]])



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
result = np.append(np.array([8, 500, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,296,251,242,246,277,286,283],
[204,0,229,223,224,258,226,239],
[249,271,0,251,268,251,282,252],
[258,277,249,0,249,276,245,255],
[254,276,232,251,0,248,270,274],
[223,242,249,224,252,0,273,239],
[214,274,218,255,230,227,0,258],
[217,261,248,245,226,261,242,0]])



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
result = np.append(np.array([8, 500, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,219,225,247,234,238,236,231],
[281,0,259,260,262,250,246,261],
[275,241,0,253,253,250,259,249],
[253,240,247,0,258,254,248,258],
[266,238,247,242,0,243,256,238],
[262,250,250,246,257,0,254,252],
[264,254,241,252,244,246,0,254],
[269,239,251,242,262,248,246,0]])



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
result = np.append(np.array([8, 500, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,253,203,313,271,233,250],
[243,0,239,232,294,244,184,264],
[247,261,0,180,189,215,158,238],
[297,268,320,0,196,278,244,268],
[187,206,311,304,0,339,270,222],
[229,256,285,222,161,0,229,245],
[267,316,342,256,230,271,0,238],
[250,236,262,232,278,255,262,0]])



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
result = np.append(np.array([8, 500, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,237,239,228,271,278,248,230],
[263,0,252,227,281,256,234,246],
[261,248,0,235,279,258,263,260],
[272,273,265,0,297,257,263,246],
[229,219,221,203,0,248,223,221],
[222,244,242,243,252,0,237,214],
[252,266,237,237,277,263,0,246],
[270,254,240,254,279,286,254,0]])



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
result = np.append(np.array([8, 500, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,270,253,270,250,273,243,257],
[230,0,229,230,255,252,238,248],
[247,271,0,267,257,263,248,265],
[230,270,233,0,236,230,247,247],
[250,245,243,264,0,231,247,253],
[227,248,237,270,269,0,231,271],
[257,262,252,253,253,269,0,242],
[243,252,235,253,247,229,258,0]])



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
result = np.append(np.array([8, 500, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,263,245,247,245,256,260,258],
[237,0,223,265,250,249,257,240],
[255,277,0,257,247,255,239,254],
[253,235,243,0,239,245,237,240],
[255,250,253,261,0,258,255,248],
[244,251,245,255,242,0,245,255],
[240,243,261,263,245,255,0,250],
[242,260,246,260,252,245,250,0]])



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
result = np.append(np.array([8, 500, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,221,288,237,268,296,257,254],
[279,0,316,269,279,303,271,228],
[212,184,0,233,269,241,200,174],
[263,231,267,0,266,249,255,223],
[232,221,231,234,0,286,232,236],
[204,197,259,251,214,0,252,230],
[243,229,300,245,268,248,0,223],
[246,272,326,277,264,270,277,0]])



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
result = np.append(np.array([8, 500, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,235,260,287,256,249,265],
[255,0,238,264,277,262,249,264],
[265,262,0,270,286,274,250,271],
[240,236,230,0,252,231,229,251],
[213,223,214,248,0,240,224,241],
[244,238,226,269,260,0,232,254],
[251,251,250,271,276,268,0,255],
[235,236,229,249,259,246,245,0]])



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
result = np.append(np.array([8, 500, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,249,275,223,262,245,264,261],
[251,0,259,258,245,221,242,267],
[225,241,0,248,265,254,257,241],
[277,242,252,0,259,259,273,257],
[238,255,235,241,0,233,270,256],
[255,279,246,241,267,0,219,290],
[236,258,243,227,230,281,0,251],
[239,233,259,243,244,210,249,0]])



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
result = np.append(np.array([8, 500, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,258,241,225,252,244,251,237],
[242,0,245,219,246,228,238,230],
[259,255,0,246,250,241,249,240],
[275,281,254,0,267,245,261,251],
[248,254,250,233,0,227,245,242],
[256,272,259,255,273,0,239,251],
[249,262,251,239,255,261,0,250],
[263,270,260,249,258,249,250,0]])



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
result = np.append(np.array([8, 500, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,260,257,254,283,253,246,262],
[240,0,240,260,250,245,224,243],
[243,260,0,260,250,257,250,259],
[246,240,240,0,247,232,237,248],
[217,250,250,253,0,252,245,239],
[247,255,243,268,248,0,241,252],
[254,276,250,263,255,259,0,263],
[238,257,241,252,261,248,237,0]])



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
result = np.append(np.array([8, 500, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,250,262,199,213,200,191,241],
[250,0,271,201,199,240,280,229],
[238,229,0,178,241,263,249,231],
[301,299,322,0,238,276,259,256],
[287,301,259,262,0,313,229,277],
[300,260,237,224,187,0,242,261],
[309,220,251,241,271,258,0,298],
[259,271,269,244,223,239,202,0]])



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
result = np.append(np.array([8, 500, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,297,268,261,277,251,251,236],
[203,0,221,223,224,214,230,211],
[232,279,0,253,267,239,255,253],
[239,277,247,0,252,227,262,212],
[223,276,233,248,0,234,231,228],
[249,286,261,273,266,0,269,240],
[249,270,245,238,269,231,0,234],
[264,289,247,288,272,260,266,0]])



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
result = np.append(np.array([8, 500, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,248,250,258,248,250,236],
[253,0,234,247,249,243,252,258],
[252,266,0,246,262,252,256,250],
[250,253,254,0,272,253,237,237],
[242,251,238,228,0,232,246,238],
[252,257,248,247,268,0,261,238],
[250,248,244,263,254,239,0,229],
[264,242,250,263,262,262,271,0]])



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
result = np.append(np.array([8, 500, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,286,223,203,214,192,259,213],
[214,0,188,250,145,209,222,196],
[277,312,0,234,234,237,273,285],
[297,250,266,0,283,216,260,266],
[286,355,266,217,0,267,236,210],
[308,291,263,284,233,0,316,292],
[241,278,227,240,264,184,0,238],
[287,304,215,234,290,208,262,0]])



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
result = np.append(np.array([8, 500, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,284,267,264,264,244,242],
[253,0,267,252,271,243,242,240],
[216,233,0,215,223,216,199,208],
[233,248,285,0,267,248,269,226],
[236,229,277,233,0,246,234,248],
[236,257,284,252,254,0,242,238],
[256,258,301,231,266,258,0,261],
[258,260,292,274,252,262,239,0]])



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
result = np.append(np.array([8, 500, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,253,262,247,251,249,252,244],
[247,0,264,250,256,250,249,238],
[238,236,0,254,248,239,237,245],
[253,250,246,0,236,230,246,238],
[249,244,252,264,0,248,249,241],
[251,250,261,270,252,0,232,255],
[248,251,263,254,251,268,0,259],
[256,262,255,262,259,245,241,0]])



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
result = np.append(np.array([8, 500, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,252,245,261,244,264,251,272],
[248,0,259,266,254,252,268,274],
[255,241,0,246,237,245,248,254],
[239,234,254,0,240,235,230,266],
[256,246,263,260,0,249,250,267],
[236,248,255,265,251,0,238,241],
[249,232,252,270,250,262,0,266],
[228,226,246,234,233,259,234,0]])



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
result = np.append(np.array([8, 500, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,245,262,249,248,248,237,245],
[255,0,238,255,251,245,245,262],
[238,262,0,256,246,260,246,255],
[251,245,244,0,238,238,239,248],
[252,249,254,262,0,255,260,256],
[252,255,240,262,245,0,240,275],
[263,255,254,261,240,260,0,259],
[255,238,245,252,244,225,241,0]])



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
result = np.append(np.array([8, 500, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,247,255,254,242,257,253,268],
[253,0,239,248,243,256,232,261],
[245,261,0,256,242,265,233,266],
[246,252,244,0,239,259,234,259],
[258,257,258,261,0,259,239,282],
[243,244,235,241,241,0,237,266],
[247,268,267,266,261,263,0,266],
[232,239,234,241,218,234,234,0]])



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
result = np.append(np.array([8, 500, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,195,233,200,220,216,211,211],
[305,0,252,292,236,262,277,229],
[267,248,0,247,227,264,265,240],
[300,208,253,0,216,236,225,224],
[280,264,273,284,0,245,240,253],
[284,238,236,264,255,0,209,224],
[289,223,235,275,260,291,0,231],
[289,271,260,276,247,276,269,0]])



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
result = np.append(np.array([8, 500, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,264,245,248,249,261,282,252],
[236,0,231,244,244,245,255,242],
[255,269,0,252,237,245,266,254],
[252,256,248,0,251,252,266,256],
[251,256,263,249,0,256,245,246],
[239,255,255,248,244,0,265,241],
[218,245,234,234,255,235,0,236],
[248,258,246,244,254,259,264,0]])



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
result = np.append(np.array([8, 500, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,257,238,265,249,257,255,257],
[243,0,250,269,268,257,257,262],
[262,250,0,271,245,243,263,264],
[235,231,229,0,247,241,236,243],
[251,232,255,253,0,223,240,230],
[243,243,257,259,277,0,244,268],
[245,243,237,264,260,256,0,246],
[243,238,236,257,270,232,254,0]])



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
result = np.append(np.array([8, 500, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,222,272,270,244,248,219,238],
[278,0,280,268,290,245,257,258],
[228,220,0,243,246,228,253,228],
[230,232,257,0,234,232,236,243],
[256,210,254,266,0,233,221,245],
[252,255,272,268,267,0,243,262],
[281,243,247,264,279,257,0,251],
[262,242,272,257,255,238,249,0]])



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
result = np.append(np.array([8, 500, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_8_500.csv", index=False, header=False)