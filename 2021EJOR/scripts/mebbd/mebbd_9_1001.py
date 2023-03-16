
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,487,489,502,489,498,507,518,506],
[514,0,471,485,509,510,511,528,440],
[512,530,0,530,519,529,524,535,451],
[499,516,471,0,513,552,493,525,474],
[512,492,482,488,0,527,476,544,484],
[503,491,472,449,474,0,485,513,444],
[494,490,477,508,525,516,0,503,478],
[483,473,466,476,457,488,498,0,450],
[495,561,550,527,517,557,523,551,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,530,484,495,502,531,520,517],
[483,0,462,489,474,497,494,508,510],
[471,539,0,506,478,507,536,502,475],
[517,512,495,0,501,490,509,523,511],
[506,527,523,500,0,517,481,490,559],
[499,504,494,511,484,0,533,501,512],
[470,507,465,492,520,468,0,487,523],
[481,493,499,478,511,500,514,0,505],
[484,491,526,490,442,489,478,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,466,471,464,507,471,448,531],
[535,0,547,516,494,576,561,498,511],
[535,454,0,474,504,586,530,457,518],
[530,485,527,0,479,540,523,525,498],
[537,507,497,522,0,545,545,481,529],
[494,425,415,461,456,0,466,434,473],
[530,440,471,478,456,535,0,472,512],
[553,503,544,476,520,567,529,0,539],
[470,490,483,503,472,528,489,462,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,507,485,510,489,498,489,491],
[505,0,493,477,510,490,479,506,481],
[494,508,0,486,494,480,478,482,491],
[516,524,515,0,528,492,495,511,497],
[491,491,507,473,0,487,471,498,491],
[512,511,521,509,514,0,498,515,500],
[503,522,523,506,530,503,0,496,494],
[512,495,519,490,503,486,505,0,516],
[510,520,510,504,510,501,507,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,480,490,488,517,476,504,464],
[505,0,458,487,446,508,487,470,465],
[521,543,0,504,471,483,510,486,465],
[511,514,497,0,511,510,506,520,483],
[513,555,530,490,0,516,500,498,503],
[484,493,518,491,485,0,489,507,488],
[525,514,491,495,501,512,0,518,499],
[497,531,515,481,503,494,483,0,485],
[537,536,536,518,498,513,502,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,445,443,454,512,449,477,526,471],
[556,0,466,487,538,461,536,540,520],
[558,535,0,505,538,520,558,560,487],
[547,514,496,0,539,491,507,545,496],
[489,463,463,462,0,451,496,472,471],
[552,540,481,510,550,0,541,534,497],
[524,465,443,494,505,460,0,516,441],
[475,461,441,456,529,467,485,0,491],
[530,481,514,505,530,504,560,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,446,485,467,425,462,449,484],
[540,0,522,511,519,482,538,498,538],
[555,479,0,491,500,492,519,504,536],
[516,490,510,0,495,509,510,460,527],
[534,482,501,506,0,479,510,462,500],
[576,519,509,492,522,0,545,491,523],
[539,463,482,491,491,456,0,462,503],
[552,503,497,541,539,510,539,0,527],
[517,463,465,474,501,478,498,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,506,508,511,499,501,483,518],
[504,0,491,507,510,507,501,489,522],
[495,510,0,504,517,516,501,504,500],
[493,494,497,0,502,505,494,491,508],
[490,491,484,499,0,490,481,489,514],
[502,494,485,496,511,0,508,482,511],
[500,500,500,507,520,493,0,489,498],
[518,512,497,510,512,519,512,0,494],
[483,479,501,493,487,490,503,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,497,507,504,438,494,473,458],
[514,0,528,475,526,482,512,502,494],
[504,473,0,478,495,481,497,425,460],
[494,526,523,0,511,502,513,480,506],
[497,475,506,490,0,471,501,484,467],
[563,519,520,499,530,0,483,492,525],
[507,489,504,488,500,518,0,489,461],
[528,499,576,521,517,509,512,0,474],
[543,507,541,495,534,476,540,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,481,480,492,495,473,478,471],
[519,0,515,510,500,501,489,487,502],
[520,486,0,503,507,513,485,508,498],
[521,491,498,0,513,480,488,505,490],
[509,501,494,488,0,491,477,496,490],
[506,500,488,521,510,0,487,499,491],
[528,512,516,513,524,514,0,501,498],
[523,514,493,496,505,502,500,0,500],
[530,499,503,511,511,510,503,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,519,501,474,482,501,533,525],
[474,0,487,495,409,467,474,528,478],
[482,514,0,480,487,492,487,526,530],
[500,506,521,0,504,509,515,549,524],
[527,592,514,497,0,505,544,573,518],
[519,534,509,492,496,0,515,537,547],
[500,527,514,486,457,486,0,511,488],
[468,473,475,452,428,464,490,0,479],
[476,523,471,477,483,454,513,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,499,498,494,508,511,512,476],
[489,0,504,509,507,501,501,519,489],
[502,497,0,518,488,497,497,485,471],
[503,492,483,0,465,503,490,484,491],
[507,494,513,536,0,514,526,519,511],
[493,500,504,498,487,0,515,488,497],
[490,500,504,511,475,486,0,502,498],
[489,482,516,517,482,513,499,0,458],
[525,512,530,510,490,504,503,543,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,480,487,474,494,492,469,481],
[513,0,514,495,497,500,500,495,486],
[521,487,0,491,473,488,500,473,491],
[514,506,510,0,483,500,518,472,497],
[527,504,528,518,0,503,515,486,492],
[507,501,513,501,498,0,522,505,496],
[509,501,501,483,486,479,0,482,496],
[532,506,528,529,515,496,519,0,507],
[520,515,510,504,509,505,505,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,494,536,520,519,516,517,560],
[476,0,518,505,492,500,486,480,540],
[507,483,0,544,502,500,506,506,532],
[465,496,457,0,510,490,483,486,521],
[481,509,499,491,0,493,504,491,533],
[482,501,501,511,508,0,502,523,520],
[485,515,495,518,497,499,0,500,548],
[484,521,495,515,510,478,501,0,513],
[441,461,469,480,468,481,453,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,441,571,502,467,513,530,508,484],
[560,0,526,495,478,541,511,527,512],
[430,475,0,477,526,489,563,496,511],
[499,506,524,0,470,443,447,464,503],
[534,523,475,531,0,507,533,588,468],
[488,460,512,558,494,0,484,512,492],
[471,490,438,554,468,517,0,517,510],
[493,474,505,537,413,489,484,0,483],
[517,489,490,498,533,509,491,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,581,604,631,548,570,467,549,655],
[420,0,476,525,461,496,392,449,567],
[397,525,0,525,465,535,469,528,631],
[370,476,476,0,452,495,398,447,502],
[453,540,536,549,0,558,491,511,589],
[431,505,466,506,443,0,346,461,516],
[534,609,532,603,510,655,0,481,660],
[452,552,473,554,490,540,520,0,594],
[346,434,370,499,412,485,341,407,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,482,429,533,518,507,477,500],
[493,0,531,476,489,475,523,507,459],
[519,470,0,503,499,502,525,531,522],
[572,525,498,0,547,522,562,482,581],
[468,512,502,454,0,489,543,464,525],
[483,526,499,479,512,0,538,554,491],
[494,478,476,439,458,463,0,462,495],
[524,494,470,519,537,447,539,0,496],
[501,542,479,420,476,510,506,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,478,492,514,491,475,508,491],
[499,0,480,501,521,477,508,508,484],
[523,521,0,510,530,504,494,508,515],
[509,500,491,0,514,495,492,498,509],
[487,480,471,487,0,455,485,491,464],
[510,524,497,506,546,0,511,516,502],
[526,493,507,509,516,490,0,528,492],
[493,493,493,503,510,485,473,0,475],
[510,517,486,492,537,499,509,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,526,501,548,552,471,539,533],
[543,0,564,478,545,543,496,550,563],
[475,437,0,432,515,505,430,521,481],
[500,523,569,0,519,518,519,558,551],
[453,456,486,482,0,479,415,479,497],
[449,458,496,483,522,0,446,515,512],
[530,505,571,482,586,555,0,563,530],
[462,451,480,443,522,486,438,0,443],
[468,438,520,450,504,489,471,558,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,505,503,483,499,460,500,483],
[515,0,518,537,515,484,523,515,509],
[496,483,0,498,510,475,482,500,492],
[498,464,503,0,506,484,485,511,466],
[518,486,491,495,0,520,474,483,488],
[502,517,526,517,481,0,499,497,491],
[541,478,519,516,527,502,0,503,511],
[501,486,501,490,518,504,498,0,484],
[518,492,509,535,513,510,490,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,519,518,496,562,522,504,551],
[465,0,494,512,475,514,487,484,502],
[482,507,0,482,475,514,500,463,513],
[483,489,519,0,476,512,504,452,537],
[505,526,526,525,0,542,520,453,531],
[439,487,487,489,459,0,475,448,509],
[479,514,501,497,481,526,0,470,513],
[497,517,538,549,548,553,531,0,548],
[450,499,488,464,470,492,488,453,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,384,576,591,486,519,392,567,432],
[617,0,589,598,535,639,471,444,603],
[425,412,0,458,537,529,419,514,418],
[410,403,543,0,400,410,302,404,368],
[515,466,464,601,0,482,460,550,456],
[482,362,472,591,519,0,488,444,273],
[609,530,582,699,541,513,0,711,434],
[434,557,487,597,451,557,290,0,423],
[569,398,583,633,545,728,567,578,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,501,492,464,492,476,512,499],
[498,0,459,516,510,543,494,531,504],
[500,542,0,503,525,528,493,527,498],
[509,485,498,0,523,502,487,506,494],
[537,491,476,478,0,477,528,514,521],
[509,458,473,499,524,0,488,521,520],
[525,507,508,514,473,513,0,516,514],
[489,470,474,495,487,480,485,0,474],
[502,497,503,507,480,481,487,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,502,497,570,501,491,505,512],
[517,0,533,474,558,507,485,494,529],
[499,468,0,496,572,517,493,478,465],
[504,527,505,0,570,498,467,493,517],
[431,443,429,431,0,493,447,449,440],
[500,494,484,503,508,0,452,477,514],
[510,516,508,534,554,549,0,534,480],
[496,507,523,508,552,524,467,0,526],
[489,472,536,484,561,487,521,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,430,487,468,461,444,443,469],
[503,0,476,550,525,518,488,480,523],
[571,525,0,555,512,521,459,509,570],
[514,451,446,0,477,488,454,438,482],
[533,476,489,524,0,495,483,521,518],
[540,483,480,513,506,0,513,460,512],
[557,513,542,547,518,488,0,455,483],
[558,521,492,563,480,541,546,0,540],
[532,478,431,519,483,489,518,461,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,509,512,496,522,501,488,485],
[506,0,493,554,484,505,518,521,464],
[492,508,0,528,465,527,493,566,529],
[489,447,473,0,438,510,463,530,492],
[505,517,536,563,0,503,486,567,577],
[479,496,474,491,498,0,454,493,436],
[500,483,508,538,515,547,0,541,501],
[513,480,435,471,434,508,460,0,499],
[516,537,472,509,424,565,500,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,488,490,517,473,493,508,510],
[476,0,495,498,496,491,459,504,527],
[513,506,0,487,496,496,493,515,527],
[511,503,514,0,533,508,510,494,513],
[484,505,505,468,0,487,483,489,507],
[528,510,505,493,514,0,485,518,499],
[508,542,508,491,518,516,0,510,529],
[493,497,486,507,512,483,491,0,496],
[491,474,474,488,494,502,472,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,514,501,522,554,512,526,481],
[465,0,490,508,540,513,511,525,508],
[487,511,0,494,518,540,530,550,563],
[500,493,507,0,505,542,509,528,521],
[479,461,483,496,0,553,557,549,509],
[447,488,461,459,448,0,463,526,471],
[489,490,471,492,444,538,0,514,529],
[475,476,451,473,452,475,487,0,466],
[520,493,438,480,492,530,472,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,527,473,480,527,463,496,453],
[507,0,520,498,510,515,450,508,504],
[474,481,0,474,490,447,498,507,485],
[528,503,527,0,538,515,493,569,472],
[521,491,511,463,0,472,468,512,448],
[474,486,554,486,529,0,504,484,494],
[538,551,503,508,533,497,0,508,514],
[505,493,494,432,489,517,493,0,486],
[548,497,516,529,553,507,487,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,513,507,503,497,508,514,511],
[471,0,489,483,488,479,480,506,498],
[488,512,0,525,513,492,499,519,491],
[494,518,476,0,482,493,494,508,508],
[498,513,488,519,0,477,488,502,485],
[504,522,509,508,524,0,497,503,515],
[493,521,502,507,513,504,0,496,519],
[487,495,482,493,499,498,505,0,505],
[490,503,510,493,516,486,482,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,496,491,505,502,503,509,484],
[517,0,512,509,494,509,515,520,514],
[505,489,0,498,502,492,508,516,496],
[510,492,503,0,475,481,493,507,505],
[496,507,499,526,0,487,509,530,508],
[499,492,509,520,514,0,488,516,482],
[498,486,493,508,492,513,0,518,504],
[492,481,485,494,471,485,483,0,476],
[517,487,505,496,493,519,497,525,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,512,507,474,481,504,480,471],
[499,0,499,511,515,489,496,495,482],
[489,502,0,529,500,474,503,495,486],
[494,490,472,0,504,462,492,477,477],
[527,486,501,497,0,493,496,477,470],
[520,512,527,539,508,0,531,514,496],
[497,505,498,509,505,470,0,475,497],
[521,506,506,524,524,487,526,0,503],
[530,519,515,524,531,505,504,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,436,557,350,457,446,528,401],
[542,0,376,587,427,503,432,530,446],
[565,625,0,547,524,569,559,637,390],
[444,414,454,0,434,426,365,556,333],
[651,574,477,567,0,458,719,590,500],
[544,498,432,575,543,0,456,459,379],
[555,569,442,636,282,545,0,557,477],
[473,471,364,445,411,542,444,0,565],
[600,555,611,668,501,622,524,436,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,526,529,520,559,508,497,491],
[518,0,475,548,512,538,489,488,492],
[475,526,0,532,527,499,469,502,464],
[472,453,469,0,470,474,453,488,462],
[481,489,474,531,0,497,471,479,503],
[442,463,502,527,504,0,479,491,473],
[493,512,532,548,530,522,0,526,491],
[504,513,499,513,522,510,475,0,498],
[510,509,537,539,498,528,510,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,556,509,541,511,534,492,515,506],
[445,0,500,486,498,511,478,518,512],
[492,501,0,522,486,491,483,532,488],
[460,515,479,0,489,508,506,494,512],
[490,503,515,512,0,506,490,530,507],
[467,490,510,493,495,0,498,499,485],
[509,523,518,495,511,503,0,556,501],
[486,483,469,507,471,502,445,0,455],
[495,489,513,489,494,516,500,546,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,482,466,546,495,506,503,503],
[524,0,519,489,518,520,523,537,503],
[519,482,0,502,538,536,519,522,535],
[535,512,499,0,538,523,491,513,527],
[455,483,463,463,0,473,484,487,492],
[506,481,465,478,528,0,493,526,516],
[495,478,482,510,517,508,0,494,528],
[498,464,479,488,514,475,507,0,512],
[498,498,466,474,509,485,473,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,514,472,489,445,493,526,504],
[498,0,555,496,539,480,493,510,498],
[487,446,0,482,507,508,486,490,542],
[529,505,519,0,539,536,493,543,553],
[512,462,494,462,0,476,490,505,481],
[556,521,493,465,525,0,513,475,511],
[508,508,515,508,511,488,0,481,537],
[475,491,511,458,496,526,520,0,511],
[497,503,459,448,520,490,464,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,492,515,486,479,480,495,482],
[506,0,514,556,490,465,525,481,510],
[509,487,0,519,505,488,493,556,490],
[486,445,482,0,511,473,456,519,515],
[515,511,496,490,0,441,514,496,480],
[522,536,513,528,560,0,495,553,548],
[521,476,508,545,487,506,0,520,488],
[506,520,445,482,505,448,481,0,473],
[519,491,511,486,521,453,513,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,484,540,510,564,517,546,545],
[481,0,541,562,474,549,549,543,525],
[517,460,0,553,464,553,508,517,514],
[461,439,448,0,441,514,484,490,502],
[491,527,537,560,0,549,523,551,601],
[437,452,448,487,452,0,469,507,510],
[484,452,493,517,478,532,0,532,501],
[455,458,484,511,450,494,469,0,543],
[456,476,487,499,400,491,500,458,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,552,527,513,523,506,500,540],
[511,0,535,529,498,528,494,534,529],
[449,466,0,476,488,486,486,502,492],
[474,472,525,0,492,501,485,508,514],
[488,503,513,509,0,508,484,517,529],
[478,473,515,500,493,0,491,531,503],
[495,507,515,516,517,510,0,541,530],
[501,467,499,493,484,470,460,0,492],
[461,472,509,487,472,498,471,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,438,457,477,490,488,457,541,488],
[563,0,493,476,556,493,522,531,552],
[544,508,0,508,530,512,495,514,509],
[524,525,493,0,482,506,448,552,476],
[511,445,471,519,0,444,449,523,480],
[513,508,489,495,557,0,507,548,496],
[544,479,506,553,552,494,0,536,522],
[460,470,487,449,478,453,465,0,462],
[513,449,492,525,521,505,479,539,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,513,468,481,468,498,499,486],
[516,0,516,531,506,485,500,497,543],
[488,485,0,480,496,471,450,485,503],
[533,470,521,0,520,486,492,487,541],
[520,495,505,481,0,494,497,480,516],
[533,516,530,515,507,0,513,489,539],
[503,501,551,509,504,488,0,511,537],
[502,504,516,514,521,512,490,0,529],
[515,458,498,460,485,462,464,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,519,520,495,496,523,520,508],
[486,0,502,532,509,499,489,513,519],
[482,499,0,479,505,501,485,474,502],
[481,469,522,0,496,491,503,495,500],
[506,492,496,505,0,517,490,492,507],
[505,502,500,510,484,0,498,511,512],
[478,512,516,498,511,503,0,511,498],
[481,488,527,506,509,490,490,0,504],
[493,482,499,501,494,489,503,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,517,516,531,490,546,516,511],
[506,0,519,517,494,519,527,515,512],
[484,482,0,524,482,478,504,494,492],
[485,484,477,0,486,468,487,500,499],
[470,507,519,515,0,501,522,517,503],
[511,482,523,533,500,0,548,500,502],
[455,474,497,514,479,453,0,504,479],
[485,486,507,501,484,501,497,0,509],
[490,489,509,502,498,499,522,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,487,445,525,498,537,491,501],
[512,0,496,491,549,503,543,511,510],
[514,505,0,470,532,516,540,518,508],
[556,510,531,0,548,519,518,537,485],
[476,452,469,453,0,503,473,454,455],
[503,498,485,482,498,0,538,510,475],
[464,458,461,483,528,463,0,507,480],
[510,490,483,464,547,491,494,0,473],
[500,491,493,516,546,526,521,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,506,446,481,493,475,525,455],
[510,0,529,487,566,515,532,462,518],
[495,472,0,496,517,529,509,499,448],
[555,514,505,0,537,506,533,472,481],
[520,435,484,464,0,428,481,449,478],
[508,486,472,495,573,0,494,482,482],
[526,469,492,468,520,507,0,444,455],
[476,539,502,529,552,519,557,0,510],
[546,483,553,520,523,519,546,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,472,494,507,505,465,516,486],
[492,0,477,498,524,479,480,519,448],
[529,524,0,503,536,551,477,542,483],
[507,503,498,0,524,504,471,488,506],
[494,477,465,477,0,503,469,520,487],
[496,522,450,497,498,0,492,489,449],
[536,521,524,530,532,509,0,536,480],
[485,482,459,513,481,512,465,0,447],
[515,553,518,495,514,552,521,554,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,501,529,490,557,554,566,520],
[542,0,525,473,515,511,563,555,592],
[500,476,0,523,483,483,530,526,575],
[472,528,478,0,525,476,557,501,550],
[511,486,518,476,0,521,561,468,565],
[444,490,518,525,480,0,522,574,559],
[447,438,471,444,440,479,0,512,511],
[435,446,475,500,533,427,489,0,520],
[481,409,426,451,436,442,490,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,517,457,517,504,486,492,517],
[477,0,462,469,513,475,471,503,491],
[484,539,0,529,532,492,496,517,524],
[544,532,472,0,527,492,509,546,530],
[484,488,469,474,0,457,494,504,475],
[497,526,509,509,544,0,546,495,517],
[515,530,505,492,507,455,0,492,446],
[509,498,484,455,497,506,509,0,514],
[484,510,477,471,526,484,555,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,496,521,494,525,495,535,529],
[505,0,509,474,497,503,525,507,477],
[505,492,0,480,512,529,513,522,506],
[480,527,521,0,530,562,532,555,529],
[507,504,489,471,0,496,520,554,495],
[476,498,472,439,505,0,467,498,489],
[506,476,488,469,481,534,0,519,492],
[466,494,479,446,447,503,482,0,469],
[472,524,495,472,506,512,509,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,518,491,491,507,489,494,517],
[519,0,519,494,512,527,494,500,490],
[483,482,0,478,493,515,483,484,489],
[510,507,523,0,510,527,503,495,509],
[510,489,508,491,0,507,505,491,491],
[494,474,486,474,494,0,461,472,496],
[512,507,518,498,496,540,0,480,504],
[507,501,517,506,510,529,521,0,483],
[484,511,512,492,510,505,497,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,491,515,503,510,490,497,510],
[521,0,515,510,495,518,491,497,522],
[510,486,0,514,483,517,505,501,490],
[486,491,487,0,505,512,493,488,500],
[498,506,518,496,0,512,500,494,476],
[491,483,484,489,489,0,502,482,468],
[511,510,496,508,501,499,0,480,489],
[504,504,500,513,507,519,521,0,502],
[491,479,511,501,525,533,512,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,496,499,488,512,488,521,514],
[519,0,503,463,480,505,442,456,504],
[505,498,0,487,506,499,470,503,484],
[502,538,514,0,472,556,525,512,536],
[513,521,495,529,0,526,471,500,507],
[489,496,502,445,475,0,434,479,469],
[513,559,531,476,530,567,0,523,520],
[480,545,498,489,501,522,478,0,494],
[487,497,517,465,494,532,481,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,479,425,489,445,470,567,546],
[517,0,485,412,425,461,457,572,555],
[522,516,0,495,514,537,560,552,551],
[576,589,506,0,540,555,488,529,575],
[512,576,487,461,0,520,506,562,550],
[556,540,464,446,481,0,503,509,521],
[531,544,441,513,495,498,0,545,536],
[434,429,449,472,439,492,456,0,495],
[455,446,450,426,451,480,465,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,493,505,481,494,515,496,507],
[482,0,505,492,486,486,484,464,484],
[508,496,0,492,494,500,506,504,503],
[496,509,509,0,463,502,501,493,504],
[520,515,507,538,0,490,536,487,510],
[507,515,501,499,511,0,487,472,504],
[486,517,495,500,465,514,0,506,498],
[505,537,497,508,514,529,495,0,535],
[494,517,498,497,491,497,503,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,512,521,524,527,486,574,528],
[477,0,480,497,506,519,451,530,503],
[489,521,0,525,505,523,509,510,524],
[480,504,476,0,502,517,487,511,495],
[477,495,496,499,0,498,496,527,496],
[474,482,478,484,503,0,485,528,475],
[515,550,492,514,505,516,0,535,504],
[427,471,491,490,474,473,466,0,510],
[473,498,477,506,505,526,497,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,637,498,640,438,534,599,688,643],
[364,0,447,602,389,525,458,280,503],
[503,554,0,581,549,648,442,560,465],
[361,399,420,0,405,488,333,405,476],
[563,612,452,596,0,537,537,487,460],
[467,476,353,513,464,0,478,370,526],
[402,543,559,668,464,523,0,497,479],
[313,721,441,596,514,631,504,0,587],
[358,498,536,525,541,475,522,414,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,516,541,545,487,511,563,473],
[508,0,532,531,527,503,522,536,481],
[485,469,0,524,505,489,520,539,513],
[460,470,477,0,512,486,478,532,491],
[456,474,496,489,0,490,493,508,476],
[514,498,512,515,511,0,526,547,490],
[490,479,481,523,508,475,0,557,484],
[438,465,462,469,493,454,444,0,457],
[528,520,488,510,525,511,517,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,500,488,506,507,485,506,511],
[512,0,526,477,506,495,517,525,515],
[501,475,0,492,514,488,497,508,494],
[513,524,509,0,505,481,502,506,485],
[495,495,487,496,0,459,485,499,491],
[494,506,513,520,542,0,505,497,527],
[516,484,504,499,516,496,0,516,503],
[495,476,493,495,502,504,485,0,510],
[490,486,507,516,510,474,498,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,471,472,463,484,507,509,538],
[511,0,485,512,533,532,515,540,515],
[530,516,0,490,554,527,540,549,503],
[529,489,511,0,522,536,502,530,499],
[538,468,447,479,0,514,465,492,476],
[517,469,474,465,487,0,483,493,492],
[494,486,461,499,536,518,0,489,463],
[492,461,452,471,509,508,512,0,474],
[463,486,498,502,525,509,538,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,439,464,481,499,519,482,476],
[488,0,399,443,464,532,364,467,433],
[562,602,0,516,495,544,460,530,508],
[537,558,485,0,523,559,549,471,540],
[520,537,506,478,0,558,479,538,489],
[502,469,457,442,443,0,443,506,466],
[482,637,541,452,522,558,0,506,521],
[519,534,471,530,463,495,495,0,498],
[525,568,493,461,512,535,480,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,445,478,497,484,484,504,500],
[511,0,490,486,502,497,501,500,494],
[556,511,0,519,544,508,499,502,522],
[523,515,482,0,510,524,515,507,525],
[504,499,457,491,0,505,489,504,496],
[517,504,493,477,496,0,489,490,513],
[517,500,502,486,512,512,0,507,501],
[497,501,499,494,497,511,494,0,526],
[501,507,479,476,505,488,500,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,603,538,529,502,522,500,467],
[490,0,537,529,479,531,462,466,516],
[398,464,0,534,414,449,426,376,424],
[463,472,467,0,467,513,496,371,466],
[472,522,587,534,0,523,524,484,515],
[499,470,552,488,478,0,485,447,460],
[479,539,575,505,477,516,0,535,475],
[501,535,625,630,517,554,466,0,566],
[534,485,577,535,486,541,526,435,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,493,443,515,517,511,508,499],
[496,0,422,432,473,497,472,431,421],
[508,579,0,486,562,549,538,500,532],
[558,569,515,0,574,570,533,556,484],
[486,528,439,427,0,521,486,494,482],
[484,504,452,431,480,0,480,467,451],
[490,529,463,468,515,521,0,511,492],
[493,570,501,445,507,534,490,0,467],
[502,580,469,517,519,550,509,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,493,493,486,511,506,510,504],
[493,0,495,505,497,492,502,515,490],
[508,506,0,499,497,489,507,480,503],
[508,496,502,0,498,504,522,489,496],
[515,504,504,503,0,485,520,487,521],
[490,509,512,497,516,0,531,501,499],
[495,499,494,479,481,470,0,476,476],
[491,486,521,512,514,500,525,0,505],
[497,511,498,505,480,502,525,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,578,532,520,487,510,512,520],
[523,0,545,505,486,509,511,511,451],
[423,456,0,488,487,481,489,479,492],
[469,496,513,0,492,457,530,450,519],
[481,515,514,509,0,502,494,491,501],
[514,492,520,544,499,0,535,468,466],
[491,490,512,471,507,466,0,501,448],
[489,490,522,551,510,533,500,0,530],
[481,550,509,482,500,535,553,471,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,498,523,504,483,487,501,510],
[494,0,514,533,497,503,498,502,500],
[503,487,0,509,504,488,487,492,484],
[478,468,492,0,491,490,491,489,473],
[497,504,497,510,0,495,482,487,490],
[518,498,513,511,506,0,505,509,511],
[514,503,514,510,519,496,0,503,481],
[500,499,509,512,514,492,498,0,504],
[491,501,517,528,511,490,520,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,540,515,525,501,526,510,500],
[493,0,519,508,501,516,478,495,486],
[461,482,0,496,500,500,480,480,483],
[486,493,505,0,495,489,492,496,491],
[476,500,501,506,0,494,506,490,498],
[500,485,501,512,507,0,516,500,510],
[475,523,521,509,495,485,0,488,496],
[491,506,521,505,511,501,513,0,513],
[501,515,518,510,503,491,505,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,496,509,507,482,518,513,536],
[510,0,495,491,506,505,499,535,513],
[505,506,0,504,515,495,523,523,522],
[492,510,497,0,482,500,513,515,517],
[494,495,486,519,0,481,508,504,522],
[519,496,506,501,520,0,521,522,505],
[483,502,478,488,493,480,0,531,525],
[488,466,478,486,497,479,470,0,512],
[465,488,479,484,479,496,476,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,495,497,489,516,497,502,472],
[508,0,484,482,470,508,491,506,490],
[506,517,0,503,508,510,503,521,491],
[504,519,498,0,503,496,510,525,507],
[512,531,493,498,0,521,502,530,488],
[485,493,491,505,480,0,490,511,475],
[504,510,498,491,499,511,0,517,490],
[499,495,480,476,471,490,484,0,480],
[529,511,510,494,513,526,511,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,500,500,490,494,527,517,501],
[508,0,506,506,485,489,551,491,500],
[501,495,0,463,483,471,517,507,507],
[501,495,538,0,474,475,520,495,509],
[511,516,518,527,0,507,553,499,493],
[507,512,530,526,494,0,526,507,506],
[474,450,484,481,448,475,0,477,475],
[484,510,494,506,502,494,524,0,493],
[500,501,494,492,508,495,526,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,500,458,495,516,464,491,480],
[529,0,503,496,517,505,485,498,500],
[501,498,0,485,491,470,496,502,496],
[543,505,516,0,512,498,488,500,474],
[506,484,510,489,0,471,469,506,471],
[485,496,531,503,530,0,501,509,499],
[537,516,505,513,532,500,0,538,529],
[510,503,499,501,495,492,463,0,490],
[521,501,505,527,530,502,472,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,472,472,478,461,512,471,478],
[530,0,506,514,519,503,539,540,497],
[529,495,0,506,501,513,536,519,505],
[529,487,495,0,523,542,559,527,528],
[523,482,500,478,0,460,518,510,477],
[540,498,488,459,541,0,549,533,479],
[489,462,465,442,483,452,0,507,458],
[530,461,482,474,491,468,494,0,488],
[523,504,496,473,524,522,543,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,498,505,506,503,518,501,493],
[494,0,502,499,474,509,507,503,479],
[503,499,0,504,510,524,524,512,493],
[496,502,497,0,501,512,526,494,505],
[495,527,491,500,0,520,534,506,489],
[498,492,477,489,481,0,523,513,471],
[483,494,477,475,467,478,0,488,472],
[500,498,489,507,495,488,513,0,482],
[508,522,508,496,512,530,529,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,515,480,475,502,483,506,509],
[507,0,515,485,513,491,514,525,520],
[486,486,0,477,494,522,484,499,499],
[521,516,524,0,497,516,532,516,521],
[526,488,507,504,0,503,508,539,497],
[499,510,479,485,498,0,504,498,489],
[518,487,517,469,493,497,0,502,509],
[495,476,502,485,462,503,499,0,517],
[492,481,502,480,504,512,492,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,488,485,479,509,500,494,513],
[522,0,492,507,498,519,516,522,523],
[513,509,0,514,492,506,506,516,508],
[516,494,487,0,501,524,507,505,523],
[522,503,509,500,0,528,512,508,536],
[492,482,495,477,473,0,476,501,493],
[501,485,495,494,489,525,0,498,514],
[507,479,485,496,493,500,503,0,498],
[488,478,493,478,465,508,487,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,503,499,519,518,514,522,492],
[502,0,488,500,542,510,514,495,486],
[498,513,0,494,506,553,443,511,506],
[502,501,507,0,539,517,496,524,509],
[482,459,495,462,0,493,485,498,494],
[483,491,448,484,508,0,463,496,481],
[487,487,558,505,516,538,0,494,479],
[479,506,490,477,503,505,507,0,455],
[509,515,495,492,507,520,522,546,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,489,488,450,471,488,480,501],
[526,0,481,490,448,507,466,470,516],
[512,520,0,509,514,491,534,472,536],
[513,511,492,0,487,508,494,478,485],
[551,553,487,514,0,514,596,521,480],
[530,494,510,493,487,0,511,495,520],
[513,535,467,507,405,490,0,460,533],
[521,531,529,523,480,506,541,0,497],
[500,485,465,516,521,481,468,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,437,554,443,438,416,449,462],
[521,0,442,570,514,492,457,479,446],
[564,559,0,572,514,557,460,544,569],
[447,431,429,0,438,371,436,444,453],
[558,487,487,563,0,467,522,543,555],
[563,509,444,630,534,0,457,487,575],
[585,544,541,565,479,544,0,504,574],
[552,522,457,557,458,514,497,0,517],
[539,555,432,548,446,426,427,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,468,531,503,475,506,508,503],
[495,0,471,517,498,512,500,517,504],
[533,530,0,550,509,499,523,545,517],
[470,484,451,0,467,503,517,492,483],
[498,503,492,534,0,483,503,514,549],
[526,489,502,498,518,0,506,512,513],
[495,501,478,484,498,495,0,509,497],
[493,484,456,509,487,489,492,0,494],
[498,497,484,518,452,488,504,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,569,413,490,446,410,367,336],
[526,0,389,398,393,483,469,614,452],
[432,612,0,461,483,610,437,600,449],
[588,603,540,0,397,437,422,548,308],
[511,608,518,604,0,482,386,609,537],
[555,518,391,564,519,0,490,514,408],
[591,532,564,579,615,511,0,426,370],
[634,387,401,453,392,487,575,0,362],
[665,549,552,693,464,593,631,639,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,469,470,482,494,469,482,496],
[528,0,514,481,485,505,501,481,494],
[532,487,0,493,506,478,471,519,477],
[531,520,508,0,500,521,499,529,511],
[519,516,495,501,0,519,475,502,523],
[507,496,523,480,482,0,471,470,485],
[532,500,530,502,526,530,0,526,528],
[519,520,482,472,499,531,475,0,500],
[505,507,524,490,478,516,473,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,502,502,504,529,464,474,480],
[505,0,508,506,509,485,481,493,487],
[499,493,0,520,505,522,491,502,503],
[499,495,481,0,524,543,502,500,516],
[497,492,496,477,0,500,481,488,501],
[472,516,479,458,501,0,455,488,473],
[537,520,510,499,520,546,0,507,513],
[527,508,499,501,513,513,494,0,473],
[521,514,498,485,500,528,488,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,446,451,500,495,463,474,458],
[527,0,477,468,531,515,513,480,503],
[555,524,0,502,548,523,548,499,527],
[550,533,499,0,528,542,529,532,525],
[501,470,453,473,0,488,472,454,470],
[506,486,478,459,513,0,505,503,511],
[538,488,453,472,529,496,0,507,489],
[527,521,502,469,547,498,494,0,520],
[543,498,474,476,531,490,512,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,501,507,505,502,510,498,488],
[526,0,497,502,497,524,511,494,486],
[500,504,0,505,497,520,529,499,500],
[494,499,496,0,494,520,486,490,502],
[496,504,504,507,0,485,517,504,487],
[499,477,481,481,516,0,497,499,495],
[491,490,472,515,484,504,0,485,487],
[503,507,502,511,497,502,516,0,494],
[513,515,501,499,514,506,514,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,508,517,502,497,514,510,514],
[493,0,506,500,502,506,520,499,497],
[493,495,0,517,515,493,526,516,520],
[484,501,484,0,498,478,506,506,495],
[499,499,486,503,0,497,509,491,515],
[504,495,508,523,504,0,530,516,503],
[487,481,475,495,492,471,0,468,480],
[491,502,485,495,510,485,533,0,499],
[487,504,481,506,486,498,521,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,504,488,464,516,460,494,501],
[531,0,513,516,479,593,515,580,579],
[497,488,0,462,470,533,474,498,536],
[513,485,539,0,541,565,484,516,559],
[537,522,531,460,0,574,549,560,563],
[485,408,468,436,427,0,450,500,477],
[541,486,527,517,452,551,0,513,546],
[507,421,503,485,441,501,488,0,505],
[500,422,465,442,438,524,455,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,501,556,530,540,503,565,523],
[506,0,461,505,455,531,475,487,512],
[500,540,0,523,496,529,497,592,523],
[445,496,478,0,500,511,473,529,497],
[471,546,505,501,0,536,530,541,517],
[461,470,472,490,465,0,507,503,449],
[498,526,504,528,471,494,0,513,483],
[436,514,409,472,460,498,488,0,482],
[478,489,478,504,484,552,518,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,498,510,510,474,519,489,505],
[490,0,508,517,511,484,549,453,513],
[503,493,0,503,473,449,520,478,505],
[491,484,498,0,495,456,527,475,484],
[491,490,528,506,0,489,518,475,482],
[527,517,552,545,512,0,544,507,491],
[482,452,481,474,483,457,0,427,474],
[512,548,523,526,526,494,574,0,543],
[496,488,496,517,519,510,527,458,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,511,505,539,488,501,529,497],
[500,0,535,539,549,517,519,543,521],
[490,466,0,474,500,446,472,505,484],
[496,462,527,0,520,486,513,508,470],
[462,452,501,481,0,465,470,515,472],
[513,484,555,515,536,0,500,549,492],
[500,482,529,488,531,501,0,497,510],
[472,458,496,493,486,452,504,0,470],
[504,480,517,531,529,509,491,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,427,577,533,513,468,515,523,532],
[574,0,592,595,542,574,540,497,568],
[424,409,0,503,467,439,415,421,460],
[468,406,498,0,521,484,426,459,509],
[488,459,534,480,0,419,466,499,496],
[533,427,562,517,582,0,473,531,542],
[486,461,586,575,535,528,0,485,529],
[478,504,580,542,502,470,516,0,533],
[469,433,541,492,505,459,472,468,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,495,486,509,489,466,491,501],
[507,0,485,518,484,494,493,483,477],
[506,516,0,525,515,511,486,494,503],
[515,483,476,0,504,477,461,460,493],
[492,517,486,497,0,484,485,464,489],
[512,507,490,524,517,0,502,454,504],
[535,508,515,540,516,499,0,518,503],
[510,518,507,541,537,547,483,0,505],
[500,524,498,508,512,497,498,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,452,493,432,395,481,525,437],
[495,0,470,447,467,515,507,587,486],
[549,531,0,451,489,473,529,551,538],
[508,554,550,0,501,542,493,556,496],
[569,534,512,500,0,515,514,598,506],
[606,486,528,459,486,0,462,559,473],
[520,494,472,508,487,539,0,564,520],
[476,414,450,445,403,442,437,0,428],
[564,515,463,505,495,528,481,573,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,494,556,503,514,487,469,502],
[481,0,491,530,469,514,472,445,471],
[507,510,0,513,489,513,472,483,488],
[445,471,488,0,469,503,431,428,475],
[498,532,512,532,0,508,448,477,492],
[487,487,488,498,493,0,435,444,456],
[514,529,529,570,553,566,0,504,491],
[532,556,518,573,524,557,497,0,509],
[499,530,513,526,509,545,510,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,452,508,510,474,471,453,565,486],
[549,0,514,524,493,508,468,516,504],
[493,487,0,518,445,479,433,465,472],
[491,477,483,0,505,468,489,491,479],
[527,508,556,496,0,483,533,538,477],
[530,493,522,533,518,0,503,539,488],
[548,533,568,512,468,498,0,532,526],
[436,485,536,510,463,462,469,0,514],
[515,497,529,522,524,513,475,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,520,496,552,534,535,499,509],
[475,0,498,485,511,488,463,488,481],
[481,503,0,484,527,506,511,493,472],
[505,516,517,0,531,506,518,512,495],
[449,490,474,470,0,475,488,469,489],
[467,513,495,495,526,0,472,466,479],
[466,538,490,483,513,529,0,487,503],
[502,513,508,489,532,535,514,0,521],
[492,520,529,506,512,522,498,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,516,537,539,515,510,492,502],
[460,0,442,473,521,503,502,465,517],
[485,559,0,491,554,518,501,524,543],
[464,528,510,0,529,515,516,494,550],
[462,480,447,472,0,482,411,475,497],
[486,498,483,486,519,0,505,494,506],
[491,499,500,485,590,496,0,499,492],
[509,536,477,507,526,507,502,0,501],
[499,484,458,451,504,495,509,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,495,505,485,492,482,502,481],
[509,0,474,478,491,485,472,503,478],
[506,527,0,495,476,488,489,536,478],
[496,523,506,0,506,497,498,511,477],
[516,510,525,495,0,493,507,514,500],
[509,516,513,504,508,0,516,524,486],
[519,529,512,503,494,485,0,496,502],
[499,498,465,490,487,477,505,0,486],
[520,523,523,524,501,515,499,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,504,493,502,495,528,502,512],
[492,0,487,518,503,510,482,505,490],
[497,514,0,492,496,498,509,502,518],
[508,483,509,0,466,500,489,516,496],
[499,498,505,535,0,507,489,507,529],
[506,491,503,501,494,0,495,509,498],
[473,519,492,512,512,506,0,506,528],
[499,496,499,485,494,492,495,0,491],
[489,511,483,505,472,503,473,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,508,521,508,503,507,489,514],
[490,0,528,512,495,507,517,496,512],
[493,473,0,480,491,483,491,478,505],
[480,489,521,0,481,492,486,489,487],
[493,506,510,520,0,489,511,514,532],
[498,494,518,509,512,0,504,518,519],
[494,484,510,515,490,497,0,505,524],
[512,505,523,512,487,483,496,0,520],
[487,489,496,514,469,482,477,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,491,525,511,478,499,473,526],
[484,0,471,513,531,485,497,503,520],
[510,530,0,553,513,504,509,500,542],
[476,488,448,0,499,473,449,448,498],
[490,470,488,502,0,455,502,494,507],
[523,516,497,528,546,0,504,529,562],
[502,504,492,552,499,497,0,465,518],
[528,498,501,553,507,472,536,0,521],
[475,481,459,503,494,439,483,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,485,499,495,521,509,523,516],
[495,0,471,509,473,496,477,489,529],
[516,530,0,496,506,517,485,524,530],
[502,492,505,0,513,527,521,536,530],
[506,528,495,488,0,524,512,513,516],
[480,505,484,474,477,0,497,494,518],
[492,524,516,480,489,504,0,519,511],
[478,512,477,465,488,507,482,0,504],
[485,472,471,471,485,483,490,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,569,470,463,490,551,549,527,573],
[432,0,427,369,440,526,374,450,467],
[531,574,0,485,514,508,486,522,542],
[538,632,516,0,508,515,510,467,511],
[511,561,487,493,0,518,541,518,545],
[450,475,493,486,483,0,417,473,513],
[452,627,515,491,460,584,0,520,525],
[474,551,479,534,483,528,481,0,450],
[428,534,459,490,456,488,476,551,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,474,518,475,488,511,474,492],
[504,0,511,528,495,497,493,482,504],
[527,490,0,520,504,507,527,501,526],
[483,473,481,0,477,491,480,470,486],
[526,506,497,524,0,512,521,516,523],
[513,504,494,510,489,0,497,497,523],
[490,508,474,521,480,504,0,484,518],
[527,519,500,531,485,504,517,0,524],
[509,497,475,515,478,478,483,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,468,478,491,496,498,484,473],
[538,0,513,495,498,517,524,493,510],
[533,488,0,476,493,500,515,486,496],
[523,506,525,0,502,518,511,507,492],
[510,503,508,499,0,530,525,497,519],
[505,484,501,483,471,0,524,488,487],
[503,477,486,490,476,477,0,479,490],
[517,508,515,494,504,513,522,0,510],
[528,491,505,509,482,514,511,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,471,501,507,500,515,498,496],
[511,0,441,517,527,502,480,493,503],
[530,560,0,547,533,554,499,526,520],
[500,484,454,0,480,496,510,472,507],
[494,474,468,521,0,503,505,499,504],
[501,499,447,505,498,0,481,497,497],
[486,521,502,491,496,520,0,523,505],
[503,508,475,529,502,504,478,0,503],
[505,498,481,494,497,504,496,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,481,460,616,484,426,465,323],
[506,0,558,436,339,547,591,520,362],
[520,443,0,576,597,527,506,569,359],
[541,565,425,0,558,452,470,642,313],
[385,662,404,443,0,325,501,497,403],
[517,454,474,549,676,0,620,625,394],
[575,410,495,531,500,381,0,397,587],
[536,481,432,359,504,376,604,0,489],
[678,639,642,688,598,607,414,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,523,510,516,496,485,508,500],
[490,0,486,515,478,484,462,475,482],
[478,515,0,528,492,491,473,508,501],
[491,486,473,0,473,475,494,502,479],
[485,523,509,528,0,524,502,528,514],
[505,517,510,526,477,0,485,502,488],
[516,539,528,507,499,516,0,523,521],
[493,526,493,499,473,499,478,0,502],
[501,519,500,522,487,513,480,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,522,500,494,521,503,518,530],
[495,0,495,510,516,516,490,523,516],
[479,506,0,506,490,518,510,518,537],
[501,491,495,0,466,481,485,500,521],
[507,485,511,535,0,517,481,514,513],
[480,485,483,520,484,0,480,508,535],
[498,511,491,516,520,521,0,534,535],
[483,478,483,501,487,493,467,0,523],
[471,485,464,480,488,466,466,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,438,444,455,503,510,496,452,507],
[563,0,511,474,547,502,506,533,558],
[557,490,0,497,505,522,517,506,542],
[546,527,504,0,532,511,542,497,570],
[498,454,496,469,0,535,526,466,514],
[491,499,479,490,466,0,499,529,496],
[505,495,484,459,475,502,0,524,535],
[549,468,495,504,535,472,477,0,521],
[494,443,459,431,487,505,466,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,572,611,512,528,510,460,623],
[491,0,521,511,483,594,435,462,678],
[429,480,0,471,451,487,402,468,464],
[390,490,530,0,529,401,461,483,543],
[489,518,550,472,0,550,498,508,518],
[473,407,514,600,451,0,545,487,537],
[491,566,599,540,503,456,0,522,616],
[541,539,533,518,493,514,479,0,581],
[378,323,537,458,483,464,385,420,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,486,506,494,483,490,502,496],
[511,0,519,498,507,491,498,510,493],
[515,482,0,503,502,477,493,478,495],
[495,503,498,0,487,484,504,497,511],
[507,494,499,514,0,511,489,507,509],
[518,510,524,517,490,0,502,506,512],
[511,503,508,497,512,499,0,497,494],
[499,491,523,504,494,495,504,0,508],
[505,508,506,490,492,489,507,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,499,482,513,497,478,487,490],
[517,0,512,518,532,482,495,495,508],
[502,489,0,478,521,485,483,487,467],
[519,483,523,0,518,516,503,514,483],
[488,469,480,483,0,515,475,459,517],
[504,519,516,485,486,0,488,466,523],
[523,506,518,498,526,513,0,518,488],
[514,506,514,487,542,535,483,0,515],
[511,493,534,518,484,478,513,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,604,590,562,577,596,574,491],
[509,0,559,552,499,476,524,483,478],
[397,442,0,511,459,460,549,511,525],
[411,449,490,0,464,465,471,544,481],
[439,502,542,537,0,481,544,575,502],
[424,525,541,536,520,0,594,518,513],
[405,477,452,530,457,407,0,470,440],
[427,518,490,457,426,483,531,0,495],
[510,523,476,520,499,488,561,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,470,494,473,451,485,516,450],
[530,0,491,533,496,486,495,504,516],
[531,510,0,497,510,492,459,528,471],
[507,468,504,0,513,509,479,510,482],
[528,505,491,488,0,492,495,511,484],
[550,515,509,492,509,0,500,507,469],
[516,506,542,522,506,501,0,537,487],
[485,497,473,491,490,494,464,0,452],
[551,485,530,519,517,532,514,549,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,501,475,501,476,500,476,513],
[527,0,504,499,496,501,505,507,527],
[500,497,0,494,522,476,515,518,519],
[526,502,507,0,527,489,517,542,509],
[500,505,479,474,0,481,490,504,510],
[525,500,525,512,520,0,526,533,523],
[501,496,486,484,511,475,0,508,506],
[525,494,483,459,497,468,493,0,508],
[488,474,482,492,491,478,495,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,347,390,593,523,519,427,640,291],
[654,0,379,598,750,592,578,582,484],
[611,622,0,571,608,513,468,668,535],
[408,403,430,0,547,397,423,363,351],
[478,251,393,454,0,469,376,548,178],
[482,409,488,604,532,0,422,526,387],
[574,423,533,578,625,579,0,713,491],
[361,419,333,638,453,475,288,0,306],
[710,517,466,650,823,614,510,695,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,496,503,493,473,464,480,520],
[546,0,511,536,497,534,465,497,521],
[505,490,0,523,481,470,512,494,501],
[498,465,478,0,445,460,428,481,475],
[508,504,520,556,0,482,478,496,505],
[528,467,531,541,519,0,484,536,517],
[537,536,489,573,523,517,0,523,509],
[521,504,507,520,505,465,478,0,505],
[481,480,500,526,496,484,492,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,541,541,567,479,464,487,566],
[546,0,587,486,528,479,460,499,531],
[460,414,0,492,566,545,533,570,455],
[460,515,509,0,497,511,469,510,556],
[434,473,435,504,0,462,398,529,450],
[522,522,456,490,539,0,525,597,504],
[537,541,468,532,603,476,0,559,551],
[514,502,431,491,472,404,442,0,536],
[435,470,546,445,551,497,450,465,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,521,476,493,502,508,486,504],
[486,0,503,490,494,492,507,457,482],
[480,498,0,470,463,495,462,469,498],
[525,511,531,0,527,489,503,495,500],
[508,507,538,474,0,469,504,484,536],
[499,509,506,512,532,0,530,505,515],
[493,494,539,498,497,471,0,482,472],
[515,544,532,506,517,496,519,0,511],
[497,519,503,501,465,486,529,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,450,463,470,482,503,480,492],
[527,0,508,482,504,519,536,523,578],
[551,493,0,488,535,519,541,510,560],
[538,519,513,0,511,528,541,488,565],
[531,497,466,490,0,486,530,490,539],
[519,482,482,473,515,0,530,490,551],
[498,465,460,460,471,471,0,485,511],
[521,478,491,513,511,511,516,0,552],
[509,423,441,436,462,450,490,449,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,392,586,491,470,469,497,564],
[523,0,427,519,507,518,528,498,527],
[609,574,0,588,498,499,495,555,584],
[415,482,413,0,451,451,432,472,501],
[510,494,503,550,0,450,475,505,546],
[531,483,502,550,551,0,490,522,517],
[532,473,506,569,526,511,0,545,546],
[504,503,446,529,496,479,456,0,583],
[437,474,417,500,455,484,455,418,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,524,527,494,504,487,508,504],
[518,0,531,539,508,509,500,510,506],
[477,470,0,491,499,492,491,474,487],
[474,462,510,0,496,481,512,489,488],
[507,493,502,505,0,493,520,496,501],
[497,492,509,520,508,0,511,493,501],
[514,501,510,489,481,490,0,477,490],
[493,491,527,512,505,508,524,0,490],
[497,495,514,513,500,500,511,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,481,493,495,494,501,499,505],
[499,0,470,497,506,496,514,517,526],
[520,531,0,518,497,496,516,505,529],
[508,504,483,0,518,492,517,503,524],
[506,495,504,483,0,510,522,519,502],
[507,505,505,509,491,0,511,499,519],
[500,487,485,484,479,490,0,503,508],
[502,484,496,498,482,502,498,0,498],
[496,475,472,477,499,482,493,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,472,477,486,509,512,502,485],
[526,0,520,512,544,536,553,482,509],
[529,481,0,497,508,479,511,501,476],
[524,489,504,0,507,490,513,474,485],
[515,457,493,494,0,495,500,483,449],
[492,465,522,511,506,0,525,514,495],
[489,448,490,488,501,476,0,442,466],
[499,519,500,527,518,487,559,0,521],
[516,492,525,516,552,506,535,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,535,494,479,521,516,541,524,504],
[466,0,485,477,521,494,521,502,496],
[507,516,0,505,507,483,516,535,497],
[522,524,496,0,524,485,501,505,515],
[480,480,494,477,0,448,511,474,479],
[485,507,518,516,553,0,486,511,506],
[460,480,485,500,490,515,0,499,462],
[477,499,466,496,527,490,502,0,494],
[497,505,504,486,522,495,539,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,472,486,503,495,499,478,477],
[506,0,493,484,490,519,511,496,472],
[529,508,0,502,506,521,521,536,490],
[515,517,499,0,509,521,533,513,502],
[498,511,495,492,0,526,507,495,499],
[506,482,480,480,475,0,507,485,487],
[502,490,480,468,494,494,0,493,479],
[523,505,465,488,506,516,508,0,489],
[524,529,511,499,502,514,522,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,517,479,499,493,494,494,475],
[503,0,520,505,511,497,492,504,507],
[484,481,0,490,495,493,492,496,453],
[522,496,511,0,541,516,529,498,515],
[502,490,506,460,0,479,500,515,470],
[508,504,508,485,522,0,500,499,517],
[507,509,509,472,501,501,0,501,496],
[507,497,505,503,486,502,500,0,505],
[526,494,548,486,531,484,505,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,461,491,521,441,504,482,469],
[540,0,505,540,522,515,543,516,497],
[540,496,0,499,509,494,496,510,477],
[510,461,502,0,500,485,514,495,488],
[480,479,492,501,0,471,488,499,497],
[560,486,507,516,530,0,513,516,513],
[497,458,505,487,513,488,0,489,508],
[519,485,491,506,502,485,512,0,476],
[532,504,524,513,504,488,493,525,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,520,485,493,508,508,524,524],
[487,0,508,506,498,479,500,498,523],
[481,493,0,490,475,493,498,496,499],
[516,495,511,0,505,494,505,498,519],
[508,503,526,496,0,514,502,512,523],
[493,522,508,507,487,0,494,520,505],
[493,501,503,496,499,507,0,516,517],
[477,503,505,503,489,481,485,0,509],
[477,478,502,482,478,496,484,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,475,518,472,482,503,487,510],
[492,0,491,519,496,492,492,500,508],
[526,510,0,504,491,499,522,525,509],
[483,482,497,0,484,484,495,486,482],
[529,505,510,517,0,527,515,518,491],
[519,509,502,517,474,0,507,500,523],
[498,509,479,506,486,494,0,478,512],
[514,501,476,515,483,501,523,0,492],
[491,493,492,519,510,478,489,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,508,542,409,454,519,453,408],
[535,0,495,512,517,504,468,491,461],
[493,506,0,464,420,485,544,465,411],
[459,489,537,0,412,534,504,502,434],
[592,484,581,589,0,575,532,520,516],
[547,497,516,467,426,0,524,442,422],
[482,533,457,497,469,477,0,433,491],
[548,510,536,499,481,559,568,0,443],
[593,540,590,567,485,579,510,558,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,491,518,515,496,518,506,504],
[492,0,496,518,488,536,506,501,481],
[510,505,0,532,463,516,540,517,513],
[483,483,469,0,518,516,486,508,475],
[486,513,538,483,0,502,511,456,509],
[505,465,485,485,499,0,501,481,472],
[483,495,461,515,490,500,0,506,491],
[495,500,484,493,545,520,495,0,510],
[497,520,488,526,492,529,510,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,519,477,493,469,497,500,501],
[515,0,510,486,488,494,494,497,520],
[482,491,0,487,475,479,495,467,529],
[524,515,514,0,482,499,513,494,501],
[508,513,526,519,0,474,478,510,519],
[532,507,522,502,527,0,468,508,507],
[504,507,506,488,523,533,0,532,531],
[501,504,534,507,491,493,469,0,493],
[500,481,472,500,482,494,470,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,520,560,522,551,482,504,537],
[495,0,548,524,498,538,494,493,486],
[481,453,0,466,492,521,481,479,482],
[441,477,535,0,507,526,459,507,535],
[479,503,509,494,0,525,504,509,551],
[450,463,480,475,476,0,437,435,465],
[519,507,520,542,497,564,0,495,515],
[497,508,522,494,492,566,506,0,505],
[464,515,519,466,450,536,486,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,500,502,508,528,505,541,535],
[478,0,487,502,471,537,455,506,494],
[501,514,0,525,501,527,477,523,535],
[499,499,476,0,464,530,463,502,492],
[493,530,500,537,0,540,500,512,523],
[473,464,474,471,461,0,474,481,472],
[496,546,524,538,501,527,0,523,548],
[460,495,478,499,489,520,478,0,484],
[466,507,466,509,478,529,453,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,491,555,490,509,522,533,503],
[504,0,528,523,523,498,484,522,503],
[510,473,0,547,462,517,496,505,477],
[446,478,454,0,416,471,460,473,473],
[511,478,539,585,0,521,492,560,473],
[492,503,484,530,480,0,525,494,461],
[479,517,505,541,509,476,0,509,481],
[468,479,496,528,441,507,492,0,480],
[498,498,524,528,528,540,520,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,483,497,472,506,540,511,460],
[520,0,511,490,546,550,549,522,518],
[518,490,0,512,497,553,550,544,480],
[504,511,489,0,485,503,529,513,477],
[529,455,504,516,0,517,537,495,478],
[495,451,448,498,484,0,505,466,498],
[461,452,451,472,464,496,0,458,474],
[490,479,457,488,506,535,543,0,480],
[541,483,521,524,523,503,527,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,572,526,511,571,533,447,505,542],
[429,0,435,465,487,460,413,422,484],
[475,566,0,441,495,450,391,414,477],
[490,536,560,0,533,513,479,478,510],
[430,514,506,468,0,434,453,468,537],
[468,541,551,488,567,0,467,456,527],
[554,588,610,522,548,534,0,462,552],
[496,579,587,523,533,545,539,0,541],
[459,517,524,491,464,474,449,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,512,530,517,510,498,518,550],
[470,0,502,494,494,507,493,496,503],
[489,499,0,484,470,510,488,487,491],
[471,507,517,0,507,496,502,479,513],
[484,507,531,494,0,496,485,504,507],
[491,494,491,505,505,0,492,461,470],
[503,508,513,499,516,509,0,491,507],
[483,505,514,522,497,540,510,0,509],
[451,498,510,488,494,531,494,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,499,488,467,513,527,511,522],
[511,0,464,464,501,492,538,438,491],
[502,537,0,496,493,515,551,485,555],
[513,537,505,0,471,518,500,464,532],
[534,500,508,530,0,524,563,513,537],
[488,509,486,483,477,0,541,479,528],
[474,463,450,501,438,460,0,476,475],
[490,563,516,537,488,522,525,0,555],
[479,510,446,469,464,473,526,446,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,519,506,509,493,501,502,530],
[531,0,504,503,478,508,499,524,516],
[482,497,0,478,486,484,500,498,511],
[495,498,523,0,476,506,510,507,511],
[492,523,515,525,0,530,562,546,542],
[508,493,517,495,471,0,508,504,501],
[500,502,501,491,439,493,0,500,480],
[499,477,503,494,455,497,501,0,487],
[471,485,490,490,459,500,521,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,460,473,427,463,482,414,474],
[535,0,491,490,508,510,514,513,558],
[541,510,0,536,490,514,512,526,532],
[528,511,465,0,467,491,467,519,518],
[574,493,511,534,0,499,551,506,568],
[538,491,487,510,502,0,484,496,514],
[519,487,489,534,450,517,0,521,509],
[587,488,475,482,495,505,480,0,560],
[527,443,469,483,433,487,492,441,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,511,492,468,502,503,458,518],
[513,0,518,499,489,525,502,513,515],
[490,483,0,479,468,486,489,464,522],
[509,502,522,0,509,520,518,487,515],
[533,512,533,492,0,526,507,487,514],
[499,476,515,481,475,0,506,491,492],
[498,499,512,483,494,495,0,481,498],
[543,488,537,514,514,510,520,0,527],
[483,486,479,486,487,509,503,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,471,465,495,478,494,493,492],
[521,0,510,498,533,489,507,490,484],
[530,491,0,516,517,513,518,516,492],
[536,503,485,0,516,502,500,507,499],
[506,468,484,485,0,485,486,491,488],
[523,512,488,499,516,0,507,500,498],
[507,494,483,501,515,494,0,491,510],
[508,511,485,494,510,501,510,0,493],
[509,517,509,502,513,503,491,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,538,485,547,546,505,515,521,512],
[463,0,502,513,497,487,515,495,501],
[516,499,0,534,512,488,526,542,518],
[454,488,467,0,501,481,479,480,506],
[455,504,489,500,0,458,479,453,492],
[496,514,513,520,543,0,520,522,531],
[486,486,475,522,522,481,0,501,502],
[480,506,459,521,548,479,500,0,527],
[489,500,483,495,509,470,499,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,543,506,508,501,520,520,507],
[503,0,515,519,499,510,498,512,510],
[458,486,0,490,488,500,490,514,478],
[495,482,511,0,510,510,502,528,507],
[493,502,513,491,0,505,512,501,489],
[500,491,501,491,496,0,502,491,469],
[481,503,511,499,489,499,0,509,487],
[481,489,487,473,500,510,492,0,482],
[494,491,523,494,512,532,514,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,616,448,548,439,528,432,526,439],
[385,0,438,337,532,458,525,481,531],
[553,563,0,407,451,433,479,576,506],
[453,664,594,0,451,384,522,630,567],
[562,469,550,550,0,586,525,616,520],
[473,543,568,617,415,0,420,550,511],
[569,476,522,479,476,581,0,569,508],
[475,520,425,371,385,451,432,0,436],
[562,470,495,434,481,490,493,565,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,476,518,481,498,501,479,489],
[500,0,512,518,504,496,495,504,486],
[525,489,0,516,484,479,511,510,474],
[483,483,485,0,483,486,487,489,482],
[520,497,517,518,0,517,537,506,504],
[503,505,522,515,484,0,542,493,514],
[500,506,490,514,464,459,0,482,482],
[522,497,491,512,495,508,519,0,529],
[512,515,527,519,497,487,519,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,514,512,524,522,507,526,496],
[506,0,503,493,477,506,484,513,487],
[487,498,0,510,496,506,505,522,495],
[489,508,491,0,482,491,458,511,482],
[477,524,505,519,0,510,491,518,524],
[479,495,495,510,491,0,497,527,494],
[494,517,496,543,510,504,0,542,497],
[475,488,479,490,483,474,459,0,466],
[505,514,506,519,477,507,504,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,503,494,512,476,484,508,501],
[512,0,500,507,498,477,492,523,503],
[498,501,0,514,497,463,510,491,494],
[507,494,487,0,496,459,488,499,505],
[489,503,504,505,0,485,512,490,514],
[525,524,538,542,516,0,515,516,498],
[517,509,491,513,489,486,0,502,477],
[493,478,510,502,511,485,499,0,494],
[500,498,507,496,487,503,524,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,499,547,503,473,521,529,502],
[492,0,513,527,501,510,517,500,518],
[502,488,0,523,468,494,505,493,498],
[454,474,478,0,466,482,475,507,451],
[498,500,533,535,0,503,518,509,504],
[528,491,507,519,498,0,524,521,502],
[480,484,496,526,483,477,0,519,481],
[472,501,508,494,492,480,482,0,483],
[499,483,503,550,497,499,520,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,476,552,436,481,501,535,480],
[471,0,425,473,478,550,597,439,459],
[525,576,0,481,494,540,447,450,462],
[449,528,520,0,491,506,448,498,532],
[565,523,507,510,0,506,547,467,528],
[520,451,461,495,495,0,532,481,436],
[500,404,554,553,454,469,0,469,404],
[466,562,551,503,534,520,532,0,524],
[521,542,539,469,473,565,597,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,511,499,487,497,541,513,511],
[485,0,513,470,500,468,512,484,486],
[490,488,0,478,489,493,518,497,517],
[502,531,523,0,502,498,502,486,516],
[514,501,512,499,0,517,509,509,498],
[504,533,508,503,484,0,526,527,501],
[460,489,483,499,492,475,0,501,512],
[488,517,504,515,492,474,500,0,507],
[490,515,484,485,503,500,489,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,556,462,509,468,495,469,507,561],
[445,0,432,437,397,482,467,416,500],
[539,569,0,496,533,542,538,542,511],
[492,564,505,0,473,504,452,530,496],
[533,604,468,528,0,572,521,576,555],
[506,519,459,497,429,0,491,447,428],
[532,534,463,549,480,510,0,539,459],
[494,585,459,471,425,554,462,0,502],
[440,501,490,505,446,573,542,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,484,502,481,463,467,495,484],
[539,0,539,553,537,528,499,533,541],
[517,462,0,491,514,487,483,527,506],
[499,448,510,0,484,494,473,493,491],
[520,464,487,517,0,488,476,511,502],
[538,473,514,507,513,0,506,525,533],
[534,502,518,528,525,495,0,529,515],
[506,468,474,508,490,476,472,0,493],
[517,460,495,510,499,468,486,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,481,461,490,450,521,455,484],
[517,0,480,461,466,447,524,463,461],
[520,521,0,470,524,486,502,485,473],
[540,540,531,0,527,484,545,519,499],
[511,535,477,474,0,486,549,502,502],
[551,554,515,517,515,0,561,506,493],
[480,477,499,456,452,440,0,472,474],
[546,538,516,482,499,495,529,0,491],
[517,540,528,502,499,508,527,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,506,489,531,536,506,521,509],
[471,0,511,499,498,504,497,507,490],
[495,490,0,466,493,520,502,506,492],
[512,502,535,0,519,508,504,523,498],
[470,503,508,482,0,509,489,500,487],
[465,497,481,493,492,0,479,506,473],
[495,504,499,497,512,522,0,516,492],
[480,494,495,478,501,495,485,0,480],
[492,511,509,503,514,528,509,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,490,472,493,610,465,512,501],
[495,0,448,419,518,535,423,462,401],
[511,553,0,538,510,582,440,552,465],
[529,582,463,0,566,620,539,615,538],
[508,483,491,435,0,582,456,596,469],
[391,466,419,381,419,0,400,435,369],
[536,578,561,462,545,601,0,553,521],
[489,539,449,386,405,566,448,0,453],
[500,600,536,463,532,632,480,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,444,419,440,458,482,442,496,464],
[557,0,472,482,502,494,511,544,481],
[582,529,0,489,497,556,508,519,532],
[561,519,512,0,528,550,549,567,485],
[543,499,504,473,0,548,535,523,487],
[519,507,445,451,453,0,488,538,485],
[559,490,493,452,466,513,0,563,527],
[505,457,482,434,478,463,438,0,493],
[537,520,469,516,514,516,474,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,470,469,526,483,501,504,519],
[480,0,504,459,539,466,458,481,491],
[531,497,0,472,551,464,523,493,554],
[532,542,529,0,536,509,541,485,607],
[475,462,450,465,0,474,496,497,511],
[518,535,537,492,527,0,516,471,558],
[500,543,478,460,505,485,0,482,543],
[497,520,508,516,504,530,519,0,535],
[482,510,447,394,490,443,458,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,521,506,510,532,488,488,524],
[502,0,490,514,527,528,512,502,516],
[480,511,0,496,508,505,482,488,512],
[495,487,505,0,515,521,490,483,520],
[491,474,493,486,0,523,501,481,513],
[469,473,496,480,478,0,480,474,481],
[513,489,519,511,500,521,0,483,513],
[513,499,513,518,520,527,518,0,510],
[477,485,489,481,488,520,488,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,497,526,547,512,496,521,520],
[484,0,503,508,522,512,508,510,514],
[504,498,0,550,530,507,522,504,511],
[475,493,451,0,507,493,490,485,506],
[454,479,471,494,0,511,468,447,468],
[489,489,494,508,490,0,507,495,516],
[505,493,479,511,533,494,0,510,514],
[480,491,497,516,554,506,491,0,522],
[481,487,490,495,533,485,487,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,565,533,537,545,492,498,500],
[476,0,534,483,488,494,510,497,525],
[436,467,0,491,498,488,487,469,473],
[468,518,510,0,519,514,472,453,481],
[464,513,503,482,0,514,471,475,472],
[456,507,513,487,487,0,490,465,485],
[509,491,514,529,530,511,0,525,523],
[503,504,532,548,526,536,476,0,518],
[501,476,528,520,529,516,478,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,516,550,589,574,552,628,464],
[480,0,513,604,644,631,582,579,556],
[485,488,0,540,541,592,483,549,519],
[451,397,461,0,517,620,434,621,523],
[412,357,460,484,0,560,388,573,416],
[427,370,409,381,441,0,501,536,436],
[449,419,518,567,613,500,0,604,495],
[373,422,452,380,428,465,397,0,451],
[537,445,482,478,585,565,506,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,503,481,529,455,514,462,449],
[493,0,524,499,536,486,520,503,479],
[498,477,0,496,497,473,484,462,469],
[520,502,505,0,494,473,472,477,502],
[472,465,504,507,0,475,497,456,465],
[546,515,528,528,526,0,535,516,491],
[487,481,517,529,504,466,0,483,462],
[539,498,539,524,545,485,518,0,468],
[552,522,532,499,536,510,539,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,482,452,455,483,473,455,501],
[504,0,498,485,505,530,484,464,500],
[519,503,0,513,508,540,500,495,534],
[549,516,488,0,507,498,506,519,545],
[546,496,493,494,0,549,514,472,517],
[518,471,461,503,452,0,507,440,484],
[528,517,501,495,487,494,0,484,512],
[546,537,506,482,529,561,517,0,523],
[500,501,467,456,484,517,489,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,589,486,468,478,468,486,467,570],
[412,0,450,460,430,426,461,509,499],
[515,551,0,436,594,510,528,513,634],
[533,541,565,0,589,456,471,522,573],
[523,571,407,412,0,447,467,522,569],
[533,575,491,545,554,0,492,545,541],
[515,540,473,530,534,509,0,460,515],
[534,492,488,479,479,456,541,0,550],
[431,502,367,428,432,460,486,451,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,539,512,532,542,549,522,483],
[486,0,511,488,501,508,532,514,490],
[462,490,0,477,487,491,502,484,488],
[489,513,524,0,518,520,529,520,512],
[469,500,514,483,0,484,514,493,507],
[459,493,510,481,517,0,514,497,478],
[452,469,499,472,487,487,0,493,457],
[479,487,517,481,508,504,508,0,465],
[518,511,513,489,494,523,544,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,486,493,510,469,477,500,490],
[488,0,439,449,478,462,484,495,469],
[515,562,0,477,522,534,514,544,514],
[508,552,524,0,501,480,495,519,499],
[491,523,479,500,0,477,510,524,501],
[532,539,467,521,524,0,526,568,476],
[524,517,487,506,491,475,0,534,507],
[501,506,457,482,477,433,467,0,456],
[511,532,487,502,500,525,494,545,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,526,545,653,543,643,582,573],
[502,0,488,479,617,537,561,503,529],
[475,513,0,509,605,523,497,529,583],
[456,522,492,0,608,535,513,525,528],
[348,384,396,393,0,437,400,460,501],
[458,464,478,466,564,0,540,547,537],
[358,440,504,488,601,461,0,503,520],
[419,498,472,476,541,454,498,0,561],
[428,472,418,473,500,464,481,440,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,542,519,517,522,519,480,503],
[483,0,528,498,468,482,495,457,456],
[459,473,0,464,492,497,493,475,471],
[482,503,537,0,486,502,528,501,491],
[484,533,509,515,0,493,504,475,477],
[479,519,504,499,508,0,514,482,494],
[482,506,508,473,497,487,0,478,452],
[521,544,526,500,526,519,523,0,497],
[498,545,530,510,524,507,549,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,627,484,557,538,514,537,475],
[513,0,590,466,541,453,501,464,500],
[374,411,0,436,499,475,451,411,459],
[517,535,565,0,563,435,470,504,560],
[444,460,502,438,0,461,487,425,480],
[463,548,526,566,540,0,489,527,539],
[487,500,550,531,514,512,0,511,487],
[464,537,590,497,576,474,490,0,511],
[526,501,542,441,521,462,514,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,460,486,501,460,483,472,473,498],
[541,0,516,506,493,492,529,516,505],
[515,485,0,497,500,483,519,492,500],
[500,495,504,0,486,488,507,498,469],
[541,508,501,515,0,500,513,515,523],
[518,509,518,513,501,0,508,508,495],
[529,472,482,494,488,493,0,483,450],
[528,485,509,503,486,493,518,0,491],
[503,496,501,532,478,506,551,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,514,516,511,518,505,499,496],
[471,0,477,471,479,472,499,487,463],
[487,524,0,502,513,495,492,477,482],
[485,530,499,0,526,503,504,482,501],
[490,522,488,475,0,480,493,487,478],
[483,529,506,498,521,0,521,482,521],
[496,502,509,497,508,480,0,507,499],
[502,514,524,519,514,519,494,0,496],
[505,538,519,500,523,480,502,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,514,480,481,526,547,502,478],
[521,0,459,463,462,514,551,481,495],
[487,542,0,493,488,532,547,517,508],
[521,538,508,0,500,509,537,527,519],
[520,539,513,501,0,549,552,538,479],
[475,487,469,492,452,0,496,469,455],
[454,450,454,464,449,505,0,440,466],
[499,520,484,474,463,532,561,0,487],
[523,506,493,482,522,546,535,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,511,499,501,511,512,487,509],
[511,0,519,515,519,515,482,501,502],
[490,482,0,473,503,509,495,499,488],
[502,486,528,0,506,516,489,504,492],
[500,482,498,495,0,509,471,502,474],
[490,486,492,485,492,0,473,495,469],
[489,519,506,512,530,528,0,523,514],
[514,500,502,497,499,506,478,0,494],
[492,499,513,509,527,532,487,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,484,476,552,491,530,549,600],
[546,0,480,551,521,559,560,554,602],
[517,521,0,512,519,479,527,499,558],
[525,450,489,0,526,522,552,552,623],
[449,480,482,475,0,501,459,454,593],
[510,442,522,479,500,0,503,496,557],
[471,441,474,449,542,498,0,532,550],
[452,447,502,449,547,505,469,0,564],
[401,399,443,378,408,444,451,437,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,501,540,434,484,479,451,482],
[492,0,503,517,488,472,485,494,517],
[500,498,0,505,500,533,522,494,469],
[461,484,496,0,444,488,466,464,452],
[567,513,501,557,0,515,469,489,505],
[517,529,468,513,486,0,495,465,523],
[522,516,479,535,532,506,0,465,498],
[550,507,507,537,512,536,536,0,493],
[519,484,532,549,496,478,503,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,496,464,491,495,510,471,485],
[516,0,520,543,519,478,529,523,461],
[505,481,0,488,511,475,510,487,479],
[537,458,513,0,477,444,500,480,450],
[510,482,490,524,0,453,463,517,469],
[506,523,526,557,548,0,515,494,519],
[491,472,491,501,538,486,0,499,486],
[530,478,514,521,484,507,502,0,502],
[516,540,522,551,532,482,515,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,524,529,521,498,502,530,504],
[495,0,503,493,521,511,501,514,488],
[477,498,0,521,525,497,479,525,497],
[472,508,480,0,514,518,484,517,517],
[480,480,476,487,0,495,488,477,496],
[503,490,504,483,506,0,486,503,484],
[499,500,522,517,513,515,0,511,496],
[471,487,476,484,524,498,490,0,492],
[497,513,504,484,505,517,505,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,526,487,475,527,513,509,500],
[507,0,501,473,511,499,500,514,498],
[475,500,0,491,477,514,516,504,492],
[514,528,510,0,488,520,549,489,508],
[526,490,524,513,0,528,547,493,504],
[474,502,487,481,473,0,492,485,503],
[488,501,485,452,454,509,0,488,472],
[492,487,497,512,508,516,513,0,487],
[501,503,509,493,497,498,529,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,322,473,532,551,500,290,393,469],
[679,0,743,605,702,647,469,734,718],
[528,258,0,608,506,367,265,399,377],
[469,396,393,0,448,333,402,511,453],
[450,299,495,553,0,477,342,354,410],
[501,354,634,668,524,0,580,590,587],
[711,532,736,599,659,421,0,633,579],
[608,267,602,490,647,411,368,0,484],
[532,283,624,548,591,414,422,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,530,506,497,506,567,501,514],
[486,0,512,493,497,488,536,469,516],
[471,489,0,471,478,502,494,501,506],
[495,508,530,0,511,520,524,508,532],
[504,504,523,490,0,489,488,506,508],
[495,513,499,481,512,0,527,529,537],
[434,465,507,477,513,474,0,472,468],
[500,532,500,493,495,472,529,0,517],
[487,485,495,469,493,464,533,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,505,536,467,512,519,493,601],
[479,0,548,494,524,435,502,493,559],
[496,453,0,487,455,493,513,520,540],
[465,507,514,0,529,514,525,504,592],
[534,477,546,472,0,517,520,480,591],
[489,566,508,487,484,0,500,492,594],
[482,499,488,476,481,501,0,483,604],
[508,508,481,497,521,509,518,0,625],
[400,442,461,409,410,407,397,376,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,490,490,525,493,480,486,498],
[493,0,489,522,515,521,501,525,520],
[511,512,0,516,504,498,485,544,532],
[511,479,485,0,544,506,494,552,537],
[476,486,497,457,0,476,465,506,476],
[508,480,503,495,525,0,457,518,493],
[521,500,516,507,536,544,0,546,537],
[515,476,457,449,495,483,455,0,511],
[503,481,469,464,525,508,464,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,482,500,487,507,466,489,477],
[500,0,497,485,484,509,479,478,487],
[519,504,0,505,494,502,492,498,504],
[501,516,496,0,489,518,495,488,483],
[514,517,507,512,0,525,510,495,511],
[494,492,499,483,476,0,487,480,480],
[535,522,509,506,491,514,0,497,507],
[512,523,503,513,506,521,504,0,490],
[524,514,497,518,490,521,494,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,474,536,546,511,487,486,510],
[480,0,506,516,559,462,544,510,553],
[527,495,0,507,491,482,514,559,494],
[465,485,494,0,521,488,475,439,480],
[455,442,510,480,0,495,458,473,549],
[490,539,519,513,506,0,542,511,534],
[514,457,487,526,543,459,0,547,525],
[515,491,442,562,528,490,454,0,552],
[491,448,507,521,452,467,476,449,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,518,509,526,495,501,512,514],
[481,0,523,508,474,508,501,485,493],
[483,478,0,499,489,460,488,488,490],
[492,493,502,0,503,490,519,482,494],
[475,527,512,498,0,502,485,476,488],
[506,493,541,511,499,0,502,487,517],
[500,500,513,482,516,499,0,490,507],
[489,516,513,519,525,514,511,0,504],
[487,508,511,507,513,484,494,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,462,523,452,506,501,468,456],
[497,0,485,472,446,474,490,459,467],
[539,516,0,513,519,508,528,474,497],
[478,529,488,0,469,515,505,476,470],
[549,555,482,532,0,528,528,524,516],
[495,527,493,486,473,0,490,486,492],
[500,511,473,496,473,511,0,480,488],
[533,542,527,525,477,515,521,0,488],
[545,534,504,531,485,509,513,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,435,507,489,454,498,523,480,493],
[566,0,559,518,496,533,487,477,509],
[494,442,0,514,497,479,523,483,456],
[512,483,487,0,486,463,518,500,526],
[547,505,504,515,0,525,536,455,528],
[503,468,522,538,476,0,515,534,550],
[478,514,478,483,465,486,0,456,434],
[521,524,518,501,546,467,545,0,546],
[508,492,545,475,473,451,567,455,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,469,492,498,475,461,501,479],
[533,0,487,507,500,497,494,498,493],
[532,514,0,503,520,515,512,513,491],
[509,494,498,0,480,489,469,518,479],
[503,501,481,521,0,493,490,510,497],
[526,504,486,512,508,0,504,526,489],
[540,507,489,532,511,497,0,533,525],
[500,503,488,483,491,475,468,0,503],
[522,508,510,522,504,512,476,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,507,520,502,512,549,517,496],
[473,0,496,499,506,495,499,490,485],
[494,505,0,492,502,533,530,526,514],
[481,502,509,0,517,495,547,495,506],
[499,495,499,484,0,486,521,498,478],
[489,506,468,506,515,0,513,500,483],
[452,502,471,454,480,488,0,491,472],
[484,511,475,506,503,501,510,0,464],
[505,516,487,495,523,518,529,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,384,533,342,482,583,426,336,389],
[617,0,486,569,611,618,512,538,531],
[468,515,0,375,410,464,333,342,305],
[659,432,626,0,513,398,483,359,469],
[519,390,591,488,0,502,467,362,377],
[418,383,537,603,499,0,487,340,511],
[575,489,668,518,534,514,0,418,448],
[665,463,659,642,639,661,583,0,603],
[612,470,696,532,624,490,553,398,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,475,458,458,461,504,463,477],
[544,0,524,495,510,518,538,494,529],
[526,477,0,481,480,481,509,484,504],
[543,506,520,0,480,501,526,492,539],
[543,491,521,521,0,496,520,501,532],
[540,483,520,500,505,0,500,491,518],
[497,463,492,475,481,501,0,468,505],
[538,507,517,509,500,510,533,0,527],
[524,472,497,462,469,483,496,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,496,547,572,497,501,517,449],
[494,0,422,522,552,493,461,536,429],
[505,579,0,573,547,545,449,536,478],
[454,479,428,0,492,478,389,492,421],
[429,449,454,509,0,458,412,506,464],
[504,508,456,523,543,0,488,506,441],
[500,540,552,612,589,513,0,531,505],
[484,465,465,509,495,495,470,0,408],
[552,572,523,580,537,560,496,593,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,543,478,550,523,502,499,489,513],
[458,0,517,481,469,503,493,497,498],
[523,484,0,527,480,535,481,487,531],
[451,520,474,0,441,468,469,469,504],
[478,532,521,560,0,545,522,518,527],
[499,498,466,533,456,0,492,482,464],
[502,508,520,532,479,509,0,505,534],
[512,504,514,532,483,519,496,0,518],
[488,503,470,497,474,537,467,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,541,533,529,540,492,500,487],
[540,0,555,530,539,521,436,463,507],
[460,446,0,517,444,471,455,423,451],
[468,471,484,0,507,513,464,522,485],
[472,462,557,494,0,461,478,484,452],
[461,480,530,488,540,0,436,499,424],
[509,565,546,537,523,565,0,551,470],
[501,538,578,479,517,502,450,0,468],
[514,494,550,516,549,577,531,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,530,488,486,529,521,526,496],
[531,0,488,482,463,498,472,503,485],
[471,513,0,503,444,498,476,560,446],
[513,519,498,0,490,487,512,540,570],
[515,538,557,511,0,536,487,536,516],
[472,503,503,514,465,0,510,519,465],
[480,529,525,489,514,491,0,551,529],
[475,498,441,461,465,482,450,0,437],
[505,516,555,431,485,536,472,564,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,505,503,503,471,500,512,493],
[514,0,520,546,505,521,525,509,482],
[496,481,0,496,490,474,482,470,485],
[498,455,505,0,514,486,494,503,501],
[498,496,511,487,0,490,475,496,486],
[530,480,527,515,511,0,519,506,508],
[501,476,519,507,526,482,0,505,468],
[489,492,531,498,505,495,496,0,468],
[508,519,516,500,515,493,533,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1001, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_9_1001.csv", index=False, header=False)