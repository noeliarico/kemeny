
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,522,524,512,528,462,479,480,492,513,495],
[478,0,489,491,485,457,502,506,489,481,486],
[476,511,0,483,493,462,481,448,478,506,477],
[488,509,517,0,550,519,506,523,540,519,539],
[472,515,507,450,0,424,493,498,452,501,470],
[538,543,538,481,576,0,520,518,525,553,508],
[521,498,519,494,507,480,0,483,499,497,500],
[520,494,552,477,502,482,517,0,506,513,504],
[508,511,522,460,548,475,501,494,0,513,482],
[487,519,494,481,499,447,503,487,487,0,507],
[505,514,523,461,530,492,500,496,518,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,494,498,488,471,484,514,488,493,502],
[486,0,495,511,495,489,482,502,482,500,493],
[506,505,0,503,516,501,482,509,490,483,500],
[502,489,497,0,504,490,476,481,481,480,482],
[512,505,484,496,0,509,499,538,493,497,489],
[529,511,499,510,491,0,492,510,519,493,481],
[516,518,518,524,501,508,0,528,526,505,497],
[486,498,491,519,462,490,472,0,497,477,487],
[512,518,510,519,507,481,474,503,0,501,500],
[507,500,517,520,503,507,495,523,499,0,486],
[498,507,500,518,511,519,503,513,500,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,413,504,616,461,577,543,474,553,496,491],
[587,0,436,630,577,663,454,612,549,544,490],
[496,564,0,564,427,428,517,659,563,599,562],
[384,370,436,0,560,494,491,537,576,411,446],
[539,423,573,440,0,478,430,589,540,516,556],
[423,337,572,506,522,0,593,622,404,506,491],
[457,546,483,509,570,407,0,588,578,562,463],
[526,388,341,463,411,378,412,0,339,383,428],
[447,451,437,424,460,596,422,661,0,474,567],
[504,456,401,589,484,494,438,617,526,0,522],
[509,510,438,554,444,509,537,572,433,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,540,513,486,459,513,509,480,492,478,501],
[460,0,503,487,468,537,481,450,518,462,486],
[487,497,0,512,483,550,496,462,527,516,506],
[514,513,488,0,475,509,504,453,510,490,500],
[541,532,517,525,0,559,488,513,542,516,534],
[487,463,450,491,441,0,459,437,468,452,475],
[491,519,504,496,512,541,0,498,526,490,533],
[520,550,538,547,487,563,502,0,529,533,530],
[508,482,473,490,458,532,474,471,0,489,506],
[522,538,484,510,484,548,510,467,511,0,517],
[499,514,494,500,466,525,467,470,494,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,522,645,566,522,535,540,553,516,589],
[506,0,456,577,527,562,548,523,514,524,540],
[478,544,0,588,528,535,597,515,589,560,566],
[355,423,412,0,501,511,505,455,515,414,456],
[434,473,472,499,0,494,477,442,462,463,469],
[478,438,465,489,506,0,474,470,532,510,513],
[465,452,403,495,523,526,0,489,491,440,564],
[460,477,485,545,558,530,511,0,548,516,498],
[447,486,411,485,538,468,509,452,0,518,525],
[484,476,440,586,537,490,560,484,482,0,486],
[411,460,434,544,531,487,436,502,475,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,496,490,489,466,493,493,479,484,466],
[503,0,493,497,505,493,507,527,503,494,506],
[504,507,0,497,505,492,498,534,500,481,487],
[510,503,503,0,469,494,494,508,496,468,468],
[511,495,495,531,0,482,483,512,499,477,495],
[534,507,508,506,518,0,495,534,505,488,499],
[507,493,502,506,517,505,0,494,487,494,478],
[507,473,466,492,488,466,506,0,483,481,491],
[521,497,500,504,501,495,513,517,0,488,488],
[516,506,519,532,523,512,506,519,512,0,493],
[534,494,513,532,505,501,522,509,512,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,550,540,479,538,513,523,515,545,546],
[510,0,540,506,524,491,511,528,529,514,564],
[450,460,0,513,492,512,487,489,496,493,519],
[460,494,487,0,504,515,486,521,520,469,544],
[521,476,508,496,0,517,494,550,510,518,532],
[462,509,488,485,483,0,492,507,491,499,505],
[487,489,513,514,506,508,0,513,522,485,534],
[477,472,511,479,450,493,487,0,486,474,526],
[485,471,504,480,490,509,478,514,0,466,539],
[455,486,507,531,482,501,515,526,534,0,537],
[454,436,481,456,468,495,466,474,461,463,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,500,519,523,505,506,533,510,519,475],
[504,0,525,492,507,493,498,520,499,519,502],
[500,475,0,463,489,449,489,500,490,500,448],
[481,508,537,0,513,472,524,532,519,538,516],
[477,493,511,487,0,468,505,523,500,506,475],
[495,507,551,528,532,0,519,567,519,543,509],
[494,502,511,476,495,481,0,533,521,495,497],
[467,480,500,468,477,433,467,0,497,491,492],
[490,501,510,481,500,481,479,503,0,514,463],
[481,481,500,462,494,457,505,509,486,0,481],
[525,498,552,484,525,491,503,508,537,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,508,393,500,550,464,522,434,446,471],
[525,0,533,403,525,586,453,548,454,577,507],
[492,467,0,397,500,510,486,583,419,517,462],
[607,597,603,0,617,573,448,610,538,592,528],
[500,475,500,383,0,517,439,462,448,479,508],
[450,414,490,427,483,0,414,474,437,453,442],
[536,547,514,552,561,586,0,548,606,586,494],
[478,452,417,390,538,526,452,0,481,471,403],
[566,546,581,462,552,563,394,519,0,553,492],
[554,423,483,408,521,547,414,529,447,0,466],
[529,493,538,472,492,558,506,597,508,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,487,483,496,485,539,503,486,540,499],
[513,0,479,506,526,529,549,515,529,536,517],
[513,521,0,513,533,529,537,501,494,586,536],
[517,494,487,0,490,520,549,540,520,554,514],
[504,474,467,510,0,480,549,501,529,516,543],
[515,471,471,480,520,0,546,515,489,546,506],
[461,451,463,451,451,454,0,453,469,508,460],
[497,485,499,460,499,485,547,0,503,526,534],
[514,471,506,480,471,511,531,497,0,565,489],
[460,464,414,446,484,454,492,474,435,0,450],
[501,483,464,486,457,494,540,466,511,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,500,512,498,519,501,560,526,551,410],
[493,0,505,496,508,517,517,493,524,577,462],
[500,495,0,536,471,510,484,489,532,520,467],
[488,504,464,0,480,495,486,491,505,537,467],
[502,492,529,520,0,471,509,504,510,533,431],
[481,483,490,505,529,0,519,525,530,537,503],
[499,483,516,514,491,481,0,516,530,536,409],
[440,507,511,509,496,475,484,0,516,539,404],
[474,476,468,495,490,470,470,484,0,493,451],
[449,423,480,463,467,463,464,461,507,0,421],
[590,538,533,533,569,497,591,596,549,579,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,501,497,497,482,513,462,488,460,514],
[502,0,486,493,503,497,537,466,510,484,516],
[499,514,0,486,490,481,508,467,473,465,498],
[503,507,514,0,491,498,509,483,478,471,535],
[503,497,510,509,0,489,536,468,485,469,550],
[518,503,519,502,511,0,516,470,507,496,516],
[487,463,492,491,464,484,0,460,476,475,497],
[538,534,533,517,532,530,540,0,511,484,549],
[512,490,527,522,515,493,524,489,0,508,531],
[540,516,535,529,531,504,525,516,492,0,542],
[486,484,502,465,450,484,503,451,469,458,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,492,516,528,537,493,564,529,512,496],
[508,0,483,478,500,522,492,542,516,533,491],
[508,517,0,500,521,518,501,555,511,533,505],
[484,522,500,0,501,527,482,549,507,512,483],
[472,500,479,499,0,506,472,497,489,512,478],
[463,478,482,473,494,0,485,503,487,501,473],
[507,508,499,518,528,515,0,532,531,524,476],
[436,458,445,451,503,497,468,0,466,498,444],
[471,484,489,493,511,513,469,534,0,512,451],
[488,467,467,488,488,499,476,502,488,0,447],
[504,509,495,517,522,527,524,556,549,553,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,509,499,516,505,509,487,504,500,522],
[511,0,493,495,523,512,515,520,518,522,529],
[491,507,0,511,519,479,495,490,504,496,521],
[501,505,489,0,496,498,494,501,489,497,511],
[484,477,481,504,0,472,483,479,485,482,495],
[495,488,521,502,528,0,515,521,498,498,524],
[491,485,505,506,517,485,0,486,489,491,503],
[513,480,510,499,521,479,514,0,488,519,514],
[496,482,496,511,515,502,511,512,0,518,524],
[500,478,504,503,518,502,509,481,482,0,516],
[478,471,479,489,505,476,497,486,476,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,542,494,532,508,488,449,490,494,498],
[516,0,518,539,523,535,571,495,525,521,519],
[458,482,0,502,549,520,490,419,460,458,489],
[506,461,498,0,556,513,490,476,476,519,530],
[468,477,451,444,0,483,480,484,448,473,487],
[492,465,480,487,517,0,462,456,430,505,497],
[512,429,510,510,520,538,0,468,471,490,502],
[551,505,581,524,516,544,532,0,460,531,544],
[510,475,540,524,552,570,529,540,0,530,556],
[506,479,542,481,527,495,510,469,470,0,499],
[502,481,511,470,513,503,498,456,444,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,492,490,497,533,483,485,476,514,470],
[541,0,515,505,502,548,541,499,482,540,485],
[508,485,0,500,491,528,511,471,497,547,497],
[510,495,500,0,510,543,507,501,514,545,460],
[503,498,509,490,0,520,507,502,496,524,494],
[467,452,472,457,480,0,515,466,454,529,451],
[517,459,489,493,493,485,0,500,486,567,480],
[515,501,529,499,498,534,500,0,518,534,467],
[524,518,503,486,504,546,514,482,0,547,505],
[486,460,453,455,476,471,433,466,453,0,453],
[530,515,503,540,506,549,520,533,495,547,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,506,499,484,491,498,498,496,488,540],
[486,0,504,486,478,510,521,482,458,498,529],
[494,496,0,496,475,451,487,505,460,461,500],
[501,514,504,0,505,490,515,483,483,529,540],
[516,522,525,495,0,531,513,476,481,525,531],
[509,490,549,510,469,0,535,475,491,504,534],
[502,479,513,485,487,465,0,461,529,488,492],
[502,518,495,517,524,525,539,0,512,511,528],
[504,542,540,517,519,509,471,488,0,515,522],
[512,502,539,471,475,496,512,489,485,0,534],
[460,471,500,460,469,466,508,472,478,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,524,477,498,465,520,508,502,501,534],
[515,0,515,511,531,508,521,520,491,525,523],
[476,485,0,471,494,488,499,517,472,499,502],
[523,489,529,0,490,497,532,550,484,517,511],
[502,469,506,510,0,486,510,506,469,531,517],
[535,492,512,503,514,0,510,532,500,538,517],
[480,479,501,468,490,490,0,533,465,511,524],
[492,480,483,450,494,468,467,0,498,495,486],
[498,509,528,516,531,500,535,502,0,533,512],
[499,475,501,483,469,462,489,505,467,0,520],
[466,477,498,489,483,483,476,514,488,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,559,591,549,539,565,498,571,514,538,560],
[441,0,547,403,515,512,452,492,470,416,481],
[409,453,0,449,495,463,424,486,447,350,461],
[451,597,551,0,526,528,503,550,500,507,545],
[461,485,505,474,0,506,475,520,460,422,532],
[435,488,537,472,494,0,452,539,438,419,480],
[502,548,576,497,525,548,0,471,493,407,473],
[429,508,514,450,480,461,529,0,493,378,484],
[486,530,553,500,540,562,507,507,0,540,575],
[462,584,650,493,578,581,593,622,460,0,552],
[440,519,539,455,468,520,527,516,425,448,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,500,541,474,444,509,520,476,517,555],
[486,0,502,536,464,492,466,460,499,497,490],
[500,498,0,616,470,474,464,497,508,512,524],
[459,464,384,0,467,415,424,439,461,457,496],
[526,536,530,533,0,509,494,531,532,544,558],
[556,508,526,585,491,0,518,503,524,520,507],
[491,534,536,576,506,482,0,495,531,511,543],
[480,540,503,561,469,497,505,0,500,499,541],
[524,501,492,539,468,476,469,500,0,511,531],
[483,503,488,543,456,480,489,501,489,0,562],
[445,510,476,504,442,493,457,459,469,438,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,480,481,507,500,464,488,469,488,473],
[516,0,501,498,494,496,501,500,510,497,506],
[520,499,0,479,475,519,481,515,487,495,485],
[519,502,521,0,502,519,507,504,496,493,487],
[493,506,525,498,0,514,507,489,496,496,472],
[500,504,481,481,486,0,483,516,504,490,482],
[536,499,519,493,493,517,0,539,501,521,497],
[512,500,485,496,511,484,461,0,477,504,484],
[531,490,513,504,504,496,499,523,0,505,517],
[512,503,505,507,504,510,479,496,495,0,483],
[527,494,515,513,528,518,503,516,483,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,501,510,541,530,501,527,478,525,508],
[496,0,512,490,489,552,501,521,473,483,482],
[499,488,0,482,504,498,499,503,457,471,450],
[490,510,518,0,524,529,481,489,517,526,499],
[459,511,496,476,0,520,499,497,499,499,463],
[470,448,502,471,480,0,470,486,446,504,428],
[499,499,501,519,501,530,0,468,481,528,498],
[473,479,497,511,503,514,532,0,484,508,484],
[522,527,543,483,501,554,519,516,0,547,526],
[475,517,529,474,501,496,472,492,453,0,477],
[492,518,550,501,537,572,502,516,474,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,518,534,520,504,460,543,478,519,470],
[484,0,496,489,467,515,480,483,476,522,468],
[482,504,0,531,517,561,476,545,480,525,503],
[466,511,469,0,466,476,492,515,475,524,481],
[480,533,483,534,0,513,478,559,481,517,478],
[496,485,439,524,487,0,476,538,470,509,443],
[540,520,524,508,522,524,0,536,500,516,498],
[457,517,455,485,441,462,464,0,466,505,452],
[522,524,520,525,519,530,500,534,0,565,521],
[481,478,475,476,483,491,484,495,435,0,455],
[530,532,497,519,522,557,502,548,479,545,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,504,482,463,466,481,481,455,440,515],
[514,0,491,474,477,481,532,509,477,507,480],
[496,509,0,501,503,516,529,523,491,496,507],
[518,526,499,0,528,500,556,511,478,491,524],
[537,523,497,472,0,490,483,517,490,483,506],
[534,519,484,500,510,0,532,505,475,491,525],
[519,468,471,444,517,468,0,476,470,460,502],
[519,491,477,489,483,495,524,0,504,504,486],
[545,523,509,522,510,525,530,496,0,492,510],
[560,493,504,509,517,509,540,496,508,0,486],
[485,520,493,476,494,475,498,514,490,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,503,500,456,479,467,460,487,482,463],
[495,0,480,481,469,510,481,459,507,496,489],
[497,520,0,494,477,513,504,495,508,507,497],
[500,519,506,0,490,512,487,514,488,488,493],
[544,531,523,510,0,514,493,508,509,486,527],
[521,490,487,488,486,0,495,518,501,497,511],
[533,519,496,513,507,505,0,504,509,473,497],
[540,541,505,486,492,482,496,0,534,499,505],
[513,493,492,512,491,499,491,466,0,465,489],
[518,504,493,512,514,503,527,501,535,0,520],
[537,511,503,507,473,489,503,495,511,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,546,509,543,480,447,479,523,552,538],
[473,0,567,470,450,464,490,457,468,570,511],
[454,433,0,511,468,462,445,492,425,491,490],
[491,530,489,0,524,450,489,455,490,496,527],
[457,550,532,476,0,473,443,490,491,508,517],
[520,536,538,550,527,0,473,504,484,537,511],
[553,510,555,511,557,527,0,499,492,558,539],
[521,543,508,545,510,496,501,0,510,566,514],
[477,532,575,510,509,516,508,490,0,512,487],
[448,430,509,504,492,463,442,434,488,0,442],
[462,489,510,473,483,489,461,486,513,558,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,513,502,525,515,507,526,501,531,499],
[507,0,536,523,515,520,508,478,503,551,546],
[487,464,0,470,530,474,499,467,436,501,484],
[498,477,530,0,538,475,515,498,475,510,529],
[475,485,470,462,0,462,466,478,455,491,503],
[485,480,526,525,538,0,515,535,455,488,506],
[493,492,501,485,534,485,0,492,486,557,539],
[474,522,533,502,522,465,508,0,472,508,536],
[499,497,564,525,545,545,514,528,0,546,522],
[469,449,499,490,509,512,443,492,454,0,552],
[501,454,516,471,497,494,461,464,478,448,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,487,501,490,477,514,541,527,488,489],
[513,0,490,492,478,495,543,506,500,491,496],
[513,510,0,484,475,485,530,500,516,474,474],
[499,508,516,0,498,474,545,544,520,497,473],
[510,522,525,502,0,522,521,532,508,493,513],
[523,505,515,526,478,0,553,552,536,508,506],
[486,457,470,455,479,447,0,513,484,469,463],
[459,494,500,456,468,448,487,0,474,475,459],
[473,500,484,480,492,464,516,526,0,481,517],
[512,509,526,503,507,492,531,525,519,0,500],
[511,504,526,527,487,494,537,541,483,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,481,498,432,478,433,515,479,515,528],
[491,0,531,486,523,501,509,497,492,535,493],
[519,469,0,499,479,528,536,525,544,533,539],
[502,514,501,0,448,500,454,519,496,495,469],
[568,477,521,552,0,512,550,489,515,469,511],
[522,499,472,500,488,0,477,568,455,510,481],
[567,491,464,546,450,523,0,517,519,527,538],
[485,503,475,481,511,432,483,0,501,544,533],
[521,508,456,504,485,545,481,499,0,507,514],
[485,465,467,505,531,490,473,456,493,0,490],
[472,507,461,531,489,519,462,467,486,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,479,480,481,488,478,491,499,504,485],
[515,0,477,460,458,472,483,475,477,467,495],
[521,523,0,504,492,516,498,477,488,517,508],
[520,540,496,0,505,526,512,532,520,520,533],
[519,542,508,495,0,516,499,507,494,516,494],
[512,528,484,474,484,0,474,490,461,489,493],
[522,517,502,488,501,526,0,506,481,500,519],
[509,525,523,468,493,510,494,0,470,484,515],
[501,523,512,480,506,539,519,530,0,532,527],
[496,533,483,480,484,511,500,516,468,0,489],
[515,505,492,467,506,507,481,485,473,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,458,519,493,463,487,487,471,487,520],
[515,0,502,528,525,494,514,512,499,495,491],
[542,498,0,531,528,510,518,540,499,513,538],
[481,472,469,0,500,481,478,474,460,464,495],
[507,475,472,500,0,485,477,470,482,473,471],
[537,506,490,519,515,0,532,532,500,527,523],
[513,486,482,522,523,468,0,496,501,475,518],
[513,488,460,526,530,468,504,0,472,520,505],
[529,501,501,540,518,500,499,528,0,513,490],
[513,505,487,536,527,473,525,480,487,0,512],
[480,509,462,505,529,477,482,495,510,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,574,586,571,507,497,558,587,532,547],
[514,0,462,652,527,548,622,495,612,566,534],
[426,538,0,524,493,547,476,448,617,535,562],
[414,348,476,0,404,428,499,378,555,560,557],
[429,473,507,596,0,547,491,493,591,493,565],
[493,452,453,572,453,0,489,418,556,552,562],
[503,378,524,501,509,511,0,428,562,494,533],
[442,505,552,622,507,582,572,0,694,524,554],
[413,388,383,445,409,444,438,306,0,439,476],
[468,434,465,440,507,448,506,476,561,0,571],
[453,466,438,443,435,438,467,446,524,429,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,517,499,514,528,492,516,517,519,513],
[486,0,495,498,458,515,469,488,500,525,518],
[483,505,0,491,488,494,499,506,501,510,502],
[501,502,509,0,472,518,482,503,527,518,511],
[486,542,512,528,0,528,515,509,515,515,533],
[472,485,506,482,472,0,485,458,512,510,512],
[508,531,501,518,485,515,0,496,518,507,524],
[484,512,494,497,491,542,504,0,492,531,515],
[483,500,499,473,485,488,482,508,0,494,486],
[481,475,490,482,485,490,493,469,506,0,503],
[487,482,498,489,467,488,476,485,514,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,513,511,491,522,502,524,524,525,530],
[459,0,455,470,461,472,470,496,501,482,473],
[487,545,0,510,506,535,507,525,514,491,501],
[489,530,490,0,493,522,512,498,521,517,506],
[509,539,494,507,0,503,480,503,524,521,507],
[478,528,465,478,497,0,520,511,504,495,503],
[498,530,493,488,520,480,0,510,519,498,516],
[476,504,475,502,497,489,490,0,506,483,501],
[476,499,486,479,476,496,481,494,0,505,491],
[475,518,509,483,479,505,502,517,495,0,511],
[470,527,499,494,493,497,484,499,509,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,505,501,474,494,515,512,515,546,516],
[501,0,482,497,481,474,472,500,495,518,514],
[495,518,0,481,474,479,494,518,520,517,497],
[499,503,519,0,479,453,487,505,519,523,490],
[526,519,526,521,0,487,486,535,523,546,529],
[506,526,521,547,513,0,502,511,500,534,512],
[485,528,506,513,514,498,0,537,515,538,539],
[488,500,482,495,465,489,463,0,502,508,477],
[485,505,480,481,477,500,485,498,0,511,495],
[454,482,483,477,454,466,462,492,489,0,504],
[484,486,503,510,471,488,461,523,505,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,464,508,483,530,492,497,490,516,498],
[503,0,483,514,480,503,483,493,476,490,474],
[536,517,0,531,512,541,503,513,497,533,495],
[492,486,469,0,499,493,467,480,502,498,510],
[517,520,488,501,0,532,489,507,501,549,507],
[470,497,459,507,468,0,471,483,461,521,500],
[508,517,497,533,511,529,0,505,506,535,512],
[503,507,487,520,493,517,495,0,484,508,494],
[510,524,503,498,499,539,494,516,0,548,523],
[484,510,467,502,451,479,465,492,452,0,478],
[502,526,505,490,493,500,488,506,477,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,569,505,506,566,531,506,548,539,466],
[497,0,480,446,489,544,512,540,538,501,455],
[431,520,0,505,486,572,491,493,499,500,502],
[495,554,495,0,478,571,524,524,537,563,496],
[494,511,514,522,0,538,533,557,494,500,457],
[434,456,428,429,462,0,439,450,431,502,442],
[469,488,509,476,467,561,0,475,419,478,493],
[494,460,507,476,443,550,525,0,481,523,490],
[452,462,501,463,506,569,581,519,0,499,499],
[461,499,500,437,500,498,522,477,501,0,451],
[534,545,498,504,543,558,507,510,501,549,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,481,472,507,527,493,521,495,491,470],
[519,0,474,520,517,502,478,514,497,493,511],
[519,526,0,496,504,514,479,537,507,496,541],
[528,480,504,0,481,523,511,525,501,466,540],
[493,483,496,519,0,511,476,480,491,520,487],
[473,498,486,477,489,0,496,498,515,466,483],
[507,522,521,489,524,504,0,517,521,513,507],
[479,486,463,475,520,502,483,0,496,488,525],
[505,503,493,499,509,485,479,504,0,474,492],
[509,507,504,534,480,534,487,512,526,0,515],
[530,489,459,460,513,517,493,475,508,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,514,452,474,455,501,474,458,491,505],
[485,0,508,468,541,563,506,513,532,488,438],
[486,492,0,487,452,491,488,467,465,478,388],
[548,532,513,0,463,509,478,470,558,486,518],
[526,459,548,537,0,508,486,452,504,556,439],
[545,437,509,491,492,0,452,458,428,417,425],
[499,494,512,522,514,548,0,510,520,499,478],
[526,487,533,530,548,542,490,0,520,497,491],
[542,468,535,442,496,572,480,480,0,514,454],
[509,512,522,514,444,583,501,503,486,0,473],
[495,562,612,482,561,575,522,509,546,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,523,604,559,565,508,558,532,515,512],
[502,0,587,623,499,580,537,546,592,506,593],
[477,413,0,548,479,546,458,517,530,531,529],
[396,377,452,0,419,429,465,490,473,454,449],
[441,501,521,581,0,578,494,552,590,470,582],
[435,420,454,571,422,0,470,484,457,470,465],
[492,463,542,535,506,530,0,558,516,466,525],
[442,454,483,510,448,516,442,0,503,455,499],
[468,408,470,527,410,543,484,497,0,429,524],
[485,494,469,546,530,530,534,545,571,0,528],
[488,407,471,551,418,535,475,501,476,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,525,516,523,469,493,504,507,502,512],
[517,0,533,503,531,480,499,502,524,529,508],
[475,467,0,496,505,461,492,481,489,486,478],
[484,497,504,0,523,466,480,470,493,477,490],
[477,469,495,477,0,444,476,457,508,462,473],
[531,520,539,534,556,0,512,508,519,506,483],
[507,501,508,520,524,488,0,485,519,507,492],
[496,498,519,530,543,492,515,0,515,490,477],
[493,476,511,507,492,481,481,485,0,483,496],
[498,471,514,523,538,494,493,510,517,0,493],
[488,492,522,510,527,517,508,523,504,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,567,573,496,514,572,439,422,527,629,488],
[433,0,449,537,395,421,457,457,364,633,399],
[427,551,0,530,435,422,504,438,391,541,389],
[504,463,470,0,441,489,356,425,286,679,374],
[486,605,565,559,0,532,533,524,443,577,475],
[428,579,578,511,468,0,418,420,367,513,398],
[561,543,496,644,467,582,0,508,397,634,462],
[578,543,562,575,476,580,492,0,390,652,525],
[473,636,609,714,557,633,603,610,0,659,500],
[371,367,459,321,423,487,366,348,341,0,386],
[512,601,611,626,525,602,538,475,500,614,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,529,519,471,522,450,484,477,472,512],
[484,0,496,437,453,495,424,489,496,445,493],
[471,504,0,450,469,548,453,441,459,400,471],
[481,563,550,0,484,550,492,529,530,499,526],
[529,547,531,516,0,517,492,504,515,516,484],
[478,505,452,450,483,0,432,486,518,501,442],
[550,576,547,508,508,568,0,506,577,470,492],
[516,511,559,471,496,514,494,0,531,460,481],
[523,504,541,470,485,482,423,469,0,503,468],
[528,555,600,501,484,499,530,540,497,0,513],
[488,507,529,474,516,558,508,519,532,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,512,523,493,501,489,504,480,505,509],
[493,0,492,521,514,512,454,484,491,480,484],
[488,508,0,504,521,526,479,510,470,530,542],
[477,479,496,0,504,483,470,494,458,496,513],
[507,486,479,496,0,504,450,489,485,528,488],
[499,488,474,517,496,0,459,492,497,462,488],
[511,546,521,530,550,541,0,492,511,517,532],
[496,516,490,506,511,508,508,0,496,529,486],
[520,509,530,542,515,503,489,504,0,466,507],
[495,520,470,504,472,538,483,471,534,0,522],
[491,516,458,487,512,512,468,514,493,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,521,522,486,484,498,461,476,504,473],
[500,0,518,530,504,466,529,454,500,555,485],
[479,482,0,510,482,467,491,422,458,526,478],
[478,470,490,0,492,490,513,473,482,547,469],
[514,496,518,508,0,479,521,462,462,521,482],
[516,534,533,510,521,0,497,491,536,551,503],
[502,471,509,487,479,503,0,482,470,527,451],
[539,546,578,527,538,509,518,0,493,552,517],
[524,500,542,518,538,464,530,507,0,562,492],
[496,445,474,453,479,449,473,448,438,0,461],
[527,515,522,531,518,497,549,483,508,539,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,501,477,525,499,500,516,495,511,516],
[497,0,510,482,485,517,505,505,484,500,509],
[499,490,0,497,506,498,515,529,487,493,494],
[523,518,503,0,509,500,516,519,507,502,518],
[475,515,494,491,0,504,483,518,474,498,499],
[501,483,502,500,496,0,498,512,462,499,476],
[500,495,485,484,517,502,0,509,481,511,508],
[484,495,471,481,482,488,491,0,465,486,482],
[505,516,513,493,526,538,519,535,0,509,512],
[489,500,507,498,502,501,489,514,491,0,522],
[484,491,506,482,501,524,492,518,488,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,493,479,457,461,424,472,451,481,485],
[541,0,523,505,497,520,456,504,510,496,494],
[507,477,0,460,458,446,476,479,490,459,472],
[521,495,540,0,508,477,489,518,494,484,489],
[543,503,542,492,0,516,504,536,512,505,502],
[539,480,554,523,484,0,480,497,490,492,478],
[576,544,524,511,496,520,0,515,492,502,515],
[528,496,521,482,464,503,485,0,529,480,518],
[549,490,510,506,488,510,508,471,0,533,482],
[519,504,541,516,495,508,498,520,467,0,487],
[515,506,528,511,498,522,485,482,518,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,488,533,500,465,480,492,476,464,496],
[498,0,452,511,504,464,458,472,476,486,502],
[512,548,0,503,514,459,486,496,494,483,511],
[467,489,497,0,479,454,459,501,503,490,470],
[500,496,486,521,0,498,505,481,473,479,522],
[535,536,541,546,502,0,498,559,484,506,530],
[520,542,514,541,495,502,0,501,519,527,518],
[508,528,504,499,519,441,499,0,506,487,543],
[524,524,506,497,527,516,481,494,0,498,492],
[536,514,517,510,521,494,473,513,502,0,517],
[504,498,489,530,478,470,482,457,508,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,402,500,604,476,477,384,338,454,362,652],
[598,0,561,731,557,574,531,418,648,475,844],
[500,439,0,563,455,500,529,451,529,457,611],
[396,269,437,0,345,530,467,445,511,477,440],
[524,443,545,655,0,489,500,379,694,397,737],
[523,426,500,470,511,0,491,618,603,594,570],
[616,469,471,533,500,509,0,377,606,490,604],
[662,582,549,555,621,382,623,0,564,450,672],
[546,352,471,489,306,397,394,436,0,395,631],
[638,525,543,523,603,406,510,550,605,0,557],
[348,156,389,560,263,430,396,328,369,443,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,628,906,453,784,722,1000,506,784,906,609],
[372,0,400,278,278,494,494,278,278,400,372],
[94,600,0,453,878,600,425,425,609,784,703],
[547,722,547,0,878,722,547,425,825,825,825],
[216,722,122,122,0,722,547,94,453,453,547],
[278,506,400,278,278,0,609,278,609,609,609],
[0,506,575,453,453,391,0,0,453,453,278],
[494,722,575,575,906,722,1000,0,906,906,825],
[216,722,391,175,547,391,547,94,0,391,372],
[94,600,216,175,547,391,547,94,609,0,703],
[391,628,297,175,453,391,722,175,628,297,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,485,527,479,561,531,545,512,489,539],
[512,0,520,517,486,540,522,520,501,523,526],
[515,480,0,523,493,565,503,541,500,520,539],
[473,483,477,0,489,520,502,488,496,499,524],
[521,514,507,511,0,549,524,498,492,504,537],
[439,460,435,480,451,0,455,488,454,423,493],
[469,478,497,498,476,545,0,483,481,502,501],
[455,480,459,512,502,512,517,0,501,526,543],
[488,499,500,504,508,546,519,499,0,497,513],
[511,477,480,501,496,577,498,474,503,0,484],
[461,474,461,476,463,507,499,457,487,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,377,377,1000,824,377,1000,377,377,0,824],
[623,0,623,623,824,623,623,623,447,623,623],
[623,377,0,623,824,623,623,623,447,447,623],
[0,377,377,0,824,377,824,0,377,0,377],
[176,176,176,176,0,176,176,176,0,176,176],
[623,377,377,623,824,0,623,623,824,447,447],
[0,377,377,176,824,377,0,0,377,0,0],
[623,377,377,1000,824,377,1000,0,824,0,824],
[623,553,553,623,1000,176,623,176,0,176,623],
[1000,377,553,1000,824,553,1000,1000,824,0,1000],
[176,377,377,623,824,553,1000,176,377,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,519,508,500,521,487,497,492,522,505],
[515,0,507,496,473,500,482,485,496,511,466],
[481,493,0,459,491,481,434,471,489,521,484],
[492,504,541,0,495,532,484,508,486,538,506],
[500,527,509,505,0,511,509,504,495,513,555],
[479,500,519,468,489,0,474,488,483,522,505],
[513,518,566,516,491,526,0,518,528,522,513],
[503,515,529,492,496,512,482,0,515,529,487],
[508,504,511,514,505,517,472,485,0,521,492],
[478,489,479,462,487,478,478,471,479,0,472],
[495,534,516,494,445,495,487,513,508,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,488,541,457,452,515,509,480,530,479],
[519,0,499,524,508,520,491,557,529,513,466],
[512,501,0,535,505,481,506,523,503,533,493],
[459,476,465,0,497,500,500,528,463,553,491],
[543,492,495,503,0,513,516,507,513,546,517],
[548,480,519,500,487,0,507,508,478,546,481],
[485,509,494,500,484,493,0,554,477,530,506],
[491,443,477,472,493,492,446,0,479,551,482],
[520,471,497,537,487,522,523,521,0,523,511],
[470,487,467,447,454,454,470,449,477,0,444],
[521,534,507,509,483,519,494,518,489,556,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,424,425,491,478,487,442,477,471,472,508],
[576,0,505,540,524,516,500,502,540,480,525],
[575,495,0,548,519,475,522,519,503,488,562],
[509,460,452,0,503,478,482,494,468,483,469],
[522,476,481,497,0,476,484,484,472,498,533],
[513,484,525,522,524,0,508,538,502,527,563],
[558,500,478,518,516,492,0,496,459,505,517],
[523,498,481,506,516,462,504,0,495,517,547],
[529,460,497,532,528,498,541,505,0,500,552],
[528,520,512,517,502,473,495,483,500,0,543],
[492,475,438,531,467,437,483,453,448,457,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,517,507,484,515,509,514,506,527,486],
[483,0,480,477,474,477,462,486,482,465,476],
[483,520,0,490,475,492,486,494,481,498,491],
[493,523,510,0,500,502,503,503,500,500,487],
[516,526,525,500,0,519,477,510,494,515,510],
[485,523,508,498,481,0,467,474,491,493,470],
[491,538,514,497,523,533,0,510,513,502,508],
[486,514,506,497,490,526,490,0,509,504,520],
[494,518,519,500,506,509,487,491,0,504,475],
[473,535,502,500,485,507,498,496,496,0,506],
[514,524,509,513,490,530,492,480,525,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,410,491,426,533,368,501,516,566,478],
[506,0,578,496,527,541,468,466,509,552,486],
[590,422,0,492,373,516,457,405,453,586,500],
[509,504,508,0,420,493,379,407,463,557,437],
[574,473,627,580,0,570,462,492,476,619,511],
[467,459,484,507,430,0,437,410,482,583,505],
[632,532,543,621,538,563,0,479,554,647,484],
[499,534,595,593,508,590,521,0,427,670,537],
[484,491,547,537,524,518,446,573,0,610,496],
[434,448,414,443,381,417,353,330,390,0,450],
[522,514,500,563,489,495,516,463,504,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,491,479,504,480,471,456,514,473,526],
[503,0,477,474,441,444,496,487,529,493,469],
[509,523,0,504,450,481,496,477,498,511,529],
[521,526,496,0,457,480,434,488,454,492,484],
[496,559,550,543,0,523,507,514,532,505,510],
[520,556,519,520,477,0,463,511,537,516,499],
[529,504,504,566,493,537,0,496,486,549,533],
[544,513,523,512,486,489,504,0,517,512,516],
[486,471,502,546,468,463,514,483,0,517,494],
[527,507,489,508,495,484,451,488,483,0,501],
[474,531,471,516,490,501,467,484,506,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,516,484,517,539,506,524,536,521,532],
[490,0,484,493,507,512,479,530,513,498,516],
[484,516,0,481,486,525,492,533,508,510,536],
[516,507,519,0,512,527,486,511,523,525,539],
[483,493,514,488,0,510,459,524,503,481,535],
[461,488,475,473,490,0,455,483,482,481,513],
[494,521,508,514,541,545,0,526,539,532,563],
[476,470,467,489,476,517,474,0,496,480,517],
[464,487,492,477,497,518,461,504,0,497,524],
[479,502,490,475,519,519,468,520,503,0,543],
[468,484,464,461,465,487,437,483,476,457,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,512,505,485,517,502,492,485,469,513],
[492,0,485,492,471,503,501,483,497,490,497],
[488,515,0,490,504,501,502,494,476,480,513],
[495,508,510,0,492,490,507,475,461,486,503],
[515,529,496,508,0,512,533,486,511,528,529],
[483,497,499,510,488,0,510,458,493,470,491],
[498,499,498,493,467,490,0,489,485,507,518],
[508,517,506,525,514,542,511,0,509,479,538],
[515,503,524,539,489,507,515,491,0,521,533],
[531,510,520,514,472,530,493,521,479,0,524],
[487,503,487,497,471,509,482,462,467,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,403,407,454,512,395,598,485,599,454],
[489,0,458,524,521,529,387,624,398,645,387],
[597,542,0,521,559,521,361,776,466,520,349],
[593,476,479,0,629,576,441,831,615,664,531],
[546,479,441,371,0,459,339,727,547,599,313],
[488,471,479,424,541,0,421,516,331,600,477],
[605,613,639,559,661,579,0,775,509,696,434],
[402,376,224,169,273,484,225,0,291,430,266],
[515,602,534,385,453,669,491,709,0,663,430],
[401,355,480,336,401,400,304,570,337,0,322],
[546,613,651,469,687,523,566,734,570,678,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,466,498,443,481,446,492,483,456,483],
[482,0,456,528,484,480,494,514,482,491,510],
[534,544,0,557,544,559,496,500,522,496,496],
[502,472,443,0,483,459,445,457,478,437,448],
[557,516,456,517,0,551,512,549,512,534,543],
[519,520,441,541,449,0,459,463,443,509,431],
[554,506,504,555,488,541,0,464,507,518,508],
[508,486,500,543,451,537,536,0,539,535,512],
[517,518,478,522,488,557,493,461,0,455,485],
[544,509,504,563,466,491,482,465,545,0,483],
[517,490,504,552,457,569,492,488,515,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,474,477,498,489,490,476,468,519,503],
[500,0,506,483,521,521,513,482,495,517,493],
[526,494,0,519,533,493,507,482,505,528,484],
[523,517,481,0,524,509,508,512,497,524,521],
[502,479,467,476,0,500,477,464,479,495,474],
[511,479,507,491,500,0,487,477,497,512,494],
[510,487,493,492,523,513,0,487,503,491,510],
[524,518,518,488,536,523,513,0,505,529,512],
[532,505,495,503,521,503,497,495,0,524,495],
[481,483,472,476,505,488,509,471,476,0,485],
[497,507,516,479,526,506,490,488,505,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,511,459,527,487,470,505,509,478,512],
[475,0,472,467,480,497,451,489,484,463,478],
[489,528,0,516,505,528,494,516,487,517,500],
[541,533,484,0,527,519,522,513,522,501,515],
[473,520,495,473,0,505,496,487,487,491,469],
[513,503,472,481,495,0,510,503,494,512,524],
[530,549,506,478,504,490,0,496,556,478,520],
[495,511,484,487,513,497,504,0,510,494,495],
[491,516,513,478,513,506,444,490,0,491,478],
[522,537,483,499,509,488,522,506,509,0,514],
[488,522,500,485,531,476,480,505,522,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,477,481,511,493,505,492,537,500,507],
[504,0,492,511,534,535,506,511,525,514,489],
[523,508,0,519,519,517,493,491,528,511,494],
[519,489,481,0,520,486,501,463,485,492,482],
[489,466,481,480,0,483,501,478,482,504,484],
[507,465,483,514,517,0,496,491,493,500,502],
[495,494,507,499,499,504,0,465,503,530,498],
[508,489,509,537,522,509,535,0,521,532,501],
[463,475,472,515,518,507,497,479,0,496,473],
[500,486,489,508,496,500,470,468,504,0,495],
[493,511,506,518,516,498,502,499,527,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,450,482,419,423,476,529,473,470,460,453],
[550,0,485,469,467,498,485,509,489,481,470],
[518,515,0,481,458,470,508,483,521,473,524],
[581,531,519,0,485,508,519,555,497,539,550],
[577,533,542,515,0,533,548,553,496,491,554],
[524,502,530,492,467,0,542,546,554,500,526],
[471,515,492,481,452,458,0,501,471,460,462],
[527,491,517,445,447,454,499,0,470,483,438],
[530,511,479,503,504,446,529,530,0,512,513],
[540,519,527,461,509,500,540,517,488,0,519],
[547,530,476,450,446,474,538,562,487,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,487,502,516,487,471,479,487,501,470],
[515,0,508,520,549,505,491,510,520,501,509],
[513,492,0,515,508,494,496,484,492,491,494],
[498,480,485,0,507,507,502,494,496,494,484],
[484,451,492,493,0,472,458,486,483,493,464],
[513,495,506,493,528,0,503,501,493,500,492],
[529,509,504,498,542,497,0,506,520,508,508],
[521,490,516,506,514,499,494,0,489,487,490],
[513,480,508,504,517,507,480,511,0,487,476],
[499,499,509,506,507,500,492,513,513,0,483],
[530,491,506,516,536,508,492,510,524,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,417,424,593,475,566,442,468,435,425,452],
[583,0,551,583,569,523,492,511,429,509,528],
[576,449,0,600,522,484,613,506,508,515,503],
[407,417,400,0,448,486,484,402,337,339,432],
[525,431,478,552,0,522,505,468,425,479,396],
[434,477,516,514,478,0,517,496,427,449,451],
[558,508,387,516,495,483,0,497,413,446,472],
[532,489,494,598,532,504,503,0,489,459,473],
[565,571,492,663,575,573,587,511,0,507,552],
[575,491,485,661,521,551,554,541,493,0,471],
[548,472,497,568,604,549,528,527,448,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,492,489,527,477,518,512,459,534,510],
[517,0,483,518,536,497,505,532,513,514,488],
[508,517,0,497,513,491,512,551,498,511,521],
[511,482,503,0,539,484,501,538,503,511,522],
[473,464,487,461,0,483,484,482,444,486,492],
[523,503,509,516,517,0,539,530,495,523,533],
[482,495,488,499,516,461,0,501,480,493,539],
[488,468,449,462,518,470,499,0,479,506,501],
[541,487,502,497,556,505,520,521,0,519,539],
[466,486,489,489,514,477,507,494,481,0,506],
[490,512,479,478,508,467,461,499,461,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,495,489,497,498,501,504,497,495,518],
[502,0,521,516,494,519,514,498,511,533,528],
[505,479,0,495,488,531,519,485,502,509,504],
[511,484,505,0,497,514,515,505,491,506,496],
[503,506,512,503,0,511,519,488,497,498,502],
[502,481,469,486,489,0,504,494,482,499,503],
[499,486,481,485,481,496,0,493,495,490,480],
[496,502,515,495,512,506,507,0,510,509,506],
[503,489,498,509,503,518,505,490,0,512,498],
[505,467,491,494,502,501,510,491,488,0,480],
[482,472,496,504,498,497,520,494,502,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,511,505,518,527,532,507,501,513,485],
[535,0,552,492,507,509,472,500,477,484,515],
[489,448,0,509,500,501,527,512,482,473,487],
[495,508,491,0,489,516,520,478,495,524,496],
[482,493,500,511,0,512,499,473,507,499,499],
[473,491,499,484,488,0,484,455,452,477,435],
[468,528,473,480,501,516,0,445,482,474,492],
[493,500,488,522,527,545,555,0,464,511,473],
[499,523,518,505,493,548,518,536,0,534,519],
[487,516,527,476,501,523,526,489,466,0,515],
[515,485,513,504,501,565,508,527,481,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,520,557,506,492,546,518,534,509,479],
[511,0,474,479,501,469,522,475,507,511,511],
[480,526,0,515,497,502,547,477,517,524,503],
[443,521,485,0,512,445,517,480,499,511,483],
[494,499,503,488,0,465,522,497,471,497,460],
[508,531,498,555,535,0,525,499,479,519,486],
[454,478,453,483,478,475,0,470,448,479,469],
[482,525,523,520,503,501,530,0,504,522,522],
[466,493,483,501,529,521,552,496,0,491,499],
[491,489,476,489,503,481,521,478,509,0,465],
[521,489,497,517,540,514,531,478,501,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,508,509,508,509,495,491,500,502,509],
[491,0,502,482,492,508,505,500,490,488,493],
[492,498,0,517,498,484,471,502,482,492,490],
[491,518,483,0,518,505,491,522,500,494,504],
[492,508,502,482,0,504,456,498,515,503,505],
[491,492,516,495,496,0,500,491,491,490,499],
[505,495,529,509,544,500,0,523,507,499,507],
[509,500,498,478,502,509,477,0,494,496,498],
[500,510,518,500,485,509,493,506,0,487,515],
[498,512,508,506,497,510,501,504,513,0,505],
[491,507,510,496,495,501,493,502,485,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,462,470,463,498,494,495,493,485,490],
[543,0,503,476,503,506,497,502,513,492,501],
[538,497,0,530,503,539,525,513,517,514,522],
[530,524,470,0,523,521,522,494,494,523,520],
[537,497,497,477,0,497,484,490,480,511,484],
[502,494,461,479,503,0,494,498,475,478,497],
[506,503,475,478,516,506,0,510,485,496,491],
[505,498,487,506,510,502,490,0,480,490,510],
[507,487,483,506,520,525,515,520,0,516,513],
[515,508,486,477,489,522,504,510,484,0,504],
[510,499,478,480,516,503,509,490,487,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,518,523,501,513,530,494,508,532,515],
[464,0,500,503,487,497,506,463,514,511,502],
[482,500,0,482,472,504,513,480,502,504,489],
[477,497,518,0,484,518,520,483,505,493,510],
[499,513,528,516,0,531,535,514,524,536,526],
[487,503,496,482,469,0,495,472,505,497,490],
[470,494,487,480,465,505,0,456,481,495,491],
[506,537,520,517,486,528,544,0,523,532,525],
[492,486,498,495,476,495,519,477,0,499,490],
[468,489,496,507,464,503,505,468,501,0,498],
[485,498,511,490,474,510,509,475,510,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,539,552,536,481,511,529,507,534,502],
[495,0,500,503,515,502,512,523,511,529,486],
[461,500,0,502,509,463,465,496,481,512,466],
[448,497,498,0,492,501,499,521,519,474,480],
[464,485,491,508,0,460,480,465,494,493,453],
[519,498,537,499,540,0,529,526,515,532,508],
[489,488,535,501,520,471,0,490,510,519,487],
[471,477,504,479,535,474,510,0,495,476,494],
[493,489,519,481,506,485,490,505,0,492,479],
[466,471,488,526,507,468,481,524,508,0,493],
[498,514,534,520,547,492,513,506,521,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,494,515,510,509,526,524,532,528,486],
[498,0,505,535,525,515,539,519,514,523,509],
[506,495,0,511,487,489,510,505,493,543,493],
[485,465,489,0,491,498,514,505,483,499,483],
[490,475,513,509,0,508,533,524,494,500,496],
[491,485,511,502,492,0,520,508,510,515,493],
[474,461,490,486,467,480,0,496,486,488,456],
[476,481,495,495,476,492,504,0,478,519,472],
[468,486,507,517,506,490,514,522,0,519,484],
[472,477,457,501,500,485,512,481,481,0,479],
[514,491,507,517,504,507,544,528,516,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,471,503,506,500,504,477,484,511,494],
[495,0,480,512,492,505,526,501,490,519,541],
[529,520,0,509,524,541,517,513,500,503,532],
[497,488,491,0,511,530,509,484,501,498,522],
[494,508,476,489,0,504,502,506,493,524,534],
[500,495,459,470,496,0,504,490,481,495,502],
[496,474,483,491,498,496,0,489,490,486,515],
[523,499,487,516,494,510,511,0,505,487,525],
[516,510,500,499,507,519,510,495,0,522,547],
[489,481,497,502,476,505,514,513,478,0,497],
[506,459,468,478,466,498,485,475,453,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,521,459,473,480,483,475,486,478,505],
[467,0,471,430,474,441,456,484,463,487,489],
[479,529,0,414,498,435,465,500,518,470,506],
[541,570,586,0,500,535,551,557,557,563,604],
[527,526,502,500,0,478,494,503,519,474,540],
[520,559,565,465,522,0,508,537,519,543,568],
[517,544,535,449,506,492,0,495,522,491,538],
[525,516,500,443,497,463,505,0,500,504,545],
[514,537,482,443,481,481,478,500,0,488,560],
[522,513,530,437,526,457,509,496,512,0,529],
[495,511,494,396,460,432,462,455,440,471,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,488,542,521,506,505,530,552,488,494],
[461,0,465,494,498,461,450,489,519,457,509],
[512,535,0,515,542,496,490,542,540,513,517],
[458,506,485,0,466,456,469,516,524,490,453],
[479,502,458,534,0,479,468,514,523,472,520],
[494,539,504,544,521,0,512,527,549,495,511],
[495,550,510,531,532,488,0,562,580,499,514],
[470,511,458,484,486,473,438,0,551,477,482],
[448,481,460,476,477,451,420,449,0,458,482],
[512,543,487,510,528,505,501,523,542,0,502],
[506,491,483,547,480,489,486,518,518,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,490,498,484,460,489,534,480,512,475],
[494,0,502,504,547,505,475,526,505,539,530],
[510,498,0,472,525,507,499,532,500,507,501],
[502,496,528,0,485,497,461,503,501,505,491],
[516,453,475,515,0,530,509,503,477,475,468],
[540,495,493,503,470,0,535,501,514,517,489],
[511,525,501,539,491,465,0,482,515,507,477],
[466,474,468,497,497,499,518,0,514,529,461],
[520,495,500,499,523,486,485,486,0,513,499],
[488,461,493,495,525,483,493,471,487,0,483],
[525,470,499,509,532,511,523,539,501,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,524,506,510,499,501,491,525,517,532],
[487,0,510,510,513,523,516,508,527,511,503],
[476,490,0,479,489,474,473,483,508,489,499],
[494,490,521,0,499,498,485,492,526,500,516],
[490,487,511,501,0,497,505,477,500,513,511],
[501,477,526,502,503,0,507,504,515,535,511],
[499,484,527,515,495,493,0,490,512,509,520],
[509,492,517,508,523,496,510,0,542,525,531],
[475,473,492,474,500,485,488,458,0,489,481],
[483,489,511,500,487,465,491,475,511,0,527],
[468,497,501,484,489,489,480,469,519,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,479,480,440,443,418,396,470,386,504],
[534,0,601,506,479,500,494,520,503,547,530],
[521,399,0,420,458,466,430,368,468,420,475],
[520,494,580,0,466,440,468,485,475,467,499],
[560,521,542,534,0,509,487,471,477,460,531],
[557,500,534,560,491,0,489,444,448,519,500],
[582,506,570,532,513,511,0,468,448,470,535],
[604,480,632,515,529,556,532,0,542,510,534],
[530,497,532,525,523,552,552,458,0,458,550],
[614,453,580,533,540,481,530,490,542,0,513],
[496,470,525,501,469,500,465,466,450,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,492,486,462,531,564,445,493,414,543],
[472,0,483,432,441,496,539,398,427,464,521],
[508,517,0,542,488,505,540,448,523,461,539],
[514,568,458,0,420,544,498,462,467,485,535],
[538,559,512,580,0,521,531,505,497,469,561],
[469,504,495,456,479,0,503,455,458,497,497],
[436,461,460,502,469,497,0,394,391,457,515],
[555,602,552,538,495,545,606,0,553,525,584],
[507,573,477,533,503,542,609,447,0,508,563],
[586,536,539,515,531,503,543,475,492,0,563],
[457,479,461,465,439,503,485,416,437,437,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,498,502,502,504,516,505,521,493,490],
[486,0,477,483,479,495,522,492,479,474,493],
[502,523,0,514,486,504,529,502,514,511,514],
[498,517,486,0,493,503,513,501,515,487,506],
[498,521,514,507,0,533,519,514,503,496,524],
[496,505,496,497,467,0,505,480,495,474,492],
[484,478,471,487,481,495,0,475,472,466,490],
[495,508,498,499,486,520,525,0,505,514,485],
[479,521,486,485,497,505,528,495,0,494,477],
[507,526,489,513,504,526,534,486,506,0,507],
[510,507,486,494,476,508,510,515,523,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,518,484,520,481,522,512,506,521,486],
[471,0,519,506,544,480,532,516,517,500,507],
[482,481,0,461,528,493,523,510,496,517,507],
[516,494,539,0,557,523,542,533,511,539,539],
[480,456,472,443,0,461,506,508,498,476,507],
[519,520,507,477,539,0,542,515,523,520,497],
[478,468,477,458,494,458,0,486,484,481,475],
[488,484,490,467,492,485,514,0,490,507,477],
[494,483,504,489,502,477,516,510,0,492,482],
[479,500,483,461,524,480,519,493,508,0,487],
[514,493,493,461,493,503,525,523,518,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,494,488,519,481,530,507,467,466,484],
[492,0,481,486,492,489,445,415,477,463,481],
[506,519,0,497,540,505,429,457,472,525,516],
[512,514,503,0,516,517,485,511,503,514,510],
[481,508,460,484,0,453,447,473,461,468,462],
[519,511,495,483,547,0,510,478,467,550,469],
[470,555,571,515,553,490,0,488,468,538,481],
[493,585,543,489,527,522,512,0,480,487,547],
[533,523,528,497,539,533,532,520,0,478,519],
[534,537,475,486,532,450,462,513,522,0,492],
[516,519,484,490,538,531,519,453,481,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,519,537,519,509,508,509,509,497,543],
[482,0,512,509,498,488,489,503,491,497,513],
[481,488,0,499,490,498,480,483,497,468,513],
[463,491,501,0,510,500,461,478,504,480,499],
[481,502,510,490,0,497,501,498,519,496,533],
[491,512,502,500,503,0,488,488,508,471,530],
[492,511,520,539,499,512,0,504,495,506,540],
[491,497,517,522,502,512,496,0,514,486,509],
[491,509,503,496,481,492,505,486,0,493,526],
[503,503,532,520,504,529,494,514,507,0,528],
[457,487,487,501,467,470,460,491,474,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,490,512,499,518,509,514,487,477,518],
[519,0,492,515,495,508,500,534,502,494,543],
[510,508,0,507,497,525,526,509,512,521,534],
[488,485,493,0,490,508,515,515,484,505,516],
[501,505,503,510,0,515,502,517,491,498,510],
[482,492,475,492,485,0,518,510,486,501,522],
[491,500,474,485,498,482,0,515,485,486,521],
[486,466,491,485,483,490,485,0,479,515,502],
[513,498,488,516,509,514,515,521,0,517,540],
[523,506,479,495,502,499,514,485,483,0,501],
[482,457,466,484,490,478,479,498,460,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,512,499,496,509,497,490,494,487,484],
[498,0,499,481,499,493,510,487,500,481,475],
[488,501,0,490,486,471,505,474,504,488,481],
[501,519,510,0,499,484,520,492,500,508,510],
[504,501,514,501,0,505,519,483,516,493,513],
[491,507,529,516,495,0,502,499,502,522,513],
[503,490,495,480,481,498,0,484,486,485,503],
[510,513,526,508,517,501,516,0,516,506,496],
[506,500,496,500,484,498,514,484,0,481,497],
[513,519,512,492,507,478,515,494,519,0,505],
[516,525,519,490,487,487,497,504,503,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,505,522,511,526,524,518,499,530,554],
[479,0,499,469,518,508,483,535,499,551,505],
[495,501,0,535,499,502,542,567,490,555,518],
[478,531,465,0,492,517,506,528,509,514,512],
[489,482,501,508,0,533,505,520,470,536,509],
[474,492,498,483,467,0,503,543,500,531,492],
[476,517,458,494,495,497,0,534,458,534,478],
[482,465,433,472,480,457,466,0,448,572,488],
[501,501,510,491,530,500,542,552,0,589,507],
[470,449,445,486,464,469,466,428,411,0,428],
[446,495,482,488,491,508,522,512,493,572,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,436,487,478,471,475,522,451,476,502,473],
[564,0,533,515,496,520,547,490,511,533,484],
[513,467,0,505,478,474,507,478,476,512,489],
[522,485,495,0,487,499,521,461,487,494,487],
[529,504,522,513,0,500,541,508,499,544,509],
[525,480,526,501,500,0,542,497,510,551,501],
[478,453,493,479,459,458,0,454,483,479,453],
[549,510,522,539,492,503,546,0,516,498,485],
[524,489,524,513,501,490,517,484,0,501,484],
[498,467,488,506,456,449,521,502,499,0,472],
[527,516,511,513,491,499,547,515,516,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,494,504,521,524,530,495,505,496,509],
[483,0,494,475,483,497,497,524,483,499,455],
[506,506,0,503,524,504,535,537,507,490,504],
[496,525,497,0,511,487,558,513,487,499,503],
[479,517,476,489,0,473,506,492,467,500,469],
[476,503,496,513,527,0,538,523,488,484,449],
[470,503,465,442,494,462,0,505,458,474,459],
[505,476,463,487,508,477,495,0,490,470,507],
[495,517,493,513,533,512,542,510,0,496,496],
[504,501,510,501,500,516,526,530,504,0,492],
[491,545,496,497,531,551,541,493,504,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,450,459,498,488,458,487,460,481,471],
[513,0,487,466,505,484,455,507,469,487,500],
[550,513,0,469,518,490,501,513,470,524,479],
[541,534,531,0,497,490,492,511,493,532,521],
[502,495,482,503,0,483,451,472,483,503,506],
[512,516,510,510,517,0,478,512,493,524,499],
[542,545,499,508,549,522,0,505,513,516,519],
[513,493,487,489,528,488,495,0,485,523,495],
[540,531,530,507,517,507,487,515,0,527,540],
[519,513,476,468,497,476,484,477,473,0,491],
[529,500,521,479,494,501,481,505,460,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,445,494,478,490,433,477,476,486,498],
[485,0,493,517,493,449,484,463,483,491,527],
[555,507,0,533,514,506,527,550,516,556,438],
[506,483,467,0,470,532,503,509,516,497,457],
[522,507,486,530,0,518,524,568,511,551,466],
[510,551,494,468,482,0,514,524,555,518,499],
[567,516,473,497,476,486,0,543,506,560,482],
[523,537,450,491,432,476,457,0,507,478,455],
[524,517,484,484,489,445,494,493,0,494,448],
[514,509,444,503,449,482,440,522,506,0,488],
[502,473,562,543,534,501,518,545,552,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,516,516,494,498,517,496,519,507,508],
[472,0,497,490,460,483,505,496,501,475,486],
[484,503,0,521,506,494,502,484,518,498,483],
[484,510,479,0,489,501,524,491,510,502,491],
[506,540,494,511,0,515,508,520,541,520,532],
[502,517,506,499,485,0,520,501,508,498,498],
[483,495,498,476,492,480,0,483,515,498,496],
[504,504,516,509,480,499,517,0,513,525,511],
[481,499,482,490,459,492,485,487,0,483,479],
[493,525,502,498,480,502,502,475,517,0,479],
[492,514,517,509,468,502,504,489,521,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,549,516,523,500,548,486,533,502,541,494],
[451,0,491,503,484,505,468,530,482,510,480],
[484,509,0,504,501,532,490,520,466,546,520],
[477,497,496,0,507,512,479,514,462,488,513],
[500,516,499,493,0,527,475,494,502,517,489],
[452,495,468,488,473,0,469,502,449,475,494],
[514,532,510,521,525,531,0,554,469,532,488],
[467,470,480,486,506,498,446,0,456,499,471],
[498,518,534,538,498,551,531,544,0,529,527],
[459,490,454,512,483,525,468,501,471,0,495],
[506,520,480,487,511,506,512,529,473,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,478,462,488,495,509,490,527,469,497],
[499,0,476,467,470,481,488,464,504,485,479],
[522,524,0,481,481,499,493,475,508,506,498],
[538,533,519,0,515,526,519,522,505,491,501],
[512,530,519,485,0,514,506,492,534,509,504],
[505,519,501,474,486,0,507,485,524,499,482],
[491,512,507,481,494,493,0,491,511,491,496],
[510,536,525,478,508,515,509,0,537,516,515],
[473,496,492,495,466,476,489,463,0,492,491],
[531,515,494,509,491,501,509,484,508,0,535],
[503,521,502,499,496,518,504,485,509,465,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,493,498,507,483,455,504,502,470,497],
[488,0,476,511,526,442,460,488,491,466,488],
[507,524,0,541,517,456,488,528,511,506,485],
[502,489,459,0,484,436,427,502,447,459,449],
[493,474,483,516,0,443,455,490,470,467,471],
[517,558,544,564,557,0,506,550,507,486,496],
[545,540,512,573,545,494,0,562,522,530,565],
[496,512,472,498,510,450,438,0,540,496,500],
[498,509,489,553,530,493,478,460,0,475,510],
[530,534,494,541,533,514,470,504,525,0,527],
[503,512,515,551,529,504,435,500,490,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,500,512,495,516,474,507,492,496,497],
[507,0,531,520,504,482,498,532,489,511,471],
[500,469,0,477,468,479,464,490,491,501,462],
[488,480,523,0,527,490,496,544,503,509,506],
[505,496,532,473,0,477,482,516,509,517,494],
[484,518,521,510,523,0,506,541,512,551,492],
[526,502,536,504,518,494,0,544,534,531,510],
[493,468,510,456,484,459,456,0,460,495,473],
[508,511,509,497,491,488,466,540,0,506,481],
[504,489,499,491,483,449,469,505,494,0,483],
[503,529,538,494,506,508,490,527,519,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,522,506,527,505,504,518,536,488,505],
[476,0,519,517,514,505,503,513,531,517,491],
[478,481,0,482,511,477,480,468,491,466,477],
[494,483,518,0,527,523,501,535,527,498,500],
[473,486,489,473,0,483,502,496,512,455,479],
[495,495,523,477,517,0,469,513,516,492,475],
[496,497,520,499,498,531,0,516,509,488,497],
[482,487,532,465,504,487,484,0,519,488,494],
[464,469,509,473,488,484,491,481,0,464,472],
[512,483,534,502,545,508,512,512,536,0,485],
[495,509,523,500,521,525,503,506,528,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,471,456,451,474,467,461,447,452,461],
[505,0,468,477,505,488,458,507,454,449,479],
[529,532,0,523,517,478,487,535,501,487,532],
[544,523,477,0,526,483,473,531,494,487,471],
[549,495,483,474,0,481,506,463,455,453,493],
[526,512,522,517,519,0,494,502,449,490,545],
[533,542,513,527,494,506,0,502,492,464,487],
[539,493,465,469,537,498,498,0,493,462,461],
[553,546,499,506,545,551,508,507,0,504,504],
[548,551,513,513,547,510,536,538,496,0,513],
[539,521,468,529,507,455,513,539,496,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,558,566,575,494,507,479,444,508,576,557],
[442,0,592,536,462,487,561,559,514,582,579],
[434,408,0,532,492,484,447,537,398,569,571],
[425,464,468,0,478,469,385,543,467,553,523],
[506,538,508,522,0,479,412,596,490,549,559],
[493,513,516,531,521,0,504,591,502,525,471],
[521,439,553,615,588,496,0,623,591,538,588],
[556,441,463,457,404,409,377,0,507,397,341],
[492,486,602,533,510,498,409,493,0,529,504],
[424,418,431,447,451,475,462,603,471,0,326],
[443,421,429,477,441,529,412,659,496,674,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,508,508,500,520,512,507,522,502,485],
[474,0,470,472,485,483,495,490,501,487,474],
[492,530,0,493,512,511,527,499,499,513,481],
[492,528,507,0,511,515,484,505,515,529,485],
[500,515,488,489,0,513,493,488,523,514,480],
[480,517,489,485,487,0,495,482,504,496,474],
[488,505,473,516,507,505,0,488,503,506,478],
[493,510,501,495,512,518,512,0,527,507,509],
[478,499,501,485,477,496,497,473,0,497,483],
[498,513,487,471,486,504,494,493,503,0,488],
[515,526,519,515,520,526,522,491,517,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,501,505,498,496,485,495,469,475,492],
[510,0,482,531,500,496,488,504,472,475,502],
[499,518,0,509,484,494,473,494,488,487,494],
[495,469,491,0,458,483,482,486,465,466,478],
[502,500,516,542,0,479,481,518,485,484,493],
[504,504,506,517,521,0,499,522,477,495,491],
[515,512,527,518,519,501,0,533,512,505,497],
[505,496,506,514,482,478,467,0,479,472,490],
[531,528,512,535,515,523,488,521,0,518,521],
[525,525,513,534,516,505,495,528,482,0,505],
[508,498,506,522,507,509,503,510,479,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,526,504,525,513,506,496,507,516,518],
[534,0,520,515,539,566,508,464,522,557,529],
[474,480,0,542,538,526,525,500,496,542,509],
[496,485,458,0,523,515,479,476,513,530,500],
[475,461,462,477,0,483,434,440,487,534,484],
[487,434,474,485,517,0,477,489,501,520,493],
[494,492,475,521,566,523,0,460,502,538,510],
[504,536,500,524,560,511,540,0,519,540,528],
[493,478,504,487,513,499,498,481,0,552,511],
[484,443,458,470,466,480,462,460,448,0,470],
[482,471,491,500,516,507,490,472,489,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,494,518,484,517,481,524,444,499,469],
[496,0,538,538,516,553,528,521,479,508,483],
[506,462,0,535,455,519,490,545,468,486,496],
[482,462,465,0,449,474,475,498,462,476,463],
[516,484,545,551,0,515,514,538,498,493,486],
[483,447,481,526,485,0,505,502,468,478,500],
[519,472,510,525,486,495,0,519,515,483,477],
[476,479,455,502,462,498,481,0,415,439,462],
[556,521,532,538,502,532,485,585,0,558,497],
[501,492,514,524,507,522,517,561,442,0,488],
[531,517,504,537,514,500,523,538,503,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,509,466,527,487,507,485,505,486,475],
[538,0,520,529,542,486,545,504,524,516,515],
[491,480,0,496,498,482,522,482,504,492,498],
[534,471,504,0,523,503,533,513,539,515,502],
[473,458,502,477,0,459,489,467,498,471,473],
[513,514,518,497,541,0,536,511,532,506,519],
[493,455,478,467,511,464,0,447,495,486,484],
[515,496,518,487,533,489,553,0,548,518,505],
[495,476,496,461,502,468,505,452,0,470,460],
[514,484,508,485,529,494,514,482,530,0,487],
[525,485,502,498,527,481,516,495,540,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,523,477,482,509,467,453,457,501,513],
[498,0,559,500,486,529,484,516,475,512,524],
[477,441,0,472,458,513,473,431,425,496,473],
[523,500,528,0,508,550,486,499,497,497,493],
[518,514,542,492,0,539,499,470,482,497,521],
[491,471,487,450,461,0,475,488,465,492,531],
[533,516,527,514,501,525,0,508,460,498,511],
[547,484,569,501,530,512,492,0,524,491,506],
[543,525,575,503,518,535,540,476,0,521,514],
[499,488,504,503,503,508,502,509,479,0,521],
[487,476,527,507,479,469,489,494,486,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,492,501,515,516,494,512,485,503,486],
[530,0,488,519,515,528,475,526,518,504,514],
[508,512,0,509,496,518,494,504,519,499,512],
[499,481,491,0,491,504,475,497,497,473,497],
[485,485,504,509,0,506,492,482,493,500,495],
[484,472,482,496,494,0,466,493,494,478,494],
[506,525,506,525,508,534,0,490,508,504,510],
[488,474,496,503,518,507,510,0,518,498,486],
[515,482,481,503,507,506,492,482,0,500,501],
[497,496,501,527,500,522,496,502,500,0,493],
[514,486,488,503,505,506,490,514,499,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,505,483,475,469,455,386,423,334,522],
[526,0,728,437,616,510,647,549,428,544,550],
[495,272,0,380,398,426,534,331,367,301,485],
[517,563,620,0,549,622,572,499,529,524,438],
[525,384,602,451,0,376,577,472,449,475,456],
[531,490,574,378,624,0,756,409,412,364,547],
[545,353,466,428,423,244,0,453,414,383,538],
[614,451,669,501,528,591,547,0,456,471,503],
[577,572,633,471,551,588,586,544,0,530,431],
[666,456,699,476,525,636,617,529,470,0,503],
[478,450,515,562,544,453,462,497,569,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,578,575,594,430,505,492,388,554,405,593],
[422,0,355,658,477,500,495,478,437,215,582],
[425,645,0,712,553,564,532,479,538,358,537],
[406,342,288,0,279,443,291,407,345,281,434],
[570,523,447,721,0,602,589,448,584,373,579],
[495,500,436,557,398,0,597,446,595,350,463],
[508,505,468,709,411,403,0,368,327,501,549],
[612,522,521,593,552,554,632,0,531,456,602],
[446,563,462,655,416,405,673,469,0,319,469],
[595,785,642,719,627,650,499,544,681,0,704],
[407,418,463,566,421,537,451,398,531,296,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,456,448,467,420,471,496,465,421,484],
[546,0,513,522,500,518,529,574,527,527,561],
[544,487,0,506,476,493,493,548,509,473,518],
[552,478,494,0,481,494,506,548,485,468,501],
[533,500,524,519,0,528,537,545,500,511,542],
[580,482,507,506,472,0,543,547,517,507,538],
[529,471,507,494,463,457,0,547,466,474,512],
[504,426,452,452,455,453,453,0,446,463,471],
[535,473,491,515,500,483,534,554,0,480,516],
[579,473,527,532,489,493,526,537,520,0,516],
[516,439,482,499,458,462,488,529,484,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,506,515,497,523,500,505,522,510,507],
[469,0,504,537,496,523,483,499,520,494,482],
[494,496,0,519,493,505,508,544,551,480,485],
[485,463,481,0,490,520,466,451,528,475,453],
[503,504,507,510,0,497,477,491,527,480,475],
[477,477,495,480,503,0,490,492,524,485,482],
[500,517,492,534,523,510,0,506,546,536,487],
[495,501,456,549,509,508,494,0,514,533,482],
[478,480,449,472,473,476,454,486,0,457,444],
[490,506,520,525,520,515,464,467,543,0,477],
[493,518,515,547,525,518,513,518,556,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,519,485,505,505,494,443,498,499,489],
[521,0,538,502,520,500,497,500,515,513,495],
[481,462,0,504,497,495,491,464,504,477,480],
[515,498,496,0,527,513,493,458,508,487,498],
[495,480,503,473,0,506,506,474,501,479,473],
[495,500,505,487,494,0,483,468,521,501,490],
[506,503,509,507,494,517,0,492,502,503,490],
[557,500,536,542,526,532,508,0,533,523,516],
[502,485,496,492,499,479,498,467,0,496,488],
[501,487,523,513,521,499,497,477,504,0,481],
[511,505,520,502,527,510,510,484,512,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,568,499,578,535,477,497,521,512,558,479],
[432,0,473,534,483,471,447,466,441,454,457],
[501,527,0,572,522,530,526,486,524,520,516],
[422,466,428,0,476,469,470,450,440,498,436],
[465,517,478,524,0,445,460,475,463,471,460],
[523,529,470,531,555,0,517,479,523,505,489],
[503,553,474,530,540,483,0,471,453,553,480],
[479,534,514,550,525,521,529,0,473,532,483],
[488,559,476,560,537,477,547,527,0,506,504],
[442,546,480,502,529,495,447,468,494,0,491],
[521,543,484,564,540,511,520,517,496,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,487,512,516,493,492,492,511,479,501],
[518,0,504,498,506,489,487,500,486,476,514],
[513,496,0,500,517,471,483,497,499,488,513],
[488,502,500,0,504,505,485,503,511,494,512],
[484,494,483,496,0,500,476,478,499,475,508],
[507,511,529,495,500,0,487,493,492,510,532],
[508,513,517,515,524,513,0,491,503,505,522],
[508,500,503,497,522,507,509,0,500,514,516],
[489,514,501,489,501,508,497,500,0,486,513],
[521,524,512,506,525,490,495,486,514,0,527],
[499,486,487,488,492,468,478,484,487,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,489,493,491,493,499,514,489,512,515],
[501,0,482,510,484,512,513,514,489,507,526],
[511,518,0,504,484,521,519,554,505,517,513],
[507,490,496,0,500,509,485,516,474,485,523],
[509,516,516,500,0,526,528,548,508,522,537],
[507,488,479,491,474,0,499,514,493,492,506],
[501,487,481,515,472,501,0,527,498,523,514],
[486,486,446,484,452,486,473,0,475,522,478],
[511,511,495,526,492,507,502,525,0,514,528],
[488,493,483,515,478,508,477,478,486,0,501],
[485,474,487,477,463,494,486,522,472,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,493,519,501,482,507,527,499,463,436],
[545,0,545,480,487,487,503,502,515,518,478],
[507,455,0,515,486,510,478,478,504,482,425],
[481,520,485,0,446,452,470,412,475,444,480],
[499,513,514,554,0,492,513,501,503,483,505],
[518,513,490,548,508,0,476,468,493,466,488],
[493,497,522,530,487,524,0,477,504,465,444],
[473,498,522,588,499,532,523,0,498,509,471],
[501,485,496,525,497,507,496,502,0,513,479],
[537,482,518,556,517,534,535,491,487,0,509],
[564,522,575,520,495,512,556,529,521,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,490,564,579,573,538,523,606,590,450],
[480,0,398,490,460,421,476,447,531,443,461],
[510,602,0,563,614,556,519,506,566,558,467],
[436,510,437,0,541,559,497,487,552,514,422],
[421,540,386,459,0,477,444,447,519,460,458],
[427,579,444,441,523,0,413,485,546,482,407],
[462,524,481,503,556,587,0,573,632,474,550],
[477,553,494,513,553,515,427,0,570,511,462],
[394,469,434,448,481,454,368,430,0,427,408],
[410,557,442,486,540,518,526,489,573,0,485],
[550,539,533,578,542,593,450,538,592,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,489,505,539,500,464,525,522,476,515],
[490,0,488,464,492,499,455,481,477,461,512],
[511,512,0,486,530,494,468,493,508,487,484],
[495,536,514,0,505,504,480,503,476,468,512],
[461,508,470,495,0,517,468,513,483,481,523],
[500,501,506,496,483,0,501,526,476,448,538],
[536,545,532,520,532,499,0,566,535,503,552],
[475,519,507,497,487,474,434,0,468,476,499],
[478,523,492,524,517,524,465,532,0,483,543],
[524,539,513,532,519,552,497,524,517,0,540],
[485,488,516,488,477,462,448,501,457,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,518,520,519,529,504,517,506,512,496],
[481,0,507,522,497,507,481,509,478,482,500],
[482,493,0,514,492,530,493,513,499,508,506],
[480,478,486,0,493,507,473,509,496,505,489],
[481,503,508,507,0,492,480,490,478,509,496],
[471,493,470,493,508,0,481,493,471,500,498],
[496,519,507,527,520,519,0,514,520,494,523],
[483,491,487,491,510,507,486,0,467,511,502],
[494,522,501,504,522,529,480,533,0,505,513],
[488,518,492,495,491,500,506,489,495,0,502],
[504,500,494,511,504,502,477,498,487,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,569,517,560,498,495,508,511,490,584,496],
[431,0,471,484,471,452,469,521,479,525,462],
[483,529,0,548,504,510,526,522,495,548,533],
[440,516,452,0,476,502,453,493,481,503,468],
[502,529,496,524,0,499,497,497,500,547,481],
[505,548,490,498,501,0,493,510,515,524,475],
[492,531,474,547,503,507,0,494,498,531,469],
[489,479,478,507,503,490,506,0,496,520,499],
[510,521,505,519,500,485,502,504,0,559,510],
[416,475,452,497,453,476,469,480,441,0,454],
[504,538,467,532,519,525,531,501,490,546,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,500,466,457,480,493,447,476,461,479],
[523,0,492,485,486,494,511,473,473,492,522],
[500,508,0,500,503,493,508,500,499,506,510],
[534,515,500,0,514,499,504,477,500,501,521],
[543,514,497,486,0,504,509,475,500,487,524],
[520,506,507,501,496,0,522,463,509,490,519],
[507,489,492,496,491,478,0,490,495,488,514],
[553,527,500,523,525,537,510,0,517,515,542],
[524,527,501,500,500,491,505,483,0,506,546],
[539,508,494,499,513,510,512,485,494,0,517],
[521,478,490,479,476,481,486,458,454,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,504,505,530,510,478,495,506,512,479],
[505,0,479,510,530,498,485,506,485,509,500],
[496,521,0,518,499,509,501,523,492,515,500],
[495,490,482,0,522,507,473,516,497,503,502],
[470,470,501,478,0,486,463,489,492,500,488],
[490,502,491,493,514,0,486,503,501,502,497],
[522,515,499,527,537,514,0,545,538,526,511],
[505,494,477,484,511,497,455,0,494,484,499],
[494,515,508,503,508,499,462,506,0,495,490],
[488,491,485,497,500,498,474,516,505,0,499],
[521,500,500,498,512,503,489,501,510,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,511,526,450,532,467,521,479,534,467],
[511,0,517,519,472,518,487,491,453,533,474],
[489,483,0,523,457,531,444,488,451,515,454],
[474,481,477,0,413,452,442,464,435,502,427],
[550,528,543,587,0,554,489,521,510,593,516],
[468,482,469,548,446,0,481,492,494,519,470],
[533,513,556,558,511,519,0,508,506,571,498],
[479,509,512,536,479,508,492,0,468,555,460],
[521,547,549,565,490,506,494,532,0,538,469],
[466,467,485,498,407,481,429,445,462,0,460],
[533,526,546,573,484,530,502,540,531,540,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,507,467,495,522,494,501,522,529,492],
[486,0,491,468,472,518,499,511,493,519,486],
[493,509,0,451,500,483,496,489,498,511,471],
[533,532,549,0,512,495,522,524,525,540,540],
[505,528,500,488,0,501,509,500,503,514,492],
[478,482,517,505,499,0,528,522,504,516,506],
[506,501,504,478,491,472,0,524,499,527,490],
[499,489,511,476,500,478,476,0,503,508,485],
[478,507,502,475,497,496,501,497,0,535,511],
[471,481,489,460,486,484,473,492,465,0,471],
[508,514,529,460,508,494,510,515,489,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,502,546,523,519,526,505,527,497,512],
[480,0,527,522,509,508,510,558,521,518,544],
[498,473,0,542,486,491,495,535,505,484,515],
[454,478,458,0,471,493,458,509,484,473,489],
[477,491,514,529,0,508,505,520,528,518,491],
[481,492,509,507,492,0,504,528,519,473,486],
[474,490,505,542,495,496,0,502,520,514,520],
[495,442,465,491,480,472,498,0,496,487,511],
[473,479,495,516,472,481,480,504,0,467,496],
[503,482,516,527,482,527,486,513,533,0,524],
[488,456,485,511,509,514,480,489,504,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,474,505,461,483,489,449,434,441,467],
[505,0,503,513,514,474,492,480,467,473,503],
[526,497,0,484,504,519,496,448,520,466,561],
[495,487,516,0,562,467,506,497,480,506,492],
[539,486,496,438,0,465,484,434,459,488,530],
[517,526,481,533,535,0,493,514,458,496,527],
[511,508,504,494,516,507,0,487,492,434,532],
[551,520,552,503,566,486,513,0,542,495,558],
[566,533,480,520,541,542,508,458,0,490,510],
[559,527,534,494,512,504,566,505,510,0,524],
[533,497,439,508,470,473,468,442,490,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,496,514,525,524,487,495,494,513,523],
[490,0,496,527,496,510,519,505,512,510,514],
[504,504,0,508,502,513,498,485,480,501,511],
[486,473,492,0,496,509,495,477,505,505,499],
[475,504,498,504,0,526,515,482,500,479,519],
[476,490,487,491,474,0,500,476,490,502,528],
[513,481,502,505,485,500,0,487,514,520,540],
[505,495,515,523,518,524,513,0,509,504,542],
[506,488,520,495,500,510,486,491,0,505,525],
[487,490,499,495,521,498,480,496,495,0,531],
[477,486,489,501,481,472,460,458,475,469,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,532,518,547,482,501,487,505,522,513],
[497,0,525,500,536,490,511,496,485,507,519],
[468,475,0,470,508,471,467,487,464,488,493],
[482,500,530,0,551,504,507,500,507,526,525],
[453,464,492,449,0,451,462,452,463,481,488],
[518,510,529,496,549,0,503,484,478,517,526],
[499,489,533,493,538,497,0,520,478,511,507],
[513,504,513,500,548,516,480,0,501,522,520],
[495,515,536,493,537,522,522,499,0,533,517],
[478,493,512,474,519,483,489,478,467,0,519],
[487,481,507,475,512,474,493,480,483,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,714,791,498,613,707,770,453,673,592],
[477,0,490,555,624,477,658,702,514,612,547],
[286,510,0,507,592,459,579,443,279,408,466],
[209,445,493,0,464,367,580,553,360,431,448],
[502,376,408,536,0,484,604,548,329,482,626],
[387,523,541,633,516,0,740,648,380,701,542],
[293,342,421,420,396,260,0,431,235,395,441],
[230,298,557,447,452,352,569,0,362,475,434],
[547,486,721,640,671,620,765,638,0,620,478],
[327,388,592,569,518,299,605,525,380,0,523],
[408,453,534,552,374,458,559,566,522,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,516,503,509,526,528,551,500,498,504],
[486,0,544,499,497,540,507,524,493,505,504],
[484,456,0,489,444,518,484,537,475,498,478],
[497,501,511,0,507,500,496,536,469,512,500],
[491,503,556,493,0,523,492,533,485,504,505],
[474,460,482,500,477,0,489,515,470,467,481],
[472,493,516,504,508,511,0,507,469,508,501],
[449,476,463,464,467,485,493,0,459,482,464],
[500,507,525,531,515,530,531,541,0,531,514],
[502,495,502,488,496,533,492,518,469,0,494],
[496,496,522,500,495,519,499,536,486,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,497,469,482,467,504,494,498,496,479],
[498,0,492,495,473,471,509,487,518,490,495],
[503,508,0,493,475,480,498,494,512,511,484],
[531,505,507,0,496,520,525,508,477,500,507],
[518,527,525,504,0,484,517,515,539,503,480],
[533,529,520,480,516,0,522,490,519,525,505],
[496,491,502,475,483,478,0,500,518,487,483],
[506,513,506,492,485,510,500,0,526,519,486],
[502,482,488,523,461,481,482,474,0,509,469],
[504,510,489,500,497,475,513,481,491,0,452],
[521,505,516,493,520,495,517,514,531,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,438,382,299,424,464,391,359,445,406,313],
[562,0,422,407,525,575,509,436,466,491,403],
[618,578,0,502,524,471,550,467,522,438,464],
[701,593,498,0,551,585,535,580,567,528,536],
[576,475,476,449,0,477,476,546,469,396,502],
[536,425,529,415,523,0,471,451,506,477,452],
[609,491,450,465,524,529,0,480,488,477,398],
[641,564,533,420,454,549,520,0,518,473,556],
[555,534,478,433,531,494,512,482,0,465,471],
[594,509,562,472,604,523,523,527,535,0,538],
[687,597,536,464,498,548,602,444,529,462,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,542,526,527,539,503,504,485,529,520,517],
[458,0,510,537,488,481,502,471,502,485,526],
[474,490,0,532,533,501,482,496,527,517,539],
[473,463,468,0,510,452,472,486,468,502,484],
[461,512,467,490,0,467,484,448,491,515,465],
[497,519,499,548,533,0,496,504,489,503,491],
[496,498,518,528,516,504,0,480,516,541,554],
[515,529,504,514,552,496,520,0,540,524,493],
[471,498,473,532,509,511,484,460,0,536,511],
[480,515,483,498,485,497,459,476,464,0,534],
[483,474,461,516,535,509,446,507,489,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,523,539,534,548,517,556,534,521,495],
[459,0,507,504,528,531,485,510,489,485,484],
[477,493,0,511,546,545,505,511,479,505,513],
[461,496,489,0,520,508,501,521,496,506,493],
[466,472,454,480,0,522,474,468,476,477,482],
[452,469,455,492,478,0,494,492,470,500,486],
[483,515,495,499,526,506,0,525,499,507,504],
[444,490,489,479,532,508,475,0,477,488,492],
[466,511,521,504,524,530,501,523,0,499,483],
[479,515,495,494,523,500,493,512,501,0,499],
[505,516,487,507,518,514,496,508,517,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,512,508,489,498,503,485,514,520,530],
[516,0,493,505,496,492,504,502,515,522,535],
[488,507,0,497,504,490,493,510,510,519,515],
[492,495,503,0,493,495,490,502,517,518,525],
[511,504,496,507,0,501,514,505,515,521,517],
[502,508,510,505,499,0,524,492,525,524,524],
[497,496,507,510,486,476,0,487,494,503,536],
[515,498,490,498,495,508,513,0,520,538,524],
[486,485,490,483,485,475,506,480,0,515,513],
[480,478,481,482,479,476,497,462,485,0,496],
[470,465,485,475,483,476,464,476,487,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,503,452,505,488,496,487,502,498,464],
[505,0,529,483,483,507,510,490,491,496,494],
[497,471,0,454,500,485,484,478,471,497,464],
[548,517,546,0,520,527,506,499,517,515,500],
[495,517,500,480,0,504,499,495,495,495,466],
[512,493,515,473,496,0,484,493,497,509,500],
[504,490,516,494,501,516,0,503,503,508,501],
[513,510,522,501,505,507,497,0,515,513,495],
[498,509,529,483,505,503,497,485,0,493,487],
[502,504,503,485,505,491,492,487,507,0,499],
[536,506,536,500,534,500,499,505,513,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,488,467,470,483,473,527,519,476,481],
[495,0,483,475,495,482,473,495,500,498,474],
[512,517,0,528,519,491,507,514,547,498,511],
[533,525,472,0,505,516,486,515,515,498,506],
[530,505,481,495,0,488,506,500,509,516,452],
[517,518,509,484,512,0,498,501,522,517,464],
[527,527,493,514,494,502,0,493,499,496,491],
[473,505,486,485,500,499,507,0,526,503,479],
[481,500,453,485,491,478,501,474,0,480,462],
[524,502,502,502,484,483,504,497,520,0,480],
[519,526,489,494,548,536,509,521,538,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,502,499,546,470,530,461,521,474,496],
[473,0,486,490,544,468,498,440,505,472,466],
[498,514,0,467,525,453,525,471,503,476,485],
[501,510,533,0,544,499,516,497,534,512,502],
[454,456,475,456,0,455,487,445,463,501,444],
[530,532,547,501,545,0,531,506,532,501,499],
[470,502,475,484,513,469,0,439,491,458,450],
[539,560,529,503,555,494,561,0,555,519,516],
[479,495,497,466,537,468,509,445,0,469,491],
[526,528,524,488,499,499,542,481,531,0,497],
[504,534,515,498,556,501,550,484,509,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,487,484,519,474,521,465,482,471,470],
[485,0,515,494,499,497,490,498,491,480,463],
[513,485,0,481,487,530,515,497,488,505,486],
[516,506,519,0,519,511,532,521,496,519,513],
[481,501,513,481,0,509,509,503,473,501,484],
[526,503,470,489,491,0,516,525,494,498,478],
[479,510,485,468,491,484,0,482,489,498,482],
[535,502,503,479,497,475,518,0,490,471,490],
[518,509,512,504,527,506,511,510,0,484,502],
[529,520,495,481,499,502,502,529,516,0,487],
[530,537,514,487,516,522,518,510,498,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,433,461,474,464,475,434,470,482,473,479],
[567,0,526,572,536,540,500,537,511,518,523],
[539,474,0,524,509,494,483,495,497,497,497],
[526,428,476,0,473,497,473,469,467,458,478],
[536,464,491,527,0,512,517,497,490,500,517],
[525,460,506,503,488,0,512,498,513,513,500],
[566,500,517,527,483,488,0,520,510,508,505],
[530,463,505,531,503,502,480,0,493,517,487],
[518,489,503,533,510,487,490,507,0,523,521],
[527,482,503,542,500,487,492,483,477,0,490],
[521,477,503,522,483,500,495,513,479,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,461,415,443,470,504,446,458,474,447],
[525,0,515,456,459,549,519,459,435,463,413],
[539,485,0,429,487,455,470,549,391,529,441],
[585,544,571,0,573,570,594,561,577,595,471],
[557,541,513,427,0,526,540,538,555,508,547],
[530,451,545,430,474,0,493,474,442,537,410],
[496,481,530,406,460,507,0,487,426,515,421],
[554,541,451,439,462,526,513,0,440,537,481],
[542,565,609,423,445,558,574,560,0,579,484],
[526,537,471,405,492,463,485,463,421,0,410],
[553,587,559,529,453,590,579,519,516,590,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,439,518,486,493,512,474,469,471,499],
[489,0,394,527,463,458,451,464,511,443,505],
[561,606,0,554,504,518,546,486,512,518,541],
[482,473,446,0,491,466,437,465,439,467,480],
[514,537,496,509,0,492,479,500,504,492,481],
[507,542,482,534,508,0,532,500,511,483,545],
[488,549,454,563,521,468,0,510,510,471,482],
[526,536,514,535,500,500,490,0,504,493,542],
[531,489,488,561,496,489,490,496,0,507,522],
[529,557,482,533,508,517,529,507,493,0,512],
[501,495,459,520,519,455,518,458,478,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,553,506,519,511,539,540,485,479,510,562],
[447,0,498,477,463,504,508,511,440,512,514],
[494,502,0,489,443,500,551,507,502,532,533],
[481,523,511,0,484,520,485,523,480,531,553],
[489,537,557,516,0,536,533,507,484,527,551],
[461,496,500,480,464,0,518,485,505,543,536],
[460,492,449,515,467,482,0,499,453,521,500],
[515,489,493,477,493,515,501,0,511,533,520],
[521,560,498,520,516,495,547,489,0,570,532],
[490,488,468,469,473,457,479,467,430,0,523],
[438,486,467,447,449,464,500,480,468,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,535,537,549,573,524,600,522,572,490,483],
[465,0,526,524,560,498,524,507,580,515,454],
[463,474,0,460,524,437,495,475,511,416,392],
[451,476,540,0,568,441,500,448,534,445,473],
[427,440,476,432,0,414,548,503,488,360,453],
[476,502,563,559,586,0,558,466,519,530,564],
[400,476,505,500,452,442,0,416,403,434,395],
[478,493,525,552,497,534,584,0,578,612,486],
[428,420,489,466,512,481,597,422,0,436,432],
[510,485,584,555,640,470,566,388,564,0,550],
[517,546,608,527,547,436,605,514,568,450,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,508,529,526,507,511,494,493,515,490],
[505,0,491,515,507,499,525,502,495,495,510],
[492,509,0,532,512,502,494,522,508,492,494],
[471,485,468,0,476,484,472,495,466,496,466],
[474,493,488,524,0,494,495,479,470,502,467],
[493,501,498,516,506,0,516,496,514,508,504],
[489,475,506,528,505,484,0,509,482,495,496],
[506,498,478,505,521,504,491,0,490,486,484],
[507,505,492,534,530,486,518,510,0,495,490],
[485,505,508,504,498,492,505,514,505,0,486],
[510,490,506,534,533,496,504,516,510,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,514,498,497,492,504,499,516,486,483],
[513,0,512,484,494,514,510,509,514,484,512],
[486,488,0,490,478,503,499,496,507,493,478],
[502,516,510,0,510,523,497,509,503,492,502],
[503,506,522,490,0,534,527,532,515,503,501],
[508,486,497,477,466,0,512,491,461,494,487],
[496,490,501,503,473,488,0,504,496,483,488],
[501,491,504,491,468,509,496,0,516,502,474],
[484,486,493,497,485,539,504,484,0,462,474],
[514,516,507,508,497,506,517,498,538,0,489],
[517,488,522,498,499,513,512,526,526,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,506,513,556,501,526,500,568,535,539],
[495,0,491,514,510,483,493,508,516,496,511],
[494,509,0,505,538,516,487,505,534,507,501],
[487,486,495,0,516,477,470,486,507,500,492],
[444,490,462,484,0,454,466,482,470,481,462],
[499,517,484,523,546,0,495,532,551,533,533],
[474,507,513,530,534,505,0,510,530,508,500],
[500,492,495,514,518,468,490,0,506,482,507],
[432,484,466,493,530,449,470,494,0,487,492],
[465,504,493,500,519,467,492,518,513,0,507],
[461,489,499,508,538,467,500,493,508,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,477,440,463,473,513,515,516,511,445],
[514,0,465,440,439,487,489,482,422,479,431],
[523,535,0,500,505,530,543,495,512,531,468],
[560,560,500,0,507,495,475,520,503,540,453],
[537,561,495,493,0,556,517,524,530,522,513],
[527,513,470,505,444,0,452,482,478,496,415],
[487,511,457,525,483,548,0,494,504,510,487],
[485,518,505,480,476,518,506,0,502,473,437],
[484,578,488,497,470,522,496,498,0,492,459],
[489,521,469,460,478,504,490,527,508,0,456],
[555,569,532,547,487,585,513,563,541,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,518,479,496,489,480,506,490,518,482],
[472,0,525,476,494,484,491,511,484,510,483],
[482,475,0,465,474,494,480,487,487,477,459],
[521,524,535,0,488,524,506,565,493,498,502],
[504,506,526,512,0,524,520,517,492,528,517],
[511,516,506,476,476,0,500,501,500,493,496],
[520,509,520,494,480,500,0,508,490,531,492],
[494,489,513,435,483,499,492,0,486,483,483],
[510,516,513,507,508,500,510,514,0,514,531],
[482,490,523,502,472,507,469,517,486,0,468],
[518,517,541,498,483,504,508,517,469,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,548,452,513,476,504,531,485,507,515,485],
[452,0,459,476,477,464,468,454,453,464,458],
[548,541,0,511,492,506,470,527,519,492,515],
[487,524,489,0,475,496,488,510,495,487,484],
[524,523,508,525,0,506,509,504,532,489,498],
[496,536,494,504,494,0,509,495,489,525,460],
[469,532,530,512,491,491,0,493,526,461,497],
[515,546,473,490,496,505,507,0,500,462,499],
[493,547,481,505,468,511,474,500,0,475,483],
[485,536,508,513,511,475,539,538,525,0,509],
[515,542,485,516,502,540,503,501,517,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,502,500,512,507,536,526,535,484,540],
[459,0,534,472,535,497,512,523,547,503,531],
[498,466,0,494,494,483,543,468,480,538,533],
[500,528,506,0,465,516,521,533,534,505,553],
[488,465,506,535,0,505,510,486,495,501,553],
[493,503,517,484,495,0,497,496,464,531,566],
[464,488,457,479,490,503,0,479,534,581,534],
[474,477,532,467,514,504,521,0,484,556,520],
[465,453,520,466,505,536,466,516,0,525,533],
[516,497,462,495,499,469,419,444,475,0,533],
[460,469,467,447,447,434,466,480,467,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,517,503,519,493,488,499,485,502,501],
[512,0,506,503,514,499,487,505,487,505,508],
[483,494,0,478,514,505,496,490,482,491,500],
[497,497,522,0,507,497,483,482,481,495,507],
[481,486,486,493,0,464,502,487,477,492,474],
[507,501,495,503,536,0,498,506,506,499,503],
[512,513,504,517,498,502,0,505,517,482,500],
[501,495,510,518,513,494,495,0,487,512,512],
[515,513,518,519,523,494,483,513,0,517,511],
[498,495,509,505,508,501,518,488,483,0,492],
[499,492,500,493,526,497,500,488,489,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,497,533,484,413,440,459,484,528,479],
[542,0,510,508,503,536,505,477,521,505,463],
[503,490,0,550,506,537,490,536,517,537,501],
[467,492,450,0,499,521,488,432,538,539,471],
[516,497,494,501,0,446,457,405,498,497,448],
[587,464,463,479,554,0,460,459,433,477,440],
[560,495,510,512,543,540,0,504,528,591,485],
[541,523,464,568,595,541,496,0,497,537,477],
[516,479,483,462,502,567,472,503,0,482,415],
[472,495,463,461,503,523,409,463,518,0,431],
[521,537,499,529,552,560,515,523,585,569,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,484,498,520,498,547,503,494,527,510],
[526,0,458,508,462,526,569,485,520,514,494],
[516,542,0,502,481,532,570,520,500,524,500],
[502,492,498,0,510,504,532,513,549,505,509],
[480,538,519,490,0,521,576,494,500,513,522],
[502,474,468,496,479,0,520,493,450,472,449],
[453,431,430,468,424,480,0,445,461,447,444],
[497,515,480,487,506,507,555,0,491,516,495],
[506,480,500,451,500,550,539,509,0,502,493],
[473,486,476,495,487,528,553,484,498,0,482],
[490,506,500,491,478,551,556,505,507,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,522,504,469,495,525,478,479,475,505],
[492,0,526,496,515,455,542,485,500,477,527],
[478,474,0,517,497,471,526,480,499,482,499],
[496,504,483,0,495,481,535,471,495,503,507],
[531,485,503,505,0,476,534,497,515,495,531],
[505,545,529,519,524,0,538,489,518,488,517],
[475,458,474,465,466,462,0,468,444,433,484],
[522,515,520,529,503,511,532,0,476,484,531],
[521,500,501,505,485,482,556,524,0,477,502],
[525,523,518,497,505,512,567,516,523,0,523],
[495,473,501,493,469,483,516,469,498,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,447,502,455,428,489,490,479,544,585],
[499,0,389,479,494,375,394,480,423,469,483],
[553,611,0,574,528,474,545,483,472,497,555],
[498,521,426,0,449,416,461,481,510,447,543],
[545,506,472,551,0,482,537,517,510,552,608],
[572,625,526,584,518,0,417,552,542,531,575],
[511,606,455,539,463,583,0,541,454,505,495],
[510,520,517,519,483,448,459,0,451,449,542],
[521,577,528,490,490,458,546,549,0,520,536],
[456,531,503,553,448,469,495,551,480,0,506],
[415,517,445,457,392,425,505,458,464,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,540,522,535,502,455,471,511,475,554],
[527,0,520,504,520,590,511,560,533,493,526],
[460,480,0,536,507,490,428,498,555,459,544],
[478,496,464,0,519,520,499,455,524,470,556],
[465,480,493,481,0,562,444,490,463,467,518],
[498,410,510,480,438,0,438,509,494,467,434],
[545,489,572,501,556,562,0,566,536,496,544],
[529,440,502,545,510,491,434,0,548,534,586],
[489,467,445,476,537,506,464,452,0,476,497],
[525,507,541,530,533,533,504,466,524,0,569],
[446,474,456,444,482,566,456,414,503,431,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,531,497,477,510,508,530,487,500,513],
[507,0,539,489,501,530,539,514,510,507,506],
[469,461,0,475,462,502,496,472,502,474,485],
[503,511,525,0,483,527,513,520,508,508,526],
[523,499,538,517,0,525,518,508,530,510,518],
[490,470,498,473,475,0,485,492,504,487,511],
[492,461,504,487,482,515,0,486,485,497,527],
[470,486,528,480,492,508,514,0,518,511,516],
[513,490,498,492,470,496,515,482,0,489,508],
[500,493,526,492,490,513,503,489,511,0,500],
[487,494,515,474,482,489,473,484,492,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,498,501,488,504,493,475,506,483,507],
[513,0,519,517,517,501,472,472,484,482,496],
[502,481,0,483,483,485,478,470,467,465,501],
[499,483,517,0,508,490,491,481,480,475,487],
[512,483,517,492,0,519,484,468,489,468,523],
[496,499,515,510,481,0,523,465,469,491,538],
[507,528,522,509,516,477,0,501,502,487,522],
[525,528,530,519,532,535,499,0,500,499,509],
[494,516,533,520,511,531,498,500,0,504,520],
[517,518,535,525,532,509,513,501,496,0,517],
[493,504,499,513,477,462,478,491,480,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,495,507,505,489,503,507,515,498,500],
[510,0,515,520,508,518,505,529,516,500,495],
[505,485,0,481,514,498,487,494,491,477,474],
[493,480,519,0,513,484,528,504,520,476,508],
[495,492,486,487,0,483,479,498,494,476,485],
[511,482,502,516,517,0,514,525,520,493,504],
[497,495,513,472,521,486,0,495,488,483,487],
[493,471,506,496,502,475,505,0,510,466,486],
[485,484,509,480,506,480,512,490,0,469,494],
[502,500,523,524,524,507,517,534,531,0,506],
[500,505,526,492,515,496,513,514,506,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,506,576,517,508,492,464,508,543,496],
[546,0,492,551,500,545,560,456,530,479,564],
[494,508,0,546,494,527,487,518,518,494,574],
[424,449,454,0,483,417,426,396,467,451,469],
[483,500,506,517,0,467,453,398,507,472,491],
[492,455,473,583,533,0,527,449,487,507,522],
[508,440,513,574,547,473,0,455,516,510,529],
[536,544,482,604,602,551,545,0,520,462,522],
[492,470,482,533,493,513,484,480,0,504,483],
[457,521,506,549,528,493,490,538,496,0,552],
[504,436,426,531,509,478,471,478,517,448,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,431,312,406,438,438,376,368,406,377,438],
[569,0,464,443,513,491,433,467,455,555,425],
[688,536,0,591,484,531,575,611,536,598,556],
[594,557,409,0,518,513,512,494,507,541,529],
[562,487,516,482,0,532,428,535,478,479,475],
[562,509,469,487,468,0,493,486,434,511,506],
[624,567,425,488,572,507,0,513,481,605,506],
[632,533,389,506,465,514,487,0,494,503,545],
[594,545,464,493,522,566,519,506,0,502,551],
[623,445,402,459,521,489,395,497,498,0,489],
[562,575,444,471,525,494,494,455,449,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,461,524,508,473,475,452,481,482,506],
[508,0,481,518,546,507,490,481,501,498,499],
[539,519,0,533,520,542,473,501,549,498,538],
[476,482,467,0,486,466,477,517,504,509,493],
[492,454,480,514,0,503,488,455,495,443,497],
[527,493,458,534,497,0,493,480,483,488,449],
[525,510,527,523,512,507,0,491,503,494,500],
[548,519,499,483,545,520,509,0,488,480,520],
[519,499,451,496,505,517,497,512,0,487,505],
[518,502,502,491,557,512,506,520,513,0,499],
[494,501,462,507,503,551,500,480,495,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,526,667,424,637,571,580,541,485,536],
[522,0,547,628,583,656,510,468,541,541,525],
[474,453,0,548,520,596,616,491,538,552,558],
[333,372,452,0,366,436,345,485,511,442,450],
[576,417,480,634,0,686,543,471,535,516,546],
[363,344,404,564,314,0,404,442,488,471,413],
[429,490,384,655,457,596,0,458,545,523,417],
[420,532,509,515,529,558,542,0,527,513,381],
[459,459,462,489,465,512,455,473,0,403,489],
[515,459,448,558,484,529,477,487,597,0,540],
[464,475,442,550,454,587,583,619,511,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,502,481,463,493,481,478,531,496,507],
[519,0,503,505,487,533,515,484,534,499,515],
[498,497,0,507,478,482,498,471,514,475,499],
[519,495,493,0,485,527,518,504,558,494,498],
[537,513,522,515,0,498,529,507,525,480,531],
[507,467,518,473,502,0,484,513,524,512,515],
[519,485,502,482,471,516,0,481,539,473,521],
[522,516,529,496,493,487,519,0,529,537,518],
[469,466,486,442,475,476,461,471,0,482,479],
[504,501,525,506,520,488,527,463,518,0,510],
[493,485,501,502,469,485,479,482,521,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,492,509,527,530,499,508,526,518,514],
[495,0,508,477,498,505,480,487,492,501,522],
[508,492,0,498,496,523,486,489,479,518,504],
[491,523,502,0,531,527,502,490,499,541,530],
[473,502,504,469,0,491,500,492,491,520,489],
[470,495,477,473,509,0,467,466,519,511,496],
[501,520,514,498,500,533,0,498,520,523,517],
[492,513,511,510,508,534,502,0,482,510,513],
[474,508,521,501,509,481,480,518,0,517,513],
[482,499,482,459,480,489,477,490,483,0,492],
[486,478,496,470,511,504,483,487,487,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,530,493,509,484,509,524,464,506,506],
[525,0,539,522,543,535,548,562,502,458,530],
[470,461,0,493,513,500,522,498,469,456,498],
[507,478,507,0,530,502,501,526,481,461,523],
[491,457,487,470,0,482,512,510,452,489,487],
[516,465,500,498,518,0,524,519,489,475,511],
[491,452,478,499,488,476,0,504,460,468,489],
[476,438,502,474,490,481,496,0,484,491,505],
[536,498,531,519,548,511,540,516,0,514,540],
[494,542,544,539,511,525,532,509,486,0,518],
[494,470,502,477,513,489,511,495,460,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,494,510,516,512,538,527,497,496,511],
[508,0,502,522,516,514,543,522,529,488,509],
[506,498,0,519,504,509,555,521,493,509,524],
[490,478,481,0,499,500,517,499,497,475,473],
[484,484,496,501,0,483,501,490,506,482,483],
[488,486,491,500,517,0,515,508,503,474,497],
[462,457,445,483,499,485,0,507,479,466,486],
[473,478,479,501,510,492,493,0,504,466,491],
[503,471,507,503,494,497,521,496,0,474,489],
[504,512,491,525,518,526,534,534,526,0,511],
[489,491,476,527,517,503,514,509,511,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,535,499,516,491,473,541,493,547,465,482],
[465,0,463,520,473,456,524,498,522,461,514],
[501,537,0,522,514,490,554,495,542,473,466],
[484,480,478,0,491,466,526,509,501,486,502],
[509,527,486,509,0,485,541,546,562,495,516],
[527,544,510,534,515,0,559,546,565,562,496],
[459,476,446,474,459,441,0,525,536,423,456],
[507,502,505,491,454,454,475,0,525,430,513],
[453,478,458,499,438,435,464,475,0,449,444],
[535,539,527,514,505,438,577,570,551,0,502],
[518,486,534,498,484,504,544,487,556,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,499,518,491,477,496,499,490,513,488],
[489,0,516,502,484,481,493,480,498,494,475],
[501,484,0,508,478,485,473,457,495,490,471],
[482,498,492,0,483,460,508,475,482,499,502],
[509,516,522,517,0,489,495,508,516,492,508],
[523,519,515,540,511,0,500,496,521,505,505],
[504,507,527,492,505,500,0,475,494,504,501],
[501,520,543,525,492,504,525,0,514,509,522],
[510,502,505,518,484,479,506,486,0,512,499],
[487,506,510,501,508,495,496,491,488,0,482],
[512,525,529,498,492,495,499,478,501,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,471,522,516,468,521,483,493,480,515],
[493,0,449,486,508,486,502,465,514,462,481],
[529,551,0,534,542,498,543,532,563,499,523],
[478,514,466,0,520,472,515,487,503,502,474],
[484,492,458,480,0,501,496,455,488,464,461],
[532,514,502,528,499,0,501,503,514,483,514],
[479,498,457,485,504,499,0,468,509,460,469],
[517,535,468,513,545,497,532,0,500,463,523],
[507,486,437,497,512,486,491,500,0,483,470],
[520,538,501,498,536,517,540,537,517,0,516],
[485,519,477,526,539,486,531,477,530,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,541,477,480,482,543,504,573,498,511],
[448,0,547,459,488,497,476,438,472,442,504],
[459,453,0,507,440,448,486,433,419,435,431],
[523,541,493,0,544,509,471,497,546,449,484],
[520,512,560,456,0,485,526,419,500,425,441],
[518,503,552,491,515,0,576,474,517,463,498],
[457,524,514,529,474,424,0,419,537,449,473],
[496,562,567,503,581,526,581,0,564,512,545],
[427,528,581,454,500,483,463,436,0,499,499],
[502,558,565,551,575,537,551,488,501,0,557],
[489,496,569,516,559,502,527,455,501,443,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,467,483,500,496,455,492,476,497,494],
[492,0,458,466,472,469,442,459,465,482,466],
[533,542,0,461,502,476,498,496,492,515,496],
[517,534,539,0,510,497,512,490,501,535,511],
[500,528,498,490,0,492,477,519,498,508,485],
[504,531,524,503,508,0,481,520,509,523,531],
[545,558,502,488,523,519,0,498,505,526,518],
[508,541,504,510,481,480,502,0,514,530,506],
[524,535,508,499,502,491,495,486,0,516,497],
[503,518,485,465,492,477,474,470,484,0,482],
[506,534,504,489,515,469,482,494,503,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,491,516,489,472,518,453,491,484,525],
[476,0,442,494,448,459,495,452,486,480,489],
[509,558,0,548,509,499,539,501,515,498,535],
[484,506,452,0,464,490,499,466,469,470,455],
[511,552,491,536,0,504,539,513,500,501,506],
[528,541,501,510,496,0,540,511,487,505,522],
[482,505,461,501,461,460,0,466,484,463,465],
[547,548,499,534,487,489,534,0,526,496,526],
[509,514,485,531,500,513,516,474,0,496,519],
[516,520,502,530,499,495,537,504,504,0,510],
[475,511,465,545,494,478,535,474,481,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,508,489,505,499,469,532,506,509,496],
[485,0,516,496,497,524,470,528,495,485,493],
[492,484,0,486,491,468,456,506,489,499,469],
[511,504,514,0,510,525,477,519,511,509,477],
[495,503,509,490,0,508,479,535,495,500,462],
[501,476,532,475,492,0,454,518,495,498,478],
[531,530,544,523,521,546,0,557,519,499,522],
[468,472,494,481,465,482,443,0,468,498,460],
[494,505,511,489,505,505,481,532,0,518,470],
[491,515,501,491,500,502,501,502,482,0,465],
[504,507,531,523,538,522,478,540,530,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,629,542,362,455,826,362,542,368,368],
[545,0,528,542,362,354,739,261,275,267,0],
[371,472,0,739,559,458,739,559,472,739,371],
[458,458,261,0,559,458,559,458,472,354,371],
[638,638,441,441,0,638,638,899,812,267,638],
[545,646,542,542,362,0,739,733,646,542,0],
[174,261,261,441,362,261,0,261,174,441,0],
[638,739,441,542,101,267,739,0,739,368,267],
[458,725,528,528,188,354,826,261,0,354,354],
[632,733,261,646,733,458,559,632,646,0,371],
[632,1000,629,629,362,1000,1000,733,646,629,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,564,686,601,609,588,558,494,551,387,546],
[436,0,590,487,607,543,607,530,472,458,512],
[314,410,0,579,453,607,377,356,341,331,427],
[399,513,421,0,378,536,580,567,350,402,419],
[391,393,547,622,0,466,559,485,422,512,441],
[412,457,393,464,534,0,509,460,436,380,446],
[442,393,623,420,441,491,0,492,464,385,344],
[506,470,644,433,515,540,508,0,421,563,542],
[449,528,659,650,578,564,536,579,0,436,557],
[613,542,669,598,488,620,615,437,564,0,598],
[454,488,573,581,559,554,656,458,443,402,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,424,435,407,441,479,493,359,464,404,444],
[576,0,487,504,470,527,532,445,505,489,500],
[565,513,0,480,536,537,523,505,536,517,488],
[593,496,520,0,503,531,547,528,529,457,523],
[559,530,464,497,0,558,546,504,528,481,536],
[521,473,463,469,442,0,464,435,444,424,514],
[507,468,477,453,454,536,0,416,491,456,500],
[641,555,495,472,496,565,584,0,504,483,549],
[536,495,464,471,472,556,509,496,0,444,499],
[596,511,483,543,519,576,544,517,556,0,547],
[556,500,512,477,464,486,500,451,501,453,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,516,475,485,511,498,489,460,511,497],
[553,0,528,483,525,504,516,528,507,548,485],
[484,472,0,449,468,504,463,442,469,503,463],
[525,517,551,0,495,562,516,537,497,536,510],
[515,475,532,505,0,572,510,496,496,524,492],
[489,496,496,438,428,0,429,460,459,471,496],
[502,484,537,484,490,571,0,510,515,503,542],
[511,472,558,463,504,540,490,0,501,537,470],
[540,493,531,503,504,541,485,499,0,558,490],
[489,452,497,464,476,529,497,463,442,0,491],
[503,515,537,490,508,504,458,530,510,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,488,491,518,496,481,484,499,489,513],
[516,0,479,507,495,530,477,501,498,508,525],
[512,521,0,502,521,527,499,505,514,496,531],
[509,493,498,0,519,510,483,487,532,494,526],
[482,505,479,481,0,508,502,484,483,478,523],
[504,470,473,490,492,0,473,496,488,480,510],
[519,523,501,517,498,527,0,516,517,531,539],
[516,499,495,513,516,504,484,0,507,495,520],
[501,502,486,468,517,512,483,493,0,494,516],
[511,492,504,506,522,520,469,505,506,0,530],
[487,475,469,474,477,490,461,480,484,470,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,511,511,489,504,516,495,500,520,528],
[513,0,498,509,486,508,520,513,502,486,521],
[489,502,0,507,482,498,492,506,517,474,517],
[489,491,493,0,494,494,496,500,503,511,519],
[511,514,518,506,0,473,528,511,508,511,526],
[496,492,502,506,527,0,517,510,521,495,511],
[484,480,508,504,472,483,0,499,490,488,502],
[505,487,494,500,489,490,501,0,510,485,513],
[500,498,483,497,492,479,510,490,0,483,514],
[480,514,526,489,489,505,512,515,517,0,503],
[472,479,483,481,474,489,498,487,486,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,479,486,503,469,471,462,475,443,481],
[508,0,504,485,483,484,475,497,473,468,490],
[521,496,0,486,523,489,488,490,486,489,520],
[514,515,514,0,529,505,488,504,499,484,501],
[497,517,477,471,0,505,455,488,464,490,483],
[531,516,511,495,495,0,490,485,486,472,471],
[529,525,512,512,545,510,0,505,481,489,503],
[538,503,510,496,512,515,495,0,500,472,494],
[525,527,514,501,536,514,519,500,0,515,495],
[557,532,511,516,510,528,511,528,485,0,512],
[519,510,480,499,517,529,497,506,505,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,512,519,514,507,516,530,503,501,496],
[521,0,512,544,525,528,507,541,528,528,494],
[488,488,0,507,503,534,498,494,503,479,475],
[481,456,493,0,500,510,454,497,480,459,464],
[486,475,497,500,0,488,491,492,484,485,482],
[493,472,466,490,512,0,493,490,500,495,476],
[484,493,502,546,509,507,0,526,503,511,488],
[470,459,506,503,508,510,474,0,492,468,488],
[497,472,497,520,516,500,497,508,0,473,502],
[499,472,521,541,515,505,489,532,527,0,489],
[504,506,525,536,518,524,512,512,498,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,453,450,429,426,446,473,430,454,463],
[485,0,480,454,458,446,466,457,459,481,473],
[547,520,0,525,529,474,519,518,479,505,488],
[550,546,475,0,515,490,483,529,515,519,492],
[571,542,471,485,0,471,513,520,523,506,518],
[574,554,526,510,529,0,516,538,477,514,514],
[554,534,481,517,487,484,0,499,476,500,506],
[527,543,482,471,480,462,501,0,461,497,489],
[570,541,521,485,477,523,524,539,0,508,521],
[546,519,495,481,494,486,500,503,492,0,479],
[537,527,512,508,482,486,494,511,479,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,501,481,491,464,479,466,495,487,453],
[516,0,532,515,507,500,505,502,494,535,508],
[499,468,0,478,490,457,463,462,492,519,476],
[519,485,522,0,514,485,503,503,487,498,468],
[509,493,510,486,0,491,490,477,508,477,486],
[536,500,543,515,509,0,496,512,504,541,479],
[521,495,537,497,510,504,0,509,508,526,476],
[534,498,538,497,523,488,491,0,515,544,483],
[505,506,508,513,492,496,492,485,0,523,466],
[513,465,481,502,523,459,474,456,477,0,452],
[547,492,524,532,514,521,524,517,534,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,511,496,492,503,538,507,485,523,482],
[514,0,551,501,497,525,518,540,475,509,490],
[489,449,0,441,453,483,482,494,456,458,447],
[504,499,559,0,493,524,501,511,525,508,485],
[508,503,547,507,0,473,543,527,531,492,512],
[497,475,517,476,527,0,510,480,481,529,481],
[462,482,518,499,457,490,0,499,440,528,471],
[493,460,506,489,473,520,501,0,473,538,466],
[515,525,544,475,469,519,560,527,0,566,452],
[477,491,542,492,508,471,472,462,434,0,470],
[518,510,553,515,488,519,529,534,548,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,596,514,513,503,461,499,503,558,464],
[509,0,496,531,516,520,475,478,492,545,492],
[404,504,0,521,458,463,412,386,473,514,386],
[486,469,479,0,485,466,484,470,506,508,506],
[487,484,542,515,0,486,497,563,503,580,455],
[497,480,537,534,514,0,444,549,537,517,450],
[539,525,588,516,503,556,0,559,537,494,498],
[501,522,614,530,437,451,441,0,505,543,418],
[497,508,527,494,497,463,463,495,0,487,480],
[442,455,486,492,420,483,506,457,513,0,418],
[536,508,614,494,545,550,502,582,520,582,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,488,509,478,483,508,494,472,481,489],
[496,0,483,481,475,475,492,456,458,438,485],
[512,517,0,493,478,510,511,529,490,495,499],
[491,519,507,0,469,482,525,510,524,514,503],
[522,525,522,531,0,522,525,528,507,498,503],
[517,525,490,518,478,0,501,515,504,496,525],
[492,508,489,475,475,499,0,489,502,476,474],
[506,544,471,490,472,485,511,0,492,493,485],
[528,542,510,476,493,496,498,508,0,520,499],
[519,562,505,486,502,504,524,507,480,0,512],
[511,515,501,497,497,475,526,515,501,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,491,522,513,513,485,523,519,510,518],
[511,0,505,530,535,525,491,517,512,542,541],
[509,495,0,523,518,505,540,509,515,520,529],
[478,470,477,0,483,490,482,503,493,499,488],
[487,465,482,517,0,520,488,482,501,489,490],
[487,475,495,510,480,0,497,481,490,489,500],
[515,509,460,518,512,503,0,518,513,503,514],
[477,483,491,497,518,519,482,0,492,495,512],
[481,488,485,507,499,510,487,508,0,477,493],
[490,458,480,501,511,511,497,505,523,0,497],
[482,459,471,512,510,500,486,488,507,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,522,496,528,492,523,498,469,529,510],
[464,0,474,515,504,511,509,475,452,526,497],
[478,526,0,493,496,535,524,432,495,478,449],
[504,485,507,0,526,485,511,469,449,567,529],
[472,496,504,474,0,499,498,479,499,538,549],
[508,489,465,515,501,0,539,444,482,526,512],
[477,491,476,489,502,461,0,453,447,500,487],
[502,525,568,531,521,556,547,0,549,544,458],
[531,548,505,551,501,518,553,451,0,569,512],
[471,474,522,433,462,474,500,456,431,0,492],
[490,503,551,471,451,488,513,542,488,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,508,498,493,470,484,493,502,485,488],
[507,0,526,531,494,475,489,511,509,463,480],
[492,474,0,485,481,478,481,508,494,471,473],
[502,469,515,0,485,477,463,506,488,487,466],
[507,506,519,515,0,489,472,511,502,504,497],
[530,525,522,523,511,0,495,521,525,494,515],
[516,511,519,537,528,505,0,529,517,482,481],
[507,489,492,494,489,479,471,0,466,474,462],
[498,491,506,512,498,475,483,534,0,504,471],
[515,537,529,513,496,506,518,526,496,0,505],
[512,520,527,534,503,485,519,538,529,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,484,503,468,414,451,440,490,423,441],
[531,0,492,462,470,460,455,418,448,474,414],
[516,508,0,454,486,509,458,427,499,441,494],
[497,538,546,0,519,495,457,459,521,499,547],
[532,530,514,481,0,505,396,478,493,512,473],
[586,540,491,505,495,0,490,537,523,493,505],
[549,545,542,543,604,510,0,482,523,478,531],
[560,582,573,541,522,463,518,0,581,482,513],
[510,552,501,479,507,477,477,419,0,439,491],
[577,526,559,501,488,507,522,518,561,0,495],
[559,586,506,453,527,495,469,487,509,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,515,525,489,481,492,517,515,509,514],
[490,0,530,508,495,522,511,507,516,506,513],
[485,470,0,532,494,497,495,521,505,477,518],
[475,492,468,0,483,512,475,512,527,491,482],
[511,505,506,517,0,511,481,522,520,508,508],
[519,478,503,488,489,0,481,516,507,512,489],
[508,489,505,525,519,519,0,521,530,517,518],
[483,493,479,488,478,484,479,0,499,492,501],
[485,484,495,473,480,493,470,501,0,499,497],
[491,494,523,509,492,488,483,508,501,0,515],
[486,487,482,518,492,511,482,499,503,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,482,478,478,504,480,464,490,473,469],
[543,0,514,496,494,515,483,482,545,529,487],
[518,486,0,502,500,507,488,506,509,518,518],
[522,504,498,0,512,511,509,485,511,528,521],
[522,506,500,488,0,478,480,488,489,517,467],
[496,485,493,489,522,0,507,475,499,513,516],
[520,517,512,491,520,493,0,467,506,528,522],
[536,518,494,515,512,525,533,0,540,549,506],
[510,455,491,489,511,501,494,460,0,493,494],
[527,471,482,472,483,487,472,451,507,0,471],
[531,513,482,479,533,484,478,494,506,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,481,483,487,518,499,531,514,493,485],
[506,0,490,485,484,502,528,535,513,493,495],
[519,510,0,513,481,476,525,517,487,511,493],
[517,515,487,0,501,514,527,531,524,521,523],
[513,516,519,499,0,541,546,529,539,538,511],
[482,498,524,486,459,0,518,476,480,484,527],
[501,472,475,473,454,482,0,478,472,463,495],
[469,465,483,469,471,524,522,0,482,476,488],
[486,487,513,476,461,520,528,518,0,488,520],
[507,507,489,479,462,516,537,524,512,0,515],
[515,505,507,477,489,473,505,512,480,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,507,502,507,499,464,490,486,523,512],
[502,0,489,523,514,504,498,518,497,519,514],
[493,511,0,505,518,484,496,492,498,507,498],
[498,477,495,0,485,498,489,499,499,505,501],
[493,486,482,515,0,501,501,517,494,504,535],
[501,496,516,502,499,0,507,503,489,513,520],
[536,502,504,511,499,493,0,496,494,518,522],
[510,482,508,501,483,497,504,0,489,498,507],
[514,503,502,501,506,511,506,511,0,491,499],
[477,481,493,495,496,487,482,502,509,0,496],
[488,486,502,499,465,480,478,493,501,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,484,513,500,526,488,472,481,504,479],
[482,0,486,492,520,496,434,471,465,474,477],
[516,514,0,496,511,513,460,499,491,511,514],
[487,508,504,0,522,512,484,509,512,464,510],
[500,480,489,478,0,494,457,476,493,452,487],
[474,504,487,488,506,0,460,460,489,509,464],
[512,566,540,516,543,540,0,492,504,516,534],
[528,529,501,491,524,540,508,0,476,504,535],
[519,535,509,488,507,511,496,524,0,508,507],
[496,526,489,536,548,491,484,496,492,0,517],
[521,523,486,490,513,536,466,465,493,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 1000, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_11_1000.csv", index=False, header=False)