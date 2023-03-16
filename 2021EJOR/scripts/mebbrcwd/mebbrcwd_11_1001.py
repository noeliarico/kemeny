
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,523,525,512,529,462,479,481,492,514,496],
[478,0,489,491,485,457,502,506,489,481,486],
[476,512,0,483,494,462,481,449,478,507,478],
[489,510,518,0,551,520,507,524,541,520,540],
[472,516,507,450,0,424,493,498,452,502,471],
[539,544,539,481,577,0,520,519,525,554,509],
[522,499,520,494,508,481,0,484,499,498,501],
[520,495,552,477,503,482,517,0,506,514,505],
[509,512,523,460,549,476,502,495,0,514,483],
[487,520,494,481,499,447,503,487,487,0,508],
[505,515,523,461,530,492,500,496,518,493,0]])



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
result = np.append(np.array([11, 1001, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,430,471,420,487,354,287,423,463,453,422],
[571,0,545,539,507,500,338,415,492,552,364],
[530,456,0,467,602,417,454,319,426,597,388],
[581,462,534,0,497,419,356,539,489,483,443],
[514,494,399,504,0,379,304,415,437,489,390],
[647,501,584,582,622,0,486,492,562,553,521],
[714,663,547,645,697,515,0,463,587,681,559],
[578,586,682,462,586,509,538,0,529,612,527],
[538,509,575,512,564,439,414,472,0,482,524],
[548,449,404,518,512,448,320,389,519,0,496],
[579,637,613,558,611,480,442,474,477,505,0]])



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
result = np.append(np.array([11, 1001, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,616,482,518,496,600,551,571,561,636,522],
[385,0,458,466,512,521,445,496,496,479,482],
[519,543,0,574,462,595,622,585,523,687,641],
[483,535,427,0,504,642,601,552,598,562,566],
[505,489,539,497,0,579,533,531,537,491,323],
[401,480,406,359,422,0,423,453,549,470,467],
[450,556,379,400,468,578,0,516,517,526,481],
[430,505,416,449,470,548,485,0,553,481,441],
[440,505,478,403,464,452,484,448,0,463,399],
[365,522,314,439,510,531,475,520,538,0,384],
[479,519,360,435,678,534,520,560,602,617,0]])



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
result = np.append(np.array([11, 1001, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,400,608,383,641,574,591,523,556,487],
[491,0,354,553,539,512,553,423,538,560,519],
[601,647,0,722,500,721,594,610,588,675,615],
[393,448,279,0,326,606,455,515,494,488,512],
[618,462,501,675,0,698,600,646,582,630,633],
[360,489,280,395,303,0,504,438,518,453,531],
[427,448,407,546,401,497,0,461,462,531,524],
[410,578,391,486,355,563,540,0,520,611,556],
[478,463,413,507,419,483,539,481,0,567,690],
[445,441,326,513,371,548,470,390,434,0,475],
[514,482,386,489,368,470,477,445,311,526,0]])



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
result = np.append(np.array([11, 1001, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,475,482,490,433,535,497,458,503,537],
[522,0,505,517,503,501,526,517,483,528,548],
[526,496,0,517,527,481,535,539,504,531,529],
[519,484,484,0,471,486,550,486,503,522,500],
[511,498,474,530,0,483,536,531,531,530,545],
[568,500,520,515,518,0,556,531,491,528,554],
[466,475,466,451,465,445,0,465,482,513,493],
[504,484,462,515,470,470,536,0,503,503,496],
[543,518,497,498,470,510,519,498,0,538,506],
[498,473,470,479,471,473,488,498,463,0,469],
[464,453,472,501,456,447,508,505,495,532,0]])



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
result = np.append(np.array([11, 1001, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,482,492,525,506,496,518,513,495,494],
[509,0,476,485,503,507,513,502,505,538,486],
[519,525,0,511,523,503,498,519,517,523,511],
[509,516,490,0,494,499,489,503,510,501,497],
[476,498,478,507,0,490,476,483,492,498,485],
[495,494,498,502,511,0,506,483,505,516,485],
[505,488,503,512,525,495,0,515,525,522,490],
[483,499,482,498,518,518,486,0,486,512,487],
[488,496,484,491,509,496,476,515,0,516,477],
[506,463,478,500,503,485,479,489,485,0,479],
[507,515,490,504,516,516,511,514,524,522,0]])



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
result = np.append(np.array([11, 1001, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,484,511,530,529,532,496,486,485,520],
[496,0,457,494,514,516,512,487,490,500,520],
[517,544,0,513,536,521,516,500,508,498,530],
[490,507,488,0,511,502,502,491,470,480,530],
[471,487,465,490,0,488,492,460,471,478,492],
[472,485,480,499,513,0,513,499,459,479,487],
[469,489,485,499,509,488,0,478,466,479,497],
[505,514,501,510,541,502,523,0,497,527,514],
[515,511,493,531,530,542,535,504,0,517,526],
[516,501,503,521,523,522,522,474,484,0,509],
[481,481,471,471,509,514,504,487,475,492,0]])



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
result = np.append(np.array([11, 1001, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,491,528,518,491,516,513,495,498,514],
[518,0,517,507,557,517,538,494,501,498,514],
[510,484,0,495,533,503,497,478,499,466,495],
[473,494,506,0,533,493,521,506,483,495,499],
[483,444,468,468,0,464,497,488,468,465,462],
[510,484,498,508,537,0,495,484,498,501,500],
[485,463,504,480,504,506,0,483,483,493,482],
[488,507,523,495,513,517,518,0,503,510,484],
[506,500,502,518,533,503,518,498,0,516,494],
[503,503,535,506,536,500,508,491,485,0,503],
[487,487,506,502,539,501,519,517,507,498,0]])



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
result = np.append(np.array([11, 1001, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,503,478,477,484,497,538,459,487,509],
[505,0,490,505,511,478,526,542,472,495,503],
[498,511,0,463,488,476,517,557,465,490,450],
[523,496,538,0,497,491,508,567,456,501,498],
[524,490,513,504,0,516,476,557,457,507,506],
[517,523,525,510,485,0,530,500,471,510,492],
[504,475,484,493,525,471,0,519,439,515,465],
[463,459,444,434,444,501,482,0,421,439,430],
[542,529,536,545,544,530,562,580,0,544,500],
[514,506,511,500,494,491,486,562,457,0,494],
[492,498,551,503,495,509,536,571,501,507,0]])



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
result = np.append(np.array([11, 1001, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,537,506,497,497,529,534,509,516,535],
[496,0,507,523,507,518,508,508,497,510,527],
[464,494,0,499,483,505,490,492,467,490,507],
[495,478,502,0,472,503,508,508,474,507,499],
[504,494,518,529,0,503,503,512,480,528,521],
[504,483,496,498,498,0,495,511,499,522,508],
[472,493,511,493,498,506,0,524,482,511,523],
[467,493,509,493,489,490,477,0,480,497,508],
[492,504,534,527,521,502,519,521,0,525,515],
[485,491,511,494,473,479,490,504,476,0,515],
[466,474,494,502,480,493,478,493,486,486,0]])



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
result = np.append(np.array([11, 1001, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,543,535,483,449,508,545,478,533,531],
[465,0,516,528,501,516,492,487,493,546,536],
[458,485,0,573,471,463,443,510,469,515,503],
[466,473,428,0,465,443,466,489,463,489,516],
[518,500,530,536,0,511,513,525,487,545,538],
[552,485,538,558,490,0,501,536,556,542,528],
[493,509,558,535,488,500,0,506,507,551,527],
[456,514,491,512,476,465,495,0,458,501,528],
[523,508,532,538,514,445,494,543,0,534,552],
[468,455,486,512,456,459,450,500,467,0,561],
[470,465,498,485,463,473,474,473,449,440,0]])



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
result = np.append(np.array([11, 1001, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,441,427,490,476,501,495,443,511,456,481],
[560,0,474,476,499,453,517,524,503,463,514],
[574,527,0,492,464,518,548,606,569,526,555],
[511,525,509,0,504,494,527,513,535,467,472],
[525,502,537,497,0,566,551,580,591,513,464],
[500,548,483,507,435,0,516,563,500,539,518],
[506,484,453,474,450,485,0,465,541,481,470],
[558,477,395,488,421,438,536,0,461,496,450],
[490,498,432,466,410,501,460,540,0,466,494],
[545,538,475,534,488,462,520,505,535,0,540],
[520,487,446,529,537,483,531,551,507,461,0]])



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
result = np.append(np.array([11, 1001, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,571,507,618,554,558,658,673,533,553],
[501,0,500,499,564,553,625,643,632,543,484],
[430,501,0,413,538,491,500,471,560,466,490],
[494,502,588,0,600,495,563,589,634,518,483],
[383,437,463,401,0,436,512,557,519,376,475],
[447,448,510,506,565,0,559,587,711,537,516],
[443,376,501,438,489,442,0,545,495,420,498],
[343,358,530,412,444,414,456,0,478,447,417],
[328,369,441,367,482,290,506,523,0,389,366],
[468,458,535,483,625,464,581,554,612,0,508],
[448,517,511,518,526,485,503,584,635,493,0]])



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
result = np.append(np.array([11, 1001, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,500,498,495,468,487,500,500,497,495],
[499,0,525,489,475,485,499,491,498,518,502],
[501,476,0,482,491,461,492,480,462,489,481],
[503,512,519,0,511,471,487,508,499,500,516],
[506,526,510,490,0,486,483,501,489,498,502],
[533,516,540,530,515,0,517,542,496,499,526],
[514,502,509,514,518,484,0,523,490,514,506],
[501,510,521,493,500,459,478,0,490,487,508],
[501,503,539,502,512,505,511,511,0,491,501],
[504,483,512,501,503,502,487,514,510,0,511],
[506,499,520,485,499,475,495,493,500,490,0]])



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
result = np.append(np.array([11, 1001, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,500,428,476,510,471,513,507,537,506],
[522,0,519,504,514,497,528,518,512,524,533],
[501,482,0,449,491,475,482,502,491,470,474],
[573,497,552,0,519,535,531,517,530,541,530],
[525,487,510,482,0,511,489,527,512,527,503],
[491,504,526,466,490,0,483,521,524,540,523],
[530,473,519,470,512,518,0,521,526,538,514],
[488,483,499,484,474,480,480,0,514,506,515],
[494,489,510,471,489,477,475,487,0,539,464],
[464,477,531,460,474,461,463,495,462,0,472],
[495,468,527,471,498,478,487,486,537,529,0]])



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
result = np.append(np.array([11, 1001, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,520,516,485,515,497,505,492,477,508],
[505,0,496,521,491,485,509,449,500,521,503],
[481,505,0,494,492,528,510,492,569,545,541],
[485,480,507,0,518,523,507,445,514,473,528],
[516,510,509,483,0,549,535,484,502,508,524],
[486,516,473,478,452,0,489,499,480,481,472],
[504,492,491,494,466,512,0,449,484,471,554],
[496,552,509,556,517,502,552,0,530,533,554],
[509,501,432,487,499,521,517,471,0,505,502],
[524,480,456,528,493,520,530,468,496,0,500],
[493,498,460,473,477,529,447,447,499,501,0]])



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
result = np.append(np.array([11, 1001, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,496,475,475,486,486,506,447,507,461],
[493,0,492,448,462,488,503,502,468,483,479],
[505,509,0,476,499,515,490,495,467,491,477],
[526,553,525,0,490,537,503,534,514,521,513],
[526,539,502,511,0,532,514,532,482,526,499],
[515,513,486,464,469,0,489,495,444,482,483],
[515,498,511,498,487,512,0,519,465,527,505],
[495,499,506,467,469,506,482,0,427,481,478],
[554,533,534,487,519,557,536,574,0,536,533],
[494,518,510,480,475,519,474,520,465,0,477],
[540,522,524,488,502,518,496,523,468,524,0]])



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
result = np.append(np.array([11, 1001, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,523,513,501,498,504,499,482,544,521],
[482,0,513,515,508,481,491,501,487,521,508],
[478,488,0,504,477,488,486,509,473,526,481],
[488,486,497,0,497,484,474,496,460,525,517],
[500,493,524,504,0,503,500,517,502,525,534],
[503,520,513,517,498,0,492,517,501,534,516],
[497,510,515,527,501,509,0,504,494,534,537],
[502,500,492,505,484,484,497,0,497,521,514],
[519,514,528,541,499,500,507,504,0,538,549],
[457,480,475,476,476,467,467,480,463,0,476],
[480,493,520,484,467,485,464,487,452,525,0]])



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
result = np.append(np.array([11, 1001, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,495,511,545,461,477,475,517,524,505],
[509,0,472,521,530,450,470,512,538,524,523],
[506,529,0,542,562,497,495,508,564,531,526],
[490,480,459,0,545,438,432,496,534,495,505],
[456,471,439,456,0,439,427,439,479,482,430],
[540,551,504,563,562,0,518,472,575,533,538],
[524,531,506,569,574,483,0,540,535,547,526],
[526,489,493,505,562,529,461,0,527,522,508],
[484,463,437,467,522,426,466,474,0,483,496],
[477,477,470,506,519,468,454,479,518,0,475],
[496,478,475,496,571,463,475,493,505,526,0]])



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
result = np.append(np.array([11, 1001, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,538,539,532,526,513,536,535,490,538],
[500,0,509,525,470,515,497,474,483,525,518],
[463,492,0,517,462,505,486,483,490,514,470],
[462,476,484,0,453,518,495,459,496,488,474],
[469,531,539,548,0,535,540,494,531,531,544],
[475,486,496,483,466,0,534,449,508,494,500],
[488,504,515,506,461,467,0,467,511,501,492],
[465,527,518,542,507,552,534,0,506,537,515],
[466,518,511,505,470,493,490,495,0,494,496],
[511,476,487,513,470,507,500,464,507,0,498],
[463,483,531,527,457,501,509,486,505,503,0]])



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
result = np.append(np.array([11, 1001, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,551,511,483,543,505,527,459,575,534],
[462,0,484,452,492,533,461,477,498,514,539],
[450,517,0,453,517,456,537,494,481,574,528],
[490,549,548,0,512,524,525,556,547,585,562],
[518,509,484,489,0,572,539,520,519,579,566],
[458,468,545,477,429,0,515,478,503,549,566],
[496,540,464,476,462,486,0,451,494,513,520],
[474,524,507,445,481,523,550,0,445,575,546],
[542,503,520,454,482,498,507,556,0,586,511],
[426,487,427,416,422,452,488,426,415,0,510],
[467,462,473,439,435,435,481,455,490,491,0]])



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
result = np.append(np.array([11, 1001, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,515,505,498,519,503,528,505,505,519],
[493,0,469,468,477,490,504,498,505,480,493],
[486,532,0,498,519,519,528,509,510,488,521],
[496,533,503,0,513,543,529,519,522,510,530],
[503,524,482,488,0,520,516,503,525,506,514],
[482,511,482,458,481,0,508,493,493,482,508],
[498,497,473,472,485,493,0,508,512,470,507],
[473,503,492,482,498,508,493,0,499,485,492],
[496,496,491,479,476,508,489,502,0,495,502],
[496,521,513,491,495,519,531,516,506,0,514],
[482,508,480,471,487,493,494,509,499,487,0]])



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
result = np.append(np.array([11, 1001, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,423,412,445,431,540,453,497,444,505,426],
[578,0,466,555,510,532,472,547,527,573,398],
[589,535,0,498,495,484,444,547,442,503,510],
[556,446,503,0,486,532,395,562,522,483,494],
[570,491,506,515,0,544,529,488,439,576,476],
[461,469,517,469,457,0,448,536,438,464,411],
[548,529,557,606,472,553,0,558,527,627,476],
[504,454,454,439,513,465,443,0,372,415,483],
[557,474,559,479,562,563,474,629,0,510,472],
[496,428,498,518,425,537,374,586,491,0,486],
[575,603,491,507,525,590,525,518,529,515,0]])



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
result = np.append(np.array([11, 1001, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,544,533,412,438,420,426,492,478,362],
[540,0,624,590,504,497,560,458,653,717,557],
[457,377,0,512,478,331,295,436,511,366,455],
[468,411,489,0,541,306,427,359,594,506,358],
[589,497,523,460,0,517,322,564,587,547,481],
[563,504,670,695,484,0,533,479,622,474,399],
[581,441,706,574,679,468,0,669,717,425,473],
[575,543,565,642,437,522,332,0,667,444,411],
[509,348,490,407,414,379,284,334,0,391,522],
[523,284,635,495,454,527,576,557,610,0,455],
[639,444,546,643,520,602,528,590,479,546,0]])



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
result = np.append(np.array([11, 1001, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,451,494,473,497,438,454,498,503,461,487],
[550,0,545,537,547,478,492,516,555,515,515],
[507,456,0,501,509,490,489,462,497,490,504],
[528,464,500,0,522,475,467,465,489,468,497],
[504,454,492,479,0,437,472,459,504,449,479],
[563,523,511,526,564,0,512,500,535,479,491],
[547,509,512,534,529,489,0,496,542,513,502],
[503,485,539,536,542,501,505,0,536,520,476],
[498,446,504,512,497,466,459,465,0,472,493],
[540,486,511,533,552,522,488,481,529,0,496],
[514,486,497,504,522,510,499,525,508,505,0]])



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
result = np.append(np.array([11, 1001, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,579,555,526,514,527,472,525,562,596],
[469,0,533,444,474,441,487,463,508,549,553],
[422,468,0,458,464,453,508,460,480,514,459],
[446,557,543,0,549,438,540,465,538,515,544],
[475,527,537,452,0,443,518,433,555,500,536],
[487,560,548,563,558,0,464,529,568,566,518],
[474,514,493,461,483,537,0,454,502,507,491],
[529,538,541,536,568,472,547,0,528,519,533],
[476,493,521,463,446,433,499,473,0,499,503],
[439,452,487,486,501,435,494,482,502,0,490],
[405,448,542,457,465,483,510,468,498,511,0]])



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
result = np.append(np.array([11, 1001, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,493,530,491,517,497,493,523,513,530],
[508,0,456,518,489,531,491,521,468,548,481],
[508,545,0,558,548,560,551,489,513,536,589],
[471,483,443,0,490,469,445,478,450,502,484],
[510,512,453,511,0,546,514,515,464,485,498],
[484,470,441,532,455,0,461,497,498,430,484],
[504,510,450,556,487,540,0,469,507,502,542],
[508,480,512,523,486,504,532,0,457,490,477],
[478,533,488,551,537,503,494,544,0,504,544],
[488,453,465,499,516,571,499,511,497,0,502],
[471,520,412,517,503,517,459,524,457,499,0]])



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
result = np.append(np.array([11, 1001, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,527,499,522,491,492,504,520,505,487],
[498,0,480,497,510,485,493,518,504,518,506],
[474,521,0,507,527,481,509,483,482,515,503],
[502,504,494,0,527,512,527,548,490,543,511],
[479,491,474,474,0,468,477,490,485,497,494],
[510,516,520,489,533,0,487,515,516,530,504],
[509,508,492,474,524,514,0,533,499,537,493],
[497,483,518,453,511,486,468,0,483,528,494],
[481,497,519,511,516,485,502,518,0,522,516],
[496,483,486,458,504,471,464,473,479,0,488],
[514,495,498,490,507,497,508,507,485,513,0]])



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
result = np.append(np.array([11, 1001, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,503,500,522,485,468,496,480,478,496],
[493,0,501,522,518,503,497,507,490,465,509],
[498,500,0,484,482,497,492,491,500,472,494],
[501,479,517,0,485,497,470,493,489,465,498],
[479,483,519,516,0,504,485,495,488,475,494],
[516,498,504,504,497,0,475,497,480,476,492],
[533,504,509,531,516,526,0,524,505,492,508],
[505,494,510,508,506,504,477,0,474,465,489],
[521,511,501,512,513,521,496,527,0,506,512],
[523,536,529,536,526,525,509,536,495,0,507],
[505,492,507,503,507,509,493,512,489,494,0]])



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
result = np.append(np.array([11, 1001, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,582,536,516,564,493,569,531,509,552,558],
[419,0,516,416,504,431,532,452,449,560,484],
[465,485,0,503,541,399,543,473,504,516,500],
[485,585,498,0,547,420,556,479,520,561,451],
[437,497,460,454,0,489,463,446,451,521,450],
[508,570,602,581,512,0,563,552,487,601,490],
[432,469,458,445,538,438,0,409,446,499,426],
[470,549,528,522,555,449,592,0,484,583,439],
[492,552,497,481,550,514,555,517,0,599,478],
[449,441,485,440,480,400,502,418,402,0,433],
[443,517,501,550,551,511,575,562,523,568,0]])



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
result = np.append(np.array([11, 1001, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,498,497,472,491,446,461,465,464,488],
[505,0,498,512,464,495,494,473,495,493,480],
[503,503,0,500,482,493,500,477,496,493,479],
[504,489,501,0,474,470,473,496,524,483,465],
[529,537,519,527,0,517,493,501,520,509,502],
[510,506,508,531,484,0,500,487,507,480,468],
[555,507,501,528,508,501,0,510,539,507,487],
[540,528,524,505,500,514,491,0,530,508,493],
[536,506,505,477,481,494,462,471,0,490,474],
[537,508,508,518,492,521,494,493,511,0,519],
[513,521,522,536,499,533,514,508,527,482,0]])



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
result = np.append(np.array([11, 1001, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,474,519,482,431,445,481,427,459,475],
[523,0,497,536,523,490,463,524,490,497,487],
[527,504,0,500,491,459,474,530,481,499,481],
[482,465,501,0,470,469,476,497,469,479,439],
[519,478,510,531,0,483,504,493,465,485,471],
[570,511,542,532,518,0,491,560,492,517,502],
[556,538,527,525,497,510,0,540,494,530,480],
[520,477,471,504,508,441,461,0,477,495,489],
[574,511,520,532,536,509,507,524,0,505,488],
[542,504,502,522,516,484,471,506,496,0,507],
[526,514,520,562,530,499,521,512,513,494,0]])



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
result = np.append(np.array([11, 1001, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,506,506,503,484,504,499,508,464,507],
[521,0,513,514,496,482,497,484,484,497,503],
[495,488,0,464,486,491,486,486,480,500,487],
[495,487,537,0,507,520,509,488,505,477,494],
[498,505,515,494,0,480,515,475,501,482,511],
[517,519,510,481,521,0,532,509,522,504,484],
[497,504,515,492,486,469,0,479,495,487,486],
[502,517,515,513,526,492,522,0,515,479,500],
[493,517,521,496,500,479,506,486,0,492,504],
[537,504,501,524,519,497,514,522,509,0,510],
[494,498,514,507,490,517,515,501,497,491,0]])



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
result = np.append(np.array([11, 1001, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,505,506,521,490,502,524,492,490,525],
[503,0,530,494,519,527,498,539,500,505,551],
[496,471,0,508,498,494,483,524,488,475,530],
[495,507,493,0,522,480,489,527,489,492,538],
[480,482,503,479,0,498,486,490,489,497,518],
[511,474,507,521,503,0,498,551,514,522,516],
[499,503,518,512,515,503,0,527,509,495,525],
[477,462,477,474,511,450,474,0,488,466,516],
[509,501,513,512,512,487,492,513,0,506,514],
[511,496,526,509,504,479,506,535,495,0,537],
[476,450,471,463,483,485,476,485,487,464,0]])



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
result = np.append(np.array([11, 1001, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,528,514,490,530,514,477,538,480,477],
[532,0,529,482,525,542,543,479,587,492,548],
[473,472,0,482,510,504,513,522,522,493,497],
[487,519,519,0,538,542,541,530,524,539,556],
[511,476,491,463,0,538,520,496,495,460,537],
[471,459,497,459,463,0,496,461,503,501,494],
[487,458,488,460,481,505,0,453,512,507,519],
[524,522,479,471,505,540,548,0,555,486,526],
[463,414,479,477,506,498,489,446,0,473,457],
[521,509,508,462,541,500,494,515,528,0,515],
[524,453,504,445,464,507,482,475,544,486,0]])



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
result = np.append(np.array([11, 1001, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,474,502,462,483,489,484,491,509,494],
[514,0,503,502,478,494,498,498,509,494,502],
[527,498,0,509,478,484,501,490,500,506,509],
[499,499,492,0,483,490,501,490,485,494,488],
[539,523,523,518,0,504,496,506,514,549,531],
[518,507,517,511,497,0,494,494,511,511,505],
[512,503,500,500,505,507,0,493,493,523,510],
[517,503,511,511,495,507,508,0,516,525,519],
[510,492,501,516,487,490,508,485,0,512,505],
[492,507,495,507,452,490,478,476,489,0,507],
[507,499,492,513,470,496,491,482,496,494,0]])



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
result = np.append(np.array([11, 1001, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,519,470,518,515,469,501,476,515,461],
[490,0,497,535,487,501,502,514,467,492,482],
[482,504,0,501,467,477,499,489,432,505,458],
[531,466,500,0,509,499,483,488,468,503,473],
[483,514,534,492,0,488,473,488,459,506,482],
[486,500,524,502,513,0,483,499,519,527,470],
[532,499,502,518,528,518,0,540,502,520,509],
[500,487,512,513,513,502,461,0,428,519,481],
[525,534,569,533,542,482,499,573,0,558,511],
[486,509,496,498,495,474,481,482,443,0,480],
[540,519,543,528,519,531,492,520,490,521,0]])



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
result = np.append(np.array([11, 1001, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,516,492,505,482,505,471,502,472,526],
[507,0,509,498,479,462,502,506,517,473,496],
[485,492,0,497,462,469,487,467,489,477,516],
[509,503,504,0,461,485,448,492,489,481,481],
[496,522,539,540,0,499,494,519,514,484,486],
[519,539,532,516,502,0,497,506,526,483,518],
[496,499,514,553,507,504,0,492,489,517,537],
[530,495,534,509,482,495,509,0,497,504,514],
[499,484,512,512,487,475,512,504,0,489,493],
[529,528,524,520,517,518,484,497,512,0,482],
[475,505,485,520,515,483,464,487,508,519,0]])



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
result = np.append(np.array([11, 1001, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,499,471,478,479,460,460,498,488,471],
[522,0,515,507,516,492,508,493,522,484,514],
[502,486,0,517,505,507,515,478,492,487,483],
[530,494,484,0,508,498,489,495,530,508,505],
[523,485,496,493,0,482,511,478,517,468,507],
[522,509,494,503,519,0,496,502,497,490,507],
[541,493,486,512,490,505,0,480,516,528,494],
[541,508,523,506,523,499,521,0,534,515,528],
[503,479,509,471,484,504,485,467,0,477,477],
[513,517,514,493,533,511,473,486,524,0,518],
[530,487,518,496,494,494,507,473,524,483,0]])



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
result = np.append(np.array([11, 1001, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,511,489,519,518,513,543,549,539,503],
[491,0,489,506,494,496,494,528,503,519,488],
[490,512,0,494,488,514,523,540,512,528,508],
[512,495,507,0,494,500,477,501,529,527,524],
[482,507,513,507,0,491,475,516,506,525,519],
[483,505,487,501,510,0,491,518,504,523,513],
[488,507,478,524,526,510,0,524,527,545,537],
[458,473,461,500,485,483,477,0,487,512,495],
[452,498,489,472,495,497,474,514,0,501,495],
[462,482,473,474,476,478,456,489,500,0,498],
[498,513,493,477,482,488,464,506,506,503,0]])



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
result = np.append(np.array([11, 1001, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,507,488,478,508,505,496,505,482,505],
[507,0,488,502,493,512,507,510,532,503,518],
[494,513,0,503,505,509,521,509,519,496,517],
[513,499,498,0,497,498,514,502,493,498,507],
[523,508,496,504,0,503,514,493,531,522,518],
[493,489,492,503,498,0,513,477,519,482,499],
[496,494,480,487,487,488,0,502,522,503,513],
[505,491,492,499,508,524,499,0,521,481,518],
[496,469,482,508,470,482,479,480,0,490,508],
[519,498,505,503,479,519,498,520,511,0,519],
[496,483,484,494,483,502,488,483,493,482,0]])



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
result = np.append(np.array([11, 1001, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,490,472,506,480,490,476,504,543,511],
[532,0,497,507,544,500,510,513,535,543,506],
[511,504,0,472,533,511,481,513,521,516,502],
[529,494,529,0,522,520,476,528,538,535,520],
[495,457,468,479,0,482,464,508,488,530,501],
[521,501,490,481,519,0,514,520,526,539,528],
[511,491,520,525,537,487,0,523,505,532,522],
[525,488,488,473,493,481,478,0,528,517,516],
[497,466,480,463,513,475,496,473,0,497,499],
[458,458,485,466,471,462,469,484,504,0,461],
[490,495,499,481,500,473,479,485,502,540,0]])



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
result = np.append(np.array([11, 1001, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,475,450,467,482,466,497,521,482,504],
[555,0,512,500,549,499,502,456,531,514,527],
[526,489,0,504,544,508,533,493,506,540,535],
[551,501,497,0,489,538,523,487,532,514,513],
[534,452,457,512,0,483,490,493,525,520,522],
[519,502,493,463,518,0,513,509,555,572,518],
[535,499,468,478,511,488,0,510,513,518,501],
[504,545,508,514,508,492,491,0,507,529,523],
[480,470,495,469,476,446,488,494,0,486,495],
[519,487,461,487,481,429,483,472,515,0,471],
[497,474,466,488,479,483,500,478,506,530,0]])



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
result = np.append(np.array([11, 1001, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,488,502,501,495,465,508,515,505,508],
[472,0,471,469,498,454,452,493,475,485,486],
[513,530,0,499,537,515,497,512,515,501,515],
[499,532,502,0,520,510,478,485,508,498,498],
[500,503,464,481,0,488,481,518,471,505,501],
[506,547,486,491,513,0,501,503,512,512,498],
[536,549,504,523,520,500,0,499,529,521,512],
[493,508,489,516,483,498,502,0,490,516,502],
[486,526,486,493,530,489,472,511,0,502,502],
[496,516,500,503,496,489,480,485,499,0,480],
[493,515,486,503,500,503,489,499,499,521,0]])



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
result = np.append(np.array([11, 1001, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,565,472,520,573,521,474,551,511,515,525],
[436,0,452,492,517,458,536,556,380,528,428],
[529,549,0,504,498,490,522,572,409,570,458],
[481,509,497,0,514,467,455,477,397,453,498],
[428,484,503,487,0,471,462,476,405,496,467],
[480,543,511,534,530,0,473,446,411,522,456],
[527,465,479,546,539,528,0,455,446,502,518],
[450,445,429,524,525,555,546,0,419,503,430],
[490,621,592,604,596,590,555,582,0,581,564],
[486,473,431,548,505,479,499,498,420,0,487],
[476,573,543,503,534,545,483,571,437,514,0]])



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
result = np.append(np.array([11, 1001, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,461,450,552,483,490,491,518,506,495],
[467,0,438,434,520,473,479,476,495,464,476],
[540,563,0,474,550,527,530,525,512,493,521],
[551,567,527,0,555,525,523,545,571,493,540],
[449,481,451,446,0,462,478,460,507,467,458],
[518,528,474,476,539,0,494,495,503,484,498],
[511,522,471,478,523,507,0,503,524,487,493],
[510,525,476,456,541,506,498,0,537,458,533],
[483,506,489,430,494,498,477,464,0,471,478],
[495,537,508,508,534,517,514,543,530,0,501],
[506,525,480,461,543,503,508,468,523,500,0]])



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
result = np.append(np.array([11, 1001, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,488,449,434,465,462,473,441,523,475],
[477,0,472,468,439,457,447,488,476,516,434],
[513,529,0,476,468,471,472,505,482,537,487],
[552,533,525,0,500,511,523,535,550,552,517],
[567,562,533,501,0,532,527,485,517,515,492],
[536,544,530,490,469,0,489,534,482,543,537],
[539,554,529,478,474,512,0,499,511,535,550],
[528,513,496,466,516,467,502,0,498,543,506],
[560,525,519,451,484,519,490,503,0,565,458],
[478,485,464,449,486,458,466,458,436,0,457],
[526,567,514,484,509,464,451,495,543,544,0]])



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
result = np.append(np.array([11, 1001, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,475,496,533,516,484,472,511,498,506],
[519,0,475,504,564,538,513,496,488,500,497],
[526,526,0,547,528,554,519,524,487,505,498],
[505,497,454,0,529,506,491,453,481,461,457],
[468,437,473,472,0,522,485,434,464,498,449],
[485,463,447,495,479,0,480,463,474,475,511],
[517,488,482,510,516,521,0,469,536,488,475],
[529,505,477,548,567,538,532,0,519,520,494],
[490,513,514,520,537,527,465,482,0,507,498],
[503,501,496,540,503,526,513,481,494,0,498],
[495,504,503,544,552,490,526,507,503,503,0]])



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
result = np.append(np.array([11, 1001, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,518,534,518,490,516,510,526,532,525],
[488,0,497,508,494,503,498,499,527,509,504],
[483,504,0,517,479,484,507,489,508,472,517],
[467,493,484,0,487,492,505,487,521,490,511],
[483,507,522,514,0,504,505,502,519,523,506],
[511,498,517,509,497,0,524,499,517,488,524],
[485,503,494,496,496,477,0,477,513,494,494],
[491,502,512,514,499,502,524,0,532,492,504],
[475,474,493,480,482,484,488,469,0,480,493],
[469,492,529,511,478,513,507,509,521,0,511],
[476,497,484,490,495,477,507,497,508,490,0]])



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
result = np.append(np.array([11, 1001, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,486,515,526,525,494,521,488,514,510],
[477,0,488,514,511,505,470,501,492,499,492],
[515,513,0,526,494,500,524,517,508,501,530],
[486,487,475,0,504,499,503,500,475,453,506],
[475,490,507,497,0,510,511,513,471,481,502],
[476,496,501,502,491,0,510,509,481,488,532],
[507,531,477,498,490,491,0,496,479,479,519],
[480,500,484,501,488,492,505,0,491,471,509],
[513,509,493,526,530,520,522,510,0,500,525],
[487,502,500,548,520,513,522,530,501,0,518],
[491,509,471,495,499,469,482,492,476,483,0]])



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
result = np.append(np.array([11, 1001, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,476,501,487,497,491,479,495,501,499],
[515,0,480,527,511,538,503,481,499,528,502],
[525,521,0,515,512,568,526,493,520,530,534],
[500,474,486,0,492,510,479,515,480,503,485],
[514,490,489,509,0,524,508,508,492,503,500],
[504,463,433,491,477,0,495,474,478,491,483],
[510,498,475,522,493,506,0,492,484,495,473],
[522,520,508,486,493,527,509,0,517,505,519],
[506,502,481,521,509,523,517,484,0,531,504],
[500,473,471,498,498,510,506,496,470,0,475],
[502,499,467,516,501,518,528,482,497,526,0]])



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
result = np.append(np.array([11, 1001, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,521,530,488,484,503,508,533,510,513],
[470,0,508,509,464,493,471,475,521,493,476],
[480,493,0,496,460,480,450,485,477,483,482],
[471,492,505,0,480,500,469,497,499,524,497],
[513,537,541,521,0,530,476,515,534,515,504],
[517,508,521,501,471,0,467,507,512,493,517],
[498,530,551,532,525,534,0,528,527,528,536],
[493,526,516,504,486,494,473,0,507,508,494],
[468,480,524,502,467,489,474,494,0,519,490],
[491,508,518,477,486,508,473,493,482,0,479],
[488,525,519,504,497,484,465,507,511,522,0]])



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
result = np.append(np.array([11, 1001, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,478,484,494,504,486,505,481,494,472],
[486,0,479,485,465,476,451,484,488,474,481],
[523,522,0,499,494,548,478,495,512,544,508],
[517,516,502,0,522,500,512,499,499,530,493],
[507,536,507,479,0,518,517,514,514,513,507],
[497,525,453,501,483,0,463,511,481,481,496],
[515,550,523,489,484,538,0,546,498,488,498],
[496,517,506,502,487,490,455,0,481,504,473],
[520,513,489,502,487,520,503,520,0,550,502],
[507,527,457,471,488,520,513,497,451,0,492],
[529,520,493,508,494,505,503,528,499,509,0]])



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
result = np.append(np.array([11, 1001, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,459,525,432,504,500,482,517,504,478],
[487,0,471,472,449,482,456,510,561,512,496],
[542,530,0,529,507,526,499,521,564,491,519],
[476,529,472,0,482,525,470,479,490,479,484],
[569,552,494,519,0,536,485,567,593,554,522],
[497,519,475,476,465,0,502,441,546,499,478],
[501,545,502,531,516,499,0,517,563,485,540],
[519,491,480,522,434,560,484,0,513,508,506],
[484,440,437,511,408,455,438,488,0,474,462],
[497,489,510,522,447,502,516,493,527,0,490],
[523,505,482,517,479,523,461,495,539,511,0]])



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
result = np.append(np.array([11, 1001, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,556,417,459,406,430,480,453,485,414,501],
[445,0,454,498,381,467,404,475,548,438,538],
[584,547,0,618,588,490,522,577,614,592,626],
[542,503,383,0,418,493,481,524,506,451,497],
[595,620,413,583,0,486,551,456,507,514,614],
[571,534,511,508,515,0,478,543,550,471,544],
[521,597,479,520,450,523,0,508,468,505,529],
[548,526,424,477,545,458,493,0,561,532,586],
[516,453,387,495,494,451,533,440,0,445,523],
[587,563,409,550,487,530,496,469,556,0,571],
[500,463,375,504,387,457,472,415,478,430,0]])



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
result = np.append(np.array([11, 1001, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,497,528,464,455,518,464,504,467,506],
[484,0,507,480,463,443,465,407,495,466,486],
[504,494,0,497,497,475,539,507,514,472,488],
[473,521,504,0,460,504,466,451,510,508,477],
[537,538,504,541,0,545,525,459,533,513,524],
[546,558,526,497,456,0,516,467,505,503,490],
[483,536,462,535,476,485,0,442,523,482,506],
[537,594,494,550,542,534,559,0,516,528,523],
[497,506,487,491,468,496,478,485,0,472,495],
[534,535,529,493,488,498,519,473,529,0,566],
[495,515,513,524,477,511,495,478,506,435,0]])



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
result = np.append(np.array([11, 1001, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,490,489,481,491,504,480,490,493,493],
[497,0,490,481,482,500,509,490,502,491,494],
[511,511,0,522,498,496,495,503,498,495,497],
[512,520,479,0,513,510,500,503,503,522,521],
[520,519,503,488,0,499,475,498,518,504,513],
[510,501,505,491,502,0,507,495,501,494,498],
[497,492,506,501,526,494,0,500,494,487,494],
[521,511,498,498,503,506,501,0,506,493,504],
[511,499,503,498,483,500,507,495,0,474,532],
[508,510,506,479,497,507,514,508,527,0,508],
[508,507,504,480,488,503,507,497,469,493,0]])



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
result = np.append(np.array([11, 1001, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,513,548,488,480,490,461,509,499,486],
[493,0,471,513,477,461,464,453,513,484,502],
[488,530,0,525,470,504,498,479,524,513,526],
[453,488,476,0,437,482,481,450,473,479,473],
[513,524,531,564,0,476,519,506,540,515,528],
[521,540,497,519,525,0,510,507,536,521,536],
[511,537,503,520,482,491,0,510,520,514,510],
[540,548,522,551,495,494,491,0,552,498,517],
[492,488,477,528,461,465,481,449,0,500,515],
[502,517,488,522,486,480,487,503,501,0,509],
[515,499,475,528,473,465,491,484,486,492,0]])



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
result = np.append(np.array([11, 1001, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,517,531,506,504,520,488,509,523,526],
[478,0,499,496,494,481,503,464,516,511,516],
[484,502,0,501,479,484,518,487,502,513,501],
[470,505,500,0,482,504,520,479,509,503,514],
[495,507,522,519,0,521,537,503,533,541,547],
[497,520,517,497,480,0,514,482,529,512,524],
[481,498,483,481,464,487,0,445,487,505,498],
[513,537,514,522,498,519,556,0,540,545,552],
[492,485,499,492,468,472,514,461,0,498,497],
[478,490,488,498,460,489,496,456,503,0,498],
[475,485,500,487,454,477,503,449,504,503,0]])



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
result = np.append(np.array([11, 1001, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,567,569,549,504,520,495,522,542,493],
[470,0,522,514,530,495,507,479,507,485,436],
[434,479,0,485,503,439,468,460,452,490,459],
[432,487,516,0,473,498,465,490,506,457,429],
[452,471,498,528,0,474,458,447,487,467,427],
[497,506,562,503,527,0,521,510,510,548,470],
[481,494,533,536,543,480,0,483,509,513,479],
[506,522,541,511,554,491,518,0,542,526,501],
[479,494,549,495,514,491,492,459,0,484,466],
[459,516,511,544,534,453,488,475,517,0,452],
[508,565,542,572,574,531,522,500,535,549,0]])



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
result = np.append(np.array([11, 1001, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,493,446,511,457,463,454,420,453,454],
[517,0,527,483,495,491,478,448,443,456,476],
[508,474,0,487,495,454,491,464,470,453,457],
[555,518,514,0,512,509,488,516,480,490,539],
[490,506,506,489,0,472,482,448,465,475,487],
[544,510,547,492,529,0,509,509,529,519,514],
[538,523,510,513,519,492,0,506,492,489,526],
[547,553,537,485,553,492,495,0,464,481,515],
[581,558,531,521,536,472,509,537,0,506,519],
[548,545,548,511,526,482,512,520,495,0,507],
[547,525,544,462,514,487,475,486,482,494,0]])



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
result = np.append(np.array([11, 1001, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,456,503,523,525,522,501,574,531,480],
[486,0,497,546,567,546,555,508,546,521,492],
[545,504,0,532,549,552,508,498,556,537,509],
[498,455,469,0,510,517,480,511,504,476,494],
[478,434,452,491,0,535,512,533,484,463,501],
[476,455,449,484,466,0,500,488,477,477,471],
[479,446,493,521,489,501,0,506,522,518,481],
[500,493,503,490,468,513,495,0,490,520,487],
[427,455,445,497,517,524,479,511,0,516,468],
[470,480,464,525,538,524,483,481,485,0,488],
[521,509,492,507,500,530,520,514,533,513,0]])



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
result = np.append(np.array([11, 1001, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,519,535,570,498,612,541,553,582,554],
[484,0,561,607,568,510,637,490,520,657,611],
[482,440,0,553,481,462,557,494,522,525,590],
[466,394,448,0,505,459,486,412,396,486,479],
[431,433,520,496,0,442,535,503,465,581,555],
[503,491,539,542,559,0,557,488,509,581,566],
[389,364,444,515,466,444,0,396,439,507,506],
[460,511,507,589,498,513,605,0,521,600,610],
[448,481,479,605,536,492,562,480,0,584,599],
[419,344,476,515,420,420,494,401,417,0,513],
[447,390,411,522,446,435,495,391,402,488,0]])



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
result = np.append(np.array([11, 1001, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,480,539,523,513,508,494,516,507,532],
[473,0,465,524,483,478,469,483,478,494,536],
[521,536,0,539,504,515,516,495,533,494,520],
[462,477,462,0,451,477,481,466,491,474,521],
[478,518,497,550,0,515,509,511,518,481,532],
[488,523,486,524,486,0,488,482,508,480,502],
[493,532,485,520,492,513,0,485,516,496,508],
[507,518,506,535,490,519,516,0,534,514,536],
[485,523,468,510,483,493,485,467,0,491,507],
[494,507,507,527,520,521,505,487,510,0,538],
[469,465,481,480,469,499,493,465,494,463,0]])



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
result = np.append(np.array([11, 1001, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,496,490,480,470,448,486,472,491,484],
[510,0,487,486,484,502,470,486,517,521,502],
[505,514,0,480,501,490,465,510,518,512,527],
[511,515,521,0,473,462,471,493,496,507,522],
[521,517,500,528,0,503,501,529,526,550,524],
[531,499,511,539,498,0,469,513,507,515,524],
[553,531,536,530,500,532,0,536,560,558,525],
[515,515,491,508,472,488,465,0,492,482,496],
[529,484,483,505,475,494,441,509,0,522,524],
[510,480,489,494,451,486,443,519,479,0,472],
[517,499,474,479,477,477,476,505,477,529,0]])



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
result = np.append(np.array([11, 1001, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,470,472,458,516,501,485,445,484,461],
[490,0,528,462,502,523,498,483,461,542,464],
[531,473,0,517,482,548,558,523,511,538,502],
[529,539,484,0,533,556,516,527,493,517,487],
[543,499,519,468,0,535,516,471,490,540,505],
[485,478,453,445,466,0,479,492,442,469,437],
[500,503,443,485,485,522,0,507,485,493,492],
[516,518,478,474,530,509,494,0,505,533,459],
[556,540,490,508,511,559,516,496,0,528,547],
[517,459,463,484,461,532,508,468,473,0,479],
[540,537,499,514,496,564,509,542,454,522,0]])



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
result = np.append(np.array([11, 1001, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,530,510,516,504,519,513,492,488,531],
[512,0,538,499,536,507,541,521,503,537,530],
[471,463,0,463,503,466,512,480,481,478,514],
[491,502,538,0,526,533,547,507,516,507,530],
[485,465,498,475,0,491,493,485,469,467,483],
[497,494,535,468,510,0,513,533,499,499,509],
[482,460,489,454,508,488,0,487,482,503,505],
[488,480,521,494,516,468,514,0,516,502,507],
[509,498,520,485,532,502,519,485,0,497,486],
[513,464,523,494,534,502,498,499,504,0,505],
[470,471,487,471,518,492,496,494,515,496,0]])



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
result = np.append(np.array([11, 1001, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,508,487,496,501,509,517,480,549,523],
[500,0,496,484,492,473,485,503,504,538,494],
[493,505,0,490,468,476,458,486,462,501,490],
[514,517,511,0,524,509,515,506,495,523,521],
[505,509,533,477,0,509,525,486,484,561,496],
[500,528,525,492,492,0,501,533,482,520,509],
[492,516,543,486,476,500,0,504,452,500,521],
[484,498,515,495,515,468,497,0,481,509,507],
[521,497,539,506,517,519,549,520,0,532,510],
[452,463,500,478,440,481,501,492,469,0,506],
[478,507,511,480,505,492,480,494,491,495,0]])



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
result = np.append(np.array([11, 1001, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,514,506,499,486,512,492,505,507,514],
[506,0,526,528,515,548,553,522,519,520,498],
[487,475,0,512,500,474,496,470,496,492,499],
[495,473,489,0,497,498,487,477,508,482,504],
[502,486,501,504,0,533,518,496,510,509,525],
[515,453,527,503,468,0,502,499,487,506,526],
[489,448,505,514,483,499,0,494,488,500,521],
[509,479,531,524,505,502,507,0,529,511,531],
[496,482,505,493,491,514,513,472,0,506,492],
[494,481,509,519,492,495,501,490,495,0,518],
[487,503,502,497,476,475,480,470,509,483,0]])



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
result = np.append(np.array([11, 1001, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,486,486,507,482,483,483,487,499,517],
[490,0,487,464,512,495,473,506,493,480,488],
[515,514,0,491,530,497,503,528,510,513,516],
[515,537,510,0,526,496,510,531,512,514,505],
[494,489,471,475,0,482,505,515,470,494,492],
[519,506,504,505,519,0,506,516,493,514,496],
[518,528,498,491,496,495,0,525,492,528,509],
[518,495,473,470,486,485,476,0,502,506,486],
[514,508,491,489,531,508,509,499,0,472,521],
[502,521,488,487,507,487,473,495,529,0,510],
[484,513,485,496,509,505,492,515,480,491,0]])



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
result = np.append(np.array([11, 1001, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,489,530,526,476,478,470,477,476,507],
[510,0,515,507,507,507,505,481,497,526,489],
[512,486,0,514,475,473,458,462,492,482,454],
[471,494,487,0,472,469,456,464,464,492,459],
[475,494,526,529,0,501,482,463,470,511,484],
[525,494,528,532,500,0,495,476,518,530,509],
[523,496,543,545,519,506,0,496,492,538,519],
[531,520,539,537,538,525,505,0,518,497,501],
[524,504,509,537,531,483,509,483,0,508,474],
[525,475,519,509,490,471,463,504,493,0,460],
[494,512,547,542,517,492,482,500,527,541,0]])



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
result = np.append(np.array([11, 1001, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,686,592,705,441,562,654,776,515,519,735],
[315,0,608,563,509,322,563,618,408,626,795],
[409,393,0,617,375,389,456,473,602,511,576],
[296,438,384,0,240,391,459,507,297,237,423],
[560,492,626,761,0,556,506,580,758,512,656],
[439,679,612,610,445,0,598,724,603,613,656],
[347,438,545,542,495,403,0,454,540,650,566],
[225,383,528,494,421,277,547,0,332,487,666],
[486,593,399,704,243,398,461,669,0,415,714],
[482,375,490,764,489,388,351,514,586,0,643],
[266,206,425,578,345,345,435,335,287,358,0]])



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
result = np.append(np.array([11, 1001, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,499,513,550,476,556,514,576,427,510],
[449,0,464,496,457,421,443,401,501,394,416],
[502,537,0,539,605,495,527,548,511,434,496],
[488,505,462,0,502,458,449,483,481,415,476],
[451,544,396,499,0,430,454,438,400,381,433],
[525,580,506,543,571,0,553,565,536,458,501],
[445,558,474,552,547,448,0,471,470,434,491],
[487,600,453,518,563,436,530,0,583,508,526],
[425,500,490,520,601,465,531,418,0,385,484],
[574,607,567,586,620,543,567,493,616,0,591],
[491,585,505,525,568,500,510,475,517,410,0]])



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
result = np.append(np.array([11, 1001, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,505,508,527,530,533,516,511,487,510],
[489,0,474,482,476,485,524,486,473,467,492],
[496,527,0,483,487,493,522,494,474,500,507],
[493,519,518,0,505,512,524,509,496,496,520],
[474,525,514,496,0,528,537,511,494,504,539],
[471,516,508,489,473,0,525,477,487,484,487],
[468,477,479,477,464,476,0,474,458,458,487],
[485,515,507,492,490,524,527,0,490,491,479],
[490,528,527,505,507,514,543,511,0,509,497],
[514,534,501,505,497,517,543,510,492,0,530],
[491,509,494,481,462,514,514,522,504,471,0]])



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
result = np.append(np.array([11, 1001, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,496,513,485,470,510,488,521,497,494],
[512,0,494,472,501,494,506,499,509,491,499],
[505,507,0,512,495,508,511,491,518,497,487],
[488,529,489,0,517,497,496,504,526,516,505],
[516,500,506,484,0,509,494,488,522,498,503],
[531,507,493,504,492,0,501,499,525,484,490],
[491,495,490,505,507,500,0,489,523,487,483],
[513,502,510,497,513,502,512,0,531,525,531],
[480,492,483,475,479,476,478,470,0,474,468],
[504,510,504,485,503,517,514,476,527,0,488],
[507,502,514,496,498,511,518,470,533,513,0]])



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
result = np.append(np.array([11, 1001, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,502,493,503,480,519,503,508,509,486],
[483,0,512,498,520,485,517,500,516,505,497],
[499,489,0,484,509,488,516,512,503,500,488],
[508,503,517,0,533,505,533,516,516,521,500],
[498,481,492,468,0,477,514,507,511,502,495],
[521,516,513,496,524,0,526,514,517,525,514],
[482,484,485,468,487,475,0,488,501,495,486],
[498,501,489,485,494,487,513,0,507,503,478],
[493,485,498,485,490,484,500,494,0,490,479],
[492,496,501,480,499,476,506,498,511,0,497],
[515,504,513,501,506,487,515,523,522,504,0]])



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
result = np.append(np.array([11, 1001, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,505,503,483,495,526,509,502,486,504],
[498,0,525,508,481,521,491,504,504,493,492],
[496,476,0,499,489,488,466,490,480,490,498],
[498,493,502,0,504,506,479,512,500,492,505],
[518,520,512,497,0,502,496,521,502,512,522],
[506,480,513,495,499,0,498,489,495,510,485],
[475,510,535,522,505,503,0,503,488,518,516],
[492,497,511,489,480,512,498,0,491,482,516],
[499,497,521,501,499,506,513,510,0,489,505],
[515,508,511,509,489,491,483,519,512,0,508],
[497,509,503,496,479,516,485,485,496,493,0]])



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
result = np.append(np.array([11, 1001, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,514,557,509,515,522,507,510,492,552],
[497,0,500,534,486,505,510,506,524,493,527],
[487,501,0,515,495,507,500,495,514,495,546],
[444,467,486,0,480,478,446,487,482,467,495],
[492,515,506,521,0,512,514,509,523,513,537],
[486,496,494,523,489,0,533,504,540,458,551],
[479,491,501,555,487,468,0,492,483,508,532],
[494,495,506,514,492,497,509,0,520,475,508],
[491,477,487,519,478,461,518,481,0,481,522],
[509,508,506,534,488,543,493,526,520,0,522],
[449,474,455,506,464,450,469,493,479,479,0]])



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
result = np.append(np.array([11, 1001, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,493,515,494,523,510,506,486,478,520],
[502,0,474,475,481,487,476,525,486,472,541],
[508,527,0,496,491,522,536,521,515,502,537],
[486,526,505,0,502,527,531,545,498,514,537],
[507,520,510,499,0,512,492,500,493,494,511],
[478,514,479,474,489,0,513,499,492,479,541],
[491,525,465,470,509,488,0,528,504,481,524],
[495,476,480,456,501,502,473,0,478,512,517],
[515,515,486,503,508,509,497,523,0,498,542],
[523,529,499,487,507,522,520,489,503,0,533],
[481,460,464,464,490,460,477,484,459,468,0]])



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
result = np.append(np.array([11, 1001, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,459,570,545,513,491,464,483,532,523],
[512,0,497,551,518,518,476,505,492,528,532],
[542,504,0,551,542,512,504,476,501,548,555],
[431,450,450,0,487,478,461,428,416,473,469],
[456,483,459,514,0,487,471,447,469,495,500],
[488,483,489,523,514,0,472,500,481,546,533],
[510,525,497,540,530,529,0,496,474,537,541],
[537,496,525,573,554,501,505,0,527,551,559],
[518,509,500,585,532,520,527,474,0,541,564],
[469,473,453,528,506,455,464,450,460,0,494],
[478,469,446,532,501,468,460,442,437,507,0]])



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
result = np.append(np.array([11, 1001, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,452,514,453,475,467,472,485,472,429,458],
[549,0,524,504,505,507,513,517,500,490,483],
[487,477,0,463,495,435,500,475,480,479,466],
[548,497,538,0,494,487,537,521,517,503,512],
[526,496,506,507,0,487,492,487,488,479,472],
[534,494,566,514,514,0,532,492,513,532,520],
[529,488,501,464,509,469,0,510,487,472,481],
[516,484,526,480,514,509,491,0,477,494,467],
[529,501,521,484,513,488,514,524,0,502,500],
[572,511,522,498,522,469,529,507,499,0,506],
[543,518,535,489,529,481,520,534,501,495,0]])



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
result = np.append(np.array([11, 1001, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,493,481,478,496,482,478,491,494,475],
[497,0,484,468,510,475,504,480,511,487,479],
[508,517,0,501,493,495,505,496,513,504,495],
[520,533,500,0,507,499,505,496,505,520,516],
[523,491,508,494,0,505,511,493,532,508,525],
[505,526,506,502,496,0,497,510,498,525,523],
[519,497,496,496,490,504,0,487,517,502,505],
[523,521,505,505,508,491,514,0,515,517,515],
[510,490,488,496,469,503,484,486,0,498,505],
[507,514,497,481,493,476,499,484,503,0,505],
[526,522,506,485,476,478,496,486,496,496,0]])



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
result = np.append(np.array([11, 1001, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,492,513,505,520,536,527,503,508,527],
[487,0,490,502,494,496,505,512,467,502,518],
[509,511,0,527,488,497,551,541,503,517,531],
[488,499,474,0,472,479,515,524,491,474,501],
[496,507,513,529,0,517,529,524,495,515,524],
[481,505,504,522,484,0,526,541,492,513,514],
[465,496,450,486,472,475,0,497,457,486,486],
[474,489,460,477,477,460,504,0,465,506,493],
[498,534,498,510,506,509,544,536,0,522,515],
[493,499,484,527,486,488,515,495,479,0,495],
[474,483,470,500,477,487,515,508,486,506,0]])



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
result = np.append(np.array([11, 1001, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,488,508,516,498,531,487,510,508,503],
[507,0,487,487,491,491,510,497,499,506,479],
[513,514,0,520,525,494,536,517,514,513,521],
[493,514,481,0,507,492,524,485,490,491,507],
[485,510,476,494,0,470,500,489,489,514,480],
[503,510,507,509,531,0,533,502,512,521,489],
[470,491,465,477,501,468,0,481,484,475,474],
[514,504,484,516,512,499,520,0,516,491,508],
[491,502,487,511,512,489,517,485,0,495,492],
[493,495,488,510,487,480,526,510,506,0,502],
[498,522,480,494,521,512,527,493,509,499,0]])



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
result = np.append(np.array([11, 1001, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,500,486,494,487,512,513,515,498,512],
[500,0,507,501,509,496,500,506,503,500,495],
[501,494,0,515,512,495,526,546,541,528,526],
[515,500,486,0,500,495,524,518,527,499,511],
[507,492,489,501,0,514,477,516,522,502,505],
[514,505,506,506,487,0,501,503,531,511,517],
[489,501,475,477,524,500,0,520,559,528,524],
[488,495,455,483,485,498,481,0,505,489,501],
[486,498,460,474,479,470,442,496,0,489,478],
[503,501,473,502,499,490,473,512,512,0,510],
[489,506,475,490,496,484,477,500,523,491,0]])



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
result = np.append(np.array([11, 1001, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,519,544,510,503,495,480,508,490,505],
[488,0,492,494,472,483,487,467,484,465,470],
[482,509,0,532,506,498,495,474,510,480,487],
[457,507,469,0,482,479,499,468,495,482,477],
[491,529,495,519,0,509,504,507,526,511,530],
[498,518,503,522,492,0,508,496,503,482,499],
[506,514,506,502,497,493,0,492,510,484,502],
[521,534,527,533,494,505,509,0,512,520,514],
[493,517,491,506,475,498,491,489,0,486,497],
[511,536,521,519,490,519,517,481,515,0,496],
[496,531,514,524,471,502,499,487,504,505,0]])



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
result = np.append(np.array([11, 1001, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,513,547,506,518,497,524,523,526,521],
[470,0,498,519,471,499,484,520,494,486,469],
[488,503,0,500,496,513,474,505,466,539,518],
[454,482,501,0,497,464,483,488,426,496,497],
[495,530,505,504,0,500,478,493,513,522,500],
[483,502,488,537,501,0,469,526,458,512,500],
[504,517,527,518,523,532,0,557,470,539,512],
[477,481,496,513,508,475,444,0,456,532,484],
[478,507,535,575,488,543,531,545,0,515,538],
[475,515,462,505,479,489,462,469,486,0,498],
[480,532,483,504,501,501,489,517,463,503,0]])



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
result = np.append(np.array([11, 1001, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,395,488,436,519,429,445,498,527,487,447],
[606,0,536,579,527,531,507,545,621,495,544],
[513,465,0,536,467,489,458,444,595,479,501],
[565,422,465,0,431,507,455,507,518,508,489],
[482,474,534,570,0,557,454,495,556,522,478],
[572,470,512,494,444,0,494,509,527,463,451],
[556,494,543,546,547,507,0,518,563,484,537],
[503,456,557,494,506,492,483,0,552,444,555],
[474,380,406,483,445,474,438,449,0,456,447],
[514,506,522,493,479,538,517,557,545,0,572],
[554,457,500,512,523,550,464,446,554,429,0]])



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
result = np.append(np.array([11, 1001, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,504,482,506,503,511,513,509,478,500],
[498,0,485,475,484,476,487,495,489,482,482],
[497,516,0,455,479,486,473,475,465,487,481],
[519,526,546,0,508,522,503,528,506,491,498],
[495,517,522,493,0,481,490,504,504,505,502],
[498,525,515,479,520,0,501,508,520,496,500],
[490,514,528,498,511,500,0,500,508,502,492],
[488,506,526,473,497,493,501,0,517,510,494],
[492,512,536,495,497,481,493,484,0,497,503],
[523,519,514,510,496,505,499,491,504,0,513],
[501,519,520,503,499,501,509,507,498,488,0]])



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
result = np.append(np.array([11, 1001, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,455,519,479,285,688,462,432,554,366],
[473,0,346,438,277,283,596,311,433,493,282],
[546,655,0,603,446,377,621,383,583,482,446],
[482,563,398,0,354,419,566,376,388,525,513],
[522,724,555,647,0,510,597,466,561,529,559],
[716,718,624,582,491,0,716,527,695,537,293],
[313,405,380,435,404,285,0,283,457,298,262],
[539,690,618,625,535,474,718,0,584,482,523],
[569,568,418,613,440,306,544,417,0,505,345],
[447,508,519,476,472,464,703,519,496,0,427],
[635,719,555,488,442,708,739,478,656,574,0]])



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
result = np.append(np.array([11, 1001, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,461,482,518,450,483,457,516,464,488],
[472,0,476,475,481,450,447,463,458,449,495],
[540,525,0,487,533,492,488,484,486,500,516],
[519,526,514,0,493,500,504,469,505,493,520],
[483,520,468,508,0,481,469,493,493,502,520],
[551,551,509,501,520,0,484,519,521,501,535],
[518,554,513,497,532,517,0,535,534,505,505],
[544,538,517,532,508,482,466,0,522,518,503],
[485,543,515,496,508,480,467,479,0,493,531],
[537,552,501,508,499,500,496,483,508,0,500],
[513,506,485,481,481,466,496,498,470,501,0]])



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
result = np.append(np.array([11, 1001, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,520,493,527,473,510,523,520,503,539],
[503,0,529,543,515,499,536,512,527,534,544],
[481,472,0,516,522,485,502,475,503,516,527],
[508,458,485,0,494,466,502,519,519,496,532],
[474,486,479,507,0,452,512,490,539,469,520],
[528,502,516,535,549,0,496,503,546,506,516],
[491,465,499,499,489,505,0,493,500,490,536],
[478,489,526,482,511,498,508,0,489,484,528],
[481,474,498,482,462,455,501,512,0,439,540],
[498,467,485,505,532,495,511,517,562,0,517],
[462,457,474,469,481,485,465,473,461,484,0]])



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
result = np.append(np.array([11, 1001, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,519,515,494,488,491,513,469,467,477],
[501,0,505,542,480,496,504,544,513,467,501],
[482,496,0,500,494,482,494,511,505,483,477],
[486,459,501,0,486,475,479,514,504,470,449],
[507,521,507,515,0,505,489,489,496,468,479],
[513,505,519,526,496,0,502,511,495,482,482],
[510,497,507,522,512,499,0,514,508,490,510],
[488,457,490,487,512,490,487,0,492,450,478],
[532,488,496,497,505,506,493,509,0,500,492],
[534,534,518,531,533,519,511,551,501,0,496],
[524,500,524,552,522,519,491,523,509,505,0]])



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
result = np.append(np.array([11, 1001, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,460,501,472,474,552,576,472,530,383,478],
[541,0,522,535,537,554,622,458,534,450,517],
[500,479,0,511,493,537,543,507,546,415,504],
[529,466,490,0,511,543,557,465,552,416,496],
[527,464,508,490,0,512,563,485,481,424,466],
[449,447,464,458,489,0,523,442,518,418,500],
[425,379,458,444,438,478,0,435,515,332,443],
[529,543,494,536,516,559,566,0,518,503,530],
[471,467,455,449,520,483,486,483,0,409,425],
[618,551,586,585,577,583,669,498,592,0,591],
[523,484,497,505,535,501,558,471,576,410,0]])



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
result = np.append(np.array([11, 1001, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,465,461,568,477,494,497,493,447,499],
[516,0,486,437,476,496,436,444,481,474,533],
[536,515,0,469,549,488,485,436,534,571,476],
[540,564,532,0,560,503,474,454,601,516,511],
[433,525,452,441,0,414,466,479,517,423,452],
[524,505,513,498,587,0,495,422,471,467,553],
[507,565,516,527,535,506,0,480,600,504,537],
[504,557,565,547,522,579,521,0,544,514,495],
[508,520,467,400,484,530,401,457,0,479,496],
[554,527,430,485,578,534,497,487,522,0,483],
[502,468,525,490,549,448,464,506,505,518,0]])



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
result = np.append(np.array([11, 1001, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,499,503,498,509,505,492,502,501,470],
[489,0,472,483,492,481,496,493,498,482,466],
[502,529,0,511,506,504,526,491,501,514,483],
[498,518,490,0,501,498,484,506,501,518,470],
[503,509,495,500,0,513,502,485,532,521,478],
[492,520,497,503,488,0,500,482,511,492,460],
[496,505,475,517,499,501,0,491,487,507,471],
[509,508,510,495,516,519,510,0,531,517,508],
[499,503,500,500,469,490,514,470,0,495,481],
[500,519,487,483,480,509,494,484,506,0,480],
[531,535,518,531,523,541,530,493,520,521,0]])



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
result = np.append(np.array([11, 1001, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,528,511,499,498,501,493,485,487,495],
[497,0,516,538,476,496,518,496,472,486,486],
[473,485,0,505,461,482,466,467,473,467,447],
[490,463,496,0,439,480,480,470,475,456,470],
[502,525,540,562,0,485,499,521,513,495,514],
[503,505,519,521,516,0,517,510,466,484,484],
[500,483,535,521,502,484,0,487,496,491,465],
[508,505,534,531,480,491,514,0,485,473,489],
[516,529,528,526,488,535,505,516,0,511,516],
[514,515,534,545,506,517,510,528,490,0,492],
[506,515,554,531,487,517,536,512,485,509,0]])



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
result = np.append(np.array([11, 1001, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,510,506,514,514,523,495,523,503,510],
[522,0,517,538,515,551,526,488,528,534,525],
[491,484,0,552,528,531,528,510,510,518,505],
[495,463,449,0,501,498,485,475,522,499,492],
[487,486,473,500,0,498,471,474,501,520,504],
[487,450,470,503,503,0,498,491,507,511,498],
[478,475,473,516,530,503,0,458,499,509,486],
[506,513,491,526,527,510,543,0,525,510,515],
[478,473,491,479,500,494,502,476,0,525,501],
[498,467,483,502,481,490,492,491,476,0,503],
[491,476,496,509,497,503,515,486,500,498,0]])



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
result = np.append(np.array([11, 1001, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,470,477,448,466,434,506,451,488,456],
[500,0,517,512,482,554,489,507,499,506,502],
[531,484,0,504,439,524,478,504,495,540,513],
[524,489,497,0,435,479,495,491,466,495,504],
[553,519,562,566,0,507,503,531,567,486,501],
[535,447,477,522,494,0,521,511,497,483,530],
[567,512,523,506,498,480,0,536,528,472,524],
[495,494,497,510,470,490,465,0,464,471,526],
[550,502,506,535,434,504,473,537,0,549,482],
[513,495,461,506,515,518,529,530,452,0,480],
[545,499,488,497,500,471,477,475,519,521,0]])



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
result = np.append(np.array([11, 1001, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,509,498,512,523,503,509,497,520,502],
[522,0,486,507,516,503,483,509,515,505,516],
[492,515,0,495,499,498,497,511,513,508,528],
[503,494,506,0,505,494,493,494,517,500,515],
[489,485,502,496,0,506,497,492,501,513,507],
[478,498,503,507,495,0,468,501,505,515,512],
[498,518,504,508,504,533,0,496,513,515,515],
[492,492,490,507,509,500,505,0,527,512,500],
[504,486,488,484,500,496,488,474,0,511,496],
[481,496,493,501,488,486,486,489,490,0,490],
[499,485,473,486,494,489,486,501,505,511,0]])



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
result = np.append(np.array([11, 1001, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,346,429,465,348,432,482,473,462,407,543],
[655,0,748,663,578,665,744,479,578,608,633],
[572,253,0,466,519,558,578,470,568,576,525],
[536,338,535,0,597,431,692,432,463,562,535],
[653,423,482,404,0,592,549,426,676,491,625],
[569,336,443,570,409,0,583,358,419,509,498],
[519,257,423,309,452,418,0,435,440,412,462],
[528,522,531,569,575,643,566,0,572,485,591],
[539,423,433,538,325,582,561,429,0,506,573],
[594,393,425,439,510,492,589,516,495,0,531],
[458,368,476,466,376,503,539,410,428,470,0]])



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
result = np.append(np.array([11, 1001, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,486,519,495,470,488,499,496,498,512],
[505,0,490,544,485,519,520,494,506,516,521],
[515,511,0,540,501,485,508,522,505,525,509],
[482,457,461,0,462,471,468,494,466,457,471],
[506,516,500,539,0,508,514,528,514,506,538],
[531,482,516,530,493,0,506,524,514,520,527],
[513,481,493,533,487,495,0,503,460,499,490],
[502,507,479,507,473,477,498,0,469,495,500],
[505,495,496,535,487,487,541,532,0,487,526],
[503,485,476,544,495,481,502,506,514,0,501],
[489,480,492,530,463,474,511,501,475,500,0]])



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
result = np.append(np.array([11, 1001, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,512,491,501,514,499,502,520,504,509],
[489,0,503,503,491,504,492,512,517,511,485],
[489,498,0,504,490,504,505,539,548,483,485],
[510,498,497,0,502,520,503,478,529,519,487],
[500,510,511,499,0,518,507,501,544,501,486],
[487,497,497,481,483,0,503,501,524,493,496],
[502,509,496,498,494,498,0,509,526,511,485],
[499,489,462,523,500,500,492,0,525,519,483],
[481,484,453,472,457,477,475,476,0,482,466],
[497,490,518,482,500,508,490,482,519,0,477],
[492,516,516,514,515,505,516,518,535,524,0]])



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
result = np.append(np.array([11, 1001, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,508,515,546,480,473,521,502,538,489],
[494,0,507,523,516,500,508,508,496,514,521],
[493,494,0,511,557,517,506,496,540,551,505],
[486,478,490,0,533,540,554,522,509,509,529],
[455,485,444,468,0,517,452,481,488,482,472],
[521,501,484,461,484,0,509,476,510,509,472],
[528,493,495,447,549,492,0,449,538,525,495],
[480,493,505,479,520,525,552,0,515,564,527],
[499,505,461,492,513,491,463,486,0,517,470],
[463,487,450,492,519,492,476,437,484,0,484],
[512,480,496,472,529,529,506,474,531,517,0]])



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
result = np.append(np.array([11, 1001, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,464,524,524,442,520,527,455,497,538],
[499,0,513,501,504,458,528,508,423,461,516],
[537,488,0,510,543,480,552,535,485,482,530],
[477,500,491,0,524,510,561,509,485,500,509],
[477,497,458,477,0,493,510,495,479,471,521],
[559,543,521,491,508,0,539,533,493,525,527],
[481,473,449,440,491,462,0,456,397,471,511],
[474,493,466,492,506,468,545,0,422,489,506],
[546,578,516,516,522,508,604,579,0,496,561],
[504,540,519,501,530,476,530,512,505,0,554],
[463,485,471,492,480,474,490,495,440,447,0]])



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
result = np.append(np.array([11, 1001, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,487,533,508,512,506,503,510,489,470],
[526,0,495,508,513,496,478,518,497,489,509],
[514,506,0,516,510,480,494,514,544,525,515],
[468,493,485,0,485,475,462,501,500,503,504],
[493,488,491,516,0,484,479,492,531,500,503],
[489,505,521,526,517,0,494,514,511,530,551],
[495,523,507,539,522,507,0,503,530,504,513],
[498,483,487,500,509,487,498,0,507,504,517],
[491,504,457,501,470,490,471,494,0,510,509],
[512,512,476,498,501,471,497,497,491,0,524],
[531,492,486,497,498,450,488,484,492,477,0]])



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
result = np.append(np.array([11, 1001, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,507,493,502,508,490,491,496,493,549],
[524,0,517,497,535,540,510,496,517,516,541],
[494,484,0,483,515,504,480,496,481,501,523],
[508,504,518,0,529,539,495,501,504,524,539],
[499,466,486,472,0,524,487,487,496,498,534],
[493,461,497,462,477,0,462,469,473,513,525],
[511,491,521,506,514,539,0,501,495,523,533],
[510,505,505,500,514,532,500,0,509,522,520],
[505,484,520,497,505,528,506,492,0,519,532],
[508,485,500,477,503,488,478,479,482,0,521],
[452,460,478,462,467,476,468,481,469,480,0]])



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
result = np.append(np.array([11, 1001, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,544,524,568,496,539,523,557,590,539],
[469,0,557,577,472,506,540,512,551,548,532],
[457,444,0,467,546,470,561,429,506,542,452],
[477,424,534,0,533,478,482,536,497,484,470],
[433,529,455,468,0,498,505,472,475,521,580],
[505,495,531,523,503,0,522,555,527,564,556],
[462,461,440,519,496,479,0,465,495,498,493],
[478,489,572,465,529,446,536,0,474,501,488],
[444,450,495,504,526,474,506,527,0,515,496],
[411,453,459,517,480,437,503,500,486,0,491],
[462,469,549,531,421,445,508,513,505,510,0]])



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
result = np.append(np.array([11, 1001, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,503,539,540,529,509,497,489,512,531],
[472,0,488,533,487,493,500,501,481,477,529],
[498,513,0,551,509,526,481,494,466,480,508],
[462,468,450,0,444,460,447,516,485,494,510],
[461,514,492,557,0,479,507,513,471,499,515],
[472,508,475,541,522,0,440,471,467,491,525],
[492,501,520,554,494,561,0,500,508,495,603],
[504,500,507,485,488,530,501,0,468,508,534],
[512,520,535,516,530,534,493,533,0,498,525],
[489,524,521,507,502,510,506,493,503,0,523],
[470,472,493,491,486,476,398,467,476,478,0]])



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
result = np.append(np.array([11, 1001, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,505,509,501,502,506,510,504,476,489],
[501,0,502,491,483,490,473,491,488,469,480],
[496,499,0,490,510,531,515,521,537,489,516],
[492,510,511,0,505,522,488,500,507,460,510],
[500,518,491,496,0,504,492,500,509,478,508],
[499,511,470,479,497,0,510,502,511,460,509],
[495,528,486,513,509,491,0,504,517,480,511],
[491,510,480,501,501,499,497,0,508,513,489],
[497,513,464,494,492,490,484,493,0,470,503],
[525,532,512,541,523,541,521,488,531,0,519],
[512,521,485,491,493,492,490,512,498,482,0]])



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
result = np.append(np.array([11, 1001, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,544,502,511,511,510,495,502,516,550,509],
[457,0,464,476,500,490,476,480,482,511,491],
[499,537,0,537,526,536,505,518,536,550,544],
[490,525,464,0,507,516,494,491,490,520,523],
[490,501,475,494,0,503,489,477,489,517,520],
[491,511,465,485,498,0,493,477,490,514,496],
[506,525,496,507,512,508,0,496,514,524,518],
[499,521,483,510,524,524,505,0,519,539,542],
[485,519,465,511,512,511,487,482,0,536,523],
[451,490,451,481,484,487,477,462,465,0,487],
[492,510,457,478,481,505,483,459,478,514,0]])



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
result = np.append(np.array([11, 1001, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,514,509,496,498,502,532,502,523,508],
[479,0,469,516,499,471,475,528,481,502,477],
[487,532,0,514,505,485,503,532,494,493,493],
[492,485,487,0,506,497,464,516,497,507,491],
[505,502,496,495,0,509,486,519,495,493,507],
[503,530,516,504,492,0,489,534,491,511,517],
[499,526,498,537,515,512,0,542,539,507,516],
[469,473,469,485,482,467,459,0,467,467,466],
[499,520,507,504,506,510,462,534,0,488,493],
[478,499,508,494,508,490,494,534,513,0,511],
[493,524,508,510,494,484,485,535,508,490,0]])



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
result = np.append(np.array([11, 1001, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,522,476,511,508,502,551,544,493,521],
[471,0,496,475,467,445,464,500,498,512,464],
[479,505,0,494,477,489,444,511,519,489,495],
[525,526,507,0,499,506,500,490,557,521,519],
[490,534,524,502,0,517,476,510,522,515,502],
[493,556,512,495,484,0,465,525,544,565,505],
[499,537,557,501,525,536,0,524,548,505,506],
[450,501,490,511,491,476,477,0,500,519,466],
[457,503,482,444,479,457,453,501,0,493,470],
[508,489,512,480,486,436,496,482,508,0,477],
[480,537,506,482,499,496,495,535,531,524,0]])



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
result = np.append(np.array([11, 1001, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,454,442,527,460,469,498,468,485,462],
[529,0,457,474,556,450,470,499,493,502,505],
[547,544,0,511,583,504,499,523,512,513,528],
[559,527,490,0,553,523,519,481,521,529,528],
[474,445,418,448,0,455,455,460,436,439,440],
[541,551,497,478,546,0,480,516,505,485,488],
[532,531,502,482,546,521,0,502,526,528,502],
[503,502,478,520,541,485,499,0,506,535,516],
[533,508,489,480,565,496,475,495,0,502,513],
[516,499,488,472,562,516,473,466,499,0,484],
[539,496,473,473,561,513,499,485,488,517,0]])



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
result = np.append(np.array([11, 1001, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,523,509,522,487,511,510,504,524,531],
[474,0,500,502,517,482,497,494,485,505,515],
[478,501,0,492,496,480,481,516,480,501,515],
[492,499,509,0,531,500,506,522,499,527,524],
[479,484,505,470,0,458,497,475,450,485,504],
[514,519,521,501,543,0,511,504,496,519,539],
[490,504,520,495,504,490,0,521,470,503,518],
[491,507,485,479,526,497,480,0,495,513,510],
[497,516,521,502,551,505,531,506,0,538,528],
[477,496,500,474,516,482,498,488,463,0,504],
[470,486,486,477,497,462,483,491,473,497,0]])



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
result = np.append(np.array([11, 1001, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,536,514,527,561,509,567,521,514,499],
[471,0,493,505,484,525,448,525,465,464,532],
[465,508,0,496,442,524,448,497,495,485,505],
[487,496,505,0,463,526,463,538,491,509,482],
[474,517,559,538,0,547,471,525,531,496,527],
[440,476,477,475,454,0,491,503,475,487,470],
[492,553,553,538,530,510,0,552,522,513,537],
[434,476,504,463,476,498,449,0,432,489,497],
[480,536,506,510,470,526,479,569,0,500,480],
[487,537,516,492,505,514,488,512,501,0,515],
[502,469,496,519,474,531,464,504,521,486,0]])



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
result = np.append(np.array([11, 1001, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,478,487,518,534,515,529,504,520,504],
[494,0,542,498,518,534,516,525,502,545,528],
[523,459,0,498,472,501,500,521,490,534,508],
[514,503,503,0,507,503,511,516,485,514,512],
[483,483,529,494,0,524,501,514,483,524,516],
[467,467,500,498,477,0,490,486,468,480,495],
[486,485,501,490,500,511,0,511,490,526,507],
[472,476,480,485,487,515,490,0,480,507,486],
[497,499,511,516,518,533,511,521,0,542,511],
[481,456,467,487,477,521,475,494,459,0,495],
[497,473,493,489,485,506,494,515,490,506,0]])



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
result = np.append(np.array([11, 1001, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,481,484,495,479,505,489,511,515,489],
[470,0,476,495,484,475,501,485,500,471,484],
[520,525,0,516,494,512,531,508,513,525,500],
[517,506,485,0,513,527,520,490,490,499,510],
[506,517,507,488,0,491,494,491,500,501,485],
[522,526,489,474,510,0,509,491,518,510,484],
[496,500,470,481,507,492,0,496,510,498,483],
[512,516,493,511,510,510,505,0,524,504,503],
[490,501,488,511,501,483,491,477,0,514,489],
[486,530,476,502,500,491,503,497,487,0,481],
[512,517,501,491,516,517,518,498,512,520,0]])



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
result = np.append(np.array([11, 1001, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,462,455,485,497,459,464,491,486,442],
[503,0,506,474,474,544,490,481,491,479,472],
[539,495,0,488,521,516,498,502,516,495,492],
[546,527,513,0,502,521,488,504,530,488,494],
[516,527,480,499,0,541,490,498,511,478,456],
[504,457,485,480,460,0,460,479,495,476,462],
[542,511,503,513,511,541,0,517,552,515,488],
[537,520,499,497,503,522,484,0,538,514,475],
[510,510,485,471,490,506,449,463,0,464,469],
[515,522,506,513,523,525,486,487,537,0,520],
[559,529,509,507,545,539,513,526,532,481,0]])



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
result = np.append(np.array([11, 1001, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,527,494,536,505,531,509,520,496,510],
[456,0,484,474,530,475,483,460,497,468,461],
[474,517,0,479,523,475,506,486,512,478,489],
[507,527,522,0,545,519,499,506,516,505,509],
[465,471,478,456,0,478,477,471,477,496,453],
[496,526,526,482,523,0,500,516,521,486,501],
[470,518,495,502,524,501,0,480,512,473,470],
[492,541,515,495,530,485,521,0,540,499,515],
[481,504,489,485,524,480,489,461,0,466,517],
[505,533,523,496,505,515,528,502,535,0,493],
[491,540,512,492,548,500,531,486,484,508,0]])



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
result = np.append(np.array([11, 1001, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,498,461,524,455,494,482,493,478,481],
[494,0,512,512,532,496,492,469,501,508,456],
[503,489,0,481,489,501,503,486,501,511,495],
[540,489,520,0,550,531,541,524,516,497,502],
[477,469,512,451,0,468,491,483,501,484,470],
[546,505,500,470,533,0,498,531,548,530,472],
[507,509,498,460,510,503,0,471,510,514,466],
[519,532,515,477,518,470,530,0,510,490,498],
[508,500,500,485,500,453,491,491,0,488,488],
[523,493,490,504,517,471,487,511,513,0,503],
[520,545,506,499,531,529,535,503,513,498,0]])



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
result = np.append(np.array([11, 1001, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,473,474,494,488,501,465,490,490,466],
[497,0,509,519,494,503,490,516,498,492,508],
[528,492,0,511,498,519,497,501,511,525,481],
[527,482,490,0,490,502,502,495,484,503,497],
[507,507,503,511,0,503,512,499,492,504,497],
[513,498,482,499,498,0,512,505,511,502,478],
[500,511,504,499,489,489,0,503,509,500,503],
[536,485,500,506,502,496,498,0,510,496,515],
[511,503,490,517,509,490,492,491,0,469,498],
[511,509,476,498,497,499,501,505,532,0,489],
[535,493,520,504,504,523,498,486,503,512,0]])



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
result = np.append(np.array([11, 1001, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,493,511,502,516,486,488,508,483,503],
[504,0,490,528,507,523,489,486,505,490,501],
[508,511,0,518,501,501,492,497,501,499,527],
[490,473,483,0,504,501,465,476,495,504,497],
[499,494,500,497,0,497,481,488,506,489,501],
[485,478,500,500,504,0,495,489,503,492,512],
[515,512,509,536,520,506,0,515,502,506,500],
[513,515,504,525,513,512,486,0,509,523,516],
[493,496,500,506,495,498,499,492,0,523,518],
[518,511,502,497,512,509,495,478,478,0,502],
[498,500,474,504,500,489,501,485,483,499,0]])



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
result = np.append(np.array([11, 1001, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,491,530,523,503,504,490,511,524,479],
[506,0,482,521,505,503,525,516,496,509,502],
[510,519,0,542,530,515,505,534,532,530,496],
[471,480,459,0,491,483,474,488,482,503,444],
[478,496,471,510,0,507,486,491,487,508,457],
[498,498,486,518,494,0,507,493,522,520,492],
[497,476,496,527,515,494,0,513,491,508,491],
[511,485,467,513,510,508,488,0,499,487,472],
[490,505,469,519,514,479,510,502,0,499,474],
[477,492,471,498,493,481,493,514,502,0,476],
[522,499,505,557,544,509,510,529,527,525,0]])



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
result = np.append(np.array([11, 1001, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,562,501,546,604,499,561,464,556,633,558],
[439,0,435,417,492,508,537,484,501,501,489],
[500,566,0,497,562,584,517,586,606,653,522],
[455,584,504,0,529,570,523,519,564,546,568],
[397,509,439,472,0,501,435,420,461,546,511],
[502,493,417,431,500,0,510,446,532,561,452],
[440,464,484,478,566,491,0,522,523,568,478],
[537,517,415,482,581,555,479,0,522,632,470],
[445,500,395,437,540,469,478,479,0,533,513],
[368,500,348,455,455,440,433,369,468,0,424],
[443,512,479,433,490,549,523,531,488,577,0]])



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
result = np.append(np.array([11, 1001, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,521,483,495,522,571,512,503,469,522],
[486,0,561,499,500,483,561,515,515,501,502],
[480,440,0,445,452,476,496,449,511,473,462],
[518,502,556,0,465,502,487,526,518,489,491],
[506,501,549,536,0,540,542,519,526,484,553],
[479,518,525,499,461,0,516,485,529,435,474],
[430,440,505,514,459,485,0,431,487,465,496],
[489,486,552,475,482,516,570,0,526,464,492],
[498,486,490,483,475,472,514,475,0,461,514],
[532,500,528,512,517,566,536,537,540,0,552],
[479,499,539,510,448,527,505,509,487,449,0]])



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
result = np.append(np.array([11, 1001, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,501,510,498,509,515,517,510,522,489],
[487,0,501,487,505,487,455,505,471,474,456],
[500,500,0,490,475,497,487,489,476,504,492],
[491,514,511,0,499,509,492,522,486,505,486],
[503,496,526,502,0,497,475,487,489,504,493],
[492,514,504,492,504,0,459,485,463,496,506],
[486,546,514,509,526,542,0,506,542,542,543],
[484,496,512,479,514,516,495,0,473,520,478],
[491,530,525,515,512,538,459,528,0,519,507],
[479,527,497,496,497,505,459,481,482,0,477],
[512,545,509,515,508,495,458,523,494,524,0]])



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
result = np.append(np.array([11, 1001, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,484,481,489,489,503,522,466,502,525],
[488,0,471,516,493,528,527,540,499,521,535],
[517,530,0,478,571,523,508,492,494,592,520],
[520,485,523,0,526,533,490,526,500,512,575],
[512,508,430,475,0,464,466,513,487,495,549],
[512,473,478,468,537,0,463,513,449,504,501],
[498,474,493,511,535,538,0,491,509,547,551],
[479,461,509,475,488,488,510,0,465,504,545],
[535,502,507,501,514,552,492,536,0,543,572],
[499,480,409,489,506,497,454,497,458,0,520],
[476,466,481,426,452,500,450,456,429,481,0]])



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
result = np.append(np.array([11, 1001, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,529,526,519,492,524,491,518,535,529],
[471,0,490,490,473,480,508,440,504,477,460],
[472,511,0,490,488,490,534,475,476,492,484],
[475,511,511,0,495,489,513,465,535,483,504],
[482,528,513,506,0,503,531,441,505,497,495],
[509,521,511,512,498,0,511,467,469,491,473],
[477,493,467,488,470,490,0,466,512,479,476],
[510,561,526,536,560,534,535,0,543,518,486],
[483,497,525,466,496,532,489,458,0,484,480],
[466,524,509,518,504,510,522,483,517,0,472],
[472,541,517,497,506,528,525,515,521,529,0]])



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
result = np.append(np.array([11, 1001, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,514,510,501,486,504,501,518,518,490],
[499,0,502,520,515,481,496,488,514,499,511],
[487,499,0,531,503,492,492,510,517,500,510],
[491,481,470,0,501,466,479,473,487,480,490],
[500,486,498,500,0,495,526,501,518,501,523],
[515,520,509,535,506,0,502,493,513,513,498],
[497,505,509,522,475,499,0,516,485,492,483],
[500,513,491,528,500,508,485,0,500,504,522],
[483,487,484,514,483,488,516,501,0,488,502],
[483,502,501,521,500,488,509,497,513,0,489],
[511,490,491,511,478,503,518,479,499,512,0]])



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
result = np.append(np.array([11, 1001, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,494,516,501,501,556,486,493,533,547],
[505,0,507,524,497,505,501,474,515,506,495],
[507,494,0,491,457,493,507,467,484,471,530],
[485,477,510,0,481,505,490,469,471,502,522],
[500,504,544,520,0,525,555,527,490,520,547],
[500,496,508,496,476,0,489,474,452,482,517],
[445,500,494,511,446,512,0,489,455,469,485],
[515,527,534,532,474,527,512,0,494,528,545],
[508,486,517,530,511,549,546,507,0,513,516],
[468,495,530,499,481,519,532,473,488,0,525],
[454,506,471,479,454,484,516,456,485,476,0]])



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
result = np.append(np.array([11, 1001, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,625,513,572,518,607,500,527,466,534],
[475,0,560,572,519,449,586,461,540,497,499],
[376,441,0,448,486,421,512,371,480,393,444],
[488,429,553,0,468,456,554,481,491,429,466],
[429,482,515,533,0,446,512,459,466,439,420],
[483,552,580,545,555,0,599,543,571,452,490],
[394,415,489,447,489,402,0,411,424,436,398],
[501,540,630,520,542,458,590,0,528,555,464],
[474,461,521,510,535,430,577,473,0,482,456],
[535,504,608,572,562,549,565,446,519,0,484],
[467,502,557,535,581,511,603,537,545,517,0]])



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
result = np.append(np.array([11, 1001, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,485,507,515,515,455,500,479,489,506],
[519,0,488,505,521,509,489,492,509,501,507],
[516,513,0,500,532,513,488,482,515,485,496],
[494,496,501,0,517,523,472,497,503,485,512],
[486,480,469,484,0,466,468,479,484,482,473],
[486,492,488,478,535,0,492,512,488,478,502],
[546,512,513,529,533,509,0,497,527,499,514],
[501,509,519,504,522,489,504,0,525,489,490],
[522,492,486,498,517,513,474,476,0,486,491],
[512,500,516,516,519,523,502,512,515,0,516],
[495,494,505,489,528,499,487,511,510,485,0]])



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
result = np.append(np.array([11, 1001, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,499,516,478,494,495,504,489,497,466],
[532,0,478,517,502,497,482,481,486,487,475],
[502,523,0,521,466,506,479,494,486,527,490],
[485,484,480,0,464,490,495,499,496,502,488],
[523,499,535,537,0,546,527,508,528,517,522],
[507,504,495,511,455,0,495,503,495,502,484],
[506,519,522,506,474,506,0,521,511,501,504],
[497,520,507,502,493,498,480,0,498,509,502],
[512,515,515,505,473,506,490,503,0,508,474],
[504,514,474,499,484,499,500,492,493,0,489],
[535,526,511,513,479,517,497,499,527,512,0]])



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
result = np.append(np.array([11, 1001, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,500,462,466,470,494,471,519,486,497],
[508,0,478,508,486,491,516,452,517,484,509],
[501,523,0,506,499,488,505,483,522,488,510],
[539,493,495,0,492,514,537,499,556,492,514],
[535,515,502,509,0,479,523,504,542,489,521],
[531,510,513,487,522,0,517,503,541,500,516],
[507,485,496,464,478,484,0,476,539,475,512],
[530,549,518,502,497,498,525,0,529,532,524],
[482,484,479,445,459,460,462,472,0,471,494],
[515,517,513,509,512,501,526,469,530,0,511],
[504,492,491,487,480,485,489,477,507,490,0]])



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
result = np.append(np.array([11, 1001, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,496,528,511,533,499,503,528,518,508],
[483,0,486,474,483,478,466,454,471,463,519],
[505,515,0,537,508,532,496,485,493,518,538],
[473,527,464,0,508,493,490,465,482,509,527],
[490,518,493,493,0,519,505,513,514,521,535],
[468,523,469,508,482,0,471,473,494,512,503],
[502,535,505,511,496,530,0,489,512,504,532],
[498,547,516,536,488,528,512,0,520,503,535],
[473,530,508,519,487,507,489,481,0,498,517],
[483,538,483,492,480,489,497,498,503,0,519],
[493,482,463,474,466,498,469,466,484,482,0]])



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
result = np.append(np.array([11, 1001, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,494,475,515,486,487,497,504,504,503],
[514,0,492,478,527,492,520,494,513,513,493],
[507,509,0,477,515,483,506,491,507,505,492],
[526,523,524,0,523,496,506,533,533,515,508],
[486,474,486,478,0,495,475,476,490,487,476],
[515,509,518,505,506,0,502,502,517,506,484],
[514,481,495,495,526,499,0,513,517,508,520],
[504,507,510,468,525,499,488,0,515,492,491],
[497,488,494,468,511,484,484,486,0,498,479],
[497,488,496,486,514,495,493,509,503,0,489],
[498,508,509,493,525,517,481,510,522,512,0]])



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
result = np.append(np.array([11, 1001, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,470,554,522,538,431,501,485,521,484],
[525,0,500,496,526,540,517,540,471,522,470],
[531,501,0,557,479,485,452,512,519,537,480],
[447,505,444,0,461,412,454,460,471,485,419],
[479,475,522,540,0,554,439,483,510,512,443],
[463,461,516,589,447,0,496,529,497,530,467],
[570,484,549,547,562,505,0,516,476,519,508],
[500,461,489,541,518,472,485,0,501,465,500],
[516,530,482,530,491,504,525,500,0,521,428],
[480,479,464,516,489,471,482,536,480,0,443],
[517,531,521,582,558,534,493,501,573,558,0]])



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
result = np.append(np.array([11, 1001, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,510,509,502,440,460,418,533,497,487],
[536,0,577,515,455,517,511,449,485,504,579],
[491,424,0,496,454,440,458,458,500,516,473],
[492,486,505,0,441,439,513,462,530,536,511],
[499,546,547,560,0,456,513,489,527,547,513],
[561,484,561,562,545,0,516,514,546,584,563],
[541,490,543,488,488,485,0,531,534,542,533],
[583,552,543,539,512,487,470,0,546,533,548],
[468,516,501,471,474,455,467,455,0,499,493],
[504,497,485,465,454,417,459,468,502,0,481],
[514,422,528,490,488,438,468,453,508,520,0]])



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
result = np.append(np.array([11, 1001, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,359,748,359,498,298,716,359,537,463],
[496,0,166,521,421,483,553,661,379,414,483],
[642,835,0,699,699,553,699,939,525,553,421],
[253,480,302,0,418,480,240,584,302,405,405],
[642,580,302,583,0,648,615,1001,302,641,648],
[503,518,448,521,353,0,382,800,386,456,428],
[703,448,302,761,386,619,0,869,302,537,480],
[285,340,62,417,0,201,132,0,0,132,62],
[642,622,476,699,699,615,699,1001,0,414,615],
[464,587,448,596,360,545,464,869,587,0,380],
[538,518,580,596,353,573,521,939,386,621,0]])



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
result = np.append(np.array([11, 1001, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,531,507,512,509,518,524,467,521,504],
[513,0,526,513,505,537,521,531,503,484,501],
[470,475,0,495,475,500,495,509,461,477,490],
[494,488,506,0,500,508,494,519,479,477,511],
[489,496,526,501,0,526,514,527,487,502,520],
[492,464,501,493,475,0,495,505,478,469,510],
[483,480,506,507,487,506,0,523,487,489,500],
[477,470,492,482,474,496,478,0,476,490,503],
[534,498,540,522,514,523,514,525,0,510,519],
[480,517,524,524,499,532,512,511,491,0,514],
[497,500,511,490,481,491,501,498,482,487,0]])



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
result = np.append(np.array([11, 1001, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,501,541,498,535,531,554,546,492,506],
[489,0,498,542,497,541,520,566,564,484,518],
[500,503,0,549,512,507,534,545,522,501,527],
[460,459,452,0,487,505,471,525,505,464,461],
[503,504,489,514,0,486,485,547,520,484,482],
[466,460,494,496,515,0,482,539,523,459,500],
[470,481,467,530,516,519,0,569,524,486,505],
[447,435,456,476,454,462,432,0,486,449,455],
[455,437,479,496,481,478,477,515,0,444,469],
[509,517,500,537,517,542,515,552,557,0,496],
[495,483,474,540,519,501,496,546,532,505,0]])



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
result = np.append(np.array([11, 1001, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,548,502,485,489,565,523,487,481,466,495],
[453,0,375,449,487,483,481,387,494,413,459],
[499,626,0,518,591,536,545,517,500,419,516],
[516,552,483,0,537,541,566,400,485,400,409],
[512,514,410,464,0,527,515,473,528,479,470],
[436,518,465,460,474,0,439,474,395,433,428],
[478,520,456,435,486,562,0,515,421,403,448],
[514,614,484,601,528,527,486,0,444,424,551],
[520,507,501,516,473,606,580,557,0,512,523],
[535,588,582,601,522,568,598,577,489,0,571],
[506,542,485,592,531,573,553,450,478,430,0]])



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
result = np.append(np.array([11, 1001, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,520,462,568,502,540,588,472,569,545],
[505,0,541,519,540,499,587,531,486,563,573],
[481,460,0,467,511,493,586,521,442,615,532],
[539,482,534,0,571,540,601,543,528,573,557],
[433,461,490,430,0,424,546,482,487,505,505],
[499,502,508,461,577,0,573,555,542,542,540],
[461,414,415,400,455,428,0,495,445,492,492],
[413,470,480,458,519,446,506,0,467,517,506],
[529,515,559,473,514,459,556,534,0,525,544],
[432,438,386,428,496,459,509,484,476,0,486],
[456,428,469,444,496,461,509,495,457,515,0]])



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
result = np.append(np.array([11, 1001, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,491,501,504,488,491,515,508,491,484],
[490,0,494,494,492,481,484,497,507,462,487],
[510,507,0,512,510,497,495,514,535,476,468],
[500,507,489,0,511,476,507,524,515,496,491],
[497,509,491,490,0,471,495,519,521,488,490],
[513,520,504,525,530,0,515,546,544,518,485],
[510,517,506,494,506,486,0,533,517,495,499],
[486,504,487,477,482,455,468,0,503,450,480],
[493,494,466,486,480,457,484,498,0,480,463],
[510,539,525,505,513,483,506,551,521,0,501],
[517,514,533,510,511,516,502,521,538,500,0]])



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
result = np.append(np.array([11, 1001, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,506,510,519,463,496,491,495,508,521],
[495,0,497,492,489,476,490,486,491,467,510],
[495,504,0,508,485,465,486,489,496,475,512],
[491,509,493,0,505,478,492,484,487,504,503],
[482,512,516,496,0,506,481,498,497,464,492],
[538,525,536,523,495,0,491,495,524,486,518],
[505,511,515,509,520,510,0,489,507,481,512],
[510,515,512,517,503,506,512,0,512,498,548],
[506,510,505,514,504,477,494,489,0,478,528],
[493,534,526,497,537,515,520,503,523,0,526],
[480,491,489,498,509,483,489,453,473,475,0]])



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
result = np.append(np.array([11, 1001, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,506,533,491,497,520,486,486,464,490],
[528,0,541,523,528,531,527,543,540,499,535],
[495,460,0,485,491,493,496,462,480,460,475],
[468,478,516,0,514,483,481,510,486,460,490],
[510,473,510,487,0,495,490,500,509,484,474],
[504,470,508,518,506,0,500,508,506,499,521],
[481,474,505,520,511,501,0,497,484,501,495],
[515,458,539,491,501,493,504,0,497,486,490],
[515,461,521,515,492,495,517,504,0,484,499],
[537,502,541,541,517,502,500,515,517,0,522],
[511,466,526,511,527,480,506,511,502,479,0]])



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
result = np.append(np.array([11, 1001, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,515,491,506,495,480,493,497,486,490],
[486,0,496,498,484,498,495,495,494,492,496],
[486,505,0,476,468,476,473,485,480,473,484],
[510,503,525,0,512,489,483,506,512,495,503],
[495,517,533,489,0,505,483,500,519,480,503],
[506,503,525,512,496,0,495,516,504,514,499],
[521,506,528,518,518,506,0,508,528,504,495],
[508,506,516,495,501,485,493,0,515,507,510],
[504,507,521,489,482,497,473,486,0,484,492],
[515,509,528,506,521,487,497,494,517,0,516],
[511,505,517,498,498,502,506,491,509,485,0]])



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
result = np.append(np.array([11, 1001, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,466,492,505,497,486,464,432,516,479],
[508,0,474,467,494,466,495,489,462,476,473],
[535,527,0,461,518,445,534,485,433,488,479],
[509,534,540,0,533,525,566,483,477,546,517],
[496,507,483,468,0,439,479,455,476,517,462],
[504,535,556,476,562,0,512,489,515,511,529],
[515,506,467,435,522,489,0,443,437,511,483],
[537,512,516,518,546,512,558,0,486,544,506],
[569,539,568,524,525,486,564,515,0,512,534],
[485,525,513,455,484,490,490,457,489,0,463],
[522,528,522,484,539,472,518,495,467,538,0]])



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
result = np.append(np.array([11, 1001, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,538,518,519,502,476,507,555,478,535],
[512,0,605,549,485,504,478,480,535,443,527],
[463,396,0,515,446,440,410,415,481,416,497],
[483,452,486,0,479,483,467,475,497,449,483],
[482,516,555,522,0,497,462,453,509,418,493],
[499,497,561,518,504,0,457,494,543,440,521],
[525,523,591,534,539,544,0,483,545,508,568],
[494,521,586,526,548,507,518,0,527,466,551],
[446,466,520,504,492,458,456,474,0,435,522],
[523,558,585,552,583,561,493,535,566,0,545],
[466,474,504,518,508,480,433,450,479,456,0]])



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
result = np.append(np.array([11, 1001, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,624,559,490,587,578,539,543,644,772,557],
[377,0,416,641,602,522,545,574,567,680,405],
[442,585,0,527,551,558,489,470,513,588,431],
[511,360,474,0,502,596,504,458,541,667,473],
[414,399,450,499,0,558,510,392,569,548,441],
[423,479,443,405,443,0,623,425,475,729,452],
[462,456,512,497,491,378,0,451,392,609,420],
[458,427,531,543,609,576,550,0,548,628,495],
[357,434,488,460,432,526,609,453,0,695,504],
[229,321,413,334,453,272,392,373,306,0,370],
[444,596,570,528,560,549,581,506,497,631,0]])



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
result = np.append(np.array([11, 1001, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,428,462,453,483,457,483,415,490,437,393],
[573,0,526,535,521,480,542,496,538,496,501],
[539,475,0,556,528,479,527,505,568,546,506],
[548,466,445,0,505,452,502,441,526,462,444],
[518,480,473,496,0,433,534,452,510,498,500],
[544,521,522,549,568,0,506,460,593,514,459],
[518,459,474,499,467,495,0,450,516,472,449],
[586,505,496,560,549,541,551,0,537,514,508],
[511,463,433,475,491,408,485,464,0,460,431],
[564,505,455,539,503,487,529,487,541,0,455],
[608,500,495,557,501,542,552,493,570,546,0]])



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
result = np.append(np.array([11, 1001, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,464,580,468,488,477,585,508,583,505],
[483,0,497,442,467,441,476,547,436,560,524],
[537,504,0,501,522,508,529,515,541,479,495],
[421,559,500,0,496,383,504,559,460,513,497],
[533,534,479,505,0,543,482,524,503,614,476],
[513,560,493,618,458,0,542,595,581,573,574],
[524,525,472,497,519,459,0,576,529,590,506],
[416,454,486,442,477,406,425,0,492,501,433],
[493,565,460,541,498,420,472,509,0,517,500],
[418,441,522,488,387,428,411,500,484,0,460],
[496,477,506,504,525,427,495,568,501,541,0]])



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
result = np.append(np.array([11, 1001, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,487,466,497,504,506,470,480,495,486],
[539,0,498,508,513,517,520,508,500,536,512],
[514,503,0,479,520,519,507,509,504,524,500],
[535,493,522,0,510,530,531,512,509,505,507],
[504,488,481,491,0,533,516,497,494,500,502],
[497,484,482,471,468,0,468,474,469,486,497],
[495,481,494,470,485,533,0,475,499,508,511],
[531,493,492,489,504,527,526,0,486,511,499],
[521,501,497,492,507,532,502,515,0,509,513],
[506,465,477,496,501,515,493,490,492,0,497],
[515,489,501,494,499,504,490,502,488,504,0]])



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
result = np.append(np.array([11, 1001, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,471,459,484,488,501,468,462,477,556],
[538,0,505,522,466,529,507,503,497,510,518],
[530,496,0,501,491,549,539,449,511,497,539],
[542,479,500,0,512,573,539,492,537,552,564],
[517,535,510,489,0,524,528,464,501,489,575],
[513,472,452,428,477,0,471,459,478,488,511],
[500,494,462,462,473,530,0,479,507,493,543],
[533,498,552,509,537,542,522,0,548,533,581],
[539,504,490,464,500,523,494,453,0,505,555],
[524,491,504,449,512,513,508,468,496,0,575],
[445,483,462,437,426,490,458,420,446,426,0]])



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
result = np.append(np.array([11, 1001, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,498,497,495,477,506,487,480,503,492],
[519,0,457,498,477,481,490,474,496,534,510],
[503,544,0,512,500,512,499,492,482,515,496],
[504,503,489,0,507,496,535,496,491,506,510],
[506,524,501,494,0,511,505,513,490,521,497],
[524,520,489,505,490,0,500,488,482,545,494],
[495,511,502,466,496,501,0,503,494,530,511],
[514,527,509,505,488,513,498,0,487,546,512],
[521,505,519,510,511,519,507,514,0,526,498],
[498,467,486,495,480,456,471,455,475,0,489],
[509,491,505,491,504,507,490,489,503,512,0]])



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
result = np.append(np.array([11, 1001, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,491,507,481,498,514,494,494,518,530],
[521,0,483,509,493,513,515,518,499,495,527],
[510,518,0,515,497,512,502,514,535,481,528],
[494,492,486,0,492,492,493,498,502,513,526],
[520,508,504,509,0,478,535,505,502,509,528],
[503,488,489,509,523,0,513,506,524,491,514],
[487,486,499,508,466,488,0,507,489,495,513],
[507,483,487,503,496,495,494,0,513,491,520],
[507,502,466,499,499,477,512,488,0,491,519],
[483,506,520,488,492,510,506,510,510,0,504],
[471,474,473,475,473,487,488,481,482,497,0]])



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
result = np.append(np.array([11, 1001, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,481,502,486,515,496,487,502,477,513],
[500,0,488,521,481,500,518,476,499,498,539],
[520,513,0,525,496,531,512,510,518,506,507],
[499,480,476,0,478,495,499,490,489,472,520],
[515,520,505,523,0,512,503,502,519,492,520],
[486,501,470,506,489,0,503,490,516,467,502],
[505,483,489,502,498,498,0,506,516,482,494],
[514,525,491,511,499,511,495,0,503,483,515],
[499,502,483,512,482,485,485,498,0,467,496],
[524,503,495,529,509,534,519,518,534,0,500],
[488,462,494,481,481,499,507,486,505,501,0]])



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
result = np.append(np.array([11, 1001, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,540,508,517,520,535,516,520,487,520],
[485,0,509,517,497,494,478,503,515,501,488],
[461,492,0,500,474,515,496,464,505,470,478],
[493,484,501,0,508,503,471,490,507,480,495],
[484,504,527,493,0,482,483,472,526,484,484],
[481,507,486,498,519,0,516,503,520,498,505],
[466,523,505,530,518,485,0,503,510,485,479],
[485,498,537,511,529,498,498,0,514,468,504],
[481,486,496,494,475,481,491,487,0,453,493],
[514,500,531,521,517,503,516,533,548,0,502],
[481,513,523,506,517,496,522,497,508,499,0]])



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
result = np.append(np.array([11, 1001, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,428,513,464,460,492,398,368,556,484,421],
[573,0,626,529,580,546,499,495,582,535,597],
[488,375,0,419,417,389,322,401,376,384,342],
[537,472,582,0,486,549,503,459,471,523,400],
[541,421,584,515,0,563,471,484,568,475,456],
[509,455,612,452,438,0,401,539,474,521,378],
[603,502,679,498,530,600,0,561,621,558,567],
[633,506,600,542,517,462,440,0,517,597,503],
[445,419,625,530,433,527,380,484,0,469,460],
[517,466,617,478,526,480,443,404,532,0,482],
[580,404,659,601,545,623,434,498,541,519,0]])



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
result = np.append(np.array([11, 1001, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,493,496,484,488,512,482,489,492,491],
[500,0,495,476,497,496,505,493,499,481,498],
[508,506,0,488,481,502,487,516,476,511,499],
[505,525,513,0,493,499,505,514,486,510,518],
[517,504,520,508,0,494,529,509,505,508,504],
[513,505,499,502,507,0,508,497,496,508,513],
[489,496,514,496,472,493,0,493,482,508,492],
[519,508,485,487,492,504,508,0,487,512,497],
[512,502,525,515,496,505,519,514,0,515,494],
[509,520,490,491,493,493,493,489,486,0,515],
[510,503,502,483,497,488,509,504,507,486,0]])



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
result = np.append(np.array([11, 1001, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,553,522,564,525,546,511,482,546,489,531],
[448,0,464,480,449,472,421,455,452,444,467],
[479,537,0,522,453,486,470,455,493,494,512],
[437,521,479,0,524,444,474,504,499,491,505],
[476,552,548,477,0,522,492,567,524,511,523],
[455,529,515,557,479,0,479,524,529,502,553],
[490,580,531,527,509,522,0,583,542,498,524],
[519,546,546,497,434,477,418,0,490,520,463],
[455,549,508,502,477,472,459,511,0,460,485],
[512,557,507,510,490,499,503,481,541,0,472],
[470,534,489,496,478,448,477,538,516,529,0]])



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
result = np.append(np.array([11, 1001, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,565,518,588,595,684,542,614,472,586,494],
[436,0,445,493,530,596,564,642,424,530,430],
[483,556,0,601,665,570,508,537,535,573,329],
[413,508,400,0,500,664,582,455,420,582,510],
[406,471,336,501,0,613,396,574,386,502,414],
[317,405,431,337,388,0,371,450,312,437,338],
[459,437,493,419,605,630,0,544,539,479,378],
[387,359,464,546,427,551,457,0,444,429,338],
[529,577,466,581,615,689,462,557,0,518,460],
[415,471,428,419,499,564,522,572,483,0,363],
[507,571,672,491,587,663,623,663,541,638,0]])



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
result = np.append(np.array([11, 1001, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,502,486,515,514,525,482,515,494,531],
[497,0,493,502,506,501,516,495,508,491,508],
[499,508,0,485,510,478,518,488,512,498,518],
[515,499,516,0,488,500,494,491,493,478,481],
[486,495,491,513,0,497,516,494,509,491,507],
[487,500,523,501,504,0,522,501,512,486,509],
[476,485,483,507,485,479,0,481,500,467,485],
[519,506,513,510,507,500,520,0,504,505,485],
[486,493,489,508,492,489,501,497,0,472,510],
[507,510,503,523,510,515,534,496,529,0,497],
[470,493,483,520,494,492,516,516,491,504,0]])



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
result = np.append(np.array([11, 1001, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,548,467,531,494,488,435,468,449,464],
[543,0,526,479,585,537,516,501,483,484,538],
[453,475,0,410,461,463,409,426,403,526,404],
[534,522,591,0,464,554,533,476,536,540,528],
[470,416,540,537,0,454,514,496,477,502,527],
[507,464,538,447,547,0,481,559,482,526,535],
[513,485,592,468,487,520,0,484,465,541,475],
[566,500,575,525,505,442,517,0,540,515,535],
[533,518,598,465,524,519,536,461,0,547,540],
[552,517,475,461,499,475,460,486,454,0,502],
[537,463,597,473,474,466,526,466,461,499,0]])



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
result = np.append(np.array([11, 1001, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,587,497,443,440,492,456,451,536,479,561],
[414,0,482,390,351,396,449,454,449,395,483],
[504,519,0,413,417,463,543,492,477,455,518],
[558,611,588,0,522,481,544,539,578,542,586],
[561,650,584,479,0,507,586,549,638,504,517],
[509,605,538,520,494,0,550,535,538,492,569],
[545,552,458,457,415,451,0,440,619,428,488],
[550,547,509,462,452,466,561,0,465,425,510],
[465,552,524,423,363,463,382,536,0,451,516],
[522,606,546,459,497,509,573,576,550,0,466],
[440,518,483,415,484,432,513,491,485,535,0]])



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
result = np.append(np.array([11, 1001, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,664,286,628,328,829,824,447,530,368,545],
[337,0,328,628,130,498,507,0,295,170,429],
[715,673,0,707,377,789,845,508,414,377,554],
[373,373,294,0,82,583,708,201,496,212,122],
[673,871,624,919,0,871,1001,494,742,836,706],
[172,503,212,418,130,0,384,201,295,212,212],
[177,494,156,293,0,617,0,378,281,198,299],
[554,1001,493,800,507,800,623,0,623,705,766],
[471,706,587,505,259,706,720,378,0,415,299],
[633,831,624,789,165,789,803,296,586,0,471],
[456,572,447,879,295,789,702,235,702,530,0]])



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
result = np.append(np.array([11, 1001, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,485,535,489,476,483,514,487,511,494],
[516,0,507,537,531,508,480,528,495,565,509],
[516,494,0,513,489,488,526,494,499,523,514],
[466,464,488,0,465,453,478,503,471,513,482],
[512,470,512,536,0,487,483,490,483,509,493],
[525,493,513,548,514,0,506,497,495,531,487],
[518,521,475,523,518,495,0,530,505,534,514],
[487,473,507,498,511,504,471,0,480,506,492],
[514,506,502,530,518,506,496,521,0,511,501],
[490,436,478,488,492,470,467,495,490,0,470],
[507,492,487,519,508,514,487,509,500,531,0]])



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
result = np.append(np.array([11, 1001, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,503,499,535,498,547,544,495,505,480],
[476,0,473,472,470,468,482,465,468,450,477],
[498,528,0,511,523,511,559,497,502,500,544],
[502,529,490,0,525,494,517,522,523,544,524],
[466,531,478,476,0,490,480,500,482,481,511],
[503,533,490,507,511,0,532,496,481,507,503],
[454,519,442,484,521,469,0,491,477,475,502],
[457,536,504,479,501,505,510,0,489,496,502],
[506,533,499,478,519,520,524,512,0,502,491],
[496,551,501,457,520,494,526,505,499,0,498],
[521,524,457,477,490,498,499,499,510,503,0]])



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
result = np.append(np.array([11, 1001, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,533,466,491,506,523,473,495,461,520],
[544,0,503,506,477,490,519,505,513,456,498],
[468,498,0,476,454,491,501,489,484,450,505],
[535,495,525,0,501,570,512,530,505,523,537],
[510,524,547,500,0,502,500,540,471,469,514],
[495,511,510,431,499,0,524,488,462,439,522],
[478,482,500,489,501,477,0,439,450,443,487],
[528,496,512,471,461,513,562,0,499,475,507],
[506,488,517,496,530,539,551,502,0,482,503],
[540,545,551,478,532,562,558,526,519,0,570],
[481,503,496,464,487,479,514,494,498,431,0]])



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
result = np.append(np.array([11, 1001, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,435,543,501,490,492,513,468,511,442,511],
[566,0,647,548,580,621,502,584,497,534,543],
[458,354,0,469,454,542,463,463,427,375,429],
[500,453,532,0,518,552,461,447,476,487,467],
[511,421,547,483,0,533,450,492,474,491,396],
[509,380,459,449,468,0,400,455,422,460,474],
[488,499,538,540,551,601,0,478,483,546,497],
[533,417,538,554,509,546,523,0,438,484,407],
[490,504,574,525,527,579,518,563,0,539,525],
[559,467,626,514,510,541,455,517,462,0,521],
[490,458,572,534,605,527,504,594,476,480,0]])



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
result = np.append(np.array([11, 1001, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,516,517,517,467,510,507,503,488,505],
[492,0,531,553,526,525,522,518,530,511,516],
[485,470,0,494,491,507,501,475,515,491,477],
[484,448,507,0,485,458,500,492,476,518,491],
[484,475,510,516,0,488,530,502,500,515,516],
[534,476,494,543,513,0,509,505,533,511,499],
[491,479,500,501,471,492,0,505,483,483,486],
[494,483,526,509,499,496,496,0,525,504,464],
[498,471,486,525,501,468,518,476,0,500,497],
[513,490,510,483,486,490,518,497,501,0,510],
[496,485,524,510,485,502,515,537,504,491,0]])



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
result = np.append(np.array([11, 1001, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,497,490,498,503,497,487,502,509,483],
[519,0,526,499,499,528,515,515,532,537,503],
[504,475,0,521,510,506,503,501,523,522,520],
[511,502,480,0,508,515,522,502,527,528,497],
[503,502,491,493,0,499,478,490,512,521,494],
[498,473,495,486,502,0,507,479,512,504,504],
[504,486,498,479,523,494,0,493,511,521,496],
[514,486,500,499,511,522,508,0,537,534,498],
[499,469,478,474,489,489,490,464,0,510,497],
[492,464,479,473,480,497,480,467,491,0,476],
[518,498,481,504,507,497,505,503,504,525,0]])



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
result = np.append(np.array([11, 1001, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,500,501,508,509,507,549,514,503,506],
[503,0,509,503,501,493,521,537,519,499,507],
[501,492,0,510,481,482,513,529,493,514,499],
[500,498,491,0,495,495,506,533,515,504,518],
[493,500,520,506,0,521,532,525,532,538,517],
[492,508,519,506,480,0,522,503,500,493,539],
[494,480,488,495,469,479,0,505,484,472,507],
[452,464,472,468,476,498,496,0,485,475,485],
[487,482,508,486,469,501,517,516,0,486,519],
[498,502,487,497,463,508,529,526,515,0,524],
[495,494,502,483,484,462,494,516,482,477,0]])



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
result = np.append(np.array([11, 1001, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,451,481,467,408,416,415,539,391,445],
[468,0,477,498,417,511,497,517,526,496,507],
[550,524,0,486,513,492,504,477,500,548,484],
[520,503,515,0,545,496,526,488,477,481,471],
[534,584,488,456,0,515,501,558,490,480,441],
[593,490,509,505,486,0,493,498,485,510,498],
[585,504,497,475,500,508,0,513,580,509,461],
[586,484,524,513,443,503,488,0,508,518,521],
[462,475,501,524,511,516,421,493,0,505,477],
[610,505,453,520,521,491,492,483,496,0,479],
[556,494,517,530,560,503,540,480,524,522,0]])



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
result = np.append(np.array([11, 1001, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,471,479,480,484,452,452,489,463,474],
[508,0,485,476,486,467,448,501,498,467,479],
[530,516,0,481,500,493,454,515,492,479,517],
[522,525,520,0,520,482,502,473,498,463,499],
[521,515,501,481,0,494,481,518,528,492,495],
[517,534,508,519,507,0,498,502,516,503,505],
[549,553,547,499,520,503,0,543,545,525,549],
[549,500,486,528,483,499,458,0,489,506,518],
[512,503,509,503,473,485,456,512,0,499,501],
[538,534,522,538,509,498,476,495,502,0,528],
[527,522,484,502,506,496,452,483,500,473,0]])



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
result = np.append(np.array([11, 1001, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,470,502,511,525,467,489,510,515,504],
[483,0,469,477,480,516,489,502,490,481,494],
[531,532,0,513,531,550,489,537,517,534,540],
[499,524,488,0,510,537,491,532,534,516,555],
[490,521,470,491,0,517,485,512,498,488,516],
[476,485,451,464,484,0,467,500,496,486,480],
[534,512,512,510,516,534,0,515,497,502,518],
[512,499,464,469,489,501,486,0,483,496,515],
[491,511,484,467,503,505,504,518,0,508,533],
[486,520,467,485,513,515,499,505,493,0,516],
[497,507,461,446,485,521,483,486,468,485,0]])



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
result = np.append(np.array([11, 1001, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,498,496,512,507,497,476,483,496,503],
[502,0,495,454,513,469,502,469,485,522,482],
[503,506,0,480,482,524,519,482,494,502,498],
[505,547,521,0,511,513,497,527,513,513,483],
[489,488,519,490,0,486,518,472,504,487,501],
[494,532,477,488,515,0,511,507,506,492,488],
[504,499,482,504,483,490,0,474,501,470,489],
[525,532,519,474,529,494,527,0,511,494,528],
[518,516,507,488,497,495,500,490,0,495,518],
[505,479,499,488,514,509,531,507,506,0,500],
[498,519,503,518,500,513,512,473,483,501,0]])



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
result = np.append(np.array([11, 1001, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,531,521,516,540,511,516,511,528,515],
[507,0,488,509,513,483,497,476,491,494,491],
[470,513,0,519,486,523,528,503,513,504,498],
[480,492,482,0,480,494,483,481,488,483,478],
[485,488,515,521,0,491,495,496,511,506,507],
[461,518,478,507,510,0,516,503,525,516,508],
[490,504,473,518,506,485,0,503,517,513,511],
[485,525,498,520,505,498,498,0,522,516,506],
[490,510,488,513,490,476,484,479,0,501,505],
[473,507,497,518,495,485,488,485,500,0,473],
[486,510,503,523,494,493,490,495,496,528,0]])



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
result = np.append(np.array([11, 1001, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,474,494,495,506,501,510,454,495,473],
[500,0,508,506,511,509,513,502,469,503,517],
[527,493,0,499,520,510,519,504,503,512,507],
[507,495,502,0,481,495,499,508,464,510,488],
[506,490,481,520,0,488,489,505,475,495,478],
[495,492,491,506,513,0,537,490,486,499,502],
[500,488,482,502,512,464,0,487,478,479,493],
[491,499,497,493,496,511,514,0,444,498,486],
[547,532,498,537,526,515,523,557,0,522,519],
[506,498,489,491,506,502,522,503,479,0,480],
[528,484,494,513,523,499,508,515,482,521,0]])



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
result = np.append(np.array([11, 1001, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,522,504,510,514,505,504,520,531,515],
[508,0,511,503,521,510,499,496,497,534,510],
[479,490,0,491,517,488,481,491,509,503,502],
[497,498,510,0,479,508,487,497,513,516,522],
[491,480,484,522,0,510,492,489,512,503,501],
[487,491,513,493,491,0,506,497,494,517,498],
[496,502,520,514,509,495,0,503,511,530,512],
[497,505,510,504,512,504,498,0,508,520,536],
[481,504,492,488,489,507,490,493,0,519,509],
[470,467,498,485,498,484,471,481,482,0,500],
[486,491,499,479,500,503,489,465,492,501,0]])



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
result = np.append(np.array([11, 1001, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,504,509,506,487,496,515,482,480,494],
[492,0,510,490,503,499,503,498,498,501,511],
[497,491,0,518,499,503,472,516,484,485,492],
[492,511,483,0,508,508,477,534,497,507,502],
[495,498,502,493,0,492,491,506,483,494,494],
[514,502,498,493,509,0,472,525,510,486,526],
[505,498,529,524,510,529,0,509,502,511,501],
[486,503,485,467,495,476,492,0,485,479,490],
[519,503,517,504,518,491,499,516,0,493,488],
[521,500,516,494,507,515,490,522,508,0,491],
[507,490,509,499,507,475,500,511,513,510,0]])



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
result = np.append(np.array([11, 1001, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,499,512,503,548,554,525,550,486,519],
[489,0,522,481,504,511,515,479,494,501,519],
[502,479,0,485,472,533,520,511,520,505,501],
[489,520,516,0,496,526,497,512,550,482,533],
[498,497,529,505,0,543,544,507,524,523,533],
[453,490,468,475,458,0,495,489,494,487,505],
[447,486,481,504,457,506,0,454,487,516,506],
[476,522,490,489,494,512,547,0,513,509,515],
[451,507,481,451,477,507,514,488,0,504,502],
[515,500,496,519,478,514,485,492,497,0,501],
[482,482,500,468,468,496,495,486,499,500,0]])



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
result = np.append(np.array([11, 1001, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,538,537,477,511,503,476,506,489,503,504],
[463,0,488,453,495,479,481,482,462,457,479],
[464,513,0,483,507,503,472,515,460,462,474],
[524,548,518,0,525,531,497,515,507,515,496],
[490,506,494,476,0,509,465,501,478,493,484],
[498,522,498,470,492,0,453,457,478,465,473],
[525,520,529,504,536,548,0,524,500,508,495],
[495,519,486,486,500,544,477,0,462,505,494],
[512,539,541,494,523,523,501,539,0,525,524],
[498,544,539,486,508,536,493,496,476,0,508],
[497,522,527,505,517,528,506,507,477,493,0]])



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
result = np.append(np.array([11, 1001, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,499,488,508,489,484,485,521,494,482],
[514,0,494,490,512,509,482,496,541,506,502],
[502,507,0,491,526,498,494,492,511,520,495],
[513,511,510,0,512,519,502,493,519,494,506],
[493,489,475,489,0,475,467,463,500,491,491],
[512,492,503,482,526,0,485,485,509,502,505],
[517,519,507,499,534,516,0,504,531,509,524],
[516,505,509,508,538,516,497,0,523,507,506],
[480,460,490,482,501,492,470,478,0,503,489],
[507,495,481,507,510,499,492,494,498,0,493],
[519,499,506,495,510,496,477,495,512,508,0]])



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
result = np.append(np.array([11, 1001, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,511,509,506,509,515,525,500,530,531],
[491,0,496,498,490,495,496,499,487,512,504],
[490,505,0,517,505,489,500,505,507,528,514],
[492,503,484,0,494,491,509,507,496,519,511],
[495,511,496,507,0,508,506,522,505,518,520],
[492,506,512,510,493,0,527,527,498,511,509],
[486,505,501,492,495,474,0,510,488,516,519],
[476,502,496,494,479,474,491,0,494,501,514],
[501,514,494,505,496,503,513,507,0,522,520],
[471,489,473,482,483,490,485,500,479,0,483],
[470,497,487,490,481,492,482,487,481,518,0]])



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
result = np.append(np.array([11, 1001, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,503,521,524,536,507,483,506,505,540],
[469,0,499,504,508,531,493,527,451,491,512],
[498,502,0,487,513,499,485,491,503,489,493],
[480,497,514,0,474,495,523,509,507,482,485],
[477,493,488,527,0,495,463,483,502,499,546],
[465,470,502,506,506,0,480,519,474,500,511],
[494,508,516,478,538,521,0,511,494,508,517],
[518,474,510,492,518,482,490,0,457,466,530],
[495,550,498,494,499,527,507,544,0,485,527],
[496,510,512,519,502,501,493,535,516,0,531],
[461,489,508,516,455,490,484,471,474,470,0]])



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
result = np.append(np.array([11, 1001, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,497,473,491,545,502,490,460,470,481],
[504,0,513,511,482,534,532,476,510,456,428],
[504,488,0,504,520,487,534,490,477,459,457],
[528,490,497,0,500,510,509,453,528,455,469],
[510,519,481,501,0,502,520,484,472,460,442],
[456,467,514,491,499,0,510,451,472,475,478],
[499,469,467,492,481,491,0,453,470,422,449],
[511,525,511,548,517,550,548,0,512,449,503],
[541,491,524,473,529,529,531,489,0,467,485],
[531,545,542,546,541,526,579,552,534,0,496],
[520,573,544,532,559,523,552,498,516,505,0]])



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
result = np.append(np.array([11, 1001, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,493,523,528,479,510,510,495,490,484],
[468,0,480,500,517,513,488,492,478,493,480],
[508,521,0,489,529,512,515,490,500,487,482],
[478,501,512,0,532,507,481,462,498,489,507],
[473,484,472,469,0,471,488,481,482,540,457],
[522,488,489,494,530,0,520,501,486,506,507],
[491,513,486,520,513,481,0,508,521,500,482],
[491,509,511,539,520,500,493,0,489,505,517],
[506,523,501,503,519,515,480,512,0,499,482],
[511,508,514,512,461,495,501,496,502,0,471],
[517,521,519,494,544,494,519,484,519,530,0]])



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
result = np.append(np.array([11, 1001, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,491,476,489,433,504,524,563,511,493],
[487,0,497,487,493,483,495,520,528,475,511],
[510,504,0,471,509,501,493,478,491,512,461],
[525,514,530,0,495,507,512,504,519,490,488],
[512,508,492,506,0,465,504,541,575,498,518],
[568,518,500,494,536,0,518,539,537,533,520],
[497,506,508,489,497,483,0,513,540,485,493],
[477,481,523,497,460,462,488,0,490,461,489],
[438,473,510,482,426,464,461,511,0,487,482],
[490,526,489,511,503,468,516,540,514,0,502],
[508,490,540,513,483,481,508,512,519,499,0]])



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
result = np.append(np.array([11, 1001, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,484,504,487,494,465,504,464,474,493],
[518,0,496,529,512,488,485,486,490,497,508],
[517,505,0,484,492,491,492,512,485,483,508],
[497,472,517,0,486,508,484,500,493,484,501],
[514,489,509,515,0,486,487,499,489,488,500],
[507,513,510,493,515,0,507,504,496,507,522],
[536,516,509,517,514,494,0,519,498,498,516],
[497,515,489,501,502,497,482,0,500,494,486],
[537,511,516,508,512,505,503,501,0,488,503],
[527,504,518,517,513,494,503,507,513,0,508],
[508,493,493,500,501,479,485,515,498,493,0]])



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
result = np.append(np.array([11, 1001, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,475,526,518,501,478,521,442,505,510],
[533,0,491,528,507,508,518,482,499,506,493],
[526,510,0,528,511,498,491,515,515,512,513],
[475,473,473,0,480,471,495,491,481,484,502],
[483,494,490,521,0,491,491,506,478,480,503],
[500,493,503,530,510,0,489,483,497,523,512],
[523,483,510,506,510,512,0,491,523,486,505],
[480,519,486,510,495,518,510,0,472,495,497],
[559,502,486,520,523,504,478,529,0,551,500],
[496,495,489,517,521,478,515,506,450,0,520],
[491,508,488,499,498,489,496,504,501,481,0]])



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
result = np.append(np.array([11, 1001, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,522,499,492,531,520,517,518,543,495],
[508,0,522,501,485,524,534,532,517,532,537],
[479,479,0,518,511,520,519,492,510,510,510],
[502,500,483,0,495,510,501,489,513,527,510],
[509,516,490,506,0,500,515,539,517,518,522],
[470,477,481,491,501,0,527,497,499,504,505],
[481,467,482,500,486,474,0,487,496,489,506],
[484,469,509,512,462,504,514,0,499,511,491],
[483,484,491,488,484,502,505,502,0,514,523],
[458,469,491,474,483,497,512,490,487,0,499],
[506,464,491,491,479,496,495,510,478,502,0]])



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
result = np.append(np.array([11, 1001, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,480,492,471,486,503,506,503,506,512],
[495,0,490,506,481,512,499,493,505,507,504],
[521,511,0,547,509,503,533,507,541,478,523],
[509,495,454,0,494,510,494,483,501,476,504],
[530,520,492,507,0,516,542,499,522,515,521],
[515,489,498,491,485,0,493,484,493,503,512],
[498,502,468,507,459,508,0,473,513,507,504],
[495,508,494,518,502,517,528,0,519,513,540],
[498,496,460,500,479,508,488,482,0,500,500],
[495,494,523,525,486,498,494,488,501,0,517],
[489,497,478,497,480,489,497,461,501,484,0]])



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
result = np.append(np.array([11, 1001, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,490,488,488,492,500,486,500,470,489],
[538,0,509,551,498,547,549,521,536,501,501],
[511,492,0,463,471,487,496,484,476,482,488],
[513,450,538,0,484,485,540,526,497,532,522],
[513,503,530,517,0,496,490,480,502,507,499],
[509,454,514,516,505,0,502,529,488,500,463],
[501,452,505,461,511,499,0,475,522,508,476],
[515,480,517,475,521,472,526,0,520,497,487],
[501,465,525,504,499,513,479,481,0,473,533],
[531,500,519,469,494,501,493,504,528,0,502],
[512,500,513,479,502,538,525,514,468,499,0]])



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
result = np.append(np.array([11, 1001, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,514,516,515,509,507,509,529,479,506],
[494,0,566,515,550,534,510,536,569,511,516],
[487,435,0,486,532,481,448,417,521,489,507],
[485,486,515,0,502,473,479,470,544,465,484],
[486,451,469,499,0,494,502,479,536,461,513],
[492,467,520,528,507,0,471,511,521,476,490],
[494,491,553,522,499,530,0,488,538,533,516],
[492,465,584,531,522,490,513,0,555,503,482],
[472,432,480,457,465,480,463,446,0,422,488],
[522,490,512,536,540,525,468,498,579,0,499],
[495,485,494,517,488,511,485,519,513,502,0]])



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
result = np.append(np.array([11, 1001, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,507,472,476,484,489,435,504,482,493],
[508,0,517,502,526,482,462,512,505,489,472],
[494,484,0,507,494,481,525,494,517,486,487],
[529,499,494,0,554,503,486,492,534,497,541],
[525,475,507,447,0,460,486,460,492,491,494],
[517,519,520,498,541,0,514,486,545,492,536],
[512,539,476,515,515,487,0,508,520,503,530],
[566,489,507,509,541,515,493,0,505,503,495],
[497,496,484,467,509,456,481,496,0,499,453],
[519,512,515,504,510,509,498,498,502,0,517],
[508,529,514,460,507,465,471,506,548,484,0]])



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
result = np.append(np.array([11, 1001, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,463,480,484,446,494,463,456,477,504],
[481,0,456,451,486,466,476,444,468,466,479],
[538,545,0,508,499,471,535,512,492,514,491],
[521,550,493,0,516,479,551,488,493,506,505],
[517,515,502,485,0,497,513,480,485,496,489],
[555,535,530,522,504,0,542,463,507,502,510],
[507,525,466,450,488,459,0,473,468,449,471],
[538,557,489,513,521,538,528,0,489,516,520],
[545,533,509,508,516,494,533,512,0,499,521],
[524,535,487,495,505,499,552,485,502,0,487],
[497,522,510,496,512,491,530,481,480,514,0]])



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
result = np.append(np.array([11, 1001, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,532,579,477,432,425,447,473,377,342],
[531,0,672,585,574,481,598,604,591,432,489],
[469,329,0,464,474,460,471,502,477,342,426],
[422,416,537,0,499,385,353,441,445,438,338],
[524,427,527,502,0,511,533,462,619,377,466],
[569,520,541,616,490,0,347,600,606,403,544],
[576,403,530,648,468,654,0,640,464,542,603],
[554,397,499,560,539,401,361,0,549,457,563],
[528,410,524,556,382,395,537,452,0,414,463],
[624,569,659,563,624,598,459,544,587,0,490],
[659,512,575,663,535,457,398,438,538,511,0]])



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
result = np.append(np.array([11, 1001, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,511,485,519,536,490,526,527,578,530],
[473,0,495,461,456,511,451,467,484,537,513],
[490,506,0,506,500,522,500,489,516,549,533],
[516,540,495,0,530,504,480,479,484,531,519],
[482,545,501,471,0,532,481,496,504,566,524],
[465,490,479,497,469,0,439,455,474,516,485],
[511,550,501,521,520,562,0,492,549,554,538],
[475,534,512,522,505,546,509,0,520,543,503],
[474,517,485,517,497,527,452,481,0,543,513],
[423,464,452,470,435,485,447,458,458,0,484],
[471,488,468,482,477,516,463,498,488,517,0]])



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
result = np.append(np.array([11, 1001, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_11_1001.csv", index=False, header=False)